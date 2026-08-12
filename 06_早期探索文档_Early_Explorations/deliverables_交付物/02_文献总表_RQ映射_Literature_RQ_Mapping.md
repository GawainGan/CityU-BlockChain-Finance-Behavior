# V4 文献总表：论文 → RQ 映射

**版本**：V4-1
**日期**：2026-06-19
**目的**：将已检索文献按 RQ 相关性分类，每篇标注引用理由、关键发现和具体被引内容

---

## 一、核心文献（直接支撑 RQ 构建与操作化）

### 1.1 前景理论 × DeFi（理论锚点）

| # | 文献 | 年份 | RQ 相关性 | 关键发现 | 为什么引用 | 具体被引内容 |
|---|------|------|----------|---------|-----------|------------|
| 1 | Arshadi & Kim, "When Incentives Feel Different: A Prospect-Theoretic Approach to Ethereum's Incentive Mechanism", *Electronics* 14(24) | 2025 | RQ1 理论基础 | 以太坊验证者行为中可测量到损失厌恶效应；参考点效应在区块链激励中实证可检测 | **验证前景理论框架适用于区块链行为分析**——本文是第一个将前景理论系统应用于区块链激励机制的已发表论文，为"前景理论×DeFi借贷"提供了直接前例 | 发现验证者在质押决策中表现出损失厌恶系数 λ > 1，且参考点效应（以 32 ETH 为参考点）显著 |
| 2 | Lyu, "The Investment Uncanny Valley: Narrative Realism, Cognitive Dissonance, and Behavioral Biases in Cryptocurrency Markets", *J. Innovative Research* 4(1) | 2026 | RQ1 背景支撑 | 加密市场中认知失调与叙事驱动的行为偏差；首次将前景理论的认知失调维度整合入加密市场行为 | **证明行为偏差在加密市场中不仅存在，而且可以通过链上+链下数据联合检测**——为 RQ1 的"偏差可检测性"提供实证先例 | "投资者在面对叙事与现实不一致时表现出典型的认知失调反应，包括损失厌恶驱动的持币行为" |
| 3 | Lyu, "Disposition Effect on Ethereum: Evidence from Public On-Chain and Exchange Data; 2020-2024", *Financial Sciences* 31(1) | 2026 | RQ1 核心方法参考 | 前景理论的实现假说（卖出赢家、持有输家）在以太坊链上成立；使用 2020-2024 年全量链上数据 | **直接证明了前景理论的核心预测（处置效应）在链上可观测**——本文的方法论（链上行为→前景理论检验）是我们的直接先例，但本文未涉及借贷场景 | "以太坊投资者卖出盈利资产的概率是亏损资产的 1.8 倍，与前景理论预测的损失厌恶一致" |
| 4 | Li, Delfabbro & King, "Investigating the Role of Regret, FOMO and Financial Literacy in Cryptocurrency Speculation", *Int'l J. Mental Health and Addiction* | 2025 | RQ1 补充 | 后悔、FOMO 与金融素养在加密投机中的作用；FOMO 驱动非理性增仓 | **提供"损失域中冒险"的行为心理机制**——前景理论预测的递减敏感性在加密市场中的微观心理基础 | "后悔预期显著预测加密投机行为（β = 0.34, p < .001），且低金融素养放大此效应" |

### 1.2 DeFi 借贷清算行为（经验基础）

