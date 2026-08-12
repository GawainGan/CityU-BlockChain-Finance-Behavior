# 范围、操作化与数据边界更新

**日期**：2026-08-11  
**对应**：`2026-07-17_Research_Report` 的研究范围、方法论与数据声明  
**目标**：把“现在做什么 / 不做什么 / 用什么数据能做什么”写成可汇报版本

---

## 1. 研究范围：更新后的边界

### 1.1 当前纳入（In Scope）—— Paper 1

**研究对象**：

> 以太坊主流超额抵押借贷协议中，借款人在仓位风险上升过程中的 **协议可观测主动调整行为**，及其对后续清算倾向的增量信息。

**纳入内容**：

- 协议：Aave（优先）、Compound、Maker（跨协议稳健性）
- 事件：Supply/Deposit、Withdraw、Borrow、Repay、Liquidation、（必要时）FlashLoan 标记
- 行为：追加抵押、还款、增借、提取、资产切换、不作为
- 结果：liquidation occurrence / time-to-liquidation / distance-to-liquidation 恶化

**分析单元（保持，但下沉重建频率）**：

```text
底层轨迹：borrower-position-transaction/block
分析面板：borrower-position-day / borrower-position-month
```

### 1.2 明确后置（Out of Current Paper，但保留在研究计划）

| 主题 | 为什么后置 |
|---|---|
| Payment vs Settlement 分类 | 识别问题不同；数据与标签体系不同 |
| KYC + 消费场景信用模型 | 公开数据不足以支撑；依赖支付机构数据 |
| 不足额抵押信用机制设计 | 属于机制/理论延伸，不是当前实证主问题 |
| RWA / 应收账款融资 | 相关但另成企业信用资产线 |
| “取消抵押”规范性主张 | 理论表述已纠正，不再作为论文目标 |

### 1.3 明确不声称（Non-claims）

1. 不声称观察了借款人完整资产负债表。
2. 不声称识别了每笔操作的真实心理动机。
3. 不声称 liquidation = 传统违约。
4. 不声称跨协议相似行为 = 同一自然人。
5. 不声称公开 transfer 历史可直接生成消费信用分。

---

## 2. 研究问题：措辞更新

### 2.1 保留的两层结构

**RQ1（行为层）** —— 基本保留，收紧对象：

> 当协议定义的清算距离缩小（风险上升）时，借款人是否表现出系统性的、可与价格机械效应和第三方清算相区分的主动仓位调整模式？

**RQ2（风险信息层）** —— 原“信用层”改名：

原题容易写成 Credit Layer，过强。

更新为：

> 在控制当前风险状态、账户特征、资产构成与市场条件后，行为过程变量是否对未来 **liquidation propensity** 提供增量预测能力？

### 2.2 假设层同步调整

| 原假设指向 | 更新后 |
|---|---|
| H1：主动调整随 HF 接近阈值而变化 | 保留；但 HF/风险度量按协议真实机制重建 |
| H1b/H1c：前景理论损失厌恶与参照点 | 降为 **competing explanation / framing**，不作为已证明结论前置 |
| H2：预测 future liquidation = credit outcome | 改为预测 liquidation / risk deterioration；不再直接等同 creditworthiness |

---

## 3. 操作化更新

### 3.1 风险度量

**原 Report 问题**：用 LTV 写 HF。

**更新规则**：

1. **Aave**：按 Liquidation Threshold 重建 Health Factor  
2. **Compound**：按 account liquidity / shortfall 或协议对应机制  
3. **Maker**：按 vault collateralization / liquidation structure  
4. **跨协议比较变量**：

\[
\text{DistanceToLiquidation}_{i,t}
=
f(\text{protocol-specific risk metric})
\]

再标准化为可比指标，而不是强行统一成“HF→1”。

### 3.2 主动 / 被动分类

**原规则**：

```text
msg.sender == borrower  ⇒ active
```

**更新规则（分层）**：

```text
Step 1: 解析交易发起者（EOA / Safe / router / adapter）
Step 2: 解析协议调用与 onBehalfOf
Step 3: 识别 debt owner / collateral owner / state beneficiary
Step 4: 判定是否为 borrower-authorized action
Step 5: 若无法可靠解析，标记 unclassified，不硬塞进 active
```

**样本策略**：

- 主样本可先限制在可可靠识别的 EOA borrower-authorized actions
- Safe / 智能钱包 / 代理路径单独报告覆盖率与外推限制
- 第三方 liquidation 始终记为被动事件

### 3.3 Supply 与 Collateral 的区分

```text
Supply/Deposit
≠
Collateral-enabled Supply
≠
Risk-reducing collateral addition
```

