# Aave V3 Pool Decoded Tables

**协议**：Aave V3  
**链**：Ethereum Mainnet  
**Dune 命名空间**：`aave_v3_ethereum`  
**合约名**：`Pool`  
**来源**：Dune 查询实例 + Aave V3 GitHub + Gnosis Analytics Docs

---

## 一、表名一览

| # | 事件名 | Dune 表名 | 研究用途 |
|---|--------|----------|---------|
| 1 | Supply | `aave_v3_ethereum.Pool_evt_Supply` | 追踪资产存入 |
| 2 | Withdraw | `aave_v3_ethereum.Pool_evt_Withdraw` | 追踪资产提取 |
| 3 | Borrow | `aave_v3_ethereum.Pool_evt_Borrow` | 追踪借款创建 |
| 4 | Repay | `aave_v3_ethereum.Pool_evt_Repay` | 追踪借款偿还 |
| 5 | LiquidationCall | `aave_v3_ethereum.Pool_evt_LiquidationCall` | 追踪清算执行 |
| 6 | ReserveUsedAsCollateralEnabled | `aave_v3_ethereum.Pool_evt_ReserveUsedAsCollateralEnabled` | 追踪抵押启用 |
| 7 | ReserveUsedAsCollateralDisabled | `aave_v3_ethereum.Pool_evt_ReserveUsedAsCollateralDisabled` | 追踪抵押禁用 |
| 8 | ReserveDataUpdated | `aave_v3_ethereum.Pool_evt_ReserveDataUpdated` | 追踪利率/指数变化 |
| 9 | UserEModeSet | `aave_v3_ethereum.Pool_evt_UserEModeSet` | 追踪 EMode 状态 |
| 10 | FlashLoan | `aave_v3_ethereum.Pool_evt_FlashLoan` | 识别闪电贷 |

**时间覆盖**：2023-01-27（Aave V3 Ethereum mainnet 部署日）至今  
**来源**：Dune 查询 https://dune.com/queries/6207312 确认 Ethereum 部署日期为 2023-01-27

---

## 二、事件签名与字段详情

### 2.1 Supply

**Solidity 事件签名**（来源：Aave V3 GitHub + Gnosis Analytics Docs）：
```solidity
event Supply(
    address indexed reserve,
    address user,
    address indexed onBehalfOf,
    uint256 amount,
    uint16 indexed referralCode
);
```

**Dune 字段**：

| 字段 | 类型 | 含义 | 研究用途 |
|------|------|------|---------|
| `reserve` | string | 资产合约地址 | 识别资产 |
| `user` | string | 发起者地址（msg.sender） | 主动/被动分类 |
| `onBehalfOf` | string | 实际受益人 | **关键：主动/被动分类** |
| `amount` | string | 原始精度金额 | 需除以 token decimals |
| `referralCode` | integer | 推荐码 | 可忽略 |

**验证来源**：Dune 查询 https://dune.com/queries/4408381 使用了 `aave_v3_ethereum.Pool_evt_Supply` 和 `reserve`, `amount` 字段

---

### 2.2 Withdraw

**Solidity 事件签名**：
```solidity
event Withdraw(
    address indexed reserve,
    address indexed user,
    address indexed to,
    uint256 amount
);
```

**Dune 字段**：

| 字段 | 类型 | 含义 | 研究用途 |
|------|------|------|---------|
| `reserve` | string | 资产合约地址 | 识别资产 |
| `user` | string | 被提取的用户地址 | 追踪资产提取 |
| `to` | string | 接收地址 | 可能不同于 user |
| `amount` | string | 原始精度金额 | 需除以 token decimals |

**注意**：Withdraw 没有 `onBehalfOf`。`user` 是仓位所有者，`to` 是接收地址。

---

### 2.3 Borrow

**Solidity 事件签名**：
```solidity
event Borrow(
    address indexed reserve,
    address user,
    address indexed onBehalfOf,
    uint256 amount,
    uint8 interestRateMode,
    uint256 borrowRate,
    uint16 indexed referralCode
);
```

**Dune 字段**：

| 字段 | 类型 | 含义 | 研究用途 |
|------|------|------|---------|
| `reserve` | string | 借入资产地址 | 识别资产 |
| `user` | string | 发起者地址（msg.sender） | 主动/被动分类 |
| `onBehalfOf` | string | 债务承担者 | **关键：主动/被动分类** |
| `amount` | string | 原始精度金额 | 需除以 token decimals |
| `interestRateMode` | integer | 1=stable, 2=variable | 债务重建（利息计算方式） |
| `borrowRate` | string | 借款利率（ray, /1e27） | Stable rate 利息计算 |
| `referralCode` | integer | 推荐码 | 可忽略 |

