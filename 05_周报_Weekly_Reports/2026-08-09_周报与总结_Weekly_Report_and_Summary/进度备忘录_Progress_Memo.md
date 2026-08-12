# Progress Memo

**To**: Professor Qiao Xiao  
**From**: Yiwei Gan (59765200)  
**Date**: August 12, 2026  
**Subject**: Construct Validity Review of Qualifying Report v1 — Progress and Next Steps

---

## 1. What's New? What Progress Has Been Made?

This week I completed a systematic construct validity review of [Qualifying Report v1](../../04_阶段成果_Milestone_Deliverables/2026-07-17_资格考试报告v1_Qualifying_Report_v1/main.pdf), driven by a realization that my understanding of blockchain platform mechanisms, data structures, and key terminology was insufficient to support my research claims. The work produced four deliverables:

**Six-Layer Matrix Framework.** I built a constraint framework requiring every core concept to pass through six layers: Definition → Construct → Measurement → Observable → Identification → Allowed Claim. The principle is that if a claim exceeds what the data can actually observe, it constitutes over-claiming. I filled in this matrix for all 13 core concepts in DeFi lending (Collateral, Position Risk, Health Factor, Distance to Liquidation, Borrow, Repay, Supply vs. Collateral-Enabled, Borrower Adjustment, Active vs. Passive, Liquidation Eligibility, Realized Liquidation, Borrower Identity, Boundary Concepts), and compiled 7 protocol/infrastructure technical documents (Aave V3, Compound III, MakerDAO, Chainlink, Ethereum Finality, Dune Analytics) plus 31 new references across 5 thematic areas.

**Diagnosis of 11 Problems.** Under the framework's constraints, I reviewed Qualifying Report v1 concept by concept and identified 11 problems in three categories:

- **3 Technical Errors (must fix):** (a) The HF formula used LTV instead of Liquidation Threshold; (b) Active/passive classification relied solely on `msg.sender == borrower`, ignoring `onBehalfOf`, multisig wallets, router contracts, and automation services; (c) Supply was equated with Collateral-Enabled, when they are independent states in Aave V3.

- **5 Over-Claims (need downgrading):** (a) "Complete observability of all borrower actions" → downgraded to "complete observability of protocol-level events"; (b) RQ2 named "Credit Layer" → renamed "Liquidation Propensity Layer"; (c) Prospect Theory positioned as "confirmed theory anchor" → downgraded to "compelling competing explanation" (HF=1.0 is both a psychological reference point and a mechanical protocol discontinuity — the two explanations cannot be separated); (d) Liquidation and Default conflated → distinguished throughout; (e) Collateral and Credit conflated → title changed from "Credit Signals" to "Position Management Behavior and Liquidation Risk."

- **3 Terminology Imprecisions (need clarification):** (a) Settlement used without layering; (b) Cross-protocol terminology mixed directly without acknowledging differences; (c) "Credit-relevant information" overused → replaced with "risk-relevant information."

Each problem has a dedicated diagnosis file with the original text quote, error analysis, six-layer matrix mapping, correction plan, and revised LaTeX text.

**Data Feasibility Verification.** I verified item-by-item on Dune Analytics that all data required by the revised research plan is available: 10 protocol event types have decoded tables, key fields (`onBehalfOf`, `repayer`, etc.) are complete, historical LT/LTV parameter changes are trackable via `CollateralConfigurationChanged` events, collateral enable/disable is trackable via `ReserveUsedAsCollateralEnabled/Disabled` events, and HF/Debt can be reconstructed from event data. The only true boundary is borrower economic intent (off-chain, unobtainable) — which is a research boundary, not a data gap.

## 2. What Do I Want to Do Next?

1. **Verify terminology accuracy.** Further cross-check all terminology used in the six-layer matrix and diagnosis files against actual protocol mechanisms, eliminating any residual semantic confusion.
2. **Verify whether protocol scope affects data requirements.** The current design uses Aave V3 as the primary protocol with Compound/MakerDAO analyzed separately. I need to confirm whether this scope setting affects the completeness and availability of data needed for the research, and assess whether the protocol coverage range needs adjustment.
3. **Literature search and reading.** Around the revised research questions (position management behavior and liquidation propensity), continue searching for and reading the latest literature on DeFi lending borrower behavior, liquidation prediction, and risk signals.
4. **Understand Oracle mechanisms and their impact on on-chain asset values.** I have noticed that the value of on-chain assets is not determined entirely by intra-chain transactions — it also depends on an "invisible" external component: the oracle. The oracle's role is to bring external world information (such as market prices of assets) into on-chain protocols. In Aave V3, for example, Chainlink serves as the price oracle; Chainlink aggregates prices from multiple external data sources and submits them on-chain. This means the "price" the protocol sees is not generated within the chain — it is a mapping of the external world. If the oracle experiences latency, bias, or manipulation (e.g., a flash loan attack causing momentary price distortion), it directly affects the protocol's core computations: HF changes, liquidation triggers, collateral valuation, borrowing capacity, etc. — which in turn affect borrowers' repayment, staking, and liquidation behavior. In other words, the oracle is the channel through which "the external world influences the on-chain world." What I need to figure out is: in my research, should I treat the oracle as an external factor that needs to be modeled and analyzed separately, or can I treat on-chain transactions (including oracle inputs) as a unified whole without disentangling "external world impact on the on-chain world"? This is a question about research boundary definition. I will first search for and read literature on oracle mechanisms and their impact on DeFi protocols before deciding how to handle it.

