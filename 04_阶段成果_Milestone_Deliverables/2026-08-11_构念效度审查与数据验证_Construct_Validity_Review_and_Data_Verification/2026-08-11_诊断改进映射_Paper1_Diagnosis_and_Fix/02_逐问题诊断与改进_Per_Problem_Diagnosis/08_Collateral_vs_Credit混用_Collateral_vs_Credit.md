# 08. Collateral 与 Credit 概念混用

**严重程度**：🟡 Over-claim  
**Report 1 位置**：`sections/introduction.tex`, `sections/research-topic.tex`, `sections/discussion.tex`  
**六层矩阵文件**：`02_逐概念六层矩阵/01_Collateral_抵押.md`, `05_不可声称清单.md` §1

---

## 1. 问题描述

Report 1 将 DeFi 借贷框架为 "credit" 相关研究，使用 "credit signals"、"credit-relevant information"、"credit risk" 等术语描述一个 collateral-based（抵押基础）的借贷市场。DeFi 借贷是 collateral-secured lending（抵押担保借贷），不是 traditional credit（传统信用借贷）。Collateral ≠ Credit。

---

## 2. Report 1 原文

> **标题（main.tex Line 55）:**
>
> Risk Behavior and Credit Signals in DeFi Lending Markets: Borrower Active Adjustment Under Position Risk Accumulation

> **abstract.tex Line 3:**
>
> ...credit risk...

> **introduction.tex Line 3:**
>
> ...institutional credit assessment, relationship-based lending...

> **research-topic.tex Line 47:**
>
> ...a process-based perspective on credit risk assessment...

> **literature-review.tex Section 2.3 title:**
>
> On-Chain Credit Risk Assessment

> **discussion.tex Line 29:**
>
> ...whether borrower behavior contains credit-relevant information...

---

## 3. 错误分析

### 3.1 Collateral vs Credit

| 维度 | Collateral-based Lending (DeFi) | Credit-based Lending (Traditional) |
|------|-------------------------------|-------------------------------------|
| 信任基础 | 资产（超额抵押） | 身份 + 行为 + 信用历史 |
| 信息需求 | 抵押品价值、仓位健康度 | 借款人身份、收入、信用记录 |
| 违约处理 | 自动清算（机械性） | 法律追索、信用记录 |
| 信息不对称 | 较低（超额抵押消除大部分） | 较高（需要 screening/signaling） |
| 关键变量 | HF, LT, 抵押品价格 | 信用评分、收入、债务收入比 |

### 3.2 "Credit signals" 的问题

标题中的 "Credit Signals" 暗示本研究发现的是信用信号。但本研究实际发现的是"position management behavior provides incremental information for liquidation prediction"。这不是 credit signal，而是 position risk signal。

### 3.3 连锁影响

"Credit" 的过度使用在全文中产生连锁效应：
- 标题 → "Credit Signals"
- Abstract → "credit risk"
- Introduction → "institutional credit assessment"（对比时使用，但暗示 DeFi 是 credit market）
- Literature Review → "On-Chain Credit Risk Assessment"
- Research Topic → "credit risk assessment"
- Discussion → "credit-relevant information"

---

## 4. 六层矩阵映射

**不可声称清单**：`05_不可声称清单.md`
- §1.1: "Collateral = credit"
- §1.2: "DeFi 借贷实现了 credit market"
- §1.3: "行为过程变量度量了 creditworthiness"
- §1.4: "改进清算预测 = 改进信用评分"
- §1.5: "DeFi 行为可以替代传统信用数据"

**术语边界对照表**：`06_术语边界对照表.md`
- Collateral ≠ Credit

---

## 5. 修正方案

### 5.1 标题修正

```text
原标题：Risk Behavior and Credit Signals in DeFi Lending Markets: 
        Borrower Active Adjustment Under Position Risk Accumulation

修正后：Position Management Behavior and Liquidation Risk in DeFi 
        Lending Markets: Borrower Active Adjustment Under Position 
        Risk Accumulation

或：    Behavioral Process Variables and Liquidation Propensity in 
        DeFi Lending: Borrower Active Adjustment Under Position 
        Risk Accumulation
```

### 5.2 术语替换表

| ❌ 不应使用 | ✅ 应使用 | 出现位置 |
|-----------|---------|---------|
| "Credit Signals" (标题) | "Position Risk Signals" 或 "Behavioral Risk Indicators" | 标题 |
| "credit risk" (描述 DeFi) | "liquidation risk" 或 "position risk" | abstract, 多处 |
| "credit risk assessment" (描述本研究) | "liquidation risk prediction" | research-topic, discussion |
| "credit-relevant information" | "liquidation-relevant information" 或 "risk-relevant information" | discussion |
| "credit signals" | "position risk signals" | 标题, discussion |
| "On-Chain Credit Risk Assessment" (Lit Review 标题) | "On-Chain Risk Assessment and Predictive Modeling" | literature-review |

### 5.3 保留 "Credit" 的场景

"Credit" 一词可以在以下场景保留：
- 描述传统金融作为对比（"traditional credit markets", "institutional credit assessment"）
- 描述未来研究方向（"potential connection to credit assessment in Paper 3"）
- 描述现有文献的标题（如 Ghosh et al. 的 "On-Chain Credit Risk Score"）

### 5.4 明确声明

在 Introduction 或 Research Topic 中新增：

> "DeFi lending protocols are collateral-secured lending markets, not traditional credit markets. The distinction is important: collateral-based lending substitutes trust in assets for trust in identity, and the key risk variable is position health rather than borrower creditworthiness. While behavioral patterns observed in DeFi may eventually contribute to credit assessment frameworks (a direction explored in future research), the present study does not claim to assess creditworthiness or improve credit scoring."

---

## 6. 文献支撑

| 文献 | 与本问题的关系 |
|------|---------------|
| Ioannidou et al. (2022) | Collateral 与 asymmetric information——collateral 不只是 loss protection，也有 screening/signaling 功能 |
| Asriyan et al. (2021) | Collateral boom 导致信息生产减少——与"行为信息能否替代抵押"相关 |
| Berg et al. (2020) | Digital footprint 提供 incremental information（complement, not substitute）——Paper 1 的定位参考 |
| Cong & He (2019) | Blockchain 对 contracting 的经济意义——定义 DeFi 与传统金融的区别 |

---

## 7. 修改后的文本

### 标题修正

```latex
\title{\vspace{-1.5cm} \textbf{Position Management Behavior and 
Liquidation Risk in DeFi Lending Markets:}\\\large{Borrower Active 
Adjustment Under Position Risk Accumulation}}
```

### abstract.tex 修正

```latex
...investigates whether borrowers' active adjustments during periods 
of rising position risk provide risk information beyond that captured 
by conventional on-chain indicators such as health factor, 
collateralization ratio, and account activity...
```

（删除 "credit risk"，替换为 "risk information" 或 "liquidation risk"）

### discussion.tex 修正

```latex
...whether borrower behavior contains risk-relevant information 
that could complement existing, state-based risk assessment 
mechanisms...
```

### 新增声明（建议放在 Introduction 第一段末尾）

```latex
It is important to distinguish DeFi lending from traditional 
credit-based lending. DeFi lending protocols are 
collateral-secured lending markets: borrowers provide 
over-collateralization, and the protocol's risk management is 
based on position health rather than borrower creditworthiness. 
While behavioral patterns observed in DeFi may eventually inform 
credit assessment frameworks---a direction explored in future 
research---the present study does not claim to assess 
creditworthiness or improve credit scoring. The outcome of 
interest is liquidation, a position-level event, not credit 
default, a borrower-level outcome.
```
