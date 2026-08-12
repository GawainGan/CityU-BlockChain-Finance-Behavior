# 03. Supply ≠ Collateral-Enabled Supply

**严重程度**：🔴 Hard Error  
**Report 1 位置**：`sections/methodology.tex` Line 9  
**六层矩阵文件**：`02_逐概念六层矩阵/07_Supply_vs_CollateralEnabled_供给与抵押启用.md`

---

## 1. 问题描述

Report 1 将 `Deposit` 和 `Withdraw` 事件直接等同于"提供和移除抵押品"（provision and removal of collateral）。但在 Aave V3 中，Supply（存入资产）和 Collateral-Enabled（启用为抵押）是两个独立的状态。资产可以被供应但不启用为抵押，此时它不计入 Health Factor 的计算。

---

## 2. Report 1 原文

> **methodology.tex, Line 9:**
>
> The specific event types to be extracted include: (i) `Deposit` and `Withdraw` events, representing the provision and removal of collateral; (ii) `Borrow` and `Repay` events, representing the creation and settlement of loan positions; (iii) `LiquidationCall` or equivalent events, capturing the triggering of liquidation by third parties; and (iv) `FlashLoan` events for identifying transactions that may involve complex multi-step strategies rather than simple borrowing behavior.

---

## 3. 错误分析

### 3.1 Aave V3 中的两步机制

```text
Step 1: Supply（存入资产）
    → 用户将资产存入 Aave 协议
    → 获得 aToken
    → 资产此时 NOT necessarily 计入 HF

Step 2: SetUserUseReserveAsCollateral（启用为抵押）
    → 用户选择将该资产启用为 collateral
    → 只有此时资产才计入 HF 计算
    → 用户也可以禁用 collateral（un collateral）
```

### 3.2 影响范围

| 情境 | Report 1 的理解 | 实际情况 | 对 HF 重建的影响 |
|------|----------------|---------|-----------------|
| 借款人 supply ETH 并启用为 collateral | ✅ 抵押增加 | ✅ 正确 | 无影响 |
| 借款人 supply ETH 但未启用为 collateral | ❌ 认为抵押增加 | 实际抵押未变 | HF 被高估 |
| 借款人 supply USDC 作为流动性（不启用为 collateral） | ❌ 认为抵押增加 | 实际只是存款 | HF 被高估 |
| 借款人 disable collateral 后 withdraw | ❌ 认为是抵押减少 | 实际抵押早已在 disable 时减少 | HF 时间点错误 |

### 3.3 对行为变量的影响

- "Active Collateral Adjustment Rate"（methodology.tex L44）如果直接用 Supply/Withdraw 事件计算，会把非抵押的 supply/withdraw 误算为抵押调整
- "Response Latency"（L48）如果以 Supply 事件作为"first subsequent active collateral addition"，可能将非抵押操作误判为风险减轻行为

---

## 4. 六层矩阵映射

**文件**：`02_逐概念六层矩阵/07_Supply_vs_CollateralEnabled_供给与抵押启用.md`

| 层级 | 六层矩阵内容 | Report 1 的问题 |
|------|-------------|-----------------|
| Definition | Supply = 存入资产；Collateral-Enabled = 启用为抵押。两者独立 | 将两者等同 |
| Construct | 抵押调整 = collateral-enabled supply 的变化 | 用 supply 变化替代 |
| Measurement | 需追踪 SetUserUseReserveAsCollateral 事件 | 未提及此事件 |
| Observable | Supply + SetUserUseReserveAsCollateral + Withdraw | 仅用 Supply/Withdraw |
| Identification | 需检查 collateral-enabled 状态 | 未检查 |
| Allowed Claim | "collateral-increasing supply"（需确认 collateral-enabled） | 未区分 |

---

## 5. 修正方案

### 5.1 事件类型修正

```text
原分类：
  (i) Deposit / Withdraw = 抵押提供/移除

修正后：
  (i) Supply / Withdraw = 资产存入/提取
  (i-a) SetUserUseReserveAsCollateral = 抵押启用/禁用
  → 需要同时追踪两类事件，才能准确判断抵押变化
```

### 5.2 抵押调整的判定逻辑

```text
风险减轻的追加抵押 = Supply event
    AND 该资产在事件后变为 collateral-enabled
    AND HF 分子增加

风险增加的抵押提取 = Withdraw event
    AND 该资产在事件前是 collateral-enabled
    AND HF 分子减少

单纯的 Supply（未启用为 collateral）= 不计入抵押调整
单纯的 collateral enable/disable（无 supply/withdraw）= 抵押状态变化
```

### 5.3 行为变量修正

- "Active Collateral Adjustment Rate" 应基于 **collateral-enabled supply 的变化**，而非所有 supply 事件
- 需要维护每个地址在每个时间点的 collateral-enabled 状态

---

## 6. 文献支撑

| 文献 | 与本问题的关系 |
|------|---------------|
| Aave V3 官方文档 | 明确说明了 Supply 和 Collateral-Enabled 的独立状态 |
| Bartoletti & Lipparini (2025) | 形式化了 DeFi 借贷协议中的 collateral 状态管理 |
| Iftikhar et al. (2025) | 比较了 Aave（手动 enable）和 Compound III（自动 collateral）的差异 |

---

## 7. 修改后的文本

```latex
The specific event types to be extracted include: 
(i) \texttt{Supply} and \texttt{Withdraw} events, representing the 
deposit and withdrawal of assets to and from the protocol; 
(i\textit{a}) \texttt{SetUserUseReserveAsCollateral} events, 
representing the enabling or disabling of a supplied asset as 
collateral---a state that is independent of the supply action itself 
in Aave V3, where assets may be deposited without being counted 
toward the health factor calculation; 
(ii) \texttt{Borrow} and \texttt{Repay} events, representing the 
creation and settlement of loan positions; 
(iii) \texttt{LiquidationCall} or equivalent events, capturing the 
triggering of liquidation by third parties; and 
(iv) \texttt{FlashLoan} events for identifying transactions that may 
involve complex multi-step strategies rather than simple borrowing 
behavior.

It is important to distinguish between supplying an asset and 
enabling it as collateral: in Aave V3, a user may supply assets 
without enabling them as collateral, in which case they do not 
contribute to the health factor numerator. Accurate reconstruction 
of collateral adjustments therefore requires tracking both 
\texttt{Supply}/\texttt{Withdraw} events and 
\texttt{SetUserUseReserveAsCollateral} events, and maintaining a 
time-varying record of each asset's collateral-enabled status for 
each borrower position.
```

### 行为变量修正（methodology.tex Section 4.4）

```latex
\item[Active Collateral Adjustment Rate.] The net change in 
collateral-enabled asset value (additions via supply with 
collateral enablement, or removals via withdrawal of 
collateral-enabled assets) by the borrower during the observation 
month, scaled by the average total collateral value over the same 
period. Positive values indicate net addition of collateral 
(risk-reducing) and negative values indicate net withdrawal 
(risk-increasing). This measure excludes supply and withdrawal 
activity involving assets that are not enabled as collateral.
```
