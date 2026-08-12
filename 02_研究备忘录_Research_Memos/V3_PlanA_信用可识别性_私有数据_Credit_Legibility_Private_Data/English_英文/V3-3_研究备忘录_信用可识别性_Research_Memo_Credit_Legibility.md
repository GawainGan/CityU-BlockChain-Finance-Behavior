# Research Progress Memo · Plan A (V3-3)

**Title**: Plan A: Private-Data Study of the On-Chain Credit Legibility Gap  
**One-sentence positioning**: This project turns the question “can a system actually see and interpret a pseudonymous user?” into a computable, falsifiable measure that can be validated against external risk outcomes.

---

## 1. What I Have Done (Recent Progress)

The crypto ecosystem has reached a multi-trillion-dollar scale, but pseudonymous ledgers still record only “who transferred how much to whom.” They do not record what was purchased, who made the purchase, or why the transaction occurred. Most existing Web3 credit studies treat this as a missing-credit-history problem and respond by adding alternative data to build a score (Bazarbash, 2019; Ghosh et al., 2024; Kori & Gadagin, 2024).

I think this framing makes a category mistake. Before asking whether a user is creditworthy, there is a more basic and under-theorized object: whether a system can stably identify, interpret, and reuse a subject’s behavior across decentralized contexts. I call this object **credit legibility**, and I explicitly distinguish it from creditworthiness. A user can be highly creditworthy but almost illegible to a system, or highly legible but financially risky. Conflating these two notions is a recurrent trap in Web3 credit research: systems mistake “I cannot see the user clearly” for “the user is risky,” then add more proxy variables to a score without recognizing that the scoring object was never made legible in the first place.

The idea draws on the legibility tradition of Scott’s *Seeing Like a State* (1998) and Fourcade and Gordon’s *Learning Like a State* (2020). Their work explains how states and data infrastructures reshape social life into measurable forms, but legibility remains largely qualitative in that tradition: it is not decomposed, formalized, or validated through prediction. I have narrowed the project into an empirical-methodological paper on measurement and construct validity. The contribution is not to “found a new field,” but to make a pre-scoring object computable and externally testable.

Based on this judgment, I have done four things:

**(1) I proposed an observer-relative computable measure: CVD.** I formalize it as $\mathrm{CVD}_i(t\mid O,I)=f(D_{id},D_{sem},D_{port})\in[0,1]$, combining identity deficit, semantic deficit, and portability deficit under a multiplicative canonical form constrained by seven axioms. Two design choices are central. First, CVD explicitly includes the observer $O$ and infrastructure $I$, because legibility is a property of the subject-observer-infrastructure triad rather than an intrinsic attribute of the subject. The same user can be highly legible to UnusPay, invisible to a DeFi protocol, and only partially legible to a bank. Second, high CVD does not mean that the user is “bad”; it means the system cannot see the user clearly. This distinction runs through the entire project and implies that no service decision based on CVD should equate high CVD with high user risk.

**(2) I turned UnusPay’s data asset into an observable setting.** The empirical challenge is that, from a purely on-chain view, transfers between addresses are semantically opaque; we cannot directly observe changes in legibility. UnusPay, as a crypto payment gateway integrated into e-commerce platforms, has a deterministic TxHash-to-OrderID/SKU mapping and identity anchor signals such as hashed email, device fingerprint, and IP. Its value is not merely that it has data, but that it creates a natural setting in which legibility is locally repaired: an on-chain transfer that is otherwise uninterpretable gains commercial semantics and partial identity clues through the mapping layer. This lets me observe what changes when a transaction moves from illegible to partially legible. Chainalysis/Nansen-style on-chain analytics and merchant-side order analytics cannot observe this interface alone, because one sees addresses and the other sees orders; credit legibility is produced precisely in the mapping between them.

