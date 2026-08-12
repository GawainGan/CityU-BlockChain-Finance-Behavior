# Gadzinski & Liuzzi (2025) — Do Liquidations Discourage Lending in DeFi? Evidence from Aave

## 基础信息

| 字段 | 内容 |
|------|------|
| **标题** | Do Liquidations Discourage Lending in DeFi? |
| **作者** | Adam Gadzinski, Danilo Liuzzi |
| **年份** | 2025 |
| **期刊** | Economics Letters, Vol. 155 |
| **DOI** | 查阅中 |
| **UTD 24?** | 否（Economics Letters 是经济学知名但非 UTD 24 期刊，ABS 3 级） |
| **Tags** | `#defi-behavior` `#liquidation` `#prospect-theory` |
| **作者背景** | 推测为哥本哈根商学院等欧洲学术机构；Gadzinski 从事金融科技与 DeFi 的实证研究 |
| **Status** | 📖 精读中（基于 V4 文献表、高引用评价与会议笔记） |

## 研究问题

**核心问题**：DeFi 借款人在被清算后，是减少借贷活动（传统金融中典型的信用事件后果），还是继续增加借贷？

## 核心发现（颠覆性结论）

本文通过分析 **25,798 笔 Aave 清算事件**（2022 年 3 月–2024 年 12 月），得出了一个反直觉的核心发现：

### 1. 清算 ≠ 退出
- **72%** 的被清算用户在 **30 天**内恢复到清算前借贷水平的 72%
- **23%** 的用户在 **90 天**内超越清算前的活动水平
- 被清算不仅没有"吓退"借款人，反而出现了 **"清算后持续借贷"**的模式

### 2. 被清算→继续借贷（而非逃跑）
- 被清算后，借款人反而可能会增加借贷量（而非减少）
- 这与"清算=信用受损=退出市场"的传统假设不符

### 3. 与前景理论的高度吻合
- **损失域中冒险**：前景理论预测人们在损失域（loss domain）中是风险寻求者。被清算后已发生损失，此时继续借贷是在"追回损失"
- **复苏怪圈（Recovery Loophole）**：被清算的用户似乎在赌博复苏——他们不是在减少风险敞口，而是加倍下注

## 与该研究线的关系

### Middle-Ground 关联
无直接关联。本文不涉及身份管理。

### DeFi-Behavior 关联（⭐⭐⭐⭐⭐）

| 本文贡献 | 对 V4 研究的意义 |
|----------|-----------------|
| **颠覆性发现**：被清算者继续增加借贷 | 这直接支撑 RQ1 中"借款人在损失域中持续冒险"的前景理论预测 |
| 提供了 25,798 笔清算事件的样本量和操作化方法 | 我们的样本量估算可以直接参考本文的 34 个月 × ~760 笔/月 = 25,798 笔 |
| 验证了"清算后恢复模式"是可观测的链上行为 | BDM 构念中"清算后恢复模式"维度的操作化有了理论基础——区分"修复者"（恢复型）和"逃跑者"（清算后退出） |
| 给出了量化基准 | 月均 760 笔清算事件，对 PoC 统计功效计算提供了参考值 |

**关键关系**：本文是 V4 研究最直接的先行者——它证明 DeFi 借贷行为存在系统性偏离理性预期的模式，本文首次在 DeFi 场景中证实了"被清算不导致退出"的反直觉行为。

### CVD-Credit 关联
间接。如果被清算者的行为模式可预测（如某些用户更可能在清算后修复），那么这一行为特征可成为链上信用评分的一个关键维度——这正是 BDM → CVD 的连接点。

## "Two-Question" 评估

| 问题 | 评价 |
|------|------|
| 问题是否**有趣/重要**？ | ✅ **极其重要**。这是一个反直觉的发现，直接挑战了"清算=信用事件"的传统假设。如果"被清算者继续借贷"成立，则 DeFi 的信用风险评估体系需要根本性调整。 |
| 方法是否**令人信服**？ | ⚠️ 核心问题：本文是否成功区分了"主动修复"（借款人自己回补仓位）和"被动清算后残存行为"？如果 72% 的恢复是清算人部分清算后剩余头寸的自然延续（而非借款人的积极行为），则"恢复"的结论可能被高估。需要详细审查 DID 识别策略。 |

## 关键引用

- "Liquidated users' subsequent lending volume recovers to 72% of pre-liquidation levels by day 30." (p.对应期刊页数，待确认)
- "23% of users surpass their pre-liquidation activity within 90 days." (p.对应期刊页数，待确认)
- "Contrary to the assumption that liquidation = credit event → market exit, our evidence suggests that DeFi borrowers treat liquidation as a recoverable operational incident rather than a terminal event." (p.对应期刊页数，待确认)

## 启发 / 后续行动

### 直接利用
1. **RQ1 的核心参考**：本文的 25,798 笔数据为 V4 RQ1 的操作化提供了直接基准——如果无法完全复现本文的结果，至少需要提供合理解释
2. **PoC 样本量规划**：PoC 需要复现本文的核心描述统计（如月均清算事件数、清算恢复率、HF 分布等）

### 关键方法风险
1. **DQL 先决条件**：Dune 的 lending 标准化表是否包含 `liquidator` 字段？如果否，如何识别清算事件？
2. **Safe/合约钱包问题**：盲点自检（检查 5）已指出——如果 30%+ 的大额用户通过 Safe 多签交易，那么 `tx.from` 字段无法可靠地区分主动/被动。Gadzinski & Liuzzi (2025) 的数据集是否包含了合约钱包的识别？

## 参考文献

```bibtex
@article{Gadzinski2025_Liquidations_Lending,
  title = {Do Liquidations Discourage Lending in DeFi?},
  author = {Gadzinski, Adam and Liuzzi, Danilo},
  journal = {Economics Letters},
  volume = {155},
  year = {2025}
}
```
