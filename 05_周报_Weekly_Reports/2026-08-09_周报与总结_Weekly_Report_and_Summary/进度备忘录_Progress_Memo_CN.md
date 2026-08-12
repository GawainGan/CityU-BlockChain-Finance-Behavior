# 进度备忘录

**致**：乔肖老师  
**发件人**：甘翌伟 (59765200)  
**日期**：2026 年 8 月 12 日  
**主题**：Qualifying Report v1 构念效度审查——进展与下一步计划

---

## 1. 有什么新进展？取得了哪些成果？

本周我对 [Qualifying Report v1](../../04_阶段成果_Milestone_Deliverables/2026-07-17_资格报告v1_Qualifying_Report_v1/main.pdf) 完成了一次系统性的构念效度审查。这项工作的起点是我意识到自己对区块链平台机制、数据结构和关键术语的理解还不够深入，不足以支撑研究中的声称。工作产出了四项成果：

**六层矩阵约束框架。** 我构建了一个约束框架，要求每个核心概念都必须经过六个层次的检验：定义 → 构念 → 度量 → 可观测 → 识别 → 可声称范围。核心原则是：如果声称超出了数据实际可观测的范围，就构成过度声称。

我为 DeFi 借贷中的全部 13 个核心概念逐一填写了矩阵（以下路径相对于 `04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_六层矩阵_Paper1_Six_Layer_Matrix/`）：

| # | 概念 | 文件链接 |
|---|------|---------|
| 1 | Collateral（抵押） | [01_Collateral_抵押](../../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_六层矩阵_Paper1_Six_Layer_Matrix/02_逐概念六层矩阵_Per_Concept_Matrices/01_Collateral_抵押_Collateral.md) |
| 2 | Position Risk（仓位风险） | [02_Position_Risk_仓位风险](../../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_六层矩阵_Paper1_Six_Layer_Matrix/02_逐概念六层矩阵_Per_Concept_Matrices/02_Position_Risk_仓位风险_Position_Risk.md) |
| 3 | Health Factor（健康因子） | [03_Health_Factor_健康因子](../../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_六层矩阵_Paper1_Six_Layer_Matrix/02_逐概念六层矩阵_Per_Concept_Matrices/03_Health_Factor_健康因子_Health_Factor.md) |
| 4 | Distance to Liquidation（清算距离） | [04_Distance_to_Liquidation_清算距离](../../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_六层矩阵_Paper1_Six_Layer_Matrix/02_逐概念六层矩阵_Per_Concept_Matrices/04_Distance_to_Liquidation_清算距离_Distance_to_Liquidation.md) |
| 5 | Borrow（借款） | [05_Borrow_借款](../../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_六层矩阵_Paper1_Six_Layer_Matrix/02_逐概念六层矩阵_Per_Concept_Matrices/05_Borrow_借款_Borrow.md) |
| 6 | Repay（还款） | [06_Repay_还款](../../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_六层矩阵_Paper1_Six_Layer_Matrix/02_逐概念六层矩阵_Per_Concept_Matrices/06_Repay_还款_Repay.md) |
| 7 | Supply vs Collateral-Enabled（供给与抵押启用） | [07_Supply_vs_CollateralEnabled](../../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_六层矩阵_Paper1_Six_Layer_Matrix/02_逐概念六层矩阵_Per_Concept_Matrices/07_Supply_vs_CollateralEnabled_供给与抵押启用.md) |
| 8 | Borrower Adjustment（借款人调整行为） | [08_Borrower_Adjustment](../../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_六层矩阵_Paper1_Six_Layer_Matrix/02_逐概念六层矩阵_Per_Concept_Matrices/08_Borrower_Adjustment_借款人调整行为_Borrower_Adjustment.md) |
| 9 | Active vs Passive（主动与被动分类） | [09_Active_vs_Passive](../../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_六层矩阵_Paper1_Six_Layer_Matrix/02_逐概念六层矩阵_Per_Concept_Matrices/09_Active_vs_Passive_主动与被动分类_Active_vs_Passive.md) |
| 10 | Liquidation Eligibility（清算资格） | [10_Liquidation_Eligibility_清算资格](../../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_六层矩阵_Paper1_Six_Layer_Matrix/02_逐概念六层矩阵_Per_Concept_Matrices/10_Liquidation_Eligibility_清算资格_Liquidation_Eligibility.md) |
| 11 | Realized Liquidation（实际清算） | [11_Realized_Liquidation_实际清算](../../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_六层矩阵_Paper1_Six_Layer_Matrix/02_逐概念六层矩阵_Per_Concept_Matrices/11_Realized_Liquidation_实际清算_Realized_Liquidation.md) |
| 12 | Borrower Identity（借款人身份） | [12_Borrower_Identity_借款人身份](../../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_六层矩阵_Paper1_Six_Layer_Matrix/02_逐概念六层矩阵_Per_Concept_Matrices/12_Borrower_Identity_借款人身份_Borrower_Identity.md) |
| 13 | Boundary Concepts（边界概念：Transfer/Payment/Settlement） | [13_Boundary_Concepts](../../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_六层矩阵_Paper1_Six_Layer_Matrix/02_逐概念六层矩阵_Per_Concept_Matrices/13_Boundary_Concepts_边界概念_Transfer_Payment_Settlement.md) |

