# 区块链支付/借贷研究：边界、约束与定义的文献核对与研究修订

**日期：2026-08-11**  
**用途：基于 2026-08-11 定义、范围、操作化纠错材料，对当前区块链金融研究方向进行进一步的技术与金融定义核对，并形成后续 Report v2 / Paper 1–3 的研究边界。**

---

## 0. 总体判断

这次对 7 月 Research Report 的纠错方向总体是正确的。

尤其是以下几条边界，应当保留并进一步强化：

```text
Protocol Action ≠ Economic Purpose
Liquidation ≠ Credit Default
Collateral ≠ Creditworthiness
On-chain Transfer ≠ Observed Payment Purpose
Payment ≠ Settlement
Settlement ≠ Liquidation
```

当前 Paper 1 收缩为：

> **protocol-observable position management → subsequent liquidation propensity / position distress**

是比原先“链上行为 → 信用”更可辩护的研究对象。

但在现有纠错版本基础上，仍建议进一步修正五个问题：

1. Collateral 的金融学定义仍然略显绝对；
2. Liquidation 与 Default 应进一步进入两套不同理论框架；
3. Settlement 需要加入 finality / legal discharge 维度；
4. Payment identification 必须明确区分 observation 与 inference；
5. “行为替代抵押”需要改成逐层递进的 claim ladder，而不是直接从行为预测跳到 collateral reduction。

---

# 1. Collateral：不能简单定义成“不是信用评估”

当前版本中的核心表述是：

> Collateralization is a trust-substitution mechanism, not by itself a credit-assessment mechanism.

作为 DeFi 直觉，这个方向基本正确：

在 permissionless / pseudonymous DeFi lending 中，协议通常不能像银行一样依赖传统 KYC、收入、雇佣状态、资产负债表和征信报告进行 underwriting，因此 collateral 提供了一个可以由智能合约自动执行的风险缓冲机制。

但是，从传统金融理论来看：

> **Collateral 并不仅仅是 loss protection。**

传统 collateral literature 通常同时讨论以下作用：

- loss mitigation；
- borrower incentive；
- moral hazard control；
- screening；
- signaling；
- asymmetric information；
- borrower–lender relationship；
- credit allocation。

因此：

```text
Collateral ≠ Credit Score
```

是合理的；

但是：

```text
Collateral contains no credit information
```

则不成立。

更稳妥的论文定义建议改为：

> **In permissionless DeFi lending, collateral primarily provides an enforceable loss-absorption and incentive mechanism that enables lending without conventional identity-based underwriting. It should not be equated with borrower creditworthiness, although collateral choice and collateralization levels may themselves contain information about borrower type and risk.**

中文可以写成：

> 在无需许可的 DeFi 借贷中，抵押品首先提供一种可由协议强制执行的损失吸收和激励机制，使借贷能够在缺乏传统身份式信用审核的条件下发生。抵押本身不等于借款人的信用能力，但抵押选择、抵押比例和抵押行为仍可能包含有关借款人类型与风险的信息。

这个修改非常重要。

因为 Paper 3 真正的问题不应该是：

> collateral 有没有信用功能？

而应该变成：

> **在 collateral 已经承担 enforcement、loss absorption 和 incentive 功能的情况下，额外的行为信息能否承担部分 information / screening 功能，从而改变最优 collateral requirement？**

这样才能真正连接传统金融理论。

---

# 2. Liquidation 与 Credit Default：需要彻底分开

当前纠错中：

```text
Liquidation ≠ Credit Default
```

这个判断应当作为硬边界保留。

## 2.1 Traditional Credit Default

传统银行或信用风险模型中的 default，更接近：

```text
Borrower repayment capacity / willingness
        ↓
Failure or inability to meet obligation
        ↓
Credit default
```

它关注的是：

- 是否无法偿付；
- 是否不愿偿付；
- 是否逾期；
- 是否满足监管或合同中的 default definition。

因此，它是一个 **borrower credit state / repayment outcome**。

## 2.2 DeFi Liquidation

Aave、Compound 等抵押型 DeFi 中的 liquidation 更接近：

```text
Collateral value / debt
        ↓
Position approaches protocol threshold
        ↓
Liquidation eligibility
        ↓
Third-party / protocol liquidation
        ↓
Collateral seizure + debt reduction
```

因此：

> liquidation 是一种 **mechanical position-risk realization / forced deleveraging mechanism**。

