# Dune 平台总览

**来源**：https://dune.com/docs/  
**日期**：2026-08-11

---

## 一、Dune 是什么？

Dune Analytics 是一个区块链数据分析平台，提供 SQL 查询接口访问链上数据。简单来说：

```
你写 SQL 查询 → Dune 在其数据库中执行 → 返回结果

你不需要：
  ❌ 运行自己的以太坊节点
  ❌ 下载区块链数据
  ❌ 解码原始字节码

你只需要：
  ✅ 写 SQL 查询
  ✅ 知道要查哪张表
```

---

## 二、三层数据架构

Dune 的数据分为三层，从底层到上层：

```
Layer 1: Raw Data（原始数据）
  │   直接从区块链节点索引的数据
  │   包括：区块、交易、日志、Trace
  │   特点：完整但难以直接使用（原始字节码）
  ↓
Layer 2: Decoded Data（解码数据）
  │   使用合约 ABI 将原始字节码解码为人类可读的表格
  │   包括：合约事件（events）和函数调用（calls）
  │   特点：按合约/项目组织，字段名清晰
  ↓
Layer 3: Curated Data（精选数据）
  │   Dune 数据团队维护的清洗后数据表
  │   包括：DEX 交易、价格、Token 元数据、标签等
  │   特点：跨链统一 schema，方便快速查询
```

### 各层对比

| 维度 | Raw | Decoded | Curated |
|------|-----|---------|---------|
| 数据形式 | 原始字节码 | 结构化表格 | 清洗后表格 |
| 使用难度 | 高 | 中 | 低 |
| 覆盖范围 | 全部链上数据 | 已解码的合约 | 常用数据类型 |
| 表名前缀 | `ethereum.*` | `项目_链.*` | `prices.*`, `tokens.*` 等 |
| Paper 1 使用？ | ✅（Trace） | ✅（核心） | ✅（价格、Token） |

**来源**：https://dune.com/docs/data-tables/decoded/

---

## 三、Paper 1 使用的数据层级

### 3.1 Decoded Data（核心使用）

这是 Paper 1 最主要的数据来源。Aave V3 的所有协议事件都通过 decoded tables 获取。

```
Aave V3 Decoded Tables 命名规则：

aave_v3_ethereum.Pool_evt_<EventName>
         ↑              ↑      ↑
         项目名           合约名  事件名

示例：
aave_v3_ethereum.Pool_evt_Supply
aave_v3_ethereum.Pool_evt_Borrow
aave_v3_ethereum.Pool_evt_LiquidationCall
aave_v3_ethereum.PoolConfigurator_evt_CollateralConfigurationChanged
```

**所有 decoded event 表的通用字段**：

| 字段 | 类型 | 含义 | 说明 |
|------|------|------|------|
| `evt_block_time` | timestamp | 区块时间戳 | **分区列，查询必须过滤** |
| `evt_block_number` | integer | 区块号 | 用于排序和定位 |
| `evt_tx_hash` | string | 交易哈希 | 关联交易和 trace |
| `evt_index` | integer | 事件在交易中的索引 | 同一交易中多个事件的顺序 |
| `contract_address` | string | 发出事件的合约地址 | 确认事件来源 |

**来源**：https://github.com/duneanalytics/skills/blob/HEAD/skills/dune/references/dataset-discovery.md

### 3.2 Curated Data（辅助使用）

| 表名 | 内容 | Paper 1 用途 |
|------|------|-------------|
| `prices.usd` | Token USD 价格（分钟级） | 重建历史 HF 的价格输入 |
| `tokens.erc20` | Token 元数据（decimals, symbol） | 将原始金额转换为可读金额 |
| `labels.labels` | 地址标签 | 识别已知合约（Safe, Router 等） |

**来源**：https://dune.com/docs/data-tables/decoded/ （数据目录页面）

### 3.3 Raw Data（补充使用）

| 表名 | 内容 | Paper 1 用途 |
|------|------|-------------|
| `ethereum.transactions` | 交易数据（from, to, gas 等） | 获取交易发起者 |
| `ethereum.traces` | 内部调用链 | 识别 Safe/Router/Automation 调用链 |
| `ethereum.logs` | 原始事件日志 | 补充查询（如 Chainlink 价格） |

