---
type: definition
area: dsp
source-ref: "ECE 301 equation sheet pp. 2-6; ECE 438 DSP.4.A, IP.3"
tags: [signals]
---

# Fourier transform

**Summary**: Decomposes a signal into complex sinusoids. The family has four main members: CT and DT Fourier series for periodic signals, and the CT Fourier transform and [[DTFT]] for aperiodic ones; the [[DFT]] is the finite computable version. Convolution becomes multiplication in every member, which is why the transform diagonalises an [[LTI system]].

## The four pairs
> [!definition] Fourier series and transforms (ECE 301 sheet)
> CT Fourier series, period $T$, $\omega_0=2\pi/T$:
> $$x(t)=\sum_{k}a_ke^{jk\omega_0t},\qquad a_k=\frac1T\int_{T}x(t)e^{-jk\omega_0t}dt$$
> DT Fourier series, period $N$:
> $$x[n]=\sum_{k=\langle N\rangle}a_ke^{jk(2\pi/N)n},\qquad a_k=\frac1N\sum_{n=\langle N\rangle}x[n]e^{-jk(2\pi/N)n}$$
> CT Fourier transform:
> $$X(j\omega)=\int_{-\infty}^{\infty}x(t)e^{-j\omega t}dt$$
> $$x(t)=\frac1{2\pi}\int_{-\infty}^{\infty}X(j\omega)e^{j\omega t}d\omega$$
> The DT counterpart is on [[DTFT]].
>
> (source: ece301final_equation-sheet.pdf, p. 2)

## Properties (CTFT, Table 4.1)
| Property | $x(t)$ | $X(j\omega)$ |
|---|---|---|
| Time shift | $x(t-t_0)$ | $e^{-j\omega t_0}X(j\omega)$ |
| Frequency shift | $e^{j\omega_0t}x(t)$ | $X(j(\omega-\omega_0))$ |
| Scaling | $x(at)$ | $\frac1{|a|}X(j\omega/a)$ |
| Convolution | $x*y$ | $X(j\omega)Y(j\omega)$ |
| Multiplication | $xy$ | $\frac1{2\pi}X*Y$ |
| Differentiation | $dx/dt$ | $j\omega X(j\omega)$ |
| Frequency derivative | $tx(t)$ | $j\,dX/d\omega$ |

Real $x(t)$ gives $X(j\omega)=X^*(-j\omega)$ (magnitude even, phase odd). Parseval:
$$\int|x(t)|^2dt=\frac1{2\pi}\int|X(j\omega)|^2d\omega$$
(source: ece301final_equation-sheet.pdf, p. 5)

Common pairs (Table 4.2, p. 6): $\delta(t)\leftrightarrow1$; $e^{-at}u(t)\leftrightarrow\frac1{a+j\omega}$; $\cos\omega_0t\leftrightarrow\pi[\delta(\omega-\omega_0)+\delta(\omega+\omega_0)]$; $1\leftrightarrow2\pi\delta(\omega)$; a rectangle of half-width $T_1$ gives $\frac{2\sin\omega T_1}{\omega}$; $\frac{\sin Wt}{\pi t}$ gives a rectangle of half-width $W$.

## Use in this course
- Sampling: an impulse train in time is an impulse train in frequency, so sampling replicates the spectrum every $2\pi/T$. See [[Sampling theorem]], [[Aliasing]] and [[ECE438 DSP.4.A - Sampling CT]].
- Images: the continuous-space FT and 2D aliasing are in [[ECE438 IP.3 - Continuous-space FT]].
- Wiki note: the continuous-time analogues of the [[Z-transform]] and its ROC is the [[Laplace transform]]. Time-frequency localisation, which the Fourier transform lacks, motivates the [[Wavelet transform]].

## Where it appears
- [[Wavelets vs Fourier (Strang 1993)]] and [[Wavelet transform]]: wavelets localise in both time and frequency, where Fourier is global; compare FFT with the fast wavelet transform.
- [[ECE311 lect_28 - Potentials and time-harmonic fields]]: phasor notation for sinusoidal fields (source: lect_28.pdf); [[Electromagnetic wave]].

**Sources**: `Digital Signal Processing/301 Review/ece301final_equation-sheet.pdf`, `Digital Signal Processing/Topic DSP.4.A Sampling CT.pdf`, `Digital Signal Processing/Topic IP.3 Continuous-space FT Mar 25, 2025.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[DTFT]] · [[DFT]] · [[FFT]] · [[Z-transform]] · [[Laplace transform]] · [[Convolution]] · [[LTI system]] · [[Sampling theorem]] · [[Wavelet transform]]
- [[ECE438 301R 2.3 - Period of a signal]] · [[ECE438 L16 - Impulse-train sampling in the frequency domain]]
- [[Spectral bias]] (Fourier decay of ReLU networks, Rahaman 2019 Thm 1).
