# 协议间异同对比：设计目的、机制差异与对研究的影响

**文件定位**：六层矩阵技术文档  
**用途**：系统对比 Aave V3、Compound III、MakerDAO 三个协议的设计逻辑、机制差异，并分析这些差异对本研究（借款人仓位管理行为与清算倾向）的影响  
**关联文件**：`01_Aave_V3协议_Aave_V3.md`、`02_Compound_III协议_Compound_III.md`、`03_MakerDAO与Sky_MakerDAO_Sky.md`

---

## 1. 为什么需要这份对比文档

Qualifying Report v1 原计划将三个协议的数据直接拼接为一个面板数据集。构念效度审查发现，这三个协议的架构存在根本差异，直接拼接不仅在统计上可能误导，更在概念上不可比。本文件从设计目的出发，逐层拆解三个协议的异同，并明确这些差异对研究的影响。

---

## 2. 三个协议的设计目的

### Aave V3 — 通用流动性池

**设计目的**：打造一个去中心化的"资金池"——多个供应者将资产存入共享池，多个借款者从池中借出不同资产。协议的核心是让资金供需在池内自动匹配，通过算法利率调节供需平衡。

**关键设计逻辑**：
- 供应者和借款者面对同一个资产池，利率由池的利用率（utilization rate）决定
- 借款者可以借多种资产，抵押多种资产，仓位是一个"账户"概念而非独立金库
- 风险控制通过全局参数（LT、LTV、EMode、Isolation）实现，而非逐仓管理
- 清算是即时的：HF < 1.0 时，任何第三方可触发清算，liquidator 偿还债务并获取抵押品 + 罚金

**产生的效果**：
- 借款人的操作粒度细（可以同时借多种资产、灵活切换利率模式）
- 但仓位状态复杂（多种资产 × EMode/Isolation 状态 × 利率模式），HF 重建需要处理大量组合
- 清算是"点对点"即时执行，时间戳精确

### Compound III — 单一基础资产市场

**设计目的**：与 Aave 的"通用资金池"不同，Compound III 设计为每个市场只有一个可借的基础资产（base asset，如 USDC），供应其他资产作为抵押。其设计哲学是简化风险模型——只围绕一个基础资产管理借贷关系。

**关键设计逻辑**：
- 每个市场只有一个 base asset，借款者只能借这个资产
- 供应抵押资产后自动作为 collateral（无需单独 enable，与 Aave 不同）
- 使用双 Collateral Factor：borrowCF（决定借款能力）和 liquidateCF（决定清算触发），两者可以不同
- 风险指标是 Account Liquidity / Shortfall，不是 Health Factor
- 清算通过 `absorb` 机制：协议吸收欠款账户的抵押品，后续通过市场出售

**产生的效果**：
- 风险模型更简洁（只围绕一个 base asset），但牺牲了灵活性
- Supply = Collateral-Enabled 成立（与 Aave 的 Supply ≠ Collateral-Enabled 形成对比）
- 清算方式不同：协议自己吸收抵押品，而非 liquidator 直接偿还债务并获取抵押品
- 接口语义与 Aave 相反：Supply base asset = 还款，Withdraw base asset = 借款

### MakerDAO / Sky — 抵押金库与稳定币发行

**设计目的**：MakerDAO 的核心目标不是"借贷市场"，而是"去中心化稳定币发行"——用户通过锁定抵押品在 Vault 中生成 DAI（现为 USDS）稳定币。借贷只是实现稳定币发行的手段，而非目的本身。

**关键设计逻辑**：
- 每个 Vault 是独立的抵押金库，用户 lock 抵押品 → draw 生成 DAI
- 风险指标是 Collateralization Ratio，低于 Liquidation Ratio 触发清算
- 清算是拍卖制（Dutch auction 或 English auction），不是即时执行
- 借款资产固定为 DAI/USDS（单一稳定币）

**产生的效果**：
- 仓位结构最简单（一个 Vault 一个抵押品一种债务），但清算过程最复杂
- 清算是分阶段拍卖过程，时间跨度可能从几分钟到数小时
- "Realized liquidation" 的定义与 Aave/Compound 完全不同——不是一次即时交易，而是一个拍卖过程
- 不存在"Supply vs Collateral-Enabled"的问题——lock 就是抵押，没有中间状态

---

## 3. 核心机制对比

### 3.1 风险指标

