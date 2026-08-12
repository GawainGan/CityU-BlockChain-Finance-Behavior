# 01. Collateral / 抵押

**六层矩阵详细文件**  
**相关技术文档**：`03_技术文档/01_Aave_V3.md`  
**相关文献**：`04_文献/02_Collateral_Credit/`

---

## Layer 1 — Definition

> **在无需许可的 DeFi 借贷中，抵押品首先提供一种可由协议强制执行的损失吸收和激励机制，使借贷能够在缺乏传统身份式信用审核的条件下发生。抵押本身不等于借款人的信用能力，但抵押选择、抵押比例和抵押行为仍可能包含有关借款人类型与风险的信息。**

传统 collateral literature 同时讨论以下作用：

- **Loss mitigation**：违约时的损失吸收
- **Borrower incentive**：激励借款人维持仓位
- **Moral hazard control**：限制道德风险
- **Screening**：借款人自我选择信号
- **Signaling**：向贷方传递借款人质量信息
- **Asymmetric information**：缓解信息不对称
- **Borrower–lender relationship**：关系型借贷
- **Credit allocation**：影响信贷资源配置

因此：

```text
Collateral ≠ Credit Score        （成立）
Collateral contains no credit information   （不成立）
```

### 与 Staking 的区分

```text
Staking（共识层质押，如 ETH validator 32 ETH）
≠
Collateralization（金融抵押，如 Aave 中存入 ETH 借 USDC）
```

---

## Layer 2 — Construct

我们要测量的构念是 **collateralization state**——协议中一个仓位当前的抵押状态。

它包含：
- 抵押资产的种类与数量
- 抵押资产是否被启用为 collateral（Aave 中是独立状态）
- 抵押资产相对于债务的充足程度
- 抵押资产的波动性特征

它**不包含**：
- 借款人的整体资产负债表
- 借款人的传统信用评分
- 借款人的未来偿付意愿

### 理论定位

Collateral 在传统金融理论中具有多重功能。在 DeFi 语境下：

```text
Overcollateralization = trust-substitution mechanism
```

它不是因为"照搬传统金融"才出现，而是因为 permissionless blockchain 具有 pseudonymous user + no legal identity + no credit bureau + no court-based enforcement 的约束，因此最简单且可编程的方法就是要求预先提供资产。

但它在金融功能层面可能**没有完成真正的信用中介**，因为它绕过了对借款人信用能力的识别。

---

## Layer 3 — Measurement

### Aave V3

- **事件**：`Supply` / `Withdraw` 事件记录资产存入与提取
- **状态**：`getUserReserveData()` 获取用户在每个 reserve 中的 aToken 余额
- **Collateral-enabled 状态**：`UserReserveData.usageAsCollateralEnabled` 标识该资产是否被启用为抵押
- **关键区分**：Supply ≠ Collateral-enabled Supply。只有在 `usageAsCollateralEnabled == true` 时，该资产才计入 Health Factor 计算

### Compound III

- **事件**：`Supply` / `Withdraw` 事件
- **状态**：账户的 collateral balances 直接存储在 Comet 合约中
- **区别**：Compound III 中所有 supplied asset 自动作为 collateral，无需单独 enable

### MakerDAO / Sky

- **事件**：Vault 的 `lock` / `free` 操作
- **状态**：Vault 的 collateral amount 和 debt amount
- **区别**：Maker 使用 Vault 结构，collateral 和 debt 在同一 vault 中管理

### 跨协议

- 不同协议的 collateral 机制不同，不能简单统一
- 跨协议比较应使用 protocol-native 指标，然后标准化

---

## Layer 4 — Observable

| 信息 | 可观测性 | 来源 |
|------|---------|------|
| 抵押资产种类与数量 | ✅ 高 | 合约状态 + 事件日志 |
| 抵押资产是否被启用为 collateral | ✅ 高 | Aave `UserReserveData` |
| 抵押资产的预言机价格 | ✅ 高 | Chainlink price feed 合约 |
| 抵押资产的历史参数变化（LT 等） | ✅ 高 | 历史合约参数 + governance 事件 |
| 抵押资产在协议中的总供给量 | ✅ 高 | 协议状态合约 |
| 借款人为什么选择这个资产作为抵押 | ❌ 不可观测 | 需要链下信息 |
| 借款人的整体资产组合 | ❌ 不可观测 | 可能跨协议、跨链、跨 CEX |

---

## Layer 5 — Identification

### 识别挑战

1. **Collateral choice 内生性**：借款人选择哪种资产作为抵押本身就是信号，可能与借款人类型相关（Jiménez et al. 2006; Berger et al. 2011）
2. **Collateral ratio 内生性**：抵押比例不是外生参数，而是借款人决策的结果
3. **Supply ≠ Collateral addition**：Aave 中 Supply 不一定等于风险减轻的追加抵押，因为资产可能未被启用为 collateral
4. **Collateral 的信息功能**：Collateral 不仅仅是 loss protection，它的选择和比例可能包含 screening / signaling 信息（Ioannidou et al. 2022）

### 混淆因素

- 借款人可能同时持有多个协议的仓位，链上只看到局部
- 借款人可能在 CEX 上有对冲仓位
- 借款人的 collateral 选择可能受 gas 成本、流动性、税收等多重因素影响

---

## Layer 6 — Allowed Claim

### 可以声称

- "Collateralization state"（仓位当前的抵押状态）
- "Collateral primarily provides an enforceable loss-absorption and incentive mechanism"（抵押主要提供可执行的损失吸收和激励机制）
- "Collateral choice and collateralization levels may contain information about borrower type and risk"（抵押选择和比例可能包含借款人类型信息）
- "Overcollateralization is a trust-substitution mechanism in permissionless DeFi"（超额抵押是信任替代机制）

### 不可以声称

- "Collateral contains no credit information"（抵押不包含任何信用信息）——这是不成立的
- "Collateral = creditworthiness"（抵押等于信用能力）
- "Collateral is not blockchain-native"（抵押不符合区块链原生逻辑）——恰好说反了
- "观察到 supply = 观察到追加抵押"（在 Aave 中不成立）
- "借款人的 collateral choice 反映了其完整风险偏好"（只能反映链上可见的部分）

---

## 相关文献

| 文献 | 标题 | 年份 | 链接 | 与本概念的关系 |
|------|------|------|------|---------------|
| Jiménez et al. | Determinants of Collateral | 2006 | https://www.sciencedirect.com/science/article/pii/S0304405X05002627 | Collateral 与 borrower risk 的内生关系 |
| Berger, Frame, Ioannidou | Tests of Ex Ante vs Ex Post Theories of Collateral | 2011 | https://www.sciencedirect.com/science/article/pii/S0304405X11000076 | 区分 screening/signaling 与 incentive/moral hazard |
| Ioannidou, Pavanini, Peng | Collateral and Asymmetric Information in Lending Markets | 2022 | https://www.sciencedirect.com/science/article/pii/S0304405X21005389 | Collateral 与 asymmetric information |
| Asriyan, Laeven, Martín | Collateral Booms and Information Depletion | 2021 | https://academic.oup.com/restud/article-pdf/89/2/517/42748132/rdab046.pdf | Collateral boom 导致信息生产减少 |
| Cong & He | Blockchain Disruption and Smart Contracts | 2019 | https://academic.oup.com/rfs/article/32/5/1754/5427778 | Blockchain 对 contracting / information / consensus 的经济意义 |
