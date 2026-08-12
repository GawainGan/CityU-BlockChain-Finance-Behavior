# 05. Borrow / 借款

**六层矩阵详细文件**  
**相关技术文档**：`03_技术文档/01_Aave_V3.md`  
**相关文献**：`04_文献/03_DeFi_Lending/`

---

## Layer 1 — Definition

> **Borrow 是 DeFi 借贷协议中创建债务的链上协议动作。它是一个 protocol-level 的金融操作事件，表示某个账户在协议中发起了借款，生成了新的债务。**

关键区分：

```text
Borrow (protocol action) ≠ Borrowing Motivation (economic purpose)
Borrow ≠ Leverage (可能用于杠杆，也可能用于流动性需求)
```

---

## Layer 2 — Construct

构念是 **borrowing action**——协议级的借款操作。

它**不是**：
- 借款的经济动机（杠杆、流动性、套利、消费等均可能）
- 借款人的整体杠杆变化（可能在其他协议同时还款）
- 一个信用事件

它**是**：
- 一个可从合约事件中高精度识别的协议操作
- 仓位风险变化的一个驱动因素（增加债务 → 降低 HF）

---

## Layer 3 — Measurement

### Aave V3

- **事件**：`Borrow(user, reserve, amount, interestRateMode, borrowRateMode, onBehalfOf)`
- **关键参数**：
  - `user`：发起交易的地址（msg.sender / initiator）
  - `onBehalfOf`：实际债务承担者（可能与 user 不同）
  - `amount`：借款金额
  - `interestRateMode`：Stable 或 Variable
  - `reserve`：借款资产
- **债务记录**：ScaledBalance + Reserve Index 机制，实际债务 = ScaledBalance × Index

### Compound III

- **事件**：`Withdraw(asset, amount)` 在 Compound III 中表示借款（因为 base asset 是 USDC，"提取 USDC"就是借款）
- **关键区别**：Compound III 的接口设计与 Aave 不同——只有一个 base asset 可借
- **Collateral Factor**：`borrowCollateralFactor` 决定借款能力

### MakerDAO / Sky

- **事件**：Vault 的 `draw` 操作（生成 DAI）
- **区别**：Maker 中借款生成 DAI，是 vault-level 的操作

---

## Layer 4 — Observable

| 信息 | 可观测性 | 来源 |
|------|---------|------|
| 借款发生 | ✅ 高 | Borrow 事件 |
| 借款金额与资产 | ✅ 高 | 事件参数 |
| 借款时间 | ✅ 高 | 事件 block/timestamp |
| 利率模式 | ✅ 高 | 事件参数 |
| onBehalfOf（实际债务承担者） | ✅ 高 | 事件参数 |
| 借款发起者 (msg.sender) | ✅ 高 | 交易数据 |
| 借款动机 | ❌ 不可观测 | — |
| 借款资金用途 | ❌ 不可观测 | — |

---

## Layer 5 — Identification

### 识别挑战

1. **onBehalfOf**：Aave 支持 credit delegation，`msg.sender` 可能不是债务承担者
2. **Router / Gateway**：借款可能通过 router 合约发起，需要解析中间合约
3. **FlashLoan**：FlashLoan 也是一种 "borrow"，但性质完全不同——在同一交易内偿还
4. **利率模式转换**：借款人可能在 stable 和 variable 之间切换

### 混淆因素

- 同一笔借款可能涉及多个合约调用（例如先 borrow 再 swap）
- 借款后资金可能立即转出协议，链上无法追踪完整用途

---

## Layer 6 — Allowed Claim

### 可以声称

- "Borrowing action"（借款操作）
- "The borrower increased their debt by X in asset Y at time T"（借款人在时间 T 以资产 Y 增加了 X 的债务）
- "Protocol-level borrowing event"（协议级借款事件）

### 不可以声称

- "Borrowing motivation"（借款动机）
- "The borrower used the funds for leverage/liquidity/consumption"（借款资金用途）
- "Borrow = increased borrower risk"（借款 = 借款人风险增加）——可能同时在其他协议减少杠杆
