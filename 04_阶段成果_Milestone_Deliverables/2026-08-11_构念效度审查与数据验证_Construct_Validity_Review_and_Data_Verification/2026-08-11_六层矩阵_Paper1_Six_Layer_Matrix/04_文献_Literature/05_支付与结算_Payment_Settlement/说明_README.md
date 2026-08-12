# 05. Payment / Settlement 文献

**主题**：支付、结算、Stablecoin 在支付系统中的角色  
**关联概念**：Boundary Concepts (Transfer, Payment, Settlement, Finality)  
**排序**：NEWEST → OLDEST

---

## 核心文献

### 1. Li, Zou, Liu, Ma, Zhao (2026) ★newest

- **标题**：SoK: Stablecoins in Retail Payments
- **作者**：Jianing Li, Xihan Zou, Lulu Liu, Zilin Ma, Yibo Zhao
- **年份**：2026
- **来源**：arXiv
- **链接**：https://arxiv.org/abs/2601.00196
- **RECENCY**：≤6mo ★newest
- **摘要**：系统综述稳定币在零售支付中的应用，分析支付场景、性能、安全性和监管挑战。
- **与 Paper 1 的关系**：Paper 2 的核心文献。Paper 1 需要了解 stablecoin transfer 在支付系统中的角色，但 Paper 1 本身不研究 payment。
- **引用键**：`li2026stablecoins`

### 2. Gertler, Höferle, Schittekatte, Gasior (2026) ★newest

- **标题**：Stablecoins and the Future of Money: Do We Need New Rules?
- **作者**：Maximilian Gertler, Klara Höferle, Timotheus Schittekatte, Dries Gasior
- **年份**：2026
- **来源**：Working Paper / SSRN
- **链接**：https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5210284
- **RECENCY**：≤6mo ★newest
- **摘要**：分析稳定币作为支付工具和货币替代品的监管和经济影响。
- **与 Paper 1 的关系**：稳定币的货币/支付角色——Paper 2/3 背景。
- **引用键**：`gertler2026stablecoins`

### 3. Campello, Gallo, Mota, Terracciano (2026) ★newest

- **标题**：Demand for Safety in the Crypto Ecosystem
- **作者**：Murillo Campello, Angela Gallo, Lira Mota, Tammaro Terracciano
- **年份**：2026
- **来源**：NBER Working Paper
- **DOI**：10.3386/w35557
- **链接**：https://doi.org/10.3386/w35557
- **RECENCY**：≤6mo ★newest
- **摘要**：研究加密生态系统中的安全性和流动性需求，在稳定币存款和借贷池之间分配。
- **与 Paper 1 的关系**：安全资产需求——与 DeFi 借贷市场的宏观背景相关。
- **引用键**：`campello2026demand`

### 4. Hautsch, Scheuch, Voigt (2024) ≤2y

- **标题**：Building trust takes time: limits to arbitrage for blockchain-based assets
- **作者**：Nikolaus Hautsch, Christoph Scheuch, Stefan Voigt
- **年份**：2024
- **来源**：European Finance Review, Vol. 28(4), 1345-1381
- **DOI**：10.1093/rof/rfae004
- **链接**：https://academic.oup.com/rof/advance-article-pdf/doi/10.1093/rof/rfae004/56695472/rfae004.pdf
- **RECENCY**：≤2y
- **摘要**：Blockchain settlement latency 限制了套利，影响市场效率。研究发现 trust building 需要 time——blockchain settlement 的不即时性是核心摩擦。
- **与 Paper 1 的关系**：Settlement latency 对 liquidation 执行的影响。支持 Paper 1 中 "execution ≠ finality ≠ economic settlement" 的区分。
- **引用键**：`hautsch2024building`

### 5. Bains, Dias, Emter, Holden, Morgan, Ramayandi, Shah (2025) ≤1.5y

- **标题**：Stablecoin Policy and Operations
- **作者**：Percy Bains, Daniel A. Dias, Lena Emter, Henry Holden, Iain Morgan, Vimal Ramayandi, Siddharth Shah
- **年份**：2025
- **来源**：IMF Working Paper
- **链接**：https://www.imf.org/en/Publications/WP/Issues/2025/04/24/Stablecoin-Policy-and-Operations-568056
- **RECENCY**：≤1.5y
- **摘要**：IMF 工作论文，分析稳定币的政策和操作框架。
- **与 Paper 1 的关系**：稳定币监管背景——Paper 2/3 的政策环境。
- **引用键**：`bains2025stablecoin`

---

## 整合文档推荐（未在本次搜索中出现，但为经典文献）

### Huberman, Leshno, Moallemi (2021)

- **标题**：Monopoly without a Monopolist: An Economic Analysis of the Bitcoin Payment System
- **来源**：Review of Economic Studies, Vol. 88(6), 3011-3040
- **链接**：https://academic.oup.com/restud/article/88/6/3011/6169547
- **作用**：从 payment-system economics 理解 blockchain payment。Paper 2 的理论基础。
- **引用键**：`huberman2021monopoly`

### Cong & He (2019)

- **标题**：Blockchain Disruption and Smart Contracts
- **来源**：Review of Financial Studies, Vol. 32(5), 1754-1797
- **链接**：https://academic.oup.com/rfs/article/32/5/1754/5427778
- **作用**：Blockchain 对 contracting / consensus 的经济意义。避免使用模糊的 "blockchain-native" 口号。
- **引用键**：`cong2019blockchain`

---

## 三层 Settlement 与文献映射

```text
Settlement Layer          | 文献支撑                        | Paper 1 可观测性
---------------------------|--------------------------------|------------------
Technical / Ledger          | Hautsch et al. (2024)          | ✅ 高
(交易上链、执行、最终确认)    | Ethereum PoS Finality           |
                           |                                 |
Protocol-level             | DeFi Lending 文献               | ✅ 高
(协议内义务了结，如 Repay)   | (Bartoletti & Lipparini 2025)  |
                           |                                 |
Economic / Business        | Li et al. (2026)               | ❌ 低
(商业上代表什么)             | Gertler et al. (2026)          | (需链下信息)
                           | Huberman et al. (2021)          |
```

---

## Paper 1 边界声明

> Paper 1 **不研究** payment、settlement、stablecoin transfer 的经济功能识别。这些是 Paper 2 的研究对象。Paper 1 仅在讨论 boundary concepts 时引用上述文献，用于明确自身的研究范围边界。
