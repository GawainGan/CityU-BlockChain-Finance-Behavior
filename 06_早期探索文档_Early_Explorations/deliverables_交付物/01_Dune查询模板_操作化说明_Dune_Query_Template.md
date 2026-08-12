# V4 Dune 查询模板与操作化说明

**版本**：V4-1 · Dune PoC
**日期**：2026-06-19
**目的**：验证从 Dune Analytics 提取 Aave 借贷事件时能否区分"主动补救"与"被动清算"，以及健康因子时间序列的可获取性

---

## 一、Dune 数据结构确认

### 1.1 核心表

| Dune 表名 | 内容 | 关键字段 | 与 RQ 的关系 |
|-----------|------|---------|------------|
| `lending.borrow` | 借款/还款/清算事件 | `borrower`, `amount_usd`, `evt_block_time`, `transaction_type` | RQ1 行为序列；RQ2 因变量 |
| `lending.supply` | 存款/取款事件 | `depositor`, `amount_usd`, `evt_block_time` | RQ1 主动补救（加抵押） |
| `lending.collateral` | 抵押品启用/禁用 | `user`, `reserve`, `evt_block_time` | RQ1 抵押品类型切换（BDM 构念关键维度） |

**分区键**（查询时必须指定以提高性能）：
- `blockchain` = `'ethereum'`
- `project` = `'aave_v2'` 或 `'aave_v3'`
- `block_month` = `'2025-01-01'` 等

### 1.2 Aave V2 合约事件（原始解码）

| 合约事件 | Solidity 参数 | 能否区分主动/被动 |
|---------|-------------|----------------|
| `Borrow(address reserve, address user, uint256 amount, ...)` | `user` = 借款人 | 主动借款 |
| `Repay(address reserve, address user, address repayer, uint256 amount, ...)` | `repayer` 可 ≠ `user` | ✅ **关键**：`repayer != user` → 可能是清算人代还 |
| `LiquidationCall(address collateralAsset, address debtAsset, address user, uint256 debtToCover, address liquidator, ...)` | `liquidator` ≠ `user` | ✅ **直接区分**：`liquidator` 字段明确标识清算人 |
| `Deposit(address reserve, address user, uint256 amount, ...)` | `user` = 存款人 | 主动加抵押 |
| `Withdraw(address reserve, address user, address to, uint256 amount, ...)` | `user` = 取款人 | 主动减抵押 |

### 1.3 健康因子获取

Aave V2 的 `getUserAccountData` 视图函数返回 `healthFactor`，但这是**快照值**，不会自动产生事件。

**获取 HF 时间序列的两种方案**：

- **方案 A（Dune 内置）**：使用 `lending.borrow` 表中部分已计算的健康因子字段（如 Dune 的 `health_factor` 列，如果存在）
- **方案 B（自计算）**：对每个用户在每个区块高度，根据其持仓（抵押品价值 / 借款价值 + 清算阈值）重新计算 HF

```sql
-- 方案 B 的核心逻辑（伪代码）
-- HF = (总抵押品价值 × 清算阈值) / 总借款价值
-- 当 HF < 1.0 时触发清算
-- 需要价格预言机数据（Chainlink feed）来获取历史资产价格
```

**方案 B 所需辅助表**：
- `prices.usd`：Dune 提供的历史价格表（按小时/天）
- Aave `ReserveData` 事件：获取 LTV、清算阈值等参数

---

## 二、PoC 查询模板

### 2.1 查询 1：提取某月借贷用户样本及其关键事件

```sql
-- 目的：获取 Aave V2 (Ethereum) 2025年1月所有借贷用户的交易级事件
-- 产出：每个用户在每个时间点的事件类型、金额、交易发起者

WITH user_events AS (
  SELECT
    borrower AS user_address,
    'borrow' AS event_type,
    amount_usd,
    evt_block_time,
    evt_tx_hash,
    NULL AS counterparty  -- 借款事件无对手方
  FROM lending.borrow
  WHERE blockchain = 'ethereum'
    AND project = 'aave_v2'
    AND block_month = '2025-01-01'
    AND transaction_type = 'borrow'

  UNION ALL

  SELECT
    borrower AS user_address,
    'repay' AS event_type,
    amount_usd,
    evt_block_time,
    evt_tx_hash,
    NULL AS counterparty  -- 需要 JOIN 原始事件获取 repayer
  FROM lending.borrow
  WHERE blockchain = 'ethereum'
    AND project = 'aave_v2'
    AND block_month = '2025-01-01'
    AND transaction_type = 'repay'

  UNION ALL

  SELECT
    user AS user_address,
    'liquidation' AS event_type,
    amount_usd,
    evt_block_time,
    evt_tx_hash,
    liquidator AS counterparty  -- 清算人地址
  FROM lending.borrow
  WHERE blockchain = 'ethereum'
    AND project = 'aave_v2'
    AND block_month = '2025-01-01'
    AND transaction_type = 'liquidation'
)

SELECT
  user_address,
  event_type,
  amount_usd,
  evt_block_time,
  evt_tx_hash,
  counterparty
FROM user_events
ORDER BY user_address, evt_block_time
LIMIT 5000;
```