矩阵框架的其他组成部分：

| 文件 | 内容 |
|------|------|
| [六层矩阵总表](../../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_六层矩阵_Paper1_Six_Layer_Matrix/01_六层矩阵总表_Master_Matrix_Table.md) | 12 个在范围内概念 + 6 个边界概念的总表 |
| [不可声称清单](../../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_六层矩阵_Paper1_Six_Layer_Matrix/05_不可声称清单_Non_Claims_List.md) | 9 类不可声称（40+ 条目） |
| [术语边界对照表](../../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_六层矩阵_Paper1_Six_Layer_Matrix/06_术语边界对照表_Terminology_Boundary_Reference.md) | 术语 ≠ 对照 + 协议间映射 + 正确措辞替换 |

技术文档（7 份协议/基础设施文档 + 1 份跨协议对比）：

| # | 文档 | 链接 |
|---|------|------|
| 1 | Aave V3 协议 | [01_Aave_V3](../../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_六层矩阵_Paper1_Six_Layer_Matrix/03_技术文档_Technical_Docs/01_Aave_V3协议_Aave_V3.md) |
| 2 | Compound III 协议 | [02_Compound_III](../../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_六层矩阵_Paper1_Six_Layer_Matrix/03_技术文档_Technical_Docs/02_Compound_III协议_Compound_III.md) |
| 3 | MakerDAO / Sky | [03_MakerDAO_Sky](../../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_六层矩阵_Paper1_Six_Layer_Matrix/03_技术文档_Technical_Docs/03_MakerDAO与Sky_MakerDAO_Sky.md) |
| 4 | Chainlink 预言机 | [04_Chainlink_Oracle](../../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_六层矩阵_Paper1_Six_Layer_Matrix/03_技术文档_Technical_Docs/04_Chainlink预言机_Chainlink_Oracle.md) |
| 5 | Ethereum 最终性 | [05_Ethereum_Finality](../../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_六层矩阵_Paper1_Six_Layer_Matrix/03_技术文档_Technical_Docs/05_Ethereum最终性_Ethereum_Finality.md) |
| 6 | Dune Analytics | [06_Dune_Analytics](../../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_六层矩阵_Paper1_Six_Layer_Matrix/03_技术文档_Technical_Docs/06_Dune分析平台_Dune_Analytics.md) |
| 7 | 协议间异同对比 | [07_Cross_Protocol_Comparison](../../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_六层矩阵_Paper1_Six_Layer_Matrix/03_技术文档_Technical_Docs/07_协议间异同对比_Cross_Protocol_Comparison.md) |

