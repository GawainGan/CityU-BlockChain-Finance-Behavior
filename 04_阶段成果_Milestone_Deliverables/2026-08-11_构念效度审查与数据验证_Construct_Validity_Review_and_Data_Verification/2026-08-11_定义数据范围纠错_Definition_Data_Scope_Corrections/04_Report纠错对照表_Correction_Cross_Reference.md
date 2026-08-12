# 对 2026-07-17 Research Report 的纠错对照表

**日期**：2026-08-11  
**基线**：`2026-07-17_Research_Report`（中英版结构一致，以下以中文版表述为准）  
**原则**：不推翻主问题；逐条收缩过强 claim、修正技术硬伤、标明后置主题

---

## A. 总览：哪些要改，哪些保留

| 模块 | 原状态 | 本次处理 |
|---|---|---|
| 核心问题：风险上升时的主动调整是否含增量信息 | 成立 | **保留** |
| 公开数据、可复现导向 | 成立 | **保留** |
| RQ1 行为层 | 基本成立 | **收紧对象名称** |
| RQ2 信用层 | 命名过强 | **改名 + outcome 收缩** |
| 完全行为可观测修辞 | 过强 | **纠错** |
| HF 用 LTV | 技术错误 | **纠错** |
| `msg.sender == borrower` | 过粗 | **升级操作化** |
| Supply = 追加抵押 | 不精确 | **纠错** |
| Prospect Theory 作为强结论导向 | 偏早 | **降为 framing / competing explanation** |
| Payment / Settlement | 基本缺失 | **后置为 Paper 2，不塞进正文主线** |
| “抵押不够 blockchain-native”潜在直觉 | 易说反 | **理论表述反转纠正** |

---

## B. 摘要与绪论

### B1. “完全透明 / 完全记录”类表述

| 位置 | 原倾向 | 问题 | 更新写法 |
|---|---|---|---|
| 摘要、绪论 | 强调协议产生参与者行为的完全透明记录 | 易被读成完整经济行为可观测 | 改为：**协议交互与仓位相关事件的高粒度、可复现记录** |
| 讨论中的“完全的行为可观测性” | 作为 DeFi 优势修辞 | 与后文 partial observability 自相矛盾 | 改为：**protocol-recorded actions 可观测；intent / off-chain hedge / identity 不可完全观测** |

**纠错级别**：高（construct validity / claim discipline）

---

## C. 研究课题与 RQ

### C1. 课题定义

| 原写法 | 更新写法 |
|---|---|
| 主动行为调整与后续清算或其他不利风险结果的关系 | 保留清算结果，但明确这是 **position risk outcome** |
| 隐含通向 credit assessment | 当前只承诺到 **liquidation propensity / risk-management quality** |

### C2. RQ2 命名

| 原 | 新 |
|---|---|
| RQ2（信用层面） | RQ2（风险信息层面 / Liquidation Propensity） |
| “信用相关信息”可保留为弱表述 | 避免直接写 “creditworthiness prediction” |

### C3. 假设

| 原假设 | 处理 |
|---|---|
| H1a 主动调整随风险上升而增加 | 保留 |
| H1b 损失厌恶非对称 | 保留为可检验假说，但结果解释需排除“规避清算罚金”的理性机制竞争 |
| H1c HF=1 参照点断点 | 保留检验，但承认 HF=1 同时是机制间断点，不等于已证明前景理论 |
| H2a/H2b 预测清算 | 保留预测框架；删除“即信用结果”的等同 |

**纠错级别**：高（理论识别）

---

## D. 方法论硬纠错

### D1. Health Factor 公式

| 项目 | 内容 |
|---|---|
| 原文问题 | \(\mathrm{HF}_t=\sum (C\cdot P\cdot LTV)/D\) |
| 错误点 | Aave HF 应基于 **Liquidation Threshold**，不是 LTV |
| 更新 | Aave：\(HF_t=\sum(V_{i,t}\cdot LT_i)/D_t\)；其他协议用原生机制；跨协议改 Distance-to-Liquidation |
| 级别 | **硬错误，必须改** |

### D2. 主动/被动规则

| 项目 | 内容 |
|---|---|
| 原文 | `msg.sender == borrower` ⇒ 主动 |
| 问题 | onBehalfOf、gateway、router、Safe、AA、第三方代还 |
| 更新 | 解析发起者—中间合约—onBehalfOf—受益状态；主样本可先限 EOA；无法分类单独标记 |
| 级别 | **重大操作化缺陷** |

