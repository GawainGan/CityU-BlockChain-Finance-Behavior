# 数据需求与平台映射总表

**日期**：2026-08-11  
**用途**：将 Paper 1 研究设计中每一项数据需求映射到 Dune Analytics 上的具体数据表和字段

---

## 一、研究设计中的数据需求清单

以下数据需求来自六层矩阵的 Measurement 和 Observable 层，以及 Report v1 修订后的方法论。

### 1.1 协议事件数据（Aave V3 Ethereum Mainnet）

| # | 数据需求 | 用途 | 关键字段要求 |
|---|---------|------|------------|
| E1 | Supply 事件 | 追踪资产存入 | reserve, user, **onBehalfOf**, amount, referralCode |
| E2 | Withdraw 事件 | 追踪资产提取 | reserve, user, **to**, amount |
| E3 | Borrow 事件 | 追踪借款创建 | reserve, user, **onBehalfOf**, amount, interestRateMode, borrowRate, referralCode |
| E4 | Repay 事件 | 追踪借款偿还 | reserve, user, **repayer**, amount, useATokens |
| E5 | LiquidationCall 事件 | 追踪清算执行 | collateralAsset, debtAsset, user, debtToCover, liquidatedCollateralAmount, liquidator, receiveAToken |
| E6 | ReserveUsedAsCollateralEnabled | 追踪抵押启用 | reserve, user |
| E7 | ReserveUsedAsCollateralDisabled | 追踪抵押禁用 | reserve, user |
| E8 | ReserveDataUpdated | 追踪利率/指数变化 | reserve, liquidityRate, stableBorrowRate, variableBorrowRate, liquidityIndex, variableBorrowIndex |
| E9 | UserEModeSet | 追踪 EMode 状态 | sender, categoryId |
| E10 | FlashLoan 事件 | 识别闪电贷操作 | target, initiator, asset, amount, premium |

### 1.2 协议参数数据（PoolConfigurator）

| # | 数据需求 | 用途 | 关键字段要求 |
|---|---------|------|------------|
| P1 | CollateralConfigurationChanged | 追踪历史 LT/LTV/Liquidation Bonus 变化 | asset, **ltv, liquidationThreshold, liquidationBonus** |
| P2 | ReserveInitialized | 追踪新资产上线 | asset, aToken, stableDebtToken, variableDebtToken, interestRateStrategyAddress |
| P3 | EModeCategoryAdded/Updated | 追踪 EMode 类别配置 | categoryId, ltv, liquidationThreshold, liquidationBonus |
| P4 | DebtCeilingChanged | 追踪 Isolation Mode 债务上限 | asset, debtCeiling |
| P5 | ReserveEModeChanged | 追踪资产的 EMode 归属 | asset, categoryId |
| P6 | BorrowCapChanged / SupplyCapChanged | 追踪容量限制 | asset, cap |

### 1.3 价格数据

| # | 数据需求 | 用途 | 关键字段要求 |
|---|---------|------|------------|
| PR1 | Token 历史价格 | 重建历史 HF（抵押品和债务的 USD 价值） | blockchain, contract_address, price, minute/decimals |
| PR2 | Chainlink 预言机价格 | 确保分析使用的价格与协议参与者在当时看到的一致 | 需要从 Chainlink decoded tables 或 raw events 获取 |

### 1.4 Token 元数据

| # | 数据需求 | 用途 | 关键字段要求 |
|---|---------|------|------------|
| T1 | Token decimals | 将链上原始金额转换为人类可读金额 | contract_address, symbol, decimals |
| T2 | Token symbol | 识别资产 | contract_address, symbol |

### 1.5 交易与 Trace 数据

| # | 数据需求 | 用途 | 关键字段要求 |
|---|---------|------|------------|
| TX1 | 交易数据 | 获取 gas 价格、交易发起者（from）、目标合约（to） | hash, from, to, gas_price, block_time |
| TX2 | Trace 数据 | 追踪内部调用链（识别 Safe/Router/自动化 合约） | tx_hash, from, to, value, input, output, trace_type |
| TX3 | 交易收据 | 获取事件日志所属交易 | tx_hash, block_number, logs |

