---
type: concept
area: ml
areas: [ml]
source-ref: "Vaswani 2017, §3.2"
tags: [ml]
---

# Attention

**Summary**: Maps a query and a set of key-value pairs to an output that is a weighted sum of the values, with weights from query-key compatibility (source: Vaswani 2017, §3.2, p. 3-4).

---

## Scaled dot-product form

$$\mathrm{Attention}(Q,K,V)=\mathrm{softmax}\!\left(\frac{QK^{T}}{\sqrt{d_k}}\right)V$$

- The $\sqrt{d_k}$ factor keeps dot-product variance at one so the softmax does not saturate (source: p. 4).
- Alternative: additive attention with a one-hidden-layer network. Similar in theory, but dot-product is faster and smaller in practice because it uses matrix multiplication (source: p. 4).

## Multi-head

Run $h$ attention functions on learned projections of $Q,K,V$ and concatenate. A single head averages away information from different subspaces (source: §3.2.2).

## Self-attention

Queries, keys and values all come from the same sequence, so each position relates to every other. Cost is $O(n^2d)$ per layer (source: Table 1).

## Masking

Setting illegal entries to $-\infty$ before the softmax gives causal attention for autoregressive decoding (source: §3.2.3).

## Cost and alternatives

- Quadratic in sequence length. Restricting to a neighbourhood of size $r$ cuts cost to $O(rnd)$ (source: p. 7).
- [[DeepSeek-V2 (DeepSeek-AI 2024)]] compresses the cached keys and values.
- [[Mamba (Gu 2023)]] replaces attention with a selective [[State space model]] that is linear in length.

Wiki note: the softmax weights are also a kernel smoother, so [[Kernel methods]] give a related view **[unverified]**.

**Sources**: Vaswani et al. 2017.
**Last updated**: 2026-11-06

---

## Related pages
- [[Transformer]]
- [[Attention is all you need (Vaswani 2017)]]
- [[State space model]]
- [[Mixture of experts]]
- [[Kernel methods]]
