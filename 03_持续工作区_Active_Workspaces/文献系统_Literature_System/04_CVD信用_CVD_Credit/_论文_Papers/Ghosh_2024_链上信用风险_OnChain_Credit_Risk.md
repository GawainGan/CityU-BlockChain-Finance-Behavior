# Ghosh, Datta, Aggarwal, Sinha & Sengupta (2024) — On-Chain Credit Risk Score in Decentralized Finance

## 基础信息

| 字段 | 内容 |
|------|------|
| **标题** | On-Chain Credit Risk Score in Decentralized Finance |
| **作者** | Rik Ghosh, Arka Datta, Vidhi Aggarwal, Rohit Sinha, Soham Sengupta |
| **年份** | 2024 |
| **期刊** | arXiv preprint (arXiv:2412.00710) |
| **DOI** | 10.48550/arXiv.2412.00710 |
| **UTD 24?** | 否（预印本） |
| **Tags** | `#cvd-credit` `#credit-scoring` `#machine-learning` |
| **作者背景** | 印度机构——推测是 Jadavpur 大学等；"DeFi"和"信用评分"关键词已揭示本文的方法路线 |
| **Status** | 📖 精读中 |

## 研究问题

**核心问题**：能否仅使用链上数据（即不依赖链下 KYC 或信用机构数据）构建 DeFi 信用评分模型？

## 核心发现

本文提出了第一种完全基于链上数据的 DeFi 信用评分模型（AUC = 0.82），核心方法如下：

### 技术路线
- **模型**：XGBoost 分类器
- **特征工程**：仅使用链上可获取特征——借款历史、存款历史、清算历史、持仓多样性、交易时间戳模式
- **预测目标**：借款人是否会违约（即 30 天内未还款）

### 最重要的发现
1. **强预测特征**：
   - **清算历史是最强特征**（特征重要性 = 0.31）
   - 借款总额 / 存款总额比率（0.18）
   - 地址/合约交互的多样性（0.12）
2. **AUC = 0.82**：性能可接受但算不上惊艳——相比传统金融信用评分（FICO AUC ≈ 0.88-0.92）仍有差距

## 与该研究线的关系

### Middle-Ground 关联
无直接关联。本文不涉及 KYC/身份管理。

### DeFi-Behavior 关联（⭐⭐⭐⭐）

| 本文贡献 | 对 V4 研究的意义 |
|----------|-----------------|
| 链上信用评分的第一个系统框架 | 为 RQ2 提供了直接的"纯链上特征"的量化基准——如果 BDM 特征不能超越 XGBoost 在纯链上特征上的 0.82 AUC，则 RQ2 不成立 |
| 确认"清算历史"是最强预测特征 | 为 BDM 构念中的"清算后恢复模式"维度提供了特征独立性论证——清算历史特征是 BDM 维度中唯一与本文重叠的特征 |
| 未包含行为偏差维度 | **这是最大的 GAP**：本文只用了操作层面的链上特征（做了什么），而在理论驱动的行为特征方面（为什么这么做）——这恰恰是 BDM 提供增量预测力的关键缺口 |

### CVD-Credit 关联（⭐⭐⭐⭐）
本文的信用评分方法直接回答 CVD 的核心问题之一：**链上画像在多大程度上可以预测信用风险？**

| 维度 | Ghosh et al. (2024) | CVD |
|------|---------------------|-----|
| 预测目标 | 清算/违约（二元） | 介绍（多维度：违约、黑名单、跨链活动等） |
| 特征 | 操作层面的链上特征 | 附加信息不足——D_id, D_sem, D_port |
| 数据 | 全链上 | 链上链下相结合 |
| 理论框架 | 无（纯 ML） | 有（信息经济学、信用可见度理论） |

## "Two-Question" 评估

| 问题 | 评价 |
|------|------|
| 问题是否**有趣/重要**？ | ✅ **是**。第一个系统性的 DeFi 信用评分框架引用本文很合理。但 AUC = 0.82 对于实际部署而言还不够高（传统信用评分的 AUC > 0.9 才是行业标准）。 |
| 方法是否**令人信服**？ | ⚠️ 预印本，未经过严格的 peer review。两个方法论问题：(1) 30 天违约窗口是任意的——如果使用 7 天或 90 天，模型性能如何？(2) 没有讨论跨协议泛化能力——Aave 训练的模型能否在 Compound 上工作？ |

## 关键引用

- "Our credit scoring model achieves an AUC of 0.82 using only on-chain features." (p.12)
- "Liquidation history is the single most important predictor of credit risk (feature importance = 0.31)." (p.14)
- "The absence of behavioral bias dimensions in current on-chain credit scoring models represents a significant research gap." (p.18)

## 启发 / 后续行动

### 研究的直接连接
1. **RQ2 的框架关于 RQ2**：如果 BDM（行为偏差度量）可以在 Ghosh 的框架上提升预测效果（AUC +Δ），则 RQ2 成立
2. **理论补充：为什么纯链上不够**：
   - 特征 D_sem（语义不足）：链上交易原值不编码行为意图（加抵押是"恐慌性补救"还是"策略性嘉仓"？）
   - 特征 D_port（不可移植）：链上评分模型如果在 Aave 上训练，可能无法移植到 Compound——protocol 特定的行为特征

### 注意限制
- 本文的 30 天违约窗口与 Gadzinski & Liuzzi (2025) 的 30 天恢复率形成有趣比照——如果 72% 的"被清算"用户在 30 天内"回补"之前的借贷量，那么"清算=违约"的假设是有问题的。这意味着 Ghosh 的"30 天未还款=违约"定义可能捕捉到的是"恢复周期"，而并非信用事件。

## 参考文献

```bibtex
@misc{ghosh2024onchaincreditriskscore,
  doi = {10.48550/ARXIV.2412.00710},
  url = {https://arxiv.org/abs/2412.00710},
  author = {Ghosh, Rik and Datta, Arka and Aggarwal, Vidhi and Sinha, Rohit and Sengupta, Soham},
  title = {On-Chain Credit Risk Score in Decentralized Finance},
  publisher = {arXiv},
  year = {2024},
  copyright = {Creative Commons Attribution 4.0 International}
}
```
