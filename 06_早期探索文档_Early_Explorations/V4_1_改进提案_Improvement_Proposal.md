# V4_1 改进提案：前景理论框架下的 DeFi 借贷行为偏差与信用信号

**版本**：V4-1（基于 V4 盲点自检的改进版）
**日期**：2026-06-19
**性质**：课题提案——可执行的研究设计
**前置**：V4 探索稿 → 本稿修复两个致命盲点（决策锚缺失、主动/被动混淆）
**配套文件**：
- `deliverables/01_Dune查询模板_操作化说明.md`
- `deliverables/02_文献总表_RQ映射.md`
- `deliverables/03_主动vs被动_决策树.md`

---

## 〇、V4 → V4_1 的改进摘要

V4 探索稿的盲点自检识别出两个致命问题：

1. **决策锚缺失**（🔴 致命）：没有把"行为偏差有预测力"接到一个真实决策上
2. **主动 vs 被动混淆**（🔴 致命）：无法区分"借款人主动补救"和"清算人被动清算"

V4_1 的改进：

| 致命盲点 | V4 原稿 | V4_1 改进 |
|---------|---------|----------|
| 决策锚缺失 | "协议可基于纯链上行为构建动态风险定价"（模糊） | **福利量化**：把 ΔAUC 折算为"提前清算阈值 × BDM 分层保险费"导致的期望清算损失减少量 |
| 主动/被动混淆 | "补救行动"未区分发起者 | **完整决策树**（见配套文件 03）：6 类操作分类 + HF 上下文 + 时间窗口，严格区分 A1-A5（主动）、B1-B2（被动）、C1-C2（清算后） |

同时改进了：
- 参考点的 emic 定义：增加结构断点检测（Bai-Perron）作为备选参考点
- BDM 构念新颖性：加入"抵押品切换方向"（DeFi 独有维度）
- 文献覆盖：从 7 篇扩展到 17 篇，时间梯度满足要求

---

## 一、研究问题

### 1.1 核心问题

**在去中心化借贷协议中，借款人在清算阈值附近的行为是否系统性地偏离理性预期模型的预测（符合前景理论），且这种偏离是否包含超越传统风险指标的信用预测信息？其预测力的福利含义是什么？**

### 1.2 三个子问题

- **RQ1（行为层）**：DeFi 借款人在逼近清算阈值时，其**主动发起**的操作是否呈现前景理论预测的三个特征？
  - H1a（损失厌恶）：HF 下降时的补救幅度 > HF 上升同等幅度时的增险幅度（$\lambda > 1$）
  - H1b（参考点效应）：HF=1 附近补救行动概率/幅度呈现非线性加速增长
  - H1c（递减敏感性）：远离 HF=1 后，对同等 $|\Delta\text{HF}|$ 的反应递减

- **RQ2（信用层 + 决策锚）**：控制传统链上风险指标后，行为偏差指数（BDM）是否仍对清算风险有增量预测力？**如果协议将清算阈值从 HF=1.0 提前到 HF=1.05 并对 BDM 高分用户施以更高保险费，期望清算损失降低多少？**

- **RQ3（识别层）**：跨协议行为一致性是否包含超越单协议行为特征的信用预测增量？

---

## 二、理论框架与文献定位

### 2.1 前景理论在 DeFi 中的适用性论证

前景理论（Kahneman & Tversky, 1979）的核心预测——损失厌恶、参考点效应、递减敏感性——已在传统金融中获广泛支持。近年文献确认其在区块链场景的适用性：

- **Arshadi & Kim (2025)**：以太坊 PoS 验证者行为中检测到损失厌恶（$\lambda > 1$），证明前景理论框架在区块链激励中实证可行
- **Lyu (2026a)**：处置效应（前景理论的实现假说）在以太坊链上成立，使用 2020-2024 全量数据
- **Li, Delfabbro & King (2025)**：后悔与 FOMO 驱动加密投机，提供"损失域中冒险"的心理微观基础

**但**：没有一个研究在 DeFi **借贷**场景中系统性测试前景理论的全部三个核心预测。现有工作覆盖的是交易行为（Lyu, 2026a）或验证者行为（Arshadi & Kim, 2025），而非借贷行为。

### 2.2 DeFi 借贷行为的事实基础

已有实证确认清算阈值附近的异常行为：