文献整理覆盖 5 个主题方向，共 31 篇新增文献，详见 [文献总表](../../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_六层矩阵_Paper1_Six_Layer_Matrix/04_文献_Literature/00_文献总表_Literature_Index.md)。

**11 个问题的诊断。** 在框架的约束下，我对 Qualifying Report v1 进行了逐概念审查，发现 11 个问题，分为三类：

- **3 个技术性错误（必须修正）：**（a）HF 公式使用了 LTV 而非 Liquidation Threshold——详见 [诊断文件 01](../../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_诊断改进映射_Paper1_Diagnosis_and_Fix/02_逐问题诊断与改进_Per_Problem_Diagnosis/01_HF公式错误_LT_vs_LTV_HF_Formula_Error.md)；（b）主动/被动分类仅依赖 `msg.sender == borrower`——详见 [诊断文件 02](../../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_诊断改进映射_Paper1_Diagnosis_and_Fix/02_逐问题诊断与改进_Per_Problem_Diagnosis/02_主动被动分类_Active_vs_Passive_Classification.md)；（c）Supply 被等同于 Collateral-Enabled——详见 [诊断文件 03](../../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_诊断改进映射_Paper1_Diagnosis_and_Fix/02_逐问题诊断与改进_Per_Problem_Diagnosis/03_供给与抵押启用_Supply_vs_CollateralEnabled.md)。

- **5 个过度声称（需要降级）：**（a）"完全可观测所有借款人行为" → 降级为"完全可观测协议层面事件"——详见 [诊断文件 04](../../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_诊断改进映射_Paper1_Diagnosis_and_Fix/02_逐问题诊断与改进_Per_Problem_Diagnosis/04_完全可观测性声称_Complete_Observability_Overclaim.md)；（b）RQ2 命名为"Credit Layer" → 改为"Liquidation Propensity Layer"——详见 [诊断文件 05](../../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_诊断改进映射_Paper1_Diagnosis_and_Fix/02_逐问题诊断与改进_Per_Problem_Diagnosis/05_Credit_Layer命名_Credit_Layer_Naming_Overclaim.md)；（c）Prospect Theory 定位为"已确认的理论锚" → 降级为"有吸引力的竞争性解释"——详见 [诊断文件 06](../../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_诊断改进映射_Paper1_Diagnosis_and_Fix/02_逐问题诊断与改进_Per_Problem_Diagnosis/06_Prospect_Theory定位_PT_Positioning.md)；（d）Liquidation 与 Default 混用——详见 [诊断文件 07](../../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_诊断改进映射_Paper1_Diagnosis_and_Fix/02_逐问题诊断与改进_Per_Problem_Diagnosis/07_Liquidation_vs_Default混用_Liquidation_vs_Default.md)；（e）Collateral 与 Credit 混用——详见 [诊断文件 08](../../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_诊断改进映射_Paper1_Diagnosis_and_Fix/02_逐问题诊断与改进_Per_Problem_Diagnosis/08_Collateral_vs_Credit混用_Collateral_vs_Credit.md)。

- **3 个术语不精确（需要明确）：**（a）Settlement 不分层使用——详见 [诊断文件 09](../../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_诊断改进映射_Paper1_Diagnosis_and_Fix/02_逐问题诊断与改进_Per_Problem_Diagnosis/09_Settlement层级混淆_Settlement_Layer_Confusion.md)；（b）协议间术语直接混用——详见 [诊断文件 10](../../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_诊断改进映射_Paper1_Diagnosis_and_Fix/02_逐问题诊断与改进_Per_Problem_Diagnosis/10_协议间术语混用_Cross_Protocol_Terminology.md)；（c）"Credit-relevant information"过度使用——详见 [诊断文件 11](../../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_诊断改进映射_Paper1_Diagnosis_and_Fix/02_逐问题诊断与改进_Per_Problem_Diagnosis/11_Credit_Relevant_Information过度声称_Overclaim.md)。

11 个问题的总览详见 [问题总表](../../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_诊断改进映射_Paper1_Diagnosis_and_Fix/01_问题总表_Problem_Summary.md)。每个诊断文件包含原文引用、错误分析、六层矩阵映射、修正方案和修改后的 LaTeX 文本。

