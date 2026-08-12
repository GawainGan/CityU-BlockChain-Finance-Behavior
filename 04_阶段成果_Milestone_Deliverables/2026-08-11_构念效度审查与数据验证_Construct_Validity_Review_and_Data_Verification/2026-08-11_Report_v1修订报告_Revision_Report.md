# Report v1 修订报告

**日期**：2026-08-11  
**作者**：甘轶伟 (Yiwei Gan)  
**修订对象**：2026-07-17 Qualifying Report（以下简称"Report v1"）  
**修订范围**：基于六层矩阵（Definition → Construct → Measurement → Observable → Identification → Allowed Claim）对 Report v1 进行逐概念审查后发现的 11 个问题

---

## 目录

- [第一部分：概述与背景](#第一部分概述与背景)
- [第二部分：问题总览](#第二部分问题总览)
- [第三部分：逐问题详细说明](#第三部分逐问题详细说明)
- [第四部分：文献变更清单](#第四部分文献变更清单)
- [第五部分：术语变更清单](#第五部分术语变更清单)
- [第六部分：信息来源](#第六部分信息来源)

---

# 第一部分：概述与背景

## 1.1 本报告的目的

这份报告的目的是**完整记录**我们对 Report v1 进行的所有修订工作。具体来说，它回答以下五个问题：

1. **我们发现了什么问题？** —— 基于"六层矩阵"框架，对 Report v1 中的每一个核心概念进行了系统性审查，发现了 11 个问题。
2. **问题的根源在哪里？** —— 每个问题不是孤立的笔误，而是反映了深层的构念效度（construct validity）问题——即"我们声称在测量的东西"和"我们实际能从数据中观测到的东西"之间存在差距。
3. **我们如何解决？** —— 每个问题都有具体的修正方案，包括公式的修正、分类逻辑的改进、术语的替换、以及声称范围的降级。
4. **我们修改了 v1 的什么内容？** —— 本报告完整保留了所有增加和删除的内容，包括修改前后的文本对比。
5. **我们引用了什么新文献？** —— 本报告列出了所有新增的文献、保留的文献，以及它们在修订中扮演的角色。

## 1.2 Report v1 的背景

Report v1 是我于 2026 年 7 月提交的 Qualifying Report，题为：

> *Risk Behavior and Credit Signals in DeFi Lending Markets: Borrower Active Adjustment Under Position Risk Accumulation*

报告提出了一个研究问题：**在 DeFi 借贷市场中，当借款人的仓位风险上升时，借款人的主动调整行为是否提供了超越常规链上指标（如健康因子、抵押率）的增量风险信息？**

这个问题本身是合理的。但问题出在**如何把这个问题翻译成可操作的研究设计**——在翻译过程中，报告使用了不准确的公式、过于简单的分类规则、以及超出数据支持范围的声称。

## 1.3 为什么需要修订

修订的触发点是一次系统性的"构念效度审查"。简而言之：

> **构念效度（Construct Validity）**指的是：你声称在测量的东西，和你实际从数据中测量到的东西，是不是同一件事？

举个例子：
- 你说你测量的是"借款人的信用能力"（creditworthiness）
- 但你实际的数据只能看到"借款人在 Aave 协议上的仓位管理行为"
- 这两件事不是同一件事——借款人可能在其他协议、中心化交易所、甚至链下有完全不同的行为

Report v1 的问题正是这种"声称"和"数据"之间的差距。这种差距不是一个小错误，而是系统性的——它贯穿了从公式到术语到理论定位的各个层面。

## 1.4 修订方法

修订采用了一个称为"六层矩阵"的框架。这个框架的核心思想是：**每一个概念都必须经过六个层次的检验，从理论定义到最终可声称的范围，每一层都必须与下一层一致。**

```
第 1 层：Definition（定义）
   ↓  这个概念在经济理论上是什么意思？
第 2 层：Construct（研究构念）
   ↓  在本研究中，这个概念具体指什么？
第 3 层：Measurement（操作化度量）
   ↓  用什么公式/算法来计算它？
第 4 层：Observable（链上可观测事件）
   ↓  区块链上能实际看到什么？
第 5 层：Identification（识别策略）
   ↓  如何从可观测数据中识别出这个构念？
第 6 层：Allowed Claim（可声称的范围）
   →  基于以上五层，我们最多可以说什么？
```

**如果第 6 层的声称超出了第 4 层（可观测）能够支撑的范围，就是 over-claiming（过度声称）。**

Report v1 的 11 个问题，本质上都是某一层或某几层之间的断裂。

## 1.5 给非区块链金融读者的基础概念

在进入正式讨论之前，先用最简单的语言解释几个关键概念。如果你已经熟悉这些概念，可以跳过本节。

### 什么是 DeFi 借贷？

传统借贷（如银行贷款）是这样的：

```
传统借贷流程：
借款人 → 向银行申请贷款 → 银行查信用记录 → 银行决定借不借
→ 如果借，借款人承诺未来还款 + 利息
→ 如果不还，银行通过法律手段追索
```

DeFi 借贷完全不同。它没有银行，而是由智能合约（smart contract）——一段自动执行的代码——来管理一切：

```
DeFi 借贷流程：
借款人 → 向智能合约存入抵押品（如 ETH）
→ 智能合约自动计算可以借多少
→ 借款人提取借款
→ 如果抵押品价值下跌到危险水平，任何人都可以触发清算
→ 清算 = 强制卖出抵押品来偿还债务
```

**关键区别**：
- 传统借贷靠"信用"（你过去的还款记录、收入等）来决定能不能借
- DeFi 借贷靠"抵押"（你存入的资产价值）来决定能借多少
- 传统借贷违约 = 你不还钱，银行追索你
- DeFi 借贷"违约" = 你的抵押品价值不够了，合约自动清算你的仓位

### 什么是健康因子（Health Factor, HF）？

健康因子是 Aave 协议用来衡量你的仓位有多安全的指标。

```
用一个简单的比喻：

假设你用价值 150 万的房子做抵押，借了 100 万。

你的"贷款价值比" = 100 / 150 = 66.7%
银行设定的"清算阈值" = 80%（超过就要收回房子）

你的"健康因子" = 150 × 80% / 100 = 1.2

HF = 1.2 意味着：你的房子价值还可以跌一些才到危险线
HF = 1.0 意味着：正好在危险线上
HF < 1.0 意味着：要被收回了
```

在 Aave 中，HF 的计算公式是：

```
HF = Σ(每种抵押品的价值 × 该资产的清算阈值) / 总债务

如果 HF < 1.0 → 仓位可以被清算（任何人都可以来清算）
如果 HF ≥ 1.0 → 仓位安全
```

### 什么是清算（Liquidation）？

清算就是当你的 HF 跌到 1.0 以下时，你的抵押品被强制卖出来还债的过程。

```
清算流程：

你的仓位 HF = 0.95（低于 1.0）
    ↓
任何第三方（称为 liquidator，清算者）可以触发清算
    ↓
清算者帮你还一部分债务
    ↓
作为回报，清算者拿走你的一部分抵押品 + 额外的"清算罚金"（通常 5-10%）
    ↓
你的仓位 HF 恢复到 1.0 以上
    ↓
你损失了清算罚金，但剩下的仓位保住了
```

**注意**：清算不是借款人主动选择的，而是由第三方触发的。从借款人的角度看，清算是"被动"发生的事情。

### 什么是链上数据（On-chain Data）？

所有在区块链上发生的交易都会被永久记录下来，任何人都可以查看。这意味着：

- 谁存了什么资产、存了多少、什么时候存的 → **可观测**
- 谁借了什么、借了多少、什么时候还的 → **可观测**
- 谁被清算了、清算了多少 → **可观测**
- 借款人为什么借这笔钱、借钱后拿去干嘛了 → **不可观测**

这就是我们后面要讨论的"可观测性"问题的核心。

---

# 第二部分：问题总览

## 2.1 问题清单

经过六层矩阵的系统性审查，我们在 Report v1 中发现了 11 个问题。按严重程度分为三类：

### 🔴 技术性错误（Hard Error）—— 必须修正

这类问题是事实性或技术性错误，如果不修正，研究的整个基础都会出问题。

| 编号 | 问题 | 核心问题 |
|------|------|---------|
| 01 | HF 公式使用了 LTV 而非 Liquidation Threshold | 公式里用错了参数，导致所有基于 HF 的分析都会产生偏差 |
| 02 | 主动/被动分类仅用 `msg.sender == borrower` | 太简单了，忽略了多种常见操作方式，导致大量主动行为被误分类为被动 |
| 03 | Supply 等同于 Collateral（抵押） | 在 Aave 中存入资产不等于启用为抵押，两者是独立操作 |

### 🟡 过度声称（Over-claim）—— 需要降级

这类问题是报告声称的内容超出了数据实际能够支撑的范围。

| 编号 | 问题 | 核心问题 |
|------|------|---------|
| 04 | "完全可观测性"声称 | 只能观测协议事件，不能观测经济目的和链下行为 |
| 05 | RQ2 命名为 "Credit Layer" | 研究的是清算预测，不是信用评估 |
| 06 | Prospect Theory 被定位为"已确认的理论锚" | 无法区分行为效应和理性经济激励 |
| 07 | Liquidation 与 Default 混用 | 清算 ≠ 信用违约，两者是不同的概念 |
| 08 | Collateral 与 Credit 混用 | 抵押借贷 ≠ 信用借贷 |
| 11 | "Credit-relevant information" 反复使用 | 应改为"liquidation-relevant" |

### 🔵 术语不精确（Terminology）—— 需要明确

这类问题是术语使用不够精确，可能导致误解。

| 编号 | 问题 | 核心问题 |
|------|------|---------|
| 09 | Settlement 不分层使用 | 结算有三种含义，不标注层级会导致概念混淆 |
| 10 | 协议间术语直接混用 | Aave、Compound、MakerDAO 的指标定义不同，不能直接拼接 |

## 2.2 问题之间的关系

这 11 个问题不是孤立的。它们之间存在系统性关联：

```
根本问题：Collateral ≠ Credit（问题 08）
    ↓
    这个根本问题导致了连锁反应：
    ↓
    ├── 标题用 "Credit Signals"（问题 08, 11）
    ├── RQ2 命名为 "Credit Layer"（问题 05）
    ├── Literature Review 标题用 "Credit Risk Assessment"（问题 07, 11）
    ├── Liquidation 和 Default 混用（问题 07）
    └── "Credit-relevant information" 反复使用（问题 11）

另一个根本问题：技术细节不够精确（问题 01, 02, 03）
    ↓
    ├── HF 公式用错参数（问题 01）
    ├── 主动/被动分类太简单（问题 02）
    └── Supply ≠ Collateral-Enabled 没有区分（问题 03）

第三个问题：声称范围超出数据（问题 04, 06）
    ↓
    ├── "完全可观测"过强（问题 04）
    └── Prospect Theory 定位过强（问题 06）
```

## 2.3 修订后的整体变化概览

| 维度 | Report v1 | 修订后 |
|------|---------|--------|
| 核心声称 | "借款人行为提供信用信号" | "协议可观测的仓位管理行为提供清算倾向的增量信息" |
| 理论定位 | Prospect Theory 是已确认的理论锚 | Prospect Theory 是有吸引力的理论框架/竞争性解释 |
| 研究结果 | Liquidation / Default（混用） | Liquidation eligibility / Realized liquidation（区分） |
| 可观测性 | "完全可观测" | "协议事件可观测；经济目的不可观测" |
| 协议范围 | Aave + Compound + MakerDAO（直接拼接） | Aave V3 为主，Compound/Maker 为外部有效性检验 |
| Collateral | Supply = Collateral | Supply ≠ Collateral-Enabled Supply |
| 主动/被动 | msg.sender == borrower | msg.sender + onBehalfOf + 路由/自动化识别 |
| HF 公式 | 使用 LTV | 使用 LT（Liquidation Threshold） |

---

# 第三部分：逐问题详细说明

> 以下对每个问题进行详细说明。每个问题的说明结构为：
> 1. 问题是什么（用通俗语言解释）
> 2. Report v1 原文（保留原文）
> 3. 为什么这是一个问题（用案例解释）
> 4. 根源在哪里
> 5. 如何解决
> 6. 具体修改了什么（增加/删除的内容）
> 7. 支撑文献

---

## 3.1 问题 01：HF 公式使用 LTV 而非 Liquidation Threshold

### 🔴 严重程度：技术性错误（Hard Error）

**位置**：`sections/methodology.tex`，第 32 行

### 问题是什么？

简单来说：**报告写了一个公式来计算"健康因子"（Health Factor, HF），但公式里用了一个错误的参数。**

要理解这个问题，需要先知道 Aave 协议中有两个不同的参数：

```
参数一：LTV（Loan-to-Value，贷款价值比）
  → 决定"你能借多少"
  → 比如 ETH 的 LTV = 82.5%
  → 意思是：如果你存入价值 100 的 ETH，最多可以借 82.5

参数二：LT（Liquidation Threshold，清算阈值）
  → 决定"你什么时候会被清算"
  → 比如 ETH 的 LT = 83%
  → 意思是：当你的债务超过抵押品价值的 83% 时，仓位可以被清算
```

这两个参数数值很接近（82.5% vs 83%），但含义完全不同。Report v1 在 HF 公式中使用了 LTV，但正确的参数应该是 LT。

### Report v1 原文

> For each borrowing position, a trajectory of position health will be reconstructed at a daily frequency. The core risk metric is the **health factor** (HF), defined as:
>
> HF_t = Σ(C_{i,t} · P_{i,t} · **LTV**_i) / D_t
>
> where C_{i,t} is the quantity of collateral asset i at time t, P_{i,t} is its price, **LTV_i is the protocol-specific loan-to-value parameter** for that asset, and D_t is the total outstanding debt denominated in a common currency unit.

### 为什么这是一个问题？

用一个案例来说明：

```
案例：小明在 Aave 上存入 100 ETH 作为抵押，借出 USDC

假设：
  ETH 价格 = $2,000
  抵押品总价值 = 100 × $2,000 = $200,000
  借款金额 = $160,000

  ETH 的 LTV = 82.5%
  ETH 的 LT = 83%

用 LTV 计算（Report v1 的错误做法）：
  HF = $200,000 × 82.5% / $160,000 = $165,000 / $160,000 = 1.031

用 LT 计算（正确做法）：
  HF = $200,000 × 83% / $160,000 = $166,000 / $160,000 = 1.0375

差异看起来很小（1.031 vs 1.0375），但考虑以下情况：

如果 ETH 价格跌到 $1,930：
  抵押品价值 = 100 × $1,930 = $193,000

  用 LTV 计算：HF = $193,000 × 82.5% / $160,000 = 0.995 → HF < 1 → 可被清算！
  用 LT 计算：HF = $193,000 × 83% / $160,000 = 1.001 → HF > 1 → 安全！

结论：用 LTV 计算会显示"可以清算"，但用 LT 计算显示"还安全"。
      这意味着用错误的公式会导致：
      1. 错误地认为某些仓位可以被清算
      2. 所有基于 HF 的分析都会产生系统性偏差
      3. 所有"借款人在 HF 接近 1.0 时的行为"的分析都基于错误的风险指标
```

此外，Aave V3 还有一个复杂之处：**不同的模式下 LT 值不同**。

```
普通模式：     ETH 的 LT = 83%
EMode 模式：   ETH 的 LT = 93%（高相关资产对使用更高阈值）
Isolation 模式：ETH 的 LT = 75%（隔离资产使用更低阈值）
```

如果不考虑这些模式，重建的 HF 也会有偏差。

### 根源在哪里？

这个错误的根源在于对 Aave V3 协议机制的理解不够深入。LTV 和 LT 在很多非技术讨论中经常被混用（因为它们数值相近），但在实际计算中是两个完全不同的参数，服务于不同的功能。

### 如何解决？

1. **将公式中的 LTV 替换为 LT**（Liquidation Threshold）
2. **明确说明 LT 的来源**：从 Aave V3 合约参数和治理事件中获取
3. **说明 EMode 和 Isolation Mode 的影响**：不同模式下 LT 值不同
4. **说明 LT 可能随治理提案变化**：需要按时间追踪

### 具体修改了什么？

**删除的内容**：

```latex
% 原文（删除）
\text{HF}_t = \frac{\sum_{i} (C_{i,t} \cdot P_{i,t}) \cdot \text{LTV}_i}{D_t}

where ... \text{LTV}_i is the protocol-specific loan-to-value parameter 
for that asset...
```

**新增的内容**：

```latex
% 修正后（新增）
\text{HF}_t = \frac{\sum_{i} (C_{i,t} \cdot P_{i,t}) \cdot \text{LT}_i}{D_t}

where ... \text{LT}_i is the protocol-specific \emph{liquidation threshold} 
for that asset...

% 新增：LTV 和 LT 的区分说明
It is important to distinguish the liquidation threshold (LT) from the 
loan-to-value (LTV) parameter: LTV determines borrowing capacity 
(max_debt = collateral_value × LTV), whereas LT determines the 
liquidation boundary (HF < 1 ⟹ liquidation eligibility). The two 
parameters are set independently by protocol governance and may take 
different values for the same asset.

% 新增：EMode 和 Isolation Mode 的处理
Historical LT values are obtained from Aave V3 governance events and 
contract storage, as these parameters may change over time through 
governance proposals. In addition, positions in Efficiency Mode (EMode) 
or using isolated assets are subject to different LT values, and the 
reconstruction procedure accounts for these states.
```

### 支撑文献

| 文献 | 如何支撑这个修正 |
|------|-----------------|
| Aave V3 官方文档 (https://docs.aave.com/) | 定义了 HF 使用 LT 而非 LTV |
| Iftikhar et al. (2025) — *Automated Risk Management in DeFi* | 明确区分了 Aave 和 Compound 的风险参数，包括 LT 和 LTV 的区别 |
| Bartoletti & Lipparini (2025) — *A theory of Lending Protocols in DeFi* | 形式化了 DeFi 借贷协议中清算阈值和借款能力参数的区别 |

---

## 3.2 问题 02：主动/被动分类仅用 msg.sender == borrower

### 🔴 严重程度：技术性错误（Hard Error）

**位置**：`sections/methodology.tex`，第 23-25 行

### 问题是什么？

Report v1 需要区分借款人的"主动行为"（如主动还款、主动追加抵押）和"被动行为"（如被清算）。分类规则很简单：**看交易的发起者（msg.sender）是不是借款人本人**。

这个规则看起来合理，但实际上太简单了。在 DeFi 中，借款人有多种方式与协议交互，`msg.sender` 不一定是借款人本人的钱包地址。

### Report v1 原文

> An on-chain transaction will be classified as an **active borrower action** if and only if the transaction sender (`msg.sender`) matches the borrower wallet address. [...] A transaction will be classified as a **passive liquidation event** if the transaction sender is an address other than the borrower, regardless of whether that address can be identified as a known liquidation bot.

### 为什么这是一个问题？

用一个案例来说明：

```
案例：小红通过 Gnosis Safe（多签钱包）管理她的 Aave 仓位

小红的设置：
  - 她的钱包地址：0xAAA...
  - 她使用 Gnosis Safe 多签钱包来管理仓位：0xBBB...
  - Safe 钱包需要 2 个签名者批准才能执行交易

当小红想还款时：
  - msg.sender = 0xBBB...（Safe 钱包地址，不是小红的钱包地址）
  - onBehalfOf = 0xAAA...（小红的地址，实际债务承担者）

Report v1 的分类：
  msg.sender (0xBBB) ≠ borrower (0xAAA) → 分类为"被动行为"

实际情况：
  这是小红主动发起的还款操作！只是通过 Safe 钱包执行的。
  → 应该分类为"主动行为"
```

还有更多类似场景：

```
场景一览：

1. 直接操作
   msg.sender = 借款人地址 → ✅ Report v1 正确分类为"主动"

2. 通过 Safe 多签钱包操作
   msg.sender = Safe 合约地址 → ❌ Report v1 误分类为"被动"
   实际：借款人主动操作

3. 通过 DEX Router 操作（如 1inch, Paraswap）
   msg.sender = Router 合约地址 → ❌ Report v1 误分类为"被动"
   实际：借款人主动操作

4. 通过自动化服务操作（如 DefiSaver, Gelato）
   msg.sender = 自动化合约地址 → ❌ Report v1 误分类为"被动"
   实际：借款人授权的自动化操作

5. Credit Delegation（信用委托）
   msg.sender = 委托人地址 → ❌ Report v1 误分类为"被动"
   实际：可能是借款人授权的委托操作

6. 第三方清算
   msg.sender = 清算者地址 → ✅ Report v1 正确分类为"被动"
```

**关键问题**：Aave V3 的事件中有一个 `onBehalfOf` 参数，它记录了实际受影响的地址。Report v1 完全没有提到这个参数。

### 根源在哪里？

这个错误的根源在于对 DeFi 用户实际交互方式的理解不够全面。在早期 DeFi 中，大多数用户确实直接用自己的钱包与协议交互。但随着生态发展，多签钱包、路由合约、自动化服务变得越来越普遍。`msg.sender == borrower` 的简单规则无法覆盖这些场景。

### 如何解决？

使用多层分类规则：

```
分类流程（修正后）：

Layer 1: 检查 onBehalfOf 参数
    │
    ├── onBehalfOf == 借款人地址？
    │   ├── Yes → 进入 Layer 2
    │   └── No → 不是借款人的操作，排除
    │
Layer 2: 检查 msg.sender 类型
    │
    ├── msg.sender == 借款人地址？
    │   └── Yes → 分类为"主动"（直接操作）
    │
    ├── msg.sender 是已知的 Safe/Router/Automation 合约？
    │   └── Yes → 分类为"主动"（通过中介操作）
    │
    ├── msg.sender 是已知的清算者？
    │   └── Yes → 分类为"被动"（清算事件）
    │
    └── 都不是 → 分类为"未分类"（排除或单独分析）
```

### 具体修改了什么？

**删除的内容**：

```latex
% 原文（删除）
An on-chain transaction will be classified as an active borrower action 
if and only if the transaction sender (msg.sender) matches the borrower 
wallet address.
```

**新增的内容**：

```latex
% 修正后（新增）
The classification employs a multi-layer identification procedure that 
goes beyond a simple comparison of msg.sender with the borrower address. 
In Aave V3, several common interaction patterns necessitate this more 
nuanced approach:

1. Credit delegation (onBehalfOf). Aave V3 events include an onBehalfOf 
   parameter indicating the address whose position is affected, which may 
   differ from msg.sender. A transaction is classified as an active 
   borrower action only when onBehalfOf matches the borrower address.

2. Smart-contract wallets and routers. Borrowers frequently interact 
   with the protocol through Gnosis Safe multi-signature wallets, DEX 
   router contracts, or automation services. Transactions initiated 
   through these intermediaries are classified as active borrower actions 
   when the onBehalfOf field identifies the borrower. A curated registry 
   of known intermediary contract addresses is maintained.

3. Liquidation events. A transaction is classified as a passive 
   liquidation event when the caller is an address other than the 
   borrower (or an intermediary acting on the borrower's behalf) and 
   the event is a LiquidationCall.

The classification procedure produces three categories: active 
(borrower-initiated, including via intermediaries), passive (liquidation 
by third parties), and unclassified (transactions that cannot be 
confidently assigned to either category).
```

### 支撑文献

| 文献 | 如何支撑这个修正 |
|------|-----------------|
| Aave V3 官方文档 | 定义了 `onBehalfOf` 参数和 credit delegation 机制 |
| Iftikhar et al. (2025) | 比较了 Aave 和 Compound 的接口设计差异 |
| Ghosh et al. (2024) — *On-Chain Credit Risk Score* | 使用钱包级交易历史构建评分，需要处理类似的身份识别问题 |

---

## 3.3 问题 03：Supply ≠ Collateral-Enabled Supply

### 🔴 严重程度：技术性错误（Hard Error）

**位置**：`sections/methodology.tex`，第 9 行

### 问题是什么？

Report v1 将 Aave 中的 `Deposit`（存入）和 `Withdraw`（提取）事件直接等同于"提供抵押"和"移除抵押"。但在 Aave V3 中，**存入资产和启用为抵押是两个独立的操作**。

### Report v1 原文

> (i) `Deposit` and `Withdraw` events, representing the provision and removal of collateral

### 为什么这是一个问题？

用一个案例来说明：

```
案例：小刚在 Aave 上的操作

第一步：小刚存入 100 USDC
  → 事件：Supply(user=小刚, amount=100 USDC)
  → 此时 100 USDC 是否是抵押品？答案：不一定！

第二步（情况 A）：小刚启用了 USDC 作为抵押
  → 事件：SetUserUseReserveAsCollateral(user=小刚, asset=USDC, enabled=true)
  → 此时 100 USDC 才成为抵押品，计入 HF 计算

第二步（情况 B）：小刚没有启用 USDC 作为抵押
  → 没有第二个事件
  → 此时 100 USDC 只是存款，赚取利息，但不计入 HF 计算

Report v1 的处理：
  只看 Supply 事件 → 认为 100 USDC 是抵押品
  → 如果小刚没有启用为抵押（情况 B），HF 计算就错了
  → HF 会被高估（因为把不是抵押的资产算成了抵押）
```

这看起来像是一个细节问题，但它的影响是实质性的：

```
影响分析：

1. 如果直接用 Supply/Withdraw 事件来计算"抵押调整"：
   → 把不是抵押操作的 Supply/Withdraw 算成了抵押调整
   → 行为变量"Active Collateral Adjustment Rate"会包含噪音

2. 如果用 Supply 事件作为"借款人首次追加抵押"的时间点：
   → 但实际追加抵押的时间可能是更晚的 SetUserUseReserveAsCollateral 事件
   → "Response Latency"（响应延迟）变量会算错

3. HF 重建会出错：
   → 如果一个资产被 supply 但未启用为 collateral
   → 它不应该计入 HF 的分子
   → 但如果按 Report v1 的逻辑，会把它计入
   → 导致 HF 被高估，仓位看起来比实际更安全
```

### 根源在哪里？

这个错误的根源在于没有充分理解 Aave V3 的两步抵押机制。在 Compound V2 中，所有存入的资产自动作为抵押（虽然用户可以禁用），但在 Aave V3 中，Supply 和 Collateral-Enabled 是独立的状态。

### 如何解决？

```
修正后的抵押调整判定逻辑：

风险减轻的追加抵押（正确识别）=
  Supply 事件
  AND 该资产在事件后变为 collateral-enabled
  AND HF 分子增加

风险增加的抵押提取（正确识别）=
  Withdraw 事件
  AND 该资产在事件前是 collateral-enabled
  AND HF 分子减少

单纯的 Supply（未启用为 collateral）=
  不计入抵押调整
  → 只是存款行为，不是风险管理行为

单纯的 collateral enable/disable（无 supply/withdraw）=
  抵押状态变化
  → 需要单独追踪
```

### 具体修改了什么？

**删除的内容**：

```latex
% 原文（删除）
(i) Deposit and Withdraw events, representing the provision and removal 
of collateral
```

**新增的内容**：

```latex
% 修正后（新增）
(i) Supply and Withdraw events, representing the deposit and withdrawal 
of assets to and from the protocol;

(i_a) SetUserUseReserveAsCollateral events, representing the enabling or 
disabling of a supplied asset as collateral---a state that is independent 
of the supply action itself in Aave V3, where assets may be deposited 
without being counted toward the health factor calculation;

% 新增说明
It is important to distinguish between supplying an asset and enabling 
it as collateral: in Aave V3, a user may supply assets without enabling 
them as collateral, in which case they do not contribute to the health 
factor numerator. Accurate reconstruction of collateral adjustments 
therefore requires tracking both Supply/Withdraw events and 
SetUserUseReserveAsCollateral events, and maintaining a time-varying 
record of each asset's collateral-enabled status for each borrower 
position.
```

**行为变量也需修正**：

```latex
% 原文（删除）
Active Collateral Adjustment Rate. The net amount of collateral added 
or withdrawn by the borrower during the observation month...

% 修正后（新增）
Active Collateral Adjustment Rate. The net change in collateral-enabled 
asset value (additions via supply with collateral enablement, or 
removals via withdrawal of collateral-enabled assets) by the borrower 
during the observation month... This measure excludes supply and 
withdrawal activity involving assets that are not enabled as collateral.
```

### 支撑文献

| 文献 | 如何支撑这个修正 |
|------|-----------------|
| Aave V3 官方文档 | 明确说明了 Supply 和 Collateral-Enabled 的独立状态 |
| Bartoletti & Lipparini (2025) | 形式化了 DeFi 借贷协议中的 collateral 状态管理 |
| Iftikhar et al. (2025) | 比较了 Aave（手动 enable）和 Compound III（自动 collateral）的差异 |

---

## 3.4 问题 04："完全可观测性"声称过强

### 🟡 严重程度：过度声称（Over-claim）

**位置**：`sections/introduction.tex` 第 3 行，`sections/literature-review.tex` 第 21 行

### 问题是什么？

Report v1 多处声称 DeFi 提供了"完全透明性"（complete transparency）和"所有借款人行为的完全可观测性"（complete observability of all borrower actions）。这个声称太强了。

实际上，公开链上数据只能让我们看到**协议层面的事件**（如存入、借出、还款、清算），但看不到借款人的**经济目的**、**链下活动**、以及**跨协议/跨平台的行为**。

### Report v1 原文

> **introduction.tex:**
>
> The complete transparency of these protocols means that every deposit, withdrawal, borrowing event, repayment, collateral adjustment, and liquidation is immutably recorded on a public blockchain, creating an unprecedented empirical window into the behavior of financial market participants...

> **literature-review.tex:**
>
> Furthermore, the complete observability of all borrower actions in DeFi—including collateral additions, debt repayment, additional borrowing, and collateral withdrawals—means that behavioral responses to proximity to the liquidation threshold can be measured with a level of granularity that would be impossible in traditional credit markets.

### 为什么这是一个问题？

用一个案例来说明：

```
案例：小李的"看起来被动"行为

观察到的链上数据：
  - 小李的 Aave 仓位 HF 跌到 1.1
  - 小李没有在 Aave 上做任何操作
  - 2 天后，HF 跌到 0.95，仓位被清算

Report v1 的推断：
  - "小李在风险上升时没有做任何调整" → "小李是被动的借款人"

实际情况（无法从链上数据看到）：
  - 小李在 Binance（中心化交易所）上做了 ETH 期货空头来对冲
  - 小李在 Compound 上有另一个仓位，正在那里调整
  - 小李判断 ETH 价格会反弹，所以故意不操作
  - 小李的手机坏了，两天没看到仓位状态

结论：我们只能看到小李在 Aave 上"没做什么"，
      但不知道他"为什么没做"以及"在其他地方做了什么"。
```

再看另一个角度：

```
可观测 vs 不可观测

可观测（链上公开数据）：
  ✅ 协议事件：Supply, Borrow, Repay, Liquidation 等
  ✅ 事件参数：金额、资产类型、时间、onBehalfOf 等
  ✅ 合约参数：LT, LTV, 利率等
  ✅ 预言机价格
  ✅ 交易调用链（trace）

不可观测（需要额外数据或无法获取）：
  ❌ 借款人的经济目的/意图
  ❌ 链下活动（CEX 对冲、OTC 交易、场外协议）
  ❌ 跨协议活动（除非全面追踪所有协议）
  ❌ 借款人的真实身份
  ❌ 借款人的风险偏好
  ❌ 借款人的整体财务状况
```

有趣的是，Report v1 在 Discussion 部分其实已经承认了这个限制：

> **discussion.tex:**
> The analysis is limited to on-chain transactions, which means that it cannot observe borrower behavior on centralized exchanges or off-chain activities.

但问题是：Introduction 和 Literature Review 中说"完全可观测"，Discussion 中又说"不能完全观测"，这是自相矛盾的。reviewer 会注意到这种不一致。

### 根源在哪里？

根源在于将"协议事件可观测"等同于"借款人行为完全可观测"。前者是正确的——所有协议事件确实都被记录在链上。但后者是过度推断——协议事件只是借款人整体经济行为的一个子集。

### 如何解决？

将"complete observability of all borrower actions"降级为"complete observability of protocol-level events"，并明确说明哪些是不可观测的。

### 具体修改了什么？

**删除的内容**：

```latex
% introduction.tex（删除）
The complete transparency of these protocols means that every deposit, 
withdrawal, borrowing event, repayment, collateral adjustment, and 
liquidation is immutably recorded on a public blockchain, creating an 
unprecedented empirical window into the behavior of financial market 
participants...

% literature-review.tex（删除）
the complete observability of all borrower actions in DeFi
```

**新增的内容**：

```latex
% introduction.tex（新增）
The public and verifiable nature of these protocols means that every 
protocol-level event---deposit, withdrawal, borrowing, repayment, 
collateral adjustment, and liquidation---is immutably recorded on a 
public blockchain, creating an unprecedented empirical window into 
the position management behavior of protocol participants operating 
under varying degrees of risk exposure. Importantly, however, this 
transparency is limited to protocol-observable events: the economic 
purposes underlying these actions, as well as participants' off-chain 
and cross-platform activities, remain unobservable.

% literature-review.tex（新增）
the complete observability of protocol-level events in DeFi... It 
should be noted, however, that this observability extends only to 
protocol events; the economic motives underlying these actions and 
borrowers' activities outside the observed protocol are not directly 
observable from public blockchain data.
```

### 支撑文献

| 文献 | 如何支撑这个修正 |
|------|-----------------|
| Ghosh et al. (2024) | 使用链上数据但明确承认只能观测 wallet-level 行为 |
| Cornelli et al. (2025) — *Why DeFi Lending?* | 在 Aave V2 数据中分析借贷行为，但限制在 protocol-observable 范围 |
| Budish & Sunderam (2026) | 分析 blockchain trust model 的限制 |

---

## 3.5 问题 05：RQ2 命名为 "Credit Layer"

### 🟡 严重程度：过度声称（Over-claim）

**位置**：`sections/research-topic.tex` 第 18 行，`sections/abstract.tex`，`sections/introduction.tex` 第 9 行

### 问题是什么？

Report v1 将第二个研究问题（RQ2）命名为"Credit Layer"（信用层），并在全文中使用"credit prediction"（信用预测）、"credit-relevant information"（信用相关信息）等术语。

但 RQ2 的实际研究内容是：**行为过程变量是否能预测未来的清算事件？** 清算（liquidation）不是信用违约（credit default），两者是不同的概念。

### Report v1 原文

> **RQ2 (Credit Layer).** Controlling for conventional on-chain risk indicators... do behavioral process variables... provide statistically and economically significant incremental predictive power for future **liquidation events**?

> **introduction.tex:**
> The second, **credit-oriented** layer asks whether these behavioral patterns... carry incremental predictive power for future **liquidation events**...

注意这里有一个内在矛盾：RQ2 叫"Credit Layer"，但实际问的是"liquidation events"。如果真的是 credit layer，应该问的是 default，不是 liquidation。

### 为什么这是一个问题？

```
清算 vs 信用违约的核心区别：

清算（Liquidation）：
  - 层级：仓位级别（position-level）
  - 触发：HF < 1（机械触发，由智能合约自动执行）
  - 原因：价格暴跌、杠杆过高、操作延迟
  - 后果：仓位被强制平仓，损失清算罚金
  - 可观测性：高（链上事件）
  - 可逆性：不可逆

信用违约（Credit Default）：
  - 层级：借款人级别（borrower-level）
  - 触发：偿付能力失败或偿付意愿下降
  - 原因：收入下降、财务困境、故意违约
  - 后果：信用记录受损，法律追索
  - 可观测性：低（需要链下信息）
  - 可逆性：可能重组、延期
```

用"Credit Layer"来命名一个研究清算预测的问题，就好像：

```
比喻：
  你研究的是"开车时安全带在碰撞中如何保护乘客"
  但你把它命名为"航空安全层"（Aviation Safety Layer）
  
  虽然安全带和航空安全都涉及"保护人"，但它们是完全不同的东西。
  用"航空安全"来命名会让读者以为你在研究飞机安全。
```

### 根源在哪里？

根源在于"credit"一词在金融学中含义很广，从"信用评估"到"信贷市场"到"信用风险"都可以用。但在本研究中，数据来自抵押借贷市场，outcome 是清算，不是信用违约。使用"credit"来描述这个研究会误导读者，让他们以为本研究在做信用评分。

### 如何解决？

1. 将 RQ2 从"Credit Layer"改名为"Liquidation Propensity Layer"（清算倾向层）
2. 将"credit-oriented"改为"predictive"（预测性的）
3. 在全文中明确声明清算 ≠ 信用违约

### 具体修改了什么？

**删除的内容**：

```latex
% 原文（删除）
\item[RQ2 (Credit Layer).] Controlling for conventional on-chain risk 
indicators...

The second, credit-oriented layer asks whether these behavioral 
patterns...
```

**新增的内容**：

```latex
% 修正后（新增）
\item[RQ2 (Liquidation Propensity Layer).] Controlling for conventional 
on-chain risk indicators... do behavioral process variables... provide 
statistically and economically significant incremental predictive power 
for future liquidation events?

The second, predictive layer asks whether these behavioral patterns... 
We emphasize that the outcome of interest is liquidation---a 
protocol-level, mechanically triggered event---not credit default, 
which is a borrower-level outcome requiring different data and 
identification strategies.
```

### 支撑文献

| 文献 | 如何支撑这个修正 |
|------|-----------------|
| Sadeghi & Feinstein (2026) | 专门研究 DeFi liquidation dynamics，明确将 liquidation 定位为机械过程 |
| Ghosh et al. (2024) | 直接做 on-chain credit scoring——Paper 1 与之的区别在于 outcome 不同 |
| Di Maggio & Yao (2020) | 研究 fintech 借贷中的 default——default 和 liquidation 是不同的构念 |

---

## 3.6 问题 06：Prospect Theory 定位过强

### 🟡 严重程度：过度声称（Over-claim）

**位置**：`sections/literature-review.tex` 第 21-23 行，`sections/research-topic.tex` 第 47 行，`sections/discussion.tex` 第 9 行

### 问题是什么？

Report v1 将 Prospect Theory（前景理论，PT）定位为本研究的"已确认的理论锚"（confirmed theory anchor），声称 DeFi 的清算阈值是一个"客观的、外生决定的参考点"，可以用来测试 PT 的预测。

但问题是：**HF=1.0 既是心理参考点，也是协议机制的不连续点。** 借款人在 HF=1.0 附近的行为变化既可能由心理偏差（loss aversion，损失厌恶）解释，也可能由清算罚金的经济激励（理性解释）解释。两种解释在缺乏特殊识别策略时无法分离。

### Report v1 原文

> **literature-review.tex:**
> DeFi lending provides an almost ideal empirical laboratory for testing behavioral theories. The liquidation threshold... serves as an objective, exogenously determined reference point that is identical across all participants.

> **research-topic.tex:**
> it bridges the largely separate literatures on DeFi risk modeling and behavioral finance by **testing prospect theory predictions** in a naturalistic financial setting where the reference point—the liquidation threshold—is objective, observable, and identical for all participants

> **discussion.tex:**
> it would provide the first systematic evidence that **prospect theory's predictions**—particularly those concerning loss aversion and reference-point effects—are observable in DeFi lending behavior

> **research-topic.tex (H1b):**
> The magnitude of borrower-initiated risk-reducing actions... is larger in absolute value than... consistent with the **loss aversion prediction of prospect theory**.

### 为什么这是一个问题？

用案例来说明：

```
案例：小王在 HF=1.0 附近的行为变化

观察到的现象：
  当 HF 从 1.5 降到 1.2 时，小王只做了少量调整
  当 HF 从 1.1 降到 0.95 时，小王大量追加抵押

PT 解释（行为解释）：
  HF=1.0 是小王的心理参考点
  当 HF 跌破 1.0 时，小王进入"损失域"
  根据 loss aversion，他在"损失域"的反应比"收益域"更激烈
  → 这是心理偏差导致的

理性解释（经济激励解释）：
  HF=1.0 是清算触发点
  如果 HF < 1.0，小王的仓位会被清算，损失 5-10% 的清算罚金
  为了避免这个真实的经济损失，小王在接近 1.0 时加强风险管理
  → 这是理性计算导致的

关键问题：两种解释预测了完全相同的行为模式！
         没有特殊的识别策略，我们无法知道是哪种解释在起作用。
```

用一个比喻：

```
比喻：你看到一个人在下雨时跑步加速

解释 A（心理解释）：
  下雨是这个人"不舒服"的触发点，他因为不想淋湿而加速跑
  → 这是情绪驱动的

解释 B（理性解释）：
  下雨意味着衣服会湿，换衣服的成本很高
  他是理性计算后决定加速跑以减少淋雨时间
  → 这是理性计算的

你能从"他加速跑了"这个事实中区分出是 A 还是 B 吗？
不能。因为两种解释都预测"他会加速跑"。

同样的道理：
  PT 预测"借款人在 HF 接近 1.0 时加强风险管理"
  理性模型也预测"借款人在 HF 接近 1.0 时加强风险管理"
  你无法从行为数据中区分两种解释。
```

### Report v1 的内在矛盾

有趣的是，Report v1 在 Literature Review 第 23 行其实已经承认了这个问题：

> Disentangling rational risk management from behavioral deviations therefore requires careful empirical design, including the use of control groups, instrumental variables, or regression discontinuity approaches...

但 Research Topic 和 Discussion 部分却仍然声称在"test prospect theory predictions"和"provide evidence for prospect theory"。这是自相矛盾的——如果已经承认需要特殊识别策略来分离两种解释，就不能声称在"测试"PT。

### 根源在哪里？

根源在于对理论定位的把握。PT 确实是一个有吸引力的理论框架——它提供了关于参考点行为和损失厌恶的清晰预测，而 DeFi 的清算阈值确实是一个天然的参考点。但"有吸引力"不等于"可以确认"。在缺乏分离两种解释的识别策略时，PT 最多只能作为"有吸引力的理论框架"或"竞争性解释"，不能作为"已确认的理论锚"。

### 如何解决？

将 PT 的定位从"confirmed theory anchor"降级为"compelling framing / competing explanation"（有吸引力的理论框架 / 竞争性解释）。

### 具体修改了什么？

**删除的内容**：

```latex
% literature-review.tex（删除）
DeFi lending provides an almost ideal empirical laboratory for testing 
behavioral theories. The liquidation threshold... serves as an objective, 
exogenously determined reference point...

% research-topic.tex（删除）
testing prospect theory predictions in a naturalistic financial setting

% discussion.tex（删除）
it would provide the first systematic evidence that prospect theory's 
predictions... are observable in DeFi lending behavior

% research-topic.tex H1b（删除）
consistent with the loss aversion prediction of prospect theory
```

**新增的内容**：

```latex
% literature-review.tex（新增）
However, a fundamental identification challenge arises: the liquidation 
threshold is simultaneously a psychological reference point AND a 
mechanical protocol discontinuity. The liquidation penalty (typically 
5-10% of the liquidated collateral) creates a rational economic incentive 
for borrowers to manage their positions more intensively as they approach 
the threshold. Consequently, behavioral discontinuities observed near the 
threshold are consistent with BOTH prospect theory's loss aversion 
prediction AND rational risk management. Separating these two 
explanations requires identification strategies that exploit variation in 
the economic cost of liquidation or in the salience of the threshold, 
which are beyond the scope of the present study. We therefore frame 
prospect theory as a compelling competing explanation rather than a 
confirmed theoretical anchor, and interpret any behavioral patterns 
consistent with PT predictions as suggestive rather than definitive 
evidence.

% H1b（修正后）
H1b (Asymmetry Near the Liquidation Threshold):
The magnitude of borrower-initiated risk-reducing actions per unit 
deterioration in health factor is larger in absolute value than the 
magnitude of risk-increasing actions per unit improvement in health 
factor. This asymmetry is consistent with both prospect theory's loss 
aversion prediction and the rational incentive to avoid the liquidation 
penalty; the two explanations cannot be fully separated without 
additional identification strategies.
```

### 支撑文献

| 文献 | 如何支撑这个修正 |
|------|-----------------|
| Kahneman & Tversky (1979) | PT 原始定义——reference point, loss aversion |
| Barberis (2013) | PT 在金融中的应用综述——承认 reference point 的识别挑战 |
| Sadeghi & Feinstein (2026) | DeFi 清算中的经济激励分析——理性解释的文献支撑 |

---

## 3.7 问题 07：Liquidation 与 Default 混用

### 🟡 严重程度：过度声称（Over-claim）

**位置**：`sections/abstract.tex`，`sections/literature-review.tex` 第 27-31 行，`sections/research-topic.tex`，`sections/discussion.tex`

### 问题是什么？

Report 1 在多处将 liquidation（清算）和 default（信用违约）混用，或将清算预测等同于信用风险评估。这个问题与问题 05 和 08 密切相关——它们都是"Credit"概念过度使用的不同表现。

### Report v1 原文

> **literature-review.tex:**
> ...the use of on-chain data for credit risk assessment and **default prediction**.
>
> ...predict the likelihood of **default**.
>
> ...predict whether the borrower will **default** at time t+k.

> **literature-review.tex 标题:**
> On-Chain **Credit Risk** Assessment

### 为什么这是一个问题？

```
用一张图来展示 Liquidation 和 Default 的关系：

                    ┌──────────────────────────────────────────┐
                    │           借款人的整体经济状态              │
                    │                                          │
                    │   ┌────────────────────────┐             │
                    │   │    DeFi 仓位           │             │
                    │   │                        │             │
                    │   │  HF < 1.0              │             │
                    │   │  → 被清算 (Liquidation)│             │
                    │   │  → 仓位被强制平仓       │             │
                    │   │  → 损失清算罚金         │             │
                    │   └────────────────────────┘             │
                    │                                          │
                    │   ┌────────────────────────┐             │
                    │   │    链下/其他协议活动    │             │
                    │   │                        │             │
                    │   │  收入下降               │             │
                    │   │  → Default (信用违约)   │             │
                    │   │  → 信用记录受损          │             │
                    │   │  → 法律追索             │             │
                    │   └────────────────────────┘             │
                    │                                          │
                    │  注意：被清算 ≠ 信用违约                  │
                    │  - 被清算可能是价格暴跌导致的，不代表偿付能力失败 │
                    │  - 信用违约是借款人级别的，不是仓位级别的     │
                    │  - 两者可能同时发生，也可能独立发生          │
                    └──────────────────────────────────────────┘
```

实际案例：

```
案例 1：被清算但不是违约
  小赵在 Aave 上用 ETH 抵押借了 USDC
  ETH 价格暴跌 30%
  小赵的仓位被清算
  但小赵在传统银行有稳定工作，收入充足
  → 这是清算，不是违约（小赵的偿付能力没有问题）

案例 2：违约但没被清算
  小钱的 Aave 仓位 HF 一直是 1.5（安全）
  但小钱在传统银行有一笔贷款
  小钱失业了，无法还银行的贷款
  → 这是违约，不是清算（Aave 仓位没有被清算）
```

### 根源在哪里？

根源在于 DeFi 文献中"default"一词的使用不够严谨。一些文献（如 Ghosh et al. 2024）在 DeFi 语境中使用"default"来描述清算事件，但实际上 DeFi 中可观测的不良事件是 liquidation 而非传统意义上的 default。Report v1 直接借用了这些文献的术语，没有进行概念上的澄清。

### 如何解决？

1. 在全文中统一使用"liquidation"来描述 DeFi 中的不良事件
2. 在引用使用"default"的文献时，明确说明这些文献中的"default"在 DeFi 语境中实际指 liquidation
3. 新增术语声明，明确区分 liquidation 和 default
4. 将 Literature Review 标题从"On-Chain Credit Risk Assessment"改为"On-Chain Risk Assessment and Predictive Modeling"

### 具体修改了什么？

**删除的内容**：

```latex
% literature-review.tex 标题（删除）
\subsection{On-Chain Credit Risk Assessment}

% literature-review.tex 正文（删除）
...the use of on-chain data for credit risk assessment and default 
prediction.
...predict the likelihood of default.
...predict whether the borrower will default at time t+k.
```

**新增的内容**：

```latex
% literature-review.tex 标题（新增）
\subsection{On-Chain Risk Assessment and Predictive Modeling}

% literature-review.tex 正文（新增）
...the use of on-chain data for risk assessment and predictive 
modeling of adverse position outcomes.

It should be noted that in the DeFi context, the observable adverse 
outcome is liquidation---a protocol-level, mechanically triggered 
event---rather than credit default in the traditional sense, which is 
a borrower-level outcome involving inability or unwillingness to repay. 
The distinction between liquidation and default is important: 
liquidation may be triggered by price volatility, excessive leverage, 
or operational delays rather than by a borrower's fundamental inability 
to repay, and the two concepts should not be conflated.

% 新增术语声明（放在 Research Topic 开头）
Terminological note. Throughout this report, we use "liquidation" to 
refer to the protocol-level event in which a position with a health 
factor below 1.0 is partially or fully closed by a third-party 
liquidator. We do not use "default" as a synonym for liquidation, as 
the two concepts differ in level (position vs. borrower), trigger 
(mechanical threshold vs. creditworthiness failure), and observability 
(on-chain event vs. off-chain outcome).
```

### 支撑文献

| 文献 | 如何支撑这个修正 |
|------|-----------------|
| Sadeghi & Feinstein (2026) | 明确将 DeFi liquidation 定位为 mechanical process |
| Perez et al. (2021) — *Liquidations: DeFi on a Knife-Edge* | 使用"liquidation"而非"default" |
| Ghosh et al. (2024) | 使用"default"描述 DeFi outcome——需要审查其是否实际指 liquidation |

---

## 3.8 问题 08：Collateral 与 Credit 概念混用

### 🟡 严重程度：过度声称（Over-claim）

**位置**：报告标题，`sections/introduction.tex`，`sections/research-topic.tex`，`sections/discussion.tex`

### 问题是什么？

Report v1 将整个研究框架为"credit"相关研究——标题中有"Credit Signals"，全文使用"credit risk"、"credit-relevant information"、"credit assessment"等术语。但 DeFi 借贷是**抵押担保借贷**（collateral-secured lending），不是**传统信用借贷**（traditional credit-based lending）。Collateral ≠ Credit。

### Report v1 原文

> **标题：**
> Risk Behavior and **Credit Signals** in DeFi Lending Markets: Borrower Active Adjustment Under Position Risk Accumulation

> **abstract.tex:**
> ...credit risk...

> **research-topic.tex:**
> ...a process-based perspective on **credit risk assessment**...

> **discussion.tex:**
> ...whether borrower behavior contains **credit-relevant information**...

### 为什么这是一个问题？

要理解这个问题，需要先理解传统信用借贷和 DeFi 抵押借贷的根本区别：

```
传统信用借贷：
  ┌────────────┐     信任基于     ┌──────────────────┐
  │  银行       │ ←───────────── │  借款人的信用历史  │
  │  (贷方)     │                │  - 还款记录        │
  │             │ → 贷款 ──────→ │  - 收入证明        │
  │             │                │  - 资产负债        │
  │             │ ← 还款 ←────── │  - 信用评分        │
  └────────────┘                └──────────────────┘
  
  核心问题：借款人是否会还钱？→ 信用风险
  
  如果不还：
  → 信用记录受损
  → 法律追索
  → 但银行可能损失本金

DeFi 抵押借贷：
  ┌────────────┐     信任基于     ┌──────────────────┐
  │  智能合约   │ ←───────────── │  借款人的抵押品    │
  │  (协议)     │                │  - 超额抵押        │
  │             │ → 借款 ──────→ │  - 实时盯市        │
  │             │                │  - 自动清算        │
  │             │ ← 还款 ←────── │                   │
  └────────────┘                └──────────────────┘
  
  核心问题：抵押品价值是否足够？→ 仓位风险（position risk）
  
  如果不够：
  → 自动清算
  → 损失清算罚金
  → 协议不会损失本金（因为有超额抵押）
```

关键区别：

| 维度 | 传统信用借贷 | DeFi 抵押借贷 |
|------|-----------|-------------|
| 信任基础 | 身份 + 信用历史 + 收入 | 资产（超额抵押） |
| 核心风险 | 信用风险（借款人不还钱） | 仓位风险（抵押品价值不够） |
| 信息需求 | 借款人身份、收入、信用记录 | 抵押品价值、仓位健康度 |
| 信息不对称 | 高（需要 screening/signaling） | 低（超额抵押消除大部分） |
| 违约处理 | 法律追索、信用记录 | 自动清算（机械性） |

**为什么不能说 DeFi 借贷是"credit"？** 因为在传统金融中，"credit"意味着基于借款人信用能力的借贷——银行评估借款人的还款能力和意愿，决定是否借钱。而 DeFi 借贷完全不看借款人是谁，只看抵押品价值够不够。这是两种根本不同的信任机制。

**比喻**：

```
传统信用借贷 = 朋友借你 1000 块，因为你之前都按时还了（信用）
DeFi 抵押借贷 = 你把手表（价值 1500）抵押给当铺，借 1000 块（抵押）

你不能说当铺在做"信用借贷"——当铺不在乎你的信用，只在乎手表值多少钱。
```

### 根源在哪里？

根源在于"credit"在金融学中含义很广。DeFi 借贷确实是一种"借贷"（lending/borrowing），但不是"信用借贷"（credit-based lending）。Report v1 使用"credit"来描述整个研究，让读者以为本研究在研究信用问题，但实际上研究的是仓位风险问题。

更深层的根源是：研究者可能希望将研究发现与更大的"信用评估"领域连接起来（这确实是 Paper 3 的方向），但在 Paper 1 阶段就使用"credit"术语，会让声称超出当前数据能支持的范围。

### 如何解决？

1. 修改标题，删除"Credit Signals"
2. 全文将"credit risk"（描述 DeFi 时）替换为"liquidation risk"或"position risk"
3. 将"credit-relevant information"替换为"risk-relevant information"或"liquidation-relevant information"
4. 保留"credit"在以下场景中的使用：描述传统金融作为对比、引用现有文献标题、描述未来研究方向

### 具体修改了什么？

**删除的内容**：

```latex
% 标题（删除）
Risk Behavior and Credit Signals in DeFi Lending Markets: Borrower 
Active Adjustment Under Position Risk Accumulation

% abstract.tex（删除）
...credit risk...

% research-topic.tex（删除）
...a process-based perspective on credit risk assessment...

% discussion.tex（删除）
...whether borrower behavior contains credit-relevant information...
```

**新增的内容**：

```latex
% 标题（新增）
Position Management Behavior and Liquidation Risk in DeFi Lending 
Markets: Borrower Active Adjustment Under Position Risk Accumulation

% 新增全局声明（放在 Introduction 第一段末尾）
It is important to distinguish DeFi lending from traditional 
credit-based lending. DeFi lending protocols are collateral-secured 
lending markets: borrowers provide over-collateralization, and the 
protocol's risk management is based on position health rather than 
borrower creditworthiness. While behavioral patterns observed in DeFi 
may eventually inform credit assessment frameworks---a direction 
explored in future research---the present study does not claim to 
assess creditworthiness or improve credit scoring. The outcome of 
interest is liquidation, a position-level event, not credit default, 
a borrower-level outcome.
```

### 支撑文献

| 文献 | 如何支撑这个修正 |
|------|-----------------|
| Ioannidou et al. (2022) — *Collateral and Asymmetric Information* | Collateral 不只是 loss protection，也有 screening/signaling 功能——但这是在传统信用市场中 |
| Asriyan et al. (2021) — *Collateral Booms and Information Depletion* | Collateral boom 导致信息生产减少——与"行为信息能否替代抵押"相关 |
| Berg et al. (2020) — *Credit Scoring Using Digital Footprints* | Digital footprint 提供 incremental information（补充而非替代）——Paper 1 的定位参考 |
| Cong & He (2019) — *Blockchain Disruption and Smart Contracts* | 定义 blockchain 对 contracting 的经济意义——定义 DeFi 与传统金融的区别 |

---

## 3.9 问题 09：Settlement 层级混淆

### 🔵 严重程度：术语不精确（Terminology）

**位置**：`sections/methodology.tex` 第 9 行

### 问题是什么？

Report v1 在描述 Borrow/Repay 事件时使用了"settlement"（结算）一词：`"the creation and settlement of loan positions"`。但"settlement"在区块链和金融语境中有多种含义，不加区分地使用会导致概念混淆。

### Report v1 原文

> (ii) `Borrow` and `Repay` events, representing the creation and **settlement** of loan positions

### 为什么这是一个问题？

"Settlement"（结算）在区块链金融中至少有三层含义：

```
Settlement 的三层含义：

第 1 层：Technical / Ledger Settlement（技术/账本结算）
  含义：交易上链、执行、状态更新、共识最终确认
  例子：一笔 Repay 交易被打包进区块，EVM 执行后债务状态更新
  可观测性：✅ 高（链上数据可完全观测）
  
  ↓
  
第 2 层：Protocol-level Settlement（协议层面结算）
  含义：协议内义务了结（如 Repay 完成债务了结）
  例子：借款人偿还了全部债务，Aave 协议标记该仓位为已清算
  可观测性：✅ 高（协议事件可观测）
  
  ↓
  
第 3 层：Economic / Business Settlement（经济/商业结算）
  含义：这笔钱在商业上代表什么（货款、工资、OTC 交易等）
  例子：借款人借钱是为了支付供应商货款，还款意味着货款结清
  可观测性：❌ 低（需要链下信息）
```

Report v1 使用"settlement of loan positions"来描述 Repay 事件，实际指的是第 2 层（Protocol-level Settlement），但没有标注层级。如果 reviewer 理解为第 3 层（Economic Settlement），会质疑"如何从链上数据确定经济结算？"

### 根源在哪里？

根源在于"settlement"一词在金融和区块链领域被广泛使用，但不同语境下含义不同。在传统金融中，"settlement"通常指交易的资金交割和最终确认。在区块链中，"settlement"可以指共识最终性、状态更新、或经济义务了结。Report v1 没有明确使用的是哪一层含义。

### 如何解决？

最简单的解决方案：用"repayment"（还款）替代"settlement"（结算）。"repayment"精确描述了 Repay 事件的功能，且没有"settlement"的多层歧义。

### 具体修改了什么？

**删除的内容**：

```latex
% 原文（删除）
(ii) Borrow and Repay events, representing the creation and settlement 
of loan positions
```

**新增的内容**：

```latex
% 修正后（新增）
(ii) Borrow and Repay events, representing the creation and repayment 
of loan positions
```

（简单替换"settlement"为"repayment"，消除歧义）

### 支撑文献

| 文献 | 如何支撑这个修正 |
|------|-----------------|
| Hautsch et al. (2024) — *Building trust takes time* | 区分了技术结算和经济结算——blockchain settlement latency 的研究 |
| Budish & Sunderam (2026) | 分析 blockchain trust model 在传统金融中的 settlement 含义 |
| Ethereum PoS 官方文档 | 定义了 consensus finality——Technical Settlement 的基础 |

---

## 3.10 问题 10：协议间术语直接混用

### 🔵 严重程度：术语不精确（Terminology）

**位置**：`sections/methodology.tex` 第 7-11 行

### 问题是什么？

Report v1 提议同时使用 Aave、Compound 和 MakerDAO 的数据，并将它们放在一起分析（"cross-protocol validation"）。但三个协议的风险指标定义、事件名称、清算机制都不同，不能直接拼接为一个数据集（panel）。

### Report v1 原文

> The primary data source will be the historical event logs and state data from three major DeFi lending protocols: Aave (V2 and V3), Compound (V2 and V3), and MakerDAO. These three protocols collectively account for the majority of DeFi lending activity on Ethereum and offer complementary data for cross-protocol validation.

### 为什么这是一个问题？

用一个案例来说明三个协议的关键差异：

```
案例：同一个概念，三个协议完全不同

"清算"在三个协议中：

Aave V3：
  触发：HF < 1.0
  执行方式：清算者帮你还债，拿走你的抵押品 + 罚金
  事件名：LiquidationCall
  速度：即时（一个交易内完成）

Compound III：
  触发：Account Shortfall > 0
  执行方式：协议"吸收"你的抵押品，之后通过市场处理
  事件名：AbsorbCollateral
  速度：吸收即时，但后续处理可能延迟

MakerDAO：
  触发：Collateralization Ratio < Liquidation Ratio
  执行方式：拍卖你的抵押品（Dutch auction 或 English auction）
  事件名：Liquidation auction
  速度：拍卖过程需要时间（不是即时的）
```

再看事件名称的问题：

```
"Supply" 在三个协议中的含义：

Aave V3：
  Supply = 存入资产（可能是抵押，也可能不是——见问题 03）

Compound III：
  Supply base asset = 归还借款（= Aave 的 Repay！）
  ⚠️ 同一个词，完全相反的含义！

MakerDAO：
  lock = 存入抵押品（= Aave 的 Supply + collateral-enabled）
  没有 "Supply" 这个事件名
```

**如果直接把三个协议的数据拼接为一个数据集**：

```
灾难性后果：
  
  数据集：
  ┌──────────┬──────────────┬────────────┐
  │ 协议      │ 事件名        │ 含义       │
  ├──────────┼──────────────┼────────────┤
  │ Aave     │ Supply       │ 存入资产   │
  │ Compound │ Supply       │ 还款！     │  ← 完全相反
  │ Aave     │ Borrow       │ 借款       │
  │ Compound │ Withdraw     │ 借款！     │  ← 不同的事件名
  │ Maker    │ draw         │ 借款！     │  ← 又一个不同的名字
  └──────────┴──────────────┴────────────┘

  如果不区分协议，直接按事件名拼接：
  → Compound 的"还款"被算成了 Aave 的"存入"
  → 三个协议的"借款"有三个不同的事件名
  → HF、Shortfall、Collateralization Ratio 定义不同，不能直接比较
  → 清算机制不同，"清算时间"和"清算金额"的度量也不同
```

### 根源在哪里？

根源在于将不同协议的表面相似性等同于底层机制的相似性。三个协议都是"DeFi 借贷协议"，但它们的风险指标定义、事件语义、清算机制都有显著差异。直接拼接数据会引入严重的度量误差。

### 如何解决？

**推荐方案**：以 Aave V3 为主协议，Compound 和 MakerDAO 为外部有效性检验（分别分析，不拼接）。

```
修正后的研究设计：

主分析：
  Aave V3 (Ethereum mainnet)
    → 所有变量定义一致
    → HF 重建使用 Aave V3 的 LT 参数
    → 事件类型使用 Aave V3 的事件结构
    → 样本量最大，内部有效性最高

外部有效性检验：
  Compound III
    → 单独分析（使用 Compound 的 Account Shortfall 指标）
    → 检验核心发现是否在不同清算机制下成立
    
  MakerDAO
    → 单独分析（使用 Maker 的 Collateralization Ratio）
    → 检验核心发现是否在拍卖式清算机制下成立

  不做跨协议的数据拼接
  跨协议比较 = 分别分析后比较结论方向
```

### 具体修改了什么？

**删除的内容**：

```latex
% 原文（删除）
The primary data source will be the historical event logs and state 
data from three major DeFi lending protocols: Aave (V2 and V3), 
Compound (V2 and V3), and MakerDAO. These three protocols collectively 
account for the majority of DeFi lending activity on Ethereum and offer 
complementary data for cross-protocol validation.
```

**新增的内容**：

```latex
% 修正后（新增）
The primary data source is Aave V3 on Ethereum mainnet, selected for 
three reasons: (i) it is the largest DeFi lending protocol by total 
value locked, ensuring sufficient sample size; (ii) its Health Factor 
mechanism provides a well-defined, continuously observable risk metric; 
and (iii) its event structure is sufficiently rich for reconstructing 
position-level behavioral trajectories.

To assess external validity, the analysis is replicated on Compound III 
and MakerDAO/Sky, with important caveats. These protocols differ from 
Aave V3 in structurally important ways: Compound III uses a single 
base asset per market and an absorb-based (rather than liquidator-based) 
liquidation mechanism, with different collateral factor parameters for 
borrowing and liquidation; MakerDAO uses a Vault structure with 
auction-based liquidation. Furthermore, event semantics differ across 
protocols: for example, "Supply" in Compound III denotes returning the 
base asset (functionally equivalent to repayment), not depositing 
collateral as in Aave. Consequently, the three protocols are analyzed 
separately rather than pooled into a single panel, and cross-protocol 
comparisons are conducted by examining whether the core behavioral 
findings replicate across different protocol architectures rather than 
by direct parameter comparison.
```

### 支撑文献

| 文献 | 如何支撑这个修正 |
|------|-----------------|
| Iftikhar et al. (2025) | 直接比较了 Aave 和 Compound 的风险管理机制差异 |
| Bartoletti & Lipparini (2025) | 形式化了不同 DeFi 借贷协议的结构差异 |
| Tovanich et al. (2023) | 在 Compound V2 中分析——单一协议分析的优秀范例 |
| Schuler (2026) — *Frictions in DeFi Liquidations* | 在 Aave V2 中分析——单一协议分析的优秀范例 |

---

## 3.11 问题 11："Credit-Relevant Information" 反复使用，超出范围

### 🟡 严重程度：过度声称（Over-claim）

**位置**：`sections/introduction.tex`，`sections/literature-review.tex`，`sections/research-topic.tex`，`sections/discussion.tex`

### 问题是什么？

这是问题 05（Credit Layer 命名）、07（Liquidation vs Default）、08（Collateral vs Credit）的综合体现。"Credit-relevant information"、"credit signals"、"credit prediction"等术语在 Report v1 中反复出现，贯穿全文，形成一致的过度声称模式。

### Report v1 原文中的出现位置

| 位置 | 原文中的术语 |
|------|------------|
| 标题 | "Credit Signals" |
| Abstract | "credit risk" |
| Introduction | "credit-oriented layer" |
| Literature Review 标题 | "On-Chain Credit Risk Assessment" |
| Literature Review 正文 | "credit risk assessment and default prediction" |
| Research Topic | "credit-relevant information", "credit risk assessment" |
| Discussion | "credit-relevant information", "credit prediction" |

### 为什么这是一个问题？

这些术语暗示本研究在做信用评估（credit assessment），但实际上本研究做的是清算预测（liquidation prediction）。两者的区别在前面的案例中已经详细说明（见问题 07 和 08）。

```
术语使用的正确场景：

"Credit" 可以使用的场景：
  ✅ 描述传统金融作为对比（"traditional credit markets"）
  ✅ 引用现有文献标题（"On-Chain Credit Risk Score" by Ghosh et al.）
  ✅ 描述未来研究方向（"potential connection to credit assessment"）

"Credit" 不应该使用的场景：
  ❌ 描述本研究的研究内容（应为 "liquidation prediction"）
  ❌ 描述本研究的发现（应为 "risk-relevant information"）
  ❌ 描述本研究的贡献（应为 "liquidation risk prediction"）
  ❌ 作为 RQ 的名称（应为 "Liquidation Propensity Layer"）
```

### 根源在哪里？

这个问题是问题 05、07、08 的共同症状。根源在于"credit"一词在研究设计初期被选用来描述研究的大方向，但随着研究设计的精确化，"credit"已经不能准确描述研究的实际内容。但这个词已经渗透到全文的各个部分，形成了一致的 over-claiming 模式。

### 如何解决？

全文系统性替换，并新增统一原则声明。

### 具体修改了什么？

**全文术语替换表**：

| ❌ 删除的术语 | ✅ 新增的术语 | 出现位置 |
|------------|------------|---------|
| "Credit Signals" (标题) | "Position Management Behavior and Liquidation Risk" | 标题 |
| "credit risk" (描述 DeFi) | "liquidation risk" 或 "position risk" | abstract, 全文 |
| "credit-oriented layer" | "predictive layer" | introduction |
| "Credit Layer" (RQ2) | "Liquidation Propensity Layer" | research-topic |
| "credit risk assessment" (描述本研究) | "liquidation risk prediction" | research-topic, discussion |
| "credit prediction" | "liquidation prediction" | discussion |
| "credit-relevant information" | "risk-relevant information" 或 "liquidation-relevant information" | introduction, research-topic, discussion |
| "On-Chain Credit Risk Assessment" (Lit Review 标题) | "On-Chain Risk Assessment and Predictive Modeling" | literature-review |

**新增的全局声明**：

```latex
A terminological clarification is warranted. The present study 
investigates whether protocol-observable position management behavior 
provides incremental information for predicting liquidation---a 
position-level, mechanically triggered event. We use "risk-relevant 
information" to describe this incremental predictive content, reserving 
"credit" for discussions of traditional credit markets and future 
research directions. The study does not claim to assess 
creditworthiness, improve credit scoring, or identify credit signals 
in the traditional sense.
```

### 支撑文献

| 文献 | 如何支撑这个修正 |
|------|-----------------|
| Berg et al. (2020) | Digital footprint 提供 incremental information——核心启示是 complement 而非 substitute |
| Gambacorta et al. (2024) | 系统梳理 alternative data 在信用评估中的角色——Paper 1 与之的区别在于 outcome 不同 |
| Ghosh et al. (2024) | 直接做 on-chain credit scoring——Paper 1 与之的区别在于 Paper 1 不声称做 credit scoring |

---

# 第四部分：文献变更清单

本部分完整记录了修订过程中**新增的文献**和**保留的文献**，以及每篇文献在修订中扮演的角色。

## 4.1 文献使用原则

在修订过程中，我们采用了以下文献使用原则：

```
Top Journal Literature（顶级期刊文献）
  → 决定理论语言
  → What should this construct mean?
  → 用于定义经济机制和理论框架

Recent Working Papers（近期工作论文）
  → 决定研究竞争边界
  → What has already been done?
  → 用于确认当前前沿和直接竞争
```

两类缺一不可：顶级期刊文献提供了理论严谨性，近期工作论文确保了研究的时效性。

## 4.2 新增文献（本次修订中引入的文献）

以下文献是本次修订过程中通过 `paper_search` 工具搜索并引入的。每篇文献都标注了它在哪个问题的修正中发挥了作用。

### 4.2.1 区块链基础 / Blockchain Foundation

| # | 文献 | 年份 | RECENCY | 新增用途 |
|---|------|------|---------|---------|
| 1 | Budish & Sunderam — *Blockchain Technology for Traditional Finance* | 2026 | ★newest | 分析 blockchain trust model 的限制，支撑问题 04（可观测性）和问题 09（settlement 层级） |
| 2 | Auer, Monnet, Shin — *Distributed ledgers and the governance of money* | 2025 | ≤1.5y | 从货币治理角度理解 DeFi 在金融体系中的位置 |
| 3 | Ferreira — *The Myths of Blockchain Governance* | 2025 | ≤1y | 提醒 DeFi 的"去信任"并非完全消除信任，支撑问题 08（Collateral vs Credit） |
| 4 | Wright — *Beyond 'permissionless'* | 2026 | ≤1y | 对 "permissionless" 概念的批判性审视 |
| 5 | Gramlich, Jelito, Sedlmeir — *Maximal extractable value* | 2024 | ≤2y | MEV 影响 liquidation 执行环境，是 Realized Liquidation 的混淆因素 |
| 6 | Hautsch, Scheuch, Voigt — *Building trust takes time* | 2024 | ≤2y | 区分技术结算和经济结算，支撑问题 09（settlement 层级） |

### 4.2.2 抵押与信用理论 / Collateral & Credit Theory

| # | 文献 | 年份 | RECENCY | 新增用途 |
|---|------|------|---------|---------|
| 7 | Ioannidou, Pavanini, Peng — *Collateral and Asymmetric Information* | 2022 | older | Collateral 不只是 loss protection，也有 screening/signaling 功能。支撑问题 08（Collateral vs Credit） |
| 8 | Asriyan, Laeven, Martín — *Collateral Booms and Information Depletion* | 2021 | older | Collateral boom 导致信息生产减少——与"行为信息能否替代抵押"相关 |
| 9 | Berg, Fuster, Puri — *FinTech Lending* | 2021 | older | FinTech underwriting 与 alternative data 在信用评估中的角色 |
| 10 | Di Maggio & Yao — *Fintech Borrowers: Lax-Screening or Cream-Skimming?* | 2020 | older | Alternative data 并不会自动消除 selection problem。支撑问题 07 和 08 |
| 11 | Boot, Hoffmann, Laeven, Ratnovski — *Fintech: what's old, what's new?* | 2020 | older | 理解传统金融中介与 DeFi 的功能差异 |
| 12 | He, Huang, Zhou — *Open Banking: Credit Market Competition* | 2020 | older | 数据所有权与信用评估的关系 |

### 4.2.3 DeFi 借贷 / DeFi Lending

| # | 文献 | 年份 | RECENCY | 新增用途 |
|---|------|------|---------|---------|
| 13 | Sadeghi & Feinstein — *Liquidation Dynamics in DeFi and the Role of Transaction Fees* | 2026 | ★newest | 直接涉及 Realized Liquidation 的执行摩擦。支撑问题 07（Liquidation vs Default）和问题 10（协议差异） |
| 14 | Campello, Gallo, Mota, Terracciano — *Demand for Safety in the Crypto Ecosystem* | 2026 | ★newest | 提供安全资产需求的宏观背景 |
| 15 | Wu — *Tokens All the Way Down: A Money View of DeFi* | 2026 | ★newest | 从货币视角分析 DeFi 中的多层信用创造结构 |
| 16 | Sevim — *Interoperability Effects: Multi-Chain DeFi Lending Risk* | 2026 | ★newest | 跨链风险背景 |
| 17 | Oberholzer & Zamaraiev — *Institutional DeFi Risk Assessment Framework* | 2026 | ★newest | 提供协议级风险背景 |
| 18 | Bartoletti & Lipparini — *A theory of Lending Protocols in DeFi* | 2025 | ≤1.5y | 形式化了 DeFi 借贷协议的结构差异。支撑问题 03（Supply vs Collateral）和问题 10（协议差异） |
| 19 | Iftikhar, Wei, Cartlidge — *Automated Risk Management in DeFi* | 2025 | ≤1.5y | 直接比较 Aave 和 Compound 的风险管理机制差异。支撑问题 01（HF 公式）、02（分类）、03（Supply）、10（协议差异） |
| 20 | Chitra — *A Curationary Tale: Logarithmic Regret in DeFi Lending* | 2025 | ≤1.5y | DeFi 借贷利率机制背景 |
| 21 | Qu, Gogol, Groetschla, Tessone — *From Rules to Rewards: RL for Interest Rate Adjustment* | 2025 | ≤1.5y | 利率机制优化背景 |
| 22 | Belenko & Vosorov — *DeFi Liquidation Risk Modeling Using GBM* | 2025 | ≤1.5y | 清算概率建模——与 outcome 定义相关 |
| 23 | Bastankhah et al. — *AgileRate: Bringing Adaptivity to DeFi Lending* | 2024 | ≤2y | DeFi 借贷利率机制改进背景 |
| 24 | Ghosh et al. — *On-Chain Credit Risk Score in DeFi* | 2024 | ≤2y | **直接竞争文献**。使用 ML 方法做链上信用评分。支撑问题 05、07、08、11（区分 Paper 1 与之的定位差异） |

### 4.2.4 替代数据与信用评分 / Alternative Data & Credit Scoring

| # | 文献 | 年份 | RECENCY | 新增用途 |
|---|------|------|---------|---------|
| 25 | Gambacorta et al. — *Data sources and ML methods for credit scoring* | 2024 | ≤2y | 系统梳理 alternative data 在信用评估中的角色。支撑问题 08 和 11 |
| 26 | Chioda, Kozakowski, Smith — *FinTech Lending to Borrowers with No Credit History* | 2024 | ≤2y | Transaction-level data 对预测 default 有显著增量预测力。支撑问题 08 和 11 |
| 27 | Fuster, Goldsmith, Ramadorai, Walther — *ML in Consumer Lending* | 2022 | older | ML 在信用评估中的实证基础 |
| 28 | Puri, Rocholl, Steffen, Zanetti — *ML in Consumer Credit: Default Risk* | 2024 | ≤2y | ML 违约预测的方法论参考 |

### 4.2.5 支付与结算 / Payment & Settlement

| # | 文献 | 年份 | RECENCY | 新增用途 |
|---|------|------|---------|---------|
| 29 | Li, Zou, Liu, Ma, Zhao — *SoK: Stablecoins in Retail Payments* | 2026 | ★newest | 系统综述稳定币在零售支付中的应用。Paper 2 的核心文献 |
| 30 | Gertler, Höferle, Schittekatte, Gasior — *Stablecoins and the Future of Money* | 2026 | ★newest | 稳定币的货币/支付角色 |
| 31 | Bains et al. (IMF) — *Stablecoin Policy and Operations* | 2025 | ≤1.5y | 稳定币监管背景 |

## 4.3 保留的文献（Report v1 中已有，修订后继续使用）

以下文献在 Report v1 中已经引用，修订后继续保留使用：

| # | 文献 | 年份 | 保留原因 |
|---|------|------|---------|
| 1 | Schär — *Decentralized Finance: On Blockchain- and Smart Contract-Based Financial Markets* | 2021 | DeFi 的系统性综述，定义 DeFi 的基本架构 |
| 2 | Cong & He — *Blockchain Disruption and Smart Contracts* | 2019 | 定义 blockchain 对 contracting/information/consensus 的经济意义 |
| 3 | Huberman, Leshno, Moallemi — *Monopoly without a Monopolist* | 2021 | 从 payment-system economics 理解 blockchain payment |
| 4 | Kahneman & Tversky — *Prospect Theory* | 1979 | PT 原始定义——reference point, loss aversion |
| 5 | Tversky & Kahneman — *Advances in Prospect Theory: Cumulative Representation* | 1992 | Cumulative Prospect Theory |
| 6 | Barberis — *Thirty Years of Prospect Theory in Economics* | 2013 | PT 在金融中的应用综述 |
| 7 | Benartzi & Thaler — *Myopic Loss Aversion and the Equity Premium Puzzle* | 1995 | Myopic loss aversion |
| 8 | Qin et al. — *An empirical study of DeFi liquidations* | 2021 | 最早系统分析 DeFi 清算事件的研究之一 |
| 9 | Perez et al. — *Liquidations: DeFi on a Knife-Edge* | 2021 | DeFi 清算机制的早期系统分析 |
| 10 | Gudgeon et al. — *DeFi Protocols for Loanable Funds* | 2020 | DeFi 可贷资金协议的基础架构文献 |
| 11 | Tovanich et al. — *Contagion in Decentralized Lending Protocols* | 2023 | 协议级风险背景 |
| 12 | Berg et al. — *Credit Scoring Using Digital Footprints* | 2020 | 核心启示：alternative data 首先是 complement 而非 substitute |

## 4.4 文献时间梯度覆盖

为确保文献的时效性，本次修订遵循了"最近优先"原则。以下是新增文献的时间分布：

```
时间梯度分布（新增文献 31 篇）：

≤6 个月 (★newest)  ：8 篇（26%）  ████████████████
≤1 年              ：3 篇（10%）  ██████
≤1.5 年            ：6 篇（19%）  ████████████
≤2 年              ：7 篇（23%）  ██████████████
older（基础理论）   ：7 篇（23%）  ██████████████

总结：
  最近 6 个月内的文献占 26%
  最近 2 年内的文献占 77%
  较早文献仅用于基础理论背景（23%）
```

---

# 第五部分：术语变更清单

本部分完整记录了修订过程中所有术语的变更。

## 5.1 删除的术语

以下术语在 Report v1 中使用，但在修订后被删除或替换：

| ❌ 删除的术语 | 出现位置 | 删除原因 |
|------------|---------|---------|
| "Credit Signals" | 标题 | DeFi 借贷不是信用借贷；研究的是仓位风险信号，不是信用信号 |
| "credit risk"（描述 DeFi 时） | abstract, 全文 | DeFi 的风险是仓位风险/清算风险，不是信用风险 |
| "credit-oriented layer" | introduction | RQ2 是清算预测，不是信用评估 |
| "Credit Layer"（RQ2 命名） | research-topic | 清算 ≠ 信用违约 |
| "credit risk assessment"（描述本研究） | research-topic, discussion | 本研究做的是清算风险预测 |
| "credit prediction" | discussion | 应为清算预测 |
| "credit-relevant information" | introduction, research-topic, discussion | 应为风险相关信息 |
| "credit signals" | 标题, discussion | 应为仓位风险信号 |
| "On-Chain Credit Risk Assessment" | literature-review 标题 | 应为风险评估与预测建模 |
| "complete transparency" | introduction | 应为"公开且可验证的交易记录" |
| "complete observability of all borrower actions" | literature-review | 应为"协议层面事件的完全可观测" |
| "the creation and settlement of loan positions" | methodology | "settlement"有多层含义，改为"repayment" |
| "LTV"（在 HF 公式中） | methodology | 应使用 LT（Liquidation Threshold） |
| "testing prospect theory predictions" | research-topic, discussion | 降级为"examining whether patterns are consistent with PT" |
| "prospect theory's predictions are observable" | discussion | 降级为"patterns consistent with reference-point behavior" |
| "default"（描述 DeFi outcome 时） | literature-review | 应使用"liquidation" |
| "default prediction"（描述本研究时） | literature-review | 应使用"liquidation prediction" |

## 5.2 新增的术语

以下术语在修订后新引入：

| ✅ 新增的术语 | 含义 | 引入原因 |
|------------|------|---------|
| "Liquidation Propensity Layer" | RQ2 的新名称 | 准确描述研究内容——清算倾向预测 |
| "Position Management Behavior" | 描述研究的行为类型 | 区分于"credit behavior"，准确反映研究的是仓位管理 |
| "Liquidation Risk" | 描述研究的风险类型 | 区分于"credit risk" |
| "Risk-relevant Information" | 描述研究发现的增量信息 | 区分于"credit-relevant information" |
| "Liquidation-relevant Information" | 同上的替代措辞 | 更精确地限定信息类型 |
| "Protocol-observable Events" | 描述可观测的范围 | 区分于"all borrower actions" |
| "Liquidation Threshold (LT)" | HF 公式中的正确参数 | 区分于 LTV |
| "Collateral-enabled Supply" | 描述启用了抵押的 Supply | 区分于普通 Supply |
| "SetUserUseReserveAsCollateral" | Aave V3 中的抵押启用事件 | 追踪 collateral 状态变化 |
| "onBehalfOf" | Aave V3 事件参数 | 用于主动/被动分类 |
| "Compelling competing explanation" | PT 的新定位 | 区分于"confirmed theory anchor" |
| "Protocol-level Settlement" | settlement 的第 2 层含义 | 区分技术结算和经济结算 |
| "Technical / Ledger Settlement" | settlement 的第 1 层含义 | 交易上链、执行、最终确认 |
| "Economic / Business Settlement" | settlement 的第 3 层含义 | 商业上的最终结算 |
| "Liquidation Eligibility" | HF < 1 的状态 | 区分于 Realized Liquidation |
| "Realized Liquidation" | 实际发生的清算 | 区分于 Eligibility |
| "Position Distress" | 仓位困境 | RQ2 outcome 的替代措辞 |

## 5.3 术语变更总结图

```
术语变更的核心逻辑：

从                                         到
────────────────────────────────────────────────────────────────

"Credit Signals"                     →    "Position Risk Signals"
"Credit Risk"                        →    "Liquidation Risk"
"Credit Layer" (RQ2)                 →    "Liquidation Propensity Layer"
"Credit-relevant Information"        →    "Risk-relevant Information"
"Credit Assessment"                  →    "Liquidation Risk Prediction"
"Default" (in DeFi)                 →    "Liquidation"
"Complete Observability"             →    "Protocol-observable Events"
"Testing PT Predictions"             →    "Examining Patterns Consistent with PT"
"Confirmed Theory Anchor" (PT)       →    "Compelling Competing Explanation"
"LTV" (in HF formula)                →    "LT" (Liquidation Threshold)
"Supply = Collateral"                →    "Supply ≠ Collateral-Enabled Supply"
"msg.sender == borrower"             →    "Multi-layer Classification"
"Settlement" (不分层)                 →    "Repayment" 或标注层级的 "Settlement"
"Three Protocols Pooled"             →    "Aave V3 Primary, Others for Validation"

────────────────────────────────────────────────────────────────

核心原则：
  Collateral ≠ Credit
  Liquidation ≠ Default  
  Supply ≠ Collateral-Enabled Supply
  Protocol-observable ≠ Complete Borrower Behavior
  PT Framing ≠ PT Confirmation
  Aave HF ≠ Compound Shortfall ≠ Maker Collateralization Ratio
```

---

# 第六部分：信息来源

本部分列出修订报告中所有信息的来源，确保每一条修正都有可追溯的依据。

## 6.1 六层矩阵文件

所有问题的诊断和修正方案均基于以下六层矩阵文件：

| 文件路径 | 内容 |
|---------|------|
| `2026-08-11_六层矩阵_Paper1/00_README.md` | 六层矩阵导航与使用说明 |
| `2026-08-11_六层矩阵_Paper1/01_六层矩阵总表.md` | 12个在范围内概念 + 6个边界概念的总表 |
| `2026-08-11_六层矩阵_Paper1/02_逐概念六层矩阵/01_Collateral_抵押.md` | Collateral 概念的六层矩阵 |
| `2026-08-11_六层矩阵_Paper1/02_逐概念六层矩阵/02_Position_Risk_仓位风险.md` | Position Risk 概念的六层矩阵 |
| `2026-08-11_六层矩阵_Paper1/02_逐概念六层矩阵/03_Health_Factor_健康因子.md` | Health Factor 概念的六层矩阵 |
| `2026-08-11_六层矩阵_Paper1/02_逐概念六层矩阵/04_Distance_to_Liquidation_清算距离.md` | Distance to Liquidation 概念的六层矩阵 |
| `2026-08-11_六层矩阵_Paper1/02_逐概念六层矩阵/05_Borrow_借款.md` | Borrow 概念的六层矩阵 |
| `2026-08-11_六层矩阵_Paper1/02_逐概念六层矩阵/06_Repay_还款.md` | Repay 概念的六层矩阵 |
| `2026-08-11_六层矩阵_Paper1/02_逐概念六层矩阵/07_Supply_vs_CollateralEnabled_供给与抵押启用.md` | Supply vs Collateral-Enabled 概念的六层矩阵 |
| `2026-08-11_六层矩阵_Paper1/02_逐概念六层矩阵/08_Borrower_Adjustment_借款人调整行为.md` | Borrower Adjustment 概念的六层矩阵 |
| `2026-08-11_六层矩阵_Paper1/02_逐概念六层矩阵/09_Active_vs_Passive_主动与被动分类.md` | Active vs Passive 概念的六层矩阵 |
| `2026-08-11_六层矩阵_Paper1/02_逐概念六层矩阵/10_Liquidation_Eligibility_清算资格.md` | Liquidation Eligibility 概念的六层矩阵 |
| `2026-08-11_六层矩阵_Paper1/02_逐概念六层矩阵/11_Realized_Liquidation_实际清算.md` | Realized Liquidation 概念的六层矩阵 |
| `2026-08-11_六层矩阵_Paper1/02_逐概念六层矩阵/12_Borrower_Identity_借款人身份.md` | Borrower Identity 概念的六层矩阵 |
| `2026-08-11_六层矩阵_Paper1/02_逐概念六层矩阵/13_Boundary_Concepts_边界概念.md` | Transfer/Payment/Settlement/Finality/Default/Creditworthiness 边界概念 |
| `2026-08-11_六层矩阵_Paper1/05_不可声称清单.md` | 9类不可声称（40+条目） |
| `2026-08-11_六层矩阵_Paper1/06_术语边界对照表.md` | 术语 ≠ 对照 + 协议间映射 + 正确措辞替换 |

## 6.2 技术文档来源

所有技术细节均来自以下官方文档和文档文件：

| 技术文档 | 官方来源 | 文件路径 |
|---------|---------|---------|
| Aave V3 | https://docs.aave.com/ | `03_技术文档/01_Aave_V3.md` |
| Compound III | https://docs.compound.finance/ | `03_技术文档/02_Compound_III.md` |
| MakerDAO / Sky | https://docs.makerdao.com/ | `03_技术文档/03_MakerDAO_Sky.md` |
| Chainlink Oracle | https://docs.chain.link/data-feeds | `03_技术文档/04_Chainlink_Oracle.md` |
| Ethereum Finality | https://ethereum.org/en/developers/docs/consensus-mechanisms/pos/ | `03_技术文档/05_Ethereum_Finality.md` |
| Dune Analytics | https://dune.com/docs/ | `03_技术文档/06_Dune_Analytics.md` |

### 关键技术信息的获取方式

- **Aave V3 HF 公式（LT vs LTV）**：来自 Aave V3 官方文档 https://docs.aave.com/developers/concepts/health-factor
- **Aave V3 事件类型和 onBehalfOf 参数**：来自 Aave V3 官方文档和 GitHub 仓库 https://github.com/aave/aave-v3-core
- **Aave V3 Collateral-Enabled 状态**：来自 Aave V3 官方文档关于 SetUserUseReserveAsCollateral 的说明
- **Compound III 的 Supply/Withdraw 语义反转**：来自 Compound III 官方文档 https://docs.compound.finance/
- **MakerDAO 的拍卖式清算**：来自 MakerDAO 官方文档 https://docs.makerdao.com/
- **Ethereum PoS Finality 机制**：来自 Ethereum 官方文档 https://ethereum.org/en/developers/docs/consensus-mechanisms/pos/
- **Chainlink 价格预言机机制**：来自 Chainlink 官方文档 https://docs.chain.link/data-feeds

## 6.3 文献来源

所有文献均来自以下搜索来源，**无虚构引用**：

### 搜索工具

- `paper_search`：用于搜索 arXiv、OpenAlex、PubMed 等学术数据库
- 搜索覆盖 5 个主题：
  1. Collateral / Credit Theory
  2. DeFi Lending / Liquidation
  3. Blockchain Foundation / Smart Contracts
  4. Alternative Data / Credit Scoring
  5. Stablecoin / Payment / Settlement

### 文献验证

- 所有新增文献均来自实际的 `paper_search` 搜索结果
- 每篇文献的标题、作者、年份、DOI、链接均来自搜索结果，未手动修改
- 文献按 NEWEST → OLDEST 排序

### 文献文件位置

| 文献主题 | 文件路径 |
|---------|---------|
| 文献总表 | `2026-08-11_六层矩阵_Paper1/04_文献/00_文献总表.md` |
| 区块链基础 | `2026-08-11_六层矩阵_Paper1/04_文献/01_Blockchain_Foundation/README.md` |
| 抵押与信用理论 | `2026-08-11_六层矩阵_Paper1/04_文献/02_Collateral_Credit/README.md` |
| DeFi 借贷 | `2026-08-11_六层矩阵_Paper1/04_文献/03_DeFi_Lending/README.md` |
| 替代数据与信用评分 | `2026-08-11_六层矩阵_Paper1/04_文献/04_Alternative_Data_CreditScoring/README.md` |
| 支付与结算 | `2026-08-11_六层矩阵_Paper1/04_文献/05_Payment_Settlement/README.md` |

## 6.4 诊断改进映射文件

每个问题的详细诊断和修正方案均来自以下文件：

| 问题 | 诊断文件路径 |
|------|------------|
| 01 HF 公式错误 | `2026-08-11_诊断改进映射_Paper1/02_逐问题诊断与改进/01_HF公式错误_LT_vs_LTV.md` |
| 02 主动/被动分类 | `2026-08-11_诊断改进映射_Paper1/02_逐问题诊断与改进/02_主动被动分类_msg_sender.md` |
| 03 Supply vs Collateral-Enabled | `2026-08-11_诊断改进映射_Paper1/02_逐问题诊断与改进/03_Supply_vs_CollateralEnabled.md` |
| 04 完全可观测性 | `2026-08-11_诊断改进映射_Paper1/02_逐问题诊断与改进/04_完全可观测性声称.md` |
| 05 Credit Layer 命名 | `2026-08-11_诊断改进映射_Paper1/02_逐问题诊断与改进/05_Credit_Layer命名与Credit过度声称.md` |
| 06 Prospect Theory 定位 | `2026-08-11_诊断改进映射_Paper1/02_逐问题诊断与改进/06_Prospect_Theory定位.md` |
| 07 Liquidation vs Default | `2026-08-11_诊断改进映射_Paper1/02_逐问题诊断与改进/07_Liquidation_vs_Default混用.md` |
| 08 Collateral vs Credit | `2026-08-11_诊断改进映射_Paper1/02_逐问题诊断与改进/08_Collateral_vs_Credit混用.md` |
| 09 Settlement 层级 | `2026-08-11_诊断改进映射_Paper1/02_逐问题诊断与改进/09_Settlement层级混淆.md` |
| 10 协议间术语 | `2026-08-11_诊断改进映射_Paper1/02_逐问题诊断与改进/10_协议间术语混用.md` |
| 11 Credit-Relevant Information | `2026-08-11_诊断改进映射_Paper1/02_逐问题诊断与改进/11_Credit_Relevant_Information过度声称.md` |

## 6.5 Report v1 原文来源

所有 Report v1 原文引用均来自以下文件：

| 章节 | 文件路径 |
|------|---------|
| Abstract | `2026-07-17_Research_Report/sections/abstract.tex` |
| Introduction | `2026-07-17_Research_Report/sections/introduction.tex` |
| Literature Review | `2026-07-17_Research_Report/sections/literature-review.tex` |
| Research Topic | `2026-07-17_Research_Report/sections/research-topic.tex` |
| Methodology | `2026-07-17_Research_Report/sections/methodology.tex` |
| Discussion | `2026-07-17_Research_Report/sections/discussion.tex` |
| Main (标题等) | `2026-07-17_Research_Report/main.tex` |

## 6.6 纠错包来源

部分问题的识别还参考了以下纠错文件：

| 文件 | 路径 |
|------|------|
| 纠错包 README | `V4-New_Branch/2026-08-11 定义、数据、范围更新&纠错/00_README.md` |
| 区块链支付边界约束定义 | `V4-New_Branch/2026-08-11 定义、数据、范围更新&纠错/2026-08-11_区块链支付_边界约束定义_文献核对与研究修订.md` |

---

## 附录：修订工作流程总结

```
修订工作流程：

Step 1: 阅读并理解 Report v1 全文
    ↓
Step 2: 构建"六层矩阵"框架
    → 为每个核心概念定义六个层次
    → Definition → Construct → Measurement → Observable → Identification → Allowed Claim
    ↓
Step 3: 搜索文献
    → 使用 paper_search 搜索 5 个主题
    → 获取 31 篇新增文献
    → 确保时间梯度覆盖（最近 6 个月/1 年/2 年）
    ↓
Step 4: 获取技术文档
    → 从 Aave、Compound、MakerDAO、Chainlink、Ethereum 官方文档获取技术细节
    → 验证 HF 公式、事件类型、清算机制等
    ↓
Step 5: 逐概念审查
    → 将 Report v1 的每个概念与六层矩阵对照
    → 识别"声称"与"可观测"之间的差距
    → 发现 11 个问题
    ↓
Step 6: 逐问题诊断
    → 为每个问题撰写诊断文件
    → 包含原文引用、错误分析、修正方案、文献支撑、修正后文本
    ↓
Step 7: 撰写本修订报告
    → 整合所有诊断结果
    → 完整记录增加/删除的内容
    → 列出所有文献变更和术语变更
    → 标注所有信息来源
```

---

**本修订报告到此结束。**

所有修正均有据可查，所有文献均来自实际搜索，所有技术细节均来自官方文档。修订后的研究设计在构念效度上显著优于 Report v1，为后续研究执行奠定了更坚实的基础。