# Compound III 技术文档

**官方文档**：https://docs.compound.finance/  
**版本**：Compound III (Comet)  
**用途**：Paper 1 跨协议验证协议

---

## 1. 协议概述

Compound III 是一个 EVM 兼容协议，允许用户供应加密资产作为抵押品以借入 base asset。与 Compound V2 不同，Compound III 每个市场只有一个 base asset（如 USDC）。

### 关键特性

- **Single base asset**：每个市场只有一个可借资产（如 USDC）
- **Multi-collateral**：支持多种抵押资产
- **Auto-collateral**：所有 supplied asset 自动作为 collateral（无需单独 enable）
- **Absorb mechanism**：清算通过 `absorb` 函数执行

---

## 2. 风险机制

### 双 Collateral Factor

```text
Borrow Collateral Factor ≠ Liquidate Collateral Factor
```

| 参数 | 作用 |
|------|------|
| `borrowCollateralFactor` | 决定借款能力（能借多少） |
| `liquidateCollateralFactor` | 决定清算触发（何时被清算） |

### Account Liquidity / Shortfall

- **Account Liquidity** = Σ(collateral_value × borrowCF) - debt
- **Account Shortfall** = debt - Σ(collateral_value × liquidateCF)
- Liquidity > 0 → 安全
- Shortfall > 0 → 可被清算

### 与 Aave 的关键差异

| 维度 | Aave V3 | Compound III |
|------|---------|-------------|
| 风险指标 | Health Factor (HF < 1 = liquidatable) | Account Shortfall (> 0 = liquidatable) |
| Collateral Factor | Liquidation Threshold (LT) | borrowCF ≠ liquidateCF |
| Collateral enable | 需要手动 enable | 自动作为 collateral |
| 清算机制 | Liquidator repays debt + seizes collateral | Protocol absorbs collateral |
| 借款资产 | 多种 | 单一 base asset |

---

## 3. 关键事件

| 事件 | 含义 | 与 Aave 的对应 |
|------|------|---------------|
| `Supply(asset, amount)` | 供应 base asset（=还款） | Aave Repay |
| `Withdraw(asset, amount)` | 提取 base asset（=借款） | Aave Borrow |
| `AbsorbCollateral(absorber, borrower, asset, collateralAbsorbed, usdValue)` | 清算 | Aave LiquidationCall |
| `WithdrawCollateral(asset, amount)` | 提取抵押资产 | Aave Withdraw |

### 注意

Compound III 的接口设计与 Aave **相反**：
- "Supply USDC" 在 Compound III 中是**还款**（归还 base asset）
- "Withdraw USDC" 在 Compound III 中是**借款**（提取 base asset）
- 提取非 base asset 是**提取抵押品**

---

## 4. 清算机制

### Absorb 流程

```text
Account Shortfall > 0
    ↓
任何第三方调用 absorb()
    ↓
Protocol 吸收欠款账户的 collateral
    ↓
吸收的 collateral 按折扣价格出售给市场
    ↓
Base asset 从协议储备中覆盖欠款
```

### 与 Aave 的差异

- Aave：Liquidator 直接偿还债务并获取抵押品
- Compound III：Protocol 吸收抵押品，后续通过市场处理
- 这意味着 Compound III 的"清算"执行方式与 Aave 不同

---

## 5. 合约地址

- cUSDCv3 (Ethereum Mainnet Proxy): 参见 https://docs.compound.finance/ 部署页面
- Configurator: 管理 Comet 参数
- Bulker: 批量操作合约

---

## 6. 文档链接

| 内容 | 链接 |
|------|------|
| Compound III 官方文档 | https://docs.compound.finance/ |
| Compound V2 文档 | https://docs.compound.finance/v2 |
| 创建 Liquidator 指南 | https://docs.compound.finance/developer-resources/creating-a-compound-iii-liquidator/ |
| 开发者 FAQ | https://docs.compound.finance/developer-resources/faq/ |
| GitHub | https://github.com/compound-finance/comet |