**(3) I hardened the single empirical core through several rounds of red-team review.** A measure that is only defined but not validated easily becomes a naming exercise. I therefore anchor the project on one falsifiable claim: after controlling for on-chain activity and pure SKU semantics, CVD should still add predictive power for risk outcomes external to UnusPay. This claim has to survive three attacks. The first is “is this just data coverage?” I answer it with an external-outcome ladder: internal outcomes, semi-external outcomes, and truly external hard outcomes, with the main criterion placed on tier-3 outcomes such as on-chain blacklists, DeFi liquidations, or external platform flags. The second is “does the denominator contain the numerator?” I answer it by redefining the denominator of $D_{sem}$ from “whether the transaction passed through UnusPay” to “whether the recipient is a merchant,” cutting the self-reference loop. The third is “is this just SKU-based credit prediction?” I answer it by adding an $M_{sku}$ baseline to the horse race, reproducing the upper bound of a Bazarbash-style SKU prediction model. The tightened criterion is that CVD must beat both the activity baseline and the pure-SKU baseline, showing that its non-semantic dimensions, $D_{id}$ and $D_{port}$, add information unavailable to existing approaches.

**(4) I designed a pilot de-risking checklist.** The empirical core still depends on several unknowns: whether merchant labels have sufficient coverage, whether same-person labels are obtainable, and whether external outcomes can be matched at a usable rate. Rather than spending months before discovering a blocking dependency, I designed a small-slice go/no-go pilot that can answer these questions at low cost. Each failed gate has a predefined downgrade path, which moves the main risk to the earliest and cheapest stage of the project.

## 2. Why This Is Worth Doing (Novelty and Literature Support)

**Measurement-level novelty**: Existing Web3 credit studies either build scores (Ghosh et al., 2024; Kori & Gadagin, 2024) or cluster wallets through entity-resolution heuristics (Chegenizadeh et al., 2025, for Cardano). They do not turn legibility itself into a computable, observer-relative, axiomatically grounded measure.

A criticism must be addressed directly. Since CVD is computed from UnusPay data, a natural objection is: “Are you measuring only what UnusPay happens to see, and why should that count as a general measure?” If this objection succeeds, CVD becomes merely an internal descriptive statistic for one company rather than an academic contribution. My response is to separate formula-level standardization from value-level conditionality. The functional form, the three dimensions, and the axioms are standardized across observers: any observer can use the same formula. The numerical value, however, is conditional on a given $(O,I)$, and I explicitly acknowledge that it changes when the observer changes. This is similar to apparent magnitude in astronomy: the formula is standardized, while the measured magnitude is observer-relative. Apparent magnitude is still a standard astronomical measure because the formula layer is comparable. CVD’s observer-relativity is more fundamental than ordinary data-dependence in measures such as the Gini coefficient, because different observers genuinely see different legibility states, but this does not prevent the formula layer from becoming a domain-standard measurement framework.

**Empirical novelty**: The four-way horse race includes an $M_{sku}$ baseline that reproduces the upper bound of Bazarbash-style “SKU predicts credit” information. The criterion that CVD must beat both $M_{act}$ and $M_{sku}$ directly tests whether the non-semantic components of CVD add information unavailable to previous work, rather than repackaging old variables under a new name. Liberti and Petersen’s (2019) work on hard and soft information provides a micro-foundation for the mechanism from legibility to information asymmetry and adverse selection.

---

## Appendix: Core Framework

![V3-3 research framework](figures/V3-3_framework.svg)

## Risks and Boundaries

The project has several identifiable risks: the availability of measurement inputs, especially merchant-label coverage; the match rate for outcomes external to UnusPay; and whether the incremental predictive value of CVD actually holds against both activity and pure-SKU baselines. Each risk has a corresponding downgrade path: switching to a comparison design that requires only on-chain transactions, retreating to semi-external outcomes with an explicit limitation, or returning to construct purification before resetting the empirical test. These risks should remain visible rather than hidden, because they define the honest boundary of the research design.

**Key References** (newest first)
- Chegenizadeh, Rafati Niya & Tessone (2025). Heuristic-Based Address Clustering in Cardano Blockchain. arXiv:2503.09327.
- Ghosh, Datta, Aggarwal, Sinha & Sengupta (2024). On-Chain Credit Risk Score in Decentralized Finance. arXiv:2412.00710.
- Kori & Gadagin (2024). Blockchain-Based AI Models for Credit Scoring and Risk Assessment. *International Journal of Research Publication and Reviews*, 5(11).
- Liberti & Petersen (2019). Information: Hard and Soft. *Annual Review of Economics*, 11.
- Fourcade & Gordon (2020). Learning Like a State. *Sociological Theory*, 38(4).
- Bazarbash (2019). Fintech in Financial Inclusion. *IMF Working Paper*.
- Scott (1998). *Seeing Like a State*. Yale University Press.