**数据可行性验证。** 我在 Dune Analytics 上逐项验证了修正后研究方案所需的全部数据是否可用。验证结果详见以下文件：

| 文件 | 内容 |
|------|------|
| [数据需求与平台映射总表](../../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_数据可行性验证_Paper1_Data_Feasibility/01_数据需求与平台映射总表_Data_Requirements_Mapping.md) | 每个研究变量所需的数据及其在 Dune 上的对应表 |
| [数据可行性评估](../../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_数据可行性验证_Paper1_Data_Feasibility/02_数据可行性评估_Feasibility_Assessment.md) | 逐项可行性判断 |
| [Dune 平台总览](../../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_数据可行性验证_Paper1_Data_Feasibility/03_Dune数据平台_Dune_Platform/01_Dune平台总览_Dune_Platform_Overview.md) | Dune 数据架构（Raw / Decoded / Curated） |
| [Aave V3 Pool 解码表](../../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_数据可行性验证_Paper1_Data_Feasibility/03_Dune数据平台_Dune_Platform/02_Aave_V3_Pool解码表_Decoded_Tables.md) | `Pool_evt_*` 事件表和字段 |
| [Aave V3 PoolConfigurator 表](../../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_数据可行性验证_Paper1_Data_Feasibility/03_Dune数据平台_Dune_Platform/03_Aave_V3_PoolConfigurator表_Configurator_Tables.md) | 参数变更事件表 |
| [Dune 辅助表](../../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_数据可行性验证_Paper1_Data_Feasibility/03_Dune数据平台_Dune_Platform/04_Dune辅助表_价格_Token_Labels_Auxiliary_Tables.md) | 价格、Token 元数据、地址标签 |
| [Dune 原始表](../../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_数据可行性验证_Paper1_Data_Feasibility/03_Dune数据平台_Dune_Platform/05_Dune原始表_Raw_Tables.md) | Raw transactions / traces |
| [数据缺口与解决方案](../../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_数据可行性验证_Paper1_Data_Feasibility/04_数据缺口与解决方案_Data_Gaps_and_Solutions.md) | 识别的数据缺口及应对方案 |
| [信息来源汇总](../../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_数据可行性验证_Paper1_Data_Feasibility/05_信息来源汇总_Information_Sources.md) | 所有信息的可追溯来源 |

验证结果：10 类协议事件均有 decoded tables，关键字段（`onBehalfOf`、`repayer` 等）数据完整，历史 LT/LTV 参数变化可通过 `CollateralConfigurationChanged` 事件追踪，Collateral 启用/禁用状态可通过 `ReserveUsedAsCollateralEnabled/Disabled` 事件追踪，HF 和 Debt 可从事件数据中重建。唯一的真正边界是借款人经济意图（链下信息，不可获取）——这是研究边界，不是数据缺口。

以上所有工作已整合为一份完整的 [修订报告](../../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_Report_v1修订报告_Revision_Report.md)（约 2,080 行），包含修改前后对比、文献变更清单和术语变更清单。早期定义纠错工作见 [定义数据范围纠错](../../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_定义数据范围纠错_Definition_Data_Scope_Corrections) 文件夹。


## 2. 我接下来想做什么？

