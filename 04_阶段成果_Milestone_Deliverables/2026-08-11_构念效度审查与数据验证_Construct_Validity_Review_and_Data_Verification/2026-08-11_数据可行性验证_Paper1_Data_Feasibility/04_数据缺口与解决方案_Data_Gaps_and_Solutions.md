# 数据缺口与解决方案

**日期**：2026-08-11

---

## 一、数据缺口总览

经过逐项验证，Paper 1 的数据缺口可以分为三类：

| 缺口类型 | 数量 | 严重程度 | 说明 |
|---------|------|---------|------|
| 可弥补的缺口 | 2 | 低 | 需要额外步骤但可以解决 |
| 需要重建的数据 | 5 | 中 | 不是缺口，但需要研究者编程实现 |
| 不可获取的数据 | 1 | N/A | 研究边界，不是数据缺口 |

---

## 二、可弥补的缺口

### 缺口 1：Chainlink 原始预言机价格

**缺口描述**：我们需要确保 HF 重建中使用的价格与协议参与者在当时看到的价格一致。Aave V3 使用 Chainlink 作为价格预言机，因此理论上应该使用 Chainlink 的历史价格。

**当前状态**：`prices.usd` 表提供历史价格，但其价格来源未明确说明是否包含 Chainlink 数据。

**解决方案**（按优先级排序）：

```
方案 A（推荐）：使用 prices.usd 作为价格来源
  理由：
    1. prices.usd 是 Dune 维护的 curated 价格表，来源包括 DEX 交易和预言机
    2. 对于历史 HF 重建，价格精度到分钟级已经足够
    3. Chainlink 价格和 DEX 价格在正常市场条件下差异很小
    4. 简化数据管道，减少依赖

方案 B：从 ethereum.logs 解析 Chainlink AnswerUpdated 事件
  理由：
    1. 可以获取与 Aave 协议使用的完全一致的价格
    2. 方法见 05_Dune_Raw_Tables.md 中的查询示例
  缺点：
    1. 增加数据管道复杂度
    2. 需要处理 Chainlink 价格的精度转换

方案 C：检查 Dune 上是否有 Chainlink decoded tables
  方法：
    在 Dune Data Explorer 中搜索 "chainlink" 或输入 Chainlink Price Feed 合约地址
  如果有：直接使用
  如果没有：使用方案 A 或 B
```

**建议**：先使用方案 A（prices.usd），在稳健性检验中使用方案 B 交叉验证。

### 缺口 2：已知合约地址库（Safe / Router / Automation）

**缺口描述**：主动/被动分类需要识别交易发起者是否为 Safe 钱包、Router 合约或自动化服务。Dune 的 `labels.labels` 表提供部分标签，但可能不覆盖所有需要的合约。

**解决方案**：

```
Step 1: 使用 Dune labels.labels 获取已有标签
  → 获取已标记为 exchange, protocol, DAO 等的地址

Step 2: 手动维护已知合约地址列表
  来源：
    - Etherscan 标签页面 https://etherscan.io/labels
    - Gnosis Safe 官方文档（Safe 代理合约地址有规律）
    - 1inch, Paraswap, Uniswap Router 官方文档
    - DefiSaver, Gelato 等自动化服务文档
    - 社区维护的 liquidator 地址列表

Step 3: 将手动列表作为 uploaded table 导入 Dune
  → 上传 CSV 文件到 Dune
  → 在 SQL 查询中 JOIN 这个列表

Step 4: 持续更新
  → 随着时间推移，新的 Router 和自动化服务可能出现
  → 需要定期更新地址列表
```

**风险等级**：低。这是 DeFi 研究中的标准做法，不需要特殊技术。

---

## 三、需要研究者重建的数据

以下数据不是"缺口"——所有输入数据都在 Dune 上可用——但 Dune 不直接提供计算结果，需要研究者编程重建。

### 重建 1：历史 HF 值

```
为什么不直接可用？
  HF 是一个计算值，不是链上事件。Aave 合约在内部计算 HF，
  但不发出包含 HF 值的事件。必须从事件和参数重建。

重建所需输入（全部在 Dune 可用）：
  1. 抵押品数量 → Supply / Withdraw 事件 + collateral-enabled 状态
  2. 抵押品价值 → prices.usd
  3. LT 值 → CollateralConfigurationChanged 事件 + EMode 配置
  4. 债务数量 → Borrow / Repay 事件 + ReserveDataUpdated（利息累积）
  5. 债务价值 → prices.usd
  6. EMode 状态 → UserEModeSet 事件

重建复杂度：中高
重建方法：
  按区块或按天，对每个 borrower position：
    Step 1: 获取所有 collateral-enabled 资产的数量和价值
    Step 2: 获取适用的 LT 值（考虑 EMode）
    Step 3: 获取所有债务的数量和价值（含利息累积）
    Step 4: HF = Σ(collateral_value × LT) / debt_value
```

