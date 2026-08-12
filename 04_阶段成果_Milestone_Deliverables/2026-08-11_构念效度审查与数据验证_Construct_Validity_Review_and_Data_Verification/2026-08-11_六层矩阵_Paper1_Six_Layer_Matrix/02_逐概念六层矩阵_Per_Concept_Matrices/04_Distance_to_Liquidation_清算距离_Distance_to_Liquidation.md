# 04. Distance to Liquidation / 清算距离

**六层矩阵详细文件**  
**相关技术文档**：`03_技术文档/01_Aave_V3.md`, `02_Compound_III.md`, `03_MakerDAO_Sky.md`  
**相关文献**：`04_文献/03_DeFi_Lending/`

---

## Layer 1 — Definition

> **Distance to Liquidation 是一个标准化的跨协议仓位风险度量，表示一个仓位当前距离协议特定清算边界的距离。它由各协议的原生风险指标经过标准化转换后得到。**

不同协议有不同的清算机制和风险度量，不能简单统一为一个 "HF"。Distance to Liquidation 是在尊重协议异质性的前提下，提供可比性的方案。

---

## Layer 2 — Construct

构念是 **protocol-normalized distance to liquidation**——一个跨协议可比的、标准化的仓位风险距离指标。

它**不是**：
- 一个统一的 HF
- 一个 borrower-level 风险指标
- 一个包含所有风险维度的综合指标

它**是**：
- 基于各协议原生风险机制的标准化映射
- 在各自协议内精确，跨协议可比的近似

---

## Layer 3 — Measurement

### Aave V3

```text
Distance_to_Liquidation_Aave
= (HF_t - 1.0) / HF_t
= 1 - D_t / Σ(V_i,t × LT_i)
```

- HF < 1.0 → Distance < 0（可清算）
- HF = 1.0 → Distance = 0（清算边界）
- HF = 2.0 → Distance = 0.5

### Compound III

```text
Distance_to_Liquidation_Compound
= Account_Liquidity / (Collateral_Value × Liquidate_CF)
```

- Account Liquidity > 0 → 安全
- Account Shortfall > 0 → 可清算
- 关键：Compound III 有 `borrowCollateralFactor ≠ liquidateCollateralFactor`

### MakerDAO / Sky

```text
Distance_to_Liquidation_Maker
= (Collateral_Value × Liquidation_Ratio - Debt) / Debt
= Collateralization_Ratio × Liquidation_Ratio - 1
```

- Maker 使用 auction-based liquidation，机制与 Aave/Compound 不同
- Liquidation Ratio 是协议参数

### 标准化

```text
Protocol Native Risk Metric
    ↓
Liquidation Boundary (binary: safe / liquidatable)
    ↓
Protocol-specific Distance to Liquidation
    ↓
Standardized Cross-protocol Measure (e.g., percentile rank)
```

---

## Layer 4 — Observable

| 信息 | 可观测性 | 来源 |
|------|---------|------|
| 各协议原生风险指标 | ✅ 高 | 合约状态重建 |
| 清算边界 | ✅ 高 | 协议参数 |
| 距清算边界的距离 | ✅ 高 | 计算 |
| 跨协议标准化后的距离 | ✅ 中高 | 各协议分别计算后标准化 |
| 哪个协议的仓位风险更"高" | ⚠️ 中 | 标准化后有近似可比性 |

---

## Layer 5 — Identification

### 识别挑战

1. **协议机制异质性**：Aave (liquidator-based)、Compound III (liquidator-based but different CF)、Maker (auction-based) 的清算机制不同
2. **参数时变性**：所有协议的参数都可能因 governance 变化
3. **标准化损失**：标准化过程中可能丢失协议特定的风险信息
4. **Maker 的特殊性**：Maker 的 auction 机制使得"清算"的执行方式与 Aave/Compound 不同，liquidation event 的定义也不同

### 处理策略

- 主样本以 Aave 为核心
- Compound / Maker 作为 external validity 检验
- 不强行将三个协议的仓位放入同一个 panel
- 分别报告各协议的结果

---

## Layer 6 — Allowed Claim

### 可以声称

- "Protocol-normalized distance to liquidation"（协议标准化的清算距离）
- "The position's distance to its protocol-specific liquidation boundary"（仓位到协议特定清算边界的距离）
- "Cross-protocol comparison is based on standardized distance metrics, not unified HF"（跨协议比较基于标准化距离指标，不是统一 HF）

### 不可以声称

- "Unified HF across Aave, Compound, and Maker"（统一 HF）
- "Compound shortfall = Aave HF < 1"（直接等价）
- "Maker liquidation = Aave liquidation"（机制不同）
- "The borrower's risk is X across all protocols"（借款人在所有协议的风险是 X）
