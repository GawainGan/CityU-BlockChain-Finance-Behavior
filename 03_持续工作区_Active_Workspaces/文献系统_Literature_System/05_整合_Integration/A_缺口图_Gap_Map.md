# 研究空白总图 (Gap Map)

## 概览

此文档记录三条研究线中已经被确认的**文献空白（gap）**，以及还有待确认的**待核实空白（potential gap）**。

---

## Line 1: Middle-Ground — 空白分析

### 🔍 2026-07-10 验证结果

**验证结论：选择性披露的*实现方案*很多，但正式*机制设计/经济学建模*是真实空白**

搜索发现：
- 存在大量 selective disclosure 的实现方案：BLS-MT-ZKP（Bećirović Ramić et al., 2024, *IEEE Access*）、Merkle Tree+ZKP eKYC 系统（Ahmed et al., 2025, *APCC*）、SD-JWT、BBS+签名、ISO/IEC 18013-5 mdoc 等
- Schlatt et al. (2022, *Information & Management*) 用 DSR 方法构建了 KYC+SSI 框架，提出设计原则
- Nokhbeh Zaeem et al. (2021, *IEEE/WIC WI-IAT*) 提供了 31 个 SSI 解决方案的需求对比
- **但所有这些都属于密码学/工程实现层面，缺少将 selective disclosure 作为"信息经济学机制"的正式形式化建模**

→ **Gap 状态更新**：从"待核实" → **部分填补**（有密码学方案，无经济学形式化模型）

> 📄 **深度分析文档**：详见 `02_Middle-Ground/_analysis/G01_密码学实现vs经济学形式化_深层分析.md`

### ✅ 已确认空白

| Gap | 证据 | 优先级 | 深层原因 |
|-----|------|--------|---------|
| Selective disclosure 的正式信息经济学/机制设计建模 | 现有文献集中在密码学实现（BBS+/ZKP/Merkle），没有 ISR/MS 等顶刊将 selective disclosure 作为"信息可见度"的经济学最优选择问题建模 | P0 | **五个结构性错位**：（1）激励方向反转——经典模型中发送者受益于披露好消息，选择性披露中持有者被迫披露最少属性；（2）组合选择爆炸——属性级选择从二元变为 2^N，经济学理论直到 2024 年（Farina et al. NBER WP）才开始触及证据选择问题；（3）隐私成本结构独特——不可分离、持有头寸成本、动态一致性问题，经典固定成本模型无法捕捉；（4）计算信任打破贝叶斯更新——ZKP 通过后无剩余不确定性，摧毁了经典"可信非披露"逻辑；（5）学科孤岛——密码学/会计/经济学/IS 四者互不引用 |
| KYC 在去中心化环境下的"简化版"（非"全做"）的机制设计 | Schlatt et al. (2022) 的 DSR 框架提出的是完整的 SSI-KYC 流程，但未讨论"什么条件下可以简化/跳过特定 KYC 属性"的设计原则 | P1 | 同上（3）和（5） |

### 🔬 深层分析摘要

为什么密码学实现存在但经济学形式化不存在？因为密码学回答的是"**如何**"（如何选择性地披露选中的属性子集），而经济学需要回答的是"**为什么是这些属性而不是那些**"、"**对谁**以什么**对价**披露"、"**动态上**今天的披露如何影响明天的隐私"。具体地：

| 密码学实现（BBS+、BLS-MT-ZKP 等） | 信息经济学未覆盖的部分 |
|-----------------------------------|---------------------|
| 回答：给定 S ⊆ {1,...,N}，如何只暴露 S 中的值、隐藏其余值、同时证明 S ⊆ 签名？ | 未回答：为什么选择 S 而不是 T？S 的隐私成本 c(S) 如何决定？ |
| 确保证明的零知识和不可链接性 | 未回答：验证者的策略 P 如何被持有者的多维选择行为影响？ |
| 确保原子一致性（属性属于凭证） | 未回答：当属性在统计上相关时，实时披露成本是多少？ |
| 提供常数大小的证明（与 N 无关） | 未回答：当跨会话链接信息时，长期均衡披露策略是怎样的？ |

