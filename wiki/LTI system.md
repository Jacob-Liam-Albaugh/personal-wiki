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
> Proof: $y[n]=\sum_kh[k]e^{j\omega(n-k)}=e^{j\omega n}\sum_kh[k]e^{-j\omega k}$.
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

### Proof techniques
Time invariance test: shift the input, run the system, and compare with the shifted output; they must agree for every $x$. To show non-linearity either expand both sides for general $a_1,a_2,x_1,x_2$ or give one counterexample (a single $a_1,x_1$ suffices) (source: Topic DSP.2, pp. 3-8).

The impulse response comes from writing any input as $x[n]=\sum_kx[k]\delta[n-k]$: by linearity and time invariance each term maps to a weighted, shifted copy of $h$ (source: Topic DSP.2, pp. 9-13). The recipe for evaluating the sum by hand is on [[Convolution]].

> [!theorem] BIBO stability of an LTI system
> The system is BIBO stable iff $\sum_k|h[k]|<\infty$.
> Sufficiency: if $|x|\le B$ then $|y[n]|\le\sum_k|h[k]||x[n-k]|\le B\sum_k|h[k]|$.
> Necessity: if the sum diverges, a bounded input such as $x[n]=\mathrm{sgn}\,h[-n]$ gives an unbounded output at $n=0$.
>
> (source: Topic DSP.2, pp. 15-17)

> [!example] Accumulator $y[n]=\sum_{k=0}^{n}x[k]$, $n\ge0$, else $0$
> Linear: both sides expand to $\sum_k[a_1x_1(k)+a_2x_2(k)]$. Time varying: $x=\delta[n]$ gives $u[n]$, but $x[n+1]$ gives $0\ne u[n+1]$, because the clock starts at $n=0$. Not BIBO stable: $x[n]=1$ gives $y[n]=n+1\to\infty$.
>
> (source: Topic DSP.2, pp. 3-8, 15)

> [!example] $y[n]=2x[n]+3$
> Not linear: with $a_1=2$, $a_2=0$, $x_1=1$, $\mathcal S(a_1x_1)=7$ but $a_1\mathcal S(x_1)=10$. Time invariant: replace $n$ by $n-n_0$ everywhere. BIBO stable: $|y|\le2|x|+3\le2B+3$, even though it is not linear.
>
> (source: Topic DSP.2, pp. 5-8, 15)

### FIR and IIR
An FIR system is a DT LTI system with a finite impulse response; an IIR system has an infinite one. If $H(z)$ is a ratio of polynomials, factoring numerator and denominator gives the zeros and poles, which govern the behaviour of the system (source: L23 Mar 10, 2025.pdf, p. 1). See [[Z-transform]] and [[Digital filter]].

Given an input-output relationship, the preferred way to find $H(e^{j\omega})$ is to take the DTFT of both sides, using the time-shift property $x[n-n_0]\leftrightarrow e^{-j\omega n_0}X$ and the convolution property $Y=XH$ (source: L15 Feb 19, 2025.pdf, p. 1); see [[DTFT]].

## Where it appears
- [[Transmission line]]: lossless lines as delay elements, reflection analysis for pulses ([[Transmission line]]).

**Covered in**: ECE 438 DSP.2 (Topic DSP.2 DT systems), L23 (L23 Mar 10, 2025.pdf), L15 (L15 Feb 19, 2025.pdf)
**Sources**: `Digital Signal Processing/Topic DSP.2 DT systems UPDATED Jan 22, 2025.pdf`, `Digital Signal Processing/Topic DSP.3.A DT frequency analysis Part 1 Jan 31, 2025.pdf`, `Digital Signal Processing/Topic DSP.6 z-transforms March 7, 2025.pdf`, `Digital Signal Processing/exam_1_review_transcribed.pdf`, `Digital Signal Processing/front page/L23 Mar 10, 2025.pdf`, `Digital Signal Processing/front page/L15 Feb 19, 2025.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Convolution]] · [[Digital filter]] · [[DTFT]] · [[DFT]] · [[Z-transform]] · [[Fourier transform]] · [[Discrete-time signal]]
