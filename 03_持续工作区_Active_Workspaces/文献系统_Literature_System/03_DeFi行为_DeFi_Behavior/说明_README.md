# 03_DeFi-Behavior — V4 DeFi 行为金融线

## 核心研究问题
当 DeFi 借贷者接近清算阈值时，其行为是否系统性地偏离理性预期（前景理论预测的损失厌恶、参照点效应、敏感性递减）？这些行为偏差是否携带增量信用预测信息？

## 关键构念
| 构念 | 描述 |
|------|------|
| Health Factor (HF) | Aave/Compound 中的健康因子 = 抵押品价值 / 借款价值 |
| BDM | Behavior Deviation Measure（行为偏差度量） |
| Liquidation Threshold | 清算阈值 |
| Prospect Theory | 前景理论（Kahneman & Tversky 1979） |
| Active vs. Passive | 主动修复 vs. 被动被清算 |
| Loss Aversion | 损失厌恶——亏损的心理影响大于等值收益 |
| Reference-Point Effect | 参照点效应——HF=1 是关键的参照点 |

## 导师会议指出的方向
- V4 作为备用方案：如果拿不到私密数据，则用公有数据（Aave/Compound）做
- 导师核心建议：先把"中间地带"线做起来，但不代表 V4 没有价值
- V4 的特点是：可复现、公开数据、可独立发文章

## V4 迭代状态（V4 → V4_1 → V4_2 → V4_3）
| 版本 | 核心变化 |
|------|----------|
| V4    | 初始探索：Prospect Theory × DeFi Lending |
| V4_1  | 修复决策锚（加入 $\Delta W$ 福利量化）和 Active/Passive 分类 |
| V4_2  | 知识图谱分析 → 发现 4 个断连组件 → RQ3 降级为 conditional extension |
| V4_3  | 导师版：弱化 prospect theory 假设，强调行为观测优先 |

## 文献收录建议方向
1. DeFi 清算的实证研究
2. 前景理论在金融市场的应用（尤其是危机情境）
3. 链上信用评分的机器学习方法
4. Aave/Compound 协议分析
5. 行为经济学视角的 DeFi 用户研究

## 相关关键词
`DeFi liquidation` `Aave Compound` `prospect theory` `loss aversion` `behavioral finance DeFi` `lending liquidation` `health factor` `on-chain credit scoring`
