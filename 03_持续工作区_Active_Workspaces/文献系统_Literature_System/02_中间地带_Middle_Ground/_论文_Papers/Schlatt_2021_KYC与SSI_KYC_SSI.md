# Schlatt, Sedlmeir, Feulner & Urbach (2021) — Designing a Framework for Digital KYC Processes Built on Blockchain-Based Self-Sovereign Identity

## 基础信息

| 字段 | 内容 |
|------|------|
| **标题** | Designing a Framework for Digital KYC Processes Built on Blockchain-Based Self-Sovereign Identity |
| **作者** | Vincent Schlatt, Johannes Sedlmeir, Simon Feulner, Nils Urbach |
| **年份** | 2021 (published online) / 2022 (journal issue) |
| **期刊** | Information & Management, Vol. 59(7) |
| **DOI** | 10.1016/j.im.2021.103553 |
| **UTD 24?** | **是** (Information & Management 是 IS 领域权威期刊，虽非 UTD 24 但属于 ABS 3* / VHB B 级) |
| **Tags** | `#mg` `#middle-ground` |
| **机构背景** | Friedrich-Alexander-Universität Erlangen-Nürnberg (FAU), 德国; 苏黎世大学; 巴斯夫 |
| **作者背景** | 多位作者来自德国一流大学和 Fraunhofer 研究所，Urbach 是 IS 领域知名教授 (VHB 排名前列) |
| **Status** | 📖 精读中 |

## 研究问题
(1) 如何利用区块链上的自我主权身份（SSI）来解决传统 KYC 流程中的高成本、低效率和用户隐私问题？
(2) 区块链技术在 KYC 流程中的设计原则是什么？

## 核心观点与方法
- **方法**：设计科学研究 (Design Science Research, DSR) —— 这是 IS 领域核心方法论
- **主要产出**：提出了一个**基于 SSI 的区块链 KYC 框架**，包含：
  1. 一个四层的 **"SSI 生态系统架构"**——包括 Issuer, Holder, Verifier, Blockchain 四方的交互机制
  2. **7 条初生设计原则** (nascent design principles) 用于指导基于区块链的 SSI 在 KYC 中的使用
  3. 设计原则通过两个行业案例（德国银行的 KYC 流程 + 一位中型瑞士银行）进行评估

## Schalatt 框架的核心逻辑链
1. **问题**：传统 KYC 存在三个核心痛点——高成本（银行每年花费 6 亿美元+）、低效率、 
   用户隐私被过度收集（如家庭住址、收入证明等非必要信息）
2. **技术方案**：SSI + 区块链。用户持有可验证凭证 (Verifiable Credentials)，按需选择性披露（例如仅证明"年龄>18"而无需出示身份证）
3. **创新点**：本文不是第一个提出 SSI 的，但它是第一个系统性地通过 DSR 方法为 **KYC 特定场景**设计区块链-SSI 框架的文章
4. **评估**：通过专家访谈和两个真实案例进行验证

## 与该研究线的关系

### Middle-Ground 关联（⭐⭐⭐⭐⭐）
本文与该研究线**直接高度相关**——它探讨的正是"如何利用 SSI 在 KYC 中找到隐私与合规的平衡点"

| 本文贡献 | 对你"中间地带"研究的意义 |
|----------|------------------------|
| 提出了区块链 SSI 的 4 层架构 | 为"中间地带"提供了技术实现参考 |
| 总结出 7 条设计原则 | 这些可以成为你 Proposa l 的理论起点 |
| 强调选择性披露 (Selective Disclosure) | 这是你"中间地带"的具体操作机制 |

### DeFi-Behavior 关联
间接。本文不涉及 DeFi，但 SSI 机制可以延伸到链上借贷的身份验证场景。

### CVD-Credit 关联
间接。SSI 的目标是"让系统知道你是谁（在最小范围内）"，而 CVD 是"系统如何看你"——两者构成了相反视角。

## "Two-Question" 评估

| 问题 | 评价 |
|------|------|
| 问题是否**有趣/重要**？ | ✅ **是**。KYC 是银行业的核心痛点，DSR 方法使其在 IS 领域有效。但它没有（也不能）回答"最优信息披露水平是多少"这个规范性问题 —— 这正是你的机会 |
| 方法是否**令人信服**？ | ✅ DSR 方法严谨，两个案例的选择有代表性。但由于 SSI 和区块链技术发展速度极快，该框架可能已经过时需要更新（尤其是在零知识证明方面的发展） |

## 关键引用
- "KYC processes place a great burden on banks, because they are costly, inefficient, and inconvenient for customers." (p.1)
- "We demonstrate how blockchain-based self-sovereign identity (SSI) can solve the challenges of KYC."

## 对你研究的启发 / 探索建议

### 直接利用
1. **作为"中间地带"文献综述的锚点**：Schlatt 的框架可以被视为"中间地带"问题的**第一代解决方案**——用 SSI 实现了"选择性披露"。但问题是：SSI 在 DeFi/链上场景中的适配性如何？
2. **研究 gap**：Schlatt 的框架是为**传统银行 KYC** 设计的。你的创新点在于：如果把它搬到**链上/DeFi**场景，会发生什么？在去中心化环境中，谁扮演 Issuer？谁是 Verifier？信任假设如何变化？

### 理论填充
1. **信息不对称理论在 SSI 下的变形**：当用户拥有对自己凭证的完全控制时，信息不对称不是消失了，而是转化了——从银行 vs 用户的不对称，变为用户 vs 协议 vs 监管的三方博弈
2. **设计原则的可推广性**：Schlatt 的 7 条设计原则是否可以推广到 DeFi 场景？如果不能，需要增加哪些新原则？

### 拓展方向
1. 对比 Schlatt 框架和 ZKP-based 方案（如 Khadka et al. 2026）的差异
2. 你的"中间地带"需要比 SSI 更进一步——不仅实现"选择性披露"，还要动态调节披露的程度

## 参考文献

```bibtex
@article{Schlatt2021_KYC_SSI,
  title={Designing a Framework for Digital KYC Processes Built on Blockchain-Based Self-Sovereign Identity},
  volume={59},
  DOI={10.1016/j.im.2021.103553},
  number={7},
  journal={Information & Management},
  publisher={Elsevier BV},
  author={Schlatt, Vincent and Sedlmeir, Johannes and Feulner, Simon and Urbach, Nils},
  year={2022},
  pages={103553}
}
```
