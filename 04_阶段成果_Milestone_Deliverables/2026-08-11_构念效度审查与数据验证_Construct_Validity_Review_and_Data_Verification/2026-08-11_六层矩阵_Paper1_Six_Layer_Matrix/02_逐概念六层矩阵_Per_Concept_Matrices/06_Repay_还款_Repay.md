# 06. Repay / 还款

**六层矩阵详细文件**  
**相关技术文档**：`03_技术文档/01_Aave_V3.md`  
**相关文献**：`04_文献/03_DeFi_Lending/`

---

## Layer 1 — Definition

> **Repay 是 DeFi 借贷协议中减少债务的链上协议动作。它是一个 protocol-level 的金融操作事件，表示某个账户偿还了部分或全部借款。**

关键区分：

```text
Repay (protocol action) ≠ Repayment Motivation
Repay ≠ Position Closure (可能是部分还款)
Repay ≠ Deleveraging (可能是换仓后再借)
```

---

## Layer 2 — Construct

构念是 **repayment action**——协议级的还款操作。

它**不是**：
- 还款的经济动机（降低风险、换仓、关闭仓位等均可能）
- 借款人的信用表现（repay ≠ creditworthiness signal）
- 一定是由借款人自己发起的

它**是**：
- 一个可从合约事件中高精度识别的协议操作
- 仓位风险变化的一个驱动因素（减少债务 → 提高 HF）
- 借款人主动调整行为的一个重要组成部分

---

## Layer 3 — Measurement

### Aave V3

- **事件**：`Repay(user, reserve, amount, useATokens, onBehalfOf)`
- **关键参数**：
  - `user`：发起还款的地址
  - `onBehalfOf`：被还款的债务承担者（可能与 user 不同——第三方代还）
  - `amount`：还款金额
  - `useATokens`：是否使用 aToken 直接还款
- **部分还款 vs 全部还款**：事件中的 amount 可能小于总债务（部分还款）或等于总债务（全部还款，position closed）

### Compound III

- **事件**：`Supply(asset, amount)` 在 Compound III 中表示还款（归还 base asset USDC）
- **注意**：Compound III 的接口设计与 Aave 相反——"供应 USDC"就是还款

### MakerDAO / Sky

- **事件**：Vault 的 `wipe` 操作（偿还 DAI）

---

## Layer 4 — Observable

| 信息 | 可观测性 | 来源 |
|------|---------|------|
| 还款发生 | ✅ 高 | Repay 事件 |
| 还款金额与资产 | ✅ 高 | 事件参数 |
| 还款时间 | ✅ 高 | 事件 block/timestamp |
| 还款发起者 | ✅ 高 | 交易数据 |
| onBehalfOf（被还款的债务承担者） | ✅ 高 | 事件参数 |
| 是否使用 aToken 还款 | ✅ 高 | 事件参数 |
| 还款资金来源 | ❌ 不可观测 | — |
| 还款动机 | ❌ 不可观测 | — |

---

## Layer 5 — Identification

### 识别挑战

1. **第三方代还**：`msg.sender` 可能不是债务承担者，而是第三方（如 credit delegate、自动化合约）
2. **自动化还款**：可能由 keeper bot 或自动化服务触发，不是借款人主动决策
3. **部分 vs 全部**：需要判断还款后债务是否归零（position closure）还是仍有剩余
4. **aToken 还款**：使用 aToken 直接还款的路径与普通还款不同

### 混淆因素

- 还款可能只是换仓的一部分（先还款再以不同资产重新借款）
- 还款可能由 liquidation 触发（第三方偿还债务并获取抵押品）——这是 liquidation，不是 borrower-initiated repay

---

## Layer 6 — Allowed Claim

### 可以声称

- "Repayment action"（还款操作）
- "The borrower reduced their debt by X at time T"（借款人在时间 T 减少了 X 的债务）
- "Protocol-level repayment event"（协议级还款事件）
- "Borrower-authorized repayment"（如果确认发起者是 borrower-authorized entity）

### 不可以声称

- "Repayment motive"（还款动机）
- "The borrower repaid because they wanted to reduce risk"（借款人因为想降低风险而还款）
- "Repay = credit performance"（还款 = 信用表现）——在超额抵押 DeFi 中，还款可能是换仓策略的一部分
- "The borrower repaid voluntarily"（借款人自愿还款）——可能是自动化或被迫