1. **验证术语准确性。** 对六层矩阵和诊断文件中使用的所有术语进一步核对，确保与协议实际机制完全一致，消除残留的语义混淆。
2. **验证协议范围对数据需求的影响。** 当前设计以 Aave V3 为主协议，Compound/MakerDAO 分别分析。我需要确认这一范围设定是否影响研究所需数据的完整性和可得性，评估是否需要调整协议覆盖范围。
3. **文献检索与阅读。** 围绕修正后的研究问题（仓位管理行为与清算倾向），继续检索和阅读 DeFi 借贷借款人行为、清算预测、风险信号等方向的最新文献。
4. **理解预言机（Oracle）机制及其对链上货币价值的影响。** 我注意到区块链上的货币价值并非完全由链内交易决定，还依赖一个"隐形"的外部组件——预言机。预言机的职责是将外部世界的信息（如资产的市场价格）输入链上协议。以 Aave V3 为例，它使用 [Chainlink](../../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_六层矩阵_Paper1_Six_Layer_Matrix/03_技术文档_Technical_Docs/04_Chainlink预言机_Chainlink_Oracle.md) 作为价格预言机；Chainlink 从多个外部数据源聚合价格，然后提交到链上。这意味着链上协议看到的"价格"不是链内产生的，而是对外部世界的映射。如果预言机出现更新延迟、价格偏差（例如 Chainlink 的 `minAnswer`/`maxAnswer` 机制会限制极端价格的报告），或者 OEV（Oracle Extractable Value）相关机制影响清算时机和盈利性，就会直接影响协议的核心计算：HF 变化、清算触发、抵押品估值、借款额度等，进而影响借款人的支付、质押和清算行为。换句话说，预言机是"外部世界影响链上世界"的通道。我需要搞清楚的是：在我的研究中，应该将预言机视为一个需要单独建模和分析的外部因素，还是可以将链上交易（含预言机输入）作为一个整体来理解，不必拆分"外部世界对链上世界的影响"？这个问题涉及对研究边界的判断，我会先检索阅读预言机机制及其对 DeFi 协议影响的文献，再决定如何处理。

## 3. 我遇到了什么问题或困难？

- **Prospect Theory 的定位与识别困难。**

  **背景**：Prospect Theory（前景理论，Kahneman & Tversky）是行为经济学中关于人们在风险下如何做决策的理论——人不是以绝对值来评估结果，而是相对于某个"参考点"来评估；在参考点之上的收益区间人倾向于风险规避，在参考点之下的损失区间人倾向于风险追求，且损失的痛苦大于等量收益的快乐。

  **在 Report v1 中的使用**：我将 Health Factor (HF) = 1.0 作为借款人的心理参考点。理论预期是：借款人会以 HF=1.0 为锚，在 HF 接近 1.0 时行为模式发生变化——就像人会以某个财富水平为参考点一样。PT 在报告中被定位为"已确认的理论锚"，即研究的理论基石。HF 的技术细节详见 [Health Factor 概念文件](../../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_六层矩阵_Paper1_Six_Layer_Matrix/02_逐概念六层矩阵_Per_Concept_Matrices/03_Health_Factor_健康因子_Health_Factor.md) 和 [Aave V3 技术文档](../../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_六层矩阵_Paper1_Six_Layer_Matrix/03_技术文档_Technical_Docs/01_Aave_V3协议_Aave_V3.md)。

  **问题所在**：HF=1.0 不仅仅是心理参考点——它同时也是协议的机械清算阈值。当 HF 低于 1.0 时，任何清算者都可以触发清算。因此，在 HF=1.0 附近观察到的行为变化有两种可能的解释：

  - 解释 A（心理机制）：借款人感知到 HF 接近 1.0，产生风险厌恶或风险追求的行为反应（前景理论）。
  - 解释 B（机械机制）：协议规则在 HF=1.0 处产生结构性变化，借款人的行为变化是被协议强制触发的，而非心理驱动。

  这两种解释在数据中产生的观测模式是相同的（HF=1.0 处的行为不连续），我无法仅从数据中区分到底是哪种机制在起作用。因此，我将 PT 从"已确认的理论锚"降级为"有吸引力的竞争性解释"——不是因为 PT 本身有错，而是因为我无法证明行为变化是由心理机制而非机械机制导致的。详细的诊断和修正过程见 [Prospect Theory 定位诊断文件](../../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_诊断改进映射_Paper1_Diagnosis_and_Fix/02_逐问题诊断与改进_Per_Problem_Diagnosis/06_Prospect_Theory定位_PT_Positioning.md)。

  **我的困惑**：我不确定这个"降级"处理是否恰当，也不清楚是否存在更好的识别策略来区分这两种解释。

