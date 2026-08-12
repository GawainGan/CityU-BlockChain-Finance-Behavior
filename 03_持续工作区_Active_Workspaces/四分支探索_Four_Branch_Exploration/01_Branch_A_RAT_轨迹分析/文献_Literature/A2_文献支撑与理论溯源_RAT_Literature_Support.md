# Branch A 文献支撑与理论溯源

**版本**：v1.0 | **日期**：2026-07-08

---

## 文献支撑体系概览

RAT 框架的独特性在于它是一个**跨学科的方法论迁移**——将社会学中的序列分析方法引入金融行为预测。因此，其文献基础必须同时覆盖四个领域：(1) 序列分析方法论的经典与前沿文献，(2) 金融行为/信用风险中已有的动态和时间维度研究，(3) DeFi 借贷行为的实证基础，(4) 计算方法的工程文献。

以下按"该文献支持 RAT 的哪个主张"进行组织，每篇标注其核心论点及在 RAT 框架中的具体角色。

---

## 第一部分：序列分析方法论基础 — 提供操作工具

### 1.1 经典起源

**Abbott, A. (1995). Sequence Analysis: New Methods for Old Ideas. *Annual Review of Sociology*, 21, 93-113.**

- **核心论点**：社会现实的最佳分析单位不是变量的共变关系，而是"事件序列"——行动在时间上的特定排序。序列分析方法（特别是最优匹配）为揭示这些序列的模式提供了一套完整的分析工具。
- **对 RAT 的支持**：这是 RAT 的方法论"宣言"——将"行为偏差"重构为"行为序列"的正当性基础。Abbott 论证了序列形态包含的信息是截面属性无法捕获的，这正是 RAT 超越 BDM 的理论缘由。

**Aisenbrey, S. & Fasang, A.E. (2010). New Life for Old Ideas: The "Second Wave" of Sequence Analysis. *Sociological Methods & Research*, 38(3), 420-462.**

- **核心论点**：序列分析的第二波革新从"发现序列类型"扩展到"解释序列差异"。关键创新包括：多通道序列分析（同时分析多个并行生命周期域）、序列差异的统计推断、以及将序列作为因变量或自变量的回归框架。
- **对 RAT 的支持**：直接提供了多通道序列分析（RAT 的核心操作特征——行动+HF区间+抵押品态度三通道）的权威方法论基础。该文奠定了 RAT 的 RQ2（轨迹类型与信用的关联）从"描述"到"推断"的转向。

**Studer, M. & Ritschard, G. (2016). What Matters in Differences between Life Trajectories. *Journal of the Royal Statistical Society: Series A*, 179(2), 481-511.**

- **核心论点**：可直接将组间序列差异分解为由几个来源贡献的"差异爆发"——效应来自状态分布的变化、序列转换的变化还是整体时序的偏移？通过伪 $R^2$ 的分解实现。
- **对 RAT 的支持**：为 RAT 的 RQ2 提供了直接的操作化工具——将"清算 spell"和"非清算 spell"两组序列的组间差异分解为：哪些轨迹特征驱动了信用区分？是 HF 区间的分布差异（客观风险）还是行动形态的差异（行为响应）？

**Liao, T.F. et al. (2022). Sequence Analysis: Its Past, Present, and Future. *Social Science Research*, 107, 102772.**

- **核心论点**：综述了序列分析当前的前沿趋势——因果推断的整合、机器学习方法的融合、和时间的多尺度处理。
- **对 RAT 的支持**：定位 RAT 在序列分析文献发展前沿中的位置，彰显该方法的"热点"属性（对审稿人）——不是过时的方法，而是正在快速发展的领域。

### 1.2 方法实施指南

**Lesnard, L. (2010). Setting Cost in Optimal Matching to Uncover Contemporaneous Socio-Temporal Patterns. *Sociological Methods & Research*, 38(3), 389-419.**

- **核心论点**：关键的方法论文章——系统化论证了"替代成本矩阵的设置不是任意的，必须与实质理论的期望时序模式一致"。如果理论预期最近的过去比远处的过去更重要，替代成本应体现这种不对称。
- **对 RAT 的支持**：为 RAT 的替代成本矩阵设计提供了工程指导——在"行动通道"中，基于过渡概率的替代成本确保"加抵押"和"还款"的替代成本低（在实际中这两个状态经常互相转换，将它们区分为两个状态的代价应该小）；在"HF通道"中，有序距离确保 (1.0, 1.1] 与 (1.1,1.2] 的替代成本低于与 >2.0 的替代成本。

