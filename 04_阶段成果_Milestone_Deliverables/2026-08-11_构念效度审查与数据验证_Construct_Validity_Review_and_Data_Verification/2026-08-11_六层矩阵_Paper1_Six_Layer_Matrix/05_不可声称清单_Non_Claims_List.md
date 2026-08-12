# 05. 不可声称清单 / Non-Claims List

**日期**：2026-08-11  
**用途**：明确 Paper 1 中**不可以**做出的声称，防止 over-claiming  
**原则**：每条不可声称都对应一个 construct validity 问题

---

## 总则

> Paper 1 研究的是 **protocol-observable position management behavior → liquidation propensity**。数据只能支持这一范围内的声称。超出此范围的声称需要额外的研究设计（Paper 2 / Paper 3）才能支撑。

---

## 一、关于 Collateral 与 Credit 的不可声称

| # | 不可声称 | 原因 | 正确措辞 |
|---|---------|------|---------|
| 1.1 | "Collateral = credit" | Collateral 是 trust substitution，不是 credit relationship | "Collateral-based borrowing" |
| 1.2 | "DeFi 借贷实现了 credit market" | DeFi 借贷是 collateral-based liquidity access，不是传统信用市场 | "collateral-secured lending" |
| 1.3 | "行为过程变量度量了 creditworthiness" | Creditworthiness 需要身份 + 行为 + 信用结果，Paper 1 只有行为 | "position-management behavior" |
| 1.4 | "改进清算预测 = 改进信用评分" | Liquidation ≠ default；清算预测 ≠ 信用评分 | "improved liquidation propensity prediction" |
| 1.5 | "DeFi 行为可以替代传统信用数据" | 需要实证验证替代性，Paper 1 不做此验证 | "provides incremental information beyond collateral" |
| 1.6 | "Collateral is merely a mechanical guarantee" | Collateral 还有 screening/signaling 功能（Ioannidou et al. 2022） | "collateral serves multiple functions including loss protection and information" |

---

## 二、关于 Liquidation 与 Default 的不可声称

| # | 不可声称 | 原因 | 正确措辞 |
|---|---------|------|---------|
| 2.1 | "Liquidation = credit default" | Liquidation 是 mechanical position-risk realization，可能由价格暴跌、杠杆过高、操作延迟触发，不等于偿付能力失败 | "liquidation" 或 "position distress" |
| 2.2 | "被清算的借款人 = high-risk borrower" | 被清算可能是策略性选择或操作延迟，不必然等于 high-risk | "borrowers who experienced liquidation" |
| 2.3 | "Liquidation propensity = default probability" | 两者是不同的构念 | "liquidation propensity" |
| 2.4 | "清算预测准确度提高 = 信用风险管理改善" | 清算预测是 position-level 的，不等于 borrower-level credit risk management | "improved position-level liquidation prediction" |

---

## 三、关于 Borrower Behavior 的不可声称

| # | 不可声称 | 原因 | 正确措辞 |
|---|---------|------|---------|
| 3.1 | "我们完全观测了借款人行为" | 协议事件是可观测的，但借款人的经济目的/意图不可观测 | "we observe protocol events initiated by borrower addresses" |
| 3.2 | "DeFi 仓位行为 = 完整借款人行为" | 借款人可能在多个协议、CEX、链下有活动 | "DeFi protocol-observable behavior" |
| 3.3 | "msg.sender == borrower 等于主动操作" | 忽略 onBehalfOf, Safe wallets, routers, automation, credit delegation | "transactions initiated by the borrower address" (after filtering) |
| 3.4 | "借款人的所有操作都是有意的风险管理" | 部分操作可能是套利、再融资、误操作 | "position management behavior" (without imputing intent) |
| 3.5 | "行为模式反映了借款人的风险偏好" | 风险偏好是 unobserved heterogeneity，不能从单次行为推断 | "behavioral patterns associated with liquidation propensity" |

---

## 四、关于 Prospect Theory 的不可声称

| # | 不可声称 | 原因 | 正确措辞 |
|---|---------|------|---------|
| 4.1 | "Prospect Theory 是本研究的 confirmed theory anchor" | HF=1.0 既是心理参考点也是协议机制不连续点，两者不可分离 | "compelling framing" 或 "competing explanation" |
| 4.2 | "借款人在 HF=1.0 附近的行为变化证明了 loss aversion" | 无法区分心理效应和机械协议约束 | "behavioral discontinuity near the liquidation threshold" |
| 4.3 | "我们识别了 reference-dependent preferences" | 缺乏特殊识别策略来区分两种解释 | "we document a behavioral pattern consistent with reference-point behavior" |

---

## 五、关于 Settlement / Payment 的不可声称

