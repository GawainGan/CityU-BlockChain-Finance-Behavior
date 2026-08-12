# Dune Raw Tables：交易、Trace、日志

**来源**：Dune 数据目录 + Dune Skills 文档

---

## 一、为什么需要 Raw 数据？

Decoded tables 提供了合约事件的解码数据，但有些研究需求需要回到原始数据：

```
需要 Raw 数据的场景：

1. 追踪交易发起者（from）
   → ethereum.transactions 表

2. 追踪内部调用链（识别 Safe / Router / Automation）
   → ethereum.traces 表

3. 解析 Chainlink 预言机原始价格事件
   → ethereum.logs 表

4. 获取 gas 价格
   → ethereum.transactions 表
```

---

## 二、ethereum.transactions

**Dune 表名**：`ethereum.transactions`  
**来源**：https://dune.com/docs/data-tables/decoded/ — Raw data 部分

### 关键字段

| 字段 | 类型 | 含义 | 研究用途 |
|------|------|------|---------|
| `hash` | string | 交易哈希 | 关联事件和 trace |
| `from` | string | 交易发起者 | **主动/被动分类的关键输入** |
| `to` | string | 交易目标 | 确认交易发送到哪个合约 |
| `block_time` | timestamp | 区块时间 | **分区列** |
| `block_number` | integer | 区块号 | 排序 |
| `gas_price` | string | Gas 价格 | 分析 gas 成本对行为的影响 |
| `gas_used` | string | 实际使用的 Gas | 交易成本 |
| `nonce` | integer | 交易序号 | 分析地址行为模式 |
| `value` | string | ETH 转账金额 | 原始精度（/10^18） |
| `success` | boolean | 交易是否成功 | 过滤失败交易 |

### 查询示例

```sql
-- 获取某交易的基本信息
SELECT hash, "from", "to", block_time, gas_price, gas_used, success
FROM ethereum.transactions
WHERE hash = 0x...  -- 交易哈希
  AND block_time >= TIMESTAMP '2023-01-27';
```

### 研究用途

```
ethereum.transactions 在主动/被动分类中的角色：

对于每个协议事件（如 Supply）：
  1. 从 decoded table 获取 evt_tx_hash
  2. 用 evt_tx_hash 关联 ethereum.transactions
  3. 获取 from（交易发起者 = msg.sender）
  4. 对比 from 和事件中的 user / onBehalfOf
  5. 如果 from ≠ user 但 from 是已知 Safe/Router 地址 → 仍为主动
```

---

## 三、ethereum.traces

**Dune 表名**：`ethereum.traces`  
**来源**：https://dune.com/docs/data-tables/decoded/ — Raw data 包含 trace 数据

### 关键字段

| 字段 | 类型 | 含义 | 研究用途 |
|------|------|------|---------|
| `tx_hash` | string | 交易哈希 | 关联交易 |
| `from` | string | 内部调用发起者 | **追踪调用链** |
| `to` | string | 内部调用目标 | 识别最终调用合约 |
| `value` | string | 内部转账金额 | 资金流追踪 |
| `input` | string | 调用数据 | 识别调用的函数 |
| `output` | string | 返回数据 | 调用结果 |
| `trace_type` | string | Trace 类型 | call, create, suicide 等 |
| `trace_address` | string | Trace 地址 | 调用深度和顺序 |
| `block_time` | timestamp | 区块时间 | **分区列** |

### 研究用途

```
ethereum.traces 在主动/被动分类中的角色：

场景：用户通过 Gnosis Safe → Router → Aave Pool 操作

交易结构：
  ethereum.transactions.from = 用户 EOA
  → 调用 Gnosis Safe 合约
    → Safe 内部调用 Router 合约
      → Router 内部调用 Aave Pool 合约
        → Pool 发出 Supply 事件

Trace 数据可以追踪完整调用链：
  Trace 1: EOA → Safe (from=EOA, to=Safe)
  Trace 2: Safe → Router (from=Safe, to=Router)
  Trace 3: Router → Pool (from=Router, to=Pool)

通过 trace 数据，即使 from（msg.sender）是 Router，
我们也能追溯实际发起者是 EOA（通过 Safe）。
```

