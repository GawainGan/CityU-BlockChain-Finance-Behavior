# 进度备忘录

**致**：乔肖老师  
**发件人**：甘翌伟 (59765200)  
**日期**：2026 年 8 月 12 日  
**主题**：Qualifying Report v1 构念效度审查——进展与下一步计划

---

## 1. 有什么新进展？取得了哪些成果？

本周我对 [Qualifying Report v1](../../04_阶段成果_Milestone_Deliverables/2026-07-17_资格考试报告v1_Qualifying_Report_v1/main.pdf) 完成了一次系统性的构念效度审查。这项工作的起点是我意识到自己对区块链平台机制、数据结构和关键术语的理解还不够深入，不足以支撑研究中的声称。工作产出了四项成果：

**六层矩阵约束框架。** 我构建了一个约束框架，要求每个核心概念都必须经过六个层次的检验：定义 → 构念 → 度量 → 可观测 → 识别 → 可声称范围。核心原则是：如果声称超出了数据实际可观测的范围，就构成过度声称。我为 DeFi 借贷中的全部 13 个核心概念（Collateral, Position Risk, Health Factor, Distance to Liquidation, Borrow, Repay, Supply vs. Collateral-Enabled, Borrower Adjustment, Active vs. Passive, Liquidation Eligibility, Realized Liquidation, Borrower Identity, Boundary Concepts）逐一填写了矩阵，并整理了 7 份协议/基础设施技术文档（Aave V3, Compound III, MakerDAO, Chainlink, Ethereum Finality, Dune Analytics）以及 5 个主题方向共 31 篇新增文献。

**11 个问题的诊断。** 在框架的约束下，我对 Qualifying Report v1 进行了逐概念审查，发现 11 个问题，分为三类：

- **3 个技术性错误（必须修正）：**（a）HF 公式使用了 LTV 而非 Liquidation Threshold；（b）主动/被动分类仅依赖 `msg.sender == borrower`，忽略了 `onBehalfOf`、多签钱包、Router 合约和自动化服务；（c）Supply 被等同于 Collateral-Enabled，但两者在 Aave V3 中是独立状态。

- **5 个过度声称（需要降级）：**（a）"完全可观测所有借款人行为" → 降级为"完全可观测协议层面事件"；（b）RQ2 命名为"Credit Layer" → 改为"Liquidation Propensity Layer"；（c）Prospect Theory 定位为"已确认的理论锚" → 降级为"有吸引力的竞争性解释"（HF=1.0 既是心理参考点也是机械协议不连续点，两种解释不可分离）；（d）Liquidation 与 Default 混用 → 全文区分；（e）Collateral 与 Credit 混用 → 标题从"Credit Signals"改为"Position Management Behavior and Liquidation Risk"。

- **3 个术语不精确（需要明确）：**（a）Settlement 不分层使用；（b）协议间术语直接混用未标明差异；（c）"Credit-relevant information"过度使用 → 替换为"risk-relevant information"。

每个问题都有专门的诊断文件，包含原文引用、错误分析、六层矩阵映射、修正方案和修改后的 LaTeX 文本。

**数据可行性验证。** 我在 Dune Analytics 上逐项验证了修正后研究方案所需的全部数据是否可用：10 类协议事件均有 decoded tables，关键字段（`onBehalfOf`、`repayer` 等）数据完整，历史 LT/LTV 参数变化可通过 `CollateralConfigurationChanged` 事件追踪，Collateral 启用/禁用状态可通过 `ReserveUsedAsCollateralEnabled/Disabled` 事件追踪，HF 和 Debt 可从事件数据中重建。唯一的真正边界是借款人经济意图（链下信息，不可获取）——这是研究边界，不是数据缺口。


## 2. 我接下来想做什么？

1. **验证术语准确性。** 对六层矩阵和诊断文件中使用的所有术语进一步核对，确保与协议实际机制完全一致，消除残留的语义混淆。
2. **验证协议范围对数据需求的影响。** 当前设计以 Aave V3 为主协议，Compound/MakerDAO 分别分析。我需要确认这一范围设定是否影响研究所需数据的完整性和可得性，评估是否需要调整协议覆盖范围。
3. **文献检索与阅读。** 围绕修正后的研究问题（仓位管理行为与清算倾向），继续检索和阅读 DeFi 借贷借款人行为、清算预测、风险信号等方向的最新文献。

## 3. 我遇到了什么问题或困难？

