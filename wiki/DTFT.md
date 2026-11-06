---
type: definition
area: dsp
source-ref: "ECE 438 Topic DSP.3.C, DSP.4.B, DSP.6; ECE 301 equation sheet pp. 2, 7-8"
tags: [signals]
---

# DTFT

**Summary**: The discrete-time Fourier transform of an aperiodic [[Discrete-time signal]]: a continuous, $2\pi$-periodic function of $\omega$. The [[DFT]] samples it, the [[Z-transform]] reduces to it on the unit circle, and [[Spectral leakage]] is its windowing effect.

> [!definition] DTFT pair
> $$X(e^{j\omega})=\sum_{n=-\infty}^{\infty}x[n]\,e^{-j\omega n}$$
> $$x[n]=\frac1{2\pi}\int_{2\pi}X(e^{j\omega})\,e^{j\omega n}d\omega$$
> Exists if $x$ is absolutely or square summable. Period $2\pi$ in $\omega$.
>
> (source: ece301final_equation-sheet.pdf, p. 2; Topic DSP.3.C, p. 2)

## Properties (Table 5.1)
- Time shift: $x[n-n_0]\leftrightarrow e^{-j\omega n_0}X(e^{j\omega})$.
- Convolution: $x*y\leftrightarrow X\,Y$. Multiplication: $xy\leftrightarrow\frac1{2\pi}\int_{2\pi}X(e^{j\theta})Y(e^{j(\omega-\theta)})d\theta$.
- Upsampling by $L$: $X(e^{j\omega L})$, a squished spectrum with $L$ replicas (Topic DSP.4.B, p. 2).
- Real $x[n]$: $X(e^{j\omega})=X^*(e^{-j\omega})$.
- Parseval: $\sum|x[n]|^2=\frac1{2\pi}\int_{2\pi}|X(e^{j\omega})|^2d\omega$.

(source: ece301final_equation-sheet.pdf, p. 7)

Pairs (Table 5.2, p. 8): $\delta[n]\leftrightarrow1$; $a^nu[n]\leftrightarrow\frac1{1-ae^{-j\omega}}$ for $|a|<1$; $u[n]\leftrightarrow\frac1{1-e^{-j\omega}}+\pi\sum_k\delta(\omega-2\pi k)$; a DT rectangle of half-width $N_1$ gives $\frac{\sin[\omega(N_1+\frac12)]}{\sin(\omega/2)}$; ideal low-pass of cutoff $W$ in one period gives a sampled sinc in time.

## Relations
- $H(e^{j\omega})=H(z)|_{z=e^{j\omega}}$ when the unit circle is in the ROC (Topic DSP.6, p. 2). For an [[LTI system]], $H(e^{j\omega})$ is the frequency response, see [[Digital filter]].
- DFT = DTFT of the truncated signal, sampled at $\omega_k=2\pi k/N$ (Topic DSP.3.C, p. 3).
- The sampled-CT link is $\Omega=\omega T$: $X_d(e^{j\Omega})=X_p(j\Omega/T)$ (Topic DSP.4.A, pp. 21-22), see [[Sampling theorem]].
- 2D version, the DSFT $F(\mu,\nu)$, is used in [[Spatial filtering]].

> [!example] Exam 1 review: eigenfunction through a DTFT response
> With $H(e^{j\omega})=1/(1-\frac12e^{-j\omega})$, the input $1+e^{j\pi n/2}$ gives $2+H(e^{j\pi/2})e^{j\pi n/2}$. See [[LTI system]]. (source: exam_1_review_transcribed.pdf, pp. 8-9)

**Sources**: `Digital Signal Processing/Topic DSP.3.C more on DFT Feb 2, 2025.pdf`, `Digital Signal Processing/Topic DSP.4.B Sampling DT.pdf`, `Digital Signal Processing/Topic DSP.6 z-transforms March 7, 2025.pdf`, `Digital Signal Processing/301 Review/ece301final_equation-sheet.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[ECE438 DSP.3.C - More on DFT]] · [[ECE438 DSP.4.B - Sampling DT]] · [[ECE438 DSP.6 - z-transforms]]
- [[Fourier transform]] · [[DFT]] · [[FFT]] · [[Z-transform]] · [[Spectral leakage]] · [[Convolution]] · [[Digital filter]]
