# 定义纠错卡：抵押 / 支付 / 结算 / 清算

**日期**：2026-08-11  
**用途**：纠正 7 月 Report 及此前草稿中术语混用导致的“听起来很大、落点却空”的问题  
**依据**：2026-08-09 会议整理 + 信用微支付论文学习版 + 交叉审阅笔记

---

## 1. 为什么要单独纠定义？

原先在报告与讨论中，容易把下面这些词混在一起使用：

```text
质押 / 抵押 / 支付 / 结算 / 清算 / 信用 / 违约
```

混用后果：

1. 听者以为你在研究“链上信用支付”，实际数据却主要是 DeFi lending events；
2. 把 liquidation 当 credit default，理论对象错位；
3. 把 on-chain transfer 当完整经济行为，identification 不成立；
4. 把 collateral 简单骂成“旧金融逻辑”，反而说反了 blockchain-native 的一面。

本卡片只做一件事：**把词钉死。**

---

## 2. 最小记忆版

```text
Collateral  ≠ Credit
Payment     ≠ Settlement
Settlement  ≠ Liquidation
Liquidation ≠ Default
Transfer    ≠ Purpose
Staking     ≠ Collateralization
```

---

## 3. 逐词定义

### 3.1 Collateral / 抵押（金融抵押）

**定义**：为覆盖未来偿付义务，而预先锁定、可被协议执行处置的资产。

**典型形态**：

```text
Deposit ETH
→ Borrow USDC
→ ETH 作为 collateral
```

**它解决的问题**：

> 在不知道你是谁、也难以法院追债时，用可编程资产替代信任。

**它不自动等于**：

- 你有信用
- 你有稳定现金流
- 你值得被授予无抵押额度

**研究口径**：

> Collateralization is a trust-substitution mechanism, not by itself a credit-assessment mechanism.

---

### 3.2 Staking / 质押（共识或协议质押）

**定义**：为参与共识、安全或协议权利而锁定资产（如 PoS validator stake）。

**必须与 Collateral 分开写。**

口语里常说“质押借贷”，在论文中应优先写成：

> collateralized lending / overcollateralized borrowing

而不是笼统的“质押”。

---

### 3.3 Payment / 支付

**定义**：买家/付款方产生一笔付款行为，或形成一笔付款义务。

两种常见形态：

#### A. Direct on-chain payment

```text
Wallet A → Wallet B
Payment ≈ Settlement（资产已转移）
```

#### B. Credit-based / delayed settlement payment

```text
先产生 unsettled obligation
→ 稍后统一结算
Payment ≠ 即时 Settlement
```

会议语境中的“支付”，更强调：

> 用户—时间—金额—消费场景—消费类别

也就是带有**消费语义**的支付事件，而不只是转账发生。

---

### 3.4 Settlement / 结算

必须拆成三层，不能只用一个英文词糊弄：

| 层级 | 含义 | 公开数据可观测性 |
|---|---|---|
| **Technical / Ledger Settlement** | 交易上链、执行、状态更新、最终确认 | 高 |
| **Protocol-level Settlement** | 协议内义务了结（如 Repay、epoch settlement） | 高（若有明确事件） |
| **Economic / Business Settlement** | 这笔钱在商业上代表什么（货款、工资、OTC、归集等） | 低；通常需链下信息 |

会议里说的“现在很多需求其实是 settlement”，主要指：

> 跨境/B2B 资金流转与最终了结，而不一定是 C 端消费支付。

对研究的直接含义：

- 若研究资金跨境流转、商户间清算：更靠近 settlement
- 若研究个人消费行为与信用：必须进入真正的 payment 层，且最好有场景标签

---

### 3.5 Clearing / 清分

**定义**：先算清楚“谁欠谁多少”，尚未最终履行。

```text
Payment → Clearing → Settlement
```

不要把 clearing 与 liquidation 混称“清算”。中文里“清算”极易歧义，论文中应尽量写：

- clearing = 清分
- liquidation = 强制清算 / 风险处置

---

### 3.6 Liquidation / 强制清算

**定义**：当仓位风险超过协议阈值时，由第三方或机制强制处置抵押品、降低债务的风险处置过程。

```text
HF < 1（或等价条件）
→ Liquidation
→ Collateral seized / sold
→ Debt reduced
```

**它更接近**：

> position risk realization / forced deleveraging

**它不等于**：

> traditional credit default（借款人无能力/无意愿偿付的信用事件）

因为 overcollateralized DeFi 中，liquidation 可能来自：

- 抵押品价格暴跌
- 杠杆过高
- 未及时补仓
- gas / 操作摩擦
- 主动放弃救仓

---

### 3.7 Credit / 信用

**工作定义（本项目）**：

> 在不完全依赖足额或超额抵押的前提下，基于可验证身份与可观测经济行为，对主体未来偿付可信度作出的判断，并据此给予支付/借贷能力。

因此：

```text
有抵押物 ≠ 有信用
有清算历史 ≠ 有传统信用评分
有转账记录 ≠ 有消费信用信号
```

会议提出的转化命题：

```text
Risk Asset / Collateral Logic
→ Behavior + Identity
→ Credit Asset / Credit Signal
```

---

## 4. 四类机制对照（避免把所有链上金融当成一类）

| 机制 | Capacity 从哪来 | Payment 与 Settlement 关系 | 是否依赖抵押 |
|---|---|---|---|
| Direct on-chain payment | 钱包余额 | 常近似同时完成 | 通常不需要 |
| Payment channel（如 Lightning） | 预注入通道流动性 | 多次链下更新，关闭时结算 | 需要预锁资金，但不是 undercollateralized credit |
| Overcollateralized lending（Aave/Compound） | Collateral × 风险参数 | Borrow 与后续 Payment 是分开动作 | 高度依赖抵押 |
| Credit-based micropayment（不足额抵押信用支付） | Stake + history + trust/rules | 先支付义务，后 epoch settlement | 有抵押，但允许 CL > Stake |

当前 Paper 1 属于第 3 类：

> **Collateralized lending 中的 position-management behavior**

不是第 1 类普通支付，也还不是第 4 类不足额信用支付。

---

## 5. 对原 Report 的直接纠错句式

### 不建议再写

- “完全观测借款人行为”
- “liquidation 作为信用违约结果”
- “链上历史 = 经济行为历史”
- “区块链金融都靠质押”
- “抵押不符合 blockchain-native”

### 建议改写为

- “高粒度观测协议记录的仓位管理动作”
- “liquidation propensity / 仓位风险管理质量”
- “protocol action ≠ economic purpose”
- “permissionless DeFi lending 历史上高度依赖超额抵押”
- “抵押是信任替代机制；真正的问题是它是否完成了信用评估”

---

## 6. 一张图记住资金流与信息流

```text
资金流：
Collateral lock / repayment / slashing / liquidation proceeds

信息流：
tx / event / state / proof / label / (optional) off-chain purpose

研究时必须问：
我现在用的是资金流证据，还是信息流证据？
我声称的是协议动作，还是经济目的？
```

---

## 7. 本卡片对后续写作的硬约束

1. 中文初稿若写“质押”，必须在括号注明是 collateral 还是 staking。
2. 每次出现 settlement，必须标明是 technical / protocol / economic 哪一层。
3. 每次把结果叫 credit，必须说明信用结果变量如何构造；若只有 liquidation，就不要叫 credit default。
4. Payment 研究若没有场景/身份字段，只能声称 transfer/payment-like activity，不能声称消费行为信用。
