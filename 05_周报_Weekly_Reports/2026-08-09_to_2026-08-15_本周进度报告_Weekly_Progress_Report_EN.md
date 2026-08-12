# Weekly Report: 2026-08-09 to 2026-08-15

**Reporting Period**: August 9, 2026 — August 15, 2026  
**Research Direction**: Borrower Behavioral Risk and Liquidation Prediction in DeFi Lending Markets (tentative)

---

## 1. Overview of This Week's Work

The core work this week was: **conducting a systematic construct validity review of Paper 1 (Qualifying Report v1), identifying and correcting 11 problems, verifying the feasibility of data required for the research, and producing a comprehensive revision report.**

The work originated from a conversation on August 9 with an industry contact (regarding the blockchain payment dilemma), which revealed deep semantic and conceptual problems in Report v1. The central question that guided all subsequent work was: *"How can we ensure that our research claims remain consistent with our data capabilities?"* Four major tasks were completed around this question:

| # | Task | Output | File Location |
|---|------|--------|---------------|
| 1 | Identified semantic problems; built a constraint framework | Six-layer matrix framework (13 concepts × 6 layers + literature + technical docs + non-claims list + terminology table) | [Six_Layer_Matrix](../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_六层矩阵_Paper1_Six_Layer_Matrix) |
| 2 | Diagnosed Report v1 problems using the constraint framework | Diagnosis and correction plans for 11 problems | [Diagnosis_and_Fix](../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_诊断改进映射_Paper1_Diagnosis_and_Fix) |
| 3 | Verified research data feasibility | Item-by-item verification of data availability on the Dune platform | [Data_Feasibility](../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_数据可行性验证_Paper1_Data_Feasibility) |
| 4 | Consolidated revision content | Complete revision report (with before/after comparisons, literature changes, terminology changes) | [Revision_Report](../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_Report_v1修订报告_Revision_Report.md) |

---

## 2. Detailed Description of This Week's Work

### 2.1 Starting Point: Semantic Problems Discovered Through Communication

On August 9, during a conversation with an industry contact about the blockchain payment dilemma, we discussed the conceptual boundaries between on-chain Transfer, Payment, and Settlement. This discussion made me realize a deeper issue: **multiple core concepts used in Report v1 suffer from semantic confusion — not as isolated typos, but as a systematic construct validity problem.**

Specifically, the semantic problems identified during the discussion include:

- **Collateral ≠ Credit**: DeFi lending is collateral-backed lending, not traditional credit lending. Report v1's title uses "Credit Signals," but the actual research studies position risk signals.
- **Liquidation ≠ Default**: Liquidation (position-level, mechanically triggered) is not the same as credit default (borrower-level, solvency failure), yet Report v1 conflates them in multiple places.
- **Supply ≠ Collateral-Enabled Supply**: In Aave V3, supplying an asset and enabling it as collateral are two independent operations, but Report v1 treats them as equivalent.
- **"Complete observability" is too strong**: On-chain data can only observe protocol events, not economic motives or off-chain behavior.

These problems made it clear that a systematic framework was needed to audit whether each concept's "claims" and "data capabilities" remain consistent.

### 2.2 Building the "Six-Layer Matrix" Constraint Framework

To systematically audit construct validity, I built a "Six-Layer Matrix" framework. Each core concept must pass through six layers of scrutiny:

```
Definition → Construct → Measurement
→ Observable → Identification → Allowed Claim
```

**Core Principle**: If the claim at Layer 6 exceeds what Layer 4 (Observable) can support, it constitutes over-claiming.

**Outputs** (paths relative to [`2026-08-11_六层矩阵_Paper1_Six_Layer_Matrix/`](../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_六层矩阵_Paper1_Six_Layer_Matrix)):

