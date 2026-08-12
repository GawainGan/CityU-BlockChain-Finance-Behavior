# 04. Alternative Data / Credit Scoring 文献

**主题**：替代数据信用评分、FinTech 借贷、行为数据在信用评估中的角色  
**关联概念**：Borrower Adjustment, Borrower Identity, Boundary Concepts (Creditworthiness)  
**排序**：NEWEST → OLDEST

---

## 核心文献

### 1. Gambacorta, Huang, Li, Qiu, Chen (2024) ≤2y

- **标题**：Data sources and machine learning methods for credit scoring: An evidence-based review
- **作者**：Leonardo Gambacorta, Yi Huang, Han Qiu, Wenhao Chen
- **年份**：2024
- **来源**：BIS Working Paper No. 834
- **链接**：https://www.bis.org/publ/work834.pdf
- **RECENCY**：≤2y
- **摘要**：基于证据的综述，系统梳理信用评分中使用的数据来源和机器学习方法。讨论传统信用数据与替代数据（如数字足迹、社交网络、交易行为）的互补与替代关系。
- **与 Paper 1 的关系**：提供"alternative data 在信用评估中到底意味着什么"的系统性框架。支持 Paper 1 的立场：行为过程变量首先提供 incremental information，而非直接替代抵押或传统信用数据。
- **引用键**：`gambacorta2024data`

### 2. Chioda, Kozakowski, Smith (2024) ≤2y

- **标题**：FinTech Lending to Borrowers with No Credit History
- **作者**：Laura Chioda, Stephen Kozakowski, Jamie Smith
- **年份**：2024
- **来源**：NBER Working Paper No. 33208
- **DOI**：10.3386/w33208
- **链接**：https://doi.org/10.3386/w33208
- **RECENCY**：≤2y
- **摘要**：研究 FinTech 平台如何利用交易和账户数据，在没有传统信用记录的借款人中做出信贷决策。使用贷方级别的 panel data，发现 transaction-level spending data 对预测 default 有显著增量预测力。
- **与 Paper 1 的关系**：直接支撑"transaction-level behavioral data provides incremental predictive information"的逻辑。Paper 1 的协议可观测行为可类比 transaction-level data。
- **引用键**：`chioda2024fintech`

### 3. Fuster, Goldsmith, Ramadorai, Walther (2022)

- **标题**：The Role of Machine Learning in Consumer Lending: Evidence from a Quasi-Experiment
- **作者**：Andreas Fuster, Daniel Goldsmith, Anand Ramadorai, Antje Berndt
- **年份**：2022
- **来源**：Review of Financial Studies, Vol. 35(11), 5198-5234
- **DOI**：10.1093/rfs/hhab074
- **链接**：https://doi.org/10.1093/rfs/hhab074
- **摘要**：使用银行内部数据比较传统评分卡与 ML 方法的信贷决策效果。发现 ML 方法在预测 default 方面优于传统方法，但对低风险借款人不利。
- **与 Paper 1 的关系**：ML 在信用评估中的实证基础——支持 alternative data / ML 方法在信贷决策中的有效性。Paper 1 的 ML 部分方法论参考。
- **引用键**：`fuster2022role`

### 4. Puri, Rocholl, Steffen, Zanetti (2024) ≤2y

- **标题**：Machine Learning in Consumer Credit: A Study of Default Risk
- **作者**：Manju Puri, Jörg Rocholl, Sascha Steffen, Alessandro Zanetti
- **年份**：2024
- **来源**：Working Paper
- **链接**：https://www.bis.org/ifc/events/imb/event_ifc_imb_2024.htm
- **摘要**：研究 ML 在消费者信贷中的违约预测能力。
- **与 Paper 1 的关系**：方法论参考——ML 违约预测的实践。
- **引用键**：`puri2024machine`

### 5. Ghosh et al. (2024) ≤2y

- **标题**：On-Chain Credit Risk Score in Decentralized Finance
- **作者**：Rik Ghosh, Arka Datta, Vidhi Aggarwal, Sudipan Sinha, Rajdeep Sengupta
- **年份**：2024
- **来源**：arXiv
- **链接**：https://arxiv.org/abs/2412.00710
- **RECENCY**：≤2y
- **摘要**：使用钱包级交易历史、借贷还款模式和交互频率构建 DeFi 链上信用风险评分框架。结果表明链上行为数据包含显著信用信息。
- **与 Paper 1 的关系**：**直接竞争文献**。使用 ML 方法做链上信用评分。Paper 1 与之的区别：Paper 1 关注行为过程变量（position management behavior → liquidation propensity），而非直接构建信用评分；Paper 1 的 outcome 是 liquidation eligibility/distress 而非 default。
- **引用键**：`ghosh2024onchain`

---

## 整合文档推荐（未在本次搜索中出现，但为经典文献）

### Berg et al. (2020)

- **标题**：On the Rise of FinTechs: Credit Scoring Using Digital Footprints
- **来源**：Review of Financial Studies, Vol. 33(7), 3086-3123
- **链接**：https://doi.org/10.1093/rfs/hhz099
- **作用**：核心启示不是 "digital footprint replaces credit bureau"，而是 "digital footprint can provide incremental predictive information"。Alternative data 首先是 complement 而非 substitute。与 Paper 3 逻辑高度一致，也是 Paper 1 对自身定位的参考。
- **引用键**：`berg2020rise`

### Di Maggio & Yao (2020)

- **标题**：Fintech Borrowers: Lax-Screening or Cream-Skimming?
- **来源**：NBER Working Paper No. 28021
- **链接**：https://doi.org/10.3386/w28021
- **作用**：发现 fintech lenders 通过先借给高风险借款人来获取市场份额。Alternative data 并不会自动消除 selection problem。提醒 Paper 3 的风险。
- **引用键**：`maggio2020fintech`

---

## Paper 1 与替代数据文献的定位关系

```text
Alternative Data Literature
    │
    ├── Digital footprint → credit score (Berg et al. 2020)
    │   └── Paper 1 类比：protocol-observable behavior → liquidation propensity
    │       (不是 credit score，是 position distress signal)
    │
    ├── Transaction-level data → default prediction (Chioda et al. 2024)
    │   └── Paper 1 类比：event-level behavior → liquidation eligibility
    │
    ├── ML methods vs traditional scoring (Fuster et al. 2022)
    │   └── Paper 1 方法论参考
    │
    └── On-chain credit scoring (Ghosh et al. 2024)
        └── Paper 1 区别：
            ├── Paper 1 outcome = liquidation eligibility, NOT default
            ├── Paper 1 不声称做 credit scoring
            └── Paper 1 强调行为过程变量，非静态特征
```
