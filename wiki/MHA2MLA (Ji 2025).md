---
type: paper
area: ml
areas: [ml, math]
source-ref: "Ji et al., arXiv:2502.14837v1 (20 Feb 2025)"
tags: [ml]
authors: ["[[Tao Ji]]", "[[Bin Guo]]", "[[Yuanbin Wu]]", "[[Qipeng Guo]]", "[[Lixing Shen]]", "[[Zhan Chen]]", "[[Xipeng Qiu]]", "[[Qi Zhang]]", "[[Tao Gui]]"]
year: 2025
venue: "arXiv:2502.14837v1"
file: "papers/LLMs/LLMs - DeepSeek - Multi-Head Latent Attention.pdf"
---

# MHA2MLA (Ji 2025)

**Summary**: A data-efficient fine-tuning recipe that converts a pretrained multi-head (or grouped-query) attention LLM into DeepSeek's multi-head latent attention (MLA). It needs 3 to 6 per mille of the pretraining data and cuts the KV cache sharply.

**Authors**: Tao Ji, Bin Guo, Yuanbin Wu, Qipeng Guo, Lixing Shen, Zhan Chen, Xipeng Qiu, Qi Zhang, Tao Gui · **Year**: 2025 · **File**: `papers/LLMs/LLMs - DeepSeek - Multi-Head Latent Attention.pdf`

The file name says DeepSeek but this is a third-party paper about adopting MLA, not the DeepSeek MLA paper itself. The MLA definition is in [[DeepSeek-V2 (DeepSeek-AI 2024)]].

---

## Problem

MHA's KV cache grows linearly with sequence length and model size. GQA and MQA shrink it by pruning attention parameters and lose quality. MLA stores a low-rank latent instead, and reportedly does better than MHA (source: p. 1). Zero-shot conversion is impractical and pretraining MLA from scratch is expensive.

## MLA recap (as the paper states it)

Per head, split dimension $d_h=d_r+d_c$ (source: §2):

- Position-aware part, dimension $d_r$, with RoPE.
- Position-agnostic part (NoPE), dimension $d_c$, with keys and values built from a shared latent $c_{kv}=x_iW_{dkv}$.

The cache holds $c_{kv}$ and $k_\text{rope}$: $O(l(d_r+d_{kv}))$ against $O(2ln_hd_h)$ for MHA.

Why separate RoPE from NoPE: for NoPE the product $q_\text{nope}k_\text{nope}^T$ reduces to a fixed merged matrix times the cached latent. For RoPE the rotation depends on the relative offset $j-i$, so it cannot be merged (source: p. 3).

## Method

1. **Partial RoPE.** Keep RoPE on only $r$ of the $d_h/2$ two-dimensional frequency subspaces and turn the rest into NoPE. Four selection rules (source: §3.1, Fig. 2):
   - $S_\text{high}$: the $r$ fastest-rotating subspaces.
   - $S_\text{low}$: the $r$ slowest.
   - $S_\text{uniform}$: equally spaced.
   - $S_\text{2-norm}$: top-$r$ by head-wise 2-norm contribution of query and key components, which bounds a subspace's effect on the attention logit by Cauchy-Schwarz.
2. **Low-rank approximation.** Truncated SVD of the pretrained $W_{k,\text{nope}}$ and $W_v$:
   - SVDsplit: factorise each separately.
   - SVDjoint: factorise them jointly into one shared latent. The paper finds SVDjoint better (source: §3.2, Sec. 4.3).

Rotary rotations use angles $\theta_k=\beta^{-2k/d_h}$ per subspace $k$, with base $\beta$ typically $10^4$ (source: p. 4).

## Experiments

Models: SmolLM 135M, 360M, 1B7 and Llama2-7B (source: §4). Results table (source: p. 6, SmolLM 135M GQA to MLA, 2.25B fine-tuning tokens, 3.8 per mille):

| $d_{kv}$ | KV memory | Avg. change |
|---|---|---|
| 32 | -68.75% | -1.19 |
| 16 | -81.25% | -2.41 |
| 8 | -87.50% | -3.28 |

- 1B7 SmolLM (MHA to MLA): -1.17 at -68.75%, -2.32 at -87.50%.
- Abstract: Llama2-7B KV cache down 92.19% with a 0.5% drop on LongBench; combined with KV-cache quantisation up to 96.87% reduction (source: abstract, contributions).

I read the method and part of the table; ablations and conclusion not read in detail.

## Wiki note

The central trick, factorising a pretrained weight by truncated SVD to initialise a low-rank bottleneck, is a direct use of [[Singular value decomposition]].

%% refs:start %%
**Cites in this wiki**: [[Attention is all you need (Vaswani 2017)]]
%% refs:end %%

**Sources**: Ji et al. PDF (pp. 1-6).
**Last updated**: 2026-11-06

---

## Related pages
- [[DeepSeek-V2 (DeepSeek-AI 2024)]]
- [[Attention]]
- [[Transformer]]
- [[Singular value decomposition]]
- [[Mixture of experts]]