### 2.2 查询 2：区分主动补救 vs 被动清算（核心操作化）

```sql
-- 目的：对每个用户，判断其"清算阈值附近的操作"是主动还是被动
-- 关键字段：tx.from（交易发起者）

-- 注意：Dune 的 lending 表可能不包含 tx.from
-- 如果 lending 表缺少此字段，需要 JOIN ethereum.transactions 表

WITH liquidation_events AS (
  SELECT
    l.user AS borrower,
    l.liquidator,
    l.amount_usd AS liquidated_amount,
    l.evt_block_time,
    l.evt_tx_hash,
    t."from" AS tx_sender  -- 交易的实际发起者
  FROM lending.borrow l
  LEFT JOIN ethereum.transactions t
    ON l.evt_tx_hash = t.hash
  WHERE l.blockchain = 'ethereum'
    AND l.project = 'aave_v2'
    AND l.block_month BETWEEN '2024-01-01' AND '2025-12-01'
    AND l.transaction_type = 'liquidation'
),

user_remediation AS (
  -- 主动补救：清算后 24h 内借款人自己发起的加抵押/还款
  SELECT
    l.borrower,
    l.evt_block_time AS liquidation_time,
    s.evt_block_time AS remediation_time,
    EXTRACT(EPOCH FROM (s.evt_block_time - l.evt_block_time)) / 3600 AS hours_since_liquidation,
    'supply' AS remediation_type,
    s.amount_usd
  FROM liquidation_events l
  JOIN lending.supply s
    ON l.borrower = s.depositor
    AND s.evt_block_time > l.evt_block_time
    AND s.evt_block_time < l.evt_block_time + INTERVAL '24 hours'
  WHERE s.blockchain = 'ethereum'
    AND s.project = 'aave_v2'

  UNION ALL

  SELECT
    l.borrower,
    l.evt_block_time AS liquidation_time,
    r.evt_block_time AS remediation_time,
    EXTRACT(EPOCH FROM (r.evt_block_time - l.evt_block_time)) / 3600 AS hours_since_liquidation,
    'repay' AS remediation_type,
    r.amount_usd
  FROM liquidation_events l
  JOIN lending.borrow r
    ON l.borrower = r.borrower
    AND r.transaction_type = 'repay'
    AND r.evt_block_time > l.evt_block_time
    AND r.evt_block_time < l.evt_block_time + INTERVAL '24 hours'
  WHERE r.blockchain = 'ethereum'
    AND r.project = 'aave_v2'
)

-- 分类统计
SELECT
  borrower,
  COUNT(DISTINCT liquidation_time) AS n_liquidations,
  COUNT(DISTINCT remediation_time) AS n_remediations_within_24h,
  AVG(hours_since_liquidation) AS avg_hours_to_remediate,
  SUM(CASE WHEN remediation_type = 'supply' THEN 1 ELSE 0 END) AS n_supply_remediations,
  SUM(CASE WHEN remediation_type = 'repay' THEN 1 ELSE 0 END) AS n_repay_remediations
FROM user_remediation
GROUP BY borrower
ORDER BY n_liquidations DESC
LIMIT 100;
```

### 2.3 查询 3：清算前行为（前景理论检验的输入数据）

