# V4 研究知识图谱 — Demo（核心演化片段）

## 图例

- 🧠 C: 概念节点（理论构念/假设）
- ⚠️ S: 状态/问题节点（盲点/验证状态）
- 📦 A: 产物节点（文件/提案）
- 🔧 D: 数据/工具节点

Edge 标注格式：`[类型] 具体信息`

---

## 子图：V4→V4_1 核心演化

```mermaid
graph TD
    %% ===== 产物层 =====
    A_V4["📦 A:V4探索稿<br/>(V4_探索文档_公开数据新方向.md)"]
    A_V41["📦 A:V4_1改进提案<br/>(V4_1_改进提案.md)"]
    A_DT["📦 A:主动vs被动决策树<br/>(03_主动vs被动_决策树.md)"]
    A_Dune["📦 A:Dune查询模板<br/>(01_Dune查询模板_操作化说明.md)"]
    A_Lit["📦 A:文献总表<br/>(02_文献总表_RQ映射.md)"]

    %% ===== 概念层 =====
    C_PT["🧠 C:前景理论<br/>(Kahneman & Tversky, 1979)"]
    C_LA["🧠 C:损失厌恶<br/>H1a: λ > 1"]
    C_RP["🧠 C:参考点效应<br/>H1b: HF=1处行为跳变"]
    C_DS["🧠 C:递减敏感性<br/>H1c: 远离HF=1反应钝化"]
    C_BDM["🧠 C:BDM行为偏差指数<br/>5维度含DeFi独有维度"]

    %% ===== 状态/问题层 =====
    S_DA["⚠️ S:决策锚缺失<br/>(V4盲点检查1: 🔴致命)"]
    S_AP["⚠️ S:主动vs被动混淆<br/>(V4盲点检查5: 🔴致命)"]
    S_DA_FIX["⚠️ S:决策锚部分修复<br/>(V4_1: ΔW福利量化)"]
    S_AP_FIX["⚠️ S:分类逻辑已修复<br/>(6类操作+决策树)"]
    S_SAFE["⚠️ S:Safe钱包新风险<br/>(V4_1盲点检查5: 🟡重大)"]
    S_DUNE_OK["⚠️ S:Dune数据已验证可获取<br/>(lending.borrow + LiquidationCall)"]
    S_GAP["⚠️ S:文献缺口已确认<br/>(前景理论×DeFi借贷=空白)"]

    %% ===== 数据/工具层 =====
    D_DUNE["🔧 D:Dune Analytics<br/>(lending.borrow/supply/collateral)"]
    D_SAFE["🔧 D:Safe多签钱包<br/>(tx.from=合约地址≠最终用户)"]
    D_HF["🔧 D:HF自计算管道<br/>(持仓快照+prices.usd)"]

    %% ===== Edges: 致命发现 =====
    A_V4 --X--> S_DA
    A_V4 --X--> S_AP
    S_DA --"盲点1: 无ΔW折算,<br/>论文退化为统计发现"--> S_DA_FIX
    S_AP --"盲点5: 无法区分补救vs清算,<br/>RQ1前景理论检验失效"--> S_AP_FIX

    %% ===== Edges: 演化动机 =====
    S_DA_FIX --E--> A_V41
    S_AP_FIX --E--> A_V41
    S_AP_FIX --O--> A_DT
    S_DA_FIX --O--> A_V41

    %% ===== Edges: 理论支撑 =====
    C_PT --T--> C_LA
    C_PT --T--> C_RP
    C_PT --T--> C_DS
    C_LA --"Arshadi & Kim 2025:<br/>PoS验证者λ>1"--> C_BDM
    C_RP --"Cornelli et al. 2025:<br/>HF近1时选波动抵押品2.3× "--> C_BDM
    C_DS --"Gadzinski & Liuzzi 2025:<br/>清算后30天恢复72%活动"--> C_BDM

    %% ===== Edges: 操作化映射 =====
    C_BDM --"维度3:抵押品切换方向<br/>(Collateral Enable/Disable事件)"--> D_DUNE
    C_RP --"HF=1断点检测<br/>(Bai-Perron + 接近度设计)"--> D_HF
    C_LA --"配对|ΔHF|相同,<br/>比较补救vs增险幅度"--> D_HF

    %% ===== Edges: 数据验证 =====
    D_DUNE --"lending.borrow含transaction_type=liquidation<br/>LiquidationCall含liquidator字段"--> S_DUNE_OK
    D_DUNE --"evm.transactions提供tx.from"--> S_AP_FIX
    S_DUNE_OK --D--> A_DUNE
    S_GAP --D--> A_Lit

    %% ===== 新风险暴露 =====
    S_AP_FIX --"解决分类逻辑后暴露:<br/>tx.from对Safe用户=合约地址"--> S_SAFE
    D_SAFE --"大额用户普遍使用Safe,<br/>Bank of Canada 2026:前10占97%清算量"--> S_SAFE
    S_SAFE --"可能限制RQ1仅对EOA散户成立,<br/>需PoC量化Safe占比"--> A_V41

    %% ===== 样式 =====
    classDef concept fill:#e1f5fe,stroke:#0288d1,stroke-width:2px
    classDef state fill:#fff3e0,stroke:#ef6c00,stroke-width:2px
    classDef artifact fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px
    classDef data fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px

    class C_PT,C_LA,C_RP,C_DS,C_BDM concept
    class S_DA,S_AP,S_DA_FIX,S_AP_FIX,S_SAFE,S_DUNE_OK,S_GAP state
    class A_V4,A_V41,A_DT,A_DUNE,A_Lit artifact
    class D_DUNE,D_SAFE,D_HF data
```

---

## Edge 信息密度说明

每条边必须携带以下信息之一（不能为空）：

| Edge 类型 | 必须信息 | Demo 中的示例 |
|-----------|---------|-------------|
| --T--> 理论支撑 | 作者(年): 具体结论 | "Arshadi & Kim 2025: PoS验证者λ>1" |
| --D--> 数据验证 | 数据源: 验证结果 | "lending.borrow含transaction_type=liquidation" |
| --X--> 致命发现 | 盲点编号: 具体推理 | "盲点1: 无ΔW折算,论文退化为统计发现" |
| --E--> 演化动机 | 驱动力 | "决策锚部分修复→V4_1" |
| --O--> 操作化映射 | 字段/公式 | "维度3: 抵押品切换方向 (Collateral Enable/Disable事件)" |

---

## 设计决策记录

1. **为什么不把文献单独作为节点？** 因为文献的引用总是为了支撑某个具体的推理步骤（edge），文献本身不是我们研究的"概念"。把文献放在 edge 标注中而非独立节点，强制每条引用都必须说明"用这篇文献的什么结论支撑了什么推理"。

2. **为什么状态/问题是一类节点？** 因为研究过程中的关键状态变化（如"盲点发现"、"数据验证通过"）本身是静态事实，但它们对后续路径的影响是动态的。把它们显式化为节点，可以追踪"哪些发现改变了研究走向"。

3. **Safe钱包为什么既是工具节点又是问题来源？** 因为 D:Safe钱包 作为工具是中性的，但它在"主动/被动分类"这个特定操作化路径中制造了测量约束。这个约束通过 edge（而非节点属性）表达。
