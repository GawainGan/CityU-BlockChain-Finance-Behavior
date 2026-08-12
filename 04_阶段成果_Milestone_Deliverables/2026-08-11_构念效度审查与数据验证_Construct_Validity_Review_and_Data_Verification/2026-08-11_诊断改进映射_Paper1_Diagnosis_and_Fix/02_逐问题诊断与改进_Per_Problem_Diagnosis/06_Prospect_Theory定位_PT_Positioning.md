# 06. Prospect Theory 定位：从 confirmed anchor 降级为 competing explanation

**严重程度**：🟡 Over-claim  
**Report 1 位置**：`sections/literature-review.tex` Lines 21-23, `sections/research-topic.tex` Line 47, `sections/discussion.tex` Line 9  
**六层矩阵文件**：`05_不可声称清单.md` §4

---

## 1. 问题描述

Report 1 将 Prospect Theory（PT）定位为研究的 confirmed theory anchor，声称 DeFi 的 liquidation threshold 是一个"objective, exogenously determined reference point"用于测试 PT 预测。但 HF=1.0 既是心理参考点也是协议机制不连续点——借款人在 HF=1.0 附近的行为变化既可能由 loss aversion（心理效应）解释，也可能由清算罚金的经济激励（理性解释）解释。两种解释在缺乏特殊识别策略时不可分离。

---

## 2. Report 1 原文

> **literature-review.tex, Line 21:**
>
> On the one hand, DeFi lending provides an almost ideal empirical laboratory for testing behavioral theories. The liquidation threshold—a hard-coded, protocol-defined health factor value below which positions become eligible for liquidation—serves as an objective, exogenously determined reference point that is identical across all participants.

> **literature-review.tex, Line 23:**
>
> Disentangling rational risk management from behavioral deviations therefore requires careful empirical design, including the use of control groups, instrumental variables, or regression discontinuity approaches that exploit the quasi-exogenous variation created by the protocol-defined liquidation threshold.

> **research-topic.tex, Line 47:**
>
> Second, it bridges the largely separate literatures on DeFi risk modeling and behavioral finance by testing prospect theory predictions in a naturalistic financial setting where the reference point—the liquidation threshold—is objective, observable, and identical for all participants...

> **discussion.tex, Line 9:**
>
> ...it would provide the first systematic evidence that prospect theory's predictions—particularly those concerning loss aversion and reference-point effects—are observable in DeFi lending behavior at a granular, position-by-position level.

> **research-topic.tex, Line 32 (H1b):**
>
> **H1b (Loss Aversion Asymmetry).** The magnitude of borrower-initiated risk-reducing actions (collateral additions, debt repayment) per unit deterioration in health factor is larger in absolute value than the magnitude of additional borrowing or collateral withdrawal per unit improvement in health factor, consistent with the loss aversion prediction of prospect theory.

---

## 3. 错误分析

### 3.1 双重解释问题

HF=1.0 附近的行为不连续性有两种解释：

| 解释 | 机制 | 预测 |
|------|------|------|
| **Prospect Theory（行为解释）** | HF=1.0 是心理参考点；loss aversion 导致借款人在"损失域"（HF<1 区域）的行为比"收益域"更激烈 | 行为不连续性来源于心理偏差 |
| **Rational Risk Management（理性解释）** | HF=1.0 是清算触发点；清算罚金（5-10%）是真实的经济成本；理性借款人会在接近清算边界时加强风险管理 | 行为不连续性来源于经济激励 |

**关键问题**：两种解释预测相同的行为模式（HF 接近 1.0 时风险减轻行为增加），在没有特殊识别策略时不可分离。

### 3.2 Report 1 的矛盾

- Literature Review Line 23 已经承认了这个问题："Disentangling rational risk management from behavioral deviations therefore requires careful empirical design"
- 但 Research Topic Line 47 和 Discussion Line 9 仍然将 PT 定位为可以"test"和"provide evidence for"的理论
- 方法论部分没有提出能够分离两种解释的识别策略

### 3.3 H1b 的问题

H1b 直接声称测试 "loss aversion prediction of prospect theory"，但如果理性解释也能产生相同的 asymmetry，H1b 的结果不能归因于 PT。

---

## 4. 六层矩阵映射

