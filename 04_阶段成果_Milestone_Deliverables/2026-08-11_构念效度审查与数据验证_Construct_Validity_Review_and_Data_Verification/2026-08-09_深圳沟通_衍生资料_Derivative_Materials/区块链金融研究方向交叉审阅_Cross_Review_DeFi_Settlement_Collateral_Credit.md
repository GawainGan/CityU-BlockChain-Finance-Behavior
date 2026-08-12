# 区块链金融研究方向交叉审阅：DeFi 行为、结算可观测性、质押/抵押与信用形成

> 基于现有 Qualifying Report《Risk Behavior and Credit Signals in DeFi Lending Markets: Borrower Active Adjustment Under Position Risk Accumulation》以及 2026-08-09 区块链支付/结算会议内容进行交叉审阅，并结合外部行业资料与相关研究扩展。
>
> 核心目标：检查现有 Report 是否遗漏 settlement；判断 settlement 的可观测性和数据来源；检查“从链上历史识别用户行为”是否存在 purpose / intention 不可识别问题；检查“区块链金融是否依赖质押/抵押，以及该模式是否违背 blockchain-native 属性”；最后将 DeFi、支付、结算、KYC、抵押与信用形成串成完整研究主线。

## 一、总判断

最重要的结论不是“原研究方向错了”，而是原 Report 把不同层次的内容都放进了 **on-chain behavior** 这个概念里。

Aave、Compound 等借贷协议中的 Borrow、Repay、Supply/Deposit、Withdraw、Liquidation，属于**协议语义明确的链上金融操作**。这类行为可以从智能合约事件和状态变化中较高精度观测。

但普通的钱包转账，例如：

```text
Wallet A → Wallet B
10,000 USDT
2026-08-09 14:32
```

链上通常只告诉我们 sender、receiver、token、amount、timestamp、transaction hash 和 contract interaction。它不会直接告诉研究者这是购买商品、工资、供应商货款、企业内部资金归集、跨境贸易结算、借款、OTC 还是个人转账。

因此必须明确区分：

> **Protocol-recorded action**
> 与
> **Underlying economic behavior / economic purpose**

现有 Report 对前者具有较好的识别能力，但无法仅依赖 public on-chain data 完整识别后者。这是接下来必须建立的 identification boundary。

## 二、Settlement 必须拆成三个不同概念

### 2.1 Technical / Ledger Settlement

这是底层区块链意义上的 settlement：

```text
A → B 10,000 USDC
broadcast
↓
included in block
↓
executed
↓
state updated
↓
finalized
```

这一层可以观察 sender、receiver、token、amount、transaction、block、execution status、event logs 和 finality，因此 **technical settlement 是高度可观测的**。

Ethereum 上可以通过 JSON-RPC、archive node 或 indexer 获取，例如：

```text
eth_getTransactionByHash
eth_getTransactionReceipt
eth_getLogs
eth_getBlockByNumber
```

### 2.2 Protocol-level Financial Action

第二层是协议内部的金融语义，例如：

```text
Aave.Repay
Aave.Borrow
Aave.Supply
Aave.Withdraw
Uniswap.Swap
Compound.Borrow / Repay
```

这些操作通过 contract ABI、event、function call 和 protocol state 编码了明确的金融动作。

例如：

```text
Repay(user=X, asset=USDC, amount=10,000)
```

至少可以较高置信地解释为：某个账户或代理方正在偿还 Aave 借贷头寸。

我们仍然不知道这个人的心理动机是什么，但知道这笔链上 action 的 **protocol-level function** 是什么。这正是现有 Report 的主要优势。

### 2.3 Economic / Business Settlement

第三层才是会议中真正讨论的 settlement。

例如：

```text
Company A → Company B
150,000 USDT
```

链上可以看到 sender、receiver、amount、token、timestamp，但它可能代表：

```text
supplier payment
invoice settlement
payroll
OTC settlement
treasury rebalance
exchange deposit
loan repayment
capital contribution
internal transfer
cross-border trade settlement
```

仅从公链记录，通常无法直接得到真实商业目的。

因此最准确的结论是：

> **Settlement execution is observable.**
>
> **Settlement economic purpose is only partially observable or inferable.**
>
> **Ground-truth commercial purpose is generally not observable from public blockchain data alone.**

## 三、结算到底能不能被观测？

不是简单的“能”或“不能”。