- **HF 和 Debt 的重建成本。**

  **背景**：数据可行性验证确认了所有输入数据在 Dune 上都可用（详见 [数据可行性评估](../../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_数据可行性验证_Paper1_Data_Feasibility/02_数据可行性评估_Feasibility_Assessment.md)），但"可用"不等于"可直接使用"。HF 和 Debt 在 Aave V3 中并不作为历史快照存储——协议只记录事件（Supply、Borrow、Repay、Liquidation、价格更新等）。研究者必须从这些事件中重建每个仓位在每个时间点的 HF 和 Debt 值。HF 的技术细节见 [Health Factor 概念文件](../../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_六层矩阵_Paper1_Six_Layer_Matrix/02_逐概念六层矩阵_Per_Concept_Matrices/03_Health_Factor_健康因子_Health_Factor.md)，债务重建的技术要求见 [Aave V3 技术文档 §5 利率机制](../../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_六层矩阵_Paper1_Six_Layer_Matrix/03_技术文档_Technical_Docs/01_Aave_V3协议_Aave_V3.md)。

  **困难所在**：这意味着需要处理每个仓位的全部事件历史、维护运行状态快照、处理利息累积和价格更新，并处理边缘情况（如仓位转移、EMode 切换、Isolation Mode）。计算量取决于仓位数和事件数，可能非常庞大。此外，边缘情况的错误处理（如 EMode 切换时 LT 值的突变）容易引入重建误差。这是可行的，但成本和出错风险需要认真评估。

- **协议范围的不确定性。**

  **背景**："协议范围"指的是研究覆盖哪些 DeFi 借贷协议。Report v1 原计划将 Aave、Compound 和 MakerDAO 三个协议的数据直接拼接为一个面板数据集进行分析。

  **问题所在**：这三个协议的架构有根本差异——设计目的不同（Aave 是通用流动性池，Compound III 是单一基础资产市场，MakerDAO 是稳定币发行协议），导致它们在风险指标、仓位结构、清算机制、利率机制、预言机机制上都不同。更关键的是，它们使用的"清算风险"度量本身就不在同一标尺上：Aave V3 使用 Health Factor（HF < 1 = 可清算），Compound III 使用 Account Shortfall（shortfall > 0 = 可清算），MakerDAO 使用 Collateralization Ratio。这意味着跨协议的"清算风险"概念上不可比，直接拼接不只是"可能误导"，而是**概念上不可比**——相当于把银行贷款和典当行贷款的数据放在一起分析而不加区分。

  **进一步发现**：我已将三个协议的设计目的、机制异同和对研究的影响整理为一份技术对比文档（[协议间异同对比](../../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_六层矩阵_Paper1_Six_Layer_Matrix/03_技术文档_Technical_Docs/07_协议间异同对比_Cross_Protocol_Comparison.md)）。各协议的技术细节详见 [Aave V3](../../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_六层矩阵_Paper1_Six_Layer_Matrix/03_技术文档_Technical_Docs/01_Aave_V3协议_Aave_V3.md)、[Compound III](../../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_六层矩阵_Paper1_Six_Layer_Matrix/03_技术文档_Technical_Docs/02_Compound_III协议_Compound_III.md)、[MakerDAO](../../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_六层矩阵_Paper1_Six_Layer_Matrix/03_技术文档_Technical_Docs/03_MakerDAO与Sky_MakerDAO_Sky.md)。对比发现了几个影响研究设计的结构性差异：

  - **清算机制不同**：Aave 和 Compound 是即时清算（单笔交易），MakerDAO 是拍卖制（可能持续数分钟到数小时），"清算事件"的时间定义不统一。详见各协议技术文档中的清算机制章节。
  - **PT 识别问题是 Aave 特有的**：HF=1.0 的"心理参考点 + 机械阈值"双重性质只存在于 Aave；Compound 的 Shortfall=0 和 MakerDAO 的 Ratio=LR 都是纯机械边界，没有理由认为借款人会对这些阈值产生心理锚定。因此 PT 识别问题不能通过跨协议比较来解决。
  - **外部有效性检验的含义需要重新定义**：不能将"在 Compound/MakerDAO 上也观察到类似行为模式"等同于"结果具有外部有效性"。应该关注的是"行为模式的稳健性"（在不同机制下是否仍然存在清算前的主动调整），而非"行为参数的可比性"。

  **修正方案**：改为以 Aave V3 为唯一主协议进行深度分析。Compound/MakerDAO 作为后续外部有效性检验（而非现在就投入），重点验证"行为模式的稳健性"而非"参数的一致性"。

  **剩余不确定性**：我尚未确认 Compound III 和 MakerDAO 在 Dune 上是否具有与 Aave V3 相同水平的 decoded table 可用性和事件粒度。但基于对比分析，现阶段建议先以 Aave V3 单协议推进核心分析，待核心结果出来后再评估是否有必要投入精力做外部有效性检验。

  **以上三个困难的关联**：这三个困难并非相互孤立，而是存在一条隐含的逻辑链——预言机（Oracle）的价格输入直接影响 HF 重建的准确性（如果预言机价格与市场价格存在系统性偏差，那么重建出的 HF 值本身就可能失真），而 HF 值的准确性又直接关系到 PT 识别（如果"行为变化发生在 HF=1.0 附近"这一观测受到预言机价格失真的污染，那么心理机制与机械机制之间的区分就更加困难）。换言之，Oracle → HF 重建 → PT 识别，三个问题层层依赖。这也是我下一步将 Oracle 机制列为优先研究方向的原因。

