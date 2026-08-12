# 导师汇报：定义、数据、范围的纠错与更新进度

**日期**：2026-08-11  
**性质**：阶段性纠错汇报（Correction & Scope Update），不是新版正式 Research Report  
**基线文档**：`2026-07-17_Research_Report`  
**触发事件**：2026-08-09 与业内人士就区块链支付/结算/质押信贷/KYC 的落地可行性沟通，以及会后的定义与交叉审阅整理

---

## 0. 先给结论

这次更新的核心不是推翻 7 月 Report，而是承认并修正其中若干**概念边界不清、表述过强、操作化过粗**的问题。

当前判断可以压缩成四句：

1. **原方向仍然成立**：公开链上 DeFi 借贷中的协议级仓位管理行为，仍然是可复现、可检验的第一篇论文主线。
2. **但原 Report 对“行为 / 信用 / 抵押 / 支付 / 结算”的边界写得不够干净**，导致部分 claim 看起来比实际可观测的内容更强。
3. **Payment / Settlement / KYC-行为信用** 是重要后续问题，但不应硬塞进当前 Paper 1。
4. **真正要纠的，不是“抵押不符合区块链”，而是：超额抵押更像信任替代机制，而不是完整的信用评估机制。**

因此，现阶段对教授展示的进度定位是：

> **纠错中 + 边界收紧中 + 下一阶段路线更清晰。**

---

## 1. 为什么现在要纠错？

7 月 Report 的主问题是：

> 在公开链上借贷市场中，借款人在头寸风险上升时的主动调整行为，是否提供超越常规链上风险指标的增量信息？

这个主问题本身没有被会议推翻。会议暴露的是另一层问题：

| 会议/审阅暴露的问题 | 对原 Report 的影响 |
|---|---|
| Payment 与 Settlement 经常被混谈 | 原 Report 几乎没定义 settlement；若后续扩展时不先拆清，容易再次空洞 |
| “质押/抵押”口语混用 | 容易把 staking、collateral、credit 混成一个词 |
| 公开链上 transfer ≠ 真实经济目的 | 原 Report 对“complete observability of borrower behavior”表述过强 |
| Liquidation ≠ 传统信用违约 | RQ2 把 future liquidation 当作 credit outcome，claim 过强 |
| 支付公司私有数据才有消费语义 | 进一步确认：公开数据适合协议行为，不适合直接做消费信用 |

换言之：

> 原 Report 在 **protocol-recorded action** 这一层是站得住的；  
> 它容易出问题的地方，是把这一层悄悄写成了更强的 **economic behavior / creditworthiness**。

---

## 2. 这次纠错改了什么（四块）

### 2.1 定义：先把四个词拆开

旧口径问题：抵押、支付、结算、清算在口语和草稿中经常互相替代，导致研究问题听起来大，但经验对象不稳。

更新后的最小定义：

| 概念 | 现在严格指什么 | 明确不是什么 |
|---|---|---|
| **Collateral / 抵押** | 为偿付义务提供可执行经济担保而锁定的资产 | 不是 PoS staking；也不等于信用本身 |
| **Payment / 支付** | 产生一笔付款行为或付款义务 | 不等于已经完成最终资金了结 |
| **Settlement / 结算** | 对既有义务做最终确认与履行 | 不等于 liquidation；也不等于商业目的已知 |
| **Liquidation / 清算** | 头寸风险过高时的强制风险处置 | 不等于传统信用违约（default） |

额外区分：

```text
Staking（共识层质押）
≠
Collateralization（金融抵押）
≠
Credit Assessment（信用评估）
```

以及：

```text
Payment ≠ Settlement
Settlement ≠ Liquidation
Liquidation ≠ Credit Default
On-chain Transfer ≠ Economic Purpose
```

详细定义见：[[02_定义纠错卡_抵押_支付_结算_清算]]

### 2.2 范围：把研究拆成三阶段，而不是一篇论文装所有问题

| 阶段 | 研究对象 | 是否进入当前 Paper 1 |
|---|---|---|
| **Paper 1** | 协议可观测的仓位管理行为（Borrow / Repay / Supply / Withdraw / Liquidation） | **是，当前主线** |
| **Paper 2** | Stablecoin transfer 的 Payment vs Settlement 语义识别 | 否，后续 |
| **Paper 3** | 行为信息能否替代一部分抵押要求（behavior-informed credit） | 否，远期 |

当前 Paper 1 的收紧表述：

> 研究 **protocol-observable position-management behavior**，  
> 而不是直接声称研究完整的现实世界经济行为或传统信用能力。

### 2.3 操作化：修正原 Report 中几处硬伤/过粗规则

| 原写法 | 问题 | 更新后 |
|---|---|---|
| HF 公式用 LTV | Aave 实际用 Liquidation Threshold | 改为按协议真实参数重建；跨协议用 Distance-to-Liquidation |
| `msg.sender == borrower` = 主动 | 忽略 onBehalfOf、router、Safe、AA 等 | 改为重建 initiator → intermediate → onBehalfOf → beneficiary，再定义 borrower-authorized action |
| Supply = 追加抵押 | Aave 中 Supply 不一定开启为 collateral | 区分 Supply 与 Collateral-enabled Supply |
| Liquidation 直接当 credit outcome | 更接近仓位风险管理结果 | RQ2 改称 liquidation propensity / position risk-management quality |
| Daily HF 轨迹 | 临界反应可能被日频抹掉 | 底层按 block/tx 重建，分析面板可再聚合到小时/日/月 |