### D3. Supply / Deposit

| 项目 | 内容 |
|---|---|
| 原文 | Deposit/Withdraw 直接代表抵押提供与提取 |
| 问题 | Supply 后未必启用为 collateral |
| 更新 | 增加 collateral-enabled 状态判断；风险减轻变量只计入真正增加缓冲的操作 |
| 级别 | **中高** |

### D4. 频率

| 项目 | 内容 |
|---|---|
| 原文 | 每日频率重构 HF 轨迹；分析单元 borrower-position-month |
| 问题 | 临界分钟/小时级反应被抹平 |
| 更新 | 底层 tx/block 重建；面板可日/月；清算前窗口单独做 event study |
| 级别 | **中高** |

### D5. FlashLoan

| 项目 | 内容 |
|---|---|
| 原文 | 用于识别复杂策略 |
| 更新 | 保留；但明确 FlashLoan 路径默认不进入“普通主动风险管理”主样本，或单列 |
| 级别 | 中 |

---

## E. 结果解释与贡献表述

### E1. Liquidation 的理论地位

| 原风险 | 更新 |
|---|---|
| 把 future liquidation 当作 credit outcome | 改为 liquidation propensity / forced deleveraging outcome |
| 讨论中连接“信用风险工具” | 可写“风险早期信号”，慎写“信用评分已改进” |

### E2. 前景理论贡献句

| 原倾向 | 更新 |
|---|---|
| 较容易写成“提供前景理论在 DeFi 中的系统证据” | 先写行为结构是否存在；前景理论仅作候选解释之一 |
| HF=1 作为干净参照点 | 补充：它同时也是协议机制阈值，识别不自动等于行为偏差 |

### E3. 实践启示

| 原倾向 | 更新 |
|---|---|
| 协议可引入行为性早期预警 | 保留为潜在启示 |
| 直接导向信用评估改造 | 降级；需先证明增量信息与决策相关量级 |

---

## F. 局限性：把“已有承认”升级为“硬边界”

原 Report 讨论部分其实已承认：

- 用户行为部分可观测
- 无法从链上推断意图
- 外部有效性有限
- 不可观测异质性

本次要求：这些内容从“局限性段落”前移到 **定义与 claim 纪律**，避免前文过强、后文再收回。

新增必须写明的边界：

1. Protocol action ≠ economic purpose  
2. Liquidation ≠ credit default  
3. Public transfer ≠ consumption behavior  
4. Collateral ≠ credit assessment  

---

## G. 因会议而新增、但不并入当前正文主线的内容

| 新认识 | 处理方式 |
|---|---|
| 行业真实需求大量在 settlement 层 | 记入总研究地图 Paper 2，不塞进 Paper 1 |
| KYC + 支付场景才接近行为信用 | Paper 3；当前只作动机与长期问题 |
| 小样本支付数据可能不够建模 | 作为数据可行性约束，防止过早承诺 |
| RWA/应收账款 | 另线记录，不干扰当前借贷行为论文 |
| 纯币质押信贷商业模型脆弱 | 作为动机背景；Paper 1 仍先研究现行 overcollateralized 机制下的行为 |

---

## H. 建议写入 Report v2 的“修订清单”（执行用）

### 必须改（P0）

1. 修正 HF 公式与跨协议风险度量  
2. 升级主动/被动操作化  
3. 区分 Supply 与 collateral-enabled  
4. 全文替换“完全观测行为”为“协议动作高粒度可观测”  
5. RQ2 去 credit-default 化，改 liquidation propensity  

### 应当改（P1）

6. 前景理论改作 framing，不作为开篇既定结论  
7. 增加可观测性分层表（technical / protocol / economic）  
8. 明确日频面板之前有 tx 级重建  
9. 增加 Safe/onBehalfOf 外推限制声明  

### 可后置（P2）

10. Payment/Settlement 专节 → 移到后续研究方向  
11. KYC-行为信用 → 研究展望  
12. 不足额抵押机制文献对话 → 长期主线附录  

---

## I. 一句话对照（适合口述给教授）

> 7 月 Report 的主问题还在，但我会把“信用/行为/结算”这些词收紧：  
> 现在这篇只做 **协议可观测的仓位管理行为 → 清算倾向**；  
> 支付/结算语义和真正的行为信用，放到定义清楚、数据匹配之后的下一阶段。
