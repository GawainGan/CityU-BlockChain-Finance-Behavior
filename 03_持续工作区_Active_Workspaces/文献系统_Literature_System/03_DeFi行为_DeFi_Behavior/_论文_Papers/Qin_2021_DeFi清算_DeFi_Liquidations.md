# Qin, Zhou, Gamito, Jovanovic & Gervais (2021) — An Empirical Study of DeFi Liquidations: Incentives, Risks, and Instabilities

## 基础信息

| 字段 | 内容 |
|------|------|
| **标题** | An Empirical Study of DeFi Liquidations: Incentives, Risks, and Instabilities |
| **作者** | Kaihua Qin, Liyi Zhou, Pablo Gamito, Philipp Jovanovic, Arthur Gervais |
| **年份** | 2021 |
| **期刊/会议** | ACM Internet Measurement Conference (IMC) 2021 |
| **DOI** | 10.1145/3487552.3487811 |
| **UTD 24?** | 否（但 IMC 是网络测量领域的顶级会议，CCF A 类） |
| **Tags** | `#defi-behavior` `#liquidation` |
| **作者背景** | 瑞士卢加诺大学（USI）；Arthur Gervais 是 DeFi 领域知名学者，eBZ 创始人，长期研究 DeFi 安全与行为，曾任职于 MIT、UCL |
| **Status** | 📖 精读中 |

## 研究问题

(1) DeFi 清算机制的激励机制是什么？清算人如何在不同协议（MakerDAO、Compound、Aave）之间行为？  
(2) 清算事件是否存在系统性风险（如级联清算、价格螺旋）？  
(3) 不同协议的清算机制设计（价差、拍卖、部分清算）如何影响市场稳定？

## 核心观点与方法

- **方法**：利用 2020–2021 约 1 年间的链上数据，覆盖 MakerDAO、Compound 和 Aave 三大协议，分析超过 15 万笔清算事件
- **核心发现**：
  1. **HF=1 是硬编码参考点**：所有协议的清算机制都围绕 Health Factor = 1 设计——Compound 的 `seize`、Aave 的 `LiquidationCall` 都是在 HF < 1 时触发
  2. **清算人行为高度专业化**：大量的清算通过 MEV 机器人和闪电贷执行；闪电贷使清算人无需自有资本即可参与
  3. **价格影响**：清算事件本身会加剧资产价格下行，形成"清算-价格下跌-更多清算"的级联风险
  4. **激励差异**：Compound 的全额清算可能导致借款人完全失去头寸，而 Aave 的部分清算允许借款人部分恢复

## 前景理论的相关性

本文最关键的贡献在于确认了 **HF=1 作为 DeFi 借贷中外生可观测的参考点**——这为前景理论的"参考点效应"（Reference-Point Effect）提供了天然的研究场景：

| 前景理论预测 | 与本文的关系 |
|-------------|------------|
| 参考点效应：HF=1 是关键的参考点 | 本文确认 HF=1 是硬编码的清算阈值 |
| 损失域中风险偏好翻转 | 本文未直接检验，但提供了数据基础（在 HF 接近 1 时的行为变化） |
| RDD 设计的可能性 | 根据本文数据，HF=1 的两侧是随机变异的？否——需要更细致的识别策略（见 V4_1 的接近度设计） |

## 与该研究线的关系

### Middle-Ground 关联
无关。本文不涉及 KYC/SSI/身份管理。

### DeFi-Behavior 关联（⭐⭐⭐⭐⭐）

| 本文贡献 | 对 V4 研究的意义 |
|----------|----------------|
| 确认 HF=1 是外生可观测的参考点 | 为 RQ1 的 RDD 设计提供了理论依据；Aave 的 5–10% 清算罚金是可观测的外生冲击 |
| 文档化 Aave vs Compound 的清算设计差异 | 支撑多协议对照分析；不同清算设计（价差 vs 拍卖）创造不同激励结构 |
| 闪电贷清算占比高 | 提示 RQ1 需要量化闪电贷清算的占比——如果占主导，借款人无时间进行"主动补救" |

### CVD-Credit 关联
间接。清算历史是链上信用评分的关键特征（类似于传统金融的违约记录），但本文未直接构建信用评分模型。

## "Two-Question" 评估

| 问题 | 评价 |
|------|------|
| 问题是否**有趣/重要**？ | ✅ **是**。第一次大规模实证研究 DeFi 清算机制。但注意：本文是 2021 年的数据，DeFi 市场规模和参与者在过去几年已经发生了质变。 |
| 方法是否**令人信服**？ | ✅ 链上数据覆盖全面，方法透明可复现。但数据时间范围（2020–2021）可能无法完全反映 2022 年后的市场结构变化（如 Curve 危机、Luna/UST 崩盘等系统级事件）。 |

## 关键引用

- "In total, we analyze 158,015 liquidation events across three major DeFi protocols." (p.336)
- "Liquidations are primarily conducted by a small set of professional liquidators and MEV bots." (p.346)
- "A 1% decrease in the collateral price can amplify to a 2.3% effective decrease due to cascading liquidations." (p.348)
- "Aave's partial liquidation model allows borrowers to retain some of their position after liquidation, while Compound's full liquidation is more punitive." (p.342)

## 启发 / 后续行动

### 研究启发
1. **RQ1 的核心参考点论证**：本文确认了 HF=1 是一个硬编码的外生参考点——而不是变量的或文化构建的。这极大增强了 RQ1 的 RDD 设计说服力
2. **但有一个关键限制**：本文没有检验"用户"的异质行为。它研究的是"清算事件"本身，而不是"借款人在逼近清算时的行为"
3. **方法论启发**：可以用类似的 SQL 方法提取 Aave 的清算事件序列，与 Gazinski & Liuzzi (2025) 的方法结合

### 具体下一步
- [ ] 使用本文的清算事件识别方法交叉验证 Gazinski & Liuzzi (2025) 的部分发现
- [ ] 注意控制闪电贷清算的占比（本文建议该比例较高）

## 参考文献

```bibtex
@inproceedings{Qin2021_DeFi_Liquidations_IMC,
  series = {IMC '21},
  title = {An Empirical Study of DeFi Liquidations: Incentives, Risks, and Instabilities},
  url = {http://dx.doi.org/10.1145/3487552.3487811},
  DOI = {10.1145/3487552.3487811},
  booktitle = {Proceedings of the 21st ACM Internet Measurement Conference},
  publisher = {ACM},
  author = {Qin, Kaihua and Zhou, Liyi and Gamito, Pablo and Jovanovic, Philipp and Gervais, Arthur},
  year = {2021},
  month = nov,
  pages = {336--350}
}
```
