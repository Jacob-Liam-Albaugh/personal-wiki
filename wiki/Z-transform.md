---
type: definition
area: dsp
source-ref: "ECE 438 Topic DSP.6, pp. 1-16"
tags: [signals]
---

# Z-transform

**Summary**: Generalises the [[DTFT]] from the unit circle to the whole complex plane, $z=re^{j\omega}$. It handles signals with no DTFT, turns difference equations into rational functions, and reads causality and stability off the region of convergence (ROC) and the poles. The CT analogue is the [[Laplace transform]].

> [!definition] Z-transform and ROC
> $$X(z)=\sum_{n=-\infty}^{\infty}x[n]\,z^{-n}$$
> The ROC is the set of $z$ where the sum converges, and is part of the answer: $a^nu[n]$ and $-a^nu[-n-1]$ share $X(z)=\frac1{1-az^{-1}}$ but have ROC $|z|>|a|$ and $|z|<|a|$.
>
> (source: Topic DSP.6, pp. 2-5)

## ROC rules (pp. 8-10)
- A disc or ring centred at the origin; no poles inside it.
- Right-sided: outside the outermost pole. Left-sided: inside the innermost. Finite duration: whole plane except maybe $0$ and $\infty$.
- DTFT exists iff the ROC contains the unit circle.
- [[LTI system]]: causal iff ROC is an exterior; BIBO stable iff ROC contains the unit circle; causal and stable iff poles inside the unit circle.

## Properties and rational systems
Shift $x[n-n_0]\leftrightarrow z^{-n_0}X(z)$, convolution $\leftrightarrow X(z)H(z)$, time reversal $\leftrightarrow X(z^{-1})$, $nx[n]\leftrightarrow-z\,dX/dz$, upsampling by $k\leftrightarrow X(z^k)$ (p. 12).
A difference equation $y[n]=\sum_ib_ix[n-i]-\sum_ka_ky[n-k]$ gives
$$H(z)=\frac{\sum_ib_iz^{-i}}{1+\sum_ka_kz^{-k}}$$
FIR if all $a_k=0$, else IIR. Real $h[n]$ means poles and zeros come in conjugate pairs (pp. 6-7, 12). See [[Digital filter]].

> [!example] Inverse transform by partial fractions
> $$X(z)=\frac{1-4z^{-1}}{(1-2z^{-1})(1-z^{-1})}=\frac{-2}{1-2z^{-1}}+\frac3{1-z^{-1}}$$
> $|z|>2$: $x[n]=3u[n]-2\cdot2^nu[n]$. $1<|z|<2$: $x[n]=3u[n]+2\cdot2^nu[-n-1]$. $|z|<1$: both terms anti-causal. No case has the unit circle in its ROC, so no DTFT.
> Wiki note: the sheet's $|z|<1$ simplification drops a factor 2 on the $2^n$ term.
>
> (source: Topic DSP.6, pp. 13-15)

> [!theorem] Eigenfunction
> $z_0^n\to z_0^nH(z_0)$ for $z_0$ in the ROC (p. 16). Wiki note: the sheet writes $z_0H(z)$, which is a slip.

**Sources**: `Digital Signal Processing/Topic DSP.6 z-transforms March 7, 2025.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[ECE438 DSP.6 - z-transforms]] · [[ECE438 L20 - Optimal quantization and the z-transform]] · [[ECE438 L22 - More z-transform and exam 2 topics]]
- [[DTFT]] · [[Laplace transform]] · [[LTI system]] · [[Convolution]] · [[Digital filter]] · [[Fourier transform]]