它可能由很多原因触发：

- collateral price crash；
- leverage 太高；
- borrower 未及时补仓；
- gas friction；
- oracle update；
- network congestion；
- liquidator competition；
- borrower 主动放弃救仓。

这些原因并不等价于：

> borrower lacks repayment capacity。

所以 Paper 1 的 outcome 最好不要叫：

```text
Credit Default
Creditworthiness
Credit Failure
```

更稳妥的是：

```text
Liquidation Propensity
Position Distress
Liquidation Eligibility
Realized Liquidation
Forced Deleveraging
```

---

# 3. 建议进一步区分：Liquidation Eligibility vs Realized Liquidation

这是 Paper 1 很重要的一步。

现在如果直接用：

```text
Y = whether liquidation occurred
```

会混入 liquidator-side friction。

更干净的设计是：

```text
Borrower behavior
      ↓
Position state deterioration
      ↓
Liquidation eligibility
      ↓
Execution frictions
      ↓
Realized liquidation
```

因此可以考虑两个 outcome：

### Outcome A：Liquidation Eligibility

例如：

```text
HF < 1
```

或者对应 Compound / Maker 的原生风险条件。

这个 outcome 更接近：

> borrower position entered a mechanically liquidatable state。

### Outcome B：Realized Liquidation

实际是否发生：

```text
Liquidation event = 1
```

这个 outcome 除 borrower state 外，还受到：

- liquidator profitability；
- gas；
- MEV；
- liquidity；
- network congestion；
- oracle timing；
- liquidation architecture

影响。

因此，可以形成两个层次：

```text
Behavior → Liquidation Eligibility
```

和：

```text
Behavior + Execution Environment → Realized Liquidation
```

这可能比简单预测 future liquidation 更有 identification 价值。

---

# 4. Payment / Clearing / Settlement：现有三层定义还需要 finality

当前纠错已经将 settlement 拆成：

- technical / ledger settlement；
- protocol-level settlement；
- economic / business settlement。

这个方向正确，但还可以进一步细化。

传统 payment system 通常至少区分：

```text
Payment obligation
      ↓
Payment instruction / authorization
      ↓
Clearing
      ↓
Settlement
```

而区块链又增加一个非常重要的概念：

```text
Consensus Finality
```

因此，一个更严格的链条是：

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

这些概念不能混在一起。

---

# 5. 为什么“交易上链”不能直接叫最终 settlement

对于 Ethereum 等区块链：

```text
Transaction submitted
      ↓
Included in block
      ↓
EVM state transition
      ↓
Confirmations
      ↓
Finality
```

因此：

> execution ≠ finality。

所以将来写 Paper 2 时：

如果只是观察到 transaction 被执行，建议写：

> **the transaction was executed and recorded on-chain**

如果确认已经达到共识 finality，才可以写：

> **the transaction reached protocol consensus finality**

如果讨论现实世界债权债务关系是否已经消灭，则进入：

> **legal / economic settlement**

这三个层面不能用一个 settlement 全部概括。

---

# 6. Payment ≠ Transfer：必须明确 Observation 与 Inference

这是 Paper 2 最重要的方法论边界之一。

链上真正直接观测到的是：

```text
Address A
    ↓
Token transfer
    ↓
Address B
```

这意味着：

> token ownership / balance state 发生变化。

但是它本身并没有告诉研究者：

```text
Why?
```

例如同一个 stablecoin transfer 可能是：

- merchant payment；
- payroll；
- exchange deposit；
- exchange withdrawal；
- bridge；
- treasury transfer；
- OTC settlement；
- loan repayment；
- collateral movement；
- internal wallet transfer；
- remittance；
- arbitrage；
- market-making；
- custody movement。

所以链上数据的正确识别链条应该写成：

```text
Observed Transfer
      ↓
Entity Attribution
      ↓
Transaction-Type Classification
      ↓
Economic-Purpose Inference
```

而不是：

```text
Observed Transfer
      ↓
Observed Economic Purpose
```

因此 Paper 2 的关键词应优先使用：

```text
inferred payment
payment-like transaction
transaction-purpose classification
economic-function identification
```

而不是直接写：

```text
consumer payment
consumption behavior
merchant purchase
```

除非已经拥有真实链下标签。

---

# 7. Allium / Visa / Nansen 等数据的正确研究定位

这些平台非常有价值，但用途要分清。

