# Paper 1 六层矩阵：Definition–Construct–Measurement–Observable–Identification–Allowed Claim

**日期**：2026-08-11  
**用途**：在改写 Report v2 之前，先建立 Paper 1 每个核心概念的六层矩阵，确保构念效度（construct validity）从定义到声称的完整可追踪性  
**基线文档**：`2026-07-17_Research_Report` + `2026-08-11 定义、数据、范围更新&纠错` + `2026-08-11 区块链支付_边界约束定义_文献核对与研究修订.md`

---

## 0. 为什么要做六层矩阵

7 月 Report 的核心问题不是研究方向错了，而是 **construct validity** 不够干净：

> 你测量的变量（协议事件、HF 轨迹、主动/被动分类）到底是不是你声称的概念（信用、行为、风险）？

报告前半部分用了一些过强的修辞（"complete observability of borrower behavior"、"Credit Layer"、"credit signals"），而后半部分的 limitations 又承认了 partial observability 和 cannot infer intent。这种**前文过强、后文收回**的结构在答辩或审稿中容易被攻击。

六层矩阵的作用是：把 limitations 部分的承认**前移到定义与 claim 纪律**中，让全文的声称从一开始就与数据能支撑的边界一致。

---

## 1. 六层结构说明

每个概念都按以下六层展开：

| 层级 | 名称 | 回答的问题 |
|------|------|-----------|
| 1 | **Definition** | 这个概念在金融学/技术上的精确定义是什么？ |
| 2 | **Construct** | 我们要测量的理论构念是什么？它与定义的关系是什么？ |
| 3 | **Measurement** | 我们如何在操作上测量这个构念？具体的变量、公式、数据来源是什么？ |
| 4 | **Observable** | 从公开链上数据中，我们真正能观测到什么？可观测性等级如何？ |
| 5 | **Identification** | 我们无法识别什么？存在哪些识别挑战和混淆因素？ |
| 6 | **Allowed Claim** | 基于以上五层，我们被允许声称什么？不被允许声称什么？ |

---

## 2. 文件夹结构

```
2026-08-11_六层矩阵_Paper1/
├── 00_README.md                          ← 本文件：总览与导航
├── 01_六层矩阵总表.md                     ← 所有概念压缩到一张总表
├── 02_逐概念六层矩阵/                      ← 每个概念的完整六层展开
│   ├── 01_Collateral_抵押.md
│   ├── 02_Position_Risk_仓位风险.md
│   ├── 03_Health_Factor_健康因子.md
│   ├── 04_Distance_to_Liquidation_清算距离.md
│   ├── 05_Borrow_借款.md
│   ├── 06_Repay_还款.md
│   ├── 07_Supply_vs_CollateralEnabled_供给与抵押启用.md
│   ├── 08_Borrower_Adjustment_借款人调整行为.md
│   ├── 09_Active_vs_Passive_主动与被动分类.md
│   ├── 10_Liquidation_Eligibility_清算资格.md
│   ├── 11_Realized_Liquidation_实际清算.md
│   ├── 12_Borrower_Identity_借款人身份.md
│   └── 13_Boundary_Concepts_边界概念_Transfer_Payment_Settlement.md
├── 03_技术文档/                           ← 协议技术文档与链接
│   ├── 00_技术文档总表.md
│   ├── 01_Aave_V3.md
│   ├── 02_Compound_III.md
│   ├── 03_MakerDAO_Sky.md
│   ├── 04_Chainlink_Oracle.md
│   ├── 05_Ethereum_Finality.md
│   └── 06_Dune_Analytics.md
├── 04_文献/                               ← 文献按主题分组
│   ├── 00_文献总表.md
│   ├── 01_Blockchain_Foundation/
│   ├── 02_Collateral_Credit/
│   ├── 03_DeFi_Lending/
│   ├── 04_Alternative_Data_CreditScoring/
│   └── 05_Payment_Settlement/
├── 05_不可声称清单.md                       ← Paper 1 不能声称的内容
└── 06_术语边界对照表.md                     ← 术语之间的 ≠ 关系
```

