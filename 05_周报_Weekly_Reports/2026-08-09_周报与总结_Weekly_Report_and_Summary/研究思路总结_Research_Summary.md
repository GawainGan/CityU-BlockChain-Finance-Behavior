# 研究思路总结：从语义困惑到系统性验证

**日期**：2026 年 8 月 12 日。 
**研究方向**：DeFi 借贷市场中的借款人行为风险与清算预测

---

## 一、起点：语义困惑暴露了认知缺口

我在撰写 [Qualifying Report v1](../../04_阶段成果_Milestone_Deliverables/2026-07-17_资格报告v1_Qualifying_Report_v1/main.pdf) 时，使用了"Credit Signals""Liquidation""Complete Observability"等概念来描述研究问题。但在 8 月 9 日与内部人士讨论区块链支付困境时，我意识到自己对链上转账（Transfer）、支付（Payment）、结算（Settlement）之间的边界并没有清晰的认识。

这次讨论让我发现了一个更深层的问题：**我对区块链平台、协议机制和数据结构的理解还不够深入，导致我在 Qualifying Report v1 中使用的术语和概念存在系统性的语义混淆。** 这些混淆不是个别笔误，而是反映了我对底层技术细节的掌握不足以支撑研究声称。

具体来说，我发现自己在以下几个关键点上认识不清：

1. **抵押（Collateral）与信用（Credit）的边界**：DeFi 借贷是超额抵押担保，不是传统信用借贷。我把"信用信号"用在了实际研究的是仓位风险信号上，说明我对两类借贷范式的本质区别理解不够。
2. **清算（Liquidation）与违约（Default）的区别**：清算是仓位级别的机械触发，违约是借款人级别的偿付能力失败。我在报告中混用这两个概念，说明我没有区分协议机制与经济行为。
3. **供给（Supply）与抵押启用（Collateral-Enabled）的分离**：Aave V3 中存入资产和启用为抵押是两个独立操作，我之前将两者等同，说明我对协议的实际操作流程不够清楚。
4. **可观测性的边界**：我声称"完全可观测所有借款人行为"，但实际上链上数据只能观测协议事件，不能观测经济意图。这说明我对数据能力的边界缺乏清醒认识。

这些问题让我意识到：**在继续推进研究之前，我必须先搞清楚自己到底在研究什么，以及我声称要用数据是否真的可以使用。**

---

## 二、第一步：建立约束框架——六层矩阵

为了系统性地审查每个概念的"声称"与"数据能力"是否一致，我构建了一个六层矩阵框架，要求每个核心概念都必须经过六个层次的检验：

> Definition（定义）→ Construct（构念）→ Measurement（度量）→ Observable（可观测）→ Identification（识别）→ Allowed Claim（可声称范围）

核心原则是：**如果第 6 层的声称超出了第 4 层（可观测）能够支撑的范围，就是过度声称（over-claiming）。**

我围绕 DeFi 借贷中的 13 个核心概念逐一填写了这个矩阵，并为每个概念整理了对应的技术文档（Aave V3、Compound III、MakerDAO、Chainlink、Ethereum Finality、Dune Analytics）和相关文献。这一步帮助我明确了两件事：

- 每个概念在协议层面到底意味着什么；
- 每个概念能从数据中观测到什么、不能观测到什么。

详见：[六层矩阵 Paper1 Six Layer Matrix](../../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_六层矩阵_Paper1_Six_Layer_Matrix)

---

## 三、第二步：用约束框架诊断 Qualifying Report v1

在六层矩阵的约束下，我对 [Qualifying Report v1](../../04_阶段成果_Milestone_Deliverables/2026-07-17_资格报告v1_Qualifying_Report_v1/main.pdf) 进行了逐概念审查，发现了 11 个问题，分为三类：

- **3 个技术性错误**：HF 公式用 LTV 而非 LT、主动/被动分类过于简化、Supply 等同于 Collateral。这些是"我搞错了协议机制"的问题。
- **5 个过度声称**：完全可观测性、Credit Layer 命名、Prospect Theory 定位过强、Liquidation/Default 混用、Collateral/Credit 混用。这些是"我说得超出了数据能支撑的范围"的问题。
- **3 个术语不精确**：Settlement 不分层、协议间术语混用、credit-relevant information 过度使用。这些是"我用词不够严谨"的问题。

每个问题我都写了详细的诊断文件，包括原文引用、错误分析、六层矩阵映射和修正方案。

详见：[诊断改进映射 Paper1 Diagnosis and Fix](../../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_诊断改进映射_Paper1_Diagnosis_and_Fix)

---

## 四、第三步：验证数据是否真的可以使用

在完成诊断后，我意识到一个关键问题：**我声称要使用的数据，在数据平台上是否真的可用？** 如果数据不可用，那么所有的修正方案都是空谈。

因此，我对选定的数据平台 Dune Analytics 进行了逐项验证，确认：

- 10 类协议事件（Supply, Borrow, Repay, LiquidationCall 等）在 Dune 上都有对应的 decoded tables；
- 关键字段（onBehalfOf, repayer 等）数据完整，支持修正后的多层分类方案；
- 历史 LT/LTV 参数变化、Collateral 启用/禁用状态、EMode 状态等都可以追踪；
- HF 和 Debt 需要从事件中重建，但所有输入数据都可用；
- 借款人经济意图是不可获取的链下信息——这是研究边界，不是数据缺口。

验证结果让我确认了：修正后的研究方案在数据层面是可行的。

详见：[数据可行性验证 Paper1 Data Feasibility](../../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_数据可行性验证_Paper1_Data_Feasibility)

---

## 五、整体思路总结

回顾整个过程，我的思路可以概括为一条清晰的逻辑链：

```
与内部人士讨论区块链支付
    ↓
发现自己对协议、数据、概念的语义理解不够清晰
    ↓
决定先搞清楚"我到底在研究什么"——构建六层矩阵约束框架
    ↓
用框架审查 Qualifying Report v1——发现 11 个问题
    ↓
修正后追问"我要用的数据真的能用吗"——验证数据可行性
    ↓
确认数据可行，研究方案可执行——生成完整修订报告
    ↓
现阶段继续推进：验证术语准确性 → 验证协议范围是否影响数据需求 → 检索阅读文献
```

简单来说：**语义困惑让我意识到认知缺口 → 认知缺口促使我建立约束框架 → 约束框架帮我诊断和修正问题 → 修正后的方案需要验证数据可行性 → 数据验证确认研究可执行 → 现在进入持续验证与文献补充阶段。**

这个过程的本质是：**先确保"我在说什么"是准确的，再确保"我能做什么"是可行的，最后才继续推进研究本身。**