### 重建 2：历史 Debt 值

```
为什么不直接可用？
  债务随利息累积，但 Aave 不发出包含当前债务总额的事件。
  Variable rate 债务 = ScaledBalance × variableBorrowIndex
  需要按区块追踪 Index 变化。

重建所需输入（全部在 Dune 可用）：
  1. Borrow 事件 → 增加 ScaledBalance
  2. Repay 事件 → 减少 ScaledBalance
  3. ReserveDataUpdated → 获取 variableBorrowIndex 变化
  4. Borrow 事件中的 borrowRate → Stable rate 债务的利息计算

重建复杂度：高（需要按区块追踪 Index）
```

### 重建 3：Collateral-enabled 状态时间线

```
为什么不直接可用？
  Aave 不发出包含当前 collateral-enabled 状态的快照事件。
  但每次状态变化都有事件记录。

重建所需输入（全部在 Dune 可用）：
  1. ReserveUsedAsCollateralEnabled 事件
  2. ReserveUsedAsCollateralDisabled 事件

重建复杂度：低（只需按时间排列 enabled/disabled 事件）
```

### 重建 4：主动/被动分类

```
为什么不直接可用？
  主动/被动是研究者的分析分类，不是链上原生概念。

重建所需输入（全部在 Dune 可用）：
  1. 事件中的 onBehalfOf 参数
  2. ethereum.transactions 中的 from
  3. ethereum.traces 中的调用链
  4. labels.labels + 手动合约地址列表

重建复杂度：中
```

### 重建 5：最终分析面板

```
将以上所有重建结果组合为 borrower-position-day/month 面板：
  - HF 轨迹（R1）
  - Debt 轨迹（R2）
  - Collateral-enabled 状态（R3）
  - 主动/被动分类（R4）
  + 原始事件数据

重建复杂度：高（最终组装）
```

---

## 四、不可获取的数据

### 借款人经济意图

```
不可获取的原因：
  借款人为什么借这笔钱、借钱后拿去干嘛了——这些信息不在链上。
  链上只能看到 token 转账（Transfer），但看不到转账的经济目的。

这不是数据缺口，而是研究边界：
  → 已在 05_不可声称清单.md §3.1 中声明
  → 已在问题 04 修正中降级为"协议事件可观测；经济目的不可观测"

如果未来需要获取经济意图：
  → 需要链下数据（如交易所 KYC、支付平台数据等）
  → 这不是 Paper 1 的范围
```

---

## 五、建议的数据获取顺序

```
Phase 1：验证阶段（1-2 天）
  Step 1: 在 Dune Data Explorer 中确认所有表名存在
          → 搜索 "aave_v3_ethereum" namespace
          → 确认 Pool 和 PoolConfigurator 的 decoded tables
  
  Step 2: 编写测试查询，验证字段完整性
          → 查询 Pool_evt_Supply，确认 onBehalfOf 字段有值
          → 查询 PoolConfigurator_evt_CollateralConfigurationChanged，确认 LT 字段
          → 查询 Pool_evt_ReserveUsedAsCollateralEnabled，确认事件存在
  
  Step 3: 验证价格数据覆盖
          → 确认 prices.usd 覆盖 Aave V3 使用的所有资产

Phase 2：数据重建阶段（1-2 周）
  Step 4: 构建 collateral-enabled 状态时间线（R3，最简单）
  Step 5: 构建历史 LT 参数时间线（从 PoolConfigurator 事件）
  Step 6: 构建历史债务重建（R2，复杂度最高）
  Step 7: 构建历史 HF 重建（R1，依赖 R2）
  Step 8: 构建主动/被动分类（R4）
  Step 9: 组装最终分析面板（R5）

Phase 3：验证与稳健性（1 周）
  Step 10: 与 Dune curated Lending 数据集交叉验证
  Step 11: 抽样人工核验（选取已知事件，验证重建结果）
  Step 12: 如果需要，使用 Chainlink 原始价格交叉验证 HF
```