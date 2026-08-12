# 05. RQ2 "Credit Layer" 命名与 Credit 过度声称

**严重程度**：🟡 Over-claim  
**Report 1 位置**：`sections/research-topic.tex` Line 18, `sections/abstract.tex`, `sections/introduction.tex` Line 9  
**六层矩阵文件**：`05_不可声称清单.md` §1, §2

---

## 1. 问题描述

Report 1 将 RQ2 命名为 "Credit Layer"，并在多处使用 "credit prediction"、"credit-relevant information" 等术语。但本研究的 outcome 是 liquidation（清算），不是 credit default（信用违约）。Liquidation ≠ Default。使用 "credit" 一词来描述清算预测会误导读者，使其认为本研究在做信用评分。

---

## 2. Report 1 原文

> **research-topic.tex, Line 18:**
>
> **RQ2 (Credit Layer).** Controlling for conventional on-chain risk indicators, including current health factor, collateral ratio, account activity, asset concentration, and market volatility, do behavioral process variables capturing the *trajectory* of active adjustments provide statistically and economically significant incremental predictive power for future liquidation events?

> **introduction.tex, Line 9:**
>
> The second, credit-oriented layer asks whether these behavioral patterns, if they exist, carry incremental predictive power for future liquidation events or risk deterioration beyond what is already captured by health factors, collateral ratios, and account activity measures.

> **abstract.tex, Line 3:**
>
> ...credit risk...

> **research-topic.tex, Line 47:**
>
> ...it introduces a process-based perspective on credit risk assessment that complements the static, feature-based approaches that have dominated the on-chain credit risk literature to date...

---

## 3. 错误分析

### 3.1 Liquidation ≠ Default

| 维度 | Liquidation（清算） | Default（信用违约） |
|------|---------------------|-------------------|
| 触发 | HF < 1（仓位级别机械触发） | 偿付能力失败（借款人级别信用事件） |
| 原因 | 价格暴跌、杠杆过高、操作延迟 | 偿付能力不足、偿付意愿下降 |
| 后果 | 仓位被强制平仓，损失清算罚金 | 信用记录受损，法律追索 |
| 层级 | Position-level | Borrower-level |
| 数据可观测性 | 高（链上事件） | 低（需要链下信息） |

### 3.2 "Credit Layer" 的问题

- RQ2 的实际 outcome 是 "future liquidation events"（Line 18 原文），不是 credit default
- 但命名为 "Credit Layer" 暗示研究的是信用问题
- "credit-oriented layer"（introduction Line 9）同样误导
- "credit risk assessment"（research-topic Line 47）暗示改进信用评估，但实际改进的是清算预测

### 3.3 连锁影响

"Credit" 一词的过度使用在全文中产生连锁效应：
- Abstract 提到 "credit risk"
- Introduction 提到 "credit-oriented layer"
- Research Topic 提到 "Credit Layer" 和 "credit risk assessment"
- Literature Review 标题包含 "On-Chain Credit Risk Assessment"
- Discussion 提到 "credit prediction"

---

## 4. 六层矩阵映射

**不可声称清单**：`05_不可声称清单.md`
- §1.3: "行为过程变量度量了 creditworthiness"
- §1.4: "改进清算预测 = 改进信用评分"
- §2.1: "Liquidation = credit default"
- §2.3: "Liquidation propensity = default probability"

**术语边界对照表**：`06_术语边界对照表.md`
- Liquidation ≠ Default

---

## 5. 修正方案

### 5.1 RQ2 命名修正

```text
原名：RQ2 (Credit Layer)
修正：RQ2 (Liquidation Propensity Layer)
或：  RQ2 (Position Distress Layer)
```

### 5.2 术语替换

| ❌ 不应使用 | ✅ 应使用 | 出现位置 |
|-----------|---------|---------|
| "Credit Layer" | "Liquidation Propensity Layer" | research-topic.tex L18 |
| "credit-oriented layer" | "predictive layer" | introduction.tex L9 |
| "credit prediction" | "liquidation prediction" | discussion.tex |
| "credit risk assessment" (for this study) | "liquidation risk prediction" | research-topic.tex L47 |
| "credit-relevant information" | "liquidation-relevant information" | 多处 |
| "credit signals" | "position risk signals" | abstract, title |

### 5.3 Literature Review 标题

```text
原标题：On-Chain Credit Risk Assessment
修正后：On-Chain Risk Assessment and Predictive Modeling
```

保留对现有 credit risk literature 的引用，但明确说明本研究不直接做 credit scoring，而是做 liquidation prediction。

### 5.4 明确声明

在论文中明确声明：

> "We do not equate liquidation with credit default. Liquidation is a mechanical, position-level risk realization triggered by the protocol when the health factor falls below 1.0, whereas credit default is a borrower-level inability or unwillingness to repay. The outcome variable in this study is liquidation eligibility and realized liquidation, not credit default."

---

## 6. 文献支撑

| 文献 | 与本问题的关系 |
|------|---------------|
| Ghosh et al. (2024) | 直接做 on-chain credit scoring——Paper 1 与之的区别在于 outcome 不同 |
| Di Maggio & Yao (2020) | 研究 fintech 借贷中的 default——default 和 liquidation 是不同的构念 |
| Sadeghi & Feinstein (2026) | 专门研究 DeFi liquidation dynamics，明确将 liquidation 定位为机械过程而非信用事件 |
| Berg et al. (2020) | digital footprint 提供 incremental information——Paper 1 类比但不声称做 credit scoring |

---

## 7. 修改后的文本

### RQ2 修正

```latex
\item[RQ2 (Liquidation Propensity Layer).] Controlling for 
conventional on-chain risk indicators, including current health 
factor, collateral ratio, account activity, asset concentration, 
and market volatility, do behavioral process variables capturing 
the \emph{trajectory} of active adjustments provide statistically 
and economically significant incremental predictive power for 
future liquidation events?
```

### Introduction 修正

```latex
The second, predictive layer asks whether these behavioral 
patterns, if they exist, carry incremental predictive power for 
future liquidation events beyond what is already captured by health 
factors, collateral ratios, and account activity measures. We 
emphasize that the outcome of interest is liquidation---a 
protocol-level, mechanically triggered event---not credit default, 
which is a borrower-level outcome requiring different data and 
identification strategies.
```

### Positioning 修正

```latex
Third, it introduces a process-based perspective on liquidation 
risk prediction that complements the static, feature-based 
approaches that have dominated the on-chain risk modeling 
literature to date~\cite{ghosh2024onchain}, potentially opening 
new avenues for the construction of behavioral early warning 
indicators in DeFi lending protocols. We are careful to distinguish 
liquidation prediction from credit scoring: while the two are 
related in principle, liquidation is a position-level mechanical 
event whereas credit scoring addresses borrower-level 
creditworthiness, and the present study does not claim to improve 
credit assessment.
```
