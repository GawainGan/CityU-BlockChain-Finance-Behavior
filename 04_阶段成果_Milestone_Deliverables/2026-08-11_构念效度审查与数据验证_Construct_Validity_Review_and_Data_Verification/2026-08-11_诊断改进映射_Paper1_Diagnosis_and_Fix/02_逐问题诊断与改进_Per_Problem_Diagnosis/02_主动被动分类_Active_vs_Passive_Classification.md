# 02. 主动/被动分类：msg.sender == borrower 过于简化

**严重程度**：🔴 Hard Error  
**Report 1 位置**：`sections/methodology.tex` Lines 23-25  
**六层矩阵文件**：`02_逐概念六层矩阵/09_Active_vs_Passive_主动与被动分类.md`

---

## 1. 问题描述

Report 1 使用 `msg.sender == borrower` 作为主动/被动分类的唯一标准。这一规则忽略了 Aave V3 的 `onBehalfOf` 机制、Safe（Gnosis Safe）多签钱包、router 合约、自动化服务和 credit delegation 等常见场景，导致主动行为被错误分类为被动行为（或反之）。

---

## 2. Report 1 原文

> **methodology.tex, Lines 19-25:**
>
> A critical element of the methodology is the operational distinction between active, borrower-initiated actions and passive, externally-driven events. [...] The classification will proceed as follows. An on-chain transaction will be classified as an **active borrower action** if and only if the transaction sender (`msg.sender`) matches the borrower wallet address. Under this criterion, the following events will be classified as active: (i) depositing additional collateral, (ii) repaying an outstanding loan, (iii) withdrawing collateral (when permitted by the protocol), (iv) borrowing additional assets, and (v) closing a position by fully repaying the outstanding debt and withdrawing all collateral. A transaction will be classified as a **passive liquidation event** if the transaction sender is an address other than the borrower, regardless of whether that address can be identified as a known liquidation bot.
>
> **methodology.tex, Line 25:**
>
> This classification rule has the important advantage of being fully deterministic and replicable: any researcher with access to the raw transaction data can apply it identically. Its primary limitation is that it cannot distinguish between cases where the borrower is the initiator of the transaction (true active behavior) and cases where the borrower delegates transaction signing to a third-party service, although the analysis can include robustness checks that restrict the sample to addresses where the majority of transactions are self-initiated based on transaction nonce patterns.

---

## 3. 错误分析

### 3.1 `msg.sender == borrower` 遗漏的场景

| 场景 | msg.sender | 实际发起者 | Report 1 分类 | 正确分类 |
|------|-----------|-----------|-------------|---------|
| 借款人直接操作 | borrower | borrower | ✅ active | ✅ active |
| Credit delegation（onBehalfOf） | delegator | delegator（但债务归属 borrower） | ❌ passive | 需单独处理 |
| Safe 多签钱包 | Safe contract | borrower（通过多签） | ❌ passive | ✅ active |
| Router 合约（如 1inch, Paraswap） | router | borrower（通过 router） | ❌ passive | ✅ active |
| 自动化服务（如 DefiSaver） | automation contract | borrower（授权的自动化） | ❌ passive | ✅ active（但需标注） |
| 第三方清算 | liquidator | liquidator | ✅ passive | ✅ passive |

### 3.2 影响范围

- 大量通过 Safe 钱包或 router 操作的借款人会被错误分类为"被动"
- Credit delegation 场景下，`msg.sender` 是 delegator 而非 borrower，但操作本身可能是借款人授权的主动行为
- 如果样本中 Safe 钱包用户占比不小，系统性分类错误会严重影响 RQ1 的结论

### 3.3 Report 1 已知但未充分处理

Report 1 在 Line 25 提到了"delegates transaction signing to a third-party service"这一限制，但：
- 仅作为"limitation"提及，未提出具体解决方案
- 未提及 `onBehalfOf` 参数
- 未提及 Safe 钱包和 router 的识别方法
- 未说明如何区分自动化服务和第三方清算

---

## 4. 六层矩阵映射

**文件**：`02_逐概念六层矩阵/09_Active_vs_Passive_主动与被动分类.md`

| 层级 | 六层矩阵内容 | Report 1 的问题 |
|------|-------------|-----------------|
| Definition | Active = human-initiated intentional position management action | 定义正确但操作化不足 |
| Construct | 主动调整 vs 被动事件 | 构念正确 |
| Measurement | 需要多层识别：msg.sender + onBehalfOf + Safe + router | 仅用 msg.sender，遗漏多层 |
| Observable | 事件参数中的 onBehalfOf, 交易发起地址, 调用链 | 未使用 onBehalfOf 参数 |
| Identification | 需要过滤规则排除自动化/路由/多签 | 识别规则不充分 |
| Allowed Claim | "transactions initiated by the borrower address (after filtering)" | 未说明过滤过程 |