**关键机制设计问题**：一个理性的持有者，面对一个要求某些属性子集的验证者，会选择披露哪一组属性？密码学原语（BBS+ 的不可链接性、BLS-MT-ZKP 的范围证明、SD-JWT 的可链接签名）的选择会改变这个经济问题的约束条件。经济模型需要将密码学基元视为**设计参数**，这些参数会改变激励相容的披露集集合——一个简单的静态"披露/不披露"决策所无法捕捉到的洞察。

### ❓ 待核实空白（需进一步验证）

| Gap 描述 | 验证状态 | 下一步 |
|----------|---------|--------|
| 隐私与合规之间的"最优权衡点"的形式化建模 | 未搜索到 ISR/MS 相关文章 | 需扩展搜索到 JPE/Econometrica 等信息经济学。注意：Farina et al. (2024, NBER WP) 已经进入"证据选择"实验空间，但仍是传统的二元/单证据范式 |
| ZKP/凭证在链上金融中做身份验证时，对"信任假设"的实证检验 | 未找到 | 需等 Khadka et al. (2026) 发表后再评估 |
| 有没有办法用量化方法，形式化地推导出"哪些 KYC 属性应该遵循无条件披露、哪些有条件地披露、哪些完全跳过"？ | 未找到 | 这是经常被问到的研究问题，也是全 View 模型潜在的因果回答——但需要预封闭形式和一些"真实世界可接受的"基准 |

### 🗺️ 这条线的定位验证（2026-07-10）

验证后，我已针对 MG 线是否是博士论文核心提出了一种具体的、可反驳的表述：

> **不，这条线本身不足以支撑博士论文的核心**，原因如下：
> 1. 没有工程问题——密码学已经解决了"如何"，经济学问题仍未解决，但只能产生一个**建模贡献**，在实证上无法检验，并且到达经济的路径也很模糊
> 2. 没有建立竞争的既定社区（学者们在信息经济学、安全或法律期刊上阅读、撰写和发表）
> 3. 法里纳等人的 NBER 工作论文已经进入"证据选择"的空间，降低了其独占性
> 
> **还是有很大的用处**：它作为一个**概念框架或理论透镜**，在其他两条线的交汇处很有价值——V4（行为）和 CVD（信用可见度公理化度量）都可以从这个形式化模型中受益（分别用于行为类型和"进一步假设"）。

> 关于 MG 线的含义及其后续方向的更深入探讨，见`G01_密码学实现vs经济学形式化_深层分析.md`。

---

## Line 2: V4 DeFi-Behavior — 空白分析

### 🔍 2026-07-10 验证结果

**验证结论：两个核心空白均已确认；PT×DeFi 有 SSRN 工作论文但非已发表研究**

搜索发现：
- **Prospect Theory × DeFi 清算是真实空白**：Xiong et al. (2005, *SSRN*) 延续 Kyle, Ou-Yang & Xiong 的传统——将前景理论引入最优清算决策——但这是关于做市商/传统资产清算的纯理论模型，不是 DeFi 清算。Gadzinski & Liuzzi (2025, *Economics Letters*) 提供了 DeFi 被清算后行为证据但非 PT 框架。**无已发表研究将 PT 参数（λ, α, β）操作化为 DeFi 清算行为假设**
- **OECD 2023 DeFi liquidation 报告** 和 Chiu (2026, *BoC Staff Paper*) 分析了清算的宏观影响，但均无行为偏差视角
- **Bank opacity 文献成熟**（Morgan 2002, *AER*; Flannery et al. 2004, *JFE*; Bruno et al. 2023, *JFI*）但聚焦 TradFi 银行，未扩展到链上信用可见度

### ✅ 已确认空白

