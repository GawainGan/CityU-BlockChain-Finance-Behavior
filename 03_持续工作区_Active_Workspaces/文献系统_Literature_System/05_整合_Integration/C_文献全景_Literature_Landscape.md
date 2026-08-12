# 综合文献景观图

## 三条线的文献演化

此文档追踪三条线的文献从"已知"到"已搜索"的演化。每条线维护一个 4x4 网格：已知量（k） vs 已知未知（U-k） vs 未知已知（knowable） vs 未知未知（truly unknown）。

## 中间地带 (MG) 文献景观

### 2026-07-10 更新：深层分析已完成

经过对 MG 线的缺口验证搜索，我们现在对"缺失"有了更深刻的理解：

- **有密码学**：BBS+ 签名、BLS-MT-ZKP、SD-JWT、ISO/IEC 18013-5 mdoc——所有都确认已存在
- **没有经济学模型**：在信息经济学传统（Verrecchia 2001、Dye 2001）中，没有发现将"选择性披露"作为多维属性选择问题进行建模的论文
- **为什么会这样**：见 `02_Middle-Ground/_analysis/G01_密码学实现vs经济学形式化_深层分析.md` 中对五个结构性错位的分析

### 文献库更新

| 文献 | 主题 | 状态 | 来自搜索 |
|------|------|------|---------|
| Schlatt et al. (2022) | Blockchain-based SSI for KYC | ✅ 已读取 — DSR 框架，密码学实现，非经济学建模 | bib_fetch: 10.1016/j.im.2021.103553 |
| Nokhbeh Zaeem et al. (2021) | SSI 需求对比（31 方案） | ✅ 已读取 — 功能性/非功能性需求，无经济分析 | bib_fetch: 10.1145/3486622.3493917 |
| Bećirović Ramić et al. (2024) | BLS-MT-ZKP 选择性披露 | ✅ 已收录 — 提供 Merkle+BLS+Bulletproofs | bib_fetch: 10.1109/access.2024.3518597 |
| Farina et al. (2024) | 证据选择实验（NBER WP） | ⬜ 已关注 — 最接近的经济学"触及"，但仍然缺乏密码学约束条件 | NBER WP 32975（尚未在 bib 中） |

## V4 DeFi-Behavior 文献景观

### 核心基准文献（来自 V4_1 探索 & 已映射的 17 篇）
- Qin et al. (2021) — DeFi 清算实证（基准基准）
- Perez et al. (2020) — 清算：刀刃上的 DeFi
- Bartoletti et al. (2020/2023) — DeFi 借贷池 SoK
- Arshadi & Kim (2025) — Prospect Theory × Blockchain
- Lyu (2026) — 以太坊上处置效应
- Gadzinski & Liuzzi (2025) — 清算用户 *增加了* 借贷行为

## V3-3 CVD-Credit 文献景观

### 核心锚定文献（来自 V3.1 的 27 篇高度相关）
- Chakravarty & D'Ambrosio (2006) — axiomatic 方法论
- Liu et al. (2014) — decay 函数
- Antonakakis et al. (2020) — TVP-VAR 方法
- 其他 24 篇来自 Phase C 检索

## 文献数量目标

| 线 | 当前 | 1 个月目标 | 3 个月目标 | 终稿目标 |
|----|------|-----------|-----------|---------|
| MG  | 2-3 篇 | 10 篇 | 25 篇 | 40+ 篇 |
| V4  | 17+ 篇 | 25 篇 | 40 篇 | 60+ 篇 |
| CVD | 27+ 篇 | 35 篇 | 50 篇 | 60+ 篇 |
| **合计** | **~47 篇** | **70+ 篇** | **115+ 篇** | **160+ 篇** |

> 注意：MG 线目前是从头开始建设，但 V4 和 CVD 已有大量文献基础（请确认是否准确反映当前情况）
