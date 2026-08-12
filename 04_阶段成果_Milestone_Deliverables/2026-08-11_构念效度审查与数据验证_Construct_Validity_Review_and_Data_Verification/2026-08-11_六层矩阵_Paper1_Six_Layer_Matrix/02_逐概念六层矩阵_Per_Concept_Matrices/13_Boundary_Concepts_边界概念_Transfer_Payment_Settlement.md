# 13. Boundary Concepts / 边界概念

**六层矩阵详细文件**  
**相关技术文档**：`03_技术文档/05_Ethereum_Finality.md`  
**相关文献**：`04_文献/01_Blockchain_Foundation/`, `04_文献/05_Payment_Settlement/`

---

## 概述

以下概念**不在 Paper 1 范围内**，但需要明确定义边界，以防止在写作中无意混入。

---

## 1. Transfer / 转账

### Definition

> 链上 token 所有权/余额状态的变化。Address A → Token transfer → Address B。

### 为什么不在 Paper 1

Paper 1 研究的是协议事件（Borrow, Repay, Supply, Withdraw, Liquidation），不是普通转账。普通转账是 Paper 2 的研究对象。

### Paper 1 中的处理

- 不直接使用普通转账数据
- 如果研究需要追踪借款资金去向，明确说明这是 transfer observation，不是 economic purpose identification

### 不可声称

- "Transfer = payment"（转账 = 支付）
- "Transfer history = economic behavior history"（转账历史 = 经济行为历史）

---

## 2. Payment / 支付

### Definition

> 产生一笔付款行为或付款义务。

### 为什么不在 Paper 1

支付识别是一个独立的研究问题（Paper 2）。公开链上数据只能看到 transfer，不能直接看到 payment purpose。

### Paper 1 中的处理

- 不使用 "payment" 一词来描述协议事件
- 如果讨论借款资金用途，明确说明无法从公开数据识别

### 不可声称

- "Consumer payment"（消费者支付）
- "Consumption behavior"（消费行为）
- "Merchant purchase"（商户购买）——除非有链下标签

---

## 3. Settlement / 结算

### Definition

> 对既有义务的最终确认与履行。必须拆成三层：

| 层级 | 含义 | 公开数据可观测性 |
|------|------|-----------------|
| **Technical / Ledger Settlement** | 交易上链、执行、状态更新、最终确认 | ✅ 高 |
| **Protocol-level Settlement** | 协议内义务了结（如 Repay、epoch settlement） | ✅ 高（若有明确事件） |
| **Economic / Business Settlement** | 这笔钱在商业上代表什么（货款、工资、OTC 等） | ❌ 低；需链下信息 |

### 更严格的链条

```text
Economic Obligation
    ↓
Payment Intent
    ↓
Payment Instruction / Authorization
    ↓
Clearing / Netting（如果存在）
    ↓
Ledger Execution
    ↓
Consensus Finality
    ↓
Settlement Asset Transfer
    ↓
Legal / Economic Discharge
```

### 为什么不在 Paper 1

Settlement 的经济含义识别需要 Paper 2 的框架。Paper 1 只涉及 protocol-level settlement（如 Repay 完成债务了结），不涉及 economic/business settlement。

### Paper 1 中的处理

- 如果提到 Repay 完成了 "protocol-level settlement"，明确标注层级
- 不声称 "transaction was settled" 而不说明是哪一层

### 不可声称

- "The transaction was settled"（不区分层级）
- "Settlement = liquidation"（结算 = 清算）
- "On-chain execution = final settlement"（链上执行 = 最终结算）——execution ≠ finality

---

## 4. Finality / 共识最终性

### Definition

> 区块链共识层面的不可逆性。在 Ethereum PoS 中，当 2/3 的验证者质押量在两个 checkpoint 之间投票时，区块达到 finalized 状态。

### 技术细节（Ethereum PoS）

```text
Transaction submitted
    ↓
Included in block
    ↓
EVM state transition
    ↓
Attestations
    ↓
Checkpoint (epoch start)
    ↓
Supermajority link (2/3 stake)
    ↓
Justified → Finalized
```