| 信息层级 | 可观测程度 | 示例 |
|---|---:|---|
| Transaction executed | 很高 | A → B 10,000 USDT |
| Token / Amount / Time | 很高 | USDT / 10k / 14:32 |
| Smart-contract action | 很高 | Borrow / Repay / Swap |
| Counterparty type | 中高，可推断 | Binance / payment processor |
| Wallet entity | 部分可识别 | 某交易所、机构、协议 |
| Payment vs investment | 可分类，但存在误差 | heuristic/model |
| B2B / C2B / B2C / C2C | 可推断 | enriched classification |
| Supplier / Payroll 等类别 | 可推断 | model-based purpose |
| 某张 invoice 的具体付款 | 通常不可见 | 需要企业数据 |
| Why / 真实经济动机 | 通常不可直接观察 | 需要链下数据 |

因此，如果研究想从 Wallet transaction history 直接推出真实经济行为，会存在 identification gap。

## 四、市场上已经存在用于 Payment / Settlement 语义增强的数据平台

### 4.1 Dune

适合 raw transaction、logs、decoded event、decoded call、DeFi protocol states、lending events 和 wallet activity。

它非常适合现有 Report，因为需要重建 Borrow、Repay、Deposit/Supply、Withdraw、Liquidation。

但 Dune 本身通常不会告诉你“为什么这笔 USDT transfer 发生”。

因此：

> Dune 很适合 Protocol Behavior；不足以单独解决 Economic Purpose。

### 4.2 Allium

Allium 是目前与你“Payment vs Settlement”问题最匹配的平台之一。

其 stablecoin 数据体系已经提供类似：

```text
raw transfers
↓
enriched transfers
↓
organic activity classification
↓
payment categorization
```

并可能产生：

```text
transaction_type:
- Real-World Payment
- Investment/Trade
- Store as Value
- Unclassified
```

进一步分类为：

```text
C2C
C2B
B2C
B2B
```

以及：

```text
P2P Remittance
Retail Purchase
Service Payment
Salary/Payroll
Supplier Payment
Large B2B Settlement
Institutional Settlement
```

这与会议中讨论的“到底是 payment 还是 settlement”非常接近。

但必须注意：Allium 的 payment purpose 不是 ground truth，而是依赖 wallet label、counterparty type、transaction pattern、amount、behavioral heuristics 和 classification model 推断。因此论文中应称为 **inferred payment purpose**。

### 4.3 Nansen

主要价值是：

```text
Wallet
↓
Entity label
↓
Behavioral label
↓
Counterparty profile
```

可以辅助回答“这个地址更可能属于谁/什么机构”，但不等于回答“为什么这笔 transfer 发生”。

### 4.4 Chainalysis / TRM Labs / Elliptic

这类企业级平台更强于 Address attribution、Entity clustering、Transaction monitoring、Fund flow、KYT 和 AML risk，可以补足身份和机构标签，但同样无法保证提供 invoice-level economic purpose。

### 4.5 Artemis / Visa Onchain Analytics

更适合 stablecoin market statistics、adjusted transfer volume、payment volume、cross-border activity 和 industry benchmark，不适合作为个人行为 ground truth。

### 4.6 数据平台优先级

| 平台 | 核心用途 | 与研究的关系 |
|---|---|---|
| Dune | Protocol events / state reconstruction | Paper 1 主数据 |
| Allium | Payment / settlement semantic enrichment | Paper 2 最重要候选 |
| Nansen | Entity / wallet labeling | 补充主体信息 |
| Chainalysis | Entity attribution / KYT | 企业级身份增强 |
| TRM / Elliptic | Risk / attribution | 身份和资金网络 |
| Artemis | Stablecoin benchmark | 行业验证 |
| Visa Onchain Analytics | Stablecoin payment benchmark | 行业验证 |

如果最终目标是 KYC + 用户身份 + 真实消费场景 + payment purpose + 信用结果，那么真正的 gold-standard 数据仍然是支付机构自己的私有数据库。

理想的数据结构：

```text
KYC_ID
↓
Wallet
↓
Order_ID
↓
Merchant
↓
MCC / Category
↓
Amount
↓
Payment Timestamp
↓
Settlement Batch
↓
Refund
↓
Loan / Repayment / Default Outcome
```

## 五、这是否意味着现有 Report 的核心思路存在问题？

如果研究目标是“从任意钱包 transaction history 判断这个人在现实世界进行了什么经济活动”，那么存在严重问题：

\[
	ext{On-chain Transfer}
eq	ext{Economic Purpose}
\]