### 1.6 地址标签数据

| # | 数据需求 | 用途 | 关键字段要求 |
|---|---------|------|------------|
| L1 | 已知合约标签 | 识别 Safe 钱包、Router 合约、自动化服务、清算机器人 | address, label_type, label_name |

### 1.7 需要研究者重建的数据

| # | 数据需求 | 重建所需输入 | 为什么不能直接获取 |
|---|---------|-------------|-------------------|
| R1 | 历史 HF 值 | E1-E10 + P1-P6 + PR1 + T1 + R2 | HF 是一个计算值，不是链上事件；必须从事件+参数+价格重建 |
| R2 | 历史 Debt 值 | E3(Borrow) + E4(Repay) + E8(ReserveDataUpdated for interest) | 债务随利息累积，需要按 block 追踪 Reserve Index |
| R3 | Collateral-enabled 状态时间线 | E6 + E7 | 需要从启用/禁用事件重建每个地址在每个时间点的状态 |
| R4 | 主动/被动分类 | E1-E5 + TX2(Trace) + L1(Labels) | 需要结合 onBehalfOf、交易发起者、已知合约地址进行多层判断 |
| R5 | Borrower-position 面板 | R1 + R2 + R3 + E1-E5 | 最终分析面板，需要从事件级数据聚合 |

---

## 二、数据需求 → Dune 平台映射

### 2.1 协议事件 → Dune Decoded Tables

| # | 数据需求 | Dune 表名 | 可用？ | 来源 |
|---|---------|----------|--------|------|
| E1 | Supply 事件 | `aave_v3_ethereum.Pool_evt_Supply` | ✅ | Dune 查询实例确认 |
| E2 | Withdraw 事件 | `aave_v3_ethereum.Pool_evt_Withdraw` | ✅ | Dune 查询实例确认 |
| E3 | Borrow 事件 | `aave_v3_ethereum.Pool_evt_Borrow` | ✅ | Dune 查询实例确认 |
| E4 | Repay 事件 | `aave_v3_ethereum.Pool_evt_Repay` | ✅ | Dune 查询实例确认 |
| E5 | LiquidationCall 事件 | `aave_v3_ethereum.Pool_evt_LiquidationCall` | ✅ | Dune 查询实例确认 |
| E6 | Collateral 启用 | `aave_v3_ethereum.Pool_evt_ReserveUsedAsCollateralEnabled` | ✅ | Aave V3 事件签名确认 |
| E7 | Collateral 禁用 | `aave_v3_ethereum.Pool_evt_ReserveUsedAsCollateralDisabled` | ✅ | Aave V3 事件签名确认 |
| E8 | 利率/指数更新 | `aave_v3_ethereum.Pool_evt_ReserveDataUpdated` | ✅ | Dune 查询实例确认 |
| E9 | EMode 设置 | `aave_v3_ethereum.Pool_evt_UserEModeSet` | ✅ | Aave V3 事件列表确认 |
| E10 | 闪电贷 | `aave_v3_ethereum.Pool_evt_FlashLoan` | ✅ | Aave V3 事件列表确认 |

### 2.2 协议参数 → Dune Decoded Tables

| # | 数据需求 | Dune 表名 | 可用？ | 来源 |
|---|---------|----------|--------|------|
| P1 | LT/LTV 变更 | `aave_v3_ethereum.PoolConfigurator_evt_CollateralConfigurationChanged` | ✅ | Aave V3 GitHub 源码确认 |
| P2 | 资产初始化 | `aave_v3_ethereum.PoolConfigurator_evt_ReserveInitialized` | ✅ | Aave V3 事件列表确认 |
| P3 | EMode 配置 | `aave_v3_ethereum.PoolConfigurator_evt_EModeCategoryAdded` + `_EModeCategoryUpdated` | ✅ | Aave V3 事件列表确认 |
| P4 | 债务上限 | `aave_v3_ethereum.PoolConfigurator_evt_DebtCeilingChanged` | ✅ | Aave V3 事件列表确认 |
| P5 | 资产 EMode 归属 | `aave_v3_ethereum.PoolConfigurator_evt_ReserveEModeChanged` | ✅ | Aave V3 事件列表确认 |
| P6 | 容量限制 | `aave_v3_ethereum.PoolConfigurator_evt_BorrowCapChanged` + `_SupplyCapChanged` | ✅ | Aave V3 事件列表确认 |