| 维度 | Aave V3 | Compound III | MakerDAO |
|------|---------|-------------|----------|
| 风险指标 | Health Factor (HF) | Account Liquidity / Shortfall | Collateralization Ratio |
| 清算触发条件 | HF < 1.0 | Shortfall > 0 | Ratio < Liquidation Ratio |
| 指标本质 | 抵押调整价值 / 总债务 | 借款能力差额 / 清算差额 | 抵押价值 / 债务（比率形式） |
| 是否可比 | — | 不同标尺，不可直接比较 | 不同标尺，不可直接比较 |
| 预言机依赖 | Chainlink（直接影响 V_i） | Chainlink + Open Price Feed | MakerDAO 自有预言机（OSM） |
| 边界值 | HF = 1.0（机械 + 心理双重意义） | Shortfall = 0（纯机械） | Ratio = LR（纯机械） |

**对研究的影响**：三个协议的"清算风险"不在同一标尺上。Aave 的 HF=1.0 同时承载了心理参考点和机械阈值的含义（与 PT 识别问题相关），而 Compound 和 MakerDAO 的清算边界没有这个双重性质。如果将三者直接拼接，会丢失这种结构性差异。

### 3.2 仓位结构

| 维度 | Aave V3 | Compound III | MakerDAO |
|------|---------|-------------|----------|
| 基本单位 | User Account（多资产） | Account（多抵押品，单一 base asset 债务） | Vault（单一抵押品，单一债务） |
| 抵押品管理 | Supply + 独立 Collateral-Enabled | Supply = 自动 Collateral | lock = 直接抵押 |
| 借款资产 | 多种 | 单一 base asset | DAI/USDS |
| 仓位独立性 | 一个账户内多资产混合 | 一个账户内多抵押品 + 单一债务 | 每个 Vault 独立 |

**对研究的影响**：
- Aave 的"主动/被动分类"最复杂：需要处理 onBehalfOf、credit delegation、router 合约等多种路径
- Compound III 的 Supply = Collateral 成立，简化了抵押操作的定义，但接口语义与 Aave 相反，容易混淆
- MakerDAO 的 Vault 结构最简单，但"借款人行为"的粒度不同——一个用户可能有多个 Vault，行为分析的单位是 Vault 而非用户

### 3.3 清算机制

| 维度 | Aave V3 | Compound III | MakerDAO |
|------|---------|-------------|----------|
| 触发方式 | HF < 1.0，任何第三方可触发 | Shortfall > 0，任何第三方可调用 absorb | Ratio < LR，触发拍卖 |
| 执行方式 | Liquidator 偿还债务 → 获取抵押品 + 罚金 | 协议吸收抵押品 → 后续市场出售 | 拍卖（Dutch/English auction） |
| 执行时间 | 即时（单笔交易） | 即时（单笔交易） | 非即时（拍卖过程，可能数分钟到数小时） |
| 清算罚金 | Liquidation Bonus (5-10%) | 折扣吸收（discount 由协议设定） | Liquidation Penalty + 拍卖折扣 |
| "Realized Liquidation" 定义 | 一次 LiquidationCall 事件 | 一次 Absorb 事件 | 一个完整的拍卖过程（多个事件） |
| 借款人损失构成 | 罚金 + 被清算的抵押品 | 折扣损失 + 被吸收的抵押品 | 罚金 + 拍卖折扣 + 拍卖时间风险 |

**对研究的影响**：
- "清算"在三个协议中的定义不同：Aave 是一次即时交易，MakerDAO 是一个拍卖过程
- 清算的"时间戳"含义不同：Aave 是清算执行的区块时间，MakerDAO 是拍卖开始的区块时间，最终清算价格可能在数小时后才确定
- 这意味着三个协议的"清算前行为窗口"定义不能统一——Aave 可以用清算前 N 个区块，MakerDAO 需要考虑拍卖过程本身对借款人行为的影响

### 3.4 利率机制

| 维度 | Aave V3 | Compound III | MakerDAO |
|------|---------|-------------|----------|
| 利率类型 | Variable Rate + Stable Rate | 单一利用率曲线 | Stability Fee（固定费率） |
| 债务增长方式 | Variable: ScaledBalance × Reserve Index；Stable: 线性累积 | 基于利用率曲线，按 block 累积 | 按年化 Stability Fee 累积 |
| 对 HF 重建的影响 | 需要逐 block 追踪 Reserve Index | 需要逐 block 追踪利用率变化 | 相对简单，线性累积 |

**对研究的影响**：债务重建的复杂度因协议而异。Aave 最复杂（两种利率模式 + Reserve Index 追踪），MakerDAO 最简单（线性累积），Compound III 居中。

### 3.5 预言机机制

| 维度 | Aave V3 | Compound III | MakerDAO |
|------|---------|-------------|----------|
| 预言机 | Chainlink Price Feeds | Chainlink + Open Price Feed | MakerDAO 自有 OSM (Oracle Security Module) |
| 价格延迟 | 基本实时（Deviation threshold + Heartbeat） | 基本实时 | OSM 有 1 小时延迟（防止预言机操纵） |
| 对 HF 的影响 | 预言机价格 = 协议看到的价格 | 预言机价格 = 协议看到的价格 | OSM 延迟意味着协议价格滞后于市场 1 小时 |

