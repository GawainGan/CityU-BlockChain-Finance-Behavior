# Mazzocca, Acar, Uluagac, Montanari, Bellavista & Conti (2025) — A Survey on Decentralized Identifiers and Verifiable Credentials

## 基础信息

| 字段 | 内容 |
|------|------|
| **标题** | A Survey on Decentralized Identifiers and Verifiable Credentials |
| **作者** | Carlo Mazzocca, Abbas Acar, Selcuk Uluagac, Rebecca Montanari, Paolo Bellavista, Mauro Conti |
| **年份** | 2025 |
| **期刊** | IEEE Communications Surveys & Tutorials, Vol. 27(6), pp. 3641-3671 |
| **DOI** | 10.1109/COMST.2025.3543197 |
| **UTD 24?** | **否**（但 IEEE COMST 是通信和网络领域的顶级期刊，IF ≈ 35+） |
| **Tags** | `#mg` `#middle-ground` |
| **作者背景** | 多所意大利和土耳其大学；注意 Conti 是安全领域的高引学者，Uluagac 是 FIU 的网络安全教授 |

## 研究问题
系统性地综述去中心化标识符（DID）和可验证凭证（VC）的**研究现状、技术标准和开放挑战**。

## 核心结构与发现
- **范围**：收集了 2016-2024 年间的 350+ 篇相关论文
- **结构**：按照 DID/VC 的技术栈自底向上组织：底层 DLT → DID 方法 → VC 格式 → 应用层协议
- **核心贡献**：
  1. **核心协议/标准列表**：W3C DID Core 1.0, W3C VC Data Model 1.1/2.0, DIDComm, DKMS, etc.
  2. **技术架构对比**：对比了主流的 DID 方法 (did:ethr, did:indy, did:key, did:web 等) 和 VC 格式 (JSON-LD, JWT-VC, SD-JWT 等)
  3. **安全与隐私分析**：系统性地分析了 DID/VC 中的身份绑定、撤销、女巫攻击等 10+ 种威胁
  4. **开放挑战**：互操作性、可扩展性、监管合规（GDPR）、用户采用

## 核心结论（与你的研究直接相关）

1. **选择性披露仍是开放挑战**：尽管 SD-JWT (Selective Disclosure JWT) 和 BBS+ 签名等方案已被提出，但生产级的跨域选择性披露方案仍然不足（第 V 节）
2. **SSI 在金融领域的部署极少**：虽然大量 SSI 在被提出，但在实际金融 KYC 场景中的部署仍然是"pilot stage"
3. **监管和技术不匹配**：GD PR 的"数据最小化"原则、FATF 的"旅行规则"（Trav el Rule, 即要求 VASP 在进行数字资产转移时共享发送方和接收方的身份信息）与区块链的透明性、不可篡改性之前存在根本张力

## "Two-Question" 评估

| 问题 | 评价 |
|------|------|
| 问题是否**有趣/重要**？ | ✅ **是**。作为 2025 年的最新综述，它是进入 DID/SSI 领域最好的起点 |
| 方法是否**令人信服**？ | ✅ 方法学严谨、覆盖范围广。唯一的局限是技术发展太快——可能文中的一些"未来挑战"现在已经有人在攻破了 |

## 关键引用
- "Despite significant progress, various open issues still require further investigation" (p.3655)
- "Interoperability between different DID methods remains a challenge for cross-platform adoption" (p.3660)
- "The integration of selective disclosure [SD-JWT, BBS+] with ZKP holds promise but remains largely experimental" (p.3663)

## 对你研究的启发 / 探索建议

### 直接使用
1. **作为"中间地带"的理论基础**：Mazzocca 的综述确认了——SSI 和选择性披露在**金融场景中的大规模部署是开放挑战**。这为你的研究提供了**理论 gap** 的直接证据
2. **建立技术基础**：文章第 IV 节比较了不同的 VC 格式——你可以据此了解**选择性披露（SD-JWT vs BBS+ vs ZKP-based）**的技术差别，这直接支撑你"中间地带"的技术设计

### 理论填充
1. **隐私与监管的"不可调和的矛盾"**：文章指出 GDPR 的"right to erasure"与区块链的"immutable ledger"之间的冲突（p.3665）——你的"中间地带"本质上是对这一矛盾的回应
2. **技术采用的社会层**：文章提到"用户采用"是挑战——你可以进一步从 IS 视角提出"为什么即使技术就绪，银行仍然不用 SSI？"

### 可进一步探索的方向
1. **ZKP + Selective Disclosure 在 DeFi 中的应用**：在 KYC/AML 场景实现"匿名证明 + 风险可控"
2. **跨链身份管理**：你的 D_port（CVD）本质上是一个跨链身份跟踪问题

## 参考文献

```bibtex
@article{Mazzocca2025_DID_VC_Survey,
  title={A Survey on Decentralized Identifiers and Verifiable Credentials},
  volume={27},
  ISSN={2373-745X},
  DOI={10.1109/COMST.2025.3543197},
  number={6},
  journal={IEEE Communications Surveys & Tutorials},
  publisher={IEEE},
  author={Mazzocca, Carlo and Acar, Abbas and Uluagac, Selcuk and Montanari, Rebecca and Bellavista, Paolo and Conti, Mauro},
  year={2025},
  pages={3641-3671}
}
```