## Allium

更适合：

- stablecoin transfer enrichment；
- entity labels；
- payment candidate filtering；
- transaction taxonomy；
- cross-chain standardized data。

但是：

> enriched payment classification ≠ ground-truth economic purpose。

它通常仍然依赖：

- label；
- heuristics；
- filtering；
- transaction-pattern inference。

因此更适合作为：

```text
Candidate Payment Dataset
or
Weak / Silver Label
```

而不是：

```text
Ground Truth
```

## Visa Onchain Analytics

适合：

- stablecoin payment / transfer macro trends；
- industry benchmark；
- heuristic classification comparison。

但同样不应该直接等同真实 consumer transaction labels。

## Nansen / Chainalysis / Entity-label providers

更适合：

```text
Address → Entity
```

例如：

```text
0x123... → Binance
0x456... → Uniswap Router
```

但是：

```text
Entity ≠ Purpose
```

知道对手方是谁仍然不一定知道：

> 为什么这笔钱发生。

---

# 8. 真正的 Payment / Consumer Behavior Ground Truth 需要什么？

如果 Paper 2 / Paper 3 最终要进入真实消费行为，需要尽量获得：

```text
Wallet / User ID
+
Merchant
+
Order
+
MCC / Merchant Category
+
Timestamp
+
Amount
+
Refund / Chargeback
+
Invoice / Payment purpose
```

如果进一步进入 credit：

```text
KYC Identity
+
Income / employment（如果可得）
+
Payment history
+
Repayment history
+
Credit limit
+
Delinquency
+
Default
```

因此：

> Public blockchain data 很适合研究 transaction / protocol behavior；

但：

> consumer credit research 的 gold standard 通常仍需要 private payment / lending data。

---

# 9. “行为替代抵押”不能直接成立，需要 Claim Ladder

长期命题值得保留：

> observable behavior 是否可以逐渐替代一部分 collateral？

但是这个问题不能从：

```text
Behavior predicts liquidation
```

直接跳到：

```text
Therefore collateral can be reduced
```

中间至少需要五个层次。

建议写成：

```text
Observable Behavior
        ↓
Incremental Risk Information
        ↓
Out-of-Sample Predictive Value
        ↓
Decision / Economic Value
        ↓
Collateral Requirement Counterfactual
```

分别对应：

## Level 1 — Information

行为变量是否包含静态 collateral state 之外的信息？

例如：

```text
State-only model
vs
State + behavior model
```

## Level 2 — Prediction

是否真正改善：

- AUC；
- calibration；
- log loss；
- Brier score；
- out-of-sample prediction。

## Level 3 — Stability

这种预测能力是否：

- 跨市场；
- 跨周期；
- 跨协议；
- 牛熊市；
- 不同 collateral assets

仍然存在？

## Level 4 — Economic Decision Value

预测改善是否足够大，能够改善：

- risk pricing；
- credit limit；
- early warning；
- liquidation risk management；
- capital allocation。

## Level 5 — Collateral Counterfactual

最后才能问：

> 在保持相同 expected loss / risk tolerance 的情况下，加入行为信息以后，是否可以降低 collateral requirement？

这才是真正的：

```text
Behavior → Partial Collateral Substitution
```

---

# 10. Paper 1 的推荐研究边界

当前 Paper 1 可以进一步压缩为：

> **Can protocol-observable position-management behavior provide incremental information about subsequent position distress and liquidation beyond contemporaneous collateral states?**

研究对象：

```text
Collateralized DeFi Lending
      ↓
Position Risk Accumulation
      ↓
Borrower Adjustment
      ↓
Liquidation Eligibility
      ↓
Realized Liquidation
```

重点是：

> **risk information**

不是：

> creditworthiness。

---

# 11. Paper 1 不应该声称的内容

当前论文最好明确不声称：

```text
Liquidation = traditional default
```

不声称：

```text
DeFi position behavior = complete borrower behavior
```

不声称：

```text
Borrower address = natural person
```

不声称：

```text
Protocol interaction = economic purpose
```

不声称：

```text
Improved liquidation prediction = improved credit scoring
```

也不声称：

```text
Behavior predicts liquidation
→ therefore collateral can be reduced
```

---

# 12. Paper 2 的推荐研究问题

Paper 2 可以逐渐形成一个非常独立的问题：

> **To what extent can the economic function of stablecoin transfers—payment, financial settlement, exchange-related transfer, treasury movement, etc.—be identified from public blockchain data?**

