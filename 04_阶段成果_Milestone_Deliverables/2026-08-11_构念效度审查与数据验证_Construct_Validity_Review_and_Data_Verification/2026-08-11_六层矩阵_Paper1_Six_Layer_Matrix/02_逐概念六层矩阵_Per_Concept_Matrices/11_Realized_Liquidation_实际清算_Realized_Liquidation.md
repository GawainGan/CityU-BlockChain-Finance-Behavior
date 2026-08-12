# 11. Realized Liquidation / 实际清算

**六层矩阵详细文件**  
**相关技术文档**：`03_技术文档/01_Aave_V3.md`  
**相关文献**：`04_文献/03_DeFi_Lending/`

---

## Layer 1 — Definition

> **Realized Liquidation 是清算机制实际执行的强制风险处置过程。当仓位满足协议清算条件后，由第三方 liquidator 或协议机制执行：偿还部分债务并获取对应抵押品（含清算罚金）。它是一种 mechanical position-risk realization / forced deleveraging mechanism。**

关键区分：

```text
Realized Liquidation ≠ Traditional Credit Default
Realized Liquidation ≠ Borrower Insolvency
Realized Liquidation ≠ Failure to Repay
```

### 为什么 Liquidation ≠ Credit Default

传统信用违约更接近：

```text
Borrower repayment capacity / willingness
        ↓
Failure or inability to meet obligation
        ↓
Credit default
```

DeFi liquidation 更接近：

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

DeFi liquidation 可能由以下原因触发，这些**不等于**借款人偿付能力失败：
- Collateral price crash（抵押品价格暴跌）
- Leverage too high（杠杆过高）
- Borrower 未及时补仓（操作延迟，不是无力偿还）
- Gas friction（gas 太贵无法操作）
- Oracle update timing（预言机更新时机）
- Network congestion（网络拥堵）
- Liquidator competition（清算人竞争）
- Borrower 主动放弃救仓（主动选择，不是无力）

---

## Layer 2 — Construct

构念是 **forced deleveraging / position distress realization**——仓位的强制风险处置。

它**不是**：
- 传统信用违约
- 借款人偿付能力/意愿的度量
- 借款人的信用表现

它**是**：
- 一个可从合约事件中高精度识别的协议事件
- Paper 1 RQ2 的 outcome 变量之一（但应优先使用 Liquidation Eligibility）
- 受执行环境影响的结果

---

## Layer 3 — Measurement

### Aave V3

- **事件**：`LiquidationCall(collateralAsset, debtAsset, user, debtToCover, liquidatedCollateralAmount, liquidator, receiveAToken)`
- **关键参数**：
  - `user`：被清算的借款人
  - `liquidator`：执行清算的第三方
  - `debtToCover`：清算人偿还的债务金额
  - `liquidatedCollateralAmount`：被清算的抵押品金额
  - `receiveAToken`：清算人是否接收 aToken
- **清算罚金**：Liquidation Bonus（通常 5-10%），作为对清算人的激励

### Compound III

- **事件**：`AbsorbCollateral(absorber, borrower, asset, collateralAbsorbed, usdValue)`
- **机制**：Compound III 使用 `absorb` 而非传统 liquidation call
- **区别**：Compound III 的清算由协议吸收 collateral，然后由市场决定如何处理

### MakerDAO / Sky

- **事件**：Vault liquidation 触发 auction
- **机制**：Auction-based（Dutch auction 或 English auction，取决于版本）
- **区别**：清算过程更长，涉及多个 auction 步骤

### 作为 Outcome 的度量

```text
Outcome B: Realized Liquidation
    Y = 1 if LiquidationCall (or equivalent) event occurred
    Y = 0 otherwise

附加信息：
    - 清算金额
    - 清算罚金
    - 清算时间
    - 从 eligibility 到 realized 的时间
    - 清算人地址（是否是已知 bot）
```

---

## Layer 4 — Observable

| 信息 | 可观测性 | 来源 |
|------|---------|------|
| 清算是否发生 | ✅ 高 | LiquidationCall 事件 |
| 清算金额 | ✅ 高 | 事件参数 |
| 清算罚金 | ✅ 高 | 可计算 |
| 清算人地址 | ✅ 高 | 事件参数 |
| 清算时间 | ✅ 高 | 事件 block/timestamp |
| 从 eligibility 到 realized 的时间 | ✅ 高 | 对比 eligibility 和 liquidation event |
| 清算人的 MEV/gas 策略 | ⚠️ 中 | 需分析清算人的交易模式 |
| 清算为什么未被更早执行 | ❌ 不可观测 | 涉及 liquidator 决策 |

---

## Layer 5 — Identification

### 识别挑战

1. **Liquidator-side friction**：Realized liquidation 受到 liquidator profitability、gas、MEV、网络拥堵、oracle timing 等因素影响，不完全反映 borrower state
2. **部分清算**：一次清算可能只覆盖部分债务，同一仓位可能经历多次清算
3. **清算罚金的内生性**：清算罚金大小影响 liquidator 意愿，从而影响清算是否发生
4. **Maker 的特殊性**：Maker 的 auction 机制使得 liquidation 的定义和度量与 Aave/Compound 不同

### 推荐处理

- **首选 Outcome**：Liquidation Eligibility（Outcome A），因为它隔离了 borrower state 和 liquidator friction
- **次选 Outcome**：Realized Liquidation（Outcome B），作为补充分析
- **两层分析**：先检验 behavior → eligibility，再检验 behavior + execution environment → realized liquidation

---

## Layer 6 — Allowed Claim

### 可以声称

- "Realized liquidation"（实际清算）
- "Forced deleveraging"（强制去杠杆）
- "Position distress realization"（仓位困境实现）
- "Liquidation propensity"（清算倾向）
- "Realized liquidation is contaminated by liquidator-side execution frictions"（实际清算受清算人执行摩擦影响）

### 不可以声称

- "Credit default"（信用违约）
- "Borrower failed to repay"（借款人未能偿付）
- "Borrower lacks repayment capacity"（借款人缺乏偿付能力）
- "Liquidation = traditional default"（清算 = 传统违约）
- "Improved liquidation prediction = improved credit scoring"（改进清算预测 = 改进信用评分）
- "Behavior predicts liquidation → therefore collateral can be reduced"（行为预测清算 → 因此可以减少抵押）——需要 5 层 Claim Ladder

---

## 相关文献

| 文献 | 标题 | 年份 | 链接 | 与本概念的关系 |
|------|------|------|------|---------------|
| Perez et al. | Liquidations: DeFi on a Knife-Edge | 2021 | https://doi.org/10.1007/978-3-662-64331-0_24 | 早期清算系统分析 |
| Qin et al. | An empirical study of DeFi liquidations | 2021 | https://doi.org/10.1145/3487552.3487811 | 清算激励结构 |
| Sadeghi & Feinstein | Liquidation Dynamics in DeFi and the Role of Transaction Fees | 2026 | https://arxiv.org/pdf/2602.12104 | 清算动态与交易费 |
| Schuler | Frictions in DeFi Liquidations: Evidence from Aave V2 | 2026 | — | Aave V2 清算摩擦（直接竞争文献） |
| Bartoletti & Lipparini | A theory of Lending Protocols in DeFi | 2025 | https://arxiv.org/abs/2506.15295 | DeFi 借贷协议理论 |