| Gap | 来源 | 验证状态 | 引文证据 |
|-----|------|---------|---------|
| Prospect Theory × DeFi Lending | V4_1 文献表 | **✅ 已确认空白**（无已发表研究跨接） | Kahneman & Tversky (1979); Xiong et al. (2005) 仅为 tradiitonal 清算无 DeFi; Gadzinski & Liuzzi (2025) 有行为证据无 PT 框架; Cornelli et al. (2025) 有 Aave 行为无 PT 假设 |
| Behavior Deviation → Credit Prediction | V4_1 文献表 | **✅ 已确认空白** | Ghosh et al. (2024) 链上信用评分无 BDM; Spadea & Seneviratne (2026) 有行为特征非理论驱动; Gadzinski & Liuzzi (2025) 暗示未纳入预测模型 |
| Cross-Protocol Behavioral Consistency | V4_1 文献表 | 仅存在于 RQ3，已降级为 conditional | — |

### ❓ 待核实空白（需进一步验证）

| Gap 描述 | 如何验证 | 优先级 | 状态更新 |
|----------|----------|--------|---------|
| Prospect Theory 的损失厌恶参数在 DeFi 清算中的校准 | 确认仍无实地/实验校准研究 | ⭐⭐⭐⭐⭐ | **仍为空白** |
| Active vs Passive 区分的先验标准 | 清算前主动修复 vs 被动等待 | ⭐⭐⭐⭐⭐ | **仍为空白** |
| 清算的参照点效应（HF=1）的实证证据 | 研究 HF=1 附近行为 | ⭐⭐⭐⭐ | Cornelli et al. (2025) 部分覆盖借贷行为但未设计 PT 假设检验 |

---

## Line 3: V3-3 CVD-Credit — 空白分析

### 🔍 2026-07-10 验证结果

**验证结论：信用可见度的 axiomatic measure 是强空白；bank opacity 文献丰富但无 axiomatic 公理化度量**

搜索发现：
- **Bank opacity 文献** 很成熟：Morgan (2002, *AER*) 用 split ratings 度量银行不透明度；Flannery et al. (2004, *JFE*) 用市场微观结构；Bruno et al. (2023, *JFI*) 用 IRB 模型
- **但没有一个提出"信用可见度"（credit legibility/visibility）的公理化度量**
- Diamond (1984, *REStud*) 的委托监督理论认为银行相对于市场有信息优势——但这是关于"是否应该产生信息"，而不是"如何度量信息可见度"
- Aghion et al. 和 Morgan (2002) 的 split rating 方法是最接近的"可见度代理"，但它们是实证代理而非公理化构造

→ **Gap 确认**：Credit legibility 的 axiomatic measure 是真实空白。但 bank opacity 文献提供了可借鉴的实证传统

### ✅ 已确认空白

| Gap | 来源 | 验证状态 | 引文证据 |
|-----|------|---------|---------|
| 链上信用可见度的 axiomatic measure | V3-3 设计（Chakravarty & D'Ambrosio 方法） | **✅ 确认空白** | Bank opacity 文献成熟（Morgan 2002; Flannery et al. 2004; Bruno et al. 2023）但均为实证代理，无 axiomatic 构造 |
| 专有数据"自我引用"问题 | V3-3 已修复 | 未找到类似修复方案的已发表文献 | — |

### ❓ 待核实空白

| Gap 描述 | 验证状态 | 优先级 | 下一步 |
|----------|---------|--------|--------|
| 信用可见度（Credit Legibility）作为独立构念 | **未找到**，但 bank opacity 文献提供了足够的理论基础（Morgan 的 split rating = 可见度代理的实质） | ⭐⭐⭐⭐⭐ | 可直接引用 Morgan (2002) 的 split rating 传统作为"可见度"的理论前身，然后提出 axiomatic 推广 |
| 专有数据 + 商户标签的"信用真空度"预测能力 | 需要商业数据 | ⭐⭐⭐⭐ | — |

---

## 优先级排序（综合三线）— 2026-07-10 更新