```sql
-- 目的：提取清算前 7 天内借款人的所有操作，按时间排列
-- 用于检验：HF 逼近 1.0 时，借款人的操作频率和类型是否发生变化

WITH target_users AS (
  -- 被清算过的用户
  SELECT DISTINCT
    user AS borrower,
    evt_block_time AS liquidation_time
  FROM lending.borrow
  WHERE blockchain = 'ethereum'
    AND project = 'aave_v2'
    AND block_month = '2025-01-01'
    AND transaction_type = 'liquidation'
),

pre_liquidation_actions AS (
  -- 清算前 7 天内的所有操作
  SELECT
    t.borrower,
    'borrow' AS action_type,
    b.amount_usd,
    b.evt_block_time,
    t.liquidation_time,
    EXTRACT(EPOCH FROM (t.liquidation_time - b.evt_block_time)) / 3600 AS hours_before_liquidation
  FROM target_users t
  JOIN lending.borrow b
    ON t.borrower = b.borrower
    AND b.evt_block_time >= t.liquidation_time - INTERVAL '7 days'
    AND b.evt_block_time < t.liquidation_time
    AND b.transaction_type IN ('borrow', 'repay')
  WHERE b.blockchain = 'ethereum' AND b.project = 'aave_v2'

  UNION ALL

  SELECT
    t.borrower,
    'supply' AS action_type,
    s.amount_usd,
    s.evt_block_time,
    t.liquidation_time,
    EXTRACT(EPOCH FROM (t.liquidation_time - s.evt_block_time)) / 3600 AS hours_before_liquidation
  FROM target_users t
  JOIN lending.supply s
    ON t.borrower = s.depositor
    AND s.evt_block_time >= t.liquidation_time - INTERVAL '7 days'
    AND s.evt_block_time < t.liquidation_time
  WHERE s.blockchain = 'ethereum' AND s.project = 'aave_v2'
)

SELECT *
FROM pre_liquidation_actions
ORDER BY borrower, hours_before_liquidation DESC
LIMIT 10000;
```

---

## 三、操作化定义：主动 vs 被动

### 3.1 分类规则

| 分类 | 定义 | 链上判定标准 | 与前景理论的关系 |
|------|------|-------------|---------------|
| **主动补救（Active Remediation）** | 借款人在 HF 逼近 1.0 时，**自己发起**的加抵押/还款交易 | `tx.from == borrower_address` AND 事件类型 IN (`supply`, `repay`) | 前景理论预测的损失厌恶行为——面对损失威胁时的主动防御 |
| **被动清算（Passive Liquidation）** | 清算人触发的强制平仓，借款人是被动承受方 | `tx.from == liquidator_address` AND 事件类型 = `liquidation` | 非行为主体——用于标记参考点被跨越的时刻 |
| **清算后修复（Post-Liquidation Recovery）** | 被清算后借款人采取的行动（24h 窗口内） | `tx.from == borrower_address` AND `evt_block_time - liquidation_time < 24h` | 与清算前预防行动必须分开统计；属于事后行为，不属于前景理论的参考点效应检验 |
| **主动增险（Active Risk-Taking）** | 借款人在 HF 低于安全阈值时**反而增借** | `tx.from == borrower_address` AND 事件类型 = `borrow` AND `current_HF < 1.5` | 前景理论预测的"在损失域中冒险"——递减敏感性 + 风险偏好翻转 |
| **抵押品切换（Collateral Switching）** | 借款人在逼近清算时从稳定币抵押切换到波动资产抵押 | 禁用稳定币抵押 + 启用波动资产抵押，时间窗口 < 24h | **DeFi 特有维度**：传统金融无对应物；属于 BDM 构念的核心新颖性 |

### 3.2 关键判定字段

```
必须字段：
  ├── evt_tx_hash        → JOIN ethereum.transactions 获取 tx.from
  ├── tx.from            → 判定交易发起者身份
  ├── borrower / user    → 借款人地址
  ├── liquidator         → 清算人地址（仅 LiquidationCall 事件有）
  ├── transaction_type   → borrow / repay / liquidation
  └── evt_block_time     → 时间窗口判定

需要自计算的字段：
  ├── health_factor      → 需要从持仓数据 + 价格数据自计算
  ├── collateral_type    → 需要识别资产是稳定币还是波动资产
  └── action_category    → 基于上述规则的分类结果
```

### 3.3 边缘情况处理

| 边缘情况 | 判定规则 | 理由 |
|---------|---------|------|
| 闪电贷清算（Flash Loan Liquidation） | `tx.from` 是已知的闪电贷合约地址（如 Aave V2 FlashLoan） | 闪电贷清算者仍是清算人，不是借款人；但清算速度极快，借款人无时间补救 |
| 部分清算（Partial Liquidation） | 同一借款人在同一区块内被多次清算 | 合并为一次清算事件，总金额加总 |
| 自清算（Self-Liquidation） | `tx.from == borrower_address` 但交易触发了 LiquidationCall | 极罕见；借款人选择触发清算而非手动还款（可能是 gas 优化策略）；归入"主动决策" |
| MEV 机器人清算 | `tx.from` 已知的 MEV 机器人地址 | 归入被动清算；但记录清算速度（gas price 竞争强度），作为控制变量 |
| 多协议交叉操作 | 用户在 Compound 有仓位同时 Aave 也有仓位 | 当前 PoC 仅关注 Aave 内操作；后续需扩展 |