**来源**：https://dune.com/docs/data-tables/decoded/ （Raw data 部分）

---

## 四、Ethereum 数据覆盖确认

从 Dune 数据目录页面确认，Ethereum 的数据覆盖：

| 数据类型 | 可用 | 来源 |
|---------|------|------|
| Raw（区块/交易/日志/Trace） | ✅ | Dune 数据目录 |
| Decoded（合约事件/调用） | ✅ | Dune 数据目录 |
| DEX Trades（精选） | ✅ | Dune 数据目录 |
| Token Transfers（精选） | ✅ | Dune 数据目录 |
| Balances（精选） | ✅ | Dune 数据目录 |
| Prices（精选） | ✅ | Dune 数据目录 |
| CEX Flows（精选） | ✅ | Dune 数据目录 |
| NFT Trades（精选） | ✅ | Dune 数据目录 |
| Labels（精选） | ✅ | Dune 数据目录 |
| Bridges（精选） | ✅ | Dune 数据目录 |
| Gas & Fees（精选） | ✅ | Dune 数据目录 |
| Stablecoins（精选） | ✅ | Dune 数据目录 |
| Lending（精选） | ✅ | Dune 数据目录 |

**来源**：https://dune.com/docs/data-tables/decoded/ — Ethereum 行全部为 ✅

---

## 五、Dune Curated Lending 数据集

Dune 提供了一个精选的 Lending 数据集，覆盖 15 个 EVM 链：

> "Lending — Supply, borrow, flash loans, and liquidations across lending protocols — 15 EVM chains"

**来源**：https://dune.com/docs/data-tables/decoded/ — Curated Datasets 表格中 Lending 行

**重要提醒**：
- 这个 curated lending 数据集可以作为快速查询和交叉验证使用
- **但不应该作为最终定义来源**（参见六层矩阵技术文档中的原则）
- 如果研究问题依赖 onBehalfOf、collateral enablement 状态、historical LT 等细节，应优先从 decoded tables 自己重建

---

## 六、查询性能注意事项

### 6.1 分区列

所有 Dune 表都有分区列，查询时必须过滤分区列以保证性能：

| 表类型 | 分区列 |
|--------|--------|
| `ethereum.transactions` | `block_time`, `block_date` |
| Decoded event 表 (`evt_*`) | `evt_block_time` |
| Decoded call 表 (`call_*`) | `call_block_time` |
| `prices.usd` | `minute` |

**来源**：https://github.com/duneanalytics/skills/blob/HEAD/skills/dune/references/dunesql-cheatsheet.md

### 6.2 查询示例

```sql
-- ✅ 正确：过滤分区列
SELECT *
FROM aave_v3_ethereum.Pool_evt_Supply
WHERE evt_block_time >= TIMESTAMP '2023-01-27'
  AND evt_block_time < TIMESTAMP '2024-01-01'
LIMIT 100;

-- ❌ 错误：不过滤分区列（扫描全表，极慢）
SELECT *
FROM aave_v3_ethereum.Pool_evt_Supply
LIMIT 100;
```

**来源**：https://github.com/duneanalytics/skills/blob/HEAD/skills/dune/references/dunesql-cheatsheet.md

---

## 七、Dune 访问方式

| 方式 | 说明 | 适合场景 |
|------|------|---------|
| Dune Web App | 网页版 SQL 编辑器 | 交互式查询、可视化 |
| Dune API | 编程式访问查询结果 | 自动化数据获取 |
| Datashare | 直接在 Snowflake/BigQuery/Databricks 中访问 | 大规模数据分析 |

**来源**：https://dune.com/docs/data-tables/decoded/

---

## 八、数据质量保证

Dune 官方声明：

> "Comprehensive Chain Histories: Full access to blockchain data histories without gaps, ensuring source integrity."
> 
> "Accurate and Validated Data: Commitment to accuracy, with validated consistency and uniqueness for all transactions and events."
> 
> "Raw data typically arrives within minutes of on-chain finality. Curated datasets refresh hourly."

**来源**：https://dune.com/docs/data-tables/decoded/ — Data Trust & Freshness 部分