**对研究的影响**：
- MakerDAO 的 OSM 1 小时延迟意味着借款人看到的市场价格和协议使用的价格之间存在时间差——借款人可能在协议价格尚未更新时就有动机调整仓位
- Aave 和 Compound 的预言机基本实时，但仍有更新延迟和 `minAnswer`/`maxAnswer` 限制
- 这进一步说明 Oracle 机制对研究的影响因协议而异

---

## 4. 三个协议的核心异同总结

### 相同点

1. 都是超额抵押借贷协议
2. 都使用预言机获取资产价格
3. 都有清算机制（但实现方式不同）
4. 都依赖链上事件记录（但事件结构不同）
5. 借款人的核心决策都围绕"何时调整仓位以避免清算"

### 关键差异

| 差异维度 | Aave V3 | Compound III | MakerDAO | 对研究的影响 |
|---------|---------|-------------|----------|-------------|
| 设计目的 | 通用流动性池 | 单一基础资产市场 | 稳定币发行 | 决定了借款人行为的动机不同 |
| 风险指标标尺 | HF（比率） | Shortfall（差额） | Collateralization Ratio（比率） | 不可直接比较，无法拼接 |
| 仓位单位 | Account（多资产） | Account（多抵押单债务） | Vault（单一抵押单一债务） | 行为分析的基本单位不同 |
| Supply vs Collateral | 独立状态 | 自动等价 | 直接 lock | 抵押操作的定义不同 |
| 清算执行 | 即时 | 即时 | 拍卖（非即时） | "清算"事件的时间定义不同 |
| 清算风险边界性质 | HF=1.0 有双重意义 | 纯机械边界 | 纯机械边界 | PT 识别问题仅存在于 Aave |
| 利率机制 | Variable + Stable | 利用率曲线 | Stability Fee | 债务重建复杂度不同 |
| 预言机 | Chainlink（实时） | Chainlink + OPF（实时） | OSM（1h 延迟） | 价格对行为的影响机制不同 |

---

## 5. 对研究的影响

### 5.1 不可拼接

三个协议的风险指标不在同一标尺上（HF vs Shortfall vs Collateralization Ratio），直接拼接面板数据在概念上不可比。应改为以 Aave V3 为主协议进行深度分析，Compound/MakerDAO 分别单独分析作为外部有效性检验。

### 5.2 外部有效性检验的含义需要重新定义

不能将"在 Compound/MakerDAO 上也观察到类似行为模式"简单等同于"结果具有外部有效性"。因为三个协议的清算机制、仓位结构、利率机制都不同，即使观察到类似的"清算前行为调整"模式，其驱动因素也可能不同。外部有效性检验应该关注的是"行为模式的稳健性"（在不同机制下是否仍然存在），而非"行为参数的可比性"（清算前的 HF 阈值是否一致）。

### 5.3 PT 识别问题的协议特异性

HF=1.0 的"心理参考点 + 机械阈值"双重性质是 Aave 特有的。Compound III 的 Shortfall=0 和 MakerDAO 的 Ratio=LR 都是纯机械边界，没有理由认为借款人会对这些阈值产生心理锚定。这意味着 PT 识别问题是 Aave 特有的，不能通过跨协议比较来解决（除非能找到一个"有心理参考点但无机械后果"的对照场景）。

### 5.4 数据重建难度差异

Aave V3 的 HF/Debt 重建最复杂（多资产 × EMode × Isolation × 双利率模式 × Reserve Index 追踪）。MakerDAO 相对最简单（单一抵押品 × 单一债务 × 线性利率），但清算事件需要追踪完整拍卖过程。Compound III 居中。

### 5.5 对协议范围决策的建议

基于以上分析，当前阶段建议：

1. **以 Aave V3 为唯一主协议**：所有核心分析基于 Aave V3，因为它的机制最复杂、数据最完整、且 PT 识别问题只存在于此
2. **Compound/MakerDAO 作为后续外部有效性检验**：在 Aave V3 的核心结果出来后，再评估是否有必要投入精力在 Compound/MakerDAO 上做稳健性检验
3. **如果要做外部有效性检验**：重点不是验证"参数是否一致"，而是验证"行为模式是否稳健"——即在不同清算机制和仓位结构下，借款人是否仍然表现出清算前的主动调整行为

---

## 6. 文档信息

| 项目 | 内容 |
|------|------|
| 创建日期 | 2026-08-12 |
| 关联文件 | `01_Aave_V3协议_Aave_V3.md`、`02_Compound_III协议_Compound_III.md`、`03_MakerDAO与Sky_MakerDAO_Sky.md` |
| 使用位置 | Paper 1 协议范围决策、外部有效性检验设计 |
