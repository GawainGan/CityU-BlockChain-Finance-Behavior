# Ethereum Finality 技术文档

**官方文档**：https://ethereum.org/en/developers/docs/consensus-mechanisms/pos/  
**用途**：Paper 1 数据可靠性声明；区分 execution / finality / economic settlement

---

## 1. 概述

Ethereum 于 2022 年从 Proof-of-Work 切换到 Proof-of-Stake。在 PoS 下，验证者通过质押 32 ETH 参与共识，对区块进行验证和提议。

---

## 2. 交易执行流程

```text
1. 用户创建并签名交易
    ↓
2. 交易提交到 execution client
    ↓
3. 交易进入 mempool 并广播到网络
    ↓
4. Block proposer（随机选中的验证者）将交易打包进区块
    ↓
5. 执行客户端在本地执行交易，生成状态变化
    ↓
6. 共识客户端将 execution payload 包装为 beacon block
    ↓
7. 其他验证者重新执行交易，验证状态变化
    ↓
8. 验证者发送 attestation（投票）
    ↓
9. 区块被添加到链上
```

---

## 3. Finality 机制

### Checkpoints

- 每个 epoch（32 slots = ~6.4 分钟）的第一个 block 是 checkpoint
- 验证者对 checkpoint 对进行投票

### Justified → Finalized

```text
Checkpoint A (already justified)
    ↓
Supermajority link (2/3 stake votes A → B)
    ↓
Checkpoint B becomes "justified"
    ↓
Next supermajority link (B → C)
    ↓
Checkpoint A becomes "finalized"
```

### 关键属性

- **Finalized 区块**：回滚需要至少 1/3 的总质押 ETH 被罚没（经济上不可行）
- **Justified 区块**：有较高确认度但尚未达到最终性
- **未达到 finality 的区块**：理论上可以被 reorg

### Execution ≠ Finality

```text
Transaction executed (included in block)
    ≠
Transaction finalized (2/3 stake confirmed)
```

---

## 4. 对 Paper 1 的影响

### 数据可靠性

- 分析中使用的所有交易数据应来自 finalized 区块
- Archive node 默认提供 finalized 状态
- Dune Analytics 通常只索引 finalized 数据

### 术语使用

| 情境 | 可以说 | 不应该说 |
|------|--------|---------|
| 交易被执行 | "the transaction was executed and recorded on-chain" | "the transaction was settled"（不区分层级） |
| 交易达到 finality | "the transaction reached protocol consensus finality" | "the transaction reached final economic settlement" |
| 讨论债权债务 | — | "on-chain execution = legal discharge"（execution ≠ legal settlement） |

### 三层 Settlement

```text
Technical / Ledger Settlement → 交易上链、执行、状态更新、最终确认
Protocol-level Settlement     → 协议内义务了结（如 Repay）
Economic / Business Settlement → 商业上代表什么（需要链下信息）
```

---

## 5. Fork Choice

- **LMD-GHOST**：选择具有最大 attestation 权重的 fork
- 在正常情况下，只有一个 fork
- 在网络分区时，可能出现竞争 fork

### 对研究的影响

- 在极端网络条件下，交易可能被 reorg
- 但 finalized 区块不会被 reorg（除非经济攻击）
- 研究应使用 finalized 数据

---

## 6. 文档链接

| 内容 | 链接 |
|------|------|
| Proof of Stake | https://ethereum.org/en/developers/docs/consensus-mechanisms/pos/ |
| Finality | https://ethereum.org/en/developers/docs/consensus-mechanisms/pos/#finality |
| Fork Choice | https://ethereum.org/en/developers/docs/consensus-mechanisms/pos/#fork-choice |
| PoS Attack and Defense | https://ethereum.org/en/developers/docs/consensus-mechanisms/pos/pos-vs-pow/ |
