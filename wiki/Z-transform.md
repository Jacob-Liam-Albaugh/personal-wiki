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
> $$X(z)=\frac{1-4z^{-1}}{1-3z^{-1}+2z^{-2}}=\frac{1-4z^{-1}}{(1-2z^{-1})(1-z^{-1})}=\frac{-2}{1-2z^{-1}}+\frac3{1-z^{-1}}$$
> $|z|>2$: $x[n]=3u[n]-2\cdot2^nu[n]$. $1<|z|<2$: $x[n]=3u[n]+2\cdot2^nu[-n-1]$. $|z|<1$: both terms anti-causal. No case has the unit circle in its ROC, so no DTFT.
> Wiki note: the sheet's $|z|<1$ simplification drops a factor 2 on the $2^n$ term.
>
> (source: Topic DSP.6, pp. 13-15)

> [!theorem] Eigenfunction
> $z_0^n\to z_0^nH(z_0)$ for $z_0$ in the ROC, since $y[n]=\sum_kh[k]z_0^{n-k}=z_0^nH(z_0)$ (p. 16). Wiki note: the sheet writes $z_0H(z)$, which is a slip.

## Motivation and the DTFT slice
Uses: understanding system stability, designing linear filters, and handling $h[n]$ with no DTFT (absolute summability is needed, e.g. $h[n]=e^nu[n]$ has no Fourier transform). The z-transform is to the [[Laplace transform]] what the DTFT is to the CT Fourier transform. $z=re^{j\omega}$ is any complex number, not only on the unit circle, and
$$H(e^{j\omega})=H(z)\big|_{z=e^{j\omega}}$$
when the unit circle is inside the ROC. The functional form of $X(z)$ alone does not determine $x[n]$; the ROC is critical (source: Topic DSP.6, pp. 1-3; L22 Mar 7, 2025.pdf, p. 1).

> [!example] Two-sided signal and its ring ROC
> $x[n]=a^nu[n]+b^nu[-n-1]$ converges for $|z|>|a|$ and $|z|<|b|$. If $a>b$ there is no ROC; if $a<b$ the ROC is the ring $|a|<|z|<|b|$, the intersection of the two pieces, and
> $$X(z)=\frac1{1-az^{-1}}-\frac1{1-bz^{-1}}$$
> Any causal signal has ROC outside a circle; any anti-causal signal has ROC inside a circle.
>
> (source: Topic DSP.6, pp. 3-5)

## Properties table and common pairs
| Property | $x[n]$ | $X(z)$ | ROC |
|---|---|---|---|
| linearity | $ax_1+bx_2$ | $aX_1+bX_2$ | at least $R_1\cap R_2$ |
| time shift | $x[n-n_0]$ | $z^{-n_0}X(z)$ | $R$, except maybe $z=0$ |
| convolution | $x*h$ | $X(z)H(z)$ | at least $R_1\cap R_2$ |
| upsampling | $x[r]$ if $n=rk$, else 0 | $X(z^k)$ | $R^{1/k}$ |
| time reversal | $x[-n]$ | $X(z^{-1})$ | $R^{-1}$ |
| differentiation | $nx[n]$ | $-z\,dX/dz$ | $R$ |

Also $h^*[n]\leftrightarrow H^*(z^*)$, so a real $h[n]$ has $H(z)=H^*(z^*)$ and poles and zeros come in conjugate pairs (source: Topic DSP.6, p. 12).

Common pairs, from Oppenheim and Willsky Table 10.2 as reproduced on p. 12:
$$\delta[n]\to1$$
$$u[n]\to\frac1{1-z^{-1}},\ |z|>1$$
$$\alpha^nu[n]\to\frac1{1-\alpha z^{-1}},\ |z|>|\alpha|$$
$$n\alpha^nu[n]\to\frac{\alpha z^{-1}}{(1-\alpha z^{-1})^2}$$
plus the cosine/sine and damped cosine/sine pairs. After the inversion lecture, the working picture is that the poles and zeros of a rational $H(z)$ govern system behaviour and $z^n$ is the eigenfunction of an [[LTI system]] (source: L23 Mar 10, 2025.pdf; L24 Mar 24, 2025.pdf, p. 1).

**Covered in**: ECE 438 DSP.6, L20-L24 z-transform parts (Topic DSP.6 z-transforms; L22 Mar 7, L23 Mar 10, L24 Mar 24, 2025 front pages)
**Sources**: `Digital Signal Processing/Topic DSP.6 z-transforms March 7, 2025.pdf`, `Digital Signal Processing/front page/L22 Mar 7, 2025.pdf`, `Digital Signal Processing/front page/L23 Mar 10, 2025.pdf`, `Digital Signal Processing/front page/L24 Mar 24, 2025.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[DTFT]] · [[Laplace transform]] · [[LTI system]] · [[Convolution]] · [[Digital filter]] · [[Fourier transform]]
