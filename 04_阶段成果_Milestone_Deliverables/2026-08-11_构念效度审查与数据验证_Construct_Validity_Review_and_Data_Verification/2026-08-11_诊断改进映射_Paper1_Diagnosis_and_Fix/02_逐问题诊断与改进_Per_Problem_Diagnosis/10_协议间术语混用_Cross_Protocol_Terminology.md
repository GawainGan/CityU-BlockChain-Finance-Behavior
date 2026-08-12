# 10. 协议间术语直接混用

**严重程度**：🔵 Terminology  
**Report 1 位置**：`sections/methodology.tex` Lines 9-11  
**六层矩阵文件**：`02_逐概念六层矩阵/03_Health_Factor_健康因子.md`, `06_术语边界对照表.md`

---

## 1. 问题描述

Report 1 提议同时使用 Aave、Compound 和 MakerDAO 的数据，但没有说明三个协议的风险指标定义不同。Aave 的 Health Factor、Compound 的 Account Liquidity/Shortfall、Maker 的 Collateralization Ratio 是不同的构念，不能直接比较或拼接为一个 panel。

---

## 2. Report 1 原文

> **methodology.tex, Lines 7-11:**
>
> The primary data source will be the historical event logs and state data from three major DeFi lending protocols: Aave (V2 and V3), Compound (V2 and V3), and MakerDAO. These three protocols collectively account for the majority of DeFi lending activity on Ethereum and offer complementary data for cross-protocol validation. The specific event types to be extracted include: (i) `Deposit` and `Withdraw` events, representing the provision and removal of collateral; (ii) `Borrow` and `Repay` events...

> **methodology.tex, Line 94 (Robustness):**
>
> (iv) repeating the analysis separately for each protocol to assess cross-protocol generalizability

---

## 3. 错误分析

### 3.1 三个协议的风险指标差异

| 维度 | Aave V3 | Compound III | MakerDAO |
|------|---------|-------------|----------|
| 风险指标 | Health Factor (HF < 1 = liquidatable) | Account Shortfall (> 0 = liquidatable) | Collateralization Ratio (< LR = liquidatable) |
| 清算触发参数 | Liquidation Threshold (LT) | liquidateCollateralFactor (≠ borrowCF) | Liquidation Ratio |
| 结构 | Position | Account | Vault |
| 清算方式 | Liquidator repays + seizes | Protocol absorbs collateral | Auction-based |
| Collateral enable | 手动 enable/disable | 自动（所有 supply 都是 collateral） | lock 操作即 collateral |
| 事件命名 | Supply/Withdraw/Borrow/Repay/LiquidationCall | Supply(=还款)/Withdraw(=借款)/AbsorbCollateral | lock/free/draw/wipe/liquidation |
| 借款资产 | 多种 | 单一 base asset | DAI/USDS |

### 3.2 核心问题

1. **事件名称含义不同**：Compound III 的 "Supply" 实际是还款（归还 base asset），"Withdraw" 实际是借款（提取 base asset）。如果直接用事件名称拼接，会导致借款和还款被颠倒。

2. **风险指标定义不同**：HF、Account Shortfall、Collateralization Ratio 的计算方式不同。不能直接比较"HF=1.2"（Aave）和"Shortfall=0"（Compound）。

3. **清算机制不同**：Aave 的 liquidator-based 清算、Compound 的 absorb 机制、Maker 的 auction-based 清算，在执行时间、价格影响、可观测事件上都有显著差异。

4. **Collateral 状态管理不同**：Aave 需要手动 enable collateral；Compound III 自动将所有 supply 作为 collateral；Maker 的 lock 操作直接是 collateral。

### 3.3 对 Report 1 的影响

- 如果直接将三个协议的数据拼接为一个 panel，会引入严重的 measurement error
- 不同协议的"同一事件名称"含义可能完全相反（如 Compound III 的 Supply/Withdraw）
- 跨协议的 "cross-protocol validation" 需要明确标准化方法

---

## 4. 六层矩阵映射

**术语边界对照表**：`06_术语边界对照表.md` §三、协议间术语映射表

**技术文档**：
- `03_技术文档/01_Aave_V3.md`
- `03_技术文档/02_Compound_III.md`
- `03_技术文档/03_MakerDAO_Sky.md`

---

## 5. 修正方案

### 5.1 方案选择

**推荐方案：Aave V3 为主协议，Compound/Maker 为外部有效性检验**

```text
Report 1 原方案：
  Aave + Compound + MakerDAO → 直接拼接 panel → cross-protocol validation

修正方案：
  Aave V3 (Ethereum mainnet) → 主分析
  Compound III / MakerDAO → 外部有效性检验
    → 分别分析（不拼接 panel）
    → 检验核心发现是否在不同协议机制下依然成立
    → 明确标注协议差异
```

### 5.2 理由

1. **降低 measurement error**：以 Aave V3 为主，避免跨协议事件名称和风险指标定义的混淆
2. **提高内部有效性**：单一协议内，所有变量定义一致
3. **保留外部有效性检验**：通过分别分析 Compound/Maker，检验核心发现的稳健性
4. **简化数据重建**：只需精确重建一个协议的 HF 轨迹

### 5.3 如果保留多协议设计

如果出于 reviewer 要求需要保留多协议设计，必须：

1. **分别标准化**：为每个协议建立独立的事件映射和风险指标计算
2. **明确协议差异**：在方法论中说明每个协议的机制差异
3. **不直接拼接**：分别分析，而非拼接为一个 panel
4. **标准化指标**：如果需要跨协议比较，设计标准化的风险距离指标（如 "distance to liquidation in standard deviations"）

---

## 6. 文献支撑

| 文献 | 与本问题的关系 |
|------|---------------|
| Iftikhar et al. (2025) | 直接比较了 Aave 和 Compound 的风险管理机制差异 |
| Bartoletti & Lipparini (2025) | 形式化了不同 DeFi 借贷协议的结构差异 |
| Tovanich et al. (2023) | 在 Compound V2 中分析——单一协议分析的优秀范例 |
| Schuler (2026) | 在 Aave V2 中分析——单一协议分析的优秀范例 |

---

## 7. 修改后的文本

```latex
\subsection{Data Sources and Protocol Selection}

The proposed study relies exclusively on publicly available on-chain 
data from Ethereum-based DeFi lending protocols. The primary data 
source is \textbf{Aave V3 on Ethereum mainnet}, selected for three 
reasons: (i) it is the largest DeFi lending protocol by total value 
locked, ensuring sufficient sample size; (ii) its Health Factor 
mechanism provides a well-defined, continuously observable risk 
metric; and (iii) its event structure (Supply, Withdraw, Borrow, 
Repay, LiquidationCall, SetUserUseReserveAsCollateral) is 
sufficiently rich for reconstructing position-level behavioral 
trajectories.

To assess external validity, the analysis is replicated on 
\textbf{Compound III} and \textbf{MakerDAO/Sky}, with important 
caveats. These protocols differ from Aave V3 in structurally 
important ways: Compound III uses a single base asset per market 
and an absorb-based (rather than liquidator-based) liquidation 
mechanism, with different collateral factor parameters for 
borrowing and liquidation; MakerDAO uses a Vault structure with 
auction-based liquidation. Furthermore, event semantics differ 
across protocols: for example, ``Supply'' in Compound III 
denotes returning the base asset (functionally equivalent to 
repayment), not depositing collateral as in Aave. Consequently, 
the three protocols are analyzed \emph{separately} rather than 
pooled into a single panel, and cross-protocol comparisons are 
conducted by examining whether the core behavioral findings 
replicate across different protocol architectures rather than 
by direct parameter comparison.
```