- **Gadzinski & Liuzzi (2025)**：25,798 笔 Aave 清算事件分析，发现被清算后用户**增加**而非减少借贷——这违反了传统金融中"违约→退出"的预期，但与前景理论预测的"损失域中持续冒险"一致
- **Cornelli et al. (2025)**：$61.4B Aave V2 贷款分析，发现接近清算阈值的用户**故意选择波动性抵押品**——这违反了风险管理理性，但与前景理论的"风险偏好翻转"一致
- **Mu, Tovanich & Prat (2025)**：用户对清算风险的"关注度"存在异质性，不关注用户的清算概率 4 倍于关注用户——但本文未从前景理论框架出发

### 2.3 理论缺口

| 已有 | 未有 |
|------|------|
| 前景理论 × PoS 验证者（Arshadi & Kim, 2025） | 前景理论 × DeFi 借贷 |
| 处置效应 × 以太坊交易（Lyu, 2026a） | 损失厌恶 + 参考点效应 + 递减敏感性 × 借贷行为（三项联合检验） |
| 清算后行为描述（Gadzinski & Liuzzi, 2025） | 行为偏差 → 信用预测力的增量（超越传统风险指标） |
| 链上信用评分（Ghosh et al., 2024） | 行为偏差维度的信用信息（BDM 是否是已编码信息的重复？） |

---

## 三、经验设计

### 3.1 数据

- **主数据源**：Aave V2 + V3（Ethereum 主网），通过 Dune Analytics 提取
- **对照数据源**：Compound V2 + V3（跨协议验证用）、MakerDAO
- **时间窗口**：2020-01 至 2025-12（覆盖牛熊周期）
- **分析单元**：用户-时间窗口（主要在月度级别，RQ1 在交易级）
- **样本**：所有曾开仓借款的用户（预估 200K+ 地址）
- **HF 计算**：自计算，基于持仓快照 + Chainlink/USD 价格（Dune `prices.usd` 表，小时级粒度）

**数据验证**：使用 Flipside Crypto 和/或 Aave 官方 subgraph 交叉验证关键事件的提取一致性。

### 3.2 RQ1：前景理论行为检验

**参考点**：$HF = 1.0$（Aave V2 中 $HF < 1$ 触发清算）

**核心操作化改进**：严格区分主动与被动操作（详见配套文件 03）

| 前景理论预测 | 操作化 | 可证伪形式 |
|------------|--------|-----------|
| **H1a：损失厌恶** | 配对比较：HF 下降时 A1/A4 操作的 USD 幅度 vs HF 上升时 A3/A2 操作的 USD 幅度，控制 $\|\Delta\text{HF}\|$ 相同 | $\lambda \leq 1$ 则拒绝 |
| **H1b：参考点效应** | 非线性接近度设计：HF 在 (1.0,1.1] vs (1.1,1.2] vs (1.2,1.5] 区间内主动补救（A1/A4）的概率/幅度是否呈现**加速增长** | 补救概率/幅度对 $\|HF-1\|$ 的导数在 HF→1 时无加速则拒绝 |
| **H1c：递减敏感性** | 边际效应估计：补救行动幅度对 $\|HF-1\|$ 的二阶导数为负 | 二阶导数 $\geq 0$ 则拒绝 |

**备选参考点检验**（回应 emic 参考点批判）：
- 使用 Bai-Perron 结构断点检测，从数据中估计实际行为断点位置
- 如果数据驱动的断点不在 HF=1 附近，需重新审视参考点假设
- 同时检验 HF=1.2 和 HF=1.5 作为备选 emic 参考点

**控制变量**：
- Gas price（影响补救速度的可行性；Sadeghi & Feinstein, 2026）
- 用户总持仓量（大户 vs 小户；Bank of Canada, 2026）
- 抵押品波动性（波动资产 vs 稳定币）
- 闪电贷清算占比（如果过高，"主动补救窗口"可能极短）

### 3.3 RQ2：行为偏差的信用预测力 + 决策锚

**因变量**：未来 30 天内是否被清算（二元） / 清算损失金额（连续）

**核心自变量**：BDM（Behavioral Deviation Measure），由以下维度构成：

| BDM 维度 | 操作化 | 前景理论对应 | 传统金融有无对应物 |
|---------|--------|------------|-------------------|
| 补救超配度 | 实际加抵押/还款 USD / 理性模型推荐 USD | 损失厌恶 | 有（止损超额） |
| 参考点跳变度 | HF 穿越 1.1 时操作频率变化幅度 | 参考点效应 | 有（止损线行为） |
| **抵押品切换方向** | 逼近清算时是否切换到波动资产（0/1 + 切换 USD） | 递减敏感性+风险偏好翻转 | **无——DeFi 独有** |
| 清算后恢复模式 | 被清算后 30 天内活动恢复率 | 损失域持续冒险 | 有（revenge trading） |
| 闪电贷窗口非行动 | HF<1.5 期间无主动操作天数占比 | 风险感知钝化 | 部分（inattention） |