- **Execution ≠ Finality**：交易被执行不等于达到最终性
- 一旦 finalized，回滚需要至少 1/3 的质押 ETH 被罚没

### 为什么不在 Paper 1（但需了解）

Finality 是一个技术层概念，Paper 1 的数据重建依赖 archive node 的最终状态。但 Paper 1 不研究 finality 本身。

### Paper 1 中的处理

- 假设所有分析的交易都已达到 finality
- 在数据可靠性声明中提及 finality

### 不可声称

- "Execution = finality"（执行 = 最终性）
- "Finality = economic settlement"（最终性 = 经济结算）

---

## 5. Default / 信用违约

### Definition

> 借款人无法或不愿偿还债务的信用事件。它是一个 borrower-level 的信用状态结果，关注偿付能力与意愿。

### 为什么不在 Paper 1

DeFi liquidation ≠ traditional credit default。Liquidation 是 mechanical position-risk realization，可能由价格暴跌、杠杆过高、操作延迟等多种原因触发，不等于借款人偿付能力失败。

### Paper 1 中的处理

- **不使用 "default" 一词来替代 liquidation**
- RQ2 的 outcome 改为 "liquidation propensity / position distress"
- 在论文中明确声明 "we do not equate liquidation with credit default"

### 不可声称

- "Liquidation = credit default"（清算 = 信用违约）
- "Improved liquidation prediction = improved credit scoring"（改进清算预测 = 改进信用评分）
- "DeFi position behavior = complete borrower behavior"（DeFi 仓位行为 = 完整借款人行为）

---

## 6. Creditworthiness / 信用能力

### Definition

> 在不完全依赖足额或超额抵押的前提下，基于可验证身份与可观测经济行为，对主体未来偿付可信度作出的判断。

### 为什么不在 Paper 1

Creditworthiness 需要身份 + 行为 + 信用结果，这是 Paper 3 的研究对象。Paper 1 只研究 protocol-observable behavior → position distress。

### Paper 1 中的处理

- 不声称行为过程变量度量的是 creditworthiness
- 不声称改进的 liquidation prediction 等于改进的 credit scoring
- 在 future research 中提及与 creditworthiness 的连接

### 不可声称

- "Behavioral variables measure creditworthiness"（行为变量度量信用能力）
- "This study improves credit assessment"（本研究改进了信用评估）
- "DeFi behavior can replace traditional credit data"（DeFi 行为可以替代传统信用数据）

---

## 边界概念之间的关系图

```text
Transfer
    ↓ (if has payment purpose)
Payment
    ↓ (if obligation is fulfilled)
Settlement
    ├── Technical (ledger execution + finality)
    ├── Protocol-level (e.g., Repay)
    └── Economic/Business (needs off-chain info)

Liquidation
    ≠ Settlement (it's forced deleveraging)
    ≠ Default (it's mechanical position risk)

Collateral
    ≠ Creditworthiness (it's trust substitution)
    ≠ Credit Assessment (but may contain info)

Behavioral Process Variables
    ≠ Creditworthiness itself
    ≠ Credit Score
    → measure position-management process only
```

---

## 相关文献

| 文献 | 标题 | 年份 | 链接 | 与本概念的关系 |
|------|------|------|------|---------------|
| Cong & He | Blockchain Disruption and Smart Contracts | 2019 | https://academic.oup.com/rfs/article/32/5/1754/5427778 | Blockchain 对 contracting / consensus 的经济意义 |
| Budish & Sunderam | Blockchain Technology for Traditional Finance | 2026 | https://doi.org/10.3386/w34959 | Trust 模型分析 |
| Huberman et al. | Monopoly without a Monopolist | 2021 | https://academic.oup.com/restud/article/88/6/3011/6169547 | Payment-system economics |
| Li et al. | SoK: Stablecoins in Retail Payments | 2026 | https://arxiv.org/abs/2601.00196 | Stablecoin 支付 |
| Hautsch et al. | Building trust takes time: limits to arbitrage | 2024 | https://doi.org/10.1093/rof/rfae004 | Settlement latency |
