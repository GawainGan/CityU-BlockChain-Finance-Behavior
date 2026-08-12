# Branch B 技术方案：决策本体的构建、形式化与验证

**版本**：v1.0 | **日期**：2026-07-08

---

## 1. 技术栈概览

B 的技术方案不同于 A/C/D ——它不仅是"数据分析管线"，更是"知识工程 + 数据分析"的混合。

| 阶段 | 主要活动 | 工具 / 方法 |
|------|----------|-----------|
| 本体设计 | 定义领域概念、映射到链上证据、编写公理 | 手动分析（专家判断） + Protégé |
| 本体编码 | 形式化 OWL/RDF 表示 | Protégé OWL 编辑器 |
| 数据标注 | 用本体规则对链上数据做半自动标注 | Python + SPARQL 查询 |
| 特征工程 | 从本体标注中派生数值特征 | Python (pandas, numpy) |
| 赛马验证 | 逻辑回归 / XGBoost 与 M0/M1 比较 | R (glm + pROC) 或 Python (sklearn) |
| 跨协议检验 | 本体规则的重新应用 | Python (重复步骤 3-4) |

### 1.1 为什么不用更复杂的技术？

在概念阶段，B 的价值是概念的——它问的是"哪些行为可被解释为信用证据?"而不是"哪个算法能从行为中提取更多信息?"。因此，数据预处理应该是一个简单的规则引擎而非深度学习模型。**本体在此是社会科学的解释工具，不是机器学习的特征生成器。**

---

## 2. 阶段一：本体设计（概念层）

### 2.1 本体范围与需求

**目标**：定义一个信用评估本体，用意在生产从 DeFi 借贷数据中的信用特征。
**范围**：通用（足够抽象以跨协议），但包含 DeFi 特定概念（如 HF、清算、闪电贷）。
**输出**：一个 OWL 格式的知识库，包含：
- 偿付能力（AbilityToRepay）与偿付意愿（WillingnessToRepay）的根类
- 定义子类（具体的类型，如"SavvyBorrower", "NeglectfulBorrower", "RiskTaker"）
- 对象属性（"hasEvidence", "hasPattern", "isClassifiedAs"）
- 公理（逻辑规则，如："All borrowers who repay before due date and have HF > 2.0 are Class X"）

### 2.2 类的定义（知识概念化）

**步骤 1：信用概念 $\to$ 可观测的证据映射**

为每个根概念（能力/意愿）定义一套可观测的链上证据。这不是一个任意的列表——证据的质量有层次：

| 层次 | 证据类型 | 信用含义 | 记入本体的方式 |
|------|---------|---------|-------------|
| 强意愿 | 在 HF 安全时（>1.5）仍持续加抵押 | 主动管理债务，不只是应对危机 | hasEvidence (strong_willingness) |
| 中意愿 | 在 HF 接近 1.0 时加抵押（但不是被清算） | 有认知地维护仓位 | hasEvidence (moderate_willingness) |
| 弱意愿 | 最近一次交互距今 < 2 周 | 至少是活跃的 — 不是遗忘账户 | hasEvidence (active) |
| 强能力 | HF 从 >2.0 跳下来到 >1.5 | 拥有资源去加抵押 | hasAbility (high_capacity) |
| 中能力 | HF 从 >1.5 跳下来到 >1.2 | 有预算但不宽裕 | hasAbility (moderate_capacity) |
| 弱能力 | 在 14 天内被清算过 | 能力确实不足 | hasAbility (low_capacity) |

**步骤 2：识别实体类型**

- **AssetType**：波动型 vs 稳定型
- **InteractionType**：主动交互、被动交互、与特定协议交互
- **TemporalPattern**：周期性、聚集性、突发性
- **RiskAttitude**：来源—抵押品波动倾向（GamblingRisk） vs 偿付态度（WillingnessDeficit）

**步骤 3：定义层次**

```
CreditSignal
├── AbilityToRepay
│   ├── HighCapacity
│   ├── ModerateCapacity
│   └── LowCapacity
├── WillingnessToRepay
│   ├── StrongWillingness
│   ├── ModerateWillingness
│   └── WeakWillingness
└── RiskProfile
    ├── RiskNeglecter (从不管理 — 不反映任何能力或意愿)
    ├── RiskGambler (加杠杆 + 接受高风险)
    └── RiskAvoider (保守头寸管理)
```

### 2.3 公理设计（逻辑规则）

为了将证据映射到类，需要一阶逻辑规则的公理。以下为Protege

 (OWL) 的伪规则：

```
Rule: HighCapacity
  IF (hasEvidence, strong_capacity) AND (NOT hasEvidence, recently_liquidated)

Rule: StrongWillingness
  IF (hasEvidence, active_management_when_safe) OR
     (hasEvidence, frequent_small_repayments AND hasEvidence, active_trader_flag = false)

Rule: RiskGambler  
  IF (hasEvidence, increased_leverage_during_decline) OR
     (hasEvidence, frequent_switches_to_volatile_assets)
```

这些规则可以用SWRL（Semantic Web Rule Language）直接在Protégé中编码——允许推理引擎自动对新地址进行分类。

---

## 3. 阶段二：本体自动标注（数据级）

### 3.1 半自动标注流水线

概念层的规则（如"StrongWillingness"的定义）需要被转化为一个批处理程序，可以自动从原始交易日志中为每个地址-月生成标注。流程如下：

