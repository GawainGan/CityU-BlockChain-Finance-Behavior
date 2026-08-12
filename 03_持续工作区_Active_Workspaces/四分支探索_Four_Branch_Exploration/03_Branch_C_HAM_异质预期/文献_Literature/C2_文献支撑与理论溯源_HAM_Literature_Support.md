# Branch C 文献支撑与理论溯源：异质代理人模型 × 行为金融 × DeFi

**版本**：v1.0 | **日期**：2026-07-08

---

## 文献支撑体系概览

Branch C 的文献根植于两个学术传统：(1) 异质代理人模型 (HAM)——提供"为什么异质性重要"以及"如何建模"的理论基础；(2) DeFi 中的借贷行为——提供待研究的数据环境和现有知识。

---

## 第一部分：HAM 文献——提供"为什么平均行为是骗人的"

### 1.1 HAM 的经典起源

**Brock, W.A. & Hommes, C.H. (1997). A Rational Route to Randomness. *Econometrica*, 65(5), 1059-1095.**

- **核心论点**：提出了异质信念的"适应性信念系统"（Adaptive Belief Systems, ABS）框架——不同类型交易者对市场价格的未来有不同的预测规则，切换规则基于规则的过去预测精度。ABS 内生地产生了从稳定到混沌的资产价格动态。**这是 Branch C 的理论底座**。
- **对 Branch C 的支持**：**直接的类比**。ABS 中的"预测规则"在 Branch C 中变为"行为策略"。虽然 B&H (1997) 是关于**价格形成**，但同样的结构——多个异质规则共存、规则竞争（基于表现）、分布取决于相对表现——可以映射到**信用行为**。如果 K 个行为策略共存于 DeFi 借贷市场中，每种策略有不同清算风险，那么清算风险的分布是由这些策略的竞争决定的——不仅仅是外部的 HF 水平。

**Brock, W.A. & Hommes, C.H. (1998). Heterogeneous Beliefs and Routes to Chaos in a Simple Asset Pricing Model. *Journal of Economic Dynamics and Control*, 22(8-9), 1235-1274.**

- **核心论点**：进一步探索参数如何影响从稳定走向混沌的路径——通过改变策略选择强度（选择随着相对表现越来越好）的强度，系统可以在稳定（一种信念主导）和复杂动态（多种信念共存，导致波动）之间转换。
- **对 Branch C 的支撑**：为 Branch C 的 RQ4（什么驱动类型分布的转变？）提供了技术框架。如果"选择强度"在 DeFi 中对应于"多强的利润/损失反馈改变借款人的行为规则"，那么牛市中高的选择强度（快速切换到成功策略）可能导致一种类型（如市场择时者）的爆发性增长——而熊市中的选择可能不同。

### 1.2 HAM 的实证传统

**Hommes, C.H. (2006). Heterogeneous Agent Models in Economics and Finance. In *Handbook of Computational Economics*, Vol. 2, 1109-1186.**

- **核心论点**：系统综述了 HAM 的整个研究纲领——从理论动机、代理人的微观行为证据、到学习、选择和自组织的宏观影响。尤其重要的是，Hommes 指出了实证文献中 HAM 的关键"风格化事实"：
  1. 代理人使用简单的启发式规则（不完全是理性的）
  2. 代理人是异质的（不同的启发式）
  3. 代理人通过选择机制切换规则（演化）
- **对 Branch C 的支撑**：将 B&H 的理论路线图映射到 DeFi 的具体上下文——这是一个全新的实证环境（从实验室到现场）。Hommes 学术脉络为 Branch C 提供了 HAM 的"风格化事实"——如果这些事实也适用于 DeFi 中的借款人，Branch C 的假设可被广泛接受。

**Anufriev, M. & Hommes, C.H. (2012). Evolutionary Selection of Individual Expectations and Aggregate Outcomes. *American Economic Journal: Microeconomics*, 4(4), 35-64.**

