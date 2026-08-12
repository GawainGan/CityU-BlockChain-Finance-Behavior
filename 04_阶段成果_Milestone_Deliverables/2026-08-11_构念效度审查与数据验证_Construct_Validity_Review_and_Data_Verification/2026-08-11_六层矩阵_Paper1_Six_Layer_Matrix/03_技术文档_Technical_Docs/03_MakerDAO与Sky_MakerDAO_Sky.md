# MakerDAO / Sky 技术文档

**官方文档**：https://docs.makerdao.com/ （现为 Sky Ecosystem）  
**GitHub**：https://github.com/sky-ecosystem  
**用途**：Paper 1 外部有效性检验协议

---

## 1. 协议概述

MakerDAO（现为 Sky Ecosystem）是一个去中心化借贷协议，用户通过锁定抵押品在 Vault 中生成 DAI（现为 USDS）稳定币。与 Aave/Compound 不同，Maker 使用 Vault 结构和 auction-based 清算机制。

### 关键特性

- **Vault-based**：每个借款人有一个或多个独立的 Vault
- **Single debt asset**：生成 DAI/USDS
- **Auction-based liquidation**：清算通过拍卖执行
- **Collateralization Ratio**：使用 collateralization ratio 而非 health factor

---

## 2. 风险机制

### 核心指标

```text
Collateralization Ratio = (Collateral Value × Liquidation Ratio) / Debt
```

- **Liquidation Ratio**：协议参数，低于此比率触发清算
- **Stability Fee**：借款利率
- **Liquidation Penalty**：清算罚金

### 与 Aave/Compound 的差异

| 维度 | Aave V3 | Compound III | MakerDAO |
|------|---------|-------------|----------|
| 风险指标 | HF (HF < 1) | Shortfall (> 0) | Collateralization Ratio (< LR) |
| 结构 | Position | Account | Vault |
| 清算方式 | Liquidator-based | Absorb mechanism | Auction-based |
| 借款资产 | 多种 | 单一 base asset | DAI/USDS |

---

## 3. Vault 操作

| 操作 | 含义 | 与 Aave 的对应 |
|------|------|---------------|
| `lock` | 锁入抵押品 | Supply + collateral-enabled |
| `free` | 释放抵押品 | Withdraw collateral |
| `draw` | 生成 DAI | Borrow |
| `wipe` | 偿还 DAI | Repay |

---

## 4. 清算机制

### Auction-based Liquidation

```text
Collateralization Ratio < Liquidation Ratio
    ↓
触发清算
    ↓
Collateral auction (Dutch auction 或 English auction)
    ↓
DAI/USDS 从拍卖中获得
    ↓
抵押品分配给拍卖参与者
```

### 与 Aave/Compound 的关键差异

- **时间更长**：Auction 过程需要时间，不是即时执行
- **价格发现**：Auction 本身是价格发现过程
- **批量处理**：可能影响清算的 timing 和 amount 度量

### 对 Paper 1 的影响

- Maker 更适合作为 **mechanism heterogeneity / external validity** 检验
- 不应简单拼到 Aave panel 里
- "Realized liquidation" 在 Maker 中的定义与 Aave 不同

---

## 5. 文档链接

| 内容 | 链接 |
|------|------|
| Sky Protocol 官方文档 | https://docs.makerdao.com/ |
| Chainlog（合约地址） | https://chainlog.sky.money/ |
| Portal | https://sky.money/ |
| GitHub | https://github.com/sky-ecosystem |
| MakerDAO Whitepaper | https://makerdao.com/whitepaper/ |

---

## 6. 相关文献

| 文献 | 标题 | 年份 | 链接 |
|------|------|------|------|
| Chaleenutthawut et al. | Loan Portfolio Dataset From MakerDAO Blockchain Project | 2024 | https://ieeexplore.ieee.org/document/10423641 |
