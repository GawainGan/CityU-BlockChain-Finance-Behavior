# 09. Settlement 层级混淆

**严重程度**：🔵 Terminology  
**Report 1 位置**：`sections/methodology.tex` Line 9  
**六层矩阵文件**：`02_逐概念六层矩阵/13_Boundary_Concepts_边界概念.md`

---

## 1. 问题描述

Report 1 在描述 Borrow/Repay 事件时使用 "settlement"（"the creation and settlement of loan positions"），但没有区分 settlement 的不同层级。在区块链语境中，settlement 至少有三层含义：Technical/Ledger Settlement（链上执行与最终确认）、Protocol-level Settlement（协议内义务了结）、Economic/Business Settlement（商业上的最终结算）。不加区分地使用 "settlement" 会导致概念混淆。

---

## 2. Report 1 原文

> **methodology.tex, Line 9:**
>
> (ii) `Borrow` and `Repay` events, representing the creation and settlement of loan positions

---

## 3. 错误分析

### 3.1 三层 Settlement

| 层级 | 含义 | 公开数据可观测性 |
|------|------|-----------------|
| **Technical / Ledger Settlement** | 交易上链、执行、状态更新、共识最终确认 | ✅ 高 |
| **Protocol-level Settlement** | 协议内义务了结（如 Repay 完成债务了结） | ✅ 高 |
| **Economic / Business Settlement** | 这笔钱在商业上代表什么（货款、工资等） | ❌ 低 |

### 3.2 Report 1 中的问题

- 使用 "settlement of loan positions" 描述 Repay 事件——这实际是 **Protocol-level Settlement**，但未标注层级
- 如果 reviewer 理解为 Economic Settlement，会质疑"如何从链上数据确定经济结算？"
- 更精确的说法是 "discharge of protocol-level obligations" 或 "repayment of outstanding debt"

### 3.3 影响程度

这个问题相对较轻（Terminology 级别），因为 Report 1 的核心研究不涉及 settlement 经济含义的识别（那是 Paper 2 的范围）。但术语精确化可以避免 reviewer 的误解。

---

## 4. 六层矩阵映射

**文件**：`02_逐概念六层矩阵/13_Boundary_Concepts_边界概念.md`

| 层级 | 内容 |
|------|------|
| Definition | Settlement 分三层：Technical / Protocol / Economic |
| Observable | Technical 和 Protocol 层可观测；Economic 层不可观测 |
| Allowed Claim | "protocol-level settlement"（标注层级） |

**不可声称清单**：`05_不可声称清单.md` §5
- §5.3: "On-chain execution = final settlement"
- §5.4: "Settlement = liquidation"

---

## 5. 修正方案

### 5.1 术语精确化

```text
原表述："the creation and settlement of loan positions"
修正后："the creation and repayment of loan positions"
```

用 "repayment" 替代 "settlement"，因为：
- "repayment" 精确描述了 Repay 事件的功能
- 避免了 "settlement" 的多层含义歧义
- 如果确实需要使用 "settlement"，应标注层级

### 5.2 如果需要使用 "settlement"

```text
"the creation and protocol-level settlement of loan positions 
(i.e., the discharge of protocol-level borrowing obligations through 
repayment)"
```

---

## 6. 文献支撑

| 文献 | 与本问题的关系 |
|------|---------------|
| Hautsch et al. (2024) | Blockchain settlement latency——区分了技术结算和经济结算 |
| Budish & Sunderam (2026) | 分析 blockchain trust model 在传统金融中的 settlement 含义 |
| Ethereum PoS 文档 | 定义了 consensus finality——Technical Settlement 的基础 |

---

## 7. 修改后的文本

```latex
(ii) \texttt{Borrow} and \texttt{Repay} events, representing the 
creation and repayment of loan positions;
```

（简单替换 "settlement" 为 "repayment"，消除歧义）