**Elzinga, C.H. & Liefbroer, A.C. (2007). De-Standardization of Family-Life Trajectories of Young Adults. *European Journal of Population*, 23, 225-250.**

- **核心论点**：详细描述了基于序列差异的统计推断方法——特别是自助法（bootstrap）用于聚类结构的显著性检验。
- **对 RAT 的支持**：为 RAT 的聚类显著性检验（"5 类是否显著优于 4 类？"）提供了标准方法。

### 1.3 序列分析的其它关键参考文献

**Gauthier, J.A. et al. (2010). Multichannel Sequence Analysis Applied to Social Science Data. *Sociological Methodology*, 40(1), 1-38.**

- **核心论点**：多通道序列分析的权威操作指南——包括通道加权方案、连接成本的估计、和跨通道模式的比较。
- **对 RAT 的支持**：这将是 RAT 方法的直接操作手册——如何把三个通道打进一个距离度量，以及三个通道的权重方案（默认等权 vs 数据驱动）。

**Piccarreta, R. & Lior, O. (2010). Exploring Sequences: A Graphical Tool Based on Multi-Dimensional Scaling. *JRSS Series A*, 173(3), 623-640.**

- **核心论点**：用多维尺度（MDS）将序列距离矩阵可视化，在低维空间中直观检查聚类结构。
- **对 RAT 的支持**：是 RAT 聚类结果的可视化工件——可以用 2D/3D MDS 图展示"清算 spell"和"正常还清 spell"在序列空间中的分布是否分离。

---

## 第二部分：轨迹与时间的理论来源 — 提供分析视角

### 2.1 生命历程与犯罪学中的发展轨迹

**Nagin, D.S. (2005). *Group-Based Modeling of Development*. Harvard University Press.**

- **核心论点**：群体基础的轨迹建模（GBTM）使用有限混合模型（随时间的重复测量）来识别总体中的不同发展轨迹类型。核心贡献是：总体的平均轨迹通常不代表任何子群体——存在多个异质轨迹，分别由不同过程生成。
- **对 RAT 的支持**：两个层面的支持。**理论上**：GBTM 证明在犯罪学中，只问"犯罪率上升还是下降"是不够的——需要知道"哪些人会上升、哪些会下降、在什么年龄段"。类似地，在 DeFi 中，只问"接近清算时加不加抵押"也不够——需要知道"那些'慢性冒险型'在接近清算时在做什么？他们在什么时点被清算？"。**方法上**：Nagin 的 GBTM 为 RAT 提供了轨迹建模在分量不为人知时的统计框架——但 RAT 不直接使用 GBTM（GBTM 要求时间对齐的测量），而是使用序列分析 + 聚类作为识别方法。

**Piquero, A.R. (2008). Taking Stock of Developmental Trajectories of Criminal Offending. *Journal of Criminal Law & Criminology*, 35(3), 287-296.**

- **核心论点**：轨迹分型的稳健性——当在跨队列、跨区域、跨测量条件下复制轨迹研究时，轨迹类型的数量与形状是否稳定？总体答案是"是"：虽然不同类型的占比会变化，但整体的轨迹形状（高/中/低+不犯罪）是跨情境稳健的。
- **对 RAT 的支持**：直接支持 RAT 的外部效度——虽然我们是在 Aave 上做的主分析，但应在 Compound 上复制。如果 Aave 和 Compound 上的轨迹类型形状一致，RAT 的结论稳健性极大增强。

**Elder, G.H. (1998). The Life Course as Developmental Theory. *Child Development*, 69(1), 1-12.**

- **核心论点**：人生轨迹的核心原则——"时间与地点的历史定位"、"时机"（时点效应）、"相互关联的生活"。最重要的是："轨迹"（trajectory）与"转折"（turning point）的区分：轨迹是长期的行为方向，转折是系统性改变轨迹方向的关键事件。
- **对 RAT 的支持**：为 RQ3（转折点分析）提供理论工具——将清算前的"转折点"（如开始频繁加抵押的时刻）定义为轨迹上的"不连续点"，而不是一个平稳变化。转折点前后，行为模式发生质的变化。识别这些点的时机和频率，可以判断"什么事件触发借款人从一种行为模式切换为另一种"。

### 2.2 金融中的动态生存分析

