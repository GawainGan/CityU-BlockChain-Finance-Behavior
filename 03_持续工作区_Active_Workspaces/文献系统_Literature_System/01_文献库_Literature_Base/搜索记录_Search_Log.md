# 检索日志

## 初始检索 (2026-07-10)

| # | 日期 | 数据库 | 关键词 | 结果数 | 笔记线 | 备注 |
|---|------|--------|--------|--------|--------|------|
| S1 | 07-10 | Semantic Scholar | blockchain KYC privacy selective disclosure | ~200 | MG | 泛搜 |
| S2 | 07-10 | Semantic Scholar | DeFi liquidation borrower behavior | ~180 | V4 | 泛搜 |
| S3 | 07-10 | Semantic Scholar | on-chain credit scoring DeFi | ~150 | CVD | 泛搜 |

## 批次 2：定向搜索 (第一轮)

| # | 日期 | 定向来源 | 关键词 | 结果数 | 线 | 优质结果 |
|---|---------|---------|--------|--------|-----|---------|
| S4 | 07-10 | IEEE S&P + CCS + Usenix | KYC blockchain SSI | ~50 | MG | 部分 |
| S5 | 07-10 | ACM Computing Surveys | SSI DID verifiable credential | ~20 | MG | 多篇综述 |
| S6 | 07-10 | UTD 24 Journals | DeFi liquidation empirical | ~30 | V4 | 较少 |
| S7 | 07-10 | ISR + MISQ | blockchain KYC privacy | ~15 | MG | 极少 |
| S8 | 07-10 | Management Science + JFE | prospect theory liquidation | ~25 | V4 | 极少 |

## 批次 3：定向论文查找 (2026-07-10，下午)