**不可声称清单**：`05_不可声称清单.md` §4
- §4.1: "Prospect Theory 是本研究的 confirmed theory anchor"
- §4.2: "借款人在 HF=1.0 附近的行为变化证明了 loss aversion"
- §4.3: "我们识别了 reference-dependent preferences"

---

## 5. 修正方案

### 5.1 定位降级

```text
原定位：Prospect Theory as confirmed theory anchor
修正后：Prospect Theory as compelling framing / competing explanation
```

### 5.2 措辞替换

| ❌ 不应使用 | ✅ 应使用 |
|-----------|---------|
| "testing prospect theory predictions" | "examining whether behavioral patterns are consistent with prospect theory predictions" |
| "prospect theory's predictions are observable" | "behavioral patterns consistent with reference-point behavior are observable" |
| "serves as an objective reference point for testing PT" | "serves as a natural reference point that is consistent with PT framing, though behavioral and rational explanations cannot be fully separated" |
| "consistent with the loss aversion prediction of prospect theory" (H1b) | "consistent with both loss aversion and rational risk management predictions" |

### 5.3 H1b 修正

H1b 应明确承认双重解释：

```text
H1b (Asymmetry Near the Liquidation Threshold):
The magnitude of borrower-initiated risk-reducing actions per unit 
deterioration in health factor is larger in absolute value than 
the magnitude of risk-increasing actions per unit improvement in 
health factor. This asymmetry is consistent with both prospect 
theory's loss aversion prediction and the rational incentive to 
avoid the liquidation penalty; the two explanations cannot be 
fully separated without additional identification strategies.
```

### 5.4 贡献重新定位

```text
原贡献：提供 PT 在 DeFi 中的系统性证据
修正后：记录 HF=1.0 附近的行为不连续性，并将其定位为 
       PT 和理性风险管理都能解释的现象，
       为未来研究提供识别策略的方向
```

---

## 6. 文献支撑

| 文献 | 与本问题的关系 |
|------|---------------|
| Kahneman & Tversky (1979) | PT 原始定义——reference point, loss aversion |
| Barberis (2013) | PT 在金融中的应用综述——承认 reference point 的识别挑战 |
| Benartzi & Thaler (1995) | Myopic loss aversion——但传统金融中 reference point 难以观测 |
| Sadeghi & Feinstein (2026) | DeFi 清算中的经济激励分析——理性解释的文献支撑 |

---

## 7. 修改后的文本

### literature-review.tex 修正

```latex
On the one hand, DeFi lending provides a promising setting for 
examining behavioral predictions. The liquidation threshold---a 
hard-coded, protocol-defined health factor value below which 
positions become eligible for liquidation---serves as an objective, 
exogenously determined reference point that is identical across all 
participants. This stands in contrast to traditional financial 
settings, where reference points are typically unobserved, 
subjective, and likely to vary across individuals
~\cite{barberis2013thirty}. 

However, a fundamental identification challenge arises: the 
liquidation threshold is simultaneously a psychological reference 
point \emph{and} a mechanical protocol discontinuity. The liquidation 
penalty (typically 5--10\% of the liquidated collateral) creates a 
rational economic incentive for borrowers to manage their positions 
more intensively as they approach the threshold. Consequently, 
behavioral discontinuities observed near the threshold---such as 
increased risk-reducing activity or asymmetric responses to gains 
and losses---are consistent with \emph{both} prospect theory's loss 
aversion prediction \emph{and} rational risk management. Separating 
these two explanations requires identification strategies that 
exploit variation in the economic cost of liquidation (e.g., 
cross-asset differences in liquidation penalties) or in the 
salience of the threshold (e.g., protocol interface changes), which 
are beyond the scope of the present study. We therefore frame 
prospect theory as a \emph{compelling competing explanation} rather 
than a confirmed theoretical anchor, and interpret any behavioral 
patterns consistent with PT predictions as suggestive rather than 
definitive evidence.
```

### discussion.tex Scenario 1 修正

```latex
First, at the theoretical level, it would document behavioral 
discontinuities near the liquidation threshold that are consistent 
with prospect theory's predictions---particularly those concerning 
loss aversion and reference-point effects---at a granular, 
position-by-position level. We caution, however, that these patterns 
are equally consistent with rational risk management driven by the 
economic cost of liquidation, and the present study cannot 
definitively adjudicate between the two explanations.
```
