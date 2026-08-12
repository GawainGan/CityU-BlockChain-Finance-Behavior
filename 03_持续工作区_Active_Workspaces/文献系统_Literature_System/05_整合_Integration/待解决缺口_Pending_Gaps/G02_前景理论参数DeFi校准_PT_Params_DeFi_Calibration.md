# G02: Prospect Theory 的损失厌恶参数在 DeFi 清算中的校准

## 基本信息

| 字段 | 内容 |
|------|------|
| **Gap ID** | G02 |
| **Gap 描述** | 前景理论（Prospect Theory）的损失厌恶参数在 DeFi 清算场景中是否被校准过？ |
| **涉及线** | V4 DeFi-Behavior |
| **验证优先级** | ⭐⭐⭐⭐⭐ |
| **来源** | A_gap_map.md Line 2 待核实空白 |

## 验证状态

| 轮次 | 日期 | 方法 | 结果 |
|------|------|------|------|
| 1 | 2026-07-10 | paper_search(econ): prospect theory loss aversion parameter calibration DeFi | 无直接结果 |
| — | — | — | — |

## 核心验证逻辑

前景理论的关键参数包括：

1. **损失厌恶系数 λ**（通常 Kahneman & Tversky 估计为 ~2.25，即损失的心理权重 ~ 等量收益的 2.25 倍）
2. **风险偏好翻转**：在收益域风险厌恶，在损失域风险寻求
3. **参照点依赖**：损失/收益的判定以参照点为界

**空白假设**：虽然在传统金融市场中这些参数已被大量检验（如处置效应文献、行为资产定价模型等），但在 DeFi 借贷这个特定场景中——特别是清算阈值（HF=1）作为外生参照点的设置——没有任何已发表研究系统校准过这些参数。

**潜在竞争者**：Cornelli et al. (2025) 提供的证据强烈暗示前景理论预测成立（选择波动性抵押品的 OR = 2.3, HF < 1.2），但没有估计 λ 或检验参数统计显著性。

## 参考文献

```bibtex
@article{Kahneman1979_ProspectTheory,
  title = {Prospect Theory: An Analysis of Decision under Risk},
  volume = {47},
  DOI = {10.2307/1914185},
  number = {2},
  journal = {Econometrica},
  author = {Kahneman, Daniel and Tversky, Amos},
  year = {1979},
  pages = {263}
}
```
