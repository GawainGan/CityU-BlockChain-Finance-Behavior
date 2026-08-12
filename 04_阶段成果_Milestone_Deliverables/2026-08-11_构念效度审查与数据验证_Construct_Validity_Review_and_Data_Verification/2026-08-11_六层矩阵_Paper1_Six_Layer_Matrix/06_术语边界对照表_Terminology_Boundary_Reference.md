# 06. 术语边界对照表 / Terminology Boundary Cross-Reference

**日期**：2026-08-11  
**用途**：防止术语混用，确保每个概念使用精确的语言  
**原则**：每对术语的边界必须显式声明

---

## 一、核心术语对：≠（不等于）

| 术语 A | ≠ | 术语 B | 区别说明 | 涉及概念文件 |
|--------|---|--------|---------|-------------|
| Collateral | ≠ | Credit | Collateral 是 trust substitution（用资产替代信任）；Credit 是基于身份和行为的 trust extension | 01_Collateral |
| Payment | ≠ | Settlement | Payment 是产生付款行为/义务；Settlement 是对既有义务的最终确认与履行 | 13_Boundary |
| Settlement | ≠ | Liquidation | Settlement 是义务了结（如 Repay 完成债务了结）；Liquidation 是强制去杠杆 | 13_Boundary, 11_Realized_Liquidation |
| Liquidation | ≠ | Default | Liquidation 是 mechanical position-risk realization（HF<1 → 强制平仓）；Default 是 borrower-level 信用违约（偿付能力失败） | 10_Liquidation_Eligibility, 11_Realized_Liquidation |
| Transfer | ≠ | Payment | Transfer 是 token 所有权变化（技术操作）；Payment 是产生付款行为/义务（经济行为） | 13_Boundary |
| Staking | ≠ | Collateralization | Staking 是在 PoS 共识中质押 ETH 保障网络安全；Collateralization 是在借贷协议中锁定资产作为抵押 | 01_Collateral |
| Supply | ≠ | Collateral-Enabled Supply | Supply 是存入资产；Collateral-Enabled Supply 是存入并启用为抵押的资产 | 07_Supply_vs_CollateralEnabled |
| Health Factor (Aave) | ≠ | Account Liquidity (Compound) | HF = Σ(V×LT)/D；Account Liquidity = Σ(V×borrowCF) - D。定义不同，不能直接比较 | 03_Health_Factor |
| Account Liquidity (Compound) | ≠ | Collateralization Ratio (Maker) | Compound 用 borrowCF ≠ liquidateCF；Maker 用单一 Liquidation Ratio | 03_Health_Factor |
| Liquidation Eligibility | ≠ | Realized Liquidation | Eligibility = HF<1（可被清算的状态）；Realized = 实际发生了 LiquidationCall。执行摩擦造成两者分离 | 10_Liquidation_Eligibility, 11_Realized_Liquidation |
| Protocol-Observable Behavior | ≠ | Complete Borrower Behavior | 协议事件可观测；借款人的链下/多协议/CEX 行为不可观测 | 08_Borrower_Adjustment, 12_Borrower_Identity |
| Active Action | ≠ | msg.sender == borrower | Active 需要 human-initiated intentional action；msg.sender 可能是 router, Safe, automation | 09_Active_vs_Passive |
| Position Risk | ≠ | Credit Risk | Position risk 是仓位级别的资产价格波动风险；Credit risk 是借款人级别的偿付能力风险 | 02_Position_Risk |

---

## 二、核心术语对：→（层级/包含关系）

| 上层概念 | → | 下层概念 | 关系说明 |
|---------|---|---------|---------|
| Economic Obligation | → | Payment Intent → Payment Instruction → Ledger Execution → Consensus Finality → Settlement Asset Transfer → Legal/Economic Discharge | Settlement 的完整链条 |
| Transfer | → | (if has payment purpose) Payment | Transfer 是 Payment 的必要条件，非充分条件 |
| Payment | → | (if obligation is fulfilled) Settlement | Payment 是 Settlement 的前提 |
| Settlement | → | Technical / Ledger Settlement + Protocol-level Settlement + Economic / Business Settlement | 三层 Settlement |
| Protocol-Observable Behavior | → | Supply + Withdraw + Borrow + Repay + Collateral Enable/Disable + LiquidationCall | 可观测事件的完整集合 |
| Position Management Behavior | → | Active Adjustments + Passive Events | 借款人行为的两大分类 |
| Active Adjustment | → | Active Repay + Active Supply (collateral) + Active Withdraw (collateral) + Active Borrow | 主动调整的具体类型 |
| Borrower Identity | → | Wallet Address (observable) + Real-world Identity (unobservable in Paper 1) | 身份的两层 |
| Distance to Liquidation | → | 1 - HF (normalized) 或 log(HF) | 度量方式 |

---

## 三、协议间术语映射表

