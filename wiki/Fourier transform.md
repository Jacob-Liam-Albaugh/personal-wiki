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
- Sampling: an impulse train in time is an impulse train in frequency, so sampling replicates the spectrum every $2\pi/T$. See [[Sampling theorem]] and [[Aliasing]].
- Images: the continuous-space FT and 2D aliasing are in the 2D section below; see also [[Digital image]].
- Wiki note: the continuous-time analogues of the [[Z-transform]] and its ROC is the [[Laplace transform]]. Time-frequency localisation, which the Fourier transform lacks, motivates the [[Wavelet transform]].

## Impulse-train spectrum
The impulse train $p(t)=\sum_k\delta(t-kT)$ has
$$P(j\omega)=\frac{2\pi}{T}\sum_k\delta\!\left(\omega-\frac{2\pi k}{T}\right)$$
Multiplication in time is convolution in frequency, so $x_p(t)=x_c(t)p(t)$ gives $X_p(j\omega)=\frac1{2\pi}X_c*P$: copies of $X_c$ every $2\pi/T$ (source: L16 Feb 21, 2025.pdf, p. 1).

## 2D continuous-space FT (CSFT)
> [!definition] 2D CSFT
> $$F(u,v)=\iint f(x,y)\,e^{-j2\pi ux}\,e^{-j2\pi vy}\,dx\,dy$$
> $$f(x,y)=\iint F(u,v)\,e^{j2\pi ux}\,e^{j2\pi vy}\,du\,dv$$
> $u,v$ are spatial frequencies: for $x,y$ in cm they are in cycles/cm (1D used $\omega$ in rad/s). One can integrate over $x$ then $y$ or the reverse.
>
> (source: Topic IP.3 Continuous-space FT Mar 25, 2025.pdf, p. 1; L27 Mar 31, 2025.pdf, p. 1)

> [!assumption] Reading the axes
> Oscillations in $x$ (or $y$) have frequency $u$ (or $v$). If $x$ runs down the displayed image, oscillations in $x$ are horizontal stripes and $u$ is a vertical frequency; with $x$ across, they are vertical stripes and $u$ is horizontal. Check the axes before interpreting values (source: IP.3, p. 3).

> [!theorem] Transform pairs
> $$\mathrm{rect}(x,y)\leftrightarrow\mathrm{sinc}(u,v)=\frac{\sin\pi u}{\pi u}\cdot\frac{\sin\pi v}{\pi v}$$
> with $\mathrm{rect}=1$ for $|x|,|y|<\tfrac12$.
> $$\mathrm{circ}(x,y)\leftrightarrow\mathrm{jinc}(u,v)=\frac{J_1\big(\pi\sqrt{u^2+v^2}\big)}{2\sqrt{u^2+v^2}}$$
> with $\mathrm{circ}=1$ for $\sqrt{x^2+y^2}<\tfrac12$ and $J_1$ the order-1 Bessel function. Both sides are radially symmetric: a circular hat with sinc-like ripples that decay with radius (the "pillbox"). Fig. 4.42 shows the ideal low-pass kernel as an image.
>
> (source: IP.3, pp. 3, 5)

> [!definition] 2D delta
> $$\delta(x,y)=\lim_{\Delta\to0}\frac1{\Delta^2}\,\mathrm{rect}\!\left(\frac x\Delta,\frac y\Delta\right)$$
> Sifting: $\iint f(x,y)\delta(x-x_0,y-y_0)\,dx\,dy=f(x_0,y_0)$. An impulse line $\delta(x)$ along the whole $y$ axis is $f_1(x)f_2(y)$ with $f_1=\delta(x)$, $f_2=1$, so $\delta(x)\leftrightarrow\delta(v)$: no variation across $y$.
>
> (source: IP.3, p. 5)

> [!definition] 2D sinusoid
> $$f(x,y)=A\cos\big(2\pi(u_0x+v_0y)+\theta\big)$$
> Constant along $u_0x+v_0y=C$; its transform is a pair of deltas at $\pm(u_0,v_0)$.
> $$\rho_0=\sqrt{u_0^2+v_0^2}=\frac1{P_0},\qquad \phi_0=\arctan\frac{v_0}{u_0}$$
> The distance of the deltas from the origin gives frequency (period $P_0$), their angle gives orientation, and $f$ is constant perpendicular to that direction. Slower sinusoids sit closer to the origin. The first axis intercepts of the stripes are $1/u_0$ and $1/v_0$.
>
> (source: IP.3, p. 7)

