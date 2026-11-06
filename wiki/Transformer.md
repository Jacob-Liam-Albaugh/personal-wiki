---
type: concept
area: ml
areas: [ml]
source-ref: "Vaswani 2017, §3"
tags: [ml, generative]
---

# Transformer

**Summary**: Sequence model made of stacked [[Attention]] and position-wise feed-forward layers with residual connections and layer normalisation. It has no recurrence, so all positions are processed in parallel.

---

## Block structure

Each layer applies (source: Vaswani 2017, §3.1, p. 3):

$$y=\mathrm{LayerNorm}\big(x+\mathrm{Sublayer}(x)\big)$$

with two sub-layers: multi-head self-attention, then a feed-forward network. The decoder adds cross-attention to the encoder output and masks future positions.

## Properties

- Constant path length between any two positions, at $O(n^2 d)$ cost per layer (source: Vaswani 2017, Table 1).
- Needs explicit position information, supplied by sinusoidal encodings (source: §3.5).
- Residual connections let signals bypass sub-layers (see [[ResNet]]).

## Variants in this wiki

- [[Mixture of experts]]: replace the feed-forward network with routed experts ([[DeepSeek-V2 (DeepSeek-AI 2024)]]).
- [[DeepSeek-V2 (DeepSeek-AI 2024)]]: shrink the key-value cache at inference.
- [[State space model]]: attention-free backbone ([[Mamba (Gu 2023)]]).

Wiki note: the same attention and feed-forward blocks are reused in neural operators and diffusion backbones. I have not checked which pages here use them **[unverified]**.

**Sources**: Vaswani et al. 2017.
**Last updated**: 2026-11-06

---

## Related pages
- [[Attention is all you need (Vaswani 2017)]]
- [[Attention]]
- [[Mixture of experts]]
- [[State space model]]
- [[ResNet]]
- [[Dropout]]
