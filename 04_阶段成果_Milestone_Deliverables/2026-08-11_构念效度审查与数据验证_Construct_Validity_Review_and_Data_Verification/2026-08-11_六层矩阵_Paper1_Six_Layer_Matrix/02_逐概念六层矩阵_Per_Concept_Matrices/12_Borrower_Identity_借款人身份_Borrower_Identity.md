# 12. Borrower Identity / 借款人身份

**六层矩阵详细文件**  
**相关文献**：`04_文献/04_Alternative_Data_CreditScoring/`

---

## Layer 1 — Definition

> **Borrower Identity 在 Paper 1 中指与协议交互的钱包地址（EOA 或合约钱包）。它是一个链上操作实体标识，不是自然人身份。**

关键区分：

```text
Borrower Address ≠ Natural Person
Borrower Address ≠ KYC Identity
Cross-protocol same address ≠ Same person (but likely)
Cross-protocol same behavior ≠ Same person
```

---

## Layer 2 — Construct

构念是 **on-chain operating entity**——在链上执行操作的实体标识。

它**不是**：
- 自然人身份
- KYC 身份
- 一个可以被传统信用机构验证的主体

它**是**：
- 一个可唯一标识的链上操作地址
- 可能是 EOA、Safe multisig、或通过 Account Abstraction 的智能钱包
- 一个自然人可能拥有多个地址
- 一个地址可能被多个自然人共享（如交易所地址）

---

## Layer 3 — Measurement

### 地址层面的度量

| 度量 | 定义 | 来源 |
|------|------|------|
| Address age | 地址首次在链上活动的天数 | 区块链数据 |
| Total transaction count | 地址在所有协议的总交易数 | 区块链数据 |
| Protocol diversity | 地址交互过的不同协议数量 | 区块链数据 |
| Historical borrowing volume | 地址在所有借贷协议的历史借款总额 | 协议事件 |
| Entity label | 地址是否被标记为已知实体（如交易所、liquidator bot） | 标签库 |

### 实体归属

```text
Address → Entity (via label / heuristic)
    Example:
    0x123... → Binance
    0x456... → Uniswap Router
    0x789... → Unknown EOA
```

### 跨协议同一地址

```text
Same address on Aave + Compound
    → Likely same person/entity
    → But cannot be certain (shared infrastructure)
```

---

## Layer 4 — Observable

| 信息 | 可观测性 | 来源 |
|------|---------|------|
| 地址本身 | ✅ 高 | 区块链数据 |
| 地址的交易历史 | ✅ 高 | 区块链数据 |
| 地址的协议交互 | ✅ 高 | 协议事件 |
| 地址的实体标签 | ⚠️ 中 | 标签库 / 启发式 |
| 地址是否是合约 | ✅ 高 | 区块链数据 |
| 地址是否是 Safe | ✅ 高 | Safe 合约 |
| 自然人身份 | ❌ 不可观测 | 需 KYC 数据 |
| 一个地址背后的实际控制人 | ❌ 不可观测 | — |
| 多个地址是否属于同一人 | ❌ 不可观测 | 需链下信息（除非有明确资金流关联） |

---

## Layer 5 — Identification

### 识别挑战

1. **地址 ≠ 自然人**：一个自然人可能使用多个地址，一个地址可能被多人共享
2. **Entity ≠ Purpose**：知道地址属于某实体（如 Binance）不等于知道交易的经济目的
3. **Privacy mixers**：地址可能通过 mixer 或 bridge 混淆资金流
4. **Smart contracts as borrowers**：某些"借款人"实际上是智能合约（如杠杆策略合约），不是自然人决策者
5. **地址聚类**：启发式聚类可能错误地将不同人的地址归为同一实体

### 对 Paper 1 的影响

- 不声称跨协议相似行为 = 同一自然人
- 不声称 borrower address = natural person
- 报告地址聚类的不确定性
- 将合约地址（如策略合约）单独标记

---

## Layer 6 — Allowed Claim

### 可以声称

- "Address-level behavior"（地址级行为）
- "Entity-labeled address"（有实体标签的地址）
- "The address interacted with X protocols"（该地址与 X 个协议交互过）
- "Cross-protocol behavior similarity may suggest but does not prove same entity"（跨协议行为相似可能暗示但不证明同一实体）

### 不可以声称

- "Borrower address = natural person"（借款人地址 = 自然人）
- "Cross-protocol same behavior = same person"（跨协议相同行为 = 同一人）
- "Address-level credit score = personal credit score"（地址级信用评分 = 个人信用评分）
- "The borrower's identity is known"（借款人身份已知）——除非有 KYC 数据
