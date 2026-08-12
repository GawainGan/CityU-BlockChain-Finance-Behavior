# 03. DeFi Lending 文献

**主题**：DeFi 借贷、清算机制、风险管理  
**关联概念**：Position Risk, Health Factor, Distance to Liquidation, Borrow, Repay, Borrower Adjustment, Active vs Passive, Liquidation Eligibility, Realized Liquidation  
**排序**：NEWEST → OLDEST

---

## 核心文献

### 1. Sadeghi & Feinstein (2026) ★newest

- **标题**：Liquidation Dynamics in DeFi and the Role of Transaction Fees
- **作者**：Agathe Sadeghi, Zachary Feinstein
- **年份**：2026
- **来源**：arXiv
- **链接**：https://arxiv.org/pdf/2602.12104
- **RECENCY**：≤6mo ★newest
- **摘要**：研究 DeFi 借贷中抵押品清算的动态，以及交易费对清算机制的影响。清算机制暴露协议面临 predatory price manipulation 风险。
- **与 Paper 1 的关系**：直接涉及 Realized Liquidation 的执行摩擦——transaction fees 影响 liquidation 是否发生。支持 Liquidation Eligibility vs Realized Liquidation 的区分。
- **引用键**：`sadeghi2026liquidation`

### 2. Campello, Gallo, Mota, Terracciano (2026) ★newest

- **标题**：Demand for Safety in the Crypto Ecosystem
- **作者**：Murillo Campello, Angela Gallo, Lira Mota, Tammaro Terracciano
- **年份**：2026
- **来源**：NBER Working Paper
- **DOI**：10.3386/w35557
- **链接**：https://doi.org/10.3386/w35557
- **RECENCY**：≤6mo ★newest
- **摘要**：研究加密生态系统中的安全性和流动性需求，在稳定币存款和借贷池之间分配。
- **与 Paper 1 的关系**：提供 DeFi 借贷市场的宏观背景。
- **引用键**：`campello2026demand`

### 3. Wu (2026) ★newest

- **标题**：Tokens All the Way Down: A Money View of Decentralized Finance
- **作者**：Wenbin Wu
- **年份**：2026
- **来源**：arXiv
- **链接**：https://arxiv.org/pdf/2603.01803
- **RECENCY**：≤6mo ★newest
- **摘要**：从货币视角分析 DeFi 中通过 token 产生的类似银行的多层信用创造结构。
- **与 Paper 1 的关系**：理解 DeFi 借贷在更广泛金融结构中的位置。
- **引用键**：`wu2026tokens`

### 4. Sevim (2026) ★newest

- **标题**：Interoperability Effects: Extending DeFi Lending Risk Models to Multi-Chain Environments
- **作者**：Hasret Ozan Sevim
- **年份**：2026
- **来源**：arXiv
- **链接**：https://arxiv.org/abs/2605.12508
- **RECENCY**：≤6mo ★newest
- **摘要**：将 DeFi 借贷风险模型扩展到多链环境，识别跨链互操作性引入的新风险类别。
- **与 Paper 1 的关系**：跨链风险——Paper 1 限定在 Ethereum mainnet，但需了解多链风险背景。
- **引用键**：`sevim2026interoperability`

### 5. Oberholzer & Zamaraiev (2026) ★newest

- **标题**：Toward a Risk Assessment Framework for Institutional DeFi: A Nine-Dimension Approach
- **作者**：Eva Oberholzer, Valeriy Zamaraiev
- **年份**：2026
- **来源**：arXiv
- **链接**：https://arxiv.org/abs/2605.05145
- **RECENCY**：≤6mo ★newest
- **摘要**：提出面向机构 DeFi 的九维风险评估框架，涵盖 counterparty, market, liquidity, operational, governance, legal, regulatory, smart contract, oracle 风险。
- **与 Paper 1 的关系**：提供协议级风险背景，但 Paper 1 关注 borrower-level 行为。
- **引用键**：`oberholzer2026toward`

### 6. Bartoletti & Lipparini (2025) ≤1.5y

