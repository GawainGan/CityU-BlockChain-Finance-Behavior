# 10. Liquidation Eligibility / 清算资格

**六层矩阵详细文件**  
**相关技术文档**：`03_技术文档/01_Aave_V3.md`, `02_Compound_III.md`  
**相关文献**：`04_文献/03_DeFi_Lending/`

---

## Layer 1 — Definition

> **Liquidation Eligibility 是仓位已满足协议清算条件的状态。此时该仓位在协议层面可以被第三方清算，但尚未被实际清算。它是一个 mechanical position state，不是 borrower credit state。**

关键区分：

```text
Liquidation Eligibility = position entered a mechanically liquidatable state
≠
Realized Liquidation = liquidation actually occurred
≠
Credit Default = borrower failed to repay
```

---

## Layer 2 — Construct

构念是 **liquidatable state**——仓位进入协议定义的可清算状态。

它**不是**：
- 借款人偿付能力失败（borrower insolvency）
- 传统信用违约（credit default）
- 实际发生的清算（realized liquidation）

它**是**：
- 一个可从重建的仓位状态中判断的二元状态
- 仓位风险实现链条中的一个中间阶段
- 比 realized liquidation 更干净的 outcome（不受 liquidator-side friction 影响）

### 与 Realized Liquidation 的区分（Paper 1 的重要设计）

```text
Borrower behavior
      ↓
Position state deterioration
      ↓
Liquidation eligibility      ← Outcome A（更干净）
      ↓
Execution frictions           ← liquidator profitability, gas, MEV, congestion, oracle timing
      ↓
Realized liquidation          ← Outcome B（受执行环境影响）
```

Outcome A 更适合作为 Paper 1 的主要 outcome，因为它隔离了 borrower-side state 和 liquidator-side friction。

---

## Layer 3 — Measurement

### Aave V3

- **清算条件**：HF < 1.0
- **判定方式**：重建每个时间点的 HF，检查是否 < 1.0
- **数据来源**：合约状态 + 预言机价格 + 协议参数

### Compound III

- **清算条件**：Account shortfall > 0
- **判定方式**：重建 account liquidity，检查是否 < 0
- **关键**：使用 `liquidateCollateralFactor`（不是 `borrowCollateralFactor`）

### MakerDAO / Sky

- **清算条件**：Collateralization Ratio < Liquidation Ratio
- **判定方式**：重建 vault 的 collateralization ratio
- **注意**：Maker 使用 auction-based liquidation，"eligibility" 的定义与 Aave/Compound 不同

### 作为 Outcome 的度量

```text
Outcome A: Liquidation Eligibility
    Y = 1 if HF < 1.0 (or equivalent)
    Y = 0 otherwise

Outcome B: Realized Liquidation
    Y = 1 if LiquidationCall event occurred
    Y = 0 otherwise
```

---

## Layer 4 — Observable

| 信息 | 可观测性 | 来源 |
|------|---------|------|
| 仓位在时间 T 是否处于可清算状态 | ✅ 高 | 重建状态 |
| 可清算状态的持续时间 | ✅ 高 | 状态重建 |
| 从可清算到实际清算的时间 | ✅ 高 | 对比 eligibility 和 liquidation event |
| 可清算但未被清算的比例 | ✅ 高 | 可计算 |
| 借款人是否知道自己的仓位可清算 | ❌ 不可观测 | — |

---

## Layer 5 — Identification

### 识别挑战

1. **HF 重建精度**：HF 是否 < 1.0 取决于预言机价格的精度和重建的时间粒度
2. **预言机更新频率**：Chainlink 有 heartbeat 和 deviation threshold，价格不是连续更新的
3. **协议参数变化**：LT 值可能因 governance 变化
4. **Compound III 的双 CF**：borrow CF ≠ liquidate CF，必须使用正确的 CF
5. **Maker 的 auction 机制**：Maker 的 liquidation 是 auction-based，eligibility 的定义不同

### 优势

相比于 Realized Liquidation，Liquidation Eligibility：
- 不受 liquidator 竞争、gas、MEV、网络拥堵等执行摩擦影响
- 更直接反映 borrower position state
- 更适合检验 "borrower behavior → position distress" 的关系

---

## Layer 6 — Allowed Claim

### 可以声称

- "Liquidatable state"（可清算状态）
- "The position entered a mechanically liquidatable state at time T"（仓位在时间 T 进入机械性可清算状态）
- "Position distress"（仓位困境）
- "Liquidation eligibility"（清算资格）
- "This outcome is cleaner than realized liquidation because it is not contaminated by liquidator-side execution frictions"（此 outcome 比实际清算更干净，因为不受清算人执行摩擦影响）

### 不可以声称

- "Credit default"（信用违约）
- "Borrower insolvency"（借款人资不抵债）
- "Borrower lacks repayment capacity"（借款人缺乏偿付能力）
- "The borrower is in financial distress"（借款人处于财务困境）——position distress ≠ borrower distress
