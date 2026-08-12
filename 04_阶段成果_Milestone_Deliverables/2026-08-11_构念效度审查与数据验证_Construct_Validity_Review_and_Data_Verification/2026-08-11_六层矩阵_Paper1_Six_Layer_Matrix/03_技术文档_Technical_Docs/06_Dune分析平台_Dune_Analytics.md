# Dune Analytics 技术文档

**官方文档**：https://dune.com/docs/  
**用途**：Paper 1 主要数据查询平台

---

## 1. 概述

Dune Analytics 是一个社区维护的区块链数据平台，提供 SQL 查询接口访问 decoded event logs 和 state data。非常适合 DeFi 协议事件重建。

---

## 2. 数据层级

| 层级 | 含义 | 适用场景 |
|------|------|---------|
| **Raw data** | 原始区块/交易数据 | 底层验证 |
| **Decoded data** | 解码后的 contract events 和 function calls | 协议事件提取（主要使用） |
| **Spells / Curated** | 社区维护的清洗后数据表 | 快速查询（但不应作为最终定义来源） |

### 关键原则

> **Dune 很有价值，但不应该成为最终定义来源。**

如果研究问题依赖：
- onBehalfOf 参数
- Collateral enablement 状态
- Historical liquidation threshold
- Contract upgrade
- Delegate call
- State transitions

就应优先从 **contracts + logs + state** 自己重建。

---

## 3. Aave V3 在 Dune 上的数据

### Decoded Tables

| 表名 | 内容 |
|------|------|
| `aave_v3_ethereum.LendingPool_evt_Supply` | Supply 事件 |
| `aave_v3_ethereum.LendingPool_evt_Withdraw` | Withdraw 事件 |
| `aave_v3_ethereum.LendingPool_evt_Borrow` | Borrow 事件 |
| `aave_v3_ethereum.LendingPool_evt_Repay` | Repay 事件 |
| `aave_v3_ethereum.LendingPool_evt_LiquidationCall` | 清算事件 |
| `aave_v3_ethereum.LendingPool_evt_SetUserUseReserveAsCollateral` | Collateral enable/disable |

### 注意事项

- Dune 的 decoded table 名称可能随版本更新变化
- 建议在查询前检查 Dune Spellbook 中的最新表名
- 某些历史参数可能需要从 governance 事件或合约存储中重建

---

## 4. Compound III 在 Dune 上的数据

| 表名 | 内容 |
|------|------|
| `compound_v3_ethereum.Comet_evt_Supply` | Supply (还款) |
| `compound_v3_ethereum.Comet_evt_Withdraw` | Withdraw (借款) |
| `compound_v3_ethereum.Comet_evt_AbsorbCollateral` | 清算 |

---

## 5. 推荐数据栈

```text
Layer 1: Raw / Decoded Data (Dune)
    ↓
Layer 2: Researcher-built Position State
    - 重建每个地址的仓位历史
    - 跟踪 collateral-enabled 状态
    - 按协议真实参数重建 HF
    ↓
Layer 3: Analytical Panel
    - borrower-position-day / borrower-position-month
    - 行为过程变量
    ↓
Layer 4: Validation
    - 与 Dune curated tables 交叉验证
    - 与已知事件人工核验
```

---

## 6. 文档链接

| 内容 | 链接 |
|------|------|
| Dune 官方文档 | https://dune.com/docs/ |
| Dune Query Language | https://dune.com/docs/query/ |
| Dune Spellbook | https://dune.com/docs/spellbook/ |
| Decoded Data | https://dune.com/docs/data-tables/decoded/ |
| Aave V3 on Dune | https://dune.com/dune/integrated-aave-v3 |