> [!theorem] 2D properties
> Linearity, convolution ($f_1*f_2\leftrightarrow F_1F_2$) as in 1D, and scaling and shifting:
> $$f\!\left(\tfrac{x-x_0}{a},\tfrac{y-y_0}{b}\right)\leftrightarrow|ab|\,F(au,bv)\,e^{-j2\pi(ux_0+vy_0)}$$
> - Separable: $f=g(x)h(y)$ gives $F=G(u)H(v)$ (rect, sinc, delta).
> - Radially symmetric: $f=g(r)$, $r=\sqrt{x^2+y^2}$, independent of $\theta=\arctan(y/x)$, gives a radially symmetric $F$.
> - Rotation: $f(A[x,y]^T)\leftrightarrow|A|^{-1}F([u,v]A^{-1})$.
>
> (source: IP.3, p. 13; L27, p. 1)

> [!theorem] Bed-of-nails sampling
> $f=\sum_m\sum_n\delta(x-m\Delta,y-n\Delta)$ is a product of two separable impulse trains, and its CSFT is also a bed of nails:
> $$F(u,v)=\frac1{\Delta^2}\sum\sum\delta\!\left(u-\tfrac m\Delta,\ v-\tfrac n\Delta\right)$$
> Multiplying an image $g$ by it replicates the spectrum as in 1D; a spectrum that is not band limited aliases. Shannon-Nyquist holds per axis.
>
> (source: IP.3, p. 15)

Wiki note: the IP.3 handwriting gives the replica prefactor as $1/T$; for spacing $\Delta$ on both axes it should be $1/\Delta^2$ **[unverified]**.

> [!example] Figures from Gonzalez and Woods ch. 4
> - Fig. 4.23: a vertical rectangle has spectrum zero crossings closer vertically; the longer the line in space, the longer the centre lobe. Origin at upper left, spectrum centred and log-scaled.
> - Fig. 4.24: a translated rectangle has the same spectrum magnitude; a rotated one has a rotated spectrum.
> - Fig. 4.37: building image with strong edges, apparently downsampled by 2 with a replica in the spectrum **[unverified]**.
> - Fig. 4.28: SEM image of an integrated circuit with edge streaks in the spectrum.
> - Fig. 4.20: moire, superimposed patterns multiply.
> - Fig. 4.19: a 772x548 image resized to 33% by pixel deletion aliases; averaging before decimating gives a slightly blurrier but acceptable result.
>
> (source: IP.3, pp. 9-19)

## Where it appears
- [[Wavelets vs Fourier (Strang 1993)]] and [[Wavelet transform]]: wavelets localise in both time and frequency, where Fourier is global; compare FFT with the fast wavelet transform.
- [[Maxwell's equations]]: phasor notation for sinusoidal fields (source: lect_28.pdf); [[Electromagnetic wave]].



**Covered in**: ECE 438 DSP.4.A, IP.3, L16, L26, L27 (Digital Signal Processing/Topic IP.3 Continuous-space FT Mar 25, 2025.pdf)
**Sources**: `Digital Signal Processing/301 Review/ece301final_equation-sheet.pdf`, `Digital Signal Processing/Topic DSP.4.A Sampling CT.pdf`, `Digital Signal Processing/Topic IP.3 Continuous-space FT Mar 25, 2025.pdf`, `Digital Signal Processing/front page/L16 Feb 21, 2025.pdf`, `Digital Signal Processing/front page/L26 Mar 26, 2025.pdf`, `Digital Signal Processing/front page/L27 Mar 31, 2025.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[DTFT]] · [[DFT]] · [[FFT]] · [[Z-transform]] · [[Laplace transform]] · [[Convolution]] · [[LTI system]] · [[Sampling theorem]] · [[Wavelet transform]] · [[Spectral bias]] · [[Aliasing]] · [[Digital image]]