但现有 Report 并不是完全建立在这种假设之上。其核心数据包括 Deposit/Supply、Withdraw、Borrow、Repay、LiquidationCall、FlashLoan，因此更接近研究：

> **Protocol-observable position-management behavior**

而不是普通 wallet 的现实世界消费行为。

所以现有 Report 不会因为 purpose 不可观测而整体失效，但必须更严格地限定 claim。

## 六、严格审阅现有 Report 后发现的八个关键问题

### 6.1 “Complete observability of borrower behavior” 表述过强

Report 前文强调 complete observability of borrower behavior，但第 5.5 节又承认 Partial observability of user behavior 与 Cannot infer intent from on-chain data。

更准确的写法应是：

> **complete observability of protocol-recorded actions**

或：

> **high-granularity observability of on-chain protocol interactions**

因为研究无法完整观察 CEX hedge、OTC、off-chain liquidity、其他钱包、实际身份、真实经济目的和心理动机。

这是 construct validity 问题。

### 6.2 Liquidation ≠ Credit Default

这是比 Settlement 更严重的理论问题。

当前 RQ2 被称为 Credit Layer，并试图使用 future liquidation 作为 credit outcome。但在 overcollateralized DeFi 中，liquidation 可能来自 ETH 暴跌、杠杆过高、没有及时补抵押、Gas 成本、用户主动放弃救仓等原因，不能直接说明 borrower 的传统信用差。

因此当前研究更准确地识别：

> **Position risk-management quality**

或：

> **Liquidation propensity**

而不是严格意义上的 borrower creditworthiness。

### 6.3 `msg.sender == borrower` 不能一般性代表主动行为

Report §4.3 当前定义：

```text
msg.sender == borrower wallet
→ active action
```

这一规则过于简单。

Aave 等协议支持 onBehalfOf，还存在 credit delegation、gateway、router、adapter、smart wallet、automation、third-party repay、account abstraction。

更合理的是重建：

```text
Transaction initiator
↓
Intermediate contract
↓
Protocol call
↓
onBehalfOf
↓
Debt owner / collateral owner
↓
State beneficiary
```

然后再定义 borrower-authorized action。

### 6.4 Health Factor 公式需要技术修正

当前 Report 使用类似：

\[
HF_t=rac{\sum_i(C_{i,t}P_{i,t})LTV_i}{D_t}
\]

但 Aave Health Factor 应使用 **Weighted Average Liquidation Threshold**，而不是普通 LTV。

更接近：

\[
HF_t=rac{\sum_i V_{i,t}LT_i}{D_t}
\]

其中 \(V_{i,t}\) 为抵押资产价值，\(LT_i\) 为 liquidation threshold，\(D_t\) 为债务价值。

LTV 和 liquidation threshold 是不同参数。这是 examiner 很容易发现的硬错误。

### 6.5 Aave / Compound / Maker 不应简单统一成 HF → 1

不同协议的 liquidation mechanism 并不完全相同：

```text
Aave → Health Factor
Compound → account liquidity / shortfall
Compound III → liquidation collateral factor
Maker → vault collateralization / liquidation structure
```

更好的跨协议变量是：

\[
	ext{Distance to Liquidation}_{i,t}
\]

然后针对不同 protocol 用各自真实机制计算，再标准化成 protocol-normalized distance-to-liquidation metric。

### 6.6 Supply / Deposit 不一定等于 Collateral Addition

在 Aave 中，supplied asset 是否作为 collateral 是独立状态。

因此：

```text
Supply
```

不一定等于：

```text
Risk-reducing collateral addition
```

需要区分 Supply 与 Collateral-enabled Supply。

### 6.7 Daily-frequency risk reconstruction 可能太粗

研究核心是 borrower 接近 liquidation threshold 时什么时候反应。

例如：

```text
13:00 HF = 1.18
↓
13:08 Repay
↓
13:16 Price recovery
```

如果只看 daily data，整个行为过程可能消失。

更合理的方法是：

```text
Block / Transaction-level reconstruction
↓
Hourly aggregation
↓
Daily analytical panel
↓
Monthly borrower-position panel
```

即底层轨迹高频重建，最终回归面板可以低频。

### 6.8 Prospect Theory 的 Reference Point Identification 还不够强

HF=1 不仅可能是 psychological reference point，同时也是 protocol mechanism discontinuity。

一旦跨过阈值，第三方 liquidation becomes possible。

因此：