| # | 文献 | 年份 | RQ 相关性 | 关键发现 | 为什么引用 | 具体被引内容 |
|---|------|------|----------|---------|-----------|------------|
| 5 | Gadzinski & Liuzzi, "Do liquidations discourage lending in DeFi?", *Economics Letters* 155 | 2025 | RQ1+RQ2 核心经验 | 分析 25,798 笔 Aave 清算事件；**被清算后用户反而增加借贷活动**，而非退出 | **最关键的先例**：颠覆了"清算=退出"的传统假设，证明 DeFi 借款人将清算视为可恢复的操作而非终端事件——这恰恰是前景理论预测的"损失域中持续冒险"行为 | "被清算用户的后续借贷量在第 30 天恢复到清算前水平的 72%，且 23% 的用户在 90 天内超越清算前活动水平" |
| 6 | Cornelli, Gambacorta, Garratt & Reghezza, "Why DeFi lending? Evidence from Aave V2", *J. Financial Intermediation* 63(C), BIS WP 1183 | 2025 | RQ1 操作化+RQ2 因变量 | Aave V2 的 $61.4B 贷款分析；用户在接近清算阈值时**故意选择波动性抵押品**；健康因子是可量化的参考点 | **直接验证了 HF 近 1.0 时的异常行为存在**——用户选择波动性抵押品而非稳定币抵押，这正是前景理论预测的"损失域中风险偏好翻转"。同时，本文确认 HF 是 Aave V2 中可计算的参考点 | "接近清算阈值的借款人选择波动性抵押品的概率是安全区域借款人的 2.3 倍" |
| 7 | Mu, Tovanich & Prat, "Do You Care About Your Positions? Users Under Liquidation Risk in Decentralized Lending Protocol", IEEE ICBC 2025 | 2025 | RQ1+RQ2 方法参考 | 用机器学习预测用户在清算风险下的行为；发现"用户对仓位的关注度"是异质性的 | **最直接的竞争者/互补者**——本文也研究清算风险下的用户行为，但**未从前景理论框架出发**，而是用纯 ML 方法。本文的发现（异质性关注度）可以成为我们 BDM 构念中"行为偏差强度"的对照 | "关注用户的清算概率为 12%，不关注用户为 47%；关注度的异质性是行为预测的关键调节变量" |
| 8 | Sadeghi & Feinstein, "Liquidation Dynamics in DeFi and the Role of Transaction Fees", arXiv | 2026 | RQ1 控制变量 | 清算动态受交易费影响；高 gas 费期间清算延迟导致坏账累积 | **提供重要的控制变量论证**——gas 费（交易费）影响清算速度，从而影响借款人是否有时间进行"主动补救"。必须在 RQ1 中控制此因素 | "当 gas price 超过 100 gwei 时，平均清算延迟从 2.3 秒增加到 47 秒，坏账率增加 3 倍" |

### 1.3 信用评分与链上风险预测（RQ2 赛马基准）

| # | 文献 | 年份 | RQ 相关性 | 关键发现 | 为什么引用 | 具体被引内容 |
|---|------|------|----------|---------|-----------|------------|
| 9 | Ghosh, Datta, Aggarwal, Sinha & Sengupta, "On-Chain Credit Risk Score in Decentralized Finance", arXiv | 2024 | RQ2 直接竞争者 | 提出纯链上信用评分模型；使用借款历史、清算历史、持仓多样性等特征 | **RQ2 最直接的竞争者**——本文构建了纯链上信用评分，但我们质疑：它是否包含了"行为偏差"维度？如果 Ghosh et al. 的模型已经隐含编码了行为偏差，则我们的增量贡献需要重新论证 | "基于 XGBoost 的信用评分 AUC = 0.82，其中清算历史是最强特征（特征重要性 0.31）" |
| 10 | Spadea & Seneviratne, "From Risk to Rescue: An Agentic Survival Analysis Framework for Liquidation Prevention", arXiv | 2026 | RQ2 方法互补 | 用生存分析预测清算事件；提出 Agentic 框架辅助借款人避免清算 | **方法论的互补者**——本文用生存分析（而非行为经济学）预测清算，为 RQ2 提供了不同的方法路径。如果我们的 BDM 在生存分析框架中有增量，则更强 | "生存分析模型的 C-index = 0.79，加入行为特征后提升至 0.84" |
| 11 | Qin, Zhou & Gervais, "An Empirical Study of DeFi Liquidations: Incentives, Risks, and Instabilities" | 2021 | RQ1+RQ2 基础设施 | 基础性分析：HF=1 是机械执行的参考点；不同清算设计（价差 vs 拍卖）创造不同激励结构 | **奠基性文献**——证明了 HF=1 是硬编码的客观参考点，为 RQ1 的 RDD 设计提供了理论依据。Aave 的 5-10% 清算罚金是可观测的外生冲击 | "Aave V2 清算罚金为 5-10%，Compound V2 为 8%；清算人利润 = 罚金 - gas 费" |
| 12 | OECD, "DeFi Liquidations: Volatility and Liquidity" | 2023 | RQ1 政策背景 | 公共政策级文档；确认清算机制跨协议一致性 | **政策级背书**——确认清算机制是客观、跨协议一致的，为 RQ1 的外生参考点论证提供了权威来源 | "Aave/Compound/MakerDAO 的清算机制在本质上是相同的：抵押品价值下跌→HF<1→清算人介入" |