### 2.3 价格数据 → Dune Curated Tables

| # | 数据需求 | Dune 表名 | 可用？ | 来源 |
|---|---------|----------|--------|------|
| PR1 | Token 历史价格 | `prices.usd` | ✅ | Dune 数据目录确认 |
| PR2 | Chainlink 预言机价格 | 需从 raw events 或 Chainlink decoded tables 获取 | ⚠️ 待验证 | 需进一步检查 |

### 2.4 Token 元数据 → Dune Curated Tables

| # | 数据需求 | Dune 表名 | 可用？ | 来源 |
|---|---------|----------|--------|------|
| T1 | Token decimals | `tokens.erc20` | ✅ | Dune 查询实例确认 |
| T2 | Token symbol | `tokens.erc20` | ✅ | Dune 查询实例确认 |

### 2.5 交易与 Trace 数据 → Dune Raw Tables

| # | 数据需求 | Dune 表名 | 可用？ | 来源 |
|---|---------|----------|--------|------|
| TX1 | 交易数据 | `ethereum.transactions` | ✅ | Dune 数据目录确认 |
| TX2 | Trace 数据 | `ethereum.traces` | ✅ | Dune 数据目录确认（Raw data 包含 trace） |
| TX3 | 事件日志 | `ethereum.logs` | ✅ | Dune 数据目录确认 |

### 2.6 地址标签 → Dune Curated Tables

| # | 数据需求 | Dune 表名 | 可用？ | 来源 |
|---|---------|----------|--------|------|
| L1 | 已知合约标签 | `labels.labels` | ✅ | Dune 数据目录确认 |

### 2.7 需要重建的数据 → 重建所需输入全部可用

| # | 重建数据 | 所需输入 | 输入全部可用？ |
|---|---------|---------|-------------|
| R1 | 历史 HF | E1-E2(supply/withdraw) + E6-E7(collateral) + P1(LT) + PR1(price) + T1(decimals) + R2(debt) + E9(EMode) | ✅ |
| R2 | 历史 Debt | E3(borrow) + E4(repay) + E8(ReserveDataUpdated for index) + T1(decimals) | ✅ |
| R3 | Collateral-enabled 状态 | E6(enabled) + E7(disabled) | ✅ |
| R4 | 主动/被动分类 | E1-E5(onBehalfOf) + TX1(from) + TX2(trace) + L1(labels) | ✅ |
| R5 | Borrower-position 面板 | R1 + R2 + R3 + E1-E5 | ✅ |

---

## 三、关键事件字段详情

### 3.1 Supply 事件

**Solidity 事件签名**（来源：Aave V3 GitHub + Gnosis Analytics Docs）：
```solidity
event Supply(
    address indexed reserve,     // 资产合约地址
    address user,                // 发起供应的地址（msg.sender）
    address indexed onBehalfOf,  // 实际供应受益人（可能不同于 user）
    uint256 amount,              // 供应数量（原始精度，需除以 decimals）
    uint16 indexed referralCode  // 推荐码
);
```

**Dune 表名**：`aave_v3_ethereum.Pool_evt_Supply`

**Dune 通用字段**（所有 decoded event 表都有）：
| 字段 | 类型 | 含义 |
|------|------|------|
| `evt_block_time` | timestamp | 事件所在区块的时间戳（**分区列，查询必须过滤**） |
| `evt_block_number` | integer | 事件所在区块号 |
| `evt_tx_hash` | string | 事件所在交易哈希 |
| `evt_index` | integer | 事件在交易中的索引 |
| `contract_address` | string | 发出事件的合约地址 |