### 3.4 闪电贷清算的特别说明

闪电贷清算是 DeFi 特有的清算方式：清算人在一笔交易内同时完成借款→清算→还款，不需要自有资本。这意味着：

1. **清算速度**：闪电贷清算使 HF<1 的窗口可能只有几秒，而非几分钟
2. **补救机会**：如果闪电贷清算占主导，借款人几乎不可能在清算前进行"主动补救"
3. **对 RQ1 的影响**：如果闪电贷清算占 90%+，则"逼近清算阈值时借款人的主动行为"样本极少，前景理论检验效力不足
4. **必须量化**：在 PoC 中统计闪电贷清算占比

```sql
-- 闪电贷清算占比查询（粗估）
WITH liquidations AS (
  SELECT
    evt_tx_hash,
    liquidator,
    COUNT(*) OVER (PARTITION BY evt_tx_hash) AS events_in_tx
  FROM lending.borrow
  WHERE blockchain = 'ethereum'
    AND project = 'aave_v2'
    AND transaction_type = 'liquidation'
    AND block_month = '2025-01-01'
),
flash_loan_flag AS (
  SELECT
    l.*,
    CASE WHEN f.evt_tx_hash IS NOT NULL THEN 1 ELSE 0 END AS is_flash_loan
  FROM liquidations l
  LEFT JOIN lending.flashloans f
    ON l.evt_tx_hash = f.evt_tx_hash
)
SELECT
  COUNT(*) AS total_liquidations,
  SUM(is_flash_loan) AS flash_loan_liquidations,
  SUM(is_flash_loan)::FLOAT / COUNT(*)::FLOAT AS flash_loan_pct
FROM flash_loan_flag;
```

---

## 四、PoC 验证清单

在 Dune 执行上述查询后，需回答以下问题：

- [ ] **Q1**：`lending.borrow` 表中 `transaction_type` 字段是否包含 `'liquidation'` 值？如果不能，需要使用哪个替代表/字段？
- [ ] **Q2**：JOIN `ethereum.transactions` 获取 `tx.from` 是否可行？查询性能是否可接受（<5min）？
- [ ] **Q3**：Dune 是否提供 `health_factor` 列？如果不提供，自计算 HF 的复杂度和可行性如何？
- [ ] **Q4**：`lending.flashloans` 表是否覆盖 Aave V2 的闪电贷事件？
- [ ] **Q5**：`LiquidationCall` 事件的 `liquidator` 字段在 Dune 解码中是否可靠可用？
- [ ] **Q6**：一个月的数据量级是多少？全量（2020-2025）查询是否需要分批？
- [ ] **Q7**：清算前行为样本量（有多少借款人在被清算前 7 天内有操作）是否足够统计检验？

### 预期样本量估算

基于 Gadzinski & Liuzzi (2025) 的 25,798 笔 Aave 清算事件（Mar 2022–Dec 2024，约 34 个月）：
- 月均清算事件 ≈ 760 笔
- 假设 30% 的借款人在清算前 7 天内有操作 → 月均约 230 个有效行为样本
- 2020-2025 共 72 个月 → 总有效样本约 16,500+
- 足以支撑 RQ1 的 RDD 和 RQ2 的预测模型

---

## 五、备选数据验证路径

如果 Dune 的 `lending` 标准化表不满足需求：

1. **直接查询 Aave V2 合约事件**（Dune 的 `aave_v2."LendingPool_evt_LiquidationCall"` 表）
2. **Flipside Crypto**：提供类似的链上数据仓库，可交叉验证
3. **The Graph Subgraph**：Aave 官方 subgraph，GraphQL API 直接查询
4. **自建索引**：用 ethers.js / web3.py 从以太坊节点直接索引事件（最灵活但最耗时）

### Aave V2 合约地址（Ethereum 主网）
- LendingPool: `0x7d2768dE32b0b80b7a3454c06BdAc94A69DDc7A9`
- LendingPoolV2 Proxy: `0xB53C1a33016B2DC2fF3653530bfF1848a515c8c5`
