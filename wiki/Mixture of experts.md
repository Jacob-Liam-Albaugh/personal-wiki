---
type: concept
area: ml
areas: [ml]
source-ref: "DeepSeek-V2 2024, §2.2"
tags: [ml]
---

# Mixture of experts

**Summary**: Replace a dense feed-forward layer with many expert networks and a router that sends each token to a few of them. Total parameters grow while per-token compute stays small (source: DeepSeek-V2, abstract: 236B total, 21B active).

---

## Gating

A router scores each token against each expert, keeps the top $K$, and weights expert outputs by the scores. In DeepSeekMoE (source: DeepSeek-V2, eqs. 20-22):

$$h'_t=u_t+\sum_i\mathrm{FFN}^{(s)}_i(u_t)+\sum_ig_{i,t}\,\mathrm{FFN}^{(r)}_i(u_t)$$

with $g_{i,t}$ nonzero only for the top-$K_r$ routed experts.

## Design choices

- Fine-grained experts: many small ones, for sharper specialisation.
- Shared experts: always on, absorbing common knowledge so routed experts need not duplicate it.
- Load balance: without it routing collapses onto few experts. Auxiliary losses at expert, device and communication level; token dropping under capacity limits (source: §2.2.3-2.2.4).
- Device-limited routing bounds communication when experts are spread over devices (source: §2.2.2).

## Where it sits

It replaces the FFN of the [[Transformer]] block, leaving [[Attention]] untouched. DeepSeek-V2 pairs it with latent attention for the cache ([[DeepSeek-V2 (DeepSeek-AI 2024)]]).

Wiki note: the idea of weighting several sub-models by input-dependent gates predates deep learning; here the gates are sparse so unused experts cost nothing.

**Sources**: DeepSeek-AI 2024.
**Last updated**: 2026-11-06

---

## Related pages
- [[DeepSeek-V2 (DeepSeek-AI 2024)]]
- [[Transformer]]
- [[Attention]]
- [[MHA2MLA (Ji 2025)]]