**验证来源**：Gnosis Analytics Docs 确认事件签名 https://docs.analytics.gnosis.io/protocols/lending/aave-v3/

---

### 2.4 Repay

**Solidity 事件签名**：
```solidity
event Repay(
    address indexed reserve,
    address indexed user,
    address indexed repayer,
    uint256 amount,
    bool useATokens
);
```

**Dune 字段**：

| 字段 | 类型 | 含义 | 研究用途 |
|------|------|------|---------|
| `reserve` | string | 偿还资产地址 | 识别资产 |
| `user` | string | 被偿还债务的用户 | 债务归属者 |
| `repayer` | string | 实际还款人（msg.sender） | **关键：主动/被动分类** |
| `amount` | string | 原始精度金额 | 需除以 token decimals |
| `useATokens` | boolean | 是否使用 aToken 还款 | 资金流追踪 |

**关键**：`repayer` 和 `user` 可能不同。`repayer == user` 表示借款人自己还款（主动）；`repayer != user` 可能是第三方代还或清算。

---

### 2.5 LiquidationCall

**Solidity 事件签名**：
```solidity
event LiquidationCall(
    address indexed collateralAsset,
    address indexed debtAsset,
    address indexed user,
    uint256 debtToCover,
    uint256 liquidatedCollateralAmount,
    address liquidator,
    bool receiveAToken
);
```

**Dune 字段**：

| 字段 | 类型 | 含义 | 研究用途 |
|------|------|------|---------|
| `collateralAsset` | string | 被清算的抵押资产 | 分析抵押品 |
| `debtAsset` | string | 被偿还的债务资产 | 分析债务 |
| `user` | string | 被清算的借款人 | **RQ2 outcome 变量** |
| `debtToCover` | string | 偿还的债务金额 | 清算规模 |
| `liquidatedCollateralAmount` | string | 被清算的抵押品金额 | 清算损失 |
| `liquidator` | string | 清算者地址 | 清算者分析 |
| `receiveAToken` | boolean | 是否接收 aToken | 清算方式 |

**验证来源**：Dune 查询 https://dune.com/queries/1955184 使用了 `aave_v3_ethereum.Pool_evt_LiquidationCall` 和上述字段

---

### 2.6 ReserveUsedAsCollateralEnabled / Disabled

**Solidity 事件签名**：
```solidity
event ReserveUsedAsCollateralEnabled(
    address indexed reserve,
    address indexed user
);

event ReserveUsedAsCollateralDisabled(
    address indexed reserve,
    address indexed user
);
```

**Dune 字段**：

| 字段 | 类型 | 含义 | 研究用途 |
|------|------|------|---------|
| `reserve` | string | 资产地址 | 识别资产 |
| `user` | string | 用户地址 | 追踪 collateral 状态 |

**验证来源**：Aave Protocol Subgraph 源码确认事件 https://github.com/aave/protocol-subgraphs/blob/main/src/mapping/lending-pool/lending-pool.ts  
Dune 查询 https://dune.com/queries/1026402 确认 topic0 哈希值

**关键用途**：这是区分 Supply 和 Collateral-Enabled Supply 的核心数据（问题 03 修正）

---

### 2.7 ReserveDataUpdated

**Solidity 事件签名**：
```solidity
event ReserveDataUpdated(
    address indexed reserve,
    uint256 liquidityRate,
    uint256 stableBorrowRate,
    uint256 variableBorrowRate,
    uint256 liquidityIndex,
    uint256 variableBorrowIndex
);
```

**Dune 字段**：

| 字段 | 类型 | 含义 | 研究用途 |
|------|------|------|---------|
| `reserve` | string | 资产地址 | 识别资产 |
| `liquidityRate` | string | 供应利率（ray, /1e27） | 供应者收益 |
| `stableBorrowRate` | string | 稳定借款利率（ray, /1e27） | Stable rate 债务 |
| `variableBorrowRate` | string | 浮动借款利率（ray, /1e27） | Variable rate 债务 |
| `liquidityIndex` | string | 流动性指数（ray, /1e27） | 供应者余额重建 |
| `variableBorrowIndex` | string | 浮动借款指数（ray, /1e27） | **关键：Variable rate 债务重建** |

**验证来源**：Dune 查询 https://dune.com/queries/3255356 使用了 `aave_v3_ethereum.Pool_evt_ReserveDataUpdated` 和 `variableBorrowRate`, `liquidityRate` 字段

