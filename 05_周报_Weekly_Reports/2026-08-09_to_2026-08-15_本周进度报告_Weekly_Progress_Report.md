# 周报：2026-08-09 至 2026-08-15

**报告周期**：2026 年 8 月 9 日 — 2026 年 8 月 15 日  
**研究方向**：DeFi 借贷市场中的借款人行为风险与清算预测（暂定）

---

## 一、本周工作概述

本周的核心工作是：**对 Paper 1（[Qualifying Report v1](../04_阶段成果_Milestone_Deliverables/2026-07-17_资格考试报告v1_Qualifying_Report_v1/main.pdf)）进行系统性的构念效度审查，发现并修正了 11 个问题，验证了研究所需数据的可行性，并生成了完整的修订报告。**

工作起点是 8 月 9 日与内部人士的沟通（关于区块链支付困境），由此发现 [Qualifying Report v1](../04_阶段成果_Milestone_Deliverables/2026-07-17_资格考试报告v1_Qualifying_Report_v1/main.pdf) 中存在深层的语义和概念问题。随后围绕"如何让研究声称与数据能力保持一致"这一核心问题，完成了以下四项工作：

| # | 工作 | 产出 | 文件位置 |
|---|------|------|---------|
| 1 | 发现语义问题，构建约束范围 | 六层矩阵框架（13 个概念 × 6 层 + 文献 + 技术文档 + 不可声称清单 + 术语对照） | [六层矩阵_Paper1_Six_Layer_Matrix](../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_六层矩阵_Paper1_Six_Layer_Matrix) |
| 2 | 基于约束框架诊断 Report v1 问题 | 11 个问题的诊断与修正方案 | [诊断改进映射_Paper1_Diagnosis_and_Fix](../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_诊断改进映射_Paper1_Diagnosis_and_Fix) |
| 3 | 验证研究数据可行性 | Dune 平台数据可用性逐项验证 | [数据可行性验证_Paper1_Data_Feasibility](../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_数据可行性验证_Paper1_Data_Feasibility) |
| 4 | 汇总修订内容 | 完整修订报告（含修改前后对比、文献变更、术语变更） | [Report_v1修订报告_Revision_Report](../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_Report_v1修订报告_Revision_Report.md) |

---

## 二、本周工作详细说明

### 2.1 起点：与内部人士沟通中发现语义问题

8 月 9 日，在与内部人士关于区块链支付困境的沟通中，讨论了链上转账（Transfer）与支付（Payment）、结算（Settlement）之间的概念边界。这次讨论让我意识到一个更深层的问题：**Report v1 中使用的多个核心概念存在语义混淆，这种混淆不是笔误，而是系统性的构念效度问题。**

具体来说，讨论中发现的语义问题包括：

- **Collateral ≠ Credit**：DeFi 借贷是抵押担保借贷，不是传统信用借贷。Report v1 标题使用 "Credit Signals"，但实际研究的是仓位风险信号。
- **Liquidation ≠ Default**：清算（仓位级别、机械触发）不等于信用违约（借款人级别、偿付能力失败），但 Report v1 多处混用。
- **Supply ≠ Collateral-Enabled Supply**：在 Aave V3 中，存入资产和启用为抵押是两个独立操作，但 Report v1 将两者等同。
- **"完全可观测"过强**：链上数据只能观测协议事件，不能观测经济目的和链下行为。

这些问题让我意识到，需要一个系统性的框架来审查每一个概念的"声称"与"数据能力"是否一致。

### 2.2 构建"六层矩阵"约束框架

为了系统性地审查构念效度，我构建了一个"六层矩阵"框架。每个核心概念都必须经过六个层次的检验：

```
Definition（定义）→ Construct（构念）→ Measurement（度量）
→ Observable（可观测）→ Identification（识别）→ Allowed Claim（可声称范围）
```

**核心原则**：如果第 6 层的声称超出了第 4 层（可观测）能够支撑的范围，就是 over-claiming（过度声称）。

**产出内容**（路径相对于 [`04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_六层矩阵_Paper1_Six_Layer_Matrix/`](../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_六层矩阵_Paper1_Six_Layer_Matrix)）：