**赛马设计**：

| 模型 | 特征 | 目标 |
|------|------|------|
| M0：基线 | 当前 HF + 抵押率 | 基准 |
| M_act：活跃度 | 交易频次、账户年龄、持仓多样性 | 活跃度信息 |
| M_hf：HF 动态 | HF 路径特征（均值、波动率、趋势、最小值） | HF 信息 |
| M_BDM：行为偏差增强 | M_hf + BDM 五维度 | **主判据**：BDM 的增量 AUC |

**主判据**：$M_{BDM}$ 相对 $M_{hf}$ 有显著增量 AUC（DeLong 检验），证明行为偏差包含超越传统链上风险指标的信用信息。

#### 🎯 决策锚：福利量化

**关键改进**：把 ΔAUC 折算为具体决策的福利变化。

**决策场景**：Aave 协议考虑将清算阈值从 HF=1.0 提前到 HF=1.05，并对 BDM 高分用户（行为偏差大 → 清算风险高）收取更高的稳定费（borrow rate spread）。

**福利量化公式**：

$$\Delta W = \underbrace{P(\text{liquidation} | \text{BDM-high}) \cdot E[\text{bad debt}] \cdot \Delta P(\text{avoided})}_{\text{减少的坏账期望}} - \underbrace{E[\text{higher fee cost for BDM-high users}]}_{\text{增加的借贷成本}}$$

其中：
- $P(\text{liquidation} | \text{BDM-high})$：BDM 高分用户的清算概率（从 RQ2 的预测模型获得）
- $E[\text{bad debt}]$：单次清算的期望坏账金额（从历史数据计算，约为清算金额的 5-15%）
- $\Delta P(\text{avoided})$：提前清算阈值后避免的清算概率增量（需要模拟）
- 借贷成本增加：BDM 高分用户因更高稳定费而增加的成本

**报告**：如果 $\Delta W > 0$，说明 BDM 的预测力有正的福利含义；如果 $\Delta W \leq 0$，说明即使 BDM 有增量 AUC，其决策价值不足。

**失败判据**：若 $\Delta W \leq 0$（或 BDM 无增量 AUC），则 RQ2 否——行为偏差虽然存在（RQ1 可能成立），但不构成有效的决策依据。

### 3.4 RQ3：跨协议行为指纹与信用

**方法**：
1. 为每个用户在每个协议构建行为特征向量（操作频次、品类构成、时段分布、抵押品偏好、BDM 维度）
2. 跨协议匹配：基于行为向量的相似度识别跨协议同一用户（使用启发式规则 + 匹配算法）
3. 赛马：**单协议模型 vs 跨协议增强模型**，检验跨协议维度是否有独立增量

**诚实声明**：跨协议实体解析精度有限——"同人"与"同类人"不可区分。RQ3 的增量必须通过赛马证明，而非假设。

---

## 四、与 V3-3 的关系

| 维度 | V3-3 | V4_1 |
|------|------|------|
| 数据依赖 | UnusPay 私有映射 | Aave/Compound 公开链上数据 |
| 可复现性 | 零 | 完全 |
| 理论锚 | credit legibility（Scott/Fourcade） | prospect theory（Kahneman/Tversky） |
| 经验内核 | CVD 预测外部风险结果 | 行为偏差预测清算风险 + 福利量化 |
| 因变量困境 | 同源效度 | 清算是链上硬事件，无同源问题 |
| 分母困境 | $D_{sem}$ 自指 | 无——清算阈值客观 |
| 商业污染 | UnusPay 双重角色 | 无特定商业伙伴依赖 |
| 最大风险 | 外部结果不可得 | 行为偏差可能只是 HF 的另一种编码 |

**继承**：观察者相对性、赛马设计精神、$D_{port}$ 在 RQ3 中的纯链上重生

**断裂**：理论传统不同（政治社会学 → 行为经济学）；经验锚点不同（私有 → 公开）；定位更谦逊（"增量信息"而非"先于评分的对象"）

---

## 五、已完成的验证

### 5.1 Dune 数据可行性（✅ 已验证）