研究结构：

```text
Raw Stablecoin Transfer
       ↓
Entity Attribution
       ↓
Transaction Graph / Context
       ↓
Classification
       ↓
Economic Function
       ↓
Ground-truth Validation（如果可以获得）
```

这样 Paper 2 本身可能就是：

> **identification / measurement paper**

而不是急于把它包装成消费信用。

---

# 13. Paper 3 的推荐研究问题

Paper 3 才进入：

```text
Identity
+
Position behavior
+
Economically meaningful payment behavior
+
Repayment history
        ↓
Credit Risk Signal
        ↓
Lending Decision
        ↓
Collateral Requirement
```

推荐问题：

> **Conditional on verified identity and economically meaningful transaction histories, does behavioral information improve repayment-risk assessment, and can that informational improvement support economically meaningful reductions in collateral requirements?**

这里才是真正的：

```text
credit formation
+
collateral substitution
```

---

# 14. 三篇论文之间的递进关系

建议以后整个 PhD project 都用下面这一条主线：

```text
Paper 1
Protocol-observable behavior
        ↓
Risk information

Paper 2
On-chain transfer
        ↓
Economic-function identification

Paper 3
Verified economic behavior
        ↓
Credit information
        ↓
Collateral design
```

进一步压缩就是：

```text
Observable Protocol Behavior
        ↓
Identifiable Economic Behavior
        ↓
Credit-Relevant Information
        ↓
Collateral Design
```

而不是：

```text
On-chain History
↓
Behavior
↓
Credit
↓
Less Collateral
```

后一条链条跳跃太多。

---

# 15. 不同协议需要分别定义风险机制

Paper 1 不建议一开始就把 Aave、Compound、Maker 强制统一成同一个 Health Factor。

更准确的方式是：

```text
Protocol Native Risk Metric
        ↓
Liquidation Boundary
        ↓
Protocol-specific Distance to Liquidation
        ↓
Standardized Cross-protocol Measure
```

---

# 16. Aave

Aave 中需要重点区分：

```text
LTV
≠
Liquidation Threshold
```

Health Factor 使用 liquidation threshold，而不是简单 LTV。

另外：

```text
Supply
≠
Collateral-enabled Supply
```

资产 supply 进协议并不意味着一定作为 collateral 使用。

主动行为识别也不能简单使用：

```text
msg.sender == borrower
```

因为需要考虑：

- onBehalfOf；
- router；
- smart wallet；
- Safe；
- account abstraction；
- adapter；
- repay on behalf；
- delegated actions。

因此应尽量建立：

```text
Initiator
↓
Intermediate Contract
↓
onBehalfOf / Beneficiary
↓
Debt Owner
↓
Collateral Owner
↓
State Change
```

然后再定义：

```text
Borrower-authorized Action
```

---

# 17. Compound

Compound III 与 Aave 不能简单认为只是参数不同。

它的机制中需要特别注意：

```text
Borrow Collateral Factor
≠
Liquidation Collateral Factor
```

并且 liquidation architecture 与 Aave 不同。

因此跨协议比较更适合使用：

```text
Distance to Protocol-specific Liquidation Boundary
```

而不是：

```text
Unified HF
```

---

# 18. Maker

Maker/Vault 系统又有自己的：

- collateralization ratio；
- liquidation ratio；
- vault structure；
- auction/liquidation mechanism。

因此 Maker 更适合作为：

> mechanism heterogeneity / external validity

而不是简单拼到 Aave panel 里。

---

# 19. 推荐的数据层级

Paper 1 最可信的数据结构建议是：

```text
Protocol Contract
+
Historical Protocol Parameters
+
Raw / Decoded Blockchain Data
        ↓
Researcher-built Position State
        ↓
Dune / Curated Dataset Validation
```

也就是说：

> Dune 很有价值，但不应该成为最终定义来源。

如果研究问题依赖：

- onBehalfOf；
- collateral enablement；
- historical liquidation threshold；
- contract upgrade；
- delegate call；
- state transitions；

就应该优先从：

```text
contracts + logs + state
```

自己重建。

---

# 20. 建议优先阅读的核心文献

以下分为“理论语言”和“直接竞争文献”两组。

---

## 20.1 Blockchain / Payment / Smart Contract 基础

