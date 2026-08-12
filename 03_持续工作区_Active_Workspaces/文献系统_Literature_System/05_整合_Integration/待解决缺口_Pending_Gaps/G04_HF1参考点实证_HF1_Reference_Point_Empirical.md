# G04: 清算的参照点效应（HF=1）的实证证据

## 基本信息

| 字段 | 内容 |
|------|------|
| **Gap ID** | G04 |
| **Gap 描述** | 是否有实证研究分析 HF=1 附近的借贷行为变化（参照点效应）？ |
| **涉及线** | V4 DeFi-Behavior |
| **验证优先级** | ⭐⭐⭐⭐ |
| **来源** | A_gap_map.md Line 2 待核实空白 |

## 验证状态

| 轮次 | 日期 | 方法 | 结果 |
|------|------|------|------|
| — | 2026-07-10 | 预判 | 部分已被 Cornelli et al. (2025) 覆盖 |

## 核心验证逻辑

Qin et al. (2021) 确认了 HF=1 是硬编码的清算阈值，但他们的研究问题是"清算机制如何运行"而非"借款人如何在 HF 接近 1 时改变行为"。Cornelli et al. (2025) 的研究部分覆盖了这一 gap，发现：
- HF < 1.3 时主动补救概率是 HF > 2.0 的 3-5 倍
- HF < 1.2 时选择波动性抵押品的 OR = 2.3

需要确认是否有独立研究提供了实时 HF 行为的独立证据。

## 参考文献

```bibtex
@inproceedings{Qin2021_DeFi_Liquidations_IMC,
  title = {An Empirical Study of DeFi Liquidations: Incentives, Risks, and Instabilities},
  DOI = {10.1145/3487552.3487811},
  booktitle = {Proceedings of the 21st ACM Internet Measurement Conference},
  author = {Qin, Kaihua and Zhou, Liyi and Gamito, Pablo and Jovanovic, Philipp and Gervais, Arthur},
  year = {2021},
  pages = {336--350}
}
```