| 概念 | Aave V3 | Compound III | MakerDAO/Sky |
|------|---------|-------------|-------------|
| 仓位 | Position | Account | Vault |
| 风险指标 | Health Factor (HF < 1) | Account Shortfall (> 0) | Collateralization Ratio (< LR) |
| 清算触发参数 | Liquidation Threshold (LT) | liquidateCollateralFactor | Liquidation Ratio |
| 借款能力参数 | LTV | borrowCollateralFactor | — |
| 借款资产 | 多种 | 单一 base asset | DAI/USDS |
| 清算方式 | Liquidator repays + seizes | Protocol absorbs collateral | Auction-based |
| Collateral enable | 手动 enable/disable | 自动（所有 supply 都是 collateral） | lock 操作即 collateral |
| 利率模式 | Variable / Stable | Variable | Stability Fee |
| 存入 | Supply | Supply (base asset = 还款) | lock |
| 提取 | Withdraw | Withdraw (base asset = 借款) | free |
| 借款 | Borrow | Withdraw (base asset) | draw |
| 还款 | Repay | Supply (base asset) | wipe |
| 清算事件 | LiquidationCall | AbsorbCollateral | Liquidation auction |

### 关键警告

> **不可将三个协议的数据直接拼接为一个 panel。** 不同协议的构念定义不同，强行拼接会引入 measurement error。应分别分析，或使用明确标注的标准化指标。

---

## 四、术语使用检查表

### 在写作中遇到以下术语时，必须检查：

| 术语 | 检查项 | 如果不确定 |
|------|--------|-----------|
| "credit" | 是否在讨论 traditional credit relationship？还是 DeFi collateral-based lending？ | 改用 "collateral-secured lending" |
| "default" | 是否在讨论 borrower-level 偿付能力失败？还是 protocol-level liquidation？ | 改用 "liquidation" 或 "position distress" |
| "settlement" | 在哪一层？Technical / Protocol / Economic？ | 标注层级 |
| "payment" | 是否有 payment purpose 的识别？还是只看到 transfer？ | 改用 "transfer" |
| "collateral" | 是否区分了 supply 和 collateral-enabled supply？ | 标注 collateral-enabled |
| "health factor" | 是否使用了 LT 而非 LTV？是否标注了协议来源？ | 使用 "Aave V3 Health Factor" |
| "active" | 是否只检查了 msg.sender？是否检查了 onBehalfOf / router / automation？ | 改用 "initiated by borrower address (after filtering)" |
| "borrower" | 是否区分了 wallet address 和 real-world identity？ | 标注 "borrower address" |
| "risk" | Position risk？Credit risk？Liquidation risk？ | 标注 risk 类型 |
| "liquidation" | Eligibility (HF<1)？Realized (LiquidationCall)？ | 标注 eligibility vs realized |

---

## 五、常用正确措辞替换表

| ❌ 不应使用 | ✅ 应使用 | 原因 |
|-----------|---------|------|
| "credit market" (in DeFi context) | "collateral-secured lending market" | DeFi 借贷是抵押借贷，不是信用借贷 |
| "credit risk" (in DeFi context) | "position risk" 或 "liquidation risk" | DeFi 的风险是仓位风险，不是信用风险 |
| "default" (for DeFi liquidation) | "liquidation" | Liquidation ≠ default |
| "borrower behavior" (without qualifier) | "protocol-observable borrower behavior" | 只观测到协议事件 |
| "the borrower did X" | "the borrower address initiated X" | 地址 ≠ 真实身份 |
| "collateral supply" (without checking) | "supply" + check collateral-enabled status | Supply ≠ collateral-enabled |
| "settled" (without layer) | "executed and finalized on-chain" (Technical) / "protocol obligation discharged" (Protocol) | 标注 settlement 层级 |
| "payment" (for any transfer) | "on-chain transfer" | Transfer ≠ payment |
| "the transaction was settled" | "the transaction was executed and reached consensus finality" | 区分 execution 和 finality |
| "Prospect Theory confirms..." | "behavioral patterns are consistent with reference-point behavior" | PT 是 framing，不是 confirmed anchor |
| "improved credit scoring" | "improved liquidation propensity prediction" | Liquidation prediction ≠ credit scoring |
| "complete borrower behavior" | "protocol-observable borrower behavior" | 不完整观测 |

---

## 六、与六层矩阵的对应

每个术语对都应能追溯到六层矩阵的 Definition → Construct → Measurement → Observable → Identification → Allowed Claim 链条：

```text
Definition (经济理论定义)
    ↓
Construct (研究构念)
    ↓
Measurement (操作化度量)
    ↓
Observable (链上可观测事件)
    ↓
Identification (识别策略)
    ↓
Allowed Claim (可声称的范围)
```

当术语使用超出 Allowed Claim 层时，触发不可声称清单（`05_不可声称清单.md`）中的对应条目。