### Cong, Lin William & He, Zhiguo  
**Blockchain Disruption and Smart Contracts**  
*Review of Financial Studies*, 2019.

作用：

- 定义 blockchain 对 contracting / information / consensus 的经济意义；
- 避免使用模糊的 “blockchain-native” 口号。

链接：

https://academic.oup.com/rfs/article/32/5/1754/5427778

---

### Budish, Eric  
**Trust at Scale**  
*Quarterly Journal of Economics*, 2025.

作用：

- blockchain 并不是消灭 trust；
- trust minimization 本身具有成本和机制约束；
- 可以帮助重新定义“去信任”。

链接：

https://academic.oup.com/qje/article/140/1/1/7824430

---

### Huberman, Gur; Leshno, Jacob; Moallemi, Ciamac  
**Monopoly without a Monopolist: An Economic Analysis of the Bitcoin Payment System**  
*Review of Economic Studies*, 2021.

作用：

- 从 payment-system economics，而不是工程视角理解 blockchain payment；
- network capacity、fees、settlement economics。

链接：

https://academic.oup.com/restud/article/88/6/3011/6169547

---

# 21. Collateral / Credit Literature

### Jiménez, Gabriel; Salas, Vicente; Saurina, Jesús  
**Determinants of Collateral**  
*Journal of Financial Economics*, 2006.

作用：

- collateral 与 borrower risk 的关系；
- collateral 不是简单的 mechanical guarantee；
- collateral selection 内生。

---

### Berger, Allen N.; Frame, W. Scott; Ioannidou, Vasso  
**Tests of Ex Ante versus Ex Post Theories of Collateral**  
*Journal of Financial Economics*, 2011.

作用：

区分：

```text
Ex-ante
Screening / Signaling

vs

Ex-post
Incentive / Moral Hazard
```

对重新定义 collateral 非常关键。

---

### Ioannidou, Vasso; Pavanini, Nicola; Peng, Yucheng  
**Collateral and Asymmetric Information in Lending Markets**  
*Journal of Financial Economics*, 2022.

作用：

- collateral 与 asymmetric information；
- borrower information 与 collateral requirement；
- Paper 3 的重要理论接口。

---

### Catherine et al.  
**Quantifying Reduced-Form Evidence on Collateral Constraints**  
*Journal of Finance*, 2022.

作用：

解释：

> collateral constraint 不是一个纯金融参数，而会真实影响融资与资源配置。

因此未来研究“降低 collateral”必须进入 economic allocation，而不是只谈模型预测。

---

# 22. Alternative Data / Credit Scoring Literature

### Berg, Tobias et al.  
**On the Rise of FinTechs: Credit Scoring Using Digital Footprints**  
*Review of Financial Studies*, 2020.

非常重要。

核心启示不是：

```text
Digital Footprint replaces Credit Bureau
```

而是：

```text
Digital Footprint can provide incremental predictive information
```

尤其值得注意：

> alternative data 可能首先是 complement，而不是 substitute。

这与 Paper 3 的长期逻辑高度一致。

---

### Di Maggio, Marco & Yao, Vincent  
**Fintech Borrowers: Lax Screening or Cream-Skimming?**  
*Review of Financial Studies*, 2021.

作用：

- FinTech underwriting；
- borrower selection；
- default；
- alternative data 并不会自动消除 selection problem。

---

### Chioda, Laura et al.  
**FinTech Lending to Borrowers with No Credit History**  
NBER Working Paper.

作用：

非常接近长期研究问题：

> 如果 borrower 没有传统 credit history，新的行为数据是否能够形成风险信息？

这是未来 Paper 3 很值得深入的文献。

---

# 23. DeFi Lending Literature

### Cornelli et al.  
**Why DeFi Lending? Evidence from Aave V2**  
*Journal of Financial Intermediation*, 2025.

作用：

- Aave transaction-level lending behavior；
- DeFi borrowing motivation；
- Paper 1 需要直接对话。

---

### Makarov & Schoar  
**Cryptocurrencies and Decentralized Finance (DeFi)**  
BIS Working Paper.

作用：

- DeFi architecture；
- anonymous participation；
- overcollateralization；
- liquidation；
- market structure。

---

### Schuler  
**Frictions in DeFi Liquidations: Evidence from the Aave V2 Main Market**  
Working Paper, 2026.

虽然不是顶刊，但对 Paper 1 非常重要。

因为它直接涉及：

