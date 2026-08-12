# 04. "完全可观测性"声称过强

**严重程度**：🟡 Over-claim  
**Report 1 位置**：`sections/introduction.tex` Line 3, `sections/literature-review.tex` Line 21  
**六层矩阵文件**：`02_逐概念六层矩阵/08_Borrower_Adjustment.md`, `12_Borrower_Identity.md`

---

## 1. 问题描述

Report 1 多处声称 DeFi 提供"complete transparency"和"complete observability of all borrower actions"，暗示研究者可以完全观测借款人的行为。但公开链上数据只能观测协议事件（Supply, Borrow, Repay, Liquidation 等），不能观测借款人的经济目的、链下活动、跨协议活动、CEX 活动等。

---

## 2. Report 1 原文

> **introduction.tex, Line 3:**
>
> The complete transparency of these protocols means that every deposit, withdrawal, borrowing event, repayment, collateral adjustment, and liquidation is immutably recorded on a public blockchain, creating an unprecedented empirical window into the behavior of financial market participants operating under varying degrees of risk exposure.

> **literature-review.tex, Line 21:**
>
> Furthermore, the complete observability of all borrower actions in DeFi—including collateral additions, debt repayment, additional borrowing, and collateral withdrawals—means that behavioral responses to proximity to the liquidation threshold can be measured with a level of granularity that would be impossible in traditional credit markets.

> **discussion.tex, Line 37:**
>
> The analysis is limited to on-chain transactions, which means that it cannot observe borrower behavior on centralized exchanges or off-chain activities.

---

## 3. 错误分析

### 3.1 可观测 vs 不可观测

| 可观测（公开链上数据） | 不可观测（需要额外数据或无法获取） |
|----------------------|-------------------------------|
| 协议事件（Supply, Borrow, Repay, Liquidation 等） | 借款人的经济目的/意图 |
| 事件参数（amount, onBehalfOf, asset 等） | 链下活动（CEX 对冲、OTC 交易） |
| 交易时间戳、区块号 | 跨协议活动（除非全面追踪所有协议） |
| 合约参数（LT, LTV, 利率等） | 借款人的真实身份 |
| 预言机价格 | 借款人的风险偏好 |
| 交易调用链（trace） | 借款人的整体财务状况 |

### 3.2 "Complete observability" 的误导性

- "Complete observability of all borrower actions" 暗示所有借款人行为都可以观测——但实际只能观测协议事件
- 借款人可能在 CEX 上对冲仓位，或在其他协议上管理相关仓位，这些行为不可观测
- Discussion 部分虽然承认了这一点（L37），但 Introduction 和 Literature Review 中的"complete"措辞与之矛盾

### 3.3 影响

- 如果声称"complete observability"，reviewer 可能质疑：借款人的整体经济行为是否真的完全可观测？
- 这会削弱论文的可信度，因为 over-claiming 会让 reviewer 质疑作者对数据的理解深度

---

## 4. 六层矩阵映射

| 层级 | 六层矩阵内容 | Report 1 的问题 |
|------|-------------|-----------------|
| Observable | 协议事件可观测；经济目的、链下行为不可观测 | 声称"complete observability" |
| Allowed Claim | "we observe protocol events initiated by borrower addresses" | 声称"complete observability of all borrower actions" |

**不可声称清单**：`05_不可声称清单.md` §3.1 "我们完全观测了借款人行为"

---

## 5. 修正方案

### 5.1 术语替换

| ❌ 不应使用 | ✅ 应使用 |
|-----------|---------|
| "complete transparency" | "public and verifiable transaction records" |
| "complete observability of all borrower actions" | "complete observability of protocol-level events" |
| "every deposit, withdrawal, borrowing event..." | 保留，但加上限定："at the protocol level" |
| "unprecedented empirical window into the behavior of financial market participants" | "unprecedented empirical window into protocol-level position management behavior" |

### 5.2 关键区分

在论文中明确区分：
- **Protocol-observable events**（协议可观测事件）：可以被任何观察者从公开链上数据中提取的事件
- **Economic purpose / intent**（经济目的/意图）：无法从公开链上数据中直接推断

### 5.3 一致性

确保 Introduction、Literature Review 和 Discussion 中的措辞一致。Discussion 已经正确承认了局限性，Introduction 和 Literature Review 需要降级措辞以保持一致。

---

## 6. 文献支撑

| 文献 | 与本问题的关系 |
|------|---------------|
| Ghosh et al. (2024) — On-Chain Credit Risk Score | 使用链上数据但明确承认只能观测 wallet-level 行为，不能观测 off-chain 活动 |
| Cornelli et al. (2025) — Why DeFi Lending? | 在 Aave V2 数据中分析借贷行为，但也限制在 protocol-observable 范围 |
| Budish & Sunderam (2026) | 分析 blockchain trust model 的限制 |

---

## 7. 修改后的文本

### introduction.tex 修正

```latex
The public and verifiable nature of these protocols means that 
every protocol-level event---deposit, withdrawal, borrowing, 
repayment, collateral adjustment, and liquidation---is immutably 
recorded on a public blockchain, creating an unprecedented 
empirical window into the position management behavior of protocol 
participants operating under varying degrees of risk exposure. 
Importantly, however, this transparency is limited to 
\emph{protocol-observable events}: the economic purposes underlying 
these actions, as well as participants' off-chain and cross-platform 
activities, remain unobservable.
```

### literature-review.tex 修正

```latex
Furthermore, the complete observability of protocol-level events in 
DeFi---including collateral additions, debt repayment, additional 
borrowing, and collateral withdrawals---means that behavioral 
responses to proximity to the liquidation threshold can be measured 
with a level of granularity that would be impossible in traditional 
credit markets. It should be noted, however, that this observability 
extends only to protocol events; the economic motives underlying 
these actions and borrowers' activities outside the observed 
protocol are not directly observable from public blockchain data.
```
