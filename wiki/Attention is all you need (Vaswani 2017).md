---
type: paper
area: ml
areas: [ml]
source-ref: "Vaswani et al., NIPS 2017, arXiv:1706.03762v7"
tags: [ml, generative]
authors: ["[[Ashish Vaswani]]", "[[Noam Shazeer]]", "[[Niki Parmar]]", "[[Jakob Uszkoreit]]", "[[Llion Jones]]", "[[Aidan N. Gomez]]", "[[Łukasz Kaiser]]", "[[Illia Polosukhin]]"]
year: 2017
venue: "NIPS 2017; arXiv:1706.03762v7"
file: "LLMs/LLMs - Attention is All You Need.pdf"
---

# Attention is all you need (Vaswani 2017)

**Summary**: Introduces the Transformer, a sequence-to-sequence architecture built only from attention and position-wise feed-forward layers, with no recurrence or convolution. It trains faster and in parallel, and set new translation records.

**Authors**: Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Łukasz Kaiser, Illia Polosukhin (equal contribution) · **Year**: 2017 · **File**: `LLMs/LLMs - Attention is All You Need.pdf`

---

## Motivation

Recurrent models compute hidden states $h_t$ from $h_{t-1}$, so they cannot be parallelised within an example (source: §1, p. 2). Convolutional alternatives (ConvS2S, ByteNet) relate distant positions in linear or logarithmic numbers of operations. Self-attention does it in a constant number (source: §2, p. 2), at the cost of reduced effective resolution from averaging, countered by multi-head attention.

## Architecture

Encoder-decoder (source: §3, p. 2-3, Fig. 1).

- Encoder: $N=6$ identical layers. Each has multi-head self-attention, then a position-wise feed-forward network. Each sub-layer is wrapped as $\mathrm{LayerNorm}(x+\mathrm{Sublayer}(x))$.
- Decoder: $N=6$ layers with a third sub-layer attending over the encoder output. Self-attention is masked (set to $-\infty$ before the softmax) so position $i$ sees only positions $\le i$.
- All sub-layers and embeddings have width $d_\text{model}=512$.

## Scaled dot-product attention

Queries, keys and values are vectors; the output is a weighted sum of values (source: §3.2.1, p. 4):

$$\mathrm{Attention}(Q,K,V)=\mathrm{softmax}\!\left(\frac{QK^{T}}{\sqrt{d_k}}\right)V$$

The $\sqrt{d_k}$ scaling is because for independent unit-variance components, $q\cdot k$ has variance $d_k$. Large dot products push the softmax into regions of tiny gradient (source: p. 4, footnote 4).

## Multi-head attention

Project $Q,K,V$ $h$ times with learned matrices, attend in parallel, concatenate, project (source: §3.2.2, p. 5):

$$\mathrm{MultiHead}=\mathrm{Concat}(\mathrm{head}_1,\dots,\mathrm{head}_h)W^O$$

$$\mathrm{head}_i=\mathrm{Attention}(QW_i^Q,KW_i^K,VW_i^V)$$

Base model: $h=8$, $d_k=d_v=64$, so total cost matches single-head attention at full width.

Three uses: encoder-decoder attention, encoder self-attention, masked decoder self-attention (source: §3.2.3).

## Other components

- Feed-forward, applied per position (source: §3.3):

$$\mathrm{FFN}(x)=\max(0,xW_1+b_1)W_2+b_2$$

with $d_{ff}=2048$.
- Embeddings share the weight matrix with the pre-softmax layer, scaled by $\sqrt{d_\text{model}}$.
- Sinusoidal positional encoding added to embeddings (source: §3.5):

$$PE_{(pos,2i)}=\sin\!\big(pos/10000^{2i/d_\text{model}}\big)$$

$$PE_{(pos,2i+1)}=\cos\!\big(pos/10000^{2i/d_\text{model}}\big)$$

For a fixed offset $k$, $PE_{pos+k}$ is a linear function of $PE_{pos}$, which the authors hypothesise helps learning relative positions. Learned embeddings gave nearly identical results.

## Why self-attention (Table 1)

| Layer | Cost per layer | Sequential ops | Max path |
|---|---|---|---|
| Self-attention | $O(n^2d)$ | $O(1)$ | $O(1)$ |
| Recurrent | $O(nd^2)$ | $O(n)$ | $O(n)$ |
| Convolutional | $O(knd^2)$ | $O(1)$ | $O(\log_k n)$ |
| Restricted self-attention | $O(rnd)$ | $O(1)$ | $O(n/r)$ |

Self-attention is cheaper than recurrence when $n<d$ (source: pp. 6-7).

## Training and results

- 8 NVIDIA P100 GPUs; base model 100,000 steps (12 hours), big model 300,000 steps (3.5 days).
- [[Adam]] with $\beta_1=0.9$, $\beta_2=0.98$, $\epsilon=10^{-9}$, linear warmup over 4000 steps then inverse-square-root decay.
- Residual dropout and label smoothing $\epsilon_{ls}=0.1$ (source: §5).
- WMT14 English-German: 28.4 BLEU, over 2 BLEU above previous best including ensembles. English-French: single-model record, 41.8 BLEU in the abstract (source: abstract, §6).
- Also applied to English constituency parsing (source: abstract).

## Flag

The abstract says 41.8 BLEU for English-French but the body text of §6.1 says 41.0. I did not resolve which is intended (Table 2 cells did not extract cleanly).

## Wiki note

Later work in this batch modifies each piece: [[Mixture of experts]] replaces the FFN, [[DeepSeek-V2 (DeepSeek-AI 2024)]] compresses the attention cache, and [[Mamba (Gu 2023)]] replaces attention with a [[State space model]].





%% refs:start %%
**Cites in this wiki**: [[Adam paper (Kingma 2015)]], [[Dropout paper (Srivastava 2014)]]
**Cited by in this wiki**: [[DDPM (Ho 2020)]], [[DeepONet (Lu 2021)]], [[Fourier features (Tancik 2020)]], [[MHA2MLA (Ji 2025)]], [[Mamba (Gu 2023)]], [[Neural operator (Kovachki 2022)]], [[Operator learning review (Kovachki 2024)]]
%% refs:end %%

**Sources**: Vaswani PDF (pp. 1-9).
**Last updated**: 2026-11-06

---

## Related pages
- [[Transformer]]
- [[Attention]]
- [[Mixture of experts]]
- [[State space model]]
- [[Adam]]
- [[Dropout]]
- [[ResNet]]
