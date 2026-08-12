# 07. Supply vs Collateral-Enabled / 供给与抵押启用

**六层矩阵详细文件**  
**相关技术文档**：`03_技术文档/01_Aave_V3.md`  
**相关文献**：`04_文献/03_DeFi_Lending/`

---

## Layer 1 — Definition

> **Supply 是将资产存入协议的动作。Collateral-Enabled 是该资产被标记为可用于支撑借款的状态。在 Aave V3 中，这两个是独立的操作和状态：Supply 不自动等于 Collateral-Enabled。**

关键区分（三层）：

```text
Supply / Deposit                    ← 资产存入协议
≠
Collateral-enabled Supply           ← 该资产被启用为抵押
≠
Risk-reducing collateral addition   ← 增加了实际可支撑债务的缓冲
```

### 7 月 Report 中的问题

原 Report 将 `Deposit` / `Withdraw` 直接等同于 "collateral provision and removal"：

> "Deposit and Withdraw events, representing the provision and removal of collateral"

这在 Aave 中**不准确**。Supply 后资产未必被启用为 collateral。只有在资产被启用为 collateral 且增加了可支撑债务的缓冲时，才应计入"风险减轻的追加抵押"。

---

## Layer 2 — Construct

构念是 **collateral state transition**——仓位抵押状态的实际变化，不是简单的资产存入。

它**不是**：
- 所有 Supply 事件（可能只是 earn interest，不是提供抵押）
- 所有 Withdraw 事件（可能只是提取非抵押资产）

它**是**：
- 对仓位实际风险缓冲有影响的操作
- 需要结合 collateral-enabled 状态判断

---

## Layer 3 — Measurement

### Aave V3

| 事件/状态 | 含义 | 对 HF 的影响 |
|-----------|------|-------------|
| `Supply` | 资产存入协议 | 无直接影响（除非已启用为 collateral） |
| `Withdraw` | 资产从协议提取 | 无直接影响（除非该资产是 collateral） |
| `SetUserUseReserveAsCollateral` | 启用/禁用某资产为 collateral | 直接影响：改变 HF 计算中的分子 |
| Supply + 已启用 collateral | 存入并作为抵押 | 增加风险缓冲 |
| Supply + 未启用 collateral | 存入但不作为抵押 | 不增加风险缓冲 |
| Withdraw + 该资产是 collateral | 提取抵押资产 | 减少风险缓冲 |
| Withdraw + 该资产不是 collateral | 提取非抵押资产 | 不影响风险缓冲 |

### 正确的风险减轻/增加判定逻辑

```text
风险减轻的追加抵押 =
    Supply 事件
    AND
    该资产在操作后处于 collateral-enabled 状态
    AND
    该操作增加了 HF 计算中的分子

风险增加的抵押提取 =
    Withdraw 事件
    AND
    该资产在操作前处于 collateral-enabled 状态
    AND
    该操作减少了 HF 计算中的分子
```

### Compound III

- Compound III 中所有 supplied asset 自动作为 collateral，无需单独 enable
- 因此 Supply = Collateral addition（在 Compound III 中成立）

### MakerDAO / Sky

- Vault 的 `lock` 操作直接增加 collateral
- 没有"存入但不作为抵押"的概念

---

## Layer 4 — Observable

| 信息 | 可观测性 | 来源 |
|------|---------|------|
| Supply 事件 | ✅ 高 | 合约事件 |
| Withdraw 事件 | ✅ 高 | 合约事件 |
| Collateral-enabled 状态变更 | ✅ 高 | `SetUserUseReserveAsCollateral` 事件 |
| 操作前后的 collateral-enabled 状态 | ✅ 高 | 重建仓位状态历史 |
| 操作对 HF 的实际影响 | ✅ 高 | 可计算 |
| 用户为什么 supply 但不启用为 collateral | ❌ 不可观测 | — |

---

## Layer 5 — Identification

### 识别挑战

1. **Aave 与 Compound/Maker 的差异**：Aave 需要额外步骤区分 Supply 和 Collateral-enabled，而 Compound III 和 Maker 不需要
2. **Supply 但未启用 collateral 的比例**：需要统计有多少 Supply 实际上不作为抵押（可能用于 earn interest）
3. **EMode / Isolation 下的特殊规则**：不同模式下 collateral 启用规则不同
4. **批量操作**：一个交易可能包含 Supply + Enable + Borrow 等多个操作

### 处理策略

- 对 Aave 数据，必须跟踪每个资产的 collateral-enabled 状态历史
- 对 Compound III 数据，可以直接将 Supply 视为 collateral addition
- 跨协议比较时，需要明确说明这一差异

---

## Layer 6 — Allowed Claim

### 可以声称

- "Collateral-enabled supply"（已启用为抵押的供给）
- "Risk-reducing collateral addition"（风险减轻的追加抵押，需满足上述条件）
- "In Aave, supply does not automatically equal collateral provision"（在 Aave 中供给不自动等于抵押提供）

### 不可以声称

- "Supply = collateral addition"（在 Aave 中不成立）
- "All deposits are collateral"（所有存入都是抵押）
- "Deposit = risk-reducing action"（存入 = 风险减轻操作）——需要确认 collateral-enabled 状态
