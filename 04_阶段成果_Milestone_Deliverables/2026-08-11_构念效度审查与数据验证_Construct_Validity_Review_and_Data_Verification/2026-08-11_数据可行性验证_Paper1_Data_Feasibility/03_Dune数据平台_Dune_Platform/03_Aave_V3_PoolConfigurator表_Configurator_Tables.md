# Aave V3 PoolConfigurator Decoded Tables

**协议**：Aave V3  
**链**：Ethereum Mainnet  
**Dune 命名空间**：`aave_v3_ethereum`  
**合约名**：`PoolConfigurator`  
**来源**：Aave V3 GitHub 源码 + PaulieB14/aave-v3-polygon 事件列表

---

## 一、为什么需要 PoolConfigurator 数据？

PoolConfigurator 是 Aave V3 的管理合约，负责设置和修改协议参数。Paper 1 需要这些数据来追踪历史参数变化，特别是：

1. **Liquidation Threshold (LT)** — HF 公式的关键参数（问题 01 修正）
2. **LTV** — 借款能力参数
3. **EMode 配置** — EMode 下的不同 LT 值
4. **Isolation Mode 配置** — 隔离资产的债务上限

**如果没有这些数据**：
- 无法知道某个资产在某个历史时间点的 LT 值
- 无法正确重建历史 HF
- HF 重建会使用错误的参数

---

## 二、关键事件一览

| # | 事件名 | Dune 表名 | 研究用途 |
|---|--------|----------|---------|
| 1 | CollateralConfigurationChanged | `PoolConfigurator_evt_CollateralConfigurationChanged` | **追踪历史 LT/LTV/Bonus** |
| 2 | ReserveInitialized | `PoolConfigurator_evt_ReserveInitialized` | 追踪新资产上线 |
| 3 | EModeCategoryAdded | `PoolConfigurator_evt_EModeCategoryAdded` | 追踪 EMode 类别创建 |
| 4 | EModeCategoryUpdated | `PoolConfigurator_evt_EModeCategoryUpdated` | 追踪 EMode 类别修改 |
| 5 | ReserveEModeChanged | `PoolConfigurator_evt_ReserveEModeChanged` | 追踪资产的 EMode 归属 |
| 6 | DebtCeilingChanged | `PoolConfigurator_evt_DebtCeilingChanged` | 追踪 Isolation Mode 上限 |
| 7 | BorrowCapChanged | `PoolConfigurator_evt_BorrowCapChanged` | 追踪借款容量限制 |
| 8 | SupplyCapChanged | `PoolConfigurator_evt_SupplyCapChanged` | 追踪供应容量限制 |
| 9 | ReservePaused / Unpaused | `PoolConfigurator_evt_ReservePaused` / `_Unpaused` | 追踪资产暂停状态 |
| 10 | LiquidationProtocolFeeChanged | `PoolConfigurator_evt_LiquidationProtocolFeeChanged` | 追踪清算手续费 |

**来源**：Aave V3 事件列表 https://github.com/PaulieB14/aave-v3-polygon

---

## 三、核心事件详情

### 3.1 CollateralConfigurationChanged — 最重要的事件

**Solidity 事件签名**（来源：Aave V3 GitHub 源码）：
```solidity
event CollateralConfigurationChanged(
    address indexed asset,
    uint256 ltv,
    uint256 liquidationThreshold,
    uint256 liquidationBonus
);
```

**Dune 字段**：

| 字段 | 类型 | 含义 | 精度转换 | 研究用途 |
|------|------|------|---------|---------|
| `asset` | string | 资产地址 | — | 识别资产 |
| `ltv` | string | LTV | bps, /10000 | 追踪借款能力 |
| `liquidationThreshold` | string | LT | bps, /10000 | **HF 公式核心参数** |
| `liquidationBonus` | string | 清算罚金 | bps, /10000 | 清算成本分析 |

**精度说明**：
- bps = basis points（基点）
- 8300 bps / 10000 = 0.83 = 83%
- 10500 bps / 10000 = 1.05 = 105%（清算罚金 > 10000 表示 > 100%）

