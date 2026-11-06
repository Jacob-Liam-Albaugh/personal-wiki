---
type: definition
area: dsp
source-ref: "ECE 438 Topic DSP.1; ECE 301 review topics 2.1-2.3; exam 1 review"
tags: [signals]
---

# Discrete-time signal

**Summary**: A function defined on the integers, $x[n]$ with $n\in\mathbb Z$. It is the object that every other DSP page operates on: [[LTI system]] inputs, [[DFT]] and [[DTFT]] arguments, samples from a [[Sampling theorem]] chain.

## Definition and representations
> [!definition] DT signal
> A map $x:\mathbb Z\to\mathbb R$ (or $\mathbb C$). It must be defined for every integer $n$. A digital signal also has integer values, $\mathbb Z\to\mathbb Z$.
>
> (source: Topic DSP.1 DT signals Jan 14, 2025.pdf, pp. 2-3)

Four representations: formula, stem plot, table, column vector in $\mathbb R^N$ (source: Topic DSP.1, pp. 3-5). Special signals: unit impulse $\delta[n]$, unit step $u[n]$, sinusoid $\sin(\omega n+\phi)$.

## Energy and power
> [!definition] Energy and power
> $$\mathcal E=\sum_{n=-\infty}^{\infty}|x[n]|^2$$
> $$P=\lim_{N\to\infty}\frac1{2N+1}\sum_{n=-N}^{N}|x[n]|^2$$
> Energy signals have $\mathcal E<\infty$ (so $P=0$); power signals have $0<P<\infty$.
>
> (source: Topic 2.1 power and energy Jul 17, 2022.pdf; Topic DSP.1, p. 7)

## Periodicity
> [!theorem] Periodic DT sinusoid
> $x[n]=x[n+N]$ for all $n$, some integer $N>0$. A DT sinusoid $\cos(\omega_0 n)$ is periodic iff
> $$\frac{\omega_0}{2\pi}\ \text{is rational}$$
> equivalently $\omega_0N=2\pi k$ for integers $N,k$. The fundamental period is the smallest such $N$.
>
> (source: exam_1_review_transcribed.pdf, p. 2; Topic 2.3 period of a signal Note Jul 23, 2022.pdf)

> [!example] Periodic and aperiodic cosines
> $\cos(\tfrac\pi4 n)$: $\omega_0=\pi/4$, so $N=8k$, smallest $N=8$, periodic.
> $\cos(n)$: $\omega_0=1$, $N=2\pi k$ with $2\pi$ irrational, so aperiodic.
> A periodic signal has infinite duration, and a finite-duration signal cannot be periodic (Topic DSP.1).
>
> (source: exam_1_review_transcribed.pdf, p. 2)

Frequencies $\omega$ and $\omega+2\pi$ give the same DT exponential, and the fastest oscillation is $\omega=\pm\pi$, $\cos(\pi n)=(-1)^n$ (source: Topic DSP.1). This is the root of [[Aliasing]] in DT.

## Time transformations
Shift $x[n-n_0]$, reversal $x[-n]$, and down/up-sampling are the basic operations; the CT versions and the order-of-operations rules are in [[ECE438 301R 2.2 - Time transformations]]. Wiki note: in DT, scaling is not a free operation. $x[2n]$ drops samples and can alias; see [[ECE438 DSP.4.B - Sampling DT]].

**Sources**: `Digital Signal Processing/Topic DSP.1 DT signals Jan 14, 2025.pdf`, `Digital Signal Processing/301 Review/Topic 2.1 power and energy Jul 17, 2022.pdf`, `Digital Signal Processing/301 Review/Topic 2.3 period of a signal Note Jul 23, 2022.pdf`, `Digital Signal Processing/exam_1_review_transcribed.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[ECE438 DSP.1 - DT signals]] · [[ECE438 301R 2.1 - Power and energy]] · [[ECE438 301R 2.3 - Period of a signal]]
- [[LTI system]] · [[Convolution]] · [[DFT]] · [[DTFT]] · [[Fourier transform]] · [[Z-transform]] · [[Sampling theorem]] · [[Quantization]]