**事件特定字段**：
| 字段 | 类型 | 含义 | 研究用途 |
|------|------|------|---------|
| `reserve` | string | 资产合约地址 | 识别哪种资产 |
| `user` | string | 发起者地址（msg.sender） | 主动/被动分类 |
| `onBehalfOf` | string | 实际受益人地址 | **关键：主动/被动分类** |
| `amount` | string | 原始精度金额 | 需除以 token decimals |
| `referralCode` | integer | 推荐码 | 可忽略 |

**研究中的关键用途**：
- 追踪每个地址的资产存入行为
- 通过 `onBehalfOf` 区分直接操作和委托操作（问题 02 修正）
- 结合 ReserveUsedAsCollateralEnabled 判断是否为抵押操作（问题 03 修正）

---

### 3.2 Withdraw 事件

**Solidity 事件签名**：
```solidity
event Withdraw(
    address indexed reserve,     // 资产合约地址
    address indexed user,        // 提取的用户地址
    address indexed to,          // 接收资产的地址
    uint256 amount               // 提取数量
);
```

**Dune 表名**：`aave_v3_ethereum.Pool_evt_Withdraw`

**事件特定字段**：
| 字段 | 类型 | 含义 | 研究用途 |
|------|------|------|---------|
| `reserve` | string | 资产合约地址 | 识别哪种资产 |
| `user` | string | 提取用户地址 | 追踪资产提取 |
| `to` | string | 接收地址 | 可能不同于 user |
| `amount` | string | 原始精度金额 | 需除以 token decimals |

**注意**：Withdraw 事件没有 `onBehalfOf` 参数（与 Supply/Borrow/Repay 不同）。`user` 是被提取的地址，`to` 是接收地址。

---

### 3.3 Borrow 事件

**Solidity 事件签名**：
```solidity
event Borrow(
    address indexed reserve,        // 借入资产地址
    address user,                   // 发起借入的地址（msg.sender）
    address indexed onBehalfOf,     // 实际债务承担者
    uint256 amount,                 // 借入数量
    uint8 interestRateMode,          // 利率模式（1=stable, 2=variable）
    uint256 borrowRate,             // 借款利率（ray 精度，除以 1e27）
    uint16 indexed referralCode     // 推荐码
);
```

**Dune 表名**：`aave_v3_ethereum.Pool_evt_Borrow`

**事件特定字段**：
| 字段 | 类型 | 含义 | 研究用途 |
|------|------|------|---------|
| `reserve` | string | 借入资产地址 | 识别哪种资产 |
| `user` | string | 发起者地址（msg.sender） | 主动/被动分类 |
| `onBehalfOf` | string | 债务承担者 | **关键：主动/被动分类** |
| `amount` | string | 原始精度金额 | 需除以 token decimals |
| `interestRateMode` | integer | 1=stable, 2=variable | 债务重建（利息计算方式不同） |
| `borrowRate` | string | 借款利率（ray） | Stable rate 债务的利息计算 |
| `referralCode` | integer | 推荐码 | 可忽略 |

---

### 3.4 Repay 事件

**Solidity 事件签名**：
```solidity
event Repay(
    address indexed reserve,     // 偿还资产地址
    address indexed user,        // 被偿还债务的用户
    address indexed repayer,     // 实际还款人（msg.sender，可能不同于 user）
    uint256 amount,              // 偿还数量
    bool useATokens              // 是否使用 aToken 还款
);
```

**Dune 表名**：`aave_v3_ethereum.Pool_evt_Repay`

