# 技术文档总表

**日期**：2026-08-11  
**用途**：为六层矩阵中的 Measurement 和 Observable 层提供技术文档支撑

---

## 文档清单

| # | 文档 | 协议/基础设施 | 链接 |
|---|------|-------------|------|
| 1 | Aave V3 | DeFi 借贷协议（主协议） | `01_Aave_V3协议_Aave_V3.md` |
| 2 | Compound III | DeFi 借贷协议（跨协议验证） | `02_Compound_III协议_Compound_III.md` |
| 3 | MakerDAO / Sky | DeFi 借贷协议（外部有效性） | `03_MakerDAO与Sky_MakerDAO_Sky.md` |
| 4 | Chainlink Oracle | 预言机基础设施 | `04_Chainlink预言机_Chainlink_Oracle.md` |
| 5 | Ethereum Finality | 共识与最终性 | `05_Ethereum最终性_Ethereum_Finality.md` |
| 6 | Dune Analytics | 数据查询平台 | `06_Dune分析平台_Dune_Analytics.md` |
| 7 | 协议间异同对比 | 跨协议设计目的、机制差异与研究影响 | `07_协议间异同对比_Cross_Protocol_Comparison.md` |

---

## 各文档涉及的概念

| 概念 | Aave V3 | Compound III | MakerDAO | Chainlink | Ethereum | Dune |
|------|---------|-------------|----------|-----------|----------|------|
| Collateral | ✅ | ✅ | ✅ | — | — | ✅ |
| Position Risk | ✅ | ✅ | ✅ | ✅ | — | ✅ |
| Health Factor | ✅ | — | — | ✅ | — | ✅ |
| Distance to Liquidation | ✅ | ✅ | ✅ | ✅ | — | ✅ |
| Borrow | ✅ | ✅ | ✅ | — | — | ✅ |
| Repay | ✅ | ✅ | ✅ | — | — | ✅ |
| Supply vs Collateral-Enabled | ✅ | ✅ | ✅ | — | — | ✅ |
| Borrower Adjustment | ✅ | ✅ | ✅ | ✅ | — | ✅ |
| Active vs Passive | ✅ | ✅ | ✅ | — | — | ✅ |
| Liquidation Eligibility | ✅ | ✅ | ✅ | ✅ | — | ✅ |
| Realized Liquidation | ✅ | ✅ | ✅ | — | — | ✅ |
| Borrower Identity | — | — | — | — | — | ✅ |
| Boundary Concepts | — | — | — | — | ✅ | ✅ |

---

## 官方文档链接

| 协议/基础设施 | 官方文档 | 关键页面 |
|--------------|---------|---------|
| Aave V3 | https://docs.aave.com/ | Liquidations, Health Factor, atokens |
| Compound III | https://docs.compound.finance/ | Introduction, Comet, Liquidator Guide |
| MakerDAO / Sky | https://docs.makerdao.com/ | Vault Module, Liquidation |
| Chainlink | https://docs.chain.link/data-feeds | Price Feeds, Data Feeds API |
| Ethereum | https://ethereum.org/en/developers/docs/consensus-mechanisms/pos/ | PoS, Finality, Fork Choice |
| Dune | https://dune.com/docs/ | SQL Queries, Decoded Data, Spellbook |