- **标题**：A theory of Lending Protocols in DeFi
- **作者**：Massimo Bartoletti, Enrico Lipparini
- **年份**：2025
- **来源**：arXiv
- **链接**：https://arxiv.org/abs/2506.15295
- **RECENCY**：≤1.5y
- **摘要**：DeFi 借贷协议的形式化理论。
- **与 Paper 1 的关系**：提供 DeFi 借贷的理论基础。
- **引用键**：`bartoletti2025theory`

### 7. Iftikhar, Wei, Cartlidge (2025) ≤1.5y

- **标题**：Automated Risk Management Mechanisms in DeFi Lending Protocols: A Crosschain Comparative Analysis of Aave and Compound
- **作者**：Erum Iftikhar, Wei Wei, John Cartlidge
- **年份**：2025
- **来源**：arXiv / IEEE BRAINS 2025
- **DOI**：10.1109/brains67003.2025.11302928
- **链接**：https://arxiv.org/abs/2506.12855
- **RECENCY**：≤1.5y
- **摘要**：Aave 和 Compound 的自动化风险管理机制的跨链比较分析，突出两个协议在参数调整和清算执行方面的差异。
- **与 Paper 1 的关系**：直接支撑 Aave/Compound 机制差异的分析。Distance to Liquidation 需要考虑协议差异。
- **引用键**：`iftikhar2025automated`

### 8. Chitra (2025) ≤1.5y

- **标题**：A Curationary Tale: Logarithmic Regret in DeFi Lending via Dynamic Pricing
- **作者**：Tarun Chitra
- **年份**：2025
- **来源**：arXiv
- **链接**：https://arxiv.org/abs/2503.18237
- **RECENCY**：≤1.5y
- **摘要**：分析 Aave 等协议的静态定价机制的效率问题，提出动态定价方案。
- **与 Paper 1 的关系**：DeFi 借贷利率机制背景。
- **引用键**：`chitra2025curationary`

### 9. Qu, Gogol, Groetschla, Tessone (2025) ≤1.5y

- **标题**：From Rules to Rewards: Reinforcement Learning for Interest Rate Adjustment in DeFi Lending
- **作者**：Hanxiao Qu, Krzysztof Gogol, Florian Groetschla, Claudio Tessone
- **年份**：2025
- **来源**：arXiv
- **链接**：https://arxiv.org/abs/2506.00505
- **RECENCY**：≤1.5y
- **摘要**：使用强化学习优化 DeFi 借贷利率，解决坏账和资本效率问题。
- **与 Paper 1 的关系**：利率机制优化背景。
- **引用键**：`qu2025from`

### 10. Belenko & Vosorov (2025) ≤1.5y

- **标题**：DeFi Liquidation Risk Modeling Using Geometric Brownian Motion
- **作者**：Timofei Belenko, Georgii Vosorov
- **年份**：2025
- **来源**：arXiv
- **链接**：https://arxiv.org/abs/2505.08100
- **RECENCY**：≤1.5y
- **摘要**：提出计算 DeFi 稳定币单抵押借贷中抵押品清算概率的分析方法。
- **与 Paper 1 的关系**：清算概率建模——与 Paper 1 的 outcome 定义相关。
- **引用键**：`belenko2025defi`

### 11. Bastankhah et al. (2024) ≤2y

- **标题**：AgileRate: Bringing Adaptivity and Robustness to DeFi Lending Markets
- **作者**：Mahsa Bastankhah, Viraj Nadkarni, Xuechao Wang, Pramod Viswanath
- **年份**：2024
- **来源**：arXiv
- **链接**：https://arxiv.org/abs/2410.13105
- **RECENCY**：≤2y
- **摘要**：提出自适应利率机制改善 Aave 和 Compound 的静态利率问题。
- **与 Paper 1 的关系**：DeFi 借贷利率机制改进背景。
- **引用键**：`bastankhah2024agilerate`

### 12. Ghosh et al. (2024) ≤2y

