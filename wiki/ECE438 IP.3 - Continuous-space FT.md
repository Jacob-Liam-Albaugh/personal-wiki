---
type: lecture
area: dsp
source-ref: "Topic IP.3, pp. 1-19"
course: ece438
lecture: IP.3
tags: [signals]
---

# ECE438 IP.3 - Continuous-space FT

**Summary**: Fourier analysis of images: the 2D continuous-space Fourier transform (CSFT), useful transform pairs, 2D sinusoids and their frequency-domain deltas, properties (separability, radial symmetry, scaling, rotation), and a return to sampling and aliasing with the impulse train ("bed of nails"). Reading: Gonzalez and Woods, section 4.5.

**File**: `Digital Signal Processing/Topic IP.3 Continuous-space FT Mar 25, 2025.pdf`

---

## Topics
- CSFT basics, useful special signals, CSFT properties, separable and radially symmetric functions.
- Sampling and aliasing; additional aliasing notes are in a supplemental file ([[ECE438 IP.2 - Aliasing]]).

## Key results
> [!definition] 2D CSFT (p. 1)
> $$F(u,v)=\iint f(x,y)\,e^{-j2\pi ux}\,e^{-j2\pi vy}\,dx\,dy$$
> $$f(x,y)=\iint F(u,v)\,e^{j2\pi ux}\,e^{j2\pi vy}\,du\,dv$$
> $u,v$ are spatial frequencies: if $x,y$ are in cm, $u,v$ are in cycles/cm. In 1D the course used $\omega$ in radians/second. One can integrate over $x$ then $y$ or vice versa. Both $(x,y)$ and $(u,v)$ are continuous.

> [!assumption] Reading the axes (p. 3)
> Oscillations in $x$ (or $y$) are quantified by frequency $u$ (or $v$). If $x$ runs down and $y$ across the displayed image, oscillations in $x$ appear as horizontal stripes and $u$ is a vertical frequency; with $x$ across, they are vertical stripes and $u$ is horizontal frequency. Think critically about the axes before interpreting values.

> [!theorem] Transform pairs (p. 3)
> $$\mathrm{rect}(x,y)\ \overset{\rm CSFT}{\longleftrightarrow}\ \mathrm{sinc}(u,v)$$
> $$\mathrm{sinc}(u,v)=\frac{\sin\pi u}{\pi u}\cdot\frac{\sin\pi v}{\pi v}$$
> $\mathrm{rect}=1$ for $|x|<\tfrac12,\ |y|<\tfrac12$, else 0.
> $$\mathrm{circ}(x,y)\ \longleftrightarrow\ \mathrm{jinc}(u,v)$$
> $$\mathrm{jinc}=\frac{J_1\big(\pi\sqrt{u^2+v^2}\big)}{2\sqrt{u^2+v^2}}$$
> $\mathrm{circ}=1$ for $\sqrt{x^2+y^2}<\tfrac12$. $J_1$ is a Bessel function of the first kind, order 1. The signal and its transform are radially symmetric: a circular hat with sinc-like ripples that attenuate as $x^2+y^2$ grows (the "pillbox"). Fig. 4.42 shows the ideal LPF kernel as a spatial image (p. 5).

> [!definition] 2D delta (p. 5)
> $$\delta(x,y)=\lim_{\Delta\to0}\frac1{\Delta^2}\,\mathrm{rect}\!\left(\frac x\Delta,\frac y\Delta\right)$$
> Same principle as 1D (fixed area 1). Sifting property: $\iint f(x,y)\,\delta(x-x_0,y-y_0)\,dx\,dy=f(x_0,y_0)$. An impulse line $\delta(x)$ along the whole $y$ axis has $\delta(x)\longleftrightarrow\delta(v)$: no variation across $y$; write $\delta(x)=f_1(x)f_2(y)$ with $f_1=\delta(x)$, $f_2=1$, so $F_1=1$, $F_2=\delta(v)$.

