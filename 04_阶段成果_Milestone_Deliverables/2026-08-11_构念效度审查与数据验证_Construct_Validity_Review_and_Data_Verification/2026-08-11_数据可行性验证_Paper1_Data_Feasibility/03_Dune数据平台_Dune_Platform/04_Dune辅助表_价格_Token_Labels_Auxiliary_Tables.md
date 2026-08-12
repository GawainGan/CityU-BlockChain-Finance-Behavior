# Dune 辅助表：价格、Token、标签

**来源**：Dune 数据目录 + Dune 查询实例

---

## 一、prices.usd — Token 价格

**Dune 表名**：`prices.usd`  
**来源**：https://dune.com/docs/data-tables/decoded/ — Curated Datasets → Prices  
**覆盖**：70+ 链，包括 Ethereum

### 字段

| 字段 | 类型 | 含义 | 研究用途 |
|------|------|------|---------|
| `blockchain` | string | 区块链名称 | 过滤链（如 'ethereum'） |
| `contract_address` | string | Token 合约地址 | 关联资产 |
| `symbol` | string | Token 符号 | 识别资产 |
| `price` | double | USD 价格 | **重建 HF 的价格输入** |
| `minute` | timestamp | 时间戳（分钟级） | 时间维度 |
| `decimals` | integer | Token 精度 | 金额转换 |

### 查询示例

```sql
-- 获取 ETH 的每日价格
SELECT
    DATE_TRUNC('day', minute) AS day,
    contract_address,
    AVG(price) AS avg_price
FROM prices.usd
WHERE blockchain = 'ethereum'
  AND symbol = 'WETH'
  AND minute >= TIMESTAMP '2023-01-01'
GROUP BY 1, 2
ORDER BY day;
```

**验证来源**：Dune 查询 https://dune.com/queries/1955184 使用了 `prices.usd` 表和 `minute`, `contract_address`, `price` 字段

### 研究用途

```
价格数据在 HF 重建中的角色：

HF = Σ(collateral_amount_i × price_i × LT_i) / Σ(debt_amount_j × price_j)

prices.usd 提供 price_i 和 price_j
→ 确保抵押品和债务都以 USD 计价
→ 可以与 Chainlink 预言机价格交叉验证
```

### 关于 Chainlink 原始价格的说明

**当前状态**：`prices.usd` 的价格来源可能已经包含了 Chainlink 数据，但未明确确认。

**如果需要 Chainlink 原始预言机价格**：
1. 检查 Dune 上是否有 Chainlink decoded tables
2. 从 `ethereum.logs` 中解析 Chainlink 的 `AnswerUpdated` 事件
3. 或使用 `prices.usd` 作为合理替代

**风险等级**：低。对于历史 HF 重建，`prices.usd` 的价格质量已经足够。

---

## 二、tokens.erc20 — Token 元数据

**Dune 表名**：`tokens.erc20`  
**来源**：https://dune.com/docs/data-tables/decoded/ — Curated Datasets → Token Metadata

### 字段

| 字段 | 类型 | 含义 | 研究用途 |
|------|------|------|---------|
| `blockchain` | string | 区块链名称 | 过滤链 |
| `contract_address` | string | Token 合约地址 | 关联事件中的 reserve 地址 |
| `symbol` | string | Token 符号 | 识别资产（如 WETH, USDC） |
| `decimals` | integer | Token 精度 | **关键：将原始金额转换为可读金额** |

### 查询示例

```sql
-- 获取 Aave V3 中使用的资产的 decimals
SELECT contract_address, symbol, decimals
FROM tokens.erc20
WHERE blockchain = 'ethereum'
  AND contract_address IN (
    0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2,  -- WETH
    0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48,  -- USDC
    0xdAC17F958D2ee523a2206206994597C13D831ec7   -- USDT
  );
```

**验证来源**：Dune 查询 https://dune.com/queries/3255356 使用了 `tokens.erc20` 表和 `contract_address`, `symbol` 字段

### 研究用途

```
Token decimals 在数据转换中的角色：

链上事件中的 amount 是原始精度：
  amount = 500000000000000000 (18 decimals, = 0.5 ETH)
  amount = 5000000 (6 decimals, = 5 USDC)

使用 tokens.erc20 获取 decimals 后转换：
  readable_amount = amount / (10 ^ decimals)

  WETH (18 decimals): 500000000000000000 / 10^18 = 0.5 ETH
  USDC (6 decimals): 5000000 / 10^6 = 5 USDC
```

---

## 三、labels.labels — 地址标签

**Dune 表名**：`labels.labels`  
**来源**：https://dune.com/docs/data-tables/decoded/ — Curated Datasets → Labels  
**覆盖**：跨链

### 字段

| 字段 | 类型 | 含义 | 研究用途 |
|------|------|------|---------|
| `address` | string | 地址 | 识别 |
| `blockchain` | string | 区块链 | 过滤 |
| `label_type` | string | 标签类型 | 分类 |
| `label_name` | string | 标签名称 | 识别实体 |

### 研究用途

```
地址标签在主动/被动分类中的角色（问题 02 修正）：

Dune Labels 可以帮助识别：
  ✅ 交易所地址
  ✅ 协议合约地址
  ✅ DAO 地址
  ⚠️ 可能不覆盖小型 Router / Automation 合约

需要手动补充的合约地址列表：
  - Gnosis Safe 代理合约地址（Safe 有工厂合约，地址有规律但需要追踪）
  - 1inch Router 地址
  - Paraswap Router 地址
  - Uniswap Router 地址
  - DefiSaver 自动化合约地址
  - Gelato 自动化合约地址
  - 已知 liquidator 机器人地址

手动列表来源建议：
  - Etherscan 标签页面 https://etherscan.io/labels
  - Arkham Intelligence 标签
  - 社区维护的地址列表
```

---

## 四、其他可能有用的 Curated 表

| 表名 | 内容 | Paper 1 用途 |
|------|------|-------------|
| Dune Lending (curated) | 跨协议借贷数据 | 交叉验证（不应作为最终定义来源） |
| Gas & Fees | 交易费数据 | 分析 gas 成本对主动行为的影响 |
| Token Transfers | Token 转账数据 | 追踪借款资金去向（Paper 2 范围） |
| Stablecoins | 稳定币数据 | Paper 2 范围 |

**来源**：https://dune.com/docs/data-tables/decoded/ — Curated Datasets 表格