1. **输入**：包含每个地址-月的原始数据框（Deposit/Borrow/Repay/Withdraw表）
2. **规则引擎**：对每个地址-月，逐条运行本体规则：
   ```python
   for _, row in df.iterrows():
       if row['n_repay_when_hf_safe_30d'] > 0:
           row['signal_strong_willingness'] = True
       if row['n_borrow_when_hf_danger_30d'] > 0:
           row['signal_risk_gambler'] = True
   ```
3. **输出**：一个包含本体衍生特征的数据框

### 3.2 本体特征列表

| 特征 | 定义 | 类型 | 信用含义 |
|------|------|------|----------|
| signal_strong_willingness | 在HF>1.5时加抵押/还款的次数 | binary | 主动债务管理 |
| signal_moderate_willingness | 在HF∈(1.1, 1.5]时加抵押 | binary | 有认知的维护 |
| signal_weak_willingness | 最近一次交互距今 > 90天 | binary | 忽略/遗忘账户 |
| signal_high_capacity | 全链余额 > 当前债务 | binary | 拥有足够资源 |
| signal_capacity_change | log(全链余额_t / 全链余额_{t-1}) | continuous | 财务趋势 |
| signal_risk_gambler | 在HF下降的30天内增贷 | binary | 冒险/杠杆追求 |
| signal_collateral_switch_to_volatility | 最近将稳定币转变为波动资产 | binary | 增加市场敞口 |

注意：这些特征是**二阶**的——它们不是原始的Deposit/Borrow事件，而是对这些事件进行本体解释（即：意义赋值）后的特征。比如，"一个Deposit事件"是原始数据，而"在HF安全时的Deposit"是需要本体规则的加工特征。

### 3.3 处理缺失的"能力证据"

偿付能力的一个根本问题是：在超额抵押的DeFi中，大多数人的HF > 1.0，那么怎么知道谁真正缺乏能力？（毕竟他们永远不会出现"余额不足"的错误——因为他们不可能借款更多。）

解决方案：使用**逆证据**——哪些行为是能力不足的表现？
- 虽然HF > 1.0，但从未加抵押，HF在一段时间后自然回落 → 能力不足的信号（无法持续提供缓冲）
- 从被清算的地址接收资金 → 可能是个体经济困难
- 与其他 DeFi 智能体的交互模式是"总接收"，而不是"总转出" → 可能是个被动的资金流动节点（不是积极策略）

---

## 4. 阶段三：实证验证（赛马设计）

### 4.1 赛马预测模型

**因变量**：在随后的 T 个月（T = 1, 3, 6 作为敏感度分析）内是否被清算。

**模型序列**：

| 模型 | 特征集 | 含义 |
|------|--------|------|
| M0 | HF指标（min、mean、sd）、抵押率、债务价值、利用率 | 纯传统风险模型 |
| M1 | M0 + BDM五维度（V4行为特征——无本体） | "行为偏差"是否已被传统特征编码 |
| M_B | M0 + 本体衍生特征（signal_*） | **主模型：本体是否产生增量信息？** |
| M_B_all | M0 + BDM + 本体特征 | 完整模型 |

### 4.2 关键检验

1. **AUC 比较**：DeLong检验 AUC(M_B) vs AUC(M0)
2. **特征重要性**：使用 SHAP 分解哪个本体特征贡献最大
3. **似然比检验**：比较嵌套模型 (M0 vs M_B) 的 -2LL 差异
4. **正则化后的稳健性**：使用 elastic-net 逻辑回归（l1 比率 = 0.5），观察哪些本体特征被选入最优模型

### 4.3 脆弱性分析

**"但如果本体特征不预测清算，概念框架还有用吗？"**

有。论文仍然成立作为——"DeFi中的信用本体不能从纯链上数据中有效导出——这说明信息生产需要一个观察者的隐性知识"。这是同等重要的结论，可发表在 MISQ 或 Organization Science 上。

---

## 5. 跨协议检验

### 5.1 可迁移性检验

**Aave → Compound**：将本体的类定义和规则从 Aave 复制到 Compound 的数据上，重新应用规则引擎生成特征。

**检验**：在 Compound 数据上运行相同的逻辑回归（M0 vs M_B）：
- 如果本体特征的系数方向和大小与 Aave 相似 → 证明 DeFi 的信用本体具有跨协议通用性
- 如果特征不显著 → 信用本体可能是协议特定的（"通用 DeFi 信用本体"的观念可能被过度简化了）

### 5.2 定性比较

除了定量的系数比较，还可以进行定性的比较：本体规则在两个协议上识别到相同比例的地址各信用类型吗？ 如果没有，是什么协议特有的特性（清算阈值、支持的抵押品、gas 模型）造成了差异？

---

## 6. 局限性与下一步

1. **本体构建中的主观性**：B 中定义"强意愿"的方法对个人的判断敏感。解决方案：(i) 由两人独立进行本体设计，然后比较重叠的部分；(ii) 对不同意向进行灵敏性分析（如调整"强意愿"的门槛）
2. **计算复杂度**：规则引擎的批处理可能数据密集——考虑使用 DuckDB 代替 pandas 用于内存受限的系统
3. **与 V4 的重叠**：BDM 的五个维度可能已经捕获了本体特征的线性组合。如果 M_B 不能超越 M1，需要诚实地报告这一点

---

*本技术方案的规则和参数均为初始方案，实际数值将在数据分析时根据经验修正。*
