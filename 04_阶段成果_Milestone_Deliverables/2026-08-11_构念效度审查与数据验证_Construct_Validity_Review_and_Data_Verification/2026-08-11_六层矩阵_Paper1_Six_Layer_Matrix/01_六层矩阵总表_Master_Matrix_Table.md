# 六层矩阵总表

**日期**：2026-08-11  
**用途**：将 Paper 1 所有核心概念压缩到一张总表，供快速查阅与交叉验证  
**详细展开**：见 `02_逐概念六层矩阵/` 下的对应文件

---

## In-Scope 概念总表

| 概念 | Definition | Construct | Measurement | Observable | Cannot Identify | Allowed Claim |
|------|------------|-----------|-------------|------------|-----------------|---------------|
| **Collateral** | 为覆盖偿付义务而预先锁定、可被协议强制执行处置的资产 | 损失吸收 + 激励 + 风险缓冲（不等于信用评估） | 仓位中的锁定资产种类与数量 × 预言机价格 | ✅ 高：合约状态 + 事件 | ❌ 完整借款人信用能力；❌ 借款人未来偿付意愿 | collateralization state（不声称 creditworthiness） |
| **Position Risk** | 协议定义的仓位距离 liquidation boundary 的状态 | 仓位风险水平（position-level，非 borrower-level） | 协议原生风险指标 × 预言机价格 / 债务 | ✅ 高：可从合约状态重建 | ❌ 借款人整体资产组合风险；❌ 链下对冲后的净风险 | position risk（不声称 credit risk） |
| **Health Factor** | Aave 中 collateral 加权 liquidation threshold 与债务之比 | Aave 特有的仓位风险度量 | HF = Σ(V_i × LT_i) / D（用 LT 不用 LTV） | ✅ 高：可从 Aave 合约参数 + 状态重建 | ❌ Compound/Maker 的等价指标（不同机制） | Aave-specific HF（跨协议需标准化） |
| **Distance to Liquidation** | 仓位距协议特定清算边界的标准化距离 | 跨协议可比的仓位风险度量 | 各协议原生风险指标 → 标准化转换 | ✅ 高（各协议分别重建后） | ❌ 统一的 HF 跨协议比较（需标准化） | protocol-normalized distance-to-liquidation |
| **Borrow** | 协议中创建债务的链上动作 | 协议级借贷行为（非经济动机） | Borrow 事件解析：金额、资产、时间、利率模式 | ✅ 高：合约事件 | ❌ 借款动机；❌ 借款人整体杠杆 | borrowing action（不声称 borrowing purpose） |
| **Repay** | 协议中减少债务的链上动作 | 协议级还款行为（非还款动机） | Repay 事件解析：金额、资产、时间 | ✅ 高：合约事件 | ❌ 还款动机；❌ 资金来源 | repayment action（不声称 repayment motive） |
| **Supply vs Collateral-Enabled** | Supply = 存入资产；Collateral-Enabled = 该资产被启用为抵押 | 供给动作 ≠ 风险缓冲增加 | 区分 Supply 事件与 setUserUseReserveAsCollateral 事件 | ✅ 高：可从事件日志区分 | ❌ 用户是否"打算"将其作为抵押 | collateral-enabled supply（不把所有 supply 当抵押追加） |
| **Borrower Adjustment** | 由 borrower 或 borrower-authorized entity 触发、改变仓位风险状态的协议动作 | 协议可观测的仓位管理行为过程 | 主动动作序列：时间、类型、幅度、延迟、一致性 | ✅ 中高：需解析 initiator → onBehalfOf → beneficiary | ❌ 动作的真实经济动机；❌ 借款人完整经济行为 | protocol-observable position-management behavior |
| **Active vs Passive** | 主动 = borrower-authorized action；被动 = 第三方/协议触发 | 行为归属分类 | 解析 initiator → intermediate → onBehalfOf → beneficiary → state change | ✅ 中高：需多层解析 | ❌ Safe/AA/代理路径下的确切决策者 | borrower-authorized action（无法分类单独标记） |
| **Liquidation Eligibility** | 仓位已满足协议清算条件的状态 | 仓位进入可被清算的机械状态 | 协议原生风险指标跨越阈值（如 HF < 1） | ✅ 高：可从重建状态判断 | ❌ 借款人偿付能力；❌ 是否会被实际清算 | liquidatable state / position distress |
| **Realized Liquidation** | 清算机制实际执行的强制风险处置 | 强制去杠杆 / 仓位风险实现 | LiquidationCall 事件：清算金额、罚金、清算人 | ✅ 高：合约事件 | ❌ 传统信用违约；❌ 借款人偿付能力/意愿 | realized liquidation / forced deleveraging |
| **Borrower Identity** | 与协议交互的钱包地址 | 链上操作实体（非自然人） | 地址 + 实体标签（如有） | ✅ 中：地址确定；❌ 实体归属需推断 | ❌ 自然人身份；❌ 跨地址同一人 | entity/address（不声称 natural person） |