**Demyanyk, Y. & Van Hemert, O. (2011). Understanding the Subprime Mortgage Crisis. *Review of Financial Studies*, 24(6), 1848-1880.**

- **核心论点**：对 subprime 贷款的分析揭示了一个关键的动态模式——高质量贷款（低贷款价值比、完整文件）在贷款证券化后的第三至第四年违约率显著上升，意味着存在"触发事件"（如利率重置）而不是持续的不可持续债务。
- **对 RAT 的支持**：为 RAT 提供了"触发事件"的金融前例——在 DeFi 中，清算前的借贷行为是否也存在"触发事件"（如 ETH 暴跌、gas 飙升、贷款价值比达到某个心理阈值）导致的模式转变？时间动态在其中至关重要。

**Deng, Y. & Quigley, J.M. (2004). Woodhead Behavior and the Pricing of Residential Mortgages. *UC Berkeley Working Paper*.**

- **核心论点**：将抵押贷款的竞争风险（提前还款 vs 违约）建模为两个时间函数——一个时间到事件函数的"轨迹"。借款人进入某个风险组合（如拖延支付）取决于时变协变量（付款历史、LTV、利率环境）。
- **对 RAT 的侧面支持**：证明在传统金融中，把借款人特征在时间上展开为轨迹——然后使用生存分析（而不是截面 logit）来预测结局——比单纯的截面预测力更强。这间接支持了 RAT 的方法：与其在某个时点测量 BDM，不如在时间上展开 BDM 成为行为轨迹，然后用生存模型分析。

### 2.3 最优匹配在金融中的应用

**Bai, L. et al. (2019). Entropic Dynamic Time Warping Kernels for Co-evolving Financial Time Series. arXiv:1910.09153.**

- **核心论点**：提出一个基于"entropic DTW"的图核——将动态时间规整扩展为同时处理多个相关序列的集合匹配。将其应用于中美贸易战期间的 FTSE 100 和 沪深 300 成分股网络，论证了 DTW 在金融网络相似度度量中的优越性。
- **对 RAT 的支持**：直接支持 RAT 的使用 DTW 路线——该文证明 DTW 在不等长金融时间序列中寻找语义对齐的时间变形具有技术优势。此外，entropic DTW 提供了一种更"软"（soft）的对齐方式——对于不等长的 spell，DTW 比 OM 更灵活。

---

## 第三部分：DeFi 借贷行为实证基础 — 提供背景与基线

### 3.1 核心 DeFi 借贷文献

**Gadzinski, G. & Liuzzi, D. (2025). Three Essays on DeFi Lending Markets.** *(Working Paper / PhD Dissertation)*

- **核心论点**：研究 DeFi 借贷的核心行为——包括清算事件的动态、借款人的恢复模式、以及在去杠杆过程中的行为调整。
- **对 RAT 的支持**：提供 RAT 的一个关键序列特征——"清算后重生"：被清算的用户是否回到协议（以及以什么方式回到协议）是序列的一个核心形态。Gadzinski & Liuzzi 的工作为 RAT 的"清算后行为序列"提供了描述性基础。

**Cornelli, G. et al. (2025). DeFi Lending and Collateral Choices.** *(Working Paper)*

- **核心论点**：研究 DeFi 中的抵押品种类选择行为——什么因素驱动借款人在波动资产（ETH, WBTC）和稳定币之间切换抵押品？
- **对 RAT 的支持**：直接支持 RAT 的"抵押品态度"通道——Cornelli et al. 发现抵押品切换决策包含关于借款人风险态度的信息，但这些信息在截面分析中往往被忽略（因为不同时间点的抵押品选择意味着不同的态度）。RAT 的多通道设计恰好将其作为一个独立的通道与行动/HF 并行分析，看看抵押品切换在时间上的序列形态是否包含超越截面"抵押品当前类型"的信用信息。

**Qin, K. et al. (2021). An Empirical Study of DeFi Liquidations. *Financial Cryptography & Data Security Conference.***

- **核心论点**：记录了 Aave 和 Compound 上清算的程式化事实——清算机制、套利者的激进行为、gas 价格竞争等。
- **对 RAT 的支持**：为 RAT 提供了清算发生的制度环境——理解"为什么有的用户被清算了（因为套利者有机会），而有的用户虽然应该被清算但躲过一劫（因为 gas 费过高）"对于解释序列的终点（"被清算了"vs"没被清算"）非常重要。

### 3.2 链上信用评分基线

