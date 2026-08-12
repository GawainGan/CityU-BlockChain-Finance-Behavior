# Branch D 文献支撑与理论溯源

**版本**：v1.0 | **日期**：2026-07-08

---

## 文献支撑体系概览

Branch D 的文献需求最为简约（因为不依赖任何强理论锚），分为三类：(1) 实证工作的格式文献——支持"我们需要一个描述性的、可发表的经验发现"；(2) DeFi 借贷行为的经验基线——提供赛马比较对象；(3) 方法论——赋予结果的信度。

---

## 第一部分：实证论文的格式——支持"这值得发表"

### 1.1 描述-发现传统的合法性

**Hamermesh, D.S. (2000). The Craft of Labormetrics. *Industrial and Labor Relations Review*, 53(3), 363-380.**

- **核心论点**："计量经济学应用的五个戒律"之一是：在复杂的结构模型之前，应该先提供描述性的、探索性的经验事实作为基础。这是一篇关于"不要先建模，先观察"的权威陈述。
- **对 Branch D 的支撑**：最直接支持 D 的文献。Hammermesh 的论点——"如果不知道基本事实，你将建立关于幻觉的模型"——完全适用于 D 的设计：在任何人理论化"为什么行为模式预测清算"之前，我们需要先知道它们是否真的预测清算。

**Lewbel, A. (2019). The Identification Zoo: Meanings of Identification in Econometrics. *Journal of Economic Literature*, 57(4), 835-903.**

- **核心论点**：系统梳理了计量经济学中"识别"的多重含义，区分了"结构的"（structural）和"非结构的"（descriptive/statistical）识别。这篇文章的核心信息是：一个发现的科学价值不取决于它的"结构深度"（即是否与一个深层理论联系起来），而取决于它是否构成一个稳固的、可复制的经验规律。
- **对 Branch D 的支撑**：直接反驳"没有理论贡献=不科学"的常见批评。D 回应：它的贡献是**非结构性的经验发现的识别**。这个发现有两个可能的理论解释，但它的价值——作为一个可检验的、可复制的、有政策相关性的规律——**与其理论解释的质量是分开的**。

**Christensen, G. & Miguel, E. (2018). Transparency and Reproducibility in Economics Research. *Journal of Economic Literature*, 56(3), 920-980.** (综述)

- **核心论点**：实证经济学的"可复制性危机"的分析——包括多种统计偏见（出版偏见、p 值黑客、结果报告的不透明性等）和解决方案（预注册、详细的分析计划、否定的结果不应该是"文件抽屉"中的过客）。
- **对 Branch D 的支撑**：为该方向的预注册和透明性计划提供文献支持。Branch D 是四个方向中最适合做预注册的——因为在分析前已经明确了所有四个 RQ 的全部检验判据。这种"预先规定失败判据"的设计是 D 在方法学严谨性上的主要资产。

### 1.2 数据驱动发现的哲学辩护

**Anderson, C. (2008). The End of Theory: The Data Deluge Makes the Scientific Method Obsolete. *Wired Magazine*, 16.07.**

- **核心论点**（非常挑衅但相关）：在巨量数据时代，"相关性胜于因果关系"——不是在理论上，而是在实践上。当你拥有足够的数据时，你不需要一个因果模型——相关性就足够了。
- **对 Branch D 的支撑**：虽然 D 并不完全放弃因果，但它确实接受了"不关心为什么"的实证前提——这与 Anderson 的颠覆性论点一致：如果你有足够的 DeFi 数据，你是否需要一个理论来确定相关性是否有用？D 的回答：作为第一步，不需要。

**Breiman, L. (2001). Statistical Modeling: The Two Cultures. *Statistical Science*, 16(3), 199-231.**

- **核心论点**：统计学中有两种文化——数据建模文化（regression, p-values, tests of assumptions）和算法建模文化（random forests, SVMs, neural nets）。Breiman 认为两者都可以在同样的"预测精度"标准下被评判——不需要共享一个先验理论。这个观点瓦解了传统的"数据驱动=无理论"的反对。
- **对 Branch D 的支撑**：D 与 Breiman 一致——它不认为必须有一个economic theory of behavioral deviations 才能使用这些偏差进行预测。预测精度的提高本身就是该偏差是"真实的"信号（因为它是对未来的预测）。