> [!definition] 2D sinusoid (p. 7)
> $$f(x,y)=A\cos\big(2\pi(u_0x+v_0y)+\theta\big)$$
> Constant along $u_0x+v_0y=C$. Its transform is a pair of deltas at $\pm(u_0,v_0)$.
> $$\rho_0=\sqrt{u_0^2+v_0^2}=\frac1{P_0}$$
> $$\phi_0=\arctan\frac{v_0}{u_0}$$
> $P_0$ is the period; the first intercepts on the axes are at $1/u_0$ and $1/v_0$. So $|(u,v)|$ gives frequency, the angle of $(u,v)$ gives orientation, and $f$ is constant perpendicular to that direction. The longer the period (slower the frequency), the closer the deltas to the origin. The sheet has fill-in exercises identifying $u_0,v_0$ from stripe images.

> [!theorem] Properties (p. 13)
> Many are the same as 1D: linearity, [[Convolution]] ($f_1 * f_2\leftrightarrow F_1F_2$, 2D convolution to be covered), scaling and shifting:
> $$f\!\left(\frac{x-x_0}{a},\frac{y-y_0}{b}\right)\longleftrightarrow |ab|\,F(au,bv)\,e^{-j2\pi(ux_0+vy_0)}$$
> New:
> - Separable: $f(x,y)=g(x)h(y)$ implies $F(u,v)=G(u)H(v)$. Important separable functions: $\mathrm{rect}$, $\mathrm{sinc}$, $\delta$ (products of 1D versions).
> - Radially symmetric: $f(x,y)=g(r)$ with $r=\sqrt{x^2+y^2}$, $\theta=\arctan(y/x)$. If a function is radially symmetric, so is its CSFT.
> - Rotation: $f(A[x,y]^T)\longleftrightarrow |A|^{-1}F([u,v]A^{-1})$.

> [!theorem] Sampling in 2D (p. 15)
> Bed of nails $f(x,y)=\sum_m\sum_n\delta(x-m\Delta,\,y-n\Delta)$ is the product of two separable impulse trains with spacing $\Delta$. Its CSFT is also a bed of nails:
> $$F(u,v)=\frac1{\Delta^2}\sum\sum\delta\!\left(u-\frac m\Delta,\ v-\frac n\Delta\right)$$
> Multiplying $g(x,y)$ by the train creates spectral replicas just like 1D. If the spectrum of $g$ is not band limited, this creates aliasing. Shannon-Nyquist: a band-limited signal sampled faster than twice its highest frequency can be recovered exactly; undersampled gives aliasing.

## Examples
- Fig. 4.23 (p. 9): a vertical rectangle image; its spectrum has zero crossings closer in the vertical direction because the rectangle is longer there. As the line gets longer in space, the centre sinc lobe gets longer. Origin at the upper left in the book's convention; centred spectrum and log transform shown.
- Fig. 4.24 (p. 9): a translated rectangle has the same spectrum magnitude as the original; a rotated rectangle has a rotated spectrum.
- Fig. 4.37 (p. 11): building image with strong edges; the margin note says it looks downsampled by 2 and aliased, with a replica visible in the spectrum **[unverified]**.
- Fig. 4.28 (p. 11): SEM image of an integrated circuit and its spectrum with strong edge streaks.
- Fig. 4.20 (p. 17): moire effect, superimposing patterns is analogous to multiplying them.
- Fig. 4.19 (p. 19): 772x548 image resized to 33% by pixel deletion and replication shows aliasing; blurring with an averaging filter first gives slightly blurrier but acceptable result.

## Connections
- 1D versions: [[Fourier transform]], [[Sampling theorem]], [[Aliasing]].
- The discrete counterpart is [[DFT]] in 2D, used in later IP lectures.
- Wiki note: the sheet writes the replicas' prefactor as $1/T$ in the handwriting; for spacing $\Delta$ in both axes it should be $1/\Delta^2$ (above) **[unverified]**.

**Sources**: `Digital Signal Processing/Topic IP.3 Continuous-space FT Mar 25, 2025.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Fourier transform]] · [[Sampling theorem]] · [[Aliasing]] · [[Convolution]] · [[DFT]] · [[ECE438 IP.2 - Aliasing]] · [[ECE438 IP.2 - Sampling, quantization, interpolation]]