- Aave；
- block-level position；
- liquidation；
- execution friction。

因此属于：

> **direct competitor / must-read paper**

即使尚未正式发表，也必须仔细处理。

---

# 24. 文献使用原则

研究中不能只读顶刊。

应该区分：

```text
Top Journal Literature
        ↓
决定理论语言
        ↓
What should this construct mean?

Recent Working Papers
        ↓
决定研究竞争边界
        ↓
What has already been done?
```

例如：

- QJE / JF / JFE / RFS / ReStud：用于定义经济机制；
- SSRN / NBER / BIS / top-school working paper：用于确认当前前沿和直接竞争。

两类缺一不可。

---

# 25. 推荐建立 Definition–Construct–Observable–Identification–Claim 矩阵

下一版 Report 之前，建议先建立如下矩阵。

| Concept | Definition | Construct | Observable | Cannot Identify | Allowed Claim |
|---|---|---|---|---|---|
| Transfer | token/state movement | asset movement | tx/event | purpose | observed transfer |
| Payment | economic payment activity | payment behavior | partial/inferred | exact purpose without labels | inferred payment |
| Settlement | obligation discharge / asset settlement | settlement process | protocol-dependent | legal discharge often unknown | protocol/technical settlement |
| Finality | consensus irreversibility | ledger certainty | consensus state | economic purpose | finalized transaction |
| Borrow | protocol debt creation | leverage / funding | protocol event | why borrowed | borrowing action |
| Repay | debt reduction | debt management | protocol event | repayment motive | repayment action |
| Collateral | pledged enforceable asset | loss buffer/incentive | position state | full borrower creditworthiness | collateralization state |
| Liquidation Eligibility | position crosses threshold | position distress | reconstructed state | borrower insolvency | liquidatable state |
| Liquidation | forced position intervention | forced deleveraging | event | traditional default | realized liquidation |
| Default | failure/unwillingness to repay | credit outcome | generally unavailable publicly | — | 不应由 liquidation 替代 |
| Identity | economic/legal主体 | borrower identity | usually weak | natural person identity | entity/address only |
| Creditworthiness | expected repayment reliability | credit risk | 当前无法直接观测 | complete repayment capacity | 不在 Paper 1 直接声称 |

---

# 26. Paper 1 推荐的 Definition–Measurement Matrix

### Position Risk

定义：

> 协议定义的仓位距离 liquidation boundary 的状态。

观测：

```text
Collateral
Debt
Oracle Price
Protocol Parameters
```

允许声称：

```text
Position Risk
```

不允许直接声称：

```text
Credit Risk
```

---

### Borrower Adjustment

定义：

> 由 borrower 或 borrower-authorized entity 触发、改变该仓位风险状态的协议动作。

可能包括：

- repay；
- collateral addition；
- collateral withdrawal；
- additional borrowing；
- asset switching；
- no action。

允许声称：

```text
Protocol-observable Position-management Behavior
```

不允许声称：

```text
Complete Economic Behavior
```

---

### Liquidation

定义：

> 当仓位符合协议规定条件后，由清算机制进行的强制风险处置。

允许声称：

```text
Forced Deleveraging
Position Distress Realization
Liquidation Propensity
```

不允许：

```text
Traditional Credit Default
```

---

# 27. 目前整个研究项目最值得保留的一句话

长期问题不再是：

> 区块链金融为什么还需要抵押？

而应改成：

> **As economically meaningful borrower behavior becomes more observable and verifiable, can such information perform part of the screening and risk-assessment role currently substituted by collateral in permissionless lending, and under what conditions can this support lower collateral requirements without increasing expected losses?**

中文：

> 随着具有经济意义的借款人行为变得更加可观测、可验证，这些信息能否承担当前 permissionless lending 中由抵押机制替代的一部分筛选与风险评估功能，并在不提高预期损失的条件下支持更低的抵押要求？

这个版本比：

> “行为能不能替代抵押”

更加严谨。

因为它明确区分了：

```text
Collateral 的 Enforcement Function
Collateral 的 Loss-Absorption Function
Collateral 的 Incentive Function
Collateral 的 Information Function
```

行为信息最多可能首先替代的是：

```text
Information / Screening Function
```

而不是全部 collateral function。

---

# 28. 当前最合理的研究推进顺序

建议现阶段优先级为：

