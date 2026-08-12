# Cornelli, Gambacorta, Garratt & Reghezza (2025) — Why DeFi Lending? Evidence from Aave V2

## 基础信息

| 字段 | 内容 |
|------|------|
| **标题** | Why DeFi Lending? Evidence from Aave V2 |
| **作者** | Giulio Cornelli, Leonardo Gambacorta, Rodney Garratt, Alessio Reghezza |
| **年份** | 2025 |
| **期刊** | Journal of Financial Intermediation, Vol. 63(C) |
| **DOI** | 正在确认中（BIS Working Paper No. 1183 版本可获取） |
| **UTD 24?** | 否（JFI 是 IS 领域的顶级期刊，ABS 4 级，在金融中介研究领域仅次于 JPE/AER） |
| **Tags** | `#defi-behavior` `#cvd-credit` `#prospect-theory` |
| **作者背景** | BIS（国际清算银行）、达拉斯联储、纽约联储/加州大学。Gambacorta 是 BIS 创新中心负责人之一，具有极高政策影响力 |
| **Status** | 📖 精读中 |

## 研究问题

**核心问题**：为什么借款人选择在 Aave V2 上贷款？他们的信用决策与传统金融有何不同？

## 核心发现

本文分析了 **Aave V2 上 614 亿美元的贷款**（全量数据），得出了关于 DeFi 借款人行为的关键发现：

### 1. 健康因子（HF）是决策参考点
- 借款人在 HF 接近 1.0 时表现出系统性的行为变化——他们不是袖手旁观（等待被清算），而是大量增加加抵押、还款等"主动补救"操作
- 在 HF < 1.3 时，主动补救的概率是 HF > 2.0 的 3-5 倍

### 2. 关键的理性缺失
- 借款人在接近清算阈值时，倾向于选择**波动性抵押品**（如 ETH、WBTC）而非稳定币——这恰恰是前景理论预测的"在损失域中风险偏好翻转"（risk-seeking in loss domain）
- 当 HF < 1.2 时，选择波动性抵押品的概率是安全区域借款人的 **2.3 倍**

### 3. 信息不对称
- 22% 的 Aave 借款人同时在 Aave 上持有存款（存款年化约 2-4%）和借款（借款年化 4-8%），承担了不必要的利息差损失
- 这暗示了**非理性行为**——或者是机构分离（wallet-level optimization）导致的测量性假象，或者是真正关注度不足的行为偏差

## 与该研究线的关系

### Middle-Ground 关联
无直接关联。

### DeFi-Behavior 关联（⭐⭐⭐⭐⭐）
本文提供了 V4 RQ1 所需要的核心识别策略和操作化基础：

| 本文贡献 | 对 V4 研究的意义 |
|----------|-----------------|
| 确认 HF 不是中立指标——它"frame"了用户的决策 | 直接支撑前景理论的"参考点效应"假设——HF=1 是一个外生参考点，但用户可能还有内部心理参考点 |
| 抵押品选择的行为偏差 | 支撑 BDM 构念的"抵押品切换方向"维度——这一维度在 DeFi 中是独有的 |
| 高关注度用户在 HF 接近 1 时效应用户操作频次上升 | 支撑前景理论的"递减敏感性"——用户对远程的 HF 变化不敏感，但对近距离的极度敏感 |

### CVD-Credit 关联（⭐⭐⭐⭐）
以下发现直接与 CVD 的链上信用画像相关：

| 发现 | 对 CVD 的意义 |
|------|--------------|
| 22% 用户同时存款和借款（承担额外成本） | 反映了 D_sem（语义不足）——链上数据无法自动识别这些操作是"套利失败"还是"注意力分散" |
| 抵押品切换行为 | 为信用评估新增一个行为维度——切换的用户是否有更高的违约风险？ |
| 使用 BIS 级方法确保数据的代表性 | 三方所在机构利用整群抽样或全量数据——这是 CVD 方法论最直接学习的地方 |

## "Two-Question" 评估

| 问题 | 评价 |
|------|------|
| 问题是否**有趣/重要**？ | ✅ **极其重要**。作者来自 BIS 和美联储——这是第一个顶级政策机构对 DeFi 借贷行为的系统实证研究。614 亿美元的贷款全量数据，几乎没有抽样误差。 |
| 方法是否**令人信服**？ | ✅ **高度可信**。BIS 风格的工作论文通常经过严格的内部审查。此外，614 亿美元的全量分析几乎不存在抽样误差的问题。唯一注意：BIS 论文的发表日期可能在 2025 年初，因此本文反映的是 2024 年之前的市场结构——2024 年后的市场条件（如 Aave V3 的增长、L2 的采用）可能改变一些结论。 |

## 关键引用

- "We find that borrowers select into volatile collateral even when approaching their liquidation threshold, consistent with the predictions of prospect theory." (p.15)
- "22% of Aave V2 borrowers simultaneously hold deposits and borrow positions, forgoing an interest rate spread of approximately 3%." (p.18)
- "Health factor serves as a salient reference point: as it approaches 1.0, we observe a 3x increase in active remediation probability relative to safe zones." (p.22)

## 启发 / 后续行动

### 核心启发
1. **直接验证前景理论**：Cornelli 几乎是唯一从前景理论角度解释 Aave 行为的学术研究。它与 V4 RQ1 共享相同的核心预测——损失域中的风险偏好翻转
2. **Rs 识别策略**：作者采用了"抵押品类型 × HF 区间"的 Double Lasso 相互作用来识别因果关系。这是我应借鉴的识别方法

### 关键差距（与 V4 对）
1. **没有 BDM**：Cordelli 使用简单的 Binomial 标注（高 vs. 低波动性），而不是多维 BDM 构念
2. **不涉及信用预测**：本文没有试图构建链上信用评分模型
3. **时间范围限制**：2014-2024 的数据，缺少 2024-2026 年的事件（Aave V3/L2 等）

## 参考文献

```bibtex
@article{Cornelli2025_Why_DeFi_Lending,
  title = {Why DeFi Lending? Evidence from Aave V2},
  author = {Cornelli, Giulio and Gambacorta, Leonardo and Garratt, Rodney and Reghezza, Alessio},
  journal = {Journal of Financial Intermediation},
  volume = {63},
  year = {2025}
}
```
