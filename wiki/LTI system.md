---
type: definition
area: dsp
source-ref: "ECE 438 Topic DSP.2, DSP.3.A, DSP.6; exam 1 review"
tags: [signals]
---

# LTI system

**Summary**: A linear, time-invariant system on [[Discrete-time signal]]s. Its whole behaviour is the impulse response $h[n]$, the output is [[Convolution]] with $h$, and complex exponentials pass through as eigenfunctions, which is why frequency-domain analysis ([[DTFT]], [[Z-transform]]) works.

## Definitions
> [!definition] Linear, time invariant
> Linear: $\mathcal S[a_1x_1+a_2x_2]=a_1\mathcal S[x_1]+a_2\mathcal S[x_2]$.
> Time invariant: if $y_1=\mathcal S(x[n])$ then $\mathcal S(x[n-n_0])=y_1[n-n_0]$.
>
> (source: Topic DSP.2, pp. 3-8)

> [!theorem] Impulse response
> $$y[n]=\sum_{k}x[k]\,h[n-k]$$
> with $h[n]=\mathcal S(\delta[n])$. (source: Topic DSP.2, p. 9)

## Causality and stability
- Causal: output at $n$ depends only on $x[m]$, $m\le n$. For LTI, iff $h[n]=0$ for $n<0$ (DSP.2, p. 13).
- BIBO stable: bounded input gives bounded output. For LTI, iff $\sum_k|h[k]|<\infty$ (DSP.2, pp. 15-17).
- In the $z$-domain: causal iff ROC is outside a circle; stable iff ROC contains the unit circle; causal and stable iff all poles are inside it (DSP.6, pp. 8-10).

## Eigenfunctions and frequency response
> [!theorem] Eigenfunction
> $$x[n]=e^{j\omega n}\ \Rightarrow\ y[n]=H(e^{j\omega})\,e^{j\omega n}$$
> $$H(e^{j\omega})=\sum_kh[k]e^{-j\omega k}$$
> More generally $z_0^n\to z_0^nH(z_0)$ for $z_0$ in the ROC.
>
> (source: Topic DSP.3.A, p. 4; Topic DSP.6, p. 16)

> [!example] Exam 1 review: system properties
> $y[n]=x[n-1]+x[n+2]$ is linear (homogeneity and additivity both checked), BIBO stable (only shifts), but non-causal because it uses $x[n+2]$.
> $y[n]=\big(\sum_{k=0}^nx[k]\big)^2$ is causal, non-linear, and BIBO unstable: with $x=u[n]$, $y[n]=(n+1)^2$ grows without bound.
>
> (source: exam_1_review_transcribed.pdf, pp. 6-7)

> [!example] Exam 1 review: frequency response (Quiz 3)
> $H(e^{j\omega})=\dfrac1{1-\frac12e^{-j\omega}}$. Output in the time domain, no Fourier transform needed:
> (a) $x_1[n]=e^{j\pi n/2}$ is an eigenfunction, so $y_1[n]=H(e^{j\pi/2})\,e^{j\pi n/2}$.
> (b) $x_2[n]=1+e^{j\pi n/2}$: by linearity, the constant ($\omega=0$) gets $H(e^{j0})=\frac1{1-1/2}=2$, so
> $$y_2[n]=2+H(e^{j\pi/2})\,e^{j\pi n/2}$$
>
> (source: exam_1_review_transcribed.pdf, pp. 8-9)

Wiki note: the unit-step input in the instability example shows why BIBO is a statement about all bounded inputs: one bad input is enough.

## Where it appears
- [[Transmission line]]: lossless lines as delay elements, reflection analysis for pulses ([[ECE311 lect_44 - Pulses on transmission lines]]).

**Sources**: `Digital Signal Processing/Topic DSP.2 DT systems UPDATED Jan 22, 2025.pdf`, `Digital Signal Processing/Topic DSP.3.A DT frequency analysis Part 1 Jan 31, 2025.pdf`, `Digital Signal Processing/Topic DSP.6 z-transforms March 7, 2025.pdf`, `Digital Signal Processing/exam_1_review_transcribed.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[ECE438 DSP.2 - DT systems]] · [[ECE438 DSP.6 - z-transforms]] · [[ECE438 L23 - System stability, causality and eigenfunctions]]
- [[Convolution]] · [[Digital filter]] · [[DTFT]] · [[DFT]] · [[Z-transform]] · [[Fourier transform]] · [[Discrete-time signal]]