**事件特定字段**：
| 字段 | 类型 | 含义 | 研究用途 |
|------|------|------|---------|
| `reserve` | string | 偿还资产地址 | 识别哪种资产 |
| `user` | string | 被偿还债务的用户 | 债务归属者 |
| `repayer` | string | 实际还款人 | **关键：主动/被动分类** |
| `amount` | string | 原始精度金额 | 需除以 token decimals |
| `useATokens` | boolean | 是否使用 aToken 还款 | 影响资金流追踪 |

**注意**：`repayer` 和 `user` 可能不同。如果 `repayer == user`，则是借款人自己还款（主动）；如果 `repayer != user`，可能是第三方代还或清算。

---

### 3.5 LiquidationCall 事件

**Solidity 事件签名**：
```solidity
event LiquidationCall(
    address indexed collateralAsset,           // 被清算的抵押资产
    address indexed debtAsset,                 // 被偿还的债务资产
    address indexed user,                      // 被清算的借款人
    uint256 debtToCover,                       // 偿还的债务金额
    uint256 liquidatedCollateralAmount,         // 被清算的抵押品金额
    address liquidator,                        // 清算者地址
    bool receiveAToken                         // 清算者是否接收 aToken
);
```

**Dune 表名**：`aave_v3_ethereum.Pool_evt_LiquidationCall`

**事件特定字段**：
| 字段 | 类型 | 含义 | 研究用途 |
|------|------|------|---------|
| `collateralAsset` | string | 被清算的抵押资产 | 分析哪种抵押品被清算 |
| `debtAsset` | string | 被偿还的债务资产 | 分析哪种债务被清算 |
| `user` | string | 被清算的借款人 | **RQ2 outcome 变量** |
| `debtToCover` | string | 偿还的债务金额 | 清算规模 |
| `liquidatedCollateralAmount` | string | 被清算的抵押品金额 | 清算损失 |
| `liquidator` | string | 清算者地址 | 清算者分析（MEV、竞争） |
| `receiveAToken` | boolean | 是否接收 aToken | 清算方式 |

---

### 3.6 ReserveUsedAsCollateralEnabled / Disabled 事件

**Solidity 事件签名**：
```solidity
event ReserveUsedAsCollateralEnabled(
    address indexed reserve,   // 资产地址
    address indexed user       // 启用抵押的用户
);

event ReserveUsedAsCollateralDisabled(
    address indexed reserve,   // 资产地址
    address indexed user       // 禁用抵押的用户
);
```

**Dune 表名**：
- `aave_v3_ethereum.Pool_evt_ReserveUsedAsCollateralEnabled`
- `aave_v3_ethereum.Pool_evt_ReserveUsedAsCollateralDisabled`

**事件特定字段**：
| 字段 | 类型 | 含义 | 研究用途 |
|------|------|------|---------|
| `reserve` | string | 资产地址 | 识别哪种资产的抵押状态变化 |
| `user` | string | 用户地址 | 追踪每个用户的 collateral-enabled 状态 |

**研究中的关键用途**：
- **这是问题 03 修正的核心数据**——区分 Supply 和 Collateral-Enabled Supply
- 重建每个地址在每个时间点的 collateral-enabled 状态
- 确保只有 collateral-enabled 的资产才计入 HF 计算

---

### 3.7 ReserveDataUpdated 事件

**Solidity 事件签名**：
```solidity
event ReserveDataUpdated(
    address indexed reserve,          // 资产地址
    uint256 liquidityRate,            // 供应利率（ray, /1e27）
    uint256 stableBorrowRate,         // 稳定借款利率（ray, /1e27）
    uint256 variableBorrowRate,       // 浮动借款利率（ray, /1e27）
    uint256 liquidityIndex,           // 流动性指数（ray, /1e27）
    uint256 variableBorrowIndex       // 浮动借款指数（ray, /1e27）
);
```

**Dune 表名**：`aave_v3_ethereum.Pool_evt_ReserveDataUpdated`

