# 08. Borrower Adjustment / 借款人调整行为

**六层矩阵详细文件**  
**相关技术文档**：`03_技术文档/01_Aave_V3.md`  
**相关文献**：`04_文献/03_DeFi_Lending/`, `04_文献/02_Collateral_Credit/`

---

## Layer 1 — Definition

> **Borrower Adjustment 是由 borrower 或 borrower-authorized entity 触发的、改变仓位风险状态的协议动作。它是 Paper 1 的核心研究对象——protocol-observable position-management behavior。**

可能的调整类型：

```text
- Repay（还款 → 降低风险）
- Collateral addition（追加抵押 → 降低风险）
- Collateral withdrawal（提取抵押 → 增加风险）
- Additional borrowing（增借 → 增加风险）
- Asset switching（资产切换 → 改变风险结构）
- No action（不作为 → 风险由市场决定）
```

关键区分：

```text
Borrower Adjustment ≠ Complete Economic Behavior
Borrower Adjustment ≠ Creditworthiness
Borrower Adjustment ≠ Irrational Behavior
```

---

## Layer 2 — Construct

构念是 **protocol-observable position-management behavior process**——借款人在仓位风险变化过程中的协议可观测调整行为序列。

它**不是**：
- 借款人的完整经济行为（可能有大量链下操作）
- 借款人的信用能力本身
- 一个"偏差"指标（不预设理性基准）

它**是**：
- 一个可从合约事件中高精度重建的行为过程
- Paper 1 RQ1 的研究对象（行为是否存在系统性模式）
- Paper 1 RQ2 的解释变量（行为过程是否携带增量风险信息）

### 前景理论的定位

前景理论在 Paper 1 中的角色应从"开篇既定理论锚"降为：

```text
Compelling explanation / framing
```

而不是：

```text
Confirmed theory
```

因为：
1. HF=1.0 既是心理参照点，也是协议机制间断点——两个解释不可分离
2. 规避清算罚金是理性解释，不需要行为金融
3. 需要特殊识别策略才能区分行为偏差与理性风险管理

---

## Layer 3 — Measurement

### 行为过程变量

| 变量 | 定义 | 度量方式 |
|------|------|---------|
| Active Collateral Adjustment Rate | 观察期内净抵押调整 / 平均抵押价值 | 正值=风险减轻，负值=风险增加 |
| Active Debt Management Rate | 观察期内净债务变化 / 平均债务 | 正值=增借，负值=还款 |
| Response Latency | HF 首次跌破阈值到首次主动调整的天数 | 长延迟=被动行为 |
| Adjustment Intensity | 首次调整的幅度 / 仓位总价值 | 大幅度=果断，小幅度=试探 |
| Behavioral Consistency | 行为序列与规则性策略的吻合度 | 高一致性=系统性，低=随机 |
| Inaction Duration | 在风险区内不操作的天数 | 长=被动，短=主动 |

### 度量层次

```text
重建层：transaction / block
    ↓
事件窗口层：event-window（清算前 N 天/N 小时）
    ↓
特征层：hourly 或 event-window
    ↓
回归面板：daily / monthly
```

### 解释收紧

这些变量度量的是：

> **position-management process**

而不是：

> **creditworthiness itself**

---

## Layer 4 — Observable

| 信息 | 可观测性 | 来源 |
|------|---------|------|
| 主动调整动作（类型、时间、幅度） | ✅ 高 | 协议事件（需 active/passive 分类） |
| 调整动作的序列 | ✅ 高 | 事件时间线重建 |
| 调整前的仓位状态 | ✅ 高 | 状态重建 |
| 调整后的仓位状态 | ✅ 高 | 状态重建 |
| 调整与风险变化的时序关系 | ✅ 高 | 可计算 |
| 调整的动机 | ❌ 不可观测 | — |
| 借款人在其他协议的调整 | ❌ 不可观测 | 需跨协议索引 |
| 借款人在 CEX 的对冲操作 | ❌ 不可观测 | 链下数据 |

---

## Layer 5 — Identification

### 识别挑战

1. **Active vs Passive**：必须将 borrower-authorized action 与第三方/协议触发的被动事件区分开（见 `09_Active_vs_Passive_主动与被动分类.md`）
2. **行为 vs 价格**：仓位风险变化可能来自价格波动（外部）或借款人操作（内部），需要控制价格变化
3. **Safe/AA/代理路径**：通过 Safe 或 Account Abstraction 发起的操作需要额外解析
4. **FlashLoan**：FlashLoan 路径的"调整"不是普通风险管理，应排除或单独标记
5. **行为一致性 ≠ 前景理论**：观察到系统性行为模式不自动等于前景理论证据，需要排除理性规避清算罚金的解释

### 混淆因素

- 借款人可能在多个协议有仓位，链上只看到局部
- 自动化服务（keeper bot）可能执行调整，不是借款人主动决策
- Gas 成本可能阻止借款人在关键时刻操作

---

## Layer 6 — Allowed Claim

### 可以声称

- "Protocol-observable position-management behavior"（协议可观测的仓位管理行为）
- "Behavioral process variables"（行为过程变量）
- "The borrower made risk-reducing/increasing adjustments at time T"（借款人在时间 T 做了风险减轻/增加的调整）
- "Behavioral patterns are distinguishable from random responses"（行为模式可与随机响应区分）

### 不可以声称

- "Complete economic behavior"（完整经济行为）
- "Creditworthiness itself"（信用能力本身）
- "Borrower behavior confirms prospect theory"（借款人行为证实了前景理论）——需排除理性解释
- "The borrower is irrational"（借款人不理性）
- "Behavior process variables measure credit risk"（行为过程变量度量信用风险）——它们度量的是 position-management process

---

## 相关文献

| 文献 | 标题 | 年份 | 链接 | 与本概念的关系 |
|------|------|------|------|---------------|
| Kahneman & Tversky | Prospect Theory | 1979/2000 | https://doi.org/10.1017/cbo9780511803475.003 | 行为金融理论框架（降为 framing） |
| Tversky & Kahneman | Advances in Prospect Theory | 1992/2000 | https://doi.org/10.1017/cbo9780511803475.004 | CPT 扩展 |
| Barberis | Thirty Years of Prospect Theory in Economics | 2013 | https://doi.org/10.3386/w18621 | PT 综述；指出 DeFi 参照点的测量优势 |
| Cornelli et al. | Why DeFi Lending? Evidence from Aave V2 | 2025 | https://www.sciencedirect.com/science/article/pii/S1042443725002033 | Aave 交易级借贷行为实证 |
| Schuler | Frictions in DeFi Liquidations | 2026 | Aave V2 liquidation friction 研究 | 直接竞争文献 |