## 3. What Issues or Difficulties Am I Having?

- **Prospect Theory positioning and identification challenge.**

  **Background**: Prospect Theory (Kahneman & Tversky) is a behavioral economics theory about how people make decisions under risk — people do not evaluate outcomes in absolute terms, but relative to a "reference point." Above the reference point (gains), people tend to be risk-averse; below it (losses), people tend to be risk-seeking. Moreover, losses feel more painful than equivalent gains feel pleasurable (loss aversion).

  **How it was used in Report v1**: I used Health Factor (HF) = 1.0 as the borrower's psychological reference point. The theoretical expectation was that borrowers would anchor to HF=1.0, with behavioral patterns shifting as HF approaches 1.0 — just as people anchor to a certain wealth level as a reference point. PT was positioned as the "confirmed theory anchor" of the research, i.e., its theoretical cornerstone.

  **The problem**: HF=1.0 is not just a psychological reference point — it is simultaneously the protocol's mechanical liquidation threshold. When HF drops below 1.0, any liquidator can trigger liquidation. Therefore, the behavioral change observed around HF=1.0 has two possible explanations:

  - Explanation A (psychological mechanism): Borrowers perceive HF approaching 1.0 and exhibit risk-averse or risk-seeking behavioral reactions (Prospect Theory).
  - Explanation B (mechanical mechanism): Protocol rules produce a structural change at HF=1.0 — borrowers' behavioral changes are mechanically triggered by the protocol, not psychologically driven.

  These two explanations produce identical observable patterns in the data (behavioral discontinuity at HF=1.0). I cannot distinguish which mechanism is at work from the data alone. Therefore, I downgraded PT from "confirmed theory anchor" to "compelling competing explanation" — not because PT itself is wrong, but because I cannot prove that the behavioral change is driven by the psychological mechanism rather than the mechanical mechanism.

  **My confusion**: I am not sure whether this "downgrade" is the right treatment, and I do not know whether a better identification strategy exists to separate these two explanations.

- **Reconstruction cost for HF and Debt.**

  **Background**: The data feasibility verification confirmed that all input data is available on Dune, but "available" does not mean "ready to use." HF and Debt are not stored as historical snapshots in Aave V3 — the protocol only records events (Supply, Borrow, Repay, Liquidation, price updates, etc.). The researcher must reconstruct HF and Debt values for each position at each point in time from these events.

  **The difficulty**: This means processing the full event history of every position, maintaining running state snapshots, handling interest accrual and price updates, and dealing with edge cases (e.g., position transfers, EMode switches, Isolation Mode). The computational cost depends on the number of positions and events, which could be very large. Additionally, edge-case error handling (e.g., LT value jumps during EMode switches) can easily introduce reconstruction errors. This is feasible, but the cost and error risk need careful evaluation.

- **Protocol scope uncertainty.**

  **Background**: "Protocol scope" refers to which DeFi lending protocols the study covers. Report v1 originally planned to pool data from three protocols — Aave, Compound, and MakerDAO — into a single panel dataset for analysis.

  **The problem**: These three protocols have fundamentally different architectures — different event structures, different risk parameters, different ways of handling collateral and liquidation. Treating them as the same thing and pooling the data could produce misleading results (analogous to pooling bank loan data and pawnshop loan data together without distinguishing them).

  **The revision**: Changed to Aave V3 as the primary protocol, with Compound/MakerDAO analyzed separately as external validity checks (rather than pooled together).

  **Remaining uncertainty**: I have not yet confirmed whether Compound III and MakerDAO have the same level of decoded table availability and event granularity on Dune as Aave V3. If they do not, the external validity checks may be limited.

## 4. Anything Else I Need Feedback On?

1. **Is the six-layer matrix framework the right level of rigor?** It is quite granular (13 concepts × 6 layers). Is this over-engineering at this stage, or is this the level of construct validity scrutiny expected at this stage?

2. **Prospect Theory positioning.** As described above, I downgraded PT from "confirmed theory anchor" to "compelling competing explanation" because the behavioral change at HF=1.0 cannot be distinguished in the data as psychological vs. mechanical in origin. I would appreciate your view — is this downgrade appropriate? Is there a better framing that preserves the behavioral insight while acknowledging the identification problem? Or is there an identification strategy I have not considered that could separate these two explanations?

3. **Protocol scope.** "Protocol scope" refers to which DeFi lending protocols the study covers. The current design uses Aave V3 as the primary protocol with Compound/MakerDAO analyzed separately. Does this seem reasonable, or should I invest in making Compound III and MakerDAO equally deep before proceeding? However, this investigation would require deep information matching and would be very time-consuming.

4. **Priority for next steps.** Given the current state, should I prioritize (a) beginning data acquisition and reconstruction on Dune, (b) writing Report v2 based on the correction plans, or (c) deepening the literature review? I am currently leaning toward (a) and (c) in parallel before starting (b).

---

*All deliverables are available in the GitHub repository: https://github.com/GawainGan/CityU-BlockChain-Finance-Behavior*