**事件特定字段**：
| 字段 | 类型 | 含义 | 研究用途 |
|------|------|------|---------|
| `reserve` | string | 资产地址 | 识别哪种资产的利率变化 |
| `liquidityRate` | string | 供应利率 | 供应者收益 |
| `stableBorrowRate` | string | 稳定借款利率 | Stable rate 债务利息 |
| `variableBorrowRate` | string | 浮动借款利率 | Variable rate 债务利息 |
| `liquidityIndex` | string | 流动性指数 | **关键：重建 variable rate 债务** |
| `variableBorrowIndex` | string | 浮动借款指数 | **关键：重建 variable rate 债务** |

**研究中的关键用途**：
- 重建历史债务（R2）的核心输入
- Variable rate 债务 = ScaledBalance × variableBorrowIndex
- 需要按时间追踪 Index 变化来重建历史债务

---

### 3.8 CollateralConfigurationChanged 事件（PoolConfigurator）

**Solidity 事件签名**（来源：Aave V3 GitHub 源码）：
```solidity
event CollateralConfigurationChanged(
    address indexed asset,              // 资产地址
    uint256 ltv,                        // LTV（bps, /10000）
    uint256 liquidationThreshold,       // 清算阈值 LT（bps, /10000）
    uint256 liquidationBonus            // 清算罚金（bps, /10000, >10000）
);
```

**Dune 表名**：`aave_v3_ethereum.PoolConfigurator_evt_CollateralConfigurationChanged`

**事件特定字段**：
| 字段 | 类型 | 含义 | 研究用途 |
|------|------|------|---------|
| `asset` | string | 资产地址 | 识别哪种资产的参数变化 |
| `ltv` | string | LTV 值（bps） | **追踪历史 LTV** |
| `liquidationThreshold` | string | LT 值（bps） | **追踪历史 LT（HF 公式的关键参数）** |
| `liquidationBonus` | string | 清算罚金（bps） | 追踪历史清算罚金 |

**研究中的关键用途**：
- **这是问题 01 修正的核心数据**——获取历史 LT 值用于正确重建 HF
- LT 值可能随 governance 提案变化，需要按时间追踪
- bps = basis points，/10000 得到小数（如 8300 bps = 0.83 = 83%）

---

### 3.9 UserEModeSet 事件

**Solidity 事件签名**：
```solidity
event UserEModeSet(
    address indexed sender,   // 用户地址
    uint8 categoryId          // EMode 类别 ID（0 = 退出 EMode）
);
```

**Dune 表名**：`aave_v3_ethereum.Pool_evt_UserEModeSet`

**研究中的关键用途**：
- 追踪每个地址的 EMode 状态
- EMode 下使用不同的 LT 值（通常更高），影响 HF 计算
- 需要结合 EModeCategoryAdded/Updated 获取每个 categoryId 对应的 LT 值

---

## 四、数据时间覆盖

### 4.1 Aave V3 Ethereum Mainnet 时间范围

| 数据 | 开始时间 | 来源 |
|------|---------|------|
| Aave V3 Pool 事件 | 2023-01-27（Ethereum mainnet 部署日） | Dune Aave V3 查询确认 |
| PoolConfigurator 事件 | 2023-01-27 | 同上 |
| 价格数据 | 更早（覆盖全部历史） | Dune prices.usd |
| Token 元数据 | 更早 | Dune tokens.erc20 |
| 原始交易/Trace 数据 | Ethereum 创世以来 | Dune ethereum.* |

**注意**：Aave V3 在 Ethereum mainnet 上的部署时间是 2023 年 1 月 27 日。如果需要更早的数据（如 2020-2022 年的借贷行为），需要使用 Aave V2 的数据（表名 `aave_v2_ethereum.*`）。但本研究的修正方案以 Aave V3 为主协议，因此 2023-01-27 之后的覆盖即可。

### 4.2 数据更新延迟

| 数据类型 | 延迟 | 来源 |
|---------|------|------|
| Raw 数据 | 最终性后数分钟内 | Dune 官方文档 |
| Curated 数据 | 每小时刷新 | Dune 官方文档 |

**结论**：对于历史数据分析（不是实时监控），数据延迟不影响研究可行性。