## 4. 我还需要什么反馈？

1. **六层矩阵框架的严格程度是否合适？** 它相当细致（13 个概念 × 6 层，详见 [六层矩阵总表](../../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_六层矩阵_Paper1_Six_Layer_Matrix/01_六层矩阵总表_Master_Matrix_Table.md)）。对于现阶段来说，这是过度设计，还是这个阶段所期望的构念效度审查深度？

2. **Prospect Theory 的定位。** 如上所述，我将 PT 从"已确认的理论锚"降级为"有吸引力的竞争性解释"，原因是 HF=1.0 处的行为变化无法从数据中区分是心理机制还是机械协议机制导致的。值得注意的是，Report v1 本身存在一个内部矛盾：Literature Review 中已经承认需要"careful empirical design"来区分这两种解释，但 Research Topic 和 Discussion 部分仍然把 PT 当作要"测试"和"提供证据"的对象——前后自相矛盾。详细的诊断和修正过程见 [Prospect Theory 定位诊断文件](../../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_诊断改进映射_Paper1_Diagnosis_and_Fix/02_逐问题诊断与改进_Per_Problem_Diagnosis/06_Prospect_Theory定位_PT_Positioning.md)。我想听听您的意见——这个降级是否合适？是否有更好的框架能在承认识别问题的同时保留行为洞察？或者是否有我没想到的识别策略可以区分这两种解释？

3. **协议范围。** "协议范围"指研究覆盖哪些 DeFi 借贷协议。通过对比分析（详见[协议间异同对比文档](../../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_六层矩阵_Paper1_Six_Layer_Matrix/03_技术文档_Technical_Docs/07_协议间异同对比_Cross_Protocol_Comparison.md)），我发现三个协议在风险指标标尺、清算机制、仓位结构上都不可比，且 PT 识别问题是 Aave 特有的。当前建议是以 Aave V3 为唯一主协议推进核心分析，Compound/MakerDAO 作为后续外部有效性检验。这个设计是否合理？还是说在现阶段就应该规划多协议对比？