| # | 日期 | 搜索引擎 | 搜索词 | 结果数 | 线 | 关键论文与发现 |
|---|------|---------|--------|--------|-----|---------------|
| S9 | 07-10 | paper_search | DeFi liquidation Aave Compound prospect theory lending behavior | 10 | V4 | Iftikhar et al. (2025), Qu et al. (2025), Chitra (2025) |
| S10 | 07-10 | paper_search | empirical study DeFi liquidations incentives risks | 10 | V4 | **Qin et al. (2021) @ ACM IMC** — 确认 DOI: 10.1145/3487552.3487811 |
| S11 | 07-10 | paper_search | behavioral finance cryptocurrency prospect theory empirical on-chain | 10 | V4 | 无高相关 |
| S12 | 07-10 | paper_search | on-chain credit scoring DeFi risk assessment blockchain | 10 | CVD | **Ghosh et al. (2024)** — arXiv:2412.00710 |
| S13 | 07-10 | paper_search | Do liquidations discourage lending DeFi economics letters | 10 | V4 | 未直接返回（标题匹配问题） |
| S14 | 07-10 | paper_search | Why DeFi lending Aave V2 Journal Financial Intermediation | 10 | V4/CVD | **Cornelli et al. (2025)** — BIS 工作论文 (#1183) |
| S15 | 07-10 | paper_search | Mu Tovanich Prat Do You Care About Your Positions Aave | 10 | V4 | 未直接匹配 |
| S16 | 07-10 | paper_search | Khadka privacy preserving KYC blockchain ZKP compliance | 10 | MG | **Khadka & Das (2026)** — 密码学顶级机构 KU Leuven |
| S17 | 07-10 | paper_search | Panait blockchain identity management KYC | 10 | MG | **Panait et al. (2020)** — arXiv:2004.13107 |
| S18 | 07-10 | paper_search | DeFi liquidation Aave post-liquidation borrower behavior | 10 | V4 | 结果有限 |
| S19 | 07-10 | paper_search | Bank of Canada DeFi lending returns leverage liquidation | 10 | V4/CVD | 未直接返回 |
| S20 | 07-10 | paper_search | credit legibility credit vacuum blockchain information asymmetry | 10 | CVD | 2145 条返回，需进一步筛选 |

## BibTeX 获取记录

| 论文 | 来源 | 结果 | 说明 |
|------|------|------|------|
| Qin et al. (2021) | DOI: 10.1145/3487552.3487811 | ✅ 成功 | ACM IMC 会议论文 |
| Schlatt et al. (2021) | DOI 匹配 | ✅ 成功 | Information & Management |
| Mazzocca et al. (2025) | DOI 匹配 | ✅ 成功 | IEEE COMST |
| Khadka & Das (2026) | DOI: 10.48550/arXiv.2606.20760 | ✅ 成功 | arXiv |
| Spadea & Seneviratne (2026) | DOI: 10.1109/ICBC67748.2026.11575462 | ✅ 成功 | IEEE ICBC |
| Ghosh et al. (2024) | DOI: 10.48550/arXiv.2412.00710 | ❌ 未找到 | arXiv 未注册 DOI |
| Panait et al. (2020) | arXiv export | ✅ 成功 | 直接通过 arXiv BibTeX 导出 |
| Gadzinski & Liuzzi (2025) | 经济学快报 | ❌ 未找到 | 需手动输入 |

## 关键 BibTeX 验证发现

- **Qin et al. (2021)**：通过 DOI (`10.1145/3487552.3487811`) 成功获取，`@inproceedings{...}` ACM IMC
- **Schlatt et al. (2021)**：通过 DOI 匹配自动获取
- **Mazzocca et al. (2025)**：通过 DOI 匹配自动获取  
- **Khadka & Das (2026)**：通过 arXiv DOI 获取
- **Panait et al. (2020)**：arXiv 直接导出 BibTeX（因未在 bib_fetch 注册而被拒，但实际 arXiv 提供 BibTeX 功能）
- **Spadea & Seneviratne (2026)**：通过 DOI 匹配获取

## 批次 4：第二轮广搜 (2026-07-10) — 20 次 paper_search + 15 次 bib_fetch

| # | 日期 | 来源 | 关键词 | 返回数 | 线 | 关键产出 |
|---|------|------|--------|--------|-----|---------|
| S21 | 07-10 | paper_search(econ) | blockchain KYC SSI selective disclosure design science | 10 | MG | 新 SSI 生态 (Laatikainen 2021) |
| S22 | 07-10 | paper_search(CS) | blockchain identity ZKP compliance GDPR | 10 | MG | GDPR 综述 (Belen-Saglam 2022) |
| S23 | 07-10 | paper_search(CS) | DeFi liquidation borrower prospect theory empirical | 10 | V4 | Cao & Šiška (2024) 最优清算模型 |
| S24 | 07-10 | paper_search(econ) | DeFi lending behavioral finance disposition effect on-chain | 10 | V4 | Schatzmann & Haslhofer (2020) BTC 处置效应 |
| S25 | 07-10 | paper_search(CS) | on-chain credit scoring decentralized lending information asymmetry | 10 | CVD | Ghosh 再次出现；Kandaswamy (2025) zScore |
| S26 | 07-10 | paper_search(econ) | credit legibility credit vacuum information economics blockchain | 10 | CVD | 低相关（信用评分 ML 为主） |
| S27 | 07-10 | paper_search(econ) | systemic risk DeFi contagion empirical | 10 | 跨线 | Aufiero (2025) TradFi/DeFi 综述 |
| S28 | 07-10 | paper_search(social) | blockchain identity credit risk IS design science | 10 | 跨线 | — |
| S29 | 07-10 | paper_search(CS) | "KYC" "blockchain" "self-sovereign" identity design framework | 10 | MG | 已读了；Liu (2020) SSI 设计模式 |
| S30 | 07-10 | paper_search(econ) | "DeFi" liquidation empirical study margin call behavioral | 10 | V4 | Iftikhar (2025), Belenko (2025) GBM |
| S31 | 07-10 | paper_search(CS) | verifiable credential selective disclosure DID survey | 10 | MG | COD-ssi (Onofri 2026); Buldini (2025) |
| S32 | 07-10 | paper_search(econ) | prospect theory financial markets blockchain trading behavior | 10 | V4 | — |
| S33 | 07-10 | paper_search(econ) | signaling screening decentralized finance credit reputation | 10 | CVD | — |
| S34 | 07-10 | paper_search(econ) | "DeFi" "information asymmetry" empirical lending "Aave" "Compound" | 10 | V4 | Bastankhah (2024) AgileRate; Darlin (2022) |
| S35 | 07-10 | paper_search(econ) | Kahneman Tversky prospect theory 1979 | 10 | V4 | —（经典太老，arXiv 无索引） |
| S36 | 07-10 | paper_search(econ) | Odean Barber disposition effect trading | 10 | V4 | — |
| S38 | 07-10 | paper_search(econ) | Stiglitz Weiss 1981 credit rationing | 10 | CVD | — |
| S39 | 07-10 | paper_search(econ) | Shefrin Statman disposition effect 1985 | 10 | V4 | — |
| S40 | 07-10 | paper_search(econ) | Akerlof 1970 market for lemons | 10 | econ | — |

## BibTeX 获取记录 (第二批)

| 论文 | arXiv ID / DOI | 结果 | 说明 |
|------|----------------|------|------|
| Kahneman & Tversky (1979) | DOI: 10.2307/1914185 | ✅ | Econometrica |
| Shefrin & Statman (1985) | DOI 不清晰 | ❌ | 版面标题不匹配，持续 block 待处理 |
| Akerlof (1970) | DOI 待定 | ❌ | 经典过老，需另获取 |
| Odean (1998) | DOI 未注册 | ❌ | 同上 |
| Stiglitz & Weiss (1981) | DOI 未注册 | ❌ | 同上 |
| Buldini et al. (2025) | arXiv: 2506.00262 | ✅ | 选择性披露 |
| Onofri et al. (2026) | arXiv: 2604.10685 | ✅ | COD-ssi 隐私披露 |
| Sonnino et al. (2018) | arXiv: 1802.07344 | ✅ | Coconut 选择性凭证 |
| Sun et al. (2022) | arXiv: 2206.11973 | ✅ | Aave 流动性风险 |
| Schatzmann & Haslhofer (2020) | arXiv: 2010.12415 | ✅ | BTC 处置效应 |
| Kandaswamy et al. (2025) | arXiv: 2507.20494 | ✅ | zScore 钱包评分 |
| Oberholzer & Zamaraiev (2026) | arXiv: 2605.05145 | ✅ | 9 维 DeFi 风控 |
| Aufiero et al. (2025) | arXiv: 2508.12007 | ✅ | TradFi/DeFi 文献综述 |
| Cao & Šiška (2024) | arXiv: 2411.19637 | ✅ | 遍历最优清算 |
| Darlin et al. (2022) | arXiv: 2204.11107 | ✅ | 债主杠杆稳定性 |
| Iftikhar et al. (2025) | arXiv: 2506.12855 | ✅ | Aave vs Compound 风控 |
| Chitra (2025) | arXiv: 2503.18237 | ✅ | 对数遗憾定价 |
| Laatikainen et al. (2021) | arXiv: 2105.15131 | ✅ | SSI 生态系统 |
| Liu et al. (2020) | arXiv: 2005.12112 | ✅ | SSI 设计模式 |
| Belen-Saglam et al. (2022) | arXiv: 2210.04541 | ✅ | GDPR + 区块链综述 |
| Dunphy & Petitcolas (2018) | arXiv: 1801.03294 | ✅ | 区块链身份管理初探 |
| Bastankhah et al. (2024) | arXiv: 2410.13105 | ✅ | AgileRate 自适应利率 |
| Xu & Vadgama (2021) | arXiv: 2104.00970 | ✅ | DeFi 借货演进综述 |
| Qu et al. (2025) | arXiv: 2506.00505 | ✅ | 强化学习利率调整 |
| Ao et al. (2022) | arXiv: 2206.08401 | ✅ | Aave 社交网络分析去中心化 |

## 已确定但未获 BibTeX 的论文

以下论文在 V4_1 交付物中被引用，但在本轮 bib_fetch 中未匹配：
- Gadzinski & Liuzzi (2025) — Economics Letters — 期刊本身未在 bib_fetch 系统中
- Bartoletti & Lipparini (2025) — arXiv:2506.15295 — 新预印本，尚未被 bib_fetch 索引
- Cornelli et al. (2025) — J. Financial Intermediation — 需要最终出版版本的准确 DOI

## 下一步搜索策略

1. 对 CVD 线，需要查找 `credit legibility` / `credit vacuum` 核心理论文献（信息经济学传统）
2. 主题相关：Chakravarty & D'Ambrosio (2006) 「社会排斥度的公理化」是 CVD 核心理论来源但难以检索
3. 通过引用网络找到 Schlatt (2021) 和 Qin (2021) 的被引论文
4. 在 UTD 24 期刊中直接搜索 "blockchain" + "lending" + "behavior"

## 批次 5：待核实空白专项搜索 (2026-07-10)

| # | 日期 | 来源 | 关键词 | 结果数 | 线 | 关键产出 |
|---|------|------|--------|--------|-----|---------|
| S41 | 07-10 | paper_search(econ) | credit legibility OR credit vacuum OR information opacity banking | 10 | CVD G01 | 无直接相关 |
| S42 | 07-10 | paper_search(econ) | prospect theory loss aversion parameter calibration DeFi | 5 | V4 G02 | 无直接相关 |
| S43 | 07-10 | paper_search(CS) | DeFi liquidation behavioral borrower active remediation | 10 | V4 G03 | Iftikhar (2025) 风控对比 |
| S44 | 07-10 | paper_search(econ) | Aave Compound "prospect theory" behavioral lending | 10 | V4 | 仅 Cornelli 等 (2025) 直接涉及 |
| S45 | 07-10 | paper_search(CS) | "selective disclosure" blockchain "design science" KYC | 10 | MG | 仅 Schlatt (2021) 直接相关 |
| S46 | 07-10 | paper_search(econ) | "credit visibility" financial intermediation | 10 | CVD | 无直接相关 |
| S47 | 07-10 | paper_search(econ) | behavior bias credit default prediction machine learning | 10 | V4 | 传统金融有大量行为偏差文献，但无 DeFi 特指 |
| S48 | 07-10 | paper_search(CS) | DeFi liquidation "behavioral finance" | 10 | V4 | 跨学科搜索，结果有限 |

## 批次 6：UTD 24 / 顶会定向搜索 (2026-07-10)

| # | 日期 | 来源 | 关键词 | 结果数 | 线 | 关键产出 |
|---|------|------|--------|--------|-----|---------|
| S49 | 07-10 | paper_search(econ) | "Management Science" DeFi lending liquidation | 10 | V4 | 顶会结果有限 |
| S50 | 07-10 | paper_search(CS) | "Information Systems Research" blockchain KYC identity | 10 | MG | 无直接相关 |
| S51 | 07-10 | paper_search(econ) | "Journal of Political Economy" credit markets asymmetric information | 10 | CVD | 经典结果 |
| S52 | 07-10 | paper_search(econ) | Akerlof 1970 "market for lemons" quality uncertainty | 5 | 通用 | 确认经典 BibTeX |
| S53 | 07-10 | paper_search(econ) | Kahneman Tversky 1979 prospect theory econometrica | 5 | 通用 | 确认经典 BibTeX |
| S54 | 07-10 | paper_search(econ) | Stiglitz Weiss 1981 credit rationing AER | 5 | 通用 | 确认经典 BibTeX |

## 重要经典文献获取状态

以下经典理论的原始 BibTeX 经过多轮尝试仍未完美获取（bib_fetch 返回了错误匹配），需要手动补充：

| 文献 | 正确 DOI | 状态 |
|------|---------|------|
| Akerlof (1970) "The Market for Lemons" | 10.1016/B978-0-12-214850-7.50005-8（章节版）或未知 QJE DOI | ⚠️ bib_fetch 返回书章版而非 QJE |
| Stiglitz & Weiss (1981) "Credit Rationing" | 10.1257/aer.71.3.393 | ⚠️ bib_fetch 返回错误匹配（Berardi 2007） |
| Kahneman & Tversky (1979) "Prospect Theory" | 10.2307/1914185 | ✅ bib_fetch 成功 |
| Shefrin & Statman (1985) "Disposition Effect" | 未知 | ❌ 未获取 |

这些经典需要手动验证正确的 DOI 后重新 bib_fetch，或直接手动写入 refs.bib。
