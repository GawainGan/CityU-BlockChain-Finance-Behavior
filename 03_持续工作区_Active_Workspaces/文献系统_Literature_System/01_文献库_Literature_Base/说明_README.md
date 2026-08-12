# 01_Literature-Base — 文献总库

## 用途
所有三条研究线的文献去重后统一索引在此。每篇文献只在一条线下有完整笔记，其他线的"交叉引用"通过 tags 和 cross-ref 字段链接。

## 目录结构

```
01_Literature-Base/
├── README.md              ← 本文件
├── master_index.md        ← 所有文献的主索引（按作者+年份排序）
├── search_log.md          ← 检索日志：每次检索的关键词、数据库、结果数
├── _papers/               ← 文献笔记存放处（按 Author_Year_Key.md 命名）
│   ├── Schlatt_2021_BlockchainKYC.md
│   ├── Qin_2023_DefiLiquidations.md
│   └── ...
└── _templates/            ← 模板（hard link 到上级 _templates）
```

## 三线标签约定
- `#mg` = Middle-Ground
- `#df` = DeFi-Behavior
- `#cvd` = CVD-Credit
- 多标签表示跨线，如 `#mg #df` 表示同时涉及中间地带和 DeFi
