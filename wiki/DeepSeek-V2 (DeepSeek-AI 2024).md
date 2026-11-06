---
type: paper
area: ml
areas: [ml]
source-ref: "DeepSeek-AI, DeepSeek-V2, arXiv:2405.04434v5 (19 Jun 2024), §1-2, §3.1"
tags: [ml, generative]
authors: ["[[DeepSeek-AI]]"]
year: 2024
venue: "arXiv:2405.04434v5"
file: "papers/LLMs/LLMs - DeepSeek - MoE Language Model.pdf"
---

# DeepSeek-V2 (DeepSeek-AI 2024)

**Summary**: A 236B-parameter [[Mixture of experts]] language model with 21B parameters active per token and 128K context. It pairs Multi-head Latent Attention (MLA), which compresses the key-value cache, with the DeepSeekMoE feed-forward design.

**Authors**: DeepSeek-AI · **Year**: 2024 · **File**: `papers/LLMs/LLMs - DeepSeek - MoE Language Model.pdf`

---

## Headline claims

Against DeepSeek 67B (dense): 42.5% lower training cost, 93.3% smaller KV cache, 5.76 times the maximum generation throughput (source: abstract, Fig. 1). Pretrained on 8.1T tokens, then SFT (1.5M conversations) and RL with GRPO (source: §1, p. 4).

## Multi-head latent attention

Standard [[Attention]] caches $2n_hd_hl$ elements per token ($l$ layers), which limits batch size and length (source: §2.1.1, p. 7). MQA and GQA cut the cache but lose quality (source: §2.1).

MLA compresses keys and values jointly through a low-rank latent (source: eqs. 10-11):

$$c^{KV}_t=W^{DKV}h_t$$

$$k^C_t=W^{UK}c^{KV}_t,\qquad v^C_t=W^{UV}c^{KV}_t$$

with $d_c\ll d_hn_h$. Only $c^{KV}_t$ is cached, $d_cl$ elements. At inference $W^{UK}$ is absorbed into $W^Q$ and $W^{UV}$ into $W^O$, so keys and values need never be formed (source: p. 7). Queries are also compressed, to save training activation memory (eqs. 12-13).

### Decoupled RoPE

Rotary position embedding is position dependent, so it would sit between $W^Q$ and $W^{UK}$ and block the absorption. MLA therefore adds separate small RoPE-carrying queries and a shared key $k^R_t$ and concatenates (source: §2.1.3, eqs. 14-17):

$$q_{t,i}=[q^C_{t,i};q^R_{t,i}],\qquad k_{t,i}=[k^C_{t,i};k^R_t]$$

The cache then holds $(d_c+d_h^R)\,l$ elements.

### Cache comparison (Table 1)

| Mechanism | KV cache per token |
|---|---|
| MHA | $2n_hd_hl$ |
| GQA | $2n_gd_hl$ |
| MQA | $2d_hl$ |
| MLA | $(d_c+d_h^R)\,l\approx\tfrac92d_hl$ |

For DeepSeek-V2, $d_c=4d_h$ and $d_h^R=d_h/2$, equal to GQA with 2.25 groups, yet stronger than MHA (source: p. 9).

## DeepSeekMoE

Two ideas: finer-grained experts for specialisation, and shared experts to reduce redundancy among routed ones (source: §2.2.1). FFN output (eqs. 20-22):

$$h'_t=u_t+\sum_{i=1}^{N_s}\mathrm{FFN}^{(s)}_i(u_t)+\sum_{i=1}^{N_r}g_{i,t}\,\mathrm{FFN}^{(r)}_i(u_t)$$

$$g_{i,t}=s_{i,t}\ \text{if}\ s_{i,t}\in\mathrm{Topk}(\{s_{j,t}\},K_r),\ \text{else }0$$

$$s_{i,t}=\mathrm{Softmax}_i(u_t^Te_i)$$

Here $e_i$ is the centroid of routed expert $i$.

- Device-limited routing: each token's experts lie on at most $M$ devices; $M\ge3$ performs close to unrestricted top-$K$ (source: §2.2.2).
- Three balance losses (source: eqs. 23-30): expert-level, device-level, communication.

$$\mathcal L_\text{ExpBal}=\alpha_1\sum_{i=1}^{N_r}f_iP_i$$

where $f_i$ is the scaled fraction of tokens choosing expert $i$ and $P_i$ the mean affinity.
- Device-level token dropping in training (lowest-affinity tokens), with about 10% of sequences exempt; not applied at inference (source: §2.2.4).

## Configuration

60 layers; $n_h=128$; all FFNs but the first are MoE with 2 shared and 160 routed experts (expert width 1536), 6 routed active per token; 236B total, 21B active. AdamW with $\beta_1=0.9$, $\beta_2=0.95$, weight decay 0.1, peak learning rate $2.4\times10^{-4}$ (source: §3.1.2).

Not read in detail: evaluations, alignment, appendices.

## Wiki note

Compare MLA's down-projection then up-projection with a low-rank factorisation (see [[Singular value decomposition]]); [[MHA2MLA (Ji 2025)]] makes this explicit by initialising the factors from an SVD of a pretrained model.

**Sources**: DeepSeek-V2 PDF (pp. 1-11, §3.1 hyperparameters).
**Last updated**: 2026-11-06

---

## Related pages
- [[Mixture of experts]]
- [[Attention]]
- [[Transformer]]
- [[Attention is all you need (Vaswani 2017)]]
- [[MHA2MLA (Ji 2025)]]
- [[Singular value decomposition]]
