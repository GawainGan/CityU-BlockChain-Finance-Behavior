# 11. "Credit-Relevant Information" 反复使用，超出范围

**严重程度**：🟡 Over-claim  
**Report 1 位置**：`sections/introduction.tex`, `sections/literature-review.tex`, `sections/research-topic.tex`, `sections/discussion.tex`  
**六层矩阵文件**：`05_不可声称清单.md` §1, §2

---

## 1. 问题描述

Report 1 在全文中反复使用 "credit-relevant information"、"credit signals"、"credit prediction" 等术语来描述本研究的贡献。但本研究的数据来自抵押借贷协议，outcome 是 liquidation，不是 credit default。"Credit-relevant" 暗示与信用评估直接相关，但本研究只能声称与清算预测相关。

---

## 2. Report 1 原文

以下为 "credit" 相关术语在 Report 1 中的出现位置：

> **introduction.tex Line 9:**
> "The second, credit-oriented layer asks whether these behavioral patterns..."

> **literature-review.tex Line 27:**
> "...the use of on-chain data for credit risk assessment and default prediction."

> **literature-review.tex Line 33:**
> "...prominence in the broader financial economics literature on the informational content of trading behavior."

> **research-topic.tex Line 7:**
> "...may contain credit-relevant information that is not captured by point-in-time snapshots..."

> **research-topic.tex Line 47:**
> "...a process-based perspective on credit risk assessment..."

> **discussion.tex Line 7:**
> "...contains information about future outcomes..."

> **discussion.tex Line 29:**
> "...whether borrower behavior contains credit-relevant information..."

> **discussion.tex Line 31:**
> "...the process of risk management contains information beyond the state of risk exposure..."

---

## 3. 错误分析

### 3.1 "Credit-relevant" 的问题

| 术语 | 实际含义 | 问题 |
|------|---------|------|
| "credit-relevant information" | 与信用评估相关的信息 | 本研究不评估信用，只预测清算 |
| "credit-oriented layer" | 信用导向的层级 | RQ2 是清算预测，不是信用评估 |
| "credit risk assessment" | 信用风险评估 | 本研究做的是清算风险预测 |
| "credit prediction" | 信用预测 | 实际是清算预测 |
| "credit signals" (标题) | 信用信号 | 实际是仓位风险信号 |

### 3.2 与问题 05、07、08 的关系

本问题是问题 05（Credit Layer 命名）、07（Liquidation vs Default）、08（Collateral vs Credit）的综合体现。"Credit-relevant information" 是这些问题的共同症状。

### 3.3 影响范围

"Credit" 相关术语贯穿全文（Introduction → Literature Review → Research Topic → Discussion），形成一致的 over-claiming 模式。修正需要全文范围的术语替换。

---

## 4. 六层矩阵映射

**不可声称清单**：`05_不可声称清单.md`
- §1.3: "行为过程变量度量了 creditworthiness"
- §1.4: "改进清算预测 = 改进信用评分"
- §2.3: "Liquidation propensity = default probability"

---

## 5. 修正方案

### 5.1 全文术语替换表

| ❌ 原文 | ✅ 修正 | 涉及位置 |
|--------|--------|---------|
| "credit-relevant information" | "risk-relevant information" 或 "liquidation-relevant information" | introduction, research-topic, discussion |
| "credit-oriented layer" | "predictive layer" | introduction |
| "credit risk assessment" (描述本研究) | "liquidation risk prediction" | research-topic, discussion |
| "credit prediction" | "liquidation prediction" | discussion |
| "credit signals" (标题) | "position risk signals" 或 "behavioral risk indicators" | 标题 |
| "credit risk" (描述 DeFi) | "liquidation risk" 或 "position risk" | abstract, 多处 |
| "On-Chain Credit Risk Assessment" (Lit Review 标题) | "On-Chain Risk Assessment and Predictive Modeling" | literature-review |

### 5.2 保留 "Credit" 的场景

- 描述传统金融作为对比（"traditional credit markets"）
- 引用现有文献的标题（"On-Chain Credit Risk Score" by Ghosh et al.）
- 描述未来研究方向（"potential connection to credit assessment"）

### 5.3 统一原则

在 Report v2 中采用统一原则：

> "When describing the present study, use 'liquidation,' 'position risk,' and 'risk-relevant information.' Reserve 'credit' for (a) discussions of traditional finance as a contrast, (b) citations of existing literature, and (c) future research directions connecting to Paper 3."

---

## 6. 文献支撑

| 文献 | 与本问题的关系 |
|------|---------------|
| Berg et al. (2020) | Digital footprint 提供 incremental information——核心启示是 complement 而非 substitute，Paper 1 类比但不声称做 credit scoring |
| Gambacorta et al. (2024) | 系统梳理 alternative data 在信用评估中的角色——Paper 1 与之的区别在于 outcome 不同 |
| Ghosh et al. (2024) | 直接做 on-chain credit scoring——Paper 1 与之的区别在于 Paper 1 不声称做 credit scoring |

---

## 7. 修改后的文本

### 全文修正原则

由于 "credit-relevant information" 等术语贯穿全文，修正需要逐处替换。以下是关键替换示例：

#### introduction.tex

```latex
% 原文
The second, credit-oriented layer asks whether these behavioral 
patterns, if they exist, carry incremental predictive power for 
future liquidation events...

% 修正后
The second, predictive layer asks whether these behavioral patterns, 
if they exist, carry incremental predictive power for future 
liquidation events...
```

#### research-topic.tex

```latex
% 原文
...may contain credit-relevant information that is not captured by 
point-in-time snapshots...

% 修正后
...may contain risk-relevant information that is not captured by 
point-in-time snapshots...
```

#### discussion.tex

```latex
% 原文
...whether borrower behavior contains credit-relevant information 
that could complement existing, state-based risk assessment mechanisms.

% 修正后
...whether borrower behavior contains liquidation-relevant 
information that could complement existing, state-based risk 
assessment mechanisms. We emphasize that this information pertains 
to position-level liquidation risk, not borrower-level 
creditworthiness.
```

### 新增全局声明（建议放在 Introduction）

```latex
A terminological clarification is warranted. The present study 
investigates whether protocol-observable position management 
behavior provides incremental information for predicting 
liquidation---a position-level, mechanically triggered event. We 
use ``risk-relevant information'' to describe this incremental 
predictive content, reserving ``credit'' for discussions of 
traditional credit markets and future research directions. The 
study does not claim to assess creditworthiness, improve credit 
scoring, or identify credit signals in the traditional sense.
```