- **标题**：On-Chain Credit Risk Score in Decentralized Finance
- **作者**：Rik Ghosh, Arka Datta, Vidhi Aggarwal, Sudipan Sinha, Rajdeep Sengupta
- **年份**：2024
- **来源**：arXiv
- **链接**：https://arxiv.org/abs/2412.00710
- **RECENCY**：≤2y
- **摘要**：使用钱包级交易历史、借贷还款模式和交互频率构建 DeFi 链上信用风险评分框架。结果表明链上行为数据包含显著信用信息。
- **与 Paper 1 的关系**：直接竞争文献。使用 ML 方法做链上信用评分。Paper 1 与之的区别：Paper 1 关注行为过程变量而非静态特征，且不声称直接做 credit scoring。
- **引用键**：`ghosh2024onchain`

### 13. Tovanich et al. (2023) older

- **标题**：Contagion in Decentralized Lending Protocols: A Case Study of Compound
- **作者**：Natkamon Tovanich, Myriam Kassoul, Simon Weidenholzer, Julien Prat
- **年份**：2023
- **来源**：CCS '23 Workshop on Decentralized Finance and Security, 55-63
- **DOI**：10.1145/3605768.3623544
- **链接**：https://dl.acm.org/doi/pdf/10.1145/3605768.3623544
- **摘要**：研究 Compound V2 中的金融传染，构建协议资产负债表，展示集中借贷头寸如何创造系统性风险。
- **与 Paper 1 的关系**：协议级风险背景，Paper 1 关注 borrower-level。
- **引用键**：`tovanich2023contagion`

### 14. Qin et al. (2021) older

- **标题**：An empirical study of DeFi liquidations: incentives, risks, and instabilities
- **作者**：Kaihua Qin, Liyi Zhou, Pablo Gamito, Philipp Jovanovic, Arthur Gervais
- **年份**：2021
- **来源**：IMC '21, 336-350
- **DOI**：10.1145/3487552.3487811
- **链接**：https://doi.org/10.1145/3487552.3487811
- **摘要**：最早系统分析 DeFi 清算事件的研究之一，记录清算频率、交易费和级联风险。
- **与 Paper 1 的关系**：清算机制实证基础文献。
- **引用键**：`qin2021empirical`

### 15. Perez et al. (2021) older

- **标题**：Liquidations: DeFi on a Knife-Edge
- **作者**：Daniel Perez, Sam M. Werner, Jiahua Xu, Benjamin Livshits
- **年份**：2021
- **来源**：Financial Cryptography and Data Security, 457-476
- **DOI**：10.1007/978-3-662-64331-0_24
- **链接**：https://doi.org/10.1007/978-3-662-64331-0_24
- **摘要**：DeFi 清算机制的早期系统分析。
- **与 Paper 1 的关系**：清算机制基础文献。
- **引用键**：`perez2020liquidations`

### 16. Gudgeon et al. (2020) older

- **标题**：DeFi Protocols for Loanable Funds: Interest Rates, Liquidity and Market Efficiency
- **作者**：Lewis Gudgeon, Sam Werner, Daniel Perez, William J. Knottenbelt
- **年份**：2020
- **来源**：AFT 2020, 92-112
- **DOI**：10.1145/3419614.3423254
- **链接**：https://doi.org/10.1145/3419614.3423254
- **摘要**：DeFi 可贷资金协议的利率、流动性和市场效率分析。
- **与 Paper 1 的关系**：DeFi 借贷协议的基础架构文献。
- **引用键**：`gudgeon2020defi`

---

## 整合文档推荐（未在本次搜索中出现）

### Cornelli et al. (2025)

- **标题**：Why DeFi Lending? Evidence from Aave V2
- **来源**：Journal of Financial Intermediation
- **链接**：https://www.sciencedirect.com/science/article/pii/S1042443725002033
- **作用**：Aave V2 交易级借贷行为实证；DeFi 借款动机。Paper 1 需要直接对话。
- **引用键**：`cornelli2025defi`

### Schuler (2026)

- **标题**：Frictions in DeFi Liquidations: Evidence from the Aave V2 Main Market
- **来源**：Working Paper
- **作用**：直接涉及 Aave V2 block-level position、liquidation、execution friction。属于 must-read / direct competitor。
- **引用键**：`schuler2026frictions`

### Makarov & Schoar

- **标题**：Cryptocurrencies and Decentralized Finance (DeFi)
- **来源**：BIS Working Paper
- **作用**：DeFi 架构、匿名参与、超额抵押、清算、市场结构。
- **引用键**：`makarov_schoar_defi`