```text
Behavioral explanation:
Reference-point effect / Loss aversion

vs.

Rational explanation:
Avoid liquidation penalty / Avoid collateral loss
```

所以：

\[
Behavioral\ discontinuity
eq Prospect\ Theory\ evidence
\]

除非进一步构造识别策略。

Prospect Theory 更适合作为 theoretical framing / competing explanation，而不是过早宣称已经找到 behavioral bias。

## 七、Settlement 不应该强行塞进当前这篇 Paper

现有 Report 的核心问题非常具体：

> 当 collateralized DeFi borrower 接近 liquidation risk 时，他如何调整自己的 position？

它研究的是 Protocol-native financial behavior。

会议中新出现的 settlement 问题是：

> Stablecoin 用户真实进行的是 payment、B2B settlement、remittance 还是其他经济行为？

这是另一个 identification problem。

因此不建议直接把 Settlement 加入现有 Paper。

### Paper 1：Protocol-Level Borrower Behavior

```text
Collateralized DeFi Lending
↓
Risk Accumulation
↓
Borrower Active Adjustment
↓
Liquidation Risk
```

核心：Protocol-observable position-management behavior。

数据：Aave、Compound、Maker、Dune/RPC。

### Paper 2：Payment / Settlement Behavior

```text
Stablecoin Transfer
↓
Payment vs Settlement Classification
↓
Economic Behavior Pattern
↓
Potential Credit Signal
```

核心问题：一个 transfer 到底代表什么 economic activity？

数据：Allium、Nansen、Chainalysis、Payment company data。

### Paper 3：Behavior-informed On-chain Credit

```text
Position-management Behavior
+
Payment / Settlement Behavior
+
Identity / Reputation
```

↓

```text
Credit Signal
```

↓

```text
Can required collateral be reduced?
```

这样形成一条连续的 PhD research program。

## 八、区块链金融是不是“都需要质押”？

这里首先必须纠正术语。

很多时候现在说的“质押”实际指：

> **Collateralization**

而不是：

> **Staking**

### Staking

例如：

```text
Ethereum validator
↓
32 ETH
↓
PoS consensus
```

这是共识层质押。

### Collateral

例如：

```text
Deposit ETH
↓
Borrow USDC
```

这是金融借贷中的抵押品。

以后论文中最好严格区分 staking 与 collateralization。

## 九、并不是所有 Blockchain Finance 都依赖 Collateral

支付、普通 stablecoin transfer、DEX spot swap、DAO governance 等都不等于 collateralized finance。真正高度依赖 collateral 的主要是：

> **Permissionless pseudonymous DeFi lending**

即便 DeFi lending 中也存在例外，例如 Flash Loan、credit delegation、undercollateralized lending、reputation-based lending、delegated underwriting、real-world credit structures。

因此不能提出：

> Blockchain finance = collateralized finance

但可以更严谨地提出：

> **Permissionless pseudonymous DeFi lending has historically relied heavily on overcollateralization.**

## 十、“抵押不符合 Blockchain-native”这一观点需要反过来理解

原来的直觉是：

> Collateral 是传统金融旧逻辑被搬到区块链上。

但理论上 Overcollateralization 恰恰非常 blockchain-native。

因为 permissionless blockchain 往往具有：

```text
Pseudonymous user
+
No legal identity
+
No traditional credit bureau
+
No relationship banking
+
No court-based enforcement
```

因此：

```text
No trust
↓
Need economic security
↓
Collateral
↓
Overcollateralization
↓
Automatic liquidation
```

所以：

> **Collateralization is a native trust-substitution mechanism in pseudonymous DeFi.**

它不是因为“照搬传统金融”才出现，而是因为协议不知道你是谁、无法通过法院追债，也无法判断你的未来收入，于是最简单且可编程的方法就是要求预先提供资产。

## 十一、真正值得批判的不是“它不够 Blockchain-native”，而是“它可能没有真正解决 Credit”

传统信用体系：

```text
Who are you?
+
Income
+
Payment history
+
Repayment history
+
Assets
+
Ability to repay
+
Willingness to repay
```

↓

```text
Creditworthiness
```

↓

```text
Loan
```

典型 overcollateralized DeFi：

```text
How much collateral do you have?
↓
LTV
↓
Loan
↓
HF deteriorates
↓
Liquidation
```

因此 DeFi 并没有真正回答“这个人是否值得信用”，而是绕开了这个问题。

例如：

```text
Borrower wants $100
```

协议回答：

