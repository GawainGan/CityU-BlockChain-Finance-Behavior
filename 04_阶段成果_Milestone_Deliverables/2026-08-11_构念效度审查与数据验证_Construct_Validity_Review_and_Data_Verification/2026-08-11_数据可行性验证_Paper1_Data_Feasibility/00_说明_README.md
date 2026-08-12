# 数据可行性验证 / Data Feasibility Verification

**日期**：2026-08-11  
**目的**：验证 Paper 1 研究设计中声称使用的所有数据，是否在可用数据平台上真实存在并符合研究要求

---

## 为什么需要这个文件夹？

在 Report v1 中，我们声称使用以下数据：
- Aave V3 的 Supply/Withdraw/Borrow/Repay/LiquidationCall 事件
- Health Factor（HF）重建
- Chainlink 价格数据
- 主动/被动行为分类
- Collateral-enabled 状态追踪

**但从未验证过这些数据在 Dune Analytics 上是否真的可用、字段是否完整、历史覆盖是否足够。**

这个文件夹解决了以下问题：
1. 我们需要的每一项数据，在 Dune 上对应哪张表？字段是什么？
2. 哪些数据 Dune 直接提供？哪些需要研究者自己重建？
3. 有没有关键数据缺口？如何弥补？
4. 每一项信息的来源是什么？

---

## 文件夹结构

```
2026-08-11_数据可行性验证_Paper1/
├── 00_README.md                              ← 本文件
├── 01_数据需求与平台映射总表.md                ← 需求→可用性映射总表
├── 02_数据可行性评估.md                        ← 总体评估结论
├── 03_Dune_数据平台/                           ← Dune 平台详细文档
│   ├── 01_Dune_平台总览.md                     ← Dune 三层数据架构
│   ├── 02_Aave_V3_Pool_Decoded_Tables.md      ← Pool 事件表（核心）
│   ├── 03_Aave_V3_PoolConfigurator_Tables.md  ← 参数变更表（LT/LTV追踪）
│   ├── 04_Dune_辅助表_价格_Token_Labels.md     ← 价格/Token/标签
│   └── 05_Dune_Raw_Tables.md                  ← 原始交易/Trace数据
├── 04_数据缺口与解决方案.md                     ← 缺失数据 + 如何获取
└── 05_信息来源汇总.md                          ← 所有信息来源
```

---

## 核心发现预览

| 数据需求 | Dune 可用？ | 表名/来源 | 需要重建？ |
|---------|-----------|----------|----------|
| Supply 事件（含 onBehalfOf） | ✅ 是 | `aave_v3_ethereum.Pool_evt_Supply` | 否 |
| Borrow 事件（含 onBehalfOf） | ✅ 是 | `aave_v3_ethereum.Pool_evt_Borrow` | 否 |
| Repay 事件（含 repayer） | ✅ 是 | `aave_v3_ethereum.Pool_evt_Repay` | 否 |
| LiquidationCall 事件 | ✅ 是 | `aave_v3_ethereum.Pool_evt_LiquidationCall` | 否 |
| Collateral 启用/禁用 | ✅ 是 | `Pool_evt_ReserveUsedAsCollateralEnabled/Disabled` | 否 |
| 历史 LT/LTV 值 | ✅ 是 | `PoolConfigurator_evt_CollateralConfigurationChanged` | 否 |
| EMode 状态 | ✅ 是 | `Pool_evt_UserEModeSet` | 否 |
| 利率/指数变化 | ✅ 是 | `Pool_evt_ReserveDataUpdated` | 否 |
| Token 价格 | ✅ 是 | `prices.usd` | 否 |
| Token 元数据 | ✅ 是 | `tokens.erc20` | 否 |
| 地址标签（Safe/Router等） | ✅ 是 | `labels.labels` | 需补充手动列表 |
| 交易 Trace（msg.sender 链） | ✅ 是 | `ethereum.traces` | 否 |
| 历史 HF 值 | ❌ 不直接提供 | — | ✅ **需要研究者重建** |
| 历史 Debt 值 | ❌ 不直接提供 | — | ✅ **需要研究者重建** |
| 借款人经济意图 | ❌ 不可获取 | — | 无法获取（链下信息） |

**总体结论**：Paper 1 所需的全部协议层面数据均可在 Dune 上获取。HF 和 Debt 需要研究者基于事件数据自行重建，但所有重建所需的输入数据（事件、参数、价格）均可获取。