# Progress Memo

**To**: Professor Qiao Xiao  
**From**: Yiwei Gan (59765200)  
**Date**: August 12, 2026  
**Subject**: Construct Validity Review of Qualifying Report v1 — Progress and Next Steps

---

## 1. What's New? What Progress Has Been Made?

This week I completed a systematic construct validity review of [Qualifying Report v1](../../04_阶段成果_Milestone_Deliverables/2026-07-17_资格考试报告v1_Qualifying_Report_v1/main.pdf), driven by a realization that my understanding of blockchain platform mechanisms, data structures, and key terminology was insufficient to support my research claims. The work produced four deliverables:

**Six-Layer Matrix Framework (~3,900 lines).** I built a constraint framework requiring every core concept to pass through six layers: Definition → Construct → Measurement → Observable → Identification → Allowed Claim. The principle is that if a claim exceeds what the data can actually observe, it constitutes over-claiming. I filled in this matrix for all 13 core concepts in DeFi lending (Collateral, Position Risk, Health Factor, Distance to Liquidation, Borrow, Repay, Supply vs. Collateral-Enabled, Borrower Adjustment, Active vs. Passive, Liquidation Eligibility, Realized Liquidation, Borrower Identity, Boundary Concepts), and compiled 7 protocol/infrastructure technical documents (Aave V3, Compound III, MakerDAO, Chainlink, Ethereum Finality, Dune Analytics) plus 31 new references across 5 thematic areas.

**Diagnosis of 11 Problems.** Under the framework's constraints, I reviewed Qualifying Report v1 concept by concept and identified 11 problems in three categories:

- **3 Technical Errors (must fix):** (a) The HF formula used LTV instead of Liquidation Threshold; (b) Active/passive classification relied solely on `msg.sender == borrower`, ignoring `onBehalfOf`, multisig wallets, router contracts, and automation services; (c) Supply was equated with Collateral-Enabled, when they are independent states in Aave V3.

- **5 Over-Claims (need downgrading):** (a) "Complete observability of all borrower actions" → downgraded to "complete observability of protocol-level events"; (b) RQ2 named "Credit Layer" → renamed "Liquidation Propensity Layer"; (c) Prospect Theory positioned as "confirmed theory anchor" → downgraded to "compelling competing explanation" (HF=1.0 is both a psychological reference point and a mechanical protocol discontinuity — the two explanations cannot be separated); (d) Liquidation and Default conflated → distinguished throughout; (e) Collateral and Credit conflated → title changed from "Credit Signals" to "Position Management Behavior and Liquidation Risk."

- **3 Terminology Imprecisions (need clarification):** (a) Settlement used without layering; (b) Cross-protocol terminology mixed directly without acknowledging differences; (c) "Credit-relevant information" overused → replaced with "risk-relevant information."

Each problem has a dedicated diagnosis file with the original text quote, error analysis, six-layer matrix mapping, correction plan, and revised LaTeX text.

**Data Feasibility Verification.** I verified item-by-item on Dune Analytics that all data required by the revised research plan is available: 10 protocol event types have decoded tables, key fields (`onBehalfOf`, `repayer`, etc.) are complete, historical LT/LTV parameter changes are trackable via `CollateralConfigurationChanged` events, collateral enable/disable is trackable via `ReserveUsedAsCollateralEnabled/Disabled` events, and HF/Debt can be reconstructed from event data. The only true boundary is borrower economic intent (off-chain, unobtainable) — which is a research boundary, not a data gap.

**Complete Revision Report (~2,080 lines).** All of the above was consolidated into a comprehensive revision report with before/after comparisons, literature change lists, and terminology change lists.

## 2. What Do I Want to Do Next?

1. **Verify terminology accuracy.** Further cross-check all terminology used in the six-layer matrix and diagnosis files against actual protocol mechanisms, eliminating any residual semantic confusion.
2. **Verify whether protocol scope affects data requirements.** The current design uses Aave V3 as the primary protocol with Compound/MakerDAO analyzed separately. I need to confirm whether this scope setting affects the completeness and availability of data needed for the research, and assess whether the protocol coverage range needs adjustment.
3. **Literature search and reading.** Around the revised research questions (position management behavior and liquidation propensity), continue searching for and reading the latest literature on DeFi lending borrower behavior, liquidation prediction, and risk signals.

## 3. What Issues or Difficulties Am I Having?

- **Prospect Theory identification challenge.** HF=1.0 serves as both a psychological reference point (per Prospect Theory) and a mechanical protocol discontinuity (liquidation threshold). These two explanations are observationally equivalent in the data — I cannot separate them without a special identification strategy. I have downgraded PT from "confirmed anchor" to "compelling competing explanation," but I am unsure whether this is the right treatment or whether a sharper identification approach exists.

- **Reconstruction cost for HF and Debt.** While all input data is available on Dune, reconstructing historical Health Factor and Debt values for every borrower position requires significant programming effort (processing event logs, maintaining state snapshots, handling interest accrual). The computational cost and potential for edge-case errors (e.g., position transfers, EMode switches, isolation mode) are a practical concern.

- **Protocol scope uncertainty.** I revised the scope from "three protocols pooled" to "Aave V3 primary, Compound/MakerDAO separate," but I have not yet confirmed whether Compound III and MakerDAO have the same level of decoded table availability and event granularity on Dune as Aave V3. If they do not, the external validity checks may be limited.

## 4. Anything Else I Need Feedback On?

1. **Is the six-layer matrix framework the right level of rigor?** It is quite granular (13 concepts × 6 layers). Is this over-engineering for a qualifying report, or is this the level of construct validity scrutiny expected at this stage?

2. **Prospect Theory positioning.** I would appreciate your view on whether downgrading PT to "compelling competing explanation" is appropriate, or whether there is a better framing that preserves the behavioral insight while acknowledging the identification problem.

3. **Protocol scope.** Does the Aave V3-primary design seem reasonable, or should I invest in making Compound III and MakerDAO equally deep before proceeding?

4. **Priority for next steps.** Given the current state, should I prioritize (a) beginning data acquisition and reconstruction on Dune, (b) writing Report v2 based on the correction plans, or (c) deepening the literature review? I am currently leaning toward (a) and (c) in parallel before starting (b).

---

*All deliverables are available in the GitHub repository: https://github.com/GawainGan/CityU-BlockChain-Finance-Behavior*