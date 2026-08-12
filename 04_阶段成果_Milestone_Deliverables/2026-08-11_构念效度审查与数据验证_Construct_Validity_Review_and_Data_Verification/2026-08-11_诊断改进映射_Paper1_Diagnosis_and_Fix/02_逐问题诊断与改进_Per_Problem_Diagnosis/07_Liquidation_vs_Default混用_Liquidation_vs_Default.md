# 07. Liquidation 与 Default 混用

**严重程度**：🟡 Over-claim  
**Report 1 位置**：`sections/abstract.tex`, `sections/literature-review.tex` Lines 27-31, `sections/research-topic.tex`, `sections/discussion.tex`  
**六层矩阵文件**：`02_逐概念六层矩阵/10_Liquidation_Eligibility.md`, `11_Realized_Liquidation.md`

---

## 1. 问题描述

Report 1 在多处将 liquidation（清算）和 default（信用违约）混用，或将清算预测等同于信用风险评估。Liquidation 是仓位级别的机械性强制平仓，Default 是借款人级别的偿付能力失败。两者是不同的构念，不应混用。

---

## 2. Report 1 原文

> **literature-review.tex, Line 27:**
>
> ...the use of on-chain data for credit risk assessment and default prediction.

> **literature-review.tex, Line 29:**
>
> ...predict the likelihood of default.

> **literature-review.tex, Line 31:**
>
> ...predict whether the borrower will default at time t+k.

> **literature-review.tex, Line 37:**
>
> ...whether borrowers' active adjustments during periods of rising position risk in DeFi lending markets contain risk information beyond that captured by conventional on-chain state variables...

> **discussion.tex, Line 11:**
>
> ...even a small but statistically significant improvement in predictive power could be practically relevant in the context of DeFi protocols, where even marginal improvements in liquidation prediction can have substantial economic consequences...

> **research-topic.tex, Line 9:**
>
> The empirical relationship between borrowers' active behavioral adjustments in response to rising position risk in DeFi lending protocols and the subsequent likelihood of liquidation or other adverse risk outcomes.

---

## 3. 错误分析

### 3.1 混用模式

Report 1 中的混用主要有三种模式：

1. **直接使用 "default" 描述 DeFi liquidation**：如 literature-review Line 29 "predict the likelihood of default"——但 DeFi 中没有传统意义上的 default，只有 liquidation
2. **将 on-chain credit risk literature 的 "default" 直接借用到本研究**：如 Line 31 "predict whether the borrower will default"——但 Ghosh et al. (2024) 等文献使用的 "default" 也需要审查其是否实际指 liquidation
3. **"credit risk" 和 "liquidation risk" 交替使用**：暗示两者等价

### 3.2 实际差异

| 维度 | Liquidation | Default |
|------|-----------|---------|
| 层级 | Position-level | Borrower-level |
| 触发 | HF < 1（机械触发） | 偿付能力/意愿失败 |
| 可观测性 | 链上事件（高） | 需链下信息（低） |
| 后果 | 仓位被平仓，损失清算罚金 | 信用记录受损，法律追索 |
| 原因 | 价格暴跌、杠杆过高、操作延迟、MEV | 偿付能力不足 |
| 可逆性 | 不可逆（仓位已平） | 可能重组、延期 |

### 3.3 注意：Report 1 部分地方是正确的

值得肯定的是，Report 1 在很多地方正确使用了 "liquidation"：
- RQ2 的实际 outcome 是 "future liquidation events"（正确）
- Discussion Line 11 使用了 "liquidation prediction"（正确）
- Research Topic Line 9 使用了 "likelihood of liquidation"（正确）

问题主要出在 Literature Review 中描述 on-chain credit risk literature 时，将 "default" 直接应用于 DeFi 语境。

---

## 4. 六层矩阵映射

**不可声称清单**：`05_不可声称清单.md`
- §2.1: "Liquidation = credit default"
- §2.2: "被清算的借款人 = high-risk borrower"
- §2.3: "Liquidation propensity = default probability"
- §2.4: "清算预测准确度提高 = 信用风险管理改善"