**关键用途**：重建历史债务（R2）的核心输入。Variable rate 债务 = ScaledBalance × variableBorrowIndex

---

### 2.8 UserEModeSet

**Solidity 事件签名**：
```solidity
event UserEModeSet(
    address indexed sender,
    uint8 categoryId
);
```

**Dune 字段**：

| 字段 | 类型 | 含义 | 研究用途 |
|------|------|------|---------|
| `sender` | string | 用户地址 | 追踪 EMode 状态 |
| `categoryId` | integer | EMode 类别 ID（0 = 退出 EMode） | 判断使用哪种 LT 值 |

**验证来源**：Aave V3 事件列表确认 https://github.com/PaulieB14/aave-v3-polygon

---

### 2.9 FlashLoan

**Solidity 事件签名**：
```solidity
event FlashLoan(
    address indexed target,
    address indexed initiator,
    address indexed asset,
    uint256 amount,
    uint8 interestRateMode,
    uint256 premium,
    uint16 indexed referralCode
);
```

**Dune 字段**：

| 字段 | 类型 | 含义 | 研究用途 |
|------|------|------|---------|
| `target` | string | 闪电贷接收合约 | 识别策略 |
| `initiator` | string | 闪电贷发起者 | 识别发起者 |
| `asset` | string | 借入资产 | 识别资产 |
| `amount` | string | 借入金额 | 闪电贷规模 |
| `premium` | string | 闪电贷手续费 | 成本分析 |

**研究用途**：识别涉及闪电贷的复杂交易，排除或单独分析。

---

## 三、所有表的通用字段

以下字段在所有 `evt_*` 表中都存在：

| 字段 | 类型 | 含义 | 说明 |
|------|------|------|------|
| `evt_block_time` | timestamp | 区块时间戳 | **分区列，查询必须过滤** |
| `evt_block_number` | integer | 区块号 | 排序和定位 |
| `evt_tx_hash` | string | 交易哈希 | 关联交易和 trace |
| `evt_index` | integer | 事件在交易中的索引 | 多事件排序 |
| `contract_address` | string | 发出事件的合约地址 | 确认来源 |

---

## 四、Aave V3 Ethereum Mainnet 合约地址

| 合约 | 地址 | 来源 |
|------|------|------|
| Pool (Proxy) | `0x87870Bca3F3fD6335C3F4ce8392D69350B4fA4E2` | Aave 官方文档 |
| PoolConfigurator | 参见 Aave 部署合约页面 | Aave 官方文档 |

**来源**：https://docs.aave.com/developers/deployed-contracts/v3-mainnet/

---

## 五、查询示例

### 5.1 查询某用户的全部 Supply 事件

```sql
SELECT
    evt_block_time,
    evt_block_number,
    evt_tx_hash,
    reserve,
    user,
    onBehalfOf,
    amount
FROM aave_v3_ethereum.Pool_evt_Supply
WHERE onBehalfOf = 0x...  -- 替换为目标地址
  AND evt_block_time >= TIMESTAMP '2023-01-27'
ORDER BY evt_block_time;
```

### 5.2 查询某时段的清算事件

```sql
SELECT
    evt_block_time,
    collateralAsset,
    debtAsset,
    user,
    debtToCover,
    liquidatedCollateralAmount,
    liquidator
FROM aave_v3_ethereum.Pool_evt_LiquidationCall
WHERE evt_block_time >= TIMESTAMP '2024-01-01'
  AND evt_block_time < TIMESTAMP '2025-01-01'
ORDER BY evt_block_time;
```

### 5.3 查询某用户的 collateral 状态变化

```sql
SELECT
    evt_block_time,
    reserve,
    user,
    'enabled' AS action
FROM aave_v3_ethereum.Pool_evt_ReserveUsedAsCollateralEnabled
WHERE user = 0x...
  AND evt_block_time >= TIMESTAMP '2023-01-27'

UNION ALL

SELECT
    evt_block_time,
    reserve,
    user,
    'disabled' AS action
FROM aave_v3_ethereum.Pool_evt_ReserveUsedAsCollateralDisabled
WHERE user = 0x...
  AND evt_block_time >= TIMESTAMP '2023-01-27'

ORDER BY evt_block_time;
```

### 5.4 查询某资产的 LT 变化历史

```sql
SELECT
    evt_block_time,
    asset,
    ltv,
    liquidationThreshold,
    liquidationBonus
FROM aave_v3_ethereum.PoolConfigurator_evt_CollateralConfigurationChanged
WHERE asset = 0x...  -- 替换为资产地址
  AND evt_block_time >= TIMESTAMP '2023-01-27'
ORDER BY evt_block_time;
```
