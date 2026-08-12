# Chainlink Oracle 技术文档

**官方文档**：https://docs.chain.link/data-feeds  
**用途**：Paper 1 价格数据来源，确保分析使用的价格与参与者当时可获取的价格一致

---

## 1. 概述

Chainlink Data Feeds 是连接智能合约与真实世界数据的 quickest 方式，主要提供资产价格、储备余额和 L2 sequencer 健康状态。Aave 等借贷协议使用 Chainlink Price Feeds 评估抵押品价值。

---

## 2. Price Feeds 机制

### 更新触发条件

Chainlink price feed 在以下条件下更新：
1. **Deviation threshold**：价格偏离超过设定阈值
2. **Heartbeat**：超过设定时间未更新

### 关键参数

| 参数 | 含义 | 对研究的影响 |
|------|------|-------------|
| `latestRoundData()` | 获取最新价格 | 重建历史价格的主要接口 |
| `latestTimestamp` | 最后更新时间 | 判断价格时效性 |
| `minAnswer` / `maxAnswer` | 价格上下限 | 可能限制极端情况下的价格报告 |
| Heartbeat | 最大更新间隔 | 低波动期价格可能长时间不更新 |
| Deviation threshold | 触发更新的价格偏差 | 影响价格精度 |

### 对 Paper 1 的影响

- 重建历史 HF 时，应使用 Chainlink 在该时间点报告的价格，而非市场价格
- 预言机价格与市场价格可能有偏差
- 在低波动期，预言机价格可能长时间不更新，HF 重建的时间粒度受此限制
- 需检查 `latestTimestamp` 确保价格是当时可获取的

---

## 3. 数据获取

### 链上接口

```solidity
AggregatorV3Interface priceFeed = AggregatorV3Interface(priceFeedAddress);
(
    uint80 roundID,
    int256 answer,
    uint256 startedAt,
    uint256 updatedAt,
    uint80 answeredInRound
) = priceFeed.latestRoundData();
```

### 历史价格

- `getRoundData(roundId)` 获取特定轮次的价格
- 需要知道 roundId 或从 `latestRoundData()` 反向遍历
- Archive node 可获取历史时间点的 `latestRoundData()` 返回值

### Aave 使用的预言机

- Aave 使用自己的 PriceOracle 合约，底层调用 Chainlink
- 需要通过 Aave 的 `getAssetPrice(asset)` 获取协议使用的价格
- 这确保分析使用的价格与协议当时使用的价格一致

---

## 4. SVR (Smart Value Recapture) Feeds

Chainlink 最新推出了 SVR Feeds，用于在 oracle 更新时 recapture Oracle Extractable Value (OEV)。这是一种与 MEV 相关的机制，在 liquidation 场景中尤为重要。

### 对 Paper 1 的影响

- 如果研究期间部分 price feed 迁移到 SVR，需要注意价格更新行为的可能变化
- SVR 可能影响 liquidation 的 timing 和 profitability

---

## 5. 文档链接

| 内容 | 链接 |
|------|------|
| Chainlink Data Feeds | https://docs.chain.link/data-feeds |
| Price Feed Addresses | https://docs.chain.link/data-feeds/price-feeds/addresses |
| Data Feeds API Reference | https://docs.chain.link/data-feeds/api-reference |
| Decentralized Data Model | https://docs.chain.link/data-feeds/data-feeds-data-model |
| Using Data Feeds | https://docs.chain.link/data-feeds/using-data-feeds |