```text
P0
Paper 1 Definition–Measurement Matrix

P0
Aave-specific mechanism reconstruction

P0
Liquidation Eligibility vs Realized Liquidation

P1
Borrower-authorized action identification

P1
State-only vs State+Behavior model

P1
Recent Aave liquidation literature comparison

P2
Compound / Maker external validity

P2
Payment / Settlement identification framework

P3
Behavior-informed credit / collateral counterfactual
```

现阶段最大的学术风险已经不是：

> “这个研究方向有没有意思？”

而是：

```text
Construct Validity
+
Protocol-version Heterogeneity
+
Outcome Identification
```

即：

> 你测量的变量到底是不是你声称的概念？

这个问题必须在正式修改 Report v2 之前解决。

---

# 29. 核心结论

这次纠错之后，整个研究主线已经比原版清楚很多。

最重要的变化是：

```text
原来：
On-chain History
→ Behavior
→ Credit
→ Less Collateral

修改后：
Protocol-observable Behavior
→ Incremental Risk Information

On-chain Transfer
→ Economic-purpose Identification

Verified Economic Behavior
→ Credit-Relevant Information
→ Lending Decision
→ Collateral Design
```

因此：

> **Paper 1 做“行为是否包含增量风险信息”；  
> Paper 2 做“链上转账的经济含义能否被识别”；  
> Paper 3 才做“这些行为信息能否进入信用决策并减少部分抵押要求”。**

这三个问题之间存在递进关系，但不能互相替代。

---

# 30. References / Recommended Reading

1. Cong, L. W., & He, Z. (2019). *Blockchain Disruption and Smart Contracts*. Review of Financial Studies.
2. Budish, E. (2025). *Trust at Scale*. Quarterly Journal of Economics.
3. Huberman, G., Leshno, J., & Moallemi, C. (2021). *Monopoly without a Monopolist: An Economic Analysis of the Bitcoin Payment System*. Review of Economic Studies.
4. Jiménez, G., Salas, V., & Saurina, J. (2006). *Determinants of Collateral*. Journal of Financial Economics.
5. Berger, A. N., Frame, W. S., & Ioannidou, V. (2011). *Tests of Ex Ante versus Ex Post Theories of Collateral*. Journal of Financial Economics.
6. Ioannidou, V., Pavanini, N., & Peng, Y. (2022). *Collateral and Asymmetric Information in Lending Markets*. Journal of Financial Economics.
7. Catherine et al. (2022). *Quantifying Reduced-Form Evidence on Collateral Constraints*. Journal of Finance.
8. Berg, T. et al. (2020). *On the Rise of FinTechs: Credit Scoring Using Digital Footprints*. Review of Financial Studies.
9. Di Maggio, M., & Yao, V. (2021). *Fintech Borrowers: Lax Screening or Cream-Skimming?*. Review of Financial Studies.
10. Chioda et al. *FinTech Lending to Borrowers with No Credit History*. NBER Working Paper.
11. Cornelli et al. (2025). *Why DeFi Lending? Evidence from Aave V2*. Journal of Financial Intermediation.
12. Makarov, I., & Schoar, A. *Cryptocurrencies and Decentralized Finance (DeFi)*. BIS Working Paper.
13. Schuler (2026). *Frictions in DeFi Liquidations: Evidence from the Aave V2 Main Market*. Working Paper.
14. BIS / CPMI. *Glossary of Terms Used in Payments and Settlement Systems*.
15. Ethereum Foundation documentation on Proof-of-Stake finality.
16. Aave V3 protocol contracts and documentation.
17. Compound III documentation on collateral and liquidation.
18. Dune documentation on raw / decoded / curated blockchain data.
19. Allium stablecoin payment data documentation.
20. Visa Onchain Analytics methodology documentation.

---

## 对现有 2026-08-11 纠错包的定位

本文件是在以下已有材料基础上的进一步文献核对与研究边界深化：

- `00_README.md`
- `01_导师汇报_纠错与更新进度.md`
- `02_定义纠错卡_抵押_支付_结算_清算.md`
- `03_范围_操作化_数据边界更新.md`
- `04_对2026-07-17_Report纠错对照表.md`
- `05_口头汇报卡_3到5分钟.md`

建议下一步不要直接重写整个 Research Report，而是先基于本文建立 Paper 1 的：

```text
Definition
→ Construct
→ Measurement
→ Observable
→ Identification
→ Allowed Claim
```

六层矩阵，然后再进入 Report v2。
