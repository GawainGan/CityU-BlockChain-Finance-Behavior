# D03: ZKP Proof 在 DeFi 清算中的前端运行风险

## 基本信息

| 字段 | 内容 |
|------|------|
| **方向 ID** | D03 |
| **涉及线** | MG → V4 跨线 |
| **优先级** | ⭐⭐⭐⭐ |
| **来源论文** | Khadka & Das (2026, arXiv: 2606.20760) — SDAS |

## 设想描述

Khadka & Das (2026) 的 SDAS 方案中提出了一个有趣的旁白（Section 5.3）：ZKP proof 的前端运行风险。具体来说，当用户在 DeFi 场景提交 ZKP proof 进行合规验证时，验证者（validator/sequencer）可以在确认 proof 之前抢先交易（front-run）。

**设想**：在 DeFi 借贷的隐私保护 KYC 场景中，ZKP 选择性披露系统面临两类冲突：
1. **信息被看透**（类似传统 KYC 的中心化泄露风险）
2. **交互本身被操控**（验证者看到 proof 提交行为后抢跑）

这引出一个新的安全模型：SD 方案需要不仅保护"说出去的内容"，还要保护"提交行为本身"。

## 为什么目前无对应论文

在 S45 (selective disclosure design science) 和 S31 (verifiable credential survey) 搜索中，Buldini et al. (2025) 系统性比较了所有 SD 方案，但前端运行风险不在其评估维度中。Khadka & Das (2026) 仅将其作为 future work 提出，未展开。

## 相关线索

- SDAS (Khadka & Das 2026) — 首次在 SD 方案中提出前端运行
- Buldini et al. (2025, IEEE TIFS) — 最新 SD 方案基准，0 篇讨论前端运行
- MEV 文献 — 以太坊 MEV 已充分研究（Flash Boys 2.0），但未与 ZKP 的隐私保护交叉
- SSI 工业界趋势：Sovrin 2025 年关闭、EUDIW 2026 年底推出

## 潜在验证方法

1. 构建威胁模型：ZKP proof 提交流程中的 MEV 攻击面分析
2. 在以太坊测试网实现一个概念验证：对 SDAS 协议的交易排序攻击
3. 推导 SD 方案应满足的"排序安全"（order-fairness）条件

## 状态

- [x] 方向已识别
- [x] 有初步文献支撑
- [ ] 已找到对应论文