---

## Boundary 概念总表（不在 Paper 1 范围内）

| 概念 | Definition | 为什么不在 Paper 1 | Paper 1 中的处理 |
|------|------------|-------------------|-----------------|
| **Transfer** | 链上 token 所有权/余额状态变化 | Paper 1 研究协议事件，不是普通转账 | 不直接使用 |
| **Payment** | 产生付款行为或付款义务 | 需要 economic purpose 识别 → Paper 2 | 不声称 |
| **Settlement** | 对既有义务的最终确认与履行 | 需要 legal discharge → Paper 2 | 不声称 |
| **Finality** | 共识不可逆性 | 技术层概念，不等于经济结算 | 仅用于数据可靠性声明 |
| **Default** | 借款人无法/不愿偿付的信用事件 | DeFi liquidation ≠ 传统 default | 不使用此词替代 liquidation |
| **Creditworthiness** | 对主体未来偿付可信度的判断 | 需要身份 + 行为 + 信用结果 → Paper 3 | 不声称 |

---

## 关键不等式（写论文时必须遵守）

```
Protocol Action ≠ Economic Purpose
Liquidation ≠ Credit Default
Collateral ≠ Creditworthiness
On-chain Transfer ≠ Observed Payment Purpose
Payment ≠ Settlement
Settlement ≠ Liquidation
Staking ≠ Collateralization
Supply ≠ Collateral-Enabled Supply
Health Factor (Aave) ≠ Account Liquidity (Compound) ≠ Collateralization Ratio (Maker)
Behavioral Process Variable ≠ Creditworthiness Itself
```

---

## 详细文件索引

| 概念 | 详细文件 | 相关技术文档 | 相关文献主题 |
|------|---------|-------------|-------------|
| Collateral | `02_逐概念六层矩阵/01_Collateral_抵押.md` | `03_技术文档/01_Aave_V3.md` | `04_文献/02_Collateral_Credit/` |
| Position Risk | `02_逐概念六层矩阵/02_Position_Risk_仓位风险.md` | `03_技术文档/01_Aave_V3.md`, `02_Compound_III.md` | `04_文献/03_DeFi_Lending/` |
| Health Factor | `02_逐概念六层矩阵/03_Health_Factor_健康因子.md` | `03_技术文档/01_Aave_V3.md` | `04_文献/03_DeFi_Lending/` |
| Distance to Liquidation | `02_逐概念六层矩阵/04_Distance_to_Liquidation_清算距离.md` | `03_技术文档/01_Aave_V3.md`, `02_Compound_III.md`, `03_MakerDAO_Sky.md` | `04_文献/03_DeFi_Lending/` |
| Borrow | `02_逐概念六层矩阵/05_Borrow_借款.md` | `03_技术文档/01_Aave_V3.md` | `04_文献/03_DeFi_Lending/` |
| Repay | `02_逐概念六层矩阵/06_Repay_还款.md` | `03_技术文档/01_Aave_V3.md` | `04_文献/03_DeFi_Lending/` |
| Supply vs Collateral-Enabled | `02_逐概念六层矩阵/07_Supply_vs_CollateralEnabled_供给与抵押启用.md` | `03_技术文档/01_Aave_V3.md` | `04_文献/03_DeFi_Lending/` |
| Borrower Adjustment | `02_逐概念六层矩阵/08_Borrower_Adjustment_借款人调整行为.md` | `03_技术文档/01_Aave_V3.md` | `04_文献/03_DeFi_Lending/`, `04_文献/02_Collateral_Credit/` |
| Active vs Passive | `02_逐概念六层矩阵/09_Active_vs_Passive_主动与被动分类.md` | `03_技术文档/01_Aave_V3.md` | `04_文献/03_DeFi_Lending/` |
| Liquidation Eligibility | `02_逐概念六层矩阵/10_Liquidation_Eligibility_清算资格.md` | `03_技术文档/01_Aave_V3.md`, `02_Compound_III.md` | `04_文献/03_DeFi_Lending/` |
| Realized Liquidation | `02_逐概念六层矩阵/11_Realized_Liquidation_实际清算.md` | `03_技术文档/01_Aave_V3.md` | `04_文献/03_DeFi_Lending/` |
| Borrower Identity | `02_逐概念六层矩阵/12_Borrower_Identity_借款人身份.md` | — | `04_文献/04_Alternative_Data_CreditScoring/` |
| Boundary Concepts | `02_逐概念六层矩阵/13_Boundary_Concepts_边界概念_Transfer_Payment_Settlement.md` | `03_技术文档/05_Ethereum_Finality.md` | `04_文献/05_Payment_Settlement/`, `04_文献/01_Blockchain_Foundation/` |