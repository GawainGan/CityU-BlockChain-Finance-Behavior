# 问题总表 / Problem Summary Table

**日期**：2026-08-11  
**来源**：基于六层矩阵对 Report 1（2026-07-17）的逐概念审查

---

## 问题清单

| # | 问题 | 严重程度 | Report 1 位置 | 六层矩阵文件 | 状态 |
|---|------|---------|-------------|-------------|------|
| 01 | HF 公式使用 LTV 而非 Liquidation Threshold | 🔴 Hard Error | methodology.tex L32 | 03_Health_Factor | ✅ 已诊断 |
| 02 | 主动/被动分类仅用 msg.sender == borrower | 🔴 Hard Error | methodology.tex L23-25 | 09_Active_vs_Passive | ✅ 已诊断 |
| 03 | Deposit/Withdraw 等同于 Collateral 提供/移除 | 🔴 Hard Error | methodology.tex L9 | 07_Supply_vs_CollateralEnabled | ✅ 已诊断 |
| 04 | "完全可观测性"声称过强 | 🟡 Over-claim | introduction.tex L3, literature-review.tex L21 | 08_Borrower_Adjustment, 12_Borrower_Identity | ✅ 已诊断 |
| 05 | RQ2 "Credit Layer" 命名过强 | 🟡 Over-claim | research-topic.tex L18 | 05_不可声称清单 §1, §2 | ✅ 已诊断 |
| 06 | Prospect Theory 定位为 confirmed anchor 而非 competing explanation | 🟡 Over-claim | literature-review.tex L21-23, research-topic.tex L47, discussion.tex L9 | 05_不可声称清单 §4 | ✅ 已诊断 |
| 07 | Liquidation 与 Default 混用 | 🟡 Over-claim | abstract, literature-review, discussion | 10_Liquidation_Eligibility, 11_Realized_Liquidation | ✅ 已诊断 |
| 08 | Collateral 与 Credit 概念混用 | 🟡 Over-claim | introduction, research-topic, discussion | 01_Collateral, 05_不可声称清单 §1 | ✅ 已诊断 |
| 09 | Settlement 不分层使用 | 🔵 Terminology | methodology.tex L9 | 13_Boundary_Concepts | ✅ 已诊断 |
| 10 | 协议间术语直接混用（Aave HF = Compound = Maker） | 🔵 Terminology | methodology.tex L9-11 | 03_Health_Factor, 06_术语边界对照表 | ✅ 已诊断 |
| 11 | "Credit-relevant information" 反复使用，超出范围 | 🟡 Over-claim | introduction, literature-review, research-topic | 05_不可声称清单 §1, §2 | ✅ 已诊断 |

---

## 按严重程度分组

### 🔴 Hard Errors（3个）— 事实性/技术性错误

| # | 问题 | 核心修正 |
|---|------|---------|
| 01 | HF 公式用 LTV 而非 LT | 将 LTV 替换为 LT（Liquidation Threshold） |
| 02 | msg.sender == borrower 太简单 | 增加 onBehalfOf 检查、router/automation 识别 |
| 03 | Deposit = Collateral | 区分 Supply 和 Collateral-Enabled Supply |

### 🟡 Over-claims（5个）— 声称超出数据支持

| # | 问题 | 核心修正 |
|---|------|---------|
| 04 | "完全可观测性" | 改为"协议事件可观测"，明确经济目的不可观测 |
| 05 | "Credit Layer" 命名 | 改为 "Liquidation Propensity Layer" 或 "Position Distress Layer" |
| 06 | PT 作为 confirmed anchor | 降级为 "compelling framing / competing explanation" |
| 07 | Liquidation = Default | 全文区分 liquidation 和 default，不混用 |
| 08 | Collateral = Credit | 全文区分 collateral-based lending 和 credit |
| 11 | "Credit-relevant information" | 改为 "liquidation-relevant information" 或 "position-risk-relevant information" |

### 🔵 Terminology（3个）— 术语使用不精确

| # | 问题 | 核心修正 |
|---|------|---------|
| 09 | Settlement 不分层 | 标注 Technical / Protocol / Economic 层级 |
| 10 | 协议间术语混用 | 分别使用各自术语，不直接拼接 panel |

---

## 修正优先级

```
Phase 1（必须修正，影响全篇可信度）：
  → 01 HF 公式错误
  → 02 主动/被动分类
  → 03 Supply vs Collateral-Enabled
  → 07 Liquidation vs Default
  → 08 Collateral vs Credit

Phase 2（影响声称范围，需要降级）：
  → 04 完全可观测性
  → 05 Credit Layer 命名
  → 06 Prospect Theory 定位
  → 11 Credit-relevant information

Phase 3（术语精确化）：
  → 09 Settlement 分层
  → 10 协议间术语
```

---

## 修正后的整体变化

| 维度 | Report 1 | Report v2 |
|------|---------|-----------|
| 核心声称 | "Borrower behavior provides credit signals" | "Protocol-observable position management behavior provides incremental information for liquidation propensity" |
| 理论定位 | Prospect Theory as confirmed anchor | Prospect Theory as compelling framing / competing explanation |
| Outcome | Liquidation / default (混用) | Liquidation eligibility / realized liquidation (区分) |
| 可观测性 | "Complete observability" | "Protocol-observable events; economic purpose unobservable" |
| 协议范围 | Aave + Compound + MakerDAO (直接拼接) | Aave V3 为主，Compound/Maker 为外部有效性检验 |
| Collateral | Supply = Collateral | Supply ≠ Collateral-Enabled Supply |
| 主动/被动 | msg.sender == borrower | msg.sender + onBehalfOf + router/automation 识别 |