# Aave V3 技术文档

**官方文档**：https://docs.aave.com/  
**版本**：V3（当前主线版本）  
**用途**：Paper 1 主协议，提供 HF 重建、事件解析、主动/被动分类的技术基础

---

## 1. 协议概述

Aave 是一个去中心化非托管流动性协议，用户可以作为供应者或借款者参与。供应者向市场提供流动性并赚取利息，借款者通过提供超额抵押来获取流动性。

### 关键特性

- **Permissionless**：任何人可以通过钱包地址直接交互
- **Overcollateralized**：借款需要超额抵押
- **Non-custodial**：协议不托管用户资产，用户始终控制自己的钱包
- **Multi-asset**：支持多种资产作为抵押和借款

---

## 2. Health Factor（核心风险指标）

### 公式（正确版本）

```text
HF = Σ(V_i × LT_i) / D
```

其中：
- V_i = collateral asset i 的价值（数量 × Chainlink 预言机价格）
- LT_i = asset i 的 **Liquidation Threshold**（不是 LTV！）
- D = total debt（本金 + 应计利息）

### 关键区分

```text
LTV (Loan-to-Value)        → 决定能借多少（borrowing capacity）
LT (Liquidation Threshold)  → 决定何时被清算（liquidation trigger）
```

### 清算条件

- HF < 1.0 → 仓位可被清算
- HF = 1.0 → 清算边界
- HF > 1.0 → 安全

### EMode（Efficiency Mode）

- EMode 下使用不同的 LT 值（通常更高）
- 适用于高度相关的资产对（如 USDC/USDT/DAI）
- 重建 HF 时需要识别仓位是否处于 EMode

### Isolation Mode

- Isolated assets 有特殊的 LT 限制
- 重建时需要检查 isolation 状态

---

## 3. 关键事件类型

| 事件 | 含义 | 关键参数 | 与主动/被动的关系 |
|------|------|---------|-----------------|
| `Supply` | 资产存入 | reserve, user, amount, onBehalfOf | 可能是主动（需判断） |
| `Withdraw` | 资产提取 | reserve, user, amount, onBehalfOf | 可能是主动（需判断） |
| `Borrow` | 创建借款 | reserve, user, amount, onBehalfOf, interestRateMode | 可能是主动（需判断） |
| `Repay` | 偿还借款 | reserve, user, repayer, amount, useATokens, onBehalfOf | 可能是主动（需判断） |
| `LiquidationCall` | 清算执行 | collateralAsset, debtAsset, user, debtToCover, liquidatedCollateralAmount, liquidator | **被动事件** |
| `SetUserUseReserveAsCollateral` | 启用/禁用 collateral | reserve, user, usageAsCollateral | 可能是主动 |
| `FlashLoan` | 闪电贷 | target, initiator, asset, amount, premium | 单独标记 |

### onBehalfOf 参数

Aave 支持 credit delegation：
- `user`/`repayer`：发起交易的地址（msg.sender）
- `onBehalfOf`：实际债务承担者

**关键**：`msg.sender == borrower` 不等于 "active action"。必须检查 `onBehalfOf` 参数。

---

## 4. Collateral-Enabled 状态

### Aave V3 中的独立状态

```text
Supply (存入资产)
    ≠
Collateral-Enabled (启用为抵押)
```

- 用户 supply 资产后，可以选择是否将其启用为 collateral
- 只有 collateral-enabled 的资产才计入 HF 计算
- `SetUserUseReserveAsCollateral` 事件记录了启用/禁用操作
- `UserReserveData.usageAsCollateralEnabled` 存储当前状态

### 对 Paper 1 的影响

- 风险减轻的追加抵押 = Supply + collateral-enabled + 增加了 HF 分子
- 风险增加的抵押提取 = Withdraw + 该资产是 collateral + 减少了 HF 分子
- 简单的 Supply/Withdraw 事件不能直接等同于抵押调整

---

## 5. 利率机制

### 两种利率模式

| 模式 | 特点 | 对债务计算的影响 |
|------|------|-----------------|
| Variable Rate | 随市场变化 | 债务 = ScaledBalance × Reserve Index |
| Stable Rate | 固定一段时间 | 债务按固定利率累积 |

### 债务重建

- Variable rate：需要按 block 追踪 Reserve Index 变化
- Stable rate：债务按固定利率线性增长
- 重建历史 HF 时必须使用当时的 debt（不是当前 debt）

---

## 6. 清算机制

### 清算流程

```text
HF < 1.0
    ↓
任何第三方可以触发 LiquidationCall
    ↓
Liquidator 偿还部分债务
    ↓
获取对应抵押品 + Liquidation Bonus（清算罚金）
    ↓
仓位 HF 恢复到 > 1.0
```

### 清算罚金

- Liquidation Bonus 通常为 5-10%
- 作为对 liquidator 的激励
- 从被清算借款人的抵押品中扣除

### 清算限制

- 每次清算最多覆盖一定比例的债务（close factor）
- 清算可能因 gas、MEV、网络拥堵等执行摩擦而延迟

---

## 7. 数据获取

### Dune Analytics

- 提供 SQL 查询接口访问 decoded event logs 和 state data
- Aave V3 的 decoded tables 可直接查询
- 官方文档：https://dune.com/docs/

### Archive Node / RPC

- 对于需要精确重建历史状态的场景，应使用 archive node
- `eth_getStorageAt` 获取历史存储状态
- `eth_call` 模拟历史状态下的合约调用

### 推荐数据栈

```text
Protocol Contracts + Historical Parameters
        ↓
Raw / Decoded Blockchain Data (Dune / RPC)
        ↓
Researcher-built Position State (tx/block level)
        ↓
Dune / Curated Dataset Validation
```

---

## 8. 相关合约地址

- Aave V3 Ethereum Mainnet Pool: 参见 https://docs.aave.com/developers/deployed-contracts/v3-mainnet/
- Aave V3 Ethereum Pool Proxy: 0x87870Bca3F3fD6335C3F4ce8392D69350B4fA4E2
- Chainlink Price Oracle: 参见 https://docs.aave.com/developers/deployed-contracts/v3-mainnet/price-oracle

---

## 9. 文档链接

| 内容 | 链接 |
|------|------|
| Aave 官方文档 | https://docs.aave.com/ |
| Aave V3 文档 | https://docs.aave.com/developers/concepts/aave-v3-concepts |
| Health Factor | https://docs.aave.com/developers/concepts/health-factor |
| Liquidations Guide | https://docs.aave.com/developers/guides/liquidations |
| 部署合约 | https://docs.aave.com/developers/deployed-contracts/v3-mainnet/ |
| GitHub | https://github.com/aave/aave-v3-core |
