# Khadka & Das (2026) — Privacy-Preserving Compliance on Public Ledgers via Selective Disclosure Authorization Schemes

## 基础信息

| 字段 | 内容 |
|------|------|
| **标题** | Privacy-Preserving Compliance on Public Ledgers via Selective Disclosure Authorization Schemes |
| **作者** | Supriya Khadka, Sanchari Das |
| **年份** | 2026 |
| **期刊** | arXiv preprint (arXiv:2606.20760) |
| **DOI** | 10.48550/arXiv.2606.20760 |
| **UTD 24?** | 否（预印本，但作者 Ku Leuven/Digital Security Research Group 背景扎实） |
| **Tags** | `#mg` `#middle-ground` `#zkp` `#compliance` |
| **作者背景** | 作者来自比利时的 KU Leuven——密码学和安全领域的全球顶级机构，现任 COSIC 研究组的 Das 教授在认证加密和实际电子加密货币安全领域有深入工作 |
| **Status** | 📖 精读中 |

## 研究问题

公开分布式账本的透明性（所有人都能看到所有交易）与监管合规的数据最小化需求（如 FATF Travel Rule、GDPR）之间存在根本冲突。本文的核心问题是：如何利用零知识证明（ZKP）实现公开账本上的隐私保护合规性检查？

## 核心观点与方法

本文提出了一种基于 **选择性披露授权方案（Selective Disclosure Authorization Schemes, SDAS）**的方法，用于在公开账本（如以太坊）上实现隐私保护的合规性检查。

### 技术路线
- 采用零知识证明（ZKPs）——允许证明者在不同验证者（verifier）披露某个声明的情况下证明其有效性
- 提出**选择性披露授权方案（SDAS）**：用户可选择性披露合规所需信息的最小集合，同时保持其他交易细节的保密性
- 将 SDAS 部署到兼容 EVM 的链上，通过智能合约验证合规证明

### 核心贡献
1. **SDAS 构建**：界定了一种通用的选择性披露授权方案的形式化定义、安全模型和实现框架
2. **以太坊集成**：展示了 SDAS 如何应用于以太坊交易，实现符合 FATF Travel Rule 的匿名合规检查
3. **Gas 效率分析**：尽管 ZKP 证明生成成本高，但链上验证成本与标准 ERC-20 销毁相当——这使 SDAS 成为实际可行方案

## 与该研究线的关系

### Middle-Ground 关联（⭐⭐⭐⭐⭐）
本文是该研究线的核心技术同行：它直接回答了"中间地带"的核心问题——**如何在不牺牲隐私的前提下实现链上合规**。

| 本文贡献 | 对"中间地带"研究的意义 |
|----------|----------------------|
| SDAS 方案使得选择性披露在公开账本中成为可能 | 提供了"中间地带"的技术可行性论证——"选择性披露"不再是理论概念，而是在以太坊上已实现的合约功能 |
| FATF Travel Rule 的隐私合规 | 直接支撑"中间地带"主张：去中心化系统可以同时满足监管（Travel Rule）和隐私需求 |
| Gas 效率分析 | 提供了实际可行性论证——如果 ZKP 链上验证的成本可控，则"中间地带"的技术方案离现实部署更近了一步 |

### 与 Schaltt (2021) 对比
| 维度 | Schlatt (2021) | Khadka & Das (2026) |
|------|----------------|---------------------|
| 技术路线 | SSI + 选择性披露（可信执行环境） | ZKP + 选择性披露（加密证明） |
| 信任假设 | 需要第三方 Issuer | 数学证明（无信任第三方） |
| 适用场景 | 银行 KYC（传统金融） | 公开链上合规（DeFi、DEX） |
| 隐私保护程度 | 较高（选择性披露） | 最高（零知识证明） |
| 实际部署 | 两个行业案例 | 原型在以太坊测试网上部署 |

### DeFi-Behavior 关联
间接。合规层是 DeFi 协议需要集成的上层服务，本文不涉及借贷行为分析。

### CVD-Credit 关联
间接。SDAS 可以用于 V3-3/CVD 框架中的隐私保护信用评估，但本文未讨论信用场景。

## "Two-Question" 评估

| 问题 | 评价 |
|------|------|
| 问题是否**有趣/重要**？ | ✅ **是**。隐私与合规的矛盾是区块链被主流金融采用的"终极门槛"之一。本文直面这一矛盾，提出了实际可行的技术方案。 |
| 方法是否**令人信服**？ | ⚠️ 预印本阶段，需要等 peer review 结果。但技术路线（ZKP + 选择性披露）在当前密码学界是标准且稳妥的方法。两个关注点：(1) Gas 分析仅在以太坊测试网上验证，未考虑主网的实际拥堵和 Gas 波动；(2) 没有讨论 Issuer 的密钥管理问题（谁、如何颁发合规证明）。 |

## 关键引用

- "Public distributed ledgers enforce integrity through radical transparency, creating tension with data minimization principles required for regulatory compliance." (p.1)
- "We present a novel framework for privacy-preserving compliance on public ledgers by deploying selective disclosure authorization schemes." (p.2)

## 启发 / 后续行动

### 直接利用
1. **作为"中间地带"的技术先例**：Khadka & Das 提供了"选择性披露 + ZKP"在以太坊上实现合规检查的具体方案。如果我们沿着"中间地带"的路线，SDAS 可以成为一个关键的技术实现模块。
2. **与 Schaltt 的补充**：Schaltt 更侧重银行 KYC，Khadka 更侧重公开链上合规。两者构成了"中间地带"在传统金融（Schaltt）和 DeFi（Khadka）两个场景下的技术对应。

### 研究 GAP
- **SDAS 的成本问题**：Gas 效率分析显示链上验证成本较低，但证明生成成本仍然很高（需要高性能计算资源）。这个缺陷限制了 SDAS 在低价值交易中的应用
- **现实中谁做并且正在使用 SDAS？** ：目前仅在测试网上验证，没有真实世界的大规模部署

## 参考文献

```bibtex
@misc{Khadka2026_ZKP_Compliance,
  doi = {10.48550/ARXIV.2606.20760},
  url = {https://arxiv.org/abs/2606.20760},
  author = {Khadka, Supriya and Das, Sanchari},
  title = {Privacy-Preserving Compliance on Public Ledgers via Selective Disclosure Authorization Schemes},
  publisher = {arXiv},
  year = {2026},
  copyright = {Creative Commons Attribution 4.0 International}
}
```