---

## 第二部分：DeFi 的经验基线

### 2.1 链上信用评分

**Ghosh, S. et al. (2024). On-Chain Credit Scoring for DeFi.** *(Working Paper)*

- **核心论点**：用传统链上特征（活跃度、资产、复杂图特征）来构建 DeFi 信用评分的第一次系统性尝试。该工作被认为引入了"纯链上信贷评分"的概念。
- **对 Branch D 的支撑**：提供了赛马的竞赛者角色。D 的M0模型（纯HF + 抵押率）是基线，Ghosh et al. 的工作表明"用特征来预测"在原理上是可行的。但该工作还未探索过行为偏差的特征——D 的独特性在于其行为的特征组（"行为主义的信用"与"隐私保护的"信用评分相对）。

### 2.2 DeFi 借贷的程式化事实

**Gadzinski & Liuzzi (2025)** 和 **Cornelli et al. (2025)** ——两个提供经验基础的 DeFi 工作。在 Branch D 中，它们作为"已知的经验事实"被引用。

**Mu, Y. et al. (2025). DEFI Lending: From Mechanism Efficiency to Borrower Behavior.** *(Preprint)*

- **核心论点**：从机制高效性到借款人行为的综述——覆盖 DeFi 借贷的清算效率、Gas 拍卖、清算套利等的经验事例。
- **对 Branch D 的支撑**：提供 D 要研究的"行为"的背景环境——包括清算机制的契约环境（协议不能单方面改变信用条款）和 DeFi 借款人的类型（包括 arb bot 和普通用户）。

---

## 第三部分：方法论——赛马与预测

### 3.1 比较两种预测模型

**DeLong, E.R., DeLong, D.M. & Clarke-Pearson, D.L. (1988). Comparing the Areas under Two or More Correlated Receiver Operating Characteristic Curves. *Biometrics*, 44(3), 837-845.**

- **核心论点**：当使用相同的数据测试两个分类器的ROC曲线时用于比较AUC的标准统计检验。
- **对 Branch D 的支撑**：D 的核心统计检验——哪个模型（M0 对 M2）有更大的AUC——将使用 DeLong 检验来判断差异是否统计显著。这是 D 的方法论工具箱中的关键部分。

### 3.2 特征重要性与可解释性

**Lundberg, S.M. & Lee, S.I. (2017). A Unified Approach to Interpreting Model Predictions. *Advances in Neural Information Processing Systems*, 30, 4765-4774.**

- **核心论点**：SHAP值（SHapley Additive exPlanations）作为一个跨模型的解释框架——任何机器学习模型的预测都可以被解释为"当某个特征存在时，预测偏离了平均值的幅度"。SHAP 提供了理论上的统一性。
- **对 Branch D 的支撑**：D 的辅助分析——哪些行为特征最重要？——通过 SHAP 获得。这允许 D 可以表述："行为因子 X 是预测清算的第三重要的特征，排在两个金融因子之后——因此即使未达最高30%的排名，X 在预测上也是有用的。"

---

## 第四部分：文献的角色映射

| 文献 | 支持 D 的哪个主张？ |
|------|-------------------|
| Hamermesh (2000) | 在模型前先有事实是合法的 |
| Lewbel (2019) | "识别"不需要结构解释 |
| Breiman (2001) | 预测精度独立于模型的先验理论内洽 |
| Ghosh et al. (2024) | 链上信贷评分在原则上是可行的 |
| Christensen & Miguel (2018) | 透明性和预注册对经验论文的重要性 |
| DeLong et al. (1988) | 检验增量AUC的方法论 |
| Lundberg & Lee (2017) | SHAP 用于行为因子的重要性解释 |

---

*所有引用须通过 `paper_search` 确认。在 Branch D 的简约主义精神下，只引用严格必要的参考文献。*
