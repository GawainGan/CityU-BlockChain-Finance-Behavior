# Literature System — 文献知识库

## 结构总览

```
2026-07-10_Literature-System/
│
├── 01_Literature-Base/        ← 文献总库（三线通用，统一笔记模板）
├── 02_Middle-Ground/          ← 中间地带线（Blockchain KYC / Selective Disclosure）
├── 03_DeFi-Behavior/          ← V4 DeFi 行为金融线（Prospect Theory x Lending）
├── 04_CVD-Credit/             ← V3-3 信用真空度线（Credit Legibility / On-chain Credit）
└── 05_Integration/            ← 三线整合 / 交叉映射 / 研究 gap 总图
```

## 三条研究线的核心焦点

| 线 | 核心问题 | 核心构念 | 数据 |
|---|---|---|---|
| Middle-Ground | 链上行为如何实现适度可信的交易验证（不完全KYC，不完全匿名）？ | Selective Disclosure, ZKP, DID, Credential | 文献 + 推理 |
| DeFi-Behavior (V4) | 接近清算阈值的借款者行为是否偏离理性预期？行为偏差是否携带信用预测信息？ | Prospect Theory, BDM, Liquidation HF | Aave/Compound 公开数据 |
| CVD-Credit (V3-3) | 用户对系统而言有多 "不可见"？信用真空度如何预测外部风险？ | Credit Legibility, CVD, D_id/D_sem/D_port | UnusPay 专有数据 |

## 使用方式

### I. 录入新文献（所有线统一用相同格式）
每篇文献在各自线的 `_papers/` 子目录下创建 `Author_Year_Keyword.md`，模板见 `_templates/paper_note_template.md`。

### II. 文献总库（01_Literature-Base）
所有线的文献去重后，按照三线的交叉情况记录索引。如果一篇文章横跨多条线，在 tag 字段标记 `#middle-ground #defi-behavior` 等。

### III. 整合（05_Integration）
- `gap_map.md` — 三线的研究空白总图
- `cross_mapping.md` — 三线之间的构念关联/张力
- `literature_landscape.md` — 综合文献概览