4. **下一步的优先级。** 我计划从以下两个方向并行推进，现阶段不急于重写 Report v2：

   （a）**深化协议与数据的理解**：我需要进一步研究不同协议（[Aave V3](../../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_六层矩阵_Paper1_Six_Layer_Matrix/03_技术文档_Technical_Docs/01_Aave_V3协议_Aave_V3.md)、[Compound III](../../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_六层矩阵_Paper1_Six_Layer_Matrix/03_技术文档_Technical_Docs/02_Compound_III协议_Compound_III.md)、[MakerDAO](../../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_六层矩阵_Paper1_Six_Layer_Matrix/03_技术文档_Technical_Docs/03_MakerDAO与Sky_MakerDAO_Sky.md)）和不同数据源（[Dune Analytics](../../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_六层矩阵_Paper1_Six_Layer_Matrix/03_技术文档_Technical_Docs/06_Dune分析平台_Dune_Analytics.md) 的 decoded tables、raw tables、curated tables）的具体细节，找到它们之间到底哪个更加适合我的研究。具体来说：
   - 确认 Aave V3 在 Dune 上的数据完整性（decoded table 覆盖的事件类型、字段完整性、历史时间跨度），详见 [Aave V3 Pool 解码表](../../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_数据可行性验证_Paper1_Data_Feasibility/03_Dune数据平台_Dune_Platform/02_Aave_V3_Pool解码表_Decoded_Tables.md) 和 [PoolConfigurator 表](../../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_数据可行性验证_Paper1_Data_Feasibility/03_Dune数据平台_Dune_Platform/03_Aave_V3_PoolConfigurator表_Configurator_Tables.md)
   - 确认 Compound III 和 MakerDAO 在 Dune 上的数据可用性（是否有同等水平的 decoded table 和事件粒度），以评估外部有效性检验的可行性
   - 评估 HF/Debt 重建的工程复杂度，确定在哪个协议上先进行原型测试

   （b）**文献检索与阅读**：围绕当前的研究问题和已知困难，我需要检索以下几个方向的文献：
   - **DeFi 借贷借款人行为**：借款人在清算风险下的主动调整行为、清算前行为模式、仓位管理策略
   - **清算机制与清算预测**：DeFi 清算的实证研究、清算触发与执行的时间序列分析、清算对借款人损失的影响
   - **预言机（Oracle）机制与价格影响**：预言机延迟/偏差对协议决策的影响、Oracle Extractable Value (OEV)、预言机操纵与 DeFi 安全
   - **Prospect Theory 在金融决策中的应用**：前景理论在风险阈值附近的实证检验、参考点依赖行为、损失厌恶的识别策略
   - **构念效度与方法论**：在新型数据源（链上数据）中保证构念效度的方法、行为经济学构念在实证金融中的操作化

   相关文献整理见 [文献总表](../../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_六层矩阵_Paper1_Six_Layer_Matrix/04_文献_Literature/00_文献总表_Literature_Index.md) 和已有文献笔记（[DeFi 行为](../../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_六层矩阵_Paper1_Six_Layer_Matrix/04_文献_Literature)）。

   我想听听您的意见——这两个方向的优先级和范围是否合适？是否有我应该额外关注但遗漏的文献方向？

5. **Oracle 对研究边界的影响。** 如 Part 2 第 4 条所述，预言机是"外部世界影响链上世界"的通道。预言机的技术机制详见 [Chainlink 预言机技术文档](../../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_六层矩阵_Paper1_Six_Layer_Matrix/03_技术文档_Technical_Docs/04_Chainlink预言机_Chainlink_Oracle.md)。我的核心问题是：应该将预言机视为需要单独建模的外部因素，还是将链上交易（含预言机输入）作为整体理解？这个决定会影响研究边界定义和数据处理方式。我计划先检索阅读相关文献再做判断，但想先听听您的看法——在现阶段是否有必要将 Oracle 纳入研究框架，还是可以作为边界条件暂时搁置？

---

*所有成果均可在 GitHub 仓库中查看：https://github.com/GawainGan/CityU-BlockChain-Finance-Behavior*  
*相关文件：[周报](2026-08-09_to_2026-08-15_本周进度报告_Weekly_Progress_Report.md) ｜ [研究思路总结](研究思路总结_Research_Summary.md) ｜ [进度备忘录英文版](进度备忘录_Progress_Memo.md)*