| # | 不可声称 | 原因 | 正确措辞 |
|---|---------|------|---------|
| 5.1 | "Transfer = payment" | 转账是技术操作，支付是经济行为，需要 purpose identification | "on-chain transfer" |
| 5.2 | "Transfer history = economic behavior history" | Transfer 只能说明 token movement，不能说明 economic purpose | "transaction history" |
| 5.3 | "On-chain execution = final settlement" | Execution ≠ finality；finality ≠ economic settlement | "on-chain execution" (with finality caveats) |
| 5.4 | "Settlement = liquidation" | 结算是义务了结；清算是强制去杠杆 | 分别使用 "settlement" 和 "liquidation" |
| 5.5 | "借款资金用途可以识别" | 从公开链上数据无法确定借款资金的经济用途 | "we do not identify the economic use of borrowed funds" |
| 5.6 | "消费者支付行为" / "消费行为" | 没有链下标签无法识别 | 不使用这些术语 |

---

## 六、关于 Supply 与 Collateral 的不可声称

| # | 不可声称 | 原因 | 正确措辞 |
|---|---------|------|---------|
| 6.1 | "Supply = 提供抵押" | Aave 中 supply 和 collateral-enabled 是独立状态 | "supply" 和 "collateral-enabled supply" |
| 6.2 | "所有 supplied assets 都计入 HF" | 只有 collateral-enabled 的资产计入 | "collateral-eligible assets" |
| 6.3 | "追加 supply = 风险减轻" | 只有 collateral-enabled 的 supply 才减轻风险 | "collateral-increasing supply" |
| 6.4 | "Withdraw = 风险增加" | 只有 collateral-enabled 的 withdraw 才增加风险 | "collateral-decreasing withdraw" |

---

## 七、关于 Health Factor 的不可声称

| # | 不可声称 | 原因 | 正确措辞 |
|---|---------|------|---------|
| 7.1 | "HF 使用 LTV 作为参数" | HF 使用 Liquidation Threshold (LT)，不是 LTV | "liquidation threshold" |
| 7.2 | "Aave HF = Compound Account Liquidity = Maker Collateralization Ratio" | 三个协议的风险指标定义不同，不能直接比较 | 分别使用各自术语 |
| 7.3 | "HF 是连续的 risk measure" | HF 在清算边界有不连续性（清算罚金等） | "HF with discontinuity at the liquidation boundary" |
| 7.4 | "我们使用了协议当时的真实 HF" | 除非从 archive node + Chainlink 历史价格重建 | "reconstructed HF using historical parameters and prices" |

---

## 八、关于 Liquidation Eligibility vs Realized Liquidation 的不可声称

| # | 不可声称 | 原因 | 正确措辞 |
|---|---------|------|---------|
| 8.1 | "Realized liquidation = 所有可被清算的仓位" | Realized liquidation 受 liquidator-side 执行摩擦影响（gas, MEV, competition） | "realized liquidation" (with execution friction caveat) |
| 8.2 | "所有 HF<1 的仓位都会被清算" | 清算取决于 liquidator 的执行意愿和能力 | "HF<1 indicates liquidation eligibility, not guaranteed liquidation" |
| 8.3 | "Liquidation eligibility = realized liquidation" | 两者是不同的 outcome variable | 分别使用 "eligibility" 和 "realized liquidation" |

---

## 九、关于数据与外部有效性的不可声称

| # | 不可声称 | 原因 | 正确措辞 |
|---|---------|------|---------|
| 9.1 | "Aave 的结果适用于所有 DeFi 借贷协议" | 不同协议机制不同 | "in the context of Aave V3 on Ethereum mainnet" |
| 9.2 | "链上数据是 complete and error-free" | 数据可能受 MEV、reorg、decode error 影响 | "to the best of our knowledge" / "based on decoded event data" |
| 9.3 | "结果适用于传统金融市场" | DeFi 与传统金融机制不同 | limit to DeFi context |
| 9.4 | "结果适用于所有链" | 不同链的机制、用户群体、MEV 环境不同 | "on Ethereum mainnet" |

---

## 使用方法

### 在写作时的检查流程

```text
1. 写出一句话声称
    ↓
2. 检查：这句话是否在本清单中？
    ↓ Yes → 修改措辞
3. 检查：这句话的数据支撑来自哪个 layer？
    ↓
4. 检查：Observable 层的数据能否支持 Allowed Claim 层的声称？
    ↓ No → 降级声称或删除
5. 确认通过 → 保留
```

### 在 Reviewer 回应时的使用

- 如果 reviewer 要求超出 Paper 1 范围的声称，引用本清单说明为什么不做
- 在 Limitations 部分引用本清单中的条目
- 在 Future Research 部分连接到 Paper 2 / Paper 3