| 文件 | 内容 |
|------|------|
| [`00_说明_README.md`](../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_六层矩阵_Paper1_Six_Layer_Matrix/00_说明_README.md) | 框架导航与使用说明 |
| [`01_六层矩阵总表_Master_Matrix_Table.md`](../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_六层矩阵_Paper1_Six_Layer_Matrix/01_六层矩阵总表_Master_Matrix_Table.md) | 12 个在范围内概念 + 6 个边界概念的总表 |
| [`02_逐概念六层矩阵_Per_Concept_Matrices/`](../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_六层矩阵_Paper1_Six_Layer_Matrix/02_逐概念六层矩阵_Per_Concept_Matrices) | 13 个逐概念文件（Collateral, Position Risk, Health Factor, Distance to Liquidation, Borrow, Repay, Supply vs Collateral-Enabled, Borrower Adjustment, Active vs Passive, Liquidation Eligibility, Realized Liquidation, Borrower Identity, Boundary Concepts） |
| [`03_技术文档_Technical_Docs/`](../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_六层矩阵_Paper1_Six_Layer_Matrix/03_技术文档_Technical_Docs) | 7 个协议/基础设施文档（Aave V3, Compound III, MakerDAO, Chainlink, Ethereum Finality, Dune Analytics） |
| [`04_文献_Literature/`](../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_六层矩阵_Paper1_Six_Layer_Matrix/04_文献_Literature) | 5 个主题的文献整理（Blockchain Foundation, Collateral & Credit, DeFi Lending, Alternative Data & Credit Scoring, Payment & Settlement），共 31 篇新增文献 |
| [`05_不可声称清单_Non_Claims_List.md`](../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_六层矩阵_Paper1_Six_Layer_Matrix/05_不可声称清单_Non_Claims_List.md) | 9 类不可声称（40+ 条目） |
| [`06_术语边界对照表_Terminology_Boundary_Reference.md`](../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_六层矩阵_Paper1_Six_Layer_Matrix/06_术语边界对照表_Terminology_Boundary_Reference.md) | 术语 ≠ 对照 + 协议间映射 + 正确措辞替换 |

六层矩阵共约 3,900 行，确保了每个概念的每一层都有明确定义，且概念之间的边界清晰。

### 2.3 基于约束框架诊断 Report v1

在六层矩阵的约束下，我对 Report v1 进行了逐概念审查，发现了 11 个问题。按严重程度分为三类：

**🔴 技术性错误（3 个）—— 必须修正**：

| 问题 | 核心错误 | 修正方案 |
|------|---------|---------|
| HF 公式使用 LTV 而非 LT | Aave V3 的 HF 使用 Liquidation Threshold，不是 LTV。两个参数数值相近但功能不同。 | 将公式中的 LTV 替换为 LT，并说明 EMode/Isolation Mode 下的不同 LT 值 |
| 主动/被动分类仅用 msg.sender == borrower | 忽略了 onBehalfOf、Safe 多签钱包、Router 合约、自动化服务、credit delegation | 设计多层分类规则：onBehalfOf + 已知合约地址库 + trace 调用链 |
| Supply 等同于 Collateral | Aave V3 中 Supply 和 Collateral-Enabled 是独立状态 | 增加 SetUserUseReserveAsCollateral 事件追踪，区分普通 Supply 和抵押操作 |

**🟡 过度声称（5 个）—— 需要降级**：

| 问题 | 原始声称 | 修正后 |
|------|---------|--------|
| "完全可观测性" | "complete observability of all borrower actions" | "complete observability of protocol-level events" |
| RQ2 命名为 "Credit Layer" | 研究的是清算预测，不是信用评估 | 改名 "Liquidation Propensity Layer" |
| Prospect Theory 定位过强 | 定位为 "confirmed theory anchor" | 降级为 "compelling competing explanation"（HF=1.0 既是心理参考点也是机械协议不连续点，两种解释不可分离） |
| Liquidation 与 Default 混用 | 多处将 liquidation 等同于 default | 全文区分使用，新增术语声明 |
| Collateral 与 Credit 混用 | 标题 "Credit Signals"，全文使用 "credit" | 改为 "Position Management Behavior and Liquidation Risk"，保留 "credit" 仅用于传统金融对比 |