| File | Content |
|------|---------|
| [`00_说明_README.md`](../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_六层矩阵_Paper1_Six_Layer_Matrix/00_说明_README.md) | Framework navigation and usage instructions |
| [`01_六层矩阵总表_Master_Matrix_Table.md`](../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_六层矩阵_Paper1_Six_Layer_Matrix/01_六层矩阵总表_Master_Matrix_Table.md) | Master table of 12 in-scope concepts + 6 boundary concepts |
| [`02_逐概念六层矩阵_Per_Concept_Matrices/`](../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_六层矩阵_Paper1_Six_Layer_Matrix/02_逐概念六层矩阵_Per_Concept_Matrices) | 13 per-concept files (Collateral, Position Risk, Health Factor, Distance to Liquidation, Borrow, Repay, Supply vs Collateral-Enabled, Borrower Adjustment, Active vs Passive, Liquidation Eligibility, Realized Liquidation, Borrower Identity, Boundary Concepts) |
| [`03_技术文档_Technical_Docs/`](../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_六层矩阵_Paper1_Six_Layer_Matrix/03_技术文档_Technical_Docs) | 7 protocol/infrastructure documents (Aave V3, Compound III, MakerDAO, Chainlink, Ethereum Finality, Dune Analytics) |
| [`04_文献_Literature/`](../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_六层矩阵_Paper1_Six_Layer_Matrix/04_文献_Literature) | Literature organized under 5 themes (Blockchain Foundation, Collateral & Credit, DeFi Lending, Alternative Data & Credit Scoring, Payment & Settlement), totaling 31 newly added references |
| [`05_不可声称清单_Non_Claims_List.md`](../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_六层矩阵_Paper1_Six_Layer_Matrix/05_不可声称清单_Non_Claims_List.md) | 9 categories of non-claims (40+ items) |
| [`06_术语边界对照表_Terminology_Boundary_Reference.md`](../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_六层矩阵_Paper1_Six_Layer_Matrix/06_术语边界对照表_Terminology_Boundary_Reference.md) | Term ≠ mapping + cross-protocol mapping + correct wording substitutions |

The six-layer matrix totals approximately 3,900 lines, ensuring that every layer of every concept has a clear definition and that boundaries between concepts are unambiguous.

### 2.3 Diagnosing Report v1 Using the Constraint Framework

Under the constraints of the six-layer matrix, I conducted a per-concept review of Report v1 and identified 11 problems, classified by severity into three categories:

**🔴 Technical Errors (3) — Must Fix**:

| Problem | Core Error | Correction Plan |
|---------|-----------|-----------------|
| HF formula uses LTV instead of LT | Aave V3's HF uses Liquidation Threshold, not LTV. The two parameters have similar numerical values but different functions. | Replace LTV with LT in the formula, and document different LT values under EMode/Isolation Mode |
| Active/passive classification uses only msg.sender == borrower | Ignores onBehalfOf, Safe multisig wallets, Router contracts, automation services, credit delegation | Design multi-layer classification rules: onBehalfOf + known contract address registry + trace call chain |
| Supply equated with Collateral | In Aave V3, Supply and Collateral-Enabled are independent states | Add ReserveUsedAsCollateralEnabled/Disabled event tracking; distinguish regular Supply from collateral operations |

**🟡 Over-Claims (5) — Need Downgrading**:

| Problem | Original Claim | Corrected |
|---------|---------------|-----------|
| "Complete observability" | "complete observability of all borrower actions" | "complete observability of protocol-level events" |
| RQ2 named "Credit Layer" | The research studies liquidation prediction, not credit assessment | Renamed to "Liquidation Propensity Layer" |
| Prospect Theory positioned too strongly | Positioned as "confirmed theory anchor" | Downgraded to "compelling competing explanation" (HF=1.0 is both a psychological reference point and a mechanical protocol discontinuity — the two explanations cannot be separated) |
| Liquidation and Default conflated | Multiple instances equate liquidation with default | Distinguish throughout the paper; add terminology declaration |
| Collateral and Credit conflated | Title "Credit Signals"; "credit" used throughout | Changed to "Position Management Behavior and Liquidation Risk"; retain "credit" only for traditional finance comparisons |