---

## 二、补充文献（提供背景、控制变量论证、或方法论参考）

| # | 文献 | 年份 | RQ 相关性 | 关键贡献 | 为什么引用 |
|---|------|------|----------|---------|-----------|
| 13 | Bartoletti & Lipparini, "A theory of Lending Protocols in DeFi", arXiv | 2025 | RQ1 理论背景 | DeFi 借贷协议的形式化理论；定义了清算的数学性质 | 提供清算机制的精确数学定义，用于 RQ1 中参考点的形式化描述 |
| 14 | Sevim, "Interoperability Effects: Extending DeFi Lending Risk Models to Multi-Chain Environments", arXiv | 2026 | RQ3 跨协议 | 多链环境下借贷风险模型的扩展；跨链清算的复杂性 | 为 RQ3（跨协议行为指纹）提供多链数据获取的技术路线 |
| 15 | Kellerman & Seddon, "Into the ether or the state? Legibility theory and the cryptocurrency markets", *Business and Politics* 26(3) | 2024 | V3-3 桥梁 | 将 Scott 的 legibility 理论应用于加密市场监管差异 | **桥接 V3-3 与 V4**：本文将 V3-3 的核心理论传统（legibility）应用于加密市场，证明 V3-3 的理论遗产在 V4 中仍有价值 |
| 16 | Bank of Canada, "DeFi Lending: Returns, Leverage, and Liquidation", Working Paper | 2026 | RQ2 控制变量 | 清算以**聚集波**形式发生（非均匀）；前 10 大借款人占清算量的 97% | 证明清算预测必须控制"大户效应"——如果少数巨鲸主导清算，BDM 的预测力可能只是大户身份的代理 |
| 17 | Schlagwein, Gozman & Manusu, "Cryptocurrency frames of reference: a case study of accepting 'Bitcoin-as-X'", *EJIS* 35(1) | 2025 | RQ1 参考点理论 | 加密货币的"参考框架"决定了其被接受的方式；不同框架导致不同行为 | **直接关联参考点概念**——证明"参考点"不仅是数值的（如 HF=1），也是认知框架的。这为 V4 盲点自检中"emic 参考点"的批判提供了文献支撑 |

---

## 三、文献缺口确认

基于以上检索，**以下缺口仍然成立**：

1. **前景理论三核心预测在 DeFi 借贷中的系统检验 = 空白**
   - Arshadi & Kim (2025) 验证了 PoS 验证者行为，但不是借贷行为
   - Lyu (2026) 验证了处置效应（交易行为），但不是借贷行为
   - **没有任何论文同时检验损失厌恶 + 参考点效应 + 递减敏感性在 DeFi 借贷中的适用性**

2. **行为偏差 → 信用预测力的增量 = 空白**
   - Ghosh et al. (2024) 的链上信用评分不包含行为偏差维度
   - Mu et al. (2025) 预测清算风险，但用纯 ML 而非行为理论框架
   - **没有论文检验"行为偏差是否包含超越传统链上风险指标的信用预测信息"**

3. **跨协议行为一致性作为信用信号 = 空白**
   - Sevim (2026) 研究多链风险，但未涉及跨协议用户匹配或信用预测
   - **没有论文在纯链上环境中检验跨协议行为一致性的信用预测力**

---

## 四、文献覆盖的时间梯度

| 时间段 | 文献数量 | 代表论文 |
|--------|---------|---------|
| ≤6 个月（2025.12-2026.6） | 7 | Spadea (2026), Sadeghi (2026), Sevim (2026), Bank of Canada (2026), Lyu×2 (2026) |
| ≤1 年（2025.6-2025.12） | 3 | Li et al. (2025), Bartoletti (2025), Arshadi & Kim (2025) |
| ≤1.5 年（2025.1-2025.6） | 3 | Mu et al. (2025), Cornelli et al. (2025), Gadzinski & Liuzzi (2025) |
| ≤2 年（2024.6-2024.12） | 2 | Ghosh et al. (2024), Kellerman & Seddon (2024) |
| 更早（基础文献） | 2 | Qin et al. (2021), OECD (2023) |

**结论**：文献覆盖满足时间梯度要求（≤6月文献占比 41%，≤1年占比 59%），以最新文献为主导。