---

## 四、ethereum.logs

**Dune 表名**：`ethereum.logs`  
**来源**：https://dune.com/docs/data-tables/decoded/ — Raw data

### 关键字段

| 字段 | 类型 | 含义 | 研究用途 |
|------|------|------|---------|
| `tx_hash` | string | 交易哈希 | 关联交易 |
| `contract_address` | string | 发出日志的合约 | 识别事件来源 |
| `topic0` | string | 事件签名哈希 | 识别事件类型 |
| `topic1` - `topic3` | string | indexed 参数 | 事件参数 |
| `data` | string | 非 indexed 参数 | 事件参数 |
| `block_time` | timestamp | 区块时间 | **分区列** |

### 研究用途

```
ethereum.logs 的补充用途：

1. Chainlink 价格事件解析
   Chainlink 的 AnswerUpdated 事件的 topic0 = 0x0559884fd1...
   可以从 ethereum.logs 中过滤这个 topic0 来获取 Chainlink 原始价格

2. 未被 Dune 解码的合约事件
   如果某个合约尚未被 Dune 解码（没有 decoded table），
   可以从 ethereum.logs 中手动解析事件

3. 交叉验证
   可以用 raw logs 交叉验证 decoded tables 的完整性
```

### Chainlink AnswerUpdated 事件

```solidity
// Chainlink Price Feed 的更新事件
event AnswerUpdated(
    int256 indexed current,     // 新价格
    uint256 indexed roundId,    // 轮次 ID
    uint256 updatedAt           // 更新时间
);
```

**topic0**: `0x0559884fd1a34349a7f1f0fefd5c33c03c0a4c0a4d9f7c8b3b3b7e6b7a7a7a7a`

**查询示例**：
```sql
-- 从 raw logs 中获取 Chainlink ETH/USD 价格更新
SELECT
    evt_block_time,
    contract_address,
    topic1,  -- current price (indexed)
    topic2,  -- roundId (indexed)
    data     -- updatedAt (non-indexed)
FROM ethereum.logs
WHERE contract_address = 0x5f4eC3Df9cbd43714FE2740f5E3616155c5b8419  -- Chainlink ETH/USD
  AND topic0 = 0x0559884fd1a34349a7f1f1fefd5c33c03c0a4c0a4d9f7c8b3b3b7e6b7a7a7a7a
  AND evt_block_time >= TIMESTAMP '2023-01-27'
ORDER BY evt_block_time;
```

**注意**：Chainlink ETH/USD Price Feed 地址：`0x5f4eC3Df9cbd43714FE2740f5E3616155c5b8419`  
**来源**：Chainlink 文档 https://docs.chain.link/data-feeds/price-feeds/addresses

---

## 五、Raw 数据查询注意事项

### 5.1 分区列过滤

```sql
-- ✅ 正确：过滤分区列
SELECT * FROM ethereum.transactions
WHERE block_time >= TIMESTAMP '2024-01-01'
  AND block_time < TIMESTAMP '2025-01-01';

-- ❌ 错误：不过滤分区列（极慢）
SELECT * FROM ethereum.transactions
WHERE "from" = 0x...;
```

**来源**：https://github.com/duneanalytics/skills/blob/HEAD/skills/dune/references/dunesql-cheatsheet.md

### 5.2 大地址查询优化

```sql
-- ✅ 正确：同时过滤分区列和地址
SELECT * FROM ethereum.transactions
WHERE "from" = 0x...
  AND block_time >= TIMESTAMP '2024-01-01'
  AND block_time < TIMESTAMP '2025-01-01';

-- ❌ 错误：只过滤地址不过滤时间（扫描全表）
SELECT * FROM ethereum.transactions
WHERE "from" = 0x...;
```

### 5.3 Trace 数据查询

```sql
-- 获取某交易的完整调用链
SELECT
    trace_address,
    "from",
    "to",
    trace_type,
    input
FROM ethereum.traces
WHERE tx_hash = 0x...
  AND block_time >= TIMESTAMP '2024-01-01'  -- 需要知道大致时间范围
ORDER BY trace_address;
```