**🔵 Terminology Imprecision (3) — Need Clarification**:

| Problem | Correction Plan |
|---------|-----------------|
| Settlement used without layering | Use "repayment" instead, or annotate Technical / Protocol / Economic layers |
| Cross-protocol terminology mixed directly | Aave V3 as primary protocol; Compound/MakerDAO analyzed separately (no panel pooling) |
| "Credit-relevant information" overused | Replace throughout with "risk-relevant information" or "liquidation-relevant information" |

**Outputs**: 11 per-problem diagnosis files, each containing: Report v1 original text quote → error analysis (with examples) → six-layer matrix mapping → correction plan → revised LaTeX text → supporting literature.

### 2.4 Verifying Research Data Feasibility

After completing the diagnosis and corrections, I realized a critical question: **is the data we claim to use actually available on the data platform?**

To answer this, I conducted an item-by-item verification of Dune Analytics (the selected data platform):

**Verification Method**:
1. Confirmed data architecture from Dune's official documentation (three layers: Raw / Decoded / Curated)
2. Confirmed Aave V3 table names and fields from actual query examples on Dune
3. Confirmed event signatures from the Aave V3 GitHub source code
4. Cross-verified event signatures from Gnosis Analytics documentation

**Verification Results**:

| Data Requirement | Availability | Notes |
|-----------------|-------------|-------|
| 10 protocol event types (Supply, Borrow, Repay, LiquidationCall, etc.) | ✅ All available | `aave_v3_ethereum.Pool_evt_*` decoded tables on Dune |
| Key fields (onBehalfOf, repayer, etc.) | ✅ Complete | Supports the revised multi-layer classification scheme |
| Historical LT/LTV parameter changes | ✅ Trackable | `PoolConfigurator_evt_CollateralConfigurationChanged` event |
| Collateral enable/disable status | ✅ Trackable | `Pool_evt_ReserveUsedAsCollateralEnabled/Disabled` events |
| EMode status and configuration | ✅ Trackable | `Pool_evt_UserEModeSet` + `PoolConfigurator_evt_EModeCategoryAdded/Updated` |
| Token prices | ✅ Available | `prices.usd` curated table |
| Token metadata (decimals) | ✅ Available | `tokens.erc20` curated table |
| Transaction/Trace data | ✅ Available | `ethereum.transactions` / `ethereum.traces` |
| Address labels | ✅ Available | `labels.labels` (requires supplementary manual contract address list) |
| Historical HF values | ✅ Reconstructable | All input data available; requires researcher-programmed reconstruction |
| Historical Debt values | ✅ Reconstructable | Same as above |
| Borrower economic intent | ❌ Not obtainable | Off-chain information; constitutes a research boundary (not a data gap) |

**Corrected errors in prior technical documentation**: The Aave V3 Dune table name prefix is `Pool_evt_*` (not `LendingPool_evt_*`), and collateral enable/disable consists of two separate events (`ReserveUsedAsCollateralEnabled/Disabled`, not `SetUserUseReserveAsCollateral`).

### 2.5 Producing the Complete Revision Report

Finally, I consolidated all of the above work into a comprehensive revision report ([Report_v1修订报告_Revision_Report.md](../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_Report_v1修订报告_Revision_Report.md), approximately 2,080 lines), containing:

1. **Overview and Background**: Explains construct validity issues; provides foundational concept explanations for readers without a blockchain finance background
2. **Problem Overview**: Classification and relationship diagram of the 11 problems
3. **Per-Problem Detailed Description**: Each problem presented in accessible language + examples + before/after comparisons + literature support
4. **Literature Change List**: 31 newly added references + 12 retained references + time-gradient distribution
5. **Terminology Change List**: 17 removed terms + 17 new terms + change summary diagram
6. **Information Sources**: Traceable sources for all information

---

## 3. Summary of This Week's Output Files