**验证来源**：Aave V3 GitHub 源码 https://github.com/aave/aave-v3-core/blob/master/contracts/protocol/pool/PoolConfigurator.sol 中 `configureReserveAsCollateral` 函数

**研究中的关键用途**：

```
重建历史 LT 的流程：

Step 1: 从 CollateralConfigurationChanged 事件获取所有 LT 变化
    SELECT evt_block_time, asset, liquidationThreshold
    FROM aave_v3_ethereum.PoolConfigurator_evt_CollateralConfigurationChanged
    WHERE asset = 0x...  -- ETH 地址
    ORDER BY evt_block_time;

Step 2: 对于任意历史时间点 t，找到 t 之前最近一次 LT 变更的值
    → 这就是时间 t 的 LT 值

Step 3: 使用这个 LT 值计算 HF
    HF(t) = Σ(collateral_value_i × LT_i(t)) / debt(t)
```

---

### 3.2 EModeCategoryAdded / Updated

**用途**：EMode 下使用不同的 LT 值（通常更高），需要追踪每个 EMode 类别的配置。

**Solidity 事件签名**：
```solidity
event EModeCategoryAdded(
    uint8 indexed categoryId,
    uint16 ltv,
    uint16 liquidationThreshold,
    uint16 liquidationBonus,
    address oracle,
    uint16 indexed label
);

event EModeCategoryUpdated(
    uint8 indexed categoryId,
    uint16 ltv,
    uint16 liquidationThreshold,
    uint16 liquidationBonus,
    address oracle,
    uint16 indexed label
);
```

**研究用途**：
- 结合 `UserEModeSet` 事件（Pool 事件），判断用户是否处于 EMode
- 如果处于 EMode，使用 EMode 的 LT 值而非普通 LT 值计算 HF
- 重建 HF 的完整逻辑：

```
HF 重建逻辑：

if 用户处于 EMode (categoryId > 0):
    LT = EMode_LT[categoryId][asset]
else:
    LT = normal_LT[asset]

HF = Σ(collateral_value × LT) / debt
```

---

### 3.3 ReserveEModeChanged

**用途**：追踪某个资产属于哪个 EMode 类别。

**Solidity 事件签名**：
```solidity
event ReserveEModeChanged(
    address indexed asset,
    uint8 oldCategoryId,
    uint8 newCategoryId
);
```

---

### 3.4 DebtCeilingChanged

**用途**：Isolation Mode 下的债务上限追踪。

**Solidity 事件签名**：
```solidity
event DebtCeilingChanged(
    address indexed asset,
    uint256 debtCeiling
);
```

**研究用途**：Isolation Mode 下，如果某种资产被用作唯一抵押品，可借的债务量受到 debt ceiling 限制。这影响 HF 计算的上限。

---

## 四、参数变化追踪的完整数据流

```
HF 重建所需的参数追踪：

普通模式：
  CollateralConfigurationChanged 事件
    → 追踪每个资产的 LT, LTV, Bonus 随时间变化
    → 用于普通模式下的 HF 计算

EMode 模式：
  EModeCategoryAdded/Updated 事件
    → 追踪每个 EMode 类别的 LT, LTV, Bonus
  ReserveEModeChanged 事件
    → 追踪每个资产属于哪个 EMode 类别
  UserEModeSet 事件（Pool 事件）
    → 追踪每个用户是否启用了 EMode
    → 如果启用，使用 EMode LT 而非普通 LT

Isolation Mode：
  DebtCeilingChanged 事件
    → 追踪每个资产的债务上限
  从 UserConfiguration（链上状态）
    → 判断用户是否处于 Isolation Mode
    → 可从 collateral-enabled 状态推断（只有一个 collateral = isolation）

完整 HF 计算：
  HF = Σ(V_i × LT_i) / D
  
  V_i = collateral_value（从 Supply/Withdraw + collateral-enabled 状态 + 价格重建）
  LT_i = liquidation_threshold（从 CollateralConfigurationChanged 或 EMode 配置获取）
  D = total_debt（从 Borrow/Repay + ReserveDataUpdated 重建）
```