```text
Give me $150 collateral first.
```

于是协议不需要判断你会不会还，因为如果你不还，它可以出售 collateral。

因此一个更强的理论表述是：

> **Overcollateralization is a trust-substitution mechanism, not a credit-assessment mechanism.**

## 十二、这也是现有 DeFi Lending 与传统 Credit Intermediation 的根本区别

传统银行承担的功能之一，是把对 borrower future cash flow 的判断转化为现在的信用额度。

而典型 DeFi overcollateralized lending 更像：

```text
Existing wealth
↓
Locked as collateral
↓
Borrow liquidity
```

如果 $150 assets 才能借 $100，它并没有真正解决“缺乏现有资产的人如何获得信用”。

因此从金融功能角度，它更接近：

> collateralized leverage / liquidity transformation

而不完全等价于：

> unsecured or cash-flow-based credit creation。

## 十三、这个方向已经存在相关研究

近年的一些研究已经开始提出：

```text
On-chain history
↓
Credit score
↓
Reduce collateral requirement
```

也出现：

```text
Delegated underwriting
Reputation
Repayment-earned credit
Sponsor-based credit
```

等模型。

这些研究试图解决的本质问题与当前思路非常接近：

> 能不能让 observable behavior 替代一部分 collateral？

也就是说，不再只用 Assets 来保护 lender，而是加入 Behavior、Reputation、Payment history、Repayment history、Economic activity 等信息。

## 十四、可以重新定义整个研究主线

原 Report：

\[
HF
ightarrow Borrower\ Adjustment
ightarrow Liquidation
\]

可以被重新解释为第一阶段：

\[
Collateral
ightarrow Protocol\ Position
ightarrow Position\ Management\ Behavior
\]

第二阶段研究：

\[
Wallet
ightarrow Payment/Settlement\ History
ightarrow Economic\ Behavior\ Signals
\]

第三阶段：

\[
Position\ Behavior+Payment/Settlement\ Behavior+Identity/Reputation
\]

↓

\[
Credit\ Signal
\]

↓

\[
Reduced\ Collateral\ Requirement
\]

最终形成更大的研究问题：

> **Can observable economic behavior substitute for collateral in trust-minimized on-chain credit?**

中文：

> **链上可观测的经济行为，能否替代一部分抵押品在去信任信贷中的信息与担保功能？**

这比单纯“DeFi borrower 的行为能不能预测 liquidation”更接近一个完整的金融研究问题。

## 十五、现有 Report 与新研究方向的关系

现有 Report 不需要推翻。

第一阶段：**Protocol-native Behavior**

```text
DeFi lending
↓
Position risk
↓
Borrower active adjustment
↓
Liquidation
```

目标：证明 protocol-level behavioral process 是否携带额外风险信息。

第二阶段：**Economic Transaction Behavior**

```text
Stablecoin activity
↓
Payment / Settlement
↓
Economic purpose inference
↓
Behavior profile
```

目标：判断链上转账是否能够被恢复成具有经济含义的行为数据。

第三阶段：**On-chain Credit Formation**

```text
Collateral
+
Position behavior
+
Payment behavior
+
Settlement behavior
+
Identity / Reputation
```

↓

```text
Creditworthiness
```

↓

```text
Lower collateral / undercollateralized credit
```

## 十六、最终核心判断

当前最值得保留的理论判断不是：

> **Collateral does not fit blockchain-native finance.**

因为 collateralization 在 pseudonymous、trustless、permissionless 环境中非常自然。

更严谨、更有研究价值的判断是：

> **Collateralization is blockchain-native as a trust-substitution mechanism, but it may be economically incomplete as a credit-intermediation mechanism.**

中文：

> **抵押机制在技术层面高度符合去信任区块链的原生逻辑，因为它用可编程资产替代了身份、信任和法律执行；但在金融功能层面，它可能并没有完成真正的信用中介，因为它绕过了对借款人信用能力的识别。**

进一步可以形成：

> **The central challenge is not whether blockchain finance should eliminate collateral, but whether observable economic behavior can progressively substitute for collateral as a source of credit information and economic security.**

中文：

> **真正值得研究的问题，不是区块链金融是否应该取消抵押，而是：随着链上经济行为变得越来越可观测，我们是否能够用行为信息逐步替代一部分抵押品所承担的信息与担保功能。**

这可以把 DeFi、Collateral、Liquidation、Payment、Settlement、KYC、Behavior、Credit 全部连接到同一条研究主线上。
