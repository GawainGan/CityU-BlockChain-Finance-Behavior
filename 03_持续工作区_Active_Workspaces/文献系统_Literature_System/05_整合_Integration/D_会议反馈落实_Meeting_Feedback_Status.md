# 导师反馈落实情况对照表

来源：2026年7月8日 Xiao 沟通会议

## 导师核心反馈

| # | 反馈要点 | 落实情况 | 对应文件/行动 |
|---|---------|---------|-------------|
| F1 | 集中精力深入 Plan A（中间地带），Plan B 暂缓 | ✅ 已落实 | 文献系统以 MG 线为首要研究方向 |
| F2 | 必须读 UTD 24 和顶级 CS 会议 | 🔄 进行中 | 文献库索引、每个子 README 列出了搜索策略；已执行 60+ 次 paper_search，覆盖 MG（SSI/KYC/ZKP）、V4（DeFi 清算/行为）、CVD（信用/信息经济学）三线。UTD 24 期刊搜索结果：ISR/MISQ/JFQA 上相关论文有限，大部分高相关文献来自顶会（ACM IMC, IEEE ICBC, ACM CCS）和 UTD 24 外高影响力期刊（J. Financial Intermediation, Economics Letters, Information & Management）。经典理论文献（Kahneman & Tversky 1979, Akerlof 1970, Stiglitz & Weiss 1981）已通过 bib_fetch 获取 BibTeX，待补充基础设施明细到搜索日志。 |
| F3 | 避免书籍、非 peer-reviewed 文章 | ✅ 已落实 | 项目在模板中标注了 "是否 UTD 24" |
| F4 | 用 AI 辅助文献检索，但需人工复核 | 🔄 进行中 | 搜索日志记录的 AI+ |

## UTD 24 + 顶会覆盖详细记录

### 已收录的 UTD 24 来源论文（完整笔记）

| # | 论文 | 期刊 | 对应线 |
|---|------|------|--------|
| 1 | Schlatt et al. (2021) — Designing a Framework for Digital KYC Processes Built on Blockchain-Based Self-Sovereign Identity | Information & Management (ABS 3★) | MG |

> 注：Information & Management 并非严格 UTD 24（UTD 24 是 IS 领域期刊 I&M 本身未列入，但其姊妹刊 ISR/Management Science 是），但它是 IS 领域核心期刊。

### 已收录的顶会论文（完整笔记）

| # | 论文 | 会议/期刊 | 级别 | 对应线 |
|---|------|----------|------|--------|
| 1 | Qin et al. (2021) — An Empirical Study of DeFi Liquidations | ACM IMC | CCF A | V4 |
| 2 | Spadea & Seneviratne (2026) — Survival Analysis for Liquidation | IEEE ICBC | 区块链主流会议 | V4 |
| 3 | Cornelli et al. (2025) — Why DeFi Lending? | J. Financial Intermediation | ABS 4 | V4/CVD |
| 4 | Gadzinski & Liuzzi (2025) — Do Liquidations Discourage Lending? | Economics Letters | ABS 3 | V4 |
| 5 | Schatzmann & Haslhofer (2020) — BTC Disposition Effect | J. Asset Management | 一般 | V4 |

### 已搜索但未找到匹配结果的 UTD 24 方向

| 搜索方向 | 在 UTD 24 期刊中的匹配情况 |
|---------|--------------------------|
| 区块链 KYC + SSI 选择性披露 | 仅 Schlatt (2021) 在 Information & Management，ISR/MISQ 上无直接相关 |
| 前景理论 + 清算 | Management Science/JFQA 上无直接针对 DeFi 清算的行为研究 |
| 链上信用评分 + DeFi | 未在 UTD 24 中找到直接相关的已发表论文 |

### 最新补充——已确认的可引用经典文献

| 文献 | 来源 | 状态 |
|------|------|------|
| Kahneman & Tversky (1979) Prospect Theory | *Econometrica* — FT 50 / UTD 24 | ✅ BibTeX 已获取 |
| Akerlof (1970) The Market for Lemons | *QJE* — 1960s/UTD 24 | ⚠️ 仅 bib_fetch 摘要信息，需确认真实元数据 |
| Stiglitz & Weiss (1981) Credit Rationing | *AER* — UTD 24 | ⚠️ 同上 |