| 优先级 | 待办项 | 涉及线 | 原因 | 状态 |
|--------|--------|--------|------|------|
| P0 | 阅读 Schlatt et al. (2022) 并评估 | MG | 导师直接建议 | ✅ 已读取（DSR 框架，密码学实现，非经济学建模） |
| P0 | 搜索 UTD 24 中关于 selective disclosure | MG | 确定 gap 是否存在 | ✅ **Gap 确认**：有密码学方案，无经济学形式化模型 |
| P0 | 搜索 Prospect Theory 在金融市场中应用于清算的实证 | V4 | V4_1 已列出确认空白待实证 | ✅ **Gap 确认**：无 PT×DeFi 已发表研究 |
| P1 | 读取入门的 SSI/DID 综述（Mazzocca et al. & Nokhbeh Zaeem et al.） | MG | 建立领域基础 | ✅ 已通过 Nokhbeh Zaeem et al. (2021) 覆盖 31 个方案 |
| P1 | 读取 Qin et al. (2021) DeFi 清算实证 | V4 | DeFi 基准文献 | ✅ 已回溯（BibTeX 已 registry 验证） |
| P1 | 验证 CVD 的 axiomatic 基础是否有前人 | CVD | V3-3 理论核心 | ✅ **Gap 确认**：Morgan (2002) split rating 是最近代理，但无 axiomatic 构造 |
| P2 | 扩展阅读到 ZKP/Anonymous Credentials | MG | 技术基础 | ⏳ 部分完成（BLS-MT-ZKP 等方案已收集） |
| P2 | 提供 Active/Passive 区分的算法基准 | V4 | V4_1 的核心方法论 | ⏳ 待搜索 |

---

## 参考文献

```bibtex
@article{Kahneman1979_ProspectTheory,
  title = {Prospect Theory: An Analysis of Decision under Risk},
  volume = {47},
  ISSN = {0012-9682},
  DOI = {10.2307/1914185},
  number = {2},
  journal = {Econometrica},
  publisher = {JSTOR},
  author = {Kahneman, Daniel and Tversky, Amos},
  year = {1979},
  month = mar,
  pages = {263}
}

@article{Cornelli2025_Why_DeFi_Lending,
  title = {Why DeFi Lending? Evidence from Aave V2},
  author = {Cornelli, Giulio and Gambacorta, Leonardo and Garratt, Rodney and Reghezza, Alessio},
  journal = {Journal of Financial Intermediation},
  volume = {63},
  year = {2025}
}

@article{Gadzinski2025_Liquidations_Lending,
  title = {Do Liquidations Discourage Lending in DeFi?},
  author = {Gadzinski, Adam and Liuzzi, Danilo},
  journal = {Economics Letters},
  volume = {155},
  year = {2025}
}

@misc{ghosh2024onchaincreditriskscore,
  title = {On-Chain Credit Risk Score in Decentralized Finance},
  author = {Ghosh, Rik and Datta, Arka and Aggarwal, Vidhi and Sinha, Rohit and Sengupta, Soham},
  publisher = {arXiv},
  year = {2024},
  doi = {10.48550/arXiv.2412.00710}
}

@inproceedings{Spadea2026_Survival_Liquidation,
  title = {From Risk to Rescue: An Agentic Survival Analysis Framework for Liquidation Prevention},
  DOI = {10.1109/icbc67748.2026.11575462},
  booktitle = {2026 IEEE International Conference on Blockchain and Cryptocurrency (ICBC)},
  publisher = {IEEE},
  author = {Spadea, Fernando and Seneviratne, Oshani},
  year = {2026},
  month = jun,
  pages = {1--9}
}

@article{Morgan2002_RatingBanks,
  title = {Rating Banks: Risk and Uncertainty in an Opaque Industry},
  volume = {92},
  DOI = {10.1257/00028280260344506},
  number = {4},
  journal = {American Economic Review},
  author = {Morgan, Donald P.},
  year = {2002},
  pages = {874--888}
}

@article{Flannery2004_BankOpacity,
  title = {Market Evidence on the Opaqueness of Banking Firms' Assets},
  volume = {71},
  DOI = {10.1016/S0304-405X(03)00185-5},
  number = {3},
  journal = {Journal of Financial Economics},
  author = {Flannery, Mark J. and Kwan, Simon H. and Nimalendran, M.},
  year = {2004},
  pages = {419--460}
}

@article{Diamond1984_DelegatedMonitoring,
  title = {Financial Intermediation and Delegated Monitoring},
  volume = {51},
  DOI = {10.2307/2297430},
  number = {3},
  journal = {The Review of Economic Studies},
  author = {Diamond, Douglas W.},
  year = {1984},
  pages = {393}
}
```