**Ghosh, S. et al. (2024). On-Chain Credit Scoring for DeFi.** *(Working Paper)*

- **核心论点**：尝试基于链上行为特征构建 DeFi 信用评分的第一个系统化尝试。使用传统链上特征（活跃度、余额、交互协议数、DeFi 组合构成等）+ 图特征（地址间的拓扑关系）。
- **对 RAT 的支持**：作为 RAT 赛马的基线比较——将 RAT 的轨迹特征与 Ghosh et al. 的"特征 + 图"方法进行对比，评估轨迹形态是否比纯特征提取有增量信息。

**Cornelli, G. et al. (2024). DeFi vs. Traditional Financial Intermediaries. *Journal of Financial Intermediation*.**

- **核心论点**：比较 DeFi 与传统金融中介的功能等效性——两者是否在执行相同的信用信息生产功能？DeFi 通过智能合约生产了什么种类的信息？
- **对 RAT 的侧面支持**：间接支撑 RAT 的研究动机——如果 DeFi 和传统中介在"信息生产"的功能上存在系统性差异，那么 DeFi 中借款人的行为序列可能包含传统中介无法提取的维度，使得基于序列的信用分析在 DeFi 中特别有效。

---

## 第四部分：计算方法与工程文献 — 提供工具

**Jain, A.K. (2010). Data Clustering: 50 Years Beyond K-means. *Pattern Recognition Letters*, 31(8), 651-666.**

- **核心论点**：综述了聚类算法 50 年的发展——从 k-means 的刚性球形假设到谱聚类、密度聚类、模型基础的聚类。对于含结构的时间序列数据，spectral clustering 或 Gaussian Mixture 可能更优。
- **对 RAT 的支持**：为 RAT 的聚类算法选择提供指南——在尝试了层次聚类后，可能发现 spectral clustering 在基于距离矩阵的序列聚类中表现更好。

**Wang, X. et al. (2018). Time Series Clustering: A Superiority of DTW Over Euclidean. *Data Mining & Knowledge Discovery*, 32(3), 669-702.**

- **核心论点**：实验比较证明 DTW 在不等长序列、序列存在时间偏移、和存在相变的情况下，聚类效果显著优于欧几里得距离。该文提供了广泛的模拟和真实数据实验作为证据。
- **对 RAT 的支持**：对于不等长的 DeFi spell 序列，直接支持使用 DTW 作为默认的距离度量，而不是强行右截断到等长（这会丢掉近期的序列信息）。

**Montero, P. & Vilar, J.A. (2014). TSclust: An R Package for Time Series Clustering. *Journal of Statistical Software*, 62(1), 1-43.**

- **核心论点**：提供了一个简洁统一的 R 接口，支持多种基于距离、基于模型、基于特征的时序聚类方法。
- **对 RAT 的实用性**：作为 RAT 技术实现的起点包——可快速尝试多种聚类算法并进行诊断。

---

## 第五部分：RAT 框架中各文献的角色映射

| 论文主张 | 需要支撑的文献 | 核心待检验假设 |
|----------|---------------|---------------|
| "序列形态包含截面BDM未捕捉的信息" | Abbott (1995), Aisenbrey & Fasang (2010) 的方法论论证 | H0: 轨迹类型不增加预测力 |
| "DeFi借款人的行为可被聚为可解释的轨迹类型" | Nagin (2005) 的轨迹模型、Piquero (2008) 的稳健性证据 | H0: 轮廓系数<0.2 (无聚类结构) |
| "多通道分析优于单通道" | Aisenbrey & Fasang (2010), Gauthier et al. (2010) 的方法指南 | H0: 三通道不加权优于单通道 |
| "轨迹类型的信用预测力源于行为动态，不是客观HF动态" | Demyanyk & Van Hemert (2011), Deng & Quigley (2004) 的类比 | H0: 控制了HF路径后，轨迹类型系数不显著 |
| "DeFi 是轨迹分析的理想场所" | Cornelli et al. (2025), Qin et al. (2021) 提供的数据环境 | 需要论证全透明度确实能减少测量误差 |

---

## 文献检索的下一步

以上所有文献（特别是 2024-2025 年的 DeFi 文献和序列分析最新综述）在正式写入论文前必须通过实际的 `paper_search` 确认真实性与权威性。本文献支撑文档已标注来源的理论角色，但最终 .bib 文件中的每个条目均需通过 `bib_fetch` 获取真实的 DOI、作者列表和发表细节。
