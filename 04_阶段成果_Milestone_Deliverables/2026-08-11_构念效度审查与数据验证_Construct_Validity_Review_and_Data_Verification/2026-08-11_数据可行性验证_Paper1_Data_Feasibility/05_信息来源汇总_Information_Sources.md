# 信息来源汇总

**日期**：2026-08-11  
**用途**：记录数据可行性验证中所有信息的来源

---

## 一、Dune 官方文档

| 信息 | 来源 URL |
|------|---------|
| Dune 数据目录（三层数据架构、Curated Datasets 列表、Ethereum 覆盖确认） | https://dune.com/docs/data-tables/decoded/ |
| Dune 查询语言文档 | https://dune.com/docs/query/ |
| Dune Spellbook | https://dune.com/docs/spellbook/ |
| Dune 数据浏览器使用 | https://docs.dune.com/web-app/query-editor/data-explorer |
| 合约解码机制 | https://docs.dune.com/web-app/decoding/decoding-contracts |
| 数据质量声明（"Comprehensive Chain Histories"、"Accurate and Validated Data"） | https://dune.com/docs/data-tables/decoded/ — Data Trust & Freshness 部分 |

## 二、Dune 查询实例（验证表名和字段）

| 信息 | 来源 URL |
|------|---------|
| Aave V3 Pool_evt_Supply 表名和字段确认（USDC Supply Metrics 查询） | https://dune.com/queries/4408381/7386395 |
| Aave V3 Pool_evt_ReserveDataUpdated 表名和字段确认（APY 查询） | https://dune.com/queries/3255356 |
| Aave V3 Pool_evt_LiquidationCall 表名和字段确认（Liquidation Overview 查询） | https://dune.com/queries/1955184 |
| Aave V3 Ethereum 部署日期确认（2023-01-27） | https://dune.com/queries/6207312/9904181 |
| Aave V3 ReserveUsedAsCollateralEnabled/Disabled 事件 topic0 确认 | https://dune.com/queries/1026402/1771390 |
| Dune SQL 查询最佳实践（分区列过滤） | https://github.com/duneanalytics/skills/blob/HEAD/skills/dune/references/dunesql-cheatsheet.md |
| Dune 数据集发现方法（表名命名规则） | https://github.com/duneanalytics/skills/blob/HEAD/skills/dune/references/dataset-discovery.md |

## 三、Aave 官方文档与源码

| 信息 | 来源 URL |
|------|---------|
| Aave V3 官方文档 | https://docs.aave.com/ |
| Aave V3 Health Factor 概念 | https://docs.aave.com/developers/concepts/health-factor |
| Aave V3 部署合约地址（Ethereum Mainnet） | https://docs.aave.com/developers/deployed-contracts/v3-mainnet/ |
| Aave V3 Pool 合约文档（setUserUseReserveAsCollateral 等） | https://aave.com/docs/aave-v3/smart-contracts/pool |
| Aave V3 PoolConfigurator 源码（CollateralConfigurationChanged 事件） | https://github.com/aave/aave-v3-core/blob/master/contracts/protocol/pool/PoolConfigurator.sol |
| Aave V3 UserConfiguration 源码（collateral-enabled 状态管理） | https://github.com/aave/aave-v3-core/blob/master/contracts/protocol/libraries/configuration/UserConfiguration.sol |
| Aave V3 GitHub 主仓库 | https://github.com/aave/aave-v3-core |
| Aave Protocol Subgraph 源码（事件处理逻辑确认） | https://github.com/aave/protocol-subgraphs/blob/main/src/mapping/lending-pool/lending-pool.ts |
| Aave V3 完整事件列表（Pool + PoolConfigurator） | https://github.com/PaulieB14/aave-v3-polygon |

## 四、Gnosis Analytics 文档（Aave V3 事件签名验证）

| 信息 | 来源 URL |
|------|---------|
| Aave V3 事件签名确认（Supply, Withdraw, Borrow, Repay, LiquidationCall, ReserveDataUpdated） | https://docs.analytics.gnosis.io/protocols/lending/aave-v3/ |
| Lending 协议比较 | https://docs.analytics.gnosis.io/protocols/lending/ |

## 五、Chainlink 文档

| 信息 | 来源 URL |
|------|---------|
| Chainlink Data Feeds 文档 | https://docs.chain.link/data-feeds |
| Chainlink Price Feed 地址 | https://docs.chain.link/data-feeds/price-feeds/addresses |
| Chainlink ETH/USD Price Feed 地址 (0x5f4eC3Df9cbd43714FE2740f5E3616155c5b8419) | https://docs.chain.link/data-feeds/price-feeds/addresses |

## 六、其他来源

| 信息 | 来源 URL |
|------|---------|
| Etherscan 标签页面（手动合约地址列表来源） | https://etherscan.io/labels |
| Ethereum PoS 共识文档 | https://ethereum.org/en/developers/docs/consensus-mechanisms/pos/ |

---

## 七、信息验证方法说明

本文件夹中的每一项信息都通过以下方式之一验证：

| 验证方式 | 说明 | 使用位置 |
|---------|------|---------|
| Dune 实际查询 | 在 Dune 上找到使用该表名的真实查询 | 表名确认、字段确认 |
| 官方源码 | 从 Aave V3 GitHub 仓库读取事件定义 | 事件签名、参数精度 |
| 官方文档 | 从 Aave / Chainlink / Dune 官方文档获取 | 合约地址、参数说明 |
| 第三方文档 | 从 Gnosis Analytics 等第三方文档交叉验证 | 事件签名交叉验证 |
| 搜索结果 | 通过 websearch 工具搜索验证 | 综合验证 |

---

## 八、未验证项

| 项目 | 状态 | 说明 |
|------|------|------|
| Chainlink decoded tables 在 Dune 上是否存在 | ⚠️ 待验证 | 需要在 Dune Data Explorer 中搜索 "chainlink" |
| PoolConfigurator 所有事件的 decoded tables 在 Dune 上是否完整 | ⚠️ 待验证 | 需要在 Dune Data Explorer 中确认 PoolConfigurator namespace |
| Aave V3 部署后的所有 governance 参数变更是否都有对应事件 | ⚠️ 待验证 | 需要抽样验证 CollateralConfigurationChanged 事件是否覆盖所有已知 LT 变更 |
| Dune curated Lending 数据集的具体 schema | ⚠️ 待验证 | 需要查看 Lending curated 表的文档页面 |

**建议**：在正式开始数据获取之前，先执行 Phase 1（验证阶段）中的测试查询，确认以上待验证项。