**🔵 术语不精确（3 个）—— 需要明确**：

| 问题 | 修正方案 |
|------|---------|
| Settlement 不分层使用 | 用 "repayment" 替代，或标注 Technical / Protocol / Economic 层级 |
| 协议间术语直接混用 | Aave V3 为主协议，Compound/MakerDAO 分别分析（不拼接 panel） |
| "Credit-relevant information" 反复使用 | 全文替换为 "risk-relevant information" 或 "liquidation-relevant information" |

**产出内容**：11 个逐问题诊断文件，每个包含：Report v1 原文引用 → 错误分析（含案例）→ 六层矩阵映射 → 修正方案 → 修改后的 LaTeX 文本 → 支撑文献。

### 2.4 验证研究数据可行性

在完成诊断和修正后，我意识到一个关键问题：**我们声称要使用的数据，在数据平台上是否真的可用？**

为此，我对 Dune Analytics（选定的数据平台）进行了逐项验证：

**验证方法**：
1. 从 Dune 官方文档确认数据架构（三层：Raw / Decoded / Curated）
2. 从 Dune 上的实际查询实例确认 Aave V3 的表名和字段
3. 从 Aave V3 GitHub 源码确认事件签名
4. 从 Gnosis Analytics 文档交叉验证事件签名

**验证结果**：

| 数据需求 | 可用性 | 说明 |
|---------|--------|------|
| 10 类协议事件（Supply, Borrow, Repay, LiquidationCall 等） | ✅ 全部可用 | Dune 上有 `aave_v3_ethereum.Pool_evt_*` decoded tables |
| onBehalfOf / repayer 等关键字段 | ✅ 完整 | 支持修正后的多层分类方案 |
| 历史 LT/LTV 参数变化 | ✅ 可追踪 | `PoolConfigurator_evt_CollateralConfigurationChanged` 事件 |
| Collateral 启用/禁用状态 | ✅ 可追踪 | `Pool_evt_ReserveUsedAsCollateralEnabled/Disabled` 事件 |
| EMode 状态和配置 | ✅ 可追踪 | `Pool_evt_UserEModeSet` + `PoolConfigurator_evt_EModeCategoryAdded/Updated` |
| Token 价格 | ✅ 可用 | `prices.usd` curated 表 |
| Token 元数据（decimals） | ✅ 可用 | `tokens.erc20` curated 表 |
| 交易/Trace 数据 | ✅ 可用 | `ethereum.transactions` / `ethereum.traces` |
| 地址标签 | ✅ 可用 | `labels.labels`（需补充手动合约地址列表） |
| 历史 HF 值 | ✅ 可重建 | 所有输入数据可用，需研究者编程重建 |
| 历史 Debt 值 | ✅ 可重建 | 同上 |
| 借款人经济意图 | ❌ 不可获取 | 链下信息，是研究边界（非数据缺口） |

**修正了之前技术文档中的错误**：Aave V3 的 Dune 表名前缀是 `Pool_evt_*`（不是 `LendingPool_evt_*`），collateral 启用/禁用是两个独立事件（`ReserveUsedAsCollateralEnabled/Disabled`，不是 `SetUserUseReserveAsCollateral`）。

### 2.5 生成完整修订报告

最后，我将以上所有工作整合为一份完整的修订报告（[Report_v1修订报告_Revision_Report.md](../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_Report_v1修订报告_Revision_Report.md)，约 2,080 行），包含：

1. **概述与背景**：解释构念效度问题，为非区块链金融读者提供基础概念解释
2. **问题总览**：11 个问题的分类和关系图
3. **逐问题详细说明**：每个问题用通俗语言 + 案例 + 修改前后对比 + 文献支撑
4. **文献变更清单**：31 篇新增文献 + 12 篇保留文献 + 时间梯度分布
5. **术语变更清单**：17 个删除术语 + 17 个新增术语 + 变更总结图
6. **信息来源**：所有信息的可追溯来源

