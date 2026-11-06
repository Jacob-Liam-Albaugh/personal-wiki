---
type: lecture
area: dsp
source-ref: "Topic DSP.2, pp. 1-17"
course: ece438
lecture: DSP.2
tags: [signals]
---

# ECE438 DSP.2 - DT systems

**Summary**: Systems as maps between signals; linearity and time invariance with worked proofs; the impulse response and the [[Convolution]] sum for an [[LTI system]]; how to evaluate a convolution by hand; causality and BIBO stability.

**File**: `Digital Signal Processing/Topic DSP.2 DT systems UPDATED Jan 22, 2025.pdf`

---

## Topics
- **System (DSP.2.1, p. 2)**: a map from one set of signals to another, $y[n]=\mathcal S(x)$. In block diagrams signals are arrows and systems are boxes.
- **Linearity and time invariance (DSP.2.2, pp. 3-8)**
  - Linear: $\mathcal S[a_1x_1+a_2x_2]=a_1\mathcal S[x_1]+a_2\mathcal S[x_2]$ for all signals and constants.
  - Time invariant: if $y_1=\mathcal S(x[n])$ and $y_2=\mathcal S(x[n-n_0])$ then $y_2[n]=y_1[n-n_0]$ for any $x$. Test: shift-then-system must equal system-then-shift.
  - Two proof approaches for non-linearity: expand both sides in general, or find one counterexample (one $a_1$, $x_1$ is enough).
- **Impulse response and convolution (DSP.2.3, pp. 9-13)**: every signal is a sum of weighted shifted impulses, and an LTI system maps each term to a weighted shifted impulse response.
- **Causality and stability (pp. 13-17)**.

## Key results
> [!theorem] Convolution sum
> $$y[n]=\sum_{k=-\infty}^{\infty}x[k]\,h[n-k]$$
> with $h[n]$ the response to $\delta[n]$ and $x[n]=\sum_k x[k]\delta[n-k]$. Convolution is commutative: $y[n]=\sum_k h[k]x[n-k]$. (source: p. 9)

> [!theorem] Causal LTI
> An LTI system is causal iff $h[n]=0$ for all $n<0$. An impulse can only affect the present and future. (source: p. 13)

> [!theorem] BIBO stability
> An LTI system is BIBO stable iff its impulse response is absolutely summable:
> $$\sum_{k=-\infty}^{\infty}|h[k]|<\infty$$
> Sufficiency: $|y[n]|\le\sum_k|h[k]|\,|x[n-k]|\le B\sum_k|h[k]|$ (uses LTI). Necessity: if the sum diverges, a bounded input (e.g. $x[n]=1$) can give an unbounded output. (source: pp. 15-17)

**Recipe for computing a convolution (p. 11)**: (1) pick one signal to flip and shift, $h[n-k]$ or $x[n-k]$; (2) it is now a function of $k$ as well as $n$; (3) write the other signal as a function of $k$; (4) identify the overlap scenarios as $n$ varies; (5) solve the sum in each region, each with its own bounds. Always sketch both signals; piecewise signals such as $u[n]$ make the regions tricky.

## Examples
> [!example] Accumulator $y[n]=\sum_{k=0}^{n}x[k]$ for $n\ge0$, else 0 (pp. 3-8, 15)
> Linear (both cases expand to $\sum_k[a_1x_1(k)+a_2x_2(k)]$). Time varying: with $x=\delta[n]$ the output is $u[n]$, but for $x[n+1]$ the output is $0\ne u[n+1]$, because "when you start your clock" at $n=0$ matters. Not BIBO stable: $x[n]=1$ gives $y[n]=n+1\to\infty$.

> [!example] $y[n]=2x[n]+3$ (pp. 5-8, 15)
> Not linear: with $a_1=2$, $a_2=0$, $x_1=1$, $\mathcal S(a_1x_1)=7$ but $a_1\mathcal S(x_1)=10$. Time invariant: replace $n$ by $n-n_0$ everywhere. BIBO stable: $|y|\le2|x|+3\le 2B+3$ (via $|a+b|\le|a|+|b|$), even though it is not linear.

> [!example] Convolution of $u[n]$ with $2^{-|n|}$ (pp. 11-13)
> Take $h[n]=u[n]$, $x[n]=2^{-|n|}$, flip $h$. For $n\le0$ one piece: $y[n]=\sum_{k=-\infty}^{n}2^k=2^{n+1}$. For $n>0$ two pieces ($k\le0$ and $1\le k\le n$): $y[n]=3-2^{-n}$.

## Connections
- The convolution sum is computed in the frequency domain in [[ECE438 DSP.3.D - Convolution with DFT]], and the stability condition returns as "poles inside the unit circle" in [[ECE438 DSP.6 - z-transforms]].
- System basics from ECE 301: [[ECE438 301R 2.2 - Time transformations]].

**Sources**: `Digital Signal Processing/Topic DSP.2 DT systems UPDATED Jan 22, 2025.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[LTI system]] · [[Convolution]] · [[Digital filter]] · [[ECE438 DSP.1 - DT signals]] · [[ECE438 DSP.3.A - DT frequency analysis 1]] · [[Discrete-time signal]]