只有在资产被启用为抵押、且增加了可支撑债务缓冲时，才计入“风险减轻的追加抵押”。

### 3.4 行为过程变量（保留，但解释收紧）

继续使用，但声明它们度量的是：

> **position-management process**

而不是：

> **creditworthiness itself**

变量组仍可包括：

- 主动抵押调整率
- 主动债务管理率
- 响应延迟
- 调整强度
- 行为一致性 / 不作为时长

### 3.5 时间频率

```text
重建层：transaction / block
特征层：hourly or event-window
回归层：daily / monthly panel
```

原因：清算前几分钟到几小时的反应，用纯日频可能消失。

---

## 4. 数据边界更新

### 4.1 Paper 1 数据栈（当前）

| 层级 | 来源 | 用途 |
|---|---|---|
| 协议事件与状态 | Dune / archive RPC | Borrow/Repay/Supply/Withdraw/Liquidation 重建 |
| 价格 | Chainlink 等协议实际使用预言机 | 与参与者当时信息集对齐 |
| 地址类型 | 标签库 / 启发式 | EOA vs contract / liquidator bots |
| Gas / 市场环境 | 链上费用与波动率 | 控制操作摩擦与市场状态 |

### 4.2 可观测性分层（写作时必须遵守）

| 信息 | 公开数据 | 研究可声称 |
|---|---|---|
| 交易是否执行 | ✅ | technical settlement occurred |
| 协议动作是什么 | ✅ | Borrow / Repay / ... |
| 谁受益 / onBehalfOf | 部分 ✅ | 需额外解析 |
| 对手方实体 | 部分 ✅ | 标签推断 |
| 支付还是结算 | 弱 | 仅 inferred，需 Paper 2 |
| 买了什么 / 哪个商户 | ❌ | 需支付公司数据 |
| 真实身份 KYC | ❌ | 需私有或合规数据源 |
| 传统违约标签 | ❌ | 当前通常不可得 |

### 4.3 Paper 2 / 3 的数据候选（不并入当前主文）

| 目标 | 候选数据 | 注意 |
|---|---|---|
| Payment vs Settlement 语义 | Allium enriched transfers 等 | 是推断，不是 ground truth |
| 实体识别 | Nansen / Chainalysis 类标签 | 辅助，不等于 purpose |
| 行业基准 | Artemis / Visa Onchain Analytics | 宏观验证，非个体行为 GT |
| 行为信用 gold standard | 支付机构：KYC + order + MCC + refund + repayment/default | 样本量与合规是瓶颈 |

会议对样本量的提醒（未经外部核验，仅作研究设计约束）：

> 小支付公司日订单几百到上千，可能不够支撑稳健消费信用模型；需要高频、连续、用户级、场景化数据。

### 4.4 当前数据策略的一句话

> **先用公开协议数据把 Paper 1 做扎实；  
> 不用公开 transfer 假装已经拥有消费行为与信用标签。**

---

## 5. 更新后的最小可行研究设计（Paper 1）

```text
1. 选 Aave 小样本地址
2. 按真实 LT 重建风险轨迹（tx/block 级）
3. 解析主动/被动/无法分类
4. 统计清算前窗口是否存在足够主动调整
5. 比较：状态变量模型 vs 状态+行为过程模型
6. 明确报告：
   - 能识别什么
   - 不能识别什么
   - Safe/onBehalfOf 覆盖率
   - outcome 只解释为 liquidation propensity
```

若第 4 步显示临界窗口过短：

> 研究降级为“清算前若干日的预防性行为”，而不是“最后一刻反应”。

若行为变量无增量：

> 仍可保留为行为描述论文，但不声称改进信用评估。

---

## 6. 与会议结论的接口（但不污染 Paper 1）

会议最有价值的研究命题：

```text
KYC/身份
→ 支付记录
→ 消费场景
→ 行为特征
→ 可信度
→ 信贷决策
```

这对应 **Paper 3**，不是当前实证可立即落地的 Paper 1。

Paper 1 在总计划中的位置是：

> 先证明：即便在纯抵押型 DeFi 中，**行为过程**也可能携带超出静态抵押状态的信息。  
> 这为后续“行为能否替代部分抵押”提供微观基础，而不是直接完成信用模型。

---

## 7. 给写作/汇报的检查清单

写任何段落前先问：

1. 我现在说的是 **protocol action** 还是 **economic purpose**？
2. 我的 y 变量是 **liquidation** 还是 **credit default**？
3. 我用的 capacity 来自 **collateral** 还是 **behavior-based credit**？
4. 我的数据能不能支持这个名词？
5. 如果删掉私有数据/支付公司假设，这个句子是否还成立？

若第 5 问答案为否，该句不应出现在当前 Paper 1。