---

## 三、本周产出文件汇总

所有产出文件统一放在 [2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification](../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification) 文件夹中：

```
2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/
├── 2026-08-09_老曹沟通_衍生资料_Derivative_Materials/              ← 工作起点
├── 2026-08-11_定义数据范围纠错_Definition_Data_Scope_Corrections/  ← 初步纠错包
├── 2026-08-11_六层矩阵_Paper1_Six_Layer_Matrix/                    ← 约束框架（~3,900 行）
│   ├── 00_说明_README.md
│   ├── 01_六层矩阵总表_Master_Matrix_Table.md
│   ├── 02_逐概念六层矩阵_Per_Concept_Matrices/（13 个概念文件）
│   ├── 03_技术文档_Technical_Docs/（7 个协议/平台文档）
│   ├── 04_文献_Literature/（5 个主题，31 篇文献）
│   ├── 05_不可声称清单_Non_Claims_List.md
│   └── 06_术语边界对照表_Terminology_Boundary_Reference.md
├── 2026-08-11_诊断改进映射_Paper1_Diagnosis_and_Fix/               ← 问题诊断与修正（~1,880 行）
│   ├── 00_说明_README.md
│   ├── 01_问题总表_Problem_Summary.md
│   └── 02_逐问题诊断与改进_Per_Problem_Diagnosis/（11 个问题文件）
├── 2026-08-11_数据可行性验证_Paper1_Data_Feasibility/              ← 数据可行性验证（~2,320 行）
│   ├── 00_说明_README.md
│   ├── 01_数据需求与平台映射总表_Data_Requirements_Mapping.md
│   ├── 02_数据可行性评估_Feasibility_Assessment.md
│   ├── 03_Dune数据平台_Dune_Platform/（5 个平台文档）
│   ├── 04_数据缺口与解决方案_Data_Gaps_and_Solutions.md
│   └── 05_信息来源汇总_Information_Sources.md
└── 2026-08-11_Report_v1修订报告_Revision_Report.md                 ← 完整修订报告（~2,080 行）
```

---

## 四、修订后的整体变化

| 维度 | [Qualifying Report v1](../04_阶段成果_Milestone_Deliverables/2026-07-17_资格考试报告v1_Qualifying_Report_v1/main.pdf) | 修订后 |
|------|---------|--------|
| 核心声称 | "借款人行为提供信用信号" | "协议可观测的仓位管理行为提供清算倾向的增量信息" |
| 理论定位 | Prospect Theory 是已确认的理论锚 | Prospect Theory 是有吸引力的竞争性解释（HF=1.0 既是心理参考点也是机械协议不连续点） |
| 研究结果 | Liquidation / Default 混用 | Liquidation eligibility / Realized liquidation 区分使用 |
| 可观测性 | "完全可观测" | "协议事件可观测；经济目的不可观测" |
| 协议范围 | Aave + Compound + MakerDAO 直接拼接 | Aave V3 为主，Compound/Maker 分别分析作外部有效性检验 |
| Collateral | Supply = Collateral | Supply ≠ Collateral-Enabled Supply（需追踪独立事件） |
| 主动/被动 | msg.sender == borrower | 多层分类：onBehalfOf + 已知合约地址库 + trace 调用链 |
| HF 公式 | 使用 LTV | 使用 LT（Liquidation Threshold） |

---

## 五、后续工作方向

现阶段我将继续推进以下工作：

1. **验证术语准确性**：对六层矩阵和诊断改进映射中使用的术语进行进一步核对，确保每个概念的定义、构念与协议实际机制完全一致，消除残留的语义混淆。
2. **验证协议范围对数据需求的影响**：确认当前以 Aave V3 为主、Compound/MakerDAO 分别分析的协议范围设定，是否会影响研究所需数据的完整性与可得性，评估是否需要调整协议覆盖范围。
3. **文献检索与阅读**：围绕修正后的研究问题（仓位管理行为与清算倾向），继续检索并阅读相关文献，重点补充 DeFi 借贷借款人行为、清算预测、风险信号等方向的最新研究。