---

## 5. 修正方案

### 5.1 多层分类规则

```text
Layer 1: msg.sender == onBehalfOf?
    → Yes: 直接操作，classify as active
    → No:  进入 Layer 2

Layer 2: msg.sender 是已知 router/Safe/automation 合约?
    → Yes: 且 onBehalfOf == borrower: classify as active (via intermediary)
    → No:  进入 Layer 3

Layer 3: msg.sender 是已知 liquidator?
    → Yes: classify as passive (liquidation)
    → No:  classify as unclassified / further analysis needed
```

### 5.2 具体实施

1. **提取 `onBehalfOf` 参数**：Aave V3 的 Borrow/Repay/Supply/Withdraw 事件中都包含 `onBehalfOf` 字段
2. **构建已知合约地址库**：
   - Safe（Gnosis Safe）代理合约
   - 常见 router 合约（1inch, Paraswap, Uniswap router）
   - 自动化服务合约（DefiSaver, Gelato, Oasis）
   - 已知 liquidator 地址
3. **交易调用链分析**：对于复杂交易，分析 `trace` 数据确定实际调用者
4. **标注分类置信度**：对于无法明确分类的交易，标注为 "unclassified" 并在敏感性分析中排除

### 5.3 保留确定性优势

Report 1 强调分类规则"deterministic and replicable"。修正后的方案仍然满足这一要求——所有识别规则都基于公开链上数据（事件参数、已知合约地址库、trace 数据），任何研究者可以复制。

---

## 6. 文献支撑

| 文献 | 与本问题的关系 |
|------|---------------|
| Aave V3 官方文档 | 定义了 `onBehalfOf` 参数和 credit delegation 机制 |
| Ghosh et al. (2024) — On-Chain Credit Risk Score | 使用钱包级交易历史构建评分，需要处理类似的身份识别问题 |
| Iftikhar et al. (2025) — Automated Risk Management in DeFi | 比较了 Aave 和 Compound 的机制差异，包括接口设计 |

---

## 7. 修改后的文本

```latex
\subsection{Active vs.\ Passive Classification}

A critical element of the methodology is the operational distinction 
between active, borrower-initiated actions and passive, 
externally-driven events. This distinction is essential because the 
research question concerns borrower behavior, and conflating active 
borrower decisions with events triggered by third parties or protocol 
mechanics would severely undermine the validity of the analysis.

The classification employs a multi-layer identification procedure 
that goes beyond a simple comparison of \texttt{msg.sender} with the 
borrower address. In Aave V3, several common interaction patterns 
necessitate this more nuanced approach:

\begin{enumerate}
\item \textbf{Credit delegation (\texttt{onBehalfOf}).} Aave V3 
events include an \texttt{onBehalfOf} parameter indicating the 
address whose position is affected, which may differ from 
\texttt{msg.sender}. A transaction is classified as an active 
borrower action only when \texttt{onBehalfOf} matches the borrower 
address, regardless of who initiated the transaction.

\item \textbf{Smart-contract wallets and routers.} Borrowers 
frequently interact with the protocol through Gnosis Safe 
multi-signature wallets, DEX router contracts (e.g., 1inch, 
Paraswap), or automation services (e.g., DefiSaver, Gelato). 
Transactions initiated through these intermediaries are classified 
as active borrower actions when the \texttt{onBehalfOf} field 
identifies the borrower. A curated registry of known intermediary 
contract addresses is maintained and updated throughout the study 
period.

\item \textbf{Liquidation events.} A transaction is classified as 
a \textbf{passive liquidation event} when the caller is an address 
other than the borrower (or an intermediary acting on the borrower's 
behalf) and the event is a \texttt{LiquidationCall}. Known 
liquidation bot addresses are identified through transaction pattern 
analysis but are not excluded from the passive category, as 
liquidation by any third party constitutes a passive event from 
the borrower's perspective.
\end{enumerate}

The classification procedure produces three categories: 
\textbf{active} (borrower-initiated, including via intermediaries), 
\textbf{passive} (liquidation by third parties), and 
\textbf{unclassified} (transactions that cannot be confidently 
assigned to either category). Unclassified transactions are excluded 
from the primary analysis and their sensitivity is assessed in 
robustness checks. All classification rules are deterministic, 
based solely on public on-chain data (event parameters, known 
contract registries, and transaction trace data), and can be 
replicated by any researcher with access to blockchain infrastructure.
```