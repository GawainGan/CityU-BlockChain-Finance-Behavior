# 02. Position Risk / 仓位风险

**六层矩阵详细文件**  
**相关技术文档**：`03_技术文档/01_Aave_V3.md`, `02_Compound_III.md`  
**相关文献**：`04_文献/03_DeFi_Lending/`

---

## Layer 1 — Definition

> **仓位风险是协议定义的仓位距离 liquidation boundary 的状态。它是一个 protocol-level、position-level 的机械状态指标，反映该仓位在当前协议参数和市场价格下的安全程度。**

关键区分：

```text
Position Risk ≠ Credit Risk
Position Risk ≠ Borrower-level Risk
Position Risk ≠ Portfolio Risk
```

仓位风险由以下因素决定：
- 抵押资产价值 × 协议风险参数（liquidation threshold / collateral factor）
- 债务价值（本金 + 应计利息）
- 预言机报告的资产价格
- 协议参数的当前设置（可能因 governance 而变化）

---

## Layer 2 — Construct

构念是 **position-level risk state**——单个借贷仓位在特定时间点、特定协议参数下的风险水平。

它**不是**：
- Borrower-level risk（借款人整体风险）
- Portfolio risk（资产组合风险）
- Credit risk（信用风险）
- Systemic risk（系统性风险）

它**是**：
- 一个可以由合约状态 + 预言机价格 + 协议参数机械重建的指标
- 跨协议不可直接比较（需标准化为 Distance to Liquidation）

---

## Layer 3 — Measurement

### Aave V3

- **核心指标**：Health Factor (HF)
- **公式**：HF = Σ(V_i × LT_i) / D
  - V_i = collateral asset i 的价值
  - LT_i = asset i 的 Liquidation Threshold（**不是 LTV**）
  - D = total debt（本金 + 应计利息）
- **清算条件**：HF < 1.0
- **数据来源**：合约状态 + 历史参数 + Chainlink 预言机价格

### Compound III

- **核心指标**：Account Liquidity / Shortfall
- **机制**：Compound III 使用 `getAssetInfo()` 获取每个 collateral asset 的 `borrowCollateralFactor` 和 `liquidateCollateralFactor`
- **关键区分**：Borrow Collateral Factor ≠ Liquidation Collateral Factor
- **清算条件**：Account shortfall > 0（基于 liquidation collateral factor）

### MakerDAO / Sky

- **核心指标**：Vault Collateralization Ratio
- **公式**：Collateralization Ratio = (Collateral Value × Liquidation Ratio) / Debt
- **机制**：Maker 使用 Vault 结构，每个 vault 有独立的 collateral 和 debt
- **清算方式**：Auction-based（与 Aave/Compound 的 liquidator-based 不同）

### 跨协议标准化

```text
Protocol Native Risk Metric
    ↓
Liquidation Boundary
    ↓
Protocol-specific Distance to Liquidation
    ↓
Standardized Cross-protocol Measure
```

---

## Layer 4 — Observable

| 信息 | 可观测性 | 来源 | 频率 |
|------|---------|------|------|
| 仓位当前抵押资产与数量 | ✅ 高 | 合约状态 | tx/block 级 |
| 仓位当前债务 | ✅ 高 | 合约状态 | tx/block 级 |
| 预言机报告的资产价格 | ✅ 高 | Chainlink 合约 | 更新时 |
| 协议当前风险参数（LT, CF 等） | ✅ 高 | 合约参数 | 变更时 |
| 历史协议参数变更 | ✅ 高 | governance 事件 | 事件级 |
| HF / Account Liquidity | ✅ 高 | 可从以上重建 | tx/block 级 |
| 借款人在其他协议的仓位 | ❌ 不可观测 | 需跨协议索引 | — |
| 借款人在 CEX 的仓位 | ❌ 不可观测 | 链下数据 | — |
| 借款人的整体杠杆 | ❌ 不可观测 | 需完整资产负债表 | — |

---

## Layer 5 — Identification

### 识别挑战

1. **协议参数变化**：LT、CF 等参数可能因 governance 而变化，历史数据需要使用当时的参数而非当前参数
2. **预言机延迟与精度**：Chainlink price feed 有 heartbeat 和 deviation threshold，价格更新不是连续的
3. **利率模式**：Aave 有 stable rate 和 variable rate，债务价值的计算方式不同
4. **跨协议不可比**：Aave HF、Compound shortfall、Maker collateralization ratio 是不同机制，不能简单统一为 "HF → 1"

### 混淆因素

- 仓位风险的变化可能来自价格波动（外部）或借款人操作（内部），需要区分
- 利息累积会持续改变债务值，即使借款人没有任何操作
- 预言机价格与市场价格可能有偏差

---

## Layer 6 — Allowed Claim

### 可以声称

- "Position risk"（仓位风险）
- "Distance to liquidation"（清算距离）
- "The position's current collateralization state"（仓位当前抵押状态）
- "Protocol-defined risk metric"（协议定义的风险指标）

### 不可以声称

- "Credit risk"（信用风险）——需要 borrower-level 信息
- "Borrower's overall risk exposure"（借款人整体风险暴露）
- "The borrower is in financial distress"（借款人处于财务困境）——仓位风险 ≠ 借款人困境
- "Unified HF across protocols"（跨协议统一 HF）——不同协议机制不同