### 2.4 数据边界：明确“能看见什么 / 看不见什么”

| 数据层 | 可观测性 | 当前用途 |
|---|---|---|
| 链上 execution / finality | 高 | 技术结算是否发生 |
| 协议事件（Borrow/Repay/...） | 高 | Paper 1 主数据 |
| 地址实体标签 | 中 | 辅助分类 |
| Payment vs Settlement 推断 | 中低（模型推断） | Paper 2 候选 |
| 真实消费场景 / MCC / 订单 | 低（公开数据基本没有） | 需支付机构数据 |
| KYC 身份 + 违约结果 | 低 | 真正 credit model 的 gold standard |

因此：

- **Dune / RPC**：适合 Paper 1（协议行为）
- **Allium / Nansen 等**：适合 Paper 2（支付/结算语义增强，但仍是 inferred）
- **支付机构私有数据**：才接近“定死人 + 消费场景 + 可能的信用结果”

---

## 3. 对原 Report 最重要的 claim 收缩

### 原表述容易过强之处

1. “complete observability of borrower behavior”
2. 把 RQ2 直接叫 Credit Layer，并以 future liquidation 作为信用结果
3. 隐含把 on-chain action 写成接近完整经济行为
4. 讨论中对“行为可完全观测”的修辞偏强，尽管后文已承认 partial observability

### 更新后的可辩护表述

> 我们具有 **protocol-recorded actions 的高粒度可观测性**，  
> 但不具有 borrower 完整经济行为、真实意图、链下对冲与传统信用能力的完全可观测性。

> Liquidation 衡量的是 **仓位风险处置结果 / 清算倾向**，  
> 不是直接的传统 credit default。

> Overcollateralization 是 **pseudonymous DeFi 中的信任替代机制**，  
> 它很 blockchain-native，但作为信用中介机制可能不完整。

---

## 4. 更新后的总研究主线（给教授的一页版）

```text
Paper 1（当前）
Collateralized DeFi Lending
→ Position Risk Accumulation
→ Borrower Active Adjustment
→ Liquidation Propensity
目标：协议级行为过程是否携带额外风险信息

Paper 2（后续）
Stablecoin Transfer
→ Payment vs Settlement Classification
→ Inferred Economic Behavior
目标：公开转账能否恢复出有经济含义的行为信号

Paper 3（远期）
Position Behavior
+ Payment/Settlement Behavior
+ Identity / Reputation
→ Credit Signal
→ Reduced Collateral Requirement?
目标：可观测经济行为能否替代一部分抵押品的信息与担保功能
```

最终大问题不再写成：

> “区块链金融应不应该取消抵押？”

而写成：

> **随着链上经济行为变得更可观测，我们是否能用行为信息逐步替代一部分抵押品所承担的信息与担保功能？**

---

## 5. 当前不会过度声称的内容

1. 不声称已证明 DeFi 借款人符合前景理论。
2. 不声称 liquidation = 传统违约。
3. 不声称公开链上 transfer 能直接恢复真实消费目的。
4. 不声称当前公开数据已经足够做 KYC-行为信用模型。
5. 不把 Payment/Settlement 强行并入当前 Paper 1。
6. 不把“抵押不符合 blockchain-native”作为主批评；改为“抵押完成了信任替代，但未必完成信用评估”。

---

## 6. 下一步（纠错完成后的动作）

| 优先级 | 动作 | 产出 |
|---|---|---|
| P0 | 把本文件夹中的定义/范围/操作化改写回正式 Report 草稿 | Report v2 修订提纲 |
| P0 | 用 Aave 小样本验证：HF 重建、主动/被动分类、Safe/onBehalfOf 占比 | 可检查的数据样例 |
| P1 | 明确 Paper 1 的 outcome 命名：liquidation propensity，而不是 credit default | RQ2 措辞修订 |
| P1 | 形成一页“不可声称清单”放入导师讨论材料 | 边界卡片 |
| P2 | 单独起草 Paper 2 的 Payment/Settlement identification note | 后续方向备忘 |

---

## 7. 请教授重点反馈的三个问题

1. **Paper 1 是否应继续严格限制在 protocol-observable position management**，把 payment/settlement/credit formation 明确后置？
2. **RQ2 的 outcome 是否接受改为 liquidation propensity / risk-management quality**，而不再直接叫 credit outcome？
3. **长期主问题是否接受改写为**：可观测行为能否替代一部分抵押要求，而不是“证明抵押模式错误”？

---

## 附：本次更新所依据的材料

- `2026-07-17_Research_Report`
- `0.Meeting/2026-08-09 老曹沟通-区块链支付困境沟通`
- `V4-New_Branch/2026-08-09 .../区块链抵押_信用支付_结算_完整学习版.md`
- `V4-New_Branch/2026-08-09 .../区块链金融研究方向交叉审阅_DeFi_Settlement_Collateral_Credit.md`
- `V4-New_Branch/V4_3_导师初读汇报版.md`