**术语边界对照表**：`06_术语边界对照表.md`
- Liquidation ≠ Default

---

## 5. 修正方案

### 5.1 区分使用场景

- **描述 DeFi 的 outcome**：使用 "liquidation" 或 "liquidation eligibility"
- **描述传统金融的 outcome**：可以使用 "default"
- **描述 on-chain credit risk literature**：明确说明这些文献中的 "default" 是否实际指 "liquidation"
- **描述本研究的贡献**：使用 "liquidation prediction"，不使用 "credit risk assessment"

### 5.2 Literature Review 中的处理

当引用 Ghosh et al. (2024) 等文献时，需要澄清：

```text
Ghosh et al. (2024) 框架使用 "credit risk scoring" 和 "default prediction" 
来描述其 outcome。但在 DeFi 语境中，可观测的信用不良事件是 liquidation 
而非传统意义上的 default。本研究使用 "liquidation" 作为 outcome，并明确 
区分 liquidation 与 credit default。
```

### 5.3 新增明确声明

在 Research Topic 或 Methodology 部分新增以下声明：

> "Throughout this report, we use 'liquidation' to refer to the protocol-level, mechanically triggered event in which a position with HF < 1 is partially or fully closed by a third-party liquidator. We do not use 'default' as a synonym for liquidation, as the two concepts differ in level (position vs. borrower), trigger (mechanical vs. creditworthiness), and observability (on-chain vs. off-chain)."

---

## 6. 文献支撑

| 文献 | 与本问题的关系 |
|------|---------------|
| Sadeghi & Feinstein (2026) | 明确将 DeFi liquidation 定位为 mechanical process |
| Ghosh et al. (2024) | 使用 "default" 描述 DeFi outcome——需要审查其是否实际指 liquidation |
| Di Maggio & Yao (2020) | 传统 fintech lending 中的 default——与 DeFi liquidation 不同 |
| Perez et al. (2021) | "Liquidations: DeFi on a Knife-Edge"——使用 "liquidation" 而非 "default" |

---

## 7. 修改后的文本

### literature-review.tex 修正

```latex
\subsection{On-Chain Risk Assessment and Predictive Modeling}

The third body of literature relevant to this proposal concerns the 
use of on-chain data for risk assessment and predictive modeling 
of adverse position outcomes. The fundamental premise of this 
emerging field is that the transparency of blockchain data makes 
it possible to construct risk models without relying on the 
centralized credit bureaus, bank account information, or 
traditional financial records that underpin conventional credit 
scoring systems.

Several recent studies have demonstrated the feasibility of this 
approach. \citet{ghosh2024onchain} developed a framework for 
on-chain credit risk scoring in DeFi, using machine learning models 
trained on wallet-level transaction histories, borrowing and 
repayment patterns, and interaction frequencies to predict the 
likelihood of adverse outcomes. Their results suggest that on-chain 
behavioral data contains significant risk-relevant information, 
even in the absence of off-chain identity information. It should be 
noted that in the DeFi context, the observable adverse outcome is 
liquidation---a protocol-level, mechanically triggered event---rather 
than credit default in the traditional sense, which is a 
borrower-level outcome involving inability or unwillingness to 
repay. The distinction between liquidation and default is important: 
liquidation may be triggered by price volatility, excessive 
leverage, or operational delays rather than by a borrower's 
fundamental inability to repay, and the two concepts should not be 
conflated.
```

### 新增声明（建议放在 Research Topic 开头）

```latex
\textbf{Terminological note.} Throughout this report, we use 
``liquidation'' to refer to the protocol-level event in which a 
position with a health factor below 1.0 is partially or fully 
closed by a third-party liquidator. We do not use ``default'' as a 
synonym for liquidation, as the two concepts differ in level 
(position vs.\ borrower), trigger (mechanical threshold vs.\ 
creditworthiness failure), and observability (on-chain event vs.\ 
off-chain outcome). The outcome variable in this study is 
liquidation, not credit default.
```
