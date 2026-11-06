---
type: paper
area: ml
areas: [ml, math]
source-ref: "Gu & Dao, arXiv:2312.00752v2 (31 May 2024), §2-4"
tags: [ml, signals]
authors: ["[[Albert Gu]]", "[[Tri Dao]]"]
year: 2023
venue: "arXiv:2312.00752 (v2, 31 May 2024)"
file: "LLMs/Gu, Dao - Mamba.pdf"
---

# Mamba (Gu 2023)

**Summary**: Makes structured state space model parameters depend on the input (selection), which lets a linear-time recurrent model filter and remember content like attention does. A hardware-aware scan keeps it fast, and a single homogeneous block, with no attention or MLP, forms the Mamba architecture.

**Authors**: Albert Gu, Tri Dao · **Year**: 2023 (v1; the PDF is v2, 2024) · **File**: `LLMs/Gu, Dao - Mamba.pdf`

---

## Background: structured SSMs

A continuous system maps $x(t)\to y(t)$ through a latent state (source: §2, eq. 1):

$$h'(t)=Ah(t)+Bx(t)$$

$$y(t)=Ch(t)$$

Discretisation with step $\Delta$ (zero-order hold, eq. 4):

$$\bar A=\exp(\Delta A)$$

$$\bar B=(\Delta A)^{-1}(\exp(\Delta A)-I)\,\Delta B$$

Then the model is a recurrence (eq. 2) or a global convolution (eq. 3):

$$h_t=\bar Ah_{t-1}+\bar Bx_t,\qquad y_t=Ch_t$$

$$y=x*\bar K,\quad \bar K=(C\bar B,C\bar A\bar B,\dots)$$

Convolution gives parallel training; recurrence gives cheap autoregressive inference. Both need linear time invariance (LTI): $(\Delta,A,B,C)$ fixed in time (source: pp. 3-4). Here $A$ is diagonal, so state size is $N$ per channel and total hidden state is $DN$.

## The problem: LTI cannot select

Sequence modelling is compression of context into state. Attention does not compress (the KV cache holds everything), so it is effective but quadratic. Recurrent models have fixed-size state, so quality depends on the compression (source: §3.1, p. 5).

- Selective Copying has random spacing between tokens. A static convolution kernel cannot solve it.
- Induction Heads needs associative recall in context.

## Selection mechanism

Make $B$, $C$, $\Delta$ functions of the input (Algorithm 2, "S6") (source: §3.2, p. 5):

$$s_B(x)=\mathrm{Linear}_N(x),\quad s_C(x)=\mathrm{Linear}_N(x)$$

$$s_\Delta(x)=\mathrm{Broadcast}_D(\mathrm{Linear}_1(x)),\quad \tau_\Delta=\mathrm{softplus}$$

The model becomes time-varying, so the convolutional form is lost.

- Theorem 1 (§3.5.1): for $N=1$, $A=-1$, $B=1$ the recurrence reduces to a classical gate, $h_t=(1-g_t)h_{t-1}+g_tx_t$ with $g_t=\sigma(\mathrm{Linear}(x_t))$. Discretisation is the principled basis of RNN gating.
- Large $\Delta$ resets the state and focuses on the current input; small $\Delta$ keeps state and ignores the input (§3.5.2).
- Selectivity gives variable spacing, context filtering and boundary resetting. Making $A$ selective adds little because it acts through $\Delta$ (source: p. 9).
- Real-valued state is the default; complex helps continuous modalities (source: p. 9).

## Hardware-aware scan

The expanded state has shape $(B,L,D,N)$, a factor $N$ bigger than input. Three classical techniques (source: §3.3.2, p. 7):

- Kernel fusion: discretise and scan in fast SRAM, writing only $(B,L,D)$ outputs back to HBM.
- Parallel scan to avoid sequential recurrence.
- Recomputation of intermediate states in the backward pass.

Memory then matches an optimised Transformer with FlashAttention. The paper reports up to 3 times faster than prior methods on A100 (source: p. 2).

## Architecture

Merge the H3 block and the gated MLP into one Mamba block, repeated homogeneously with normalisation and residuals (source: §3.4, Fig. 3). Expansion factor $E=2$; most parameters are in the projections ($3ED^2$). Two blocks match the $12D^2$ parameters of an attention plus MLP pair. SiLU activation.

## Results

- Synthetics: solves Selective Copying (Mamba layer in Mamba block 99.8% in Table 1) and Induction Heads, extrapolating to length $2^{20}$ (about 1M), 4000 times the training length (source: §4.1, p. 10).
- Language: Chinchilla-style scaling laws from about 125M to 1.3B parameters on the Pile; Mamba beats the baselines, including strong LLaMa-style Transformer recipes (source: §4.2).
- Abstract claims: 5 times the generation throughput of Transformers, and Mamba-3B matching Transformers twice its size.
- Audio and DNA: improves with context up to million-length (source: abstract).

I did not read the appendices or the later tables in full.

## Wiki note

The SSM here is the classical linear state space model of control with input-dependent discretisation, so [[Kalman filter]] and [[LTI system]] are the closest older relatives. The paper itself lists Kalman filters among the uses of the term (source: p. 4).





%% refs:start %%
**Cites in this wiki**: [[Attention is all you need (Vaswani 2017)]]
%% refs:end %%

**Sources**: Gu & Dao PDF (pp. 1-11 read in detail).
**Last updated**: 2026-11-06

---

## Related pages
- [[State space model]]
- [[Transformer]]
- [[Attention]]
- [[Attention is all you need (Vaswani 2017)]]
- [[Kalman filter]]
- [[LTI system]]
- [[Convolution]]
