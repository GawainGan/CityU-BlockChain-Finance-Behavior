# 03. Health Factor / 健康因子

**六层矩阵详细文件**  
**相关技术文档**：`03_技术文档/01_Aave_V3.md`  
**相关文献**：`04_文献/03_DeFi_Lending/`

---

## Layer 1 — Definition

> **Health Factor (HF) 是 Aave 协议中衡量借贷仓位安全程度的原生风险指标。它等于仓位中所有已启用为 collateral 的抵押资产价值乘以各自的 Liquidation Threshold 之和，除以总债务。HF = 1.0 是清算触发阈值。**

### 7 月 Report 中的硬错误

原 Report 使用：

```text
HF_t = Σ(C_i,t × P_i,t × LTV_i) / D_t
```

**这是错误的。** Aave HF 应使用 **Liquidation Threshold (LT)**，不是 **Loan-to-Value (LTV)**。

LTV 和 LT 是不同的参数：
- **LTV**：决定你能借多少（borrowing capacity）
- **LT**：决定你何时被清算（liquidation threshold）

正确公式：

```text
HF_t = Σ(V_i,t × LT_i) / D_t
```

其中：
- V_i,t = collateral asset i 在时间 t 的价值（数量 × 预言机价格）
- LT_i = asset i 的 Liquidation Threshold（协议参数）
- D_t = total debt（本金 + 应计利息，以 borrow asset 计价）

---

## Layer 2 — Construct

HF 是一个 **Aave-specific** 的仓位风险度量。

它**不是**：
- 一个跨协议通用指标
- 一个 borrower-level 的信用指标
- 一个可以不需要协议参数就能计算的简单比率

它**是**：
- 一个由协议定义的、机械可计算的仓位安全度量
- 清算触发条件 (HF < 1.0) 的直接决定因素
- 借款人行为响应的目标变量之一

### HF = 1.0 的双重性质

HF = 1.0 既是：
- **Protocol mechanism discontinuity**：跨过此阈值，第三方可以触发清算
- **Potential psychological reference point**：借款人可能以此为参照点调整行为

这两个解释不可分离，除非构造特殊识别策略。

---

## Layer 3 — Measurement

### 重建步骤

1. **获取仓位状态**：每个 block/transaction 时间点的 collateral balances 和 debt
2. **获取预言机价格**：Chainlink price feed 在该时间点的报告值
3. **获取协议参数**：该时间点各资产的 LT 值（可能因 governance 变化）
4. **计算 HF**：HF = Σ(V_i × LT_i) / D
5. **频率**：底层 tx/block 级重建，分析面板可聚合到 hourly/daily/monthly

### 关键技术细节

- **Collateral-enabled 状态**：只有 `usageAsCollateralEnabled == true` 的资产才计入 HF
- **EMode**：Efficiency Mode 下使用不同的 LT 值
- **Isolation mode**：Isolated assets 有不同的参数
- **利率模式**：Stable rate 和 variable rate 的债务计算方式不同
- **应计利息**：债务随时间增长（index 机制），需要按 block 重建

### 数据来源

| 数据 | 来源 | 可靠性 |
|------|------|--------|
| Collateral balances | Aave Pool 合约 `getUserReserveData()` | ✅ 高 |
| Debt (principal + interest) | Aave Pool 合约 + `ScaledBalance` + reserve index | ✅ 高 |
| LT 参数 | Aave `getReserveConfigurationData()` | ✅ 高 |
| 预言机价格 | Chainlink PriceFeed 合约 `latestRoundData()` | ✅ 高 |
| Collateral-enabled 状态 | Aave `UserReserveData.usageAsCollateralEnabled` | ✅ 高 |
| 历史参数变更 | Governance 事件 + 合约历史状态 | ✅ 高（需 archive node） |

---

## Layer 4 — Observable

| 信息 | 可观测性 | 频率 |
|------|---------|------|
| 任意时间点的 HF 值 | ✅ 高（需 archive node 重建） | tx/block 级 |
| HF 的变化轨迹 | ✅ 高 | tx/block 级 |
| HF 跨越特定阈值的时间 | ✅ 高 | tx/block 级 |
| HF 在特定 band 中的停留时间 | ✅ 高 | tx/block 级 |
| 借款人是否知道自己的 HF | ❌ 不可观测 | — |
| 借款人是否以 HF=1 为心理参照点 | ❌ 不可观测 | — |

---

## Layer 5 — Identification

### 识别挑战

1. **HF 是 Aave-specific**：不能直接用于 Compound 或 Maker。Compound 使用 account liquidity/shortfall，Maker 使用 collateralization ratio
2. **参数变化**：LT 值可能因 governance 而变化，历史 HF 重建需要使用当时的参数
3. **EMode / Isolation**：不同模式下 LT 值不同，重建时需要识别仓位所处的模式
4. **HF=1.0 的识别**：HF=1.0 既是机制间断点，也可能是心理参照点。行为不连续在 HF=1.0 附近不能自动归因于前景理论，因为规避清算罚金是理性解释

### 与 Compound/Maker 的不可比性

```text
Aave HF          → 基于 Liquidation Threshold
Compound III     → 基于 borrow/liquidate collateral factor + account shortfall
MakerDAO         → 基于 vault collateralization ratio + liquidation ratio
```

跨协议比较应使用 **Distance to Liquidation** 标准化指标，而非统一 HF。

---

## Layer 6 — Allowed Claim

### 可以声称

- "Aave-specific Health Factor"（Aave 特有的健康因子）
- "The position's distance to the Aave liquidation threshold"（仓位到 Aave 清算阈值的距离）
- "HF was reconstructed at transaction/block level using protocol parameters and oracle prices"（HF 在交易/区块级使用协议参数和预言机价格重建）

### 不可以声称

- "Unified HF across protocols"（跨协议统一 HF）
- "HF = credit risk"（HF 等于信用风险）
- "HF=1 discontinuity = prospect theory evidence"（HF=1 的不连续等价于前景理论证据）——需排除理性规避清算罚金的解释
- "HF 用 LTV 计算"（这是硬错误）