- **Prospect Theory 的定位与识别困难。**

  **背景**：Prospect Theory（前景理论，Kahneman & Tversky）是行为经济学中关于人们在风险下如何做决策的理论——人不是以绝对值来评估结果，而是相对于某个"参考点"来评估；在参考点之上的收益区间人倾向于风险规避，在参考点之下的损失区间人倾向于风险追求，且损失的痛苦大于等量收益的快乐。

  **在 Report v1 中的使用**：我将 Health Factor (HF) = 1.0 作为借款人的心理参考点。理论预期是：借款人会以 HF=1.0 为锚，在 HF 接近 1.0 时行为模式发生变化——就像人会以某个财富水平为参考点一样。PT 在报告中被定位为"已确认的理论锚"，即研究的理论基石。

  **问题所在**：HF=1.0 不仅仅是心理参考点——它同时也是协议的机械清算阈值。当 HF 低于 1.0 时，任何清算者都可以触发清算。因此，在 HF=1.0 附近观察到的行为变化有两种可能的解释：

  - 解释 A（心理机制）：借款人感知到 HF 接近 1.0，产生风险厌恶或风险追求的行为反应（前景理论）。
  - 解释 B（机械机制）：协议规则在 HF=1.0 处产生结构性变化，借款人的行为变化是被协议强制触发的，而非心理驱动。

  这两种解释在数据中产生的观测模式是相同的（HF=1.0 处的行为不连续），我无法仅从数据中区分到底是哪种机制在起作用。因此，我将 PT 从"已确认的理论锚"降级为"有吸引力的竞争性解释"——不是因为 PT 本身有错，而是因为我无法证明行为变化是由心理机制而非机械机制导致的。

  **我的困惑**：我不确定这个"降级"处理是否恰当，也不清楚是否存在更好的识别策略来区分这两种解释。

- **HF 和 Debt 的重建成本。**

  **背景**：数据可行性验证确认了所有输入数据在 Dune 上都可用，但"可用"不等于"可直接使用"。HF 和 Debt 在 Aave V3 中并不作为历史快照存储——协议只记录事件（Supply、Borrow、Repay、Liquidation、价格更新等），研究者必须从这些事件中重建每个仓位在每个时间点的 HF 和 Debt 值。

  **困难所在**：这意味着需要处理每个仓位的全部事件历史、维护运行状态快照、处理利息累积和价格更新，并处理边缘情况（如仓位转移、EMode 切换、Isolation Mode）。计算量取决于仓位数和事件数，可能非常庞大。此外，边缘情况的错误处理（如 EMode 切换时 LT 值的突变）容易引入重建误差。这是可行的，但成本和出错风险需要认真评估。

- **协议范围的不确定性。**

  **背景**："协议范围"指的是研究覆盖哪些 DeFi 借贷协议。Report v1 原计划将 Aave、Compound 和 MakerDAO 三个协议的数据直接拼接为一个面板数据集进行分析。

  **问题所在**：这三个协议的架构有根本差异——事件结构不同、风险参数不同、抵押和清算的处理方式不同。将它们视为同一事物直接拼接，可能会产生误导性结果（相当于把银行贷款和典当行贷款的数据放在一起分析而不加区分）。

  **修正方案**：改为以 Aave V3 为主协议，Compound/MakerDAO 分别单独分析，作为外部有效性检验（而不是拼接在一起）。

  **剩余不确定性**：我尚未确认 Compound III 和 MakerDAO 在 Dune 上是否具有与 Aave V3 相同水平的 decoded table 可用性和事件粒度。如果不具备，外部有效性检验可能受限。

## 4. 我还需要什么反馈？

1. **六层矩阵框架的严格程度是否合适？** 它相当细致（13 个概念 × 6 层）。对于现阶段来说，这是过度设计，还是这个阶段所期望的构念效度审查深度？

2. **Prospect Theory 的定位。** 如上所述，我将 PT 从"已确认的理论锚"降级为"有吸引力的竞争性解释"，原因是 HF=1.0 处的行为变化无法从数据中区分是心理机制还是机械协议机制导致的。我想听听您的意见——这个降级是否合适？是否有更好的框架能在承认识别问题的同时保留行为洞察？或者是否有我没想到的识别策略可以区分这两种解释？

3. **协议范围。** "协议范围"指研究覆盖哪些 DeFi 借贷协议。当前设计以 Aave V3 为主、Compound/MakerDAO 分别分析。这个设计是否合理？还是说在继续推进之前我应该投入精力让 Compound III 和 MakerDAO 达到同样的深度？但这个探究需要进行深度的信息匹配，会非常花时间。

4. **下一步的优先级。** 考虑到当前状态，我应该优先做（a）在 Dune 上开始数据获取和重建，（b）基于修正方案撰写 Report v2，还是（c）深化文献综述？我目前倾向于先并行推进（a）和（c），再开始（b）。

---

*所有成果均可在 GitHub 仓库中查看：https://github.com/GawainGan/CityU-BlockChain-Finance-Behavior*