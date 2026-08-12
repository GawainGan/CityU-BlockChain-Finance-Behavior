# Research Summary: From Semantic Confusion to Systematic Verification

**Date**: August 12, 2026  
**Research Direction**: Borrower Behavioral Risk and Liquidation Prediction in DeFi Lending Markets

---

## 1. Starting Point: Semantic Confusion Revealed a Knowledge Gap

While writing [Qualifying Report v1](../../04_阶段成果_Milestone_Deliverables/2026-07-17_资格报告v1_Qualifying_Report_v1/main.pdf), I used concepts such as "Credit Signals," "Liquidation," and "Complete Observability" to describe the research problem. However, during a discussion on August 9 with an industry contact about the blockchain payment dilemma, I realized that I did not have a clear understanding of the boundaries between on-chain Transfer, Payment, and Settlement.

This discussion made me realize a deeper problem: **my understanding of blockchain platforms, protocol mechanisms, and data structures was not deep enough, leading to systematic semantic confusion in the concepts and terminology I used in Qualifying Report v1.** These were not isolated typos — they reflected an insufficient grasp of the underlying technical details to support my research claims.

Specifically, I found that I lacked clarity on the following key points:

1. **The boundary between Collateral and Credit**: DeFi lending is over-collateralized lending, not traditional credit lending. I used "credit signals" to describe what is actually position risk signal research, showing that I did not adequately understand the fundamental difference between the two lending paradigms.
2. **The distinction between Liquidation and Default**: Liquidation is a position-level mechanical trigger, while default is a borrower-level solvency failure. I conflated the two in the report, showing that I had not distinguished protocol mechanisms from economic behavior.
3. **The separation of Supply and Collateral-Enabled**: In Aave V3, supplying an asset and enabling it as collateral are two independent operations. I had treated them as equivalent, showing that I was not clear on the actual operational flow of the protocol.
4. **The boundaries of observability**: I claimed "complete observability of all borrower actions," but in reality, on-chain data can only observe protocol events, not economic intent. This showed that I lacked a clear understanding of the boundaries of data capability.

These problems made me realize: **before continuing to advance the research, I must first clarify exactly what I am studying, and whether the data I claim to use is actually usable.**

---

## 2. Step One: Building a Constraint Framework — the Six-Layer Matrix

To systematically audit whether each concept's "claims" and "data capabilities" remain consistent, I built a Six-Layer Matrix framework requiring every core concept to pass through six layers of scrutiny:

> Definition → Construct → Measurement → Observable → Identification → Allowed Claim

The core principle is: **if the claim at Layer 6 exceeds what Layer 4 (Observable) can support, it constitutes over-claiming.**

I filled in this matrix for each of 13 core concepts in DeFi lending, and for each concept I compiled the corresponding technical documentation (Aave V3, Compound III, MakerDAO, Chainlink, Ethereum Finality, Dune Analytics) and relevant literature. This step helped me clarify two things:

- What each concept actually means at the protocol level;
- What can and cannot be observed from data for each concept.

See: [Six Layer Matrix Paper1](../../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_六层矩阵_Paper1_Six_Layer_Matrix)

---

## 3. Step Two: Diagnosing Qualifying Report v1 Using the Constraint Framework

Under the constraints of the Six-Layer Matrix, I conducted a per-concept review of [Qualifying Report v1](../../04_阶段成果_Milestone_Deliverables/2026-07-17_资格报告v1_Qualifying_Report_v1/main.pdf) and identified 11 problems, classified into three categories:

- **3 Technical Errors**: HF formula using LTV instead of LT, oversimplified active/passive classification, and equating Supply with Collateral. These were "I got the protocol mechanism wrong" problems.
- **5 Over-Claims**: Complete observability, Credit Layer naming, Prospect Theory positioned too strongly, Liquidation/Default conflation, and Collateral/Credit conflation. These were "I claimed more than the data can support" problems.
- **3 Terminology Imprecisions**: Settlement used without layering, cross-protocol terminology mixing, and overuse of "credit-relevant information." These were "I used terms carelessly" problems.

For each problem, I wrote a detailed diagnosis file including the original text quote, error analysis, six-layer matrix mapping, and correction plan.

See: [Diagnosis and Fix Paper1](../../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_诊断改进映射_Paper1_Diagnosis_and_Fix)

---

## 4. Step Three: Verifying Whether the Data Is Actually Usable

After completing the diagnosis, I realized a critical question: **is the data I claim to use actually available on the data platform?** If the data were not available, all correction plans would be empty talk.

Therefore, I conducted an item-by-item verification of the selected data platform, Dune Analytics, confirming:

- 10 protocol event types (Supply, Borrow, Repay, LiquidationCall, etc.) all have corresponding decoded tables on Dune;
- Key fields (onBehalfOf, repayer, etc.) are complete, supporting the revised multi-layer classification scheme;
- Historical LT/LTV parameter changes, collateral enable/disable status, EMode status, etc., are all trackable;
- HF and Debt need to be reconstructed from events, but all input data is available;
- Borrower economic intent is unobtainable off-chain information — this is a research boundary, not a data gap.

The verification confirmed: the revised research plan is feasible at the data level.

See: [Data Feasibility Paper1](../../04_阶段成果_Milestone_Deliverables/2026-08-11_构念效度审查与数据验证_Construct_Validity_Review_and_Data_Verification/2026-08-11_数据可行性验证_Paper1_Data_Feasibility)

---

## 5. Overall Summary of the Thought Process

Looking back at the entire process, my reasoning can be summarized as a clear logical chain:

```
Discussed blockchain payments with an industry contact
    ↓
Realized my understanding of protocols, data, and concept semantics was insufficient
    ↓
Decided to first clarify "what exactly am I studying" — built the Six-Layer Matrix framework
    ↓
Used the framework to audit Qualifying Report v1 — found 11 problems
    ↓
After corrections, asked "is the data I need actually usable?" — verified data feasibility
    ↓
Confirmed data is feasible and the research plan is executable — produced complete revision report
    ↓
Now continuing: verify terminology accuracy → verify whether protocol scope affects data requirements → search and read literature
```

In short: **semantic confusion revealed a knowledge gap → the knowledge gap motivated me to build a constraint framework → the framework helped me diagnose and fix problems → the corrected plan needed data feasibility verification → data verification confirmed the research is executable → now entering a phase of continued verification and literature supplementation.**

The essence of this process is: **first ensure that "what I am saying" is accurate, then ensure that "what I can do" is feasible, and only then continue advancing the research itself.**
