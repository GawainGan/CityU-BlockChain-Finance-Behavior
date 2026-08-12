# 进度备忘录

**致**：乔肖老师  
**发件人**：甘翌伟 (59765200)  
**日期**：2026 年 8 月 12 日  
**主题**：Qualifying Report v1 构念效度审查——进展与下一步计划

---

## 1. 有什么新进展？取得了哪些成果？

本周我对 [Qualifying Report v1](../../04_阶段成果_Milestone_Deliverables/2026-07-17_资格考试报告v1_Qualifying_Report_v1/main.pdf) 完成了一次系统性的构念效度审查。这项工作的起点是我意识到自己对区块链平台机制、数据结构和关键术语的理解还不够深入，不足以支撑研究中的声称。工作产出了四项成果：

**六层矩阵约束框架（约 3,900 行）。** 我构建了一个约束框架，要求每个核心概念都必须经过六个层次的检验：定义 → 构念 → 度量 → 可观测 → 识别 → 可声称范围。核心原则是：如果声称超出了数据实际可观测的范围，就构成过度声称。我为 DeFi 借贷中的全部 13 个核心概念（Collateral, Position Risk, Health Factor, Distance to Liquidation, Borrow, Repay, Supply vs. Collateral-Enabled, Borrower Adjustment, Active vs. Passive, Liquidation Eligibility, Realized Liquidation, Borrower Identity, Boundary Concepts）逐一填写了矩阵，并整理了 7 份协议/基础设施技术文档（Aave V3, Compound III, MakerDAO, Chainlink, Ethereum Finality, Dune Analytics）以及 5 个主题方向共 31 篇新增文献。

**11 个问题的诊断。** 在框架的约束下，我对 Qualifying Report v1 进行了逐概念审查，发现 11 个问题，分为三类：

- **3 个技术性错误（必须修正）：**（a）HF 公式使用了 LTV 而非 Liquidation Threshold；（b）主动/被动分类仅依赖 `msg.sender == borrower`，忽略了 `onBehalfOf`、多签钱包、Router 合约和自动化服务；（c）Supply 被等同于 Collateral-Enabled，但两者在 Aave V3 中是独立状态。

- **5 个过度声称（需要降级）：**（a）"完全可观测所有借款人行为" → 降级为"完全可观测协议层面事件"；（b）RQ2 命名为"Credit Layer" → 改为"Liquidation Propensity Layer"；（c）Prospect Theory 定位为"已确认的理论锚" → 降级为"有吸引力的竞争性解释"（HF=1.0 既是心理参考点也是机械协议不连续点，两种解释不可分离）；（d）Liquidation 与 Default 混用 → 全文区分；（e）Collateral 与 Credit 混用 → 标题从"Credit Signals"改为"Position Management Behavior and Liquidation Risk"。

- **3 个术语不精确（需要明确）：**（a）Settlement 不分层使用；（b）协议间术语直接混用未标明差异；（c）"Credit-relevant information"过度使用 → 替换为"risk-relevant information"。

每个问题都有专门的诊断文件，包含原文引用、错误分析、六层矩阵映射、修正方案和修改后的 LaTeX 文本。

**数据可行性验证。** 我在 Dune Analytics 上逐项验证了修正后研究方案所需的全部数据是否可用：10 类协议事件均有 decoded tables，关键字段（`onBehalfOf`、`repayer` 等）数据完整，历史 LT/LTV 参数变化可通过 `CollateralConfigurationChanged` 事件追踪，Collateral 启用/禁用状态可通过 `ReserveUsedAsCollateralEnabled/Disabled` 事件追踪，HF 和 Debt 可从事件数据中重建。唯一的真正边界是借款人经济意图（链下信息，不可获取）——这是研究边界，不是数据缺口。

**完整修订报告（约 2,080 行）。** 以上所有工作被整合为一份完整的修订报告，包含修改前后对比、文献变更清单和术语变更清单。

## 2. 我接下来想做什么？

1. **验证术语准确性。** 对六层矩阵和诊断文件中使用的所有术语进一步核对，确保与协议实际机制完全一致，消除残留的语义混淆。
2. **验证协议范围对数据需求的影响。** 当前设计以 Aave V3 为主协议，Compound/MakerDAO 分别分析。我需要确认这一范围设定是否影响研究所需数据的完整性和可得性，评估是否需要调整协议覆盖范围。
3. **文献检索与阅读。** 围绕修正后的研究问题（仓位管理行为与清算倾向），继续检索和阅读 DeFi 借贷借款人行为、清算预测、风险信号等方向的最新文献。

## 3. 我遇到了什么问题或困难？

- **Prospect Theory 识别困难。** HF=1.0 既是心理参考点（符合前景理论）也是机械协议不连续点（清算阈值）。这两种解释在数据中是观测等价的——没有特殊的识别策略，我无法将它们区分开。我已将 PT 从"已确认的理论锚"降级为"有吸引力的竞争性解释"，但不确定这个处理是否正确，或者是否存在更精确的识别方法。

- **HF 和 Debt 的重建成本。** 虽然所有输入数据在 Dune 上都可用，但为每个借款人仓位重建历史 Health Factor 和 Debt 值需要大量编程工作（处理事件日志、维护状态快照、处理利息累积）。计算成本和边缘情况错误的风险（如仓位转移、EMode 切换、Isolation Mode）是实际需要关注的问题。

- **协议范围的不确定性。** 我将研究范围从"三协议直接拼接"修正为"Aave V3 为主、Compound/MakerDAO 分别分析"，但尚未确认 Compound III 和 MakerDAO 在 Dune 上是否具有与 Aave V3 相同水平的 decoded table 可用性和事件粒度。如果不具备，外部有效性检验可能受限。

## 4. 我还需要什么反馈？

1. **六层矩阵框架的严格程度是否合适？** 它相当细致（13 个概念 × 6 层）。对于资格考试报告来说，这是过度设计，还是这个阶段所期望的构念效度审查深度？

2. **Prospect Theory 的定位。** 我想听听您的意见——将 PT 降级为"有吸引力的竞争性解释"是否合适，还是说有更好的框架能在承认识别问题的同时保留行为洞察？

3. **协议范围。** 以 Aave V3 为主的设计看起来是否合理，还是说在继续推进之前我应该投入精力让 Compound III 和 MakerDAO 达到同样的深度？

4. **下一步的优先级。** 考虑到当前状态，我应该优先做（a）在 Dune 上开始数据获取和重建，（b）基于修正方案撰写 Report v2，还是（c）深化文献综述？我目前倾向于先并行推进（a）和（c），再开始（b）。

---

*所有成果均可在 GitHub 仓库中查看：https://github.com/GawainGan/CityU-BlockChain-Finance-Behavior*