- Aave V2/V3 的借贷事件通过 Dune `lending.borrow` / `lending.supply` 表可获取
- `LiquidationCall` 事件的 `liquidator` 字段可直接区分清算人 vs 借款人
- 通过 JOIN `ethereum.transactions` 可获取 `tx.from`，判定交易发起者
- HF 需要自计算（Dune 不提供实时快照），但所需输入数据（持仓 + 价格）均可获取
- 详细的查询模板见配套文件 01

### 5.2 文献缺口确认（✅ 已确认）

- 17 篇文献的系统检索确认：**前景理论三核心预测在 DeFi 借贷中的系统检验 = 空白**
- 行为偏差 → 信用预测力的增量 = 空白
- 详细的文献总表见配套文件 02

### 5.3 主动/被动操作化（✅ 已设计）

- 6 类操作分类 + HF 上下文 + 时间窗口的完整决策树
- 5 个 BDM 维度（含 DeFi 独有的"抵押品切换方向"）
- 详细的决策树见配套文件 03

---

## 六、待执行的验证（PoC）

### 6.1 最小可行性验证（1-2 周内）

| 验证项 | 目的 | 方法 |
|-------|------|------|
| Dune PoC 查询 | 确认数据可提取性 + 样本量 | 在 Dune 执行配套文件 01 中的查询 1-3 |
| 闪电贷清算占比 | 评估"主动补救窗口"是否足够 | 执行配套文件 01 中的闪电贷占比查询 |
| HF 自计算可行性 | 确认自计算 HF 的精度和复杂度 | 对 100 个用户计算 1 个月的 HF 路径 |
| 参考点 emic 检验 | 检验 HF=1 是否为实际行为断点 | 对 PoC 数据做 Bai-Perron 断点检测 |
| Dune vs Flipside 交叉验证 | 检查数据管道偏差 | 对同一时间段的关键事件做双源比对 |

### 6.2 如果 PoC 通过

- 正式撰写 RQ1 的预注册（pre-registration），锁定分析方案
- 构建 HF 计算管道（Python + Dune API）
- 开始 V3-3 与 V4_1 的定位文档（明确投递期刊、理论贡献类型）

---

## 七、参考文献（检索获得，按时间倒序）

1. Spadea & Seneviratne (2026). From Risk to Rescue: An Agentic Survival Analysis Framework for Liquidation Prevention. arXiv.
2. Sadeghi & Feinstein (2026). Liquidation Dynamics in DeFi and the Role of Transaction Fees. arXiv.
3. Sevim (2026). Interoperability Effects: Extending DeFi Lending Risk Models to Multi-Chain Environments. arXiv.
4. Bank of Canada (2026). DeFi Lending: Returns, Leverage, and Liquidation. Working Paper.
5. Lyu (2026a). The Investment Uncanny Valley. *J. Innovative Research*, 4(1).
6. Lyu (2026b). Disposition Effect on Ethereum. *Financial Sciences*, 31(1).
7. Li, Delfabbro & King (2025). Investigating the Role of Regret, FOMO and Financial Literacy in Cryptocurrency Speculation. *Int'l J. Mental Health and Addiction*.
8. Arshadi & Kim (2025). When Incentives Feel Different: A Prospect-Theoretic Approach to Ethereum's Incentive Mechanism. *Electronics*, 14(24).
9. Bartoletti & Lipparini (2025). A theory of Lending Protocols in DeFi. arXiv.
10. Mu, Tovanich & Prat (2025). Do You Care About Your Positions? IEEE ICBC 2025.
11. Cornelli, Gambacorta, Garratt & Reghezza (2025). Why DeFi lending? Evidence from Aave V2. *J. Financial Intermediation*, 63(C).
12. Gadzinski & Liuzzi (2025). Do liquidations discourage lending in DeFi? *Economics Letters*, 155.
13. Ghosh, Datta, Aggarwal, Sinha & Sengupta (2024). On-Chain Credit Risk Score in DeFi. arXiv.
14. Kellerman & Seddon (2024). Into the ether or the state? Legibility theory and the cryptocurrency markets. *Business and Politics*, 26(3).
15. OECD (2023). DeFi Liquidations: Volatility and Liquidity.
16. Qin, Zhou & Gervais (2021). An Empirical Study of DeFi Liquidations.
17. Kahneman & Tversky (1979). Prospect Theory: An Analysis of Decision under Risk. *Econometrica*, 47(2).