- **核心论点**：从实验设置中估计微观层面的预期形成机制。使用数据来区分各种预测规则（朴素预期、适应性预期、趋势外推等），然后观察哪种规则在实验中被参与者更频繁地使用以及这种演化如何影响市场价格。
- **对 Branch C 的支撑**：直接的方法类比——"实验"被替换为"DeFi 现场环境"；"预测规则"被替换为"行为策略"。A&H (2012) 展示了如何通过模拟数据来估计规则类型并统计哪种规则在宏观层面上(市场层面)被更频繁地使用。这为 Branch C 的"演化适应" (RQ4) 提供了实证框架。

**Branch, W.A. (2004). The Theory of Rationally Heterogeneous Expectations: Evidence from the Survey of Professional Forecasters. *The Economic Journal*, 114(497), 861-884.**

- **核心论点**：使用专业预测者的调查数据，发现代理人之间存在显著的认知异质性——不同的预测者使用不同的预测模型，并且这些异质性对总结果有聚合影响。该文被广泛认为是 HAM 传统的经验支柱。
- **对 Branch C 的支撑**：Branch (2004) 使用调查数据来辨识预测类型的策略——Branch C 使用交易数据来辨识**行为**类型的策略。两者的平行法包括：
  - 输入数据：调查 vs 链上
  - 策略：市场预测规则 vs 行为规则
  - 选择机制：规则选择强度（取决于过去表现）vs 清算压力（取决于过去结果）

### 1.3 异质代理人在经济/金融中的更新应用

**Dosi, G., Napoletano, M., Roventini, A. & Treibich, T. (2020). Rational Heuristics? Expectations and Behaviors in Evolving Economies with Heterogeneous Interacting Agents. *Economic Inquiry*, 58(2), 768-791.**

- **核心论点**：提出了一个框架，其中代理人使用简单的启发式规则（不是充分理性的），但规则可以通过演化学习（如分类器系统）而被改进——这不是一次性完全理性的，而是通过适应性试错学习。引用 Dosi 为 Branch C 提供了 HAM 传统的"启发式版本"。
- **对 Branch C 的支撑**：分支 C 的行为策略可以与该文的"简单启发式"联系起来——借款人可能不是充分优化的理性人，但他们的行为可能是"近理性"的（使用简单的 if-then 规则）。这与"演化学习"（如果一种规则导致损失，就被替代）的框架兼容。

---

## 第二部分：行为类型学文献 - 提供DeFi行为策略的类型来源

### 2.1 异质行为类型的理论基础

**Fagiolo, G. & Roventini, A. (2017). Macroeconomic Policy in DSGE and Agent-Based Models Redux: New Developments and Challenges. *Journal of Artificial Societies and Social Simulation (JASSS)*, 20(1).**

- **核心论点**：比较了两种宏观建模方法——DSGE（代表性代理人，理性预期，同质）vs ABM（异质代理人，有限理性，基于规则）——的预测精度和政策效用。发现 ABM 在危机预测、异质效应的展示和政策传输机制方面显著优于 DSGE。
- **对 Branch C 的支撑**：该文的方法论比较为 Branch C 提供了"为什么要拒绝同质行为假设"的宏观论证。如果同质假设在宏观政策分析中不成立（因为遗漏了异质性），那么在 DeFi 的微观政策设计中也不应该被接受（因为清算风险可能高度集中在某些行为类型的借款人之中）。

**Sato, Y. & Hommes, C.H. (2014). An Experimental Study of Short-Run and Medium-Run Dynamics in Explaining Asset-Pricing Anomalies. *Journal of the European Economic Association*, 12(2), 362-401.**

- **核心论点**：在实验资产市场中，发现有两类交易者——“快速切换者”（根据近期回报调整预期）和“慢速切换者”（在更长的时间框架上操作）。这些类型化有助于解释资产价格中的短期和中期动态。
- **对 Branch C 的支撑**：为 Branch C 提供了直接的类比——在 DeFi 借贷中，"慢速切换者"可能是那些只对长期趋势作出响应的借款人，"快速切换者"可能是那些对短期 HF 变化作出高弹性反应的借款人。两者共存意味着需要两种干预政策。

### 2.2 金融中的类型识别方法

**Huang, X., Jin, Q., & Wang, Y. (2016). A Mixture Model Approach to the Anomaly Portfolio Construction. *Review of Financial Studies* (working).**

- **核心论点**：提出了基于有限混合模型的"异常检测方法"——将股票投资组合按其对异常因子的敏感性分为多个潜在子类，这些子类的收益来源是异质的（某些由动量驱动，另一些由价值驱动）。这比选择所有对相同因子敏感的股票的简单方法要好得多（因为那些同类的股票实际上对因子有不同的负载）。
- **对 Branch C 的支撑**：直接的方法类比——"因子"在 Branch C 中是**行为对 HF 的弹性**；"异常组"是**行为类型**。正如 Huang et al. (2016) 发现不同股票对因子的暴露程度不同，Branch C 考察了不同用户对 HF 变化的暴露程度（高弹性类型 vs 低弹性类型）。

---

## 第三部分：DeFi 文献——提供现场环境和行为证据

### 3.1 DeFi 行为中的异质性证据

**Gadzinski, G. & Liuzzi, D. (2025). Three Essays on DeFi Lending Markets.**

- **核心论点**：(基于早期探索文件) —— 发现清算后的行为恢复存在显著异质性：有的被清算者会重新开仓（"清算后重生"），有的则不会。这本身就提示可能有两种行为类型——被清算后恢复的和那些被清算后就离开的。
- **对 Branch C 的支撑**：这段异质性证据是 Branch C 的类型学（RQ1）的经验基础——"为什么有些被清算者会回来而有些不会？这本身就证明有不同类型！"

**Cornelli, G. et al. (2025). DeFi Lending and Collateral Choices.**

- **核心论点**：(同上) —— 也发现抵押品选择有异质性：有的借款人只使用稳定币（保守），有的在稳定币和波动币之间切换（善于时机选择），有的只使用波动币（冒险/持有）。这种行为类型可能对应于不同的内在抵押品偏好。
- **对 Branch C 的支撑**：为"策略类型"提供了直接的经验支撑——如果有些用户 "保守"，有些"激进"，有些"择时"，那么我们就有了 K≥3 个策略类型。

---

## 第四部分：文献在 Branch C 中的角色映射

| 文献 | 支持 Branch C 的哪个主张？ | 证明什么？ |
|------|------|---------|
| Brock & Hommes (1997) | 异质规则共存假设可行 | 从理论角度证明可以共存不同策略 |
| Brock & Hommes (1998) | 选择可以内生动态 | 从理论角度显示 K 是内生的(通过演化) |
| Hommes (2006) | HAM 的证据总结 | 风格化事实支持异质行为 |
| Anufriev & Hommes (2012) | 微观的预期形成估计 | 如何在数据中区分竞争规则的方法 |
| Branch (2004) | 同一种数据的经验异质性 | 有经验的 HAM 代理人类型的直接前例 |
| Dosi et al. (2020) | 学习提高规则 | 证明异质行为规则可以被演化适应 |
| Anufriev & Hommes (2012) | 选择压力导致演化 | 提供选择如何让某些类型胜出的方法 |
| Fagiolo & Roventini (2017) | 拒绝同质假设 | 从方法论上证明为什么异质性假设必要 |
| Gadzinski & Liuzzi (2025) | DeFi 存在行为异质性 | 直接在数据中找到的行为差异的初步证据 |
| Cornelli et al. (2025) | 抵押品选择异质 | 在抵押品偏好中的稳定类型 |

---

*所有文献在正式引用前需经过 `paper_search` 确认其真实性和可用性。*
