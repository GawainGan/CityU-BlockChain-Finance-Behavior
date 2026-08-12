# 01. HF 公式错误：使用 LTV 而非 Liquidation Threshold

**严重程度**：🔴 Hard Error  
**Report 1 位置**：`sections/methodology.tex` Line 32  
**六层矩阵文件**：`02_逐概念六层矩阵/03_Health_Factor_健康因子.md`  
**技术文档**：`03_技术文档/01_Aave_V3.md`

---

## 1. 问题描述

Report 1 中的 Health Factor（HF）公式使用了 LTV（Loan-to-Value）参数，但 Aave V3 的 HF 实际使用的是 LT（Liquidation Threshold）。LTV 和 LT 是两个不同的参数，分别决定"能借多少"和"何时被清算"。

---

## 2. Report 1 原文

> **methodology.tex, Line 29-35:**
>
> For each borrowing position, a trajectory of position health will be reconstructed at a daily frequency. The core risk metric is the **health factor** (HF), defined as:
>
> $$\text{HF}_t = \frac{\sum_{i} (C_{i,t} \cdot P_{i,t}) \cdot \text{LTV}_i}{D_t}$$
>
> where $C_{i,t}$ is the quantity of collateral asset $i$ at time $t$, $P_{i,t}$ is its price, $\text{LTV}_i$ is the protocol-specific loan-to-value parameter for that asset, and $D_t$ is the total outstanding debt denominated in a common currency unit. The HF equals 1.0 at the liquidation threshold, with lower values indicating higher risk.

---

## 3. 错误分析

### 3.1 LTV ≠ LT

| 参数 | 全称 | 作用 | 典型值（ETH） |
|------|------|------|-------------|
| **LTV** | Loan-to-Value | 决定借款能力（能借多少） | 82.5% |
| **LT** | Liquidation Threshold | 决定清算触发（何时被清算） | 83% |

- LTV 用于计算 **borrowing capacity**：`max_debt = collateral_value × LTV`
- LT 用于计算 **清算边界**：`HF = Σ(collateral_value × LT) / debt`，当 HF < 1 时可被清算
- 两者数值相近但含义完全不同，不能互换

### 3.2 影响范围

- HF 公式错误直接影响所有基于 HF 的分析
- 如果使用 LTV 而非 LT 重建历史 HF，得到的 HF 轨迹将系统性偏离真实值
- 所有关于"借款人在 HF 接近 1.0 时的行为"的分析都将基于错误的风险指标

---

## 4. 六层矩阵映射

**文件**：`02_逐概念六层矩阵/03_Health_Factor_健康因子.md`

| 层级 | 六层矩阵内容 | Report 1 的问题 |
|------|-------------|-----------------|
| Definition | HF = Σ(V_i × LT_i) / D | 使用了 LTV 而非 LT |
| Construct | 仓位级别的清算风险接近度 | 构念定义正确，但度量错误 |
| Measurement | 需从合约参数获取 LT，而非 LTV | 使用了错误的参数 |
| Observable | LT 值从 Aave governance 事件/合约存储获取 | 未说明如何获取 LT |
| Identification | HF < 1 = liquidation eligible | 识别逻辑正确，但 HF 计算错误 |
| Allowed Claim | "reconstructed HF using LT" | 不可以声称使用了正确的 HF |

---

## 5. 修正方案

### 5.1 公式修正

```text
原式（错误）：HF = Σ(C_i × P_i × LTV_i) / D
修正后：     HF = Σ(C_i × P_i × LT_i) / D
```

### 5.2 参数说明修正

- 将 `LTV_i` 替换为 `LT_i`（Liquidation Threshold）
- 明确说明 LT 的来源：Aave V3 合约参数，可通过 governance 事件或合约存储获取
- 说明 LT 可能因 EMode、Isolation Mode 而不同
- 说明 LT 值可能随 governance 提案变化，需要按时间追踪

### 5.3 补充说明

- LTV 和 LT 的区分应明确写在论文中
- 需要说明如何处理 EMode 和 Isolation Mode 下的不同 LT 值

---

## 6. 文献支撑

| 文献 | 与本问题的关系 |
|------|---------------|
| Iftikhar et al. (2025) — Automated Risk Management in DeFi | 明确区分了 Aave 和 Compound 的风险参数，包括 LT 和 LTV 的区别 |
| Bartoletti & Lipparini (2025) — A theory of Lending Protocols in DeFi | 形式化了 DeFi 借贷协议中清算阈值和借款能力参数的区别 |
| Aave V3 官方文档 | 定义了 HF 使用 LT 而非 LTV |

---

## 7. 修改后的文本

```latex
For each borrowing position, a trajectory of position health will be 
reconstructed at a daily frequency. The core risk metric is the 
\textbf{health factor} (HF), defined as:

\begin{equation}
\text{HF}_t = \frac{\sum_{i} (C_{i,t} \cdot P_{i,t}) \cdot \text{LT}_i}{D_t}
\end{equation}

where $C_{i,t}$ is the quantity of collateral asset $i$ at time $t$, 
$P_{i,t}$ is its price obtained from Chainlink price feeds (to ensure 
consistency with the price information available to protocol 
participants at the time), $\text{LT}_i$ is the protocol-specific 
\emph{liquidation threshold} for that asset, and $D_t$ is the total 
outstanding debt (principal plus accrued interest) denominated in a 
common currency unit. 

It is important to distinguish the liquidation threshold (LT) from 
the loan-to-value (LTV) parameter: LTV determines borrowing capacity 
(\texttt{max\_debt} = \texttt{collateral\_value} $\times$ LTV), whereas 
LT determines the liquidation boundary (HF $< 1$ $\Rightarrow$ 
liquidation eligibility). The two parameters are set independently by 
protocol governance and may take different values for the same asset. 
Historical LT values are obtained from Aave V3 governance events and 
contract storage, as these parameters may change over time through 
governance proposals. In addition, positions in Efficiency Mode (EMode) 
or using isolated assets are subject to different LT values, and the 
reconstruction procedure accounts for these states.
```