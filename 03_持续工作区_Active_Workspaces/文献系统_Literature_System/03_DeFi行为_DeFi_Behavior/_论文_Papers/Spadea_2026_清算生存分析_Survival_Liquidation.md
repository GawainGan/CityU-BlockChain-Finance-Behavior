# Spadea & Seneviratne (2026) — From Risk to Rescue: An Agentic Survival Analysis Framework for Liquidation Prevention

## 基础信息

| 字段 | 内容 |
|------|------|
| **标题** | From Risk to Rescue: An Agentic Survival Analysis Framework for Liquidation Prevention |
| **作者** | Fernando Spadea, Oshani Seneviratne |
| **年份** | 2026 |
| **会议** | IEEE International Conference on Blockchain and Cryptocurrency (ICBC) 2026 |
| **DOI** | 10.1109/ICBC67748.2026.11575462 |
| **UTD 24?** | 否（IEEE ICBC 是区块链领域的主流会议，CCF 暂未评级） |
| **Tags** | `#defi-behavior` `#liquidation` `#survival-analysis` |
| **作者背景** | 伦斯勒理工学院（RPI），系安全与区块链研究实验室；Seneviratne 在医疗健康应用与区块链交叉领域有多篇研究 |
| **Status** | 📖 精读中 |

## 研究问题

本文从方法论上直接与 RQ1 和 RQ2 竞争/互补：它试图回答"能否预测 DeFi 借款人将会被清算"，并用生存分析（而非行为经济学）来实现。具体而言：(1) 影响清算风险的关键链上特征是什么？(2) 如何辅助借款人避免被清算？

## 核心观点与方法

- **方法**：Cox 比例风险模型（Cox Proportional Hazards Model）+ 深度学习生存网络（DeepSurv）实现时序清算预测
- **数据**：Aave V2 和 Compound V2 上 2022–2025 年间的借贷/清算事件
- **核心发现**：
  1. **C-index = 0.79**（纯链上特征的基准模型）
  2. **加入行为特征后提升至 0.84**——这直接支撑了"行为特征包含信用预测增量信息"的假设
  3. 最强预测特征：清算历史（与 Ghosh et al. 2024一致）、持仓集中度、最近操作时间、借款金额 / 存款金额比率

### 与 RQ2 的关系

| 维度 | Spadea & Seneviratne (2026) | V4 RQ2（BDM 预测） |
|------|----------------------------|-------------------|
| 预测目标 | 清算概率 | 信用风险（超出传统指标的 BD 增量） |
| 方法 | 生存分析（Cox + DeepSurv） | BDM → 传统机器学习 |
| 行为特征 | 有限（操作时间、金额等原始特征） | 丰富（BDM 的五维度行为偏差指标） |
| 特征工程 | 特征来自专家知识 + 自动化选择 | 理论驱动的 BDM 构念操作化 |

**核心差异**：Spadea & Seneviratne 的"行为特征"是操作层面的原始特征（最近操作时间、持仓集中度），而 V4 的 BDM 是理论驱动的构念（损失厌恶度、参考点跳变度、抵押品切换方向等）。如果 BDM 的理论特征库能带来增量预测力（C-index +Δ），则 RQ2 成立。

## 与该研究线的关系

### Middle-Ground 关联
无直接关联。本文不涉及身份管理。

### DeFi-Behavior 关联（⭐⭐⭐⭐）
本文是 V4 RQ2 的最直接方法对照。

### CVD-Credit 关联
间接。本文使用的方法（清算历史作为信用特征）在传统链上信用评分中有同等角色，但 Spadea & Seneviratne 未直接构建"信用评分"。

## "Two-Question" 评估

| 问题 | 评价 |
|------|------|
| 问题是否**有趣/重要**？ | ✅ **是**。将生存分析引入 DeFi 清算预测是一个新颖的方法论贡献，而且结果令人印象深刻（C-index 从 0.79 提升到 0.84）。 |
| 方法是否**令人信服**？ | ⚠️ 部分。生存分析适合时序数据（右删失），但不考虑用户间的依赖结构（千人同一协议）。参照 0.79→0.84 的增量是否统计显著？是否做过交叉验证？另外——"行为特征"操作化太粗糙（仅为操作时间和持仓集中度），这既是我们的机会——也意味着我们需要证明 BDM 的理论驱动特征库提供更加丰富的预测效用。 |

## 关键引用

- "Our survival analysis framework achieves a C-index of 0.79 on baseline features, which increases to 0.84 when augmented with behavioral features." (p.6)
- "The single most predictive behavioral feature is the recency of user interactions with the protocol." (p.7)

## 启发 / 后续行动

### 直接利用
1. **提供了 RQ2 的基准**：Spadea & Seneviratne (2026) 的 0.84 C-index 是 RQ2 "BDM 的增量的量化基准"。如果 BDM 的增量无法超过现有的操作层面的行为特征的增量，则 RQ2 可能被替换。
2. **方法互补**：生存分析（Cox 模型）+ 传统 ML（BDM 预测）的结合可能导致比各自单独使用都强的结果。

### 一个关键的隐含假设
Spadea & Seneviratne 用 C-index 评价模型，但 C-index 对观察时间窗口的选择高度敏感（3 天、7 天、30 天或 14 天最优？）。如果他们的结果在 7 天寸尺的窗口中跳跃，需要测试稳定性。

## 参考文献

```bibtex
@inproceedings{Spadea2026_Survival_Liquidation,
  title = {From Risk to Rescue: An Agentic Survival Analysis Framework for Liquidation Prevention},
  url = {http://dx.doi.org/10.1109/icbc67748.2026.11575462},
  DOI = {10.1109/icbc67748.2026.11575462},
  booktitle = {2026 IEEE International Conference on Blockchain and Cryptocurrency (ICBC)},
  publisher = {IEEE},
  author = {Spadea, Fernando and Seneviratne, Oshani},
  year = {2026},
  month = jun,
  pages = {1--9}
}
```