---

## 3. 如何使用本文件夹

### 写作前检查

写任何段落前，先查对应概念的六层矩阵，确认：

1. 我现在说的是 **protocol action** 还是 **economic purpose**？
2. 我的 y 变量是 **liquidation** 还是 **credit default**？
3. 我用的 capacity 来自 **collateral** 还是 **behavior-based credit**？
4. 我的数据能不能支持这个名词？
5. 如果删掉私有数据/支付公司假设，这个句子是否还成立？

若第 5 问答案为否，该句不应出现在当前 Paper 1。

### 追溯链

每个概念文件中包含：

- 该概念对应的**技术文档链接**（`03_技术文档/`）
- 该概念对应的**文献链接**（`04_文献/`）
- 该概念的**不可声称内容**（`05_不可声称清单.md`）
- 该概念与其他概念的**边界关系**（`06_术语边界对照表.md`）

---

## 4. Paper 1 的研究边界（一句话）

> **Can protocol-observable position-management behavior provide incremental information about subsequent position distress and liquidation beyond contemporaneous collateral states?**

研究对象是 **protocol-observable position-management behavior**，不是完整的现实世界经济行为或传统信用能力。

---

## 5. 概念清单

Paper 1 的核心概念分为三类：

### A. In-Scope（当前 Paper 1 直接使用）

| # | 概念 | 文件 |
|---|------|------|
| 1 | Collateral / 抵押 | `02_逐概念六层矩阵/01_Collateral_抵押.md` |
| 2 | Position Risk / 仓位风险 | `02_逐概念六层矩阵/02_Position_Risk_仓位风险.md` |
| 3 | Health Factor / 健康因子 | `02_逐概念六层矩阵/03_Health_Factor_健康因子.md` |
| 4 | Distance to Liquidation / 清算距离 | `02_逐概念六层矩阵/04_Distance_to_Liquidation_清算距离.md` |
| 5 | Borrow / 借款 | `02_逐概念六层矩阵/05_Borrow_借款.md` |
| 6 | Repay / 还款 | `02_逐概念六层矩阵/06_Repay_还款.md` |
| 7 | Supply vs Collateral-Enabled / 供给与抵押启用 | `02_逐概念六层矩阵/07_Supply_vs_CollateralEnabled_供给与抵押启用.md` |
| 8 | Borrower Adjustment / 借款人调整行为 | `02_逐概念六层矩阵/08_Borrower_Adjustment_借款人调整行为.md` |
| 9 | Active vs Passive / 主动与被动分类 | `02_逐概念六层矩阵/09_Active_vs_Passive_主动与被动分类.md` |
| 10 | Liquidation Eligibility / 清算资格 | `02_逐概念六层矩阵/10_Liquidation_Eligibility_清算资格.md` |
| 11 | Realized Liquidation / 实际清算 | `02_逐概念六层矩阵/11_Realized_Liquidation_实际清算.md` |
| 12 | Borrower Identity / 借款人身份 | `02_逐概念六层矩阵/12_Borrower_Identity_借款人身份.md` |

### B. Boundary（定义边界，不在 Paper 1 范围内但需明确排除）

| # | 概念 | 文件 |
|---|------|------|
| 13 | Transfer / Payment / Settlement / Default / Creditworthiness | `02_逐概念六层矩阵/13_Boundary_Concepts_边界概念_Transfer_Payment_Settlement.md` |

---

## 6. 数据来源链

```
Protocol Contracts + Historical Parameters + Raw/Decoded Blockchain Data
        ↓
Researcher-built Position State (tx/block level)
        ↓
Dune / Curated Dataset Validation
        ↓
Analytical Panel (daily/monthly)
```

关键原则：**Dune 很有价值，但不应该成为最终定义来源。** 如果研究问题依赖 onBehalfOf、collateral enablement、historical liquidation threshold、contract upgrade、delegate call、state transitions，就应优先从 contracts + logs + state 自己重建。