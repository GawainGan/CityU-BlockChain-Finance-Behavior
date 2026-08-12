# 09. Active vs Passive / 主动与被动分类

**六层矩阵详细文件**  
**相关技术文档**：`03_技术文档/01_Aave_V3.md`  
**相关文献**：`04_文献/03_DeFi_Lending/`

---

## Layer 1 — Definition

> **Active action 是由 borrower 或 borrower-authorized entity 触发的协议操作。Passive event 是由第三方（如 liquidator）或协议机制触发的非 borrower 决策事件。**

### 7 月 Report 中的重大操作化缺陷

原 Report 使用：

```text
msg.sender == borrower wallet  →  active action
msg.sender != borrower         →  passive event
```

**这过于简单。** Aave 等协议支持 `onBehalfOf`，还存在 credit delegation、gateway、router、adapter、smart wallet (Safe)、account abstraction、third-party repay、automation 等多种路径。

---

## Layer 2 — Construct

构念是 **borrower-authorized action**——借款人授权或主动发起的仓位管理操作。

它**不是**：
- 简单的 `msg.sender == borrower`
- 借款人的心理决策（无法观测）
- 所有非 liquidation 事件（有些非 liquidation 事件也可能是第三方触发）

它**是**：
- 经过多层解析后确认由 borrower 或其授权代理发起的操作

---

## Layer 3 — Measurement

### 更新后的分层分类规则

```text
Step 1: 解析交易发起者（EOA / Safe / router / adapter）
         ↓
Step 2: 解析协议调用与 onBehalfOf 参数
         ↓
Step 3: 识别 debt owner / collateral owner / state beneficiary
         ↓
Step 4: 判定是否为 borrower-authorized action
         ↓
Step 5: 若无法可靠解析，标记 unclassified，不硬塞进 active
```

### 分类结果

| 分类 | 条件 | 处理 |
|------|------|------|
| **Active (EOA direct)** | msg.sender = borrower EOA, onBehalfOf = borrower | ✅ 主样本 |
| **Active (Safe)** | 通过 Safe multisig 发起，borrower 是 Safe owner | ✅ 主样本（需额外解析） |
| **Active (Router/Adapter)** | 通过 router/adapter 发起，但 onBehalfOf = borrower | ✅ 主样本（需额外解析） |
| **Active (Credit delegation)** | 第三方代借，但 borrower 授权了 credit delegation | ⚠️ 单独报告 |
| **Active (Automation/Keeper)** | 自动化服务发起，但代表 borrower 执行 | ⚠️ 单独报告 |
| **Passive (Liquidation)** | 第三方 liquidator 触发 | ❌ 被动事件 |
| **Unclassified** | 无法可靠解析发起者与受益者的关系 | ⚠️ 单独标记 |

### 解析链

```text
Initiator (EOA / Safe / Router)
    ↓
Intermediate Contract (Gateway / Adapter / Router)
    ↓
Protocol Call (function + parameters)
    ↓
onBehalfOf parameter
    ↓
Debt Owner / Collateral Owner
    ↓
State Beneficiary
    ↓
Classification: Active / Passive / Unclassified
```

---

## Layer 4 — Observable

| 信息 | 可观测性 | 来源 |
|------|---------|------|
| 交易发起者 (msg.sender) | ✅ 高 | 交易数据 |
| 调用的合约与函数 | ✅ 高 | 交易 input data |
| onBehalfOf 参数 | ✅ 高 | 事件参数 / 交易解析 |
| Safe multisig 的 owner 列表 | ✅ 高 | Safe 合约 |
| Router/adapter 的调用路径 | ✅ 中高 | 交易 trace 解析 |
| 借款人是否授权了自动化 | ⚠️ 中 | 需检查授权合约状态 |
| 借款人的心理决策过程 | ❌ 不可观测 | — |

---

## Layer 5 — Identification

### 识别挑战

1. **Safe 钱包占比**：如果 Safe 钱包占比高，简单 `msg.sender == borrower` 会大量误分类
2. **Account Abstraction**：ERC-4337 引入的 AA 使得发起者识别更复杂
3. **Credit delegation**：Aave 的 credit delegation 允许第三方使用 borrower 的信用额度
4. **自动化服务**：keeper bot 可能代表借款人执行操作
5. **无法分类的部分**：某些复杂路径可能无法可靠解析，不应硬塞进 active 或 passive

### 处理策略

- 主样本可先限制在可可靠识别的 EOA borrower-authorized actions
- Safe / 智能钱包 / 代理路径单独报告覆盖率与外推限制
- 第三方 liquidation 始终记为被动事件
- 无法分类的单独标记，不纳入主分析

### 样本策略

```text
主样本：可可靠识别的 EOA borrower-authorized actions
         ↓
扩展样本：加入 Safe / Router / Adapter 解析后的 actions
         ↓
外推限制报告：Safe/onBehalfOf/automation 的覆盖率与潜在偏差
         ↓
Unclassified：单独统计比例，不纳入主分析
```

---

## Layer 6 — Allowed Claim

### 可以声称

- "Borrower-authorized action"（借款人授权的操作）
- "The action was classified as active based on initiator–beneficiary parsing"（基于发起者-受益者解析，该操作被分类为主动）
- "X% of actions were classified as active; Y% were unclassified"（X% 的操作被分类为主动；Y% 无法分类）

### 不可以声称

- "All non-liquidation events are borrower-initiated"（所有非清算事件都是借款人发起的）
- "msg.sender == borrower" is sufficient for active classification（msg.sender == borrower 足够判定主动）——这是原 Report 的缺陷
- "Unclassified actions are passive"（无法分类的操作是被动的）——应单独标记
- "The borrower made a conscious decision"（借款人做了有意识的决策）——自动化服务也可能触发