All output files are organized under the [2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification](../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification) folder:

```
2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/
├── 2026-08-09_老曹沟通_衍生资料_Derivative_Materials/          ← Work starting point
├── 2026-08-11_定义数据范围纠错_Definition_Data_Scope_Corrections/  ← Initial correction package
├── 2026-08-11_六层矩阵_Paper1_Six_Layer_Matrix/               ← Constraint framework (~3,900 lines)
│   ├── 00_说明_README.md
│   ├── 01_六层矩阵总表_Master_Matrix_Table.md
│   ├── 02_逐概念六层矩阵_Per_Concept_Matrices/ (13 concept files)
│   ├── 03_技术文档_Technical_Docs/ (7 protocol/platform docs)
│   ├── 04_文献_Literature/ (5 themes, 31 references)
│   ├── 05_不可声称清单_Non_Claims_List.md
│   └── 06_术语边界对照表_Terminology_Boundary_Reference.md
├── 2026-08-11_诊断改进映射_Paper1_Diagnosis_and_Fix/           ← Problem diagnosis and corrections (~1,880 lines)
│   ├── 00_说明_README.md
│   ├── 01_问题总表_Problem_Summary.md
│   └── 02_逐问题诊断与改进_Per_Problem_Diagnosis/ (11 problem files)
├── 2026-08-11_数据可行性验证_Paper1_Data_Feasibility/         ← Data feasibility verification (~2,320 lines)
│   ├── 00_说明_README.md
│   ├── 01_数据需求与平台映射总表_Data_Requirements_Mapping.md
│   ├── 02_数据可行性评估_Feasibility_Assessment.md
│   ├── 03_Dune数据平台_Dune_Platform/ (5 platform docs)
│   ├── 04_数据缺口与解决方案_Data_Gaps_and_Solutions.md
│   └── 05_信息来源汇总_Information_Sources.md
└── 2026-08-11_Report_v1修订报告_Revision_Report.md            ← Complete revision report (~2,080 lines)
```

---

## 4. Overall Changes After Revision

| Dimension | Report v1 | After Revision |
|-----------|---------|--------|
| Core claim | "Borrower behavior provides credit signals" | "Protocol-observable position management behavior provides incremental information on liquidation propensity" |
| Theoretical positioning | Prospect Theory as confirmed theory anchor | Prospect Theory as a compelling competing explanation (HF=1.0 is both a psychological reference point and a mechanical protocol discontinuity) |
| Research outcomes | Liquidation / Default conflated | Liquidation eligibility / Realized liquidation distinguished |
| Observability | "Complete observability" | "Protocol events observable; economic motives not observable" |
| Protocol scope | Aave + Compound + MakerDAO directly pooled | Aave V3 as primary; Compound/MakerDAO analyzed separately as external validity checks |
| Collateral | Supply = Collateral | Supply ≠ Collateral-Enabled Supply (requires tracking independent events) |
| Active/Passive | msg.sender == borrower | Multi-layer classification: onBehalfOf + known contract address registry + trace call chain |
| HF formula | Uses LTV | Uses LT (Liquidation Threshold) |

---

## 5. Next Steps

I will continue working on the following at the current stage:

1. **Verify terminology accuracy**: Conduct further cross-checking of the terminology used in the six-layer matrix and the diagnosis-and-fix mapping, ensuring that each concept's definition, construct, and actual protocol mechanism are fully consistent, and eliminating any residual semantic confusion.
2. **Verify the impact of protocol scope on data requirements**: Confirm whether the current protocol scope setting — with Aave V3 as primary and Compound/MakerDAO analyzed separately — affects the completeness and availability of data needed for the research, and assess whether the protocol coverage range needs to be adjusted.
3. **Literature search and reading**: Around the revised research questions (position management behavior and liquidation propensity), continue searching for and reading relevant literature, with a focus on supplementing the latest research in directions such as DeFi lending borrower behavior, liquidation prediction, and risk signals.
