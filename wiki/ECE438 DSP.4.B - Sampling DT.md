---
type: lecture
area: dsp
source-ref: "Topic DSP.4.B, pp. 1-8"
course: ece438
lecture: DSP.4.B
tags: [signals]
---

# ECE438 DSP.4.B - Sampling DT

**Summary**: Changing the sampling rate of a discrete-time signal. Upsampling by $L$ plus a low-pass filter (interpolation), prefilter plus downsampling by $D$ (decimation), their frequency-domain effects, and rational resampling by $L/D$.

**File**: `Digital Signal Processing/Topic DSP.4.B Sampling DT.pdf`

---

## Topics
- **Interpolation in DT (p. 1)**: increase the sampling rate by a factor $L$ in the digital domain. It is easier to design a good (not ideal) low-pass [[Digital filter]] digitally than in analog, so one can interpolate by 3 in DT and then use a cheaper, less ideal CT reconstruction filter. Interpolation is two steps: upsample, then low-pass filter ($H_{LPF}$ with gain $L$ and cutoff $\pi/L$).
- **Decimation (p. 4)**: used under processing or memory constraints. Assume $x[n]$ was sampled without aliasing. Dropping to $y[m]=x[mD]$ with no prefilter could introduce aliasing, so decimation is prefilter plus downsample by $D$, keeping every $D$th sample.

## Key results
> [!definition] Upsampling (p. 1)
> Insert $L-1$ zeros between samples:
> $$x_u[Ln]=x[n]$$
> $$x_u[Ln+1]=\dots=x_u[Ln+L-1]=0$$

> [!theorem] Upsampling in frequency (p. 2)
> By a change of variables that condenses the zeros:
> $$X_u(e^{j\omega})=\sum_nx[n]\,e^{-j(\omega L)n}$$
> $$X_u(e^{j\omega})=X(e^{j\omega L})$$
> This squishes the spectrum in frequency. $X$ has period $2\pi$, so $X_u$ has period $2\pi/L$: $L$-fold periodic replication. For $L=2$ the desired copy sits at the centre and replicas land at $\pm\pi$.

> [!definition] Interpolation filter (pp. 2-4)
> The ideal digital low-pass filter removes the replicas, and is periodic with period $2\pi$:
> $$H(e^{j\omega})=\begin{cases}L&|\omega|<\pi/L\\0&\text{else}\end{cases}$$
> Its impulse response is the inverse DTFT:
> $$h[n]=\frac{\sin(\pi n/L)}{\pi n/L}=\mathrm{sinc}(n/L)$$
> a sampled sinc, with $h[0]=1$ and $h[n]=0$ at nonzero multiples of $L$. The output is
> $$x_{int}[n]=x_u[n]*h[n]=\sum_mx_u[mL]\,\mathrm{sinc}\!\left(\frac{n-mL}{L}\right)$$
> Only the nonzero samples contribute. This is very like the CT reconstruction formula (see [[ECE438 DSP.4.A - Sampling CT]]).

> [!definition] Decimation (p. 4)
> Prefilter $H_D(e^{j\omega})=1$ for $|\omega|\le\pi/D$ (periodic with period $2\pi$), then
> $$x_d[n]=h_D[n]*x[n]$$
> $$y[n]=x_d[nD]$$
> Downsampling is a time-varying system, unlike the filter.

> [!theorem] Downsampling in frequency (pp. 5-6)
> Use $X_c(j\omega)$ as an intermediary and assume no prefilter is needed. Sampling every $T$, then keeping every $D$th, is as if sampled at $T'=DT$. Splitting the replica index $k=\ell D+i$ gives
> $$Y(e^{j\omega})=\frac1D\sum_{i=0}^{D-1}X_d\!\left(e^{j(\omega/D-2\pi i/D)}\right)$$
> The spectrum is stretched by $D$ and $D$ replicas are added. Example $D=2$: stretch plus a shifted replica; they overlap (alias) unless prefiltered.

> [!theorem] Summary (assuming adequate prefiltering, p. 7)
> - Sample in CT: flattens the main frequency component and creates replicates.
> - Downsample in DT: stretches the main component, creates replicates. Aliasing can occur without proper prefiltering.
> - Upsample in DT: squishes the main component, creates replicates.
> - Interpolation (DT and CT): apply a low-pass filter to remove replicates, then rescale.

> [!algorithm] Rational resampling by $L/D$ (p. 8)
> Chain: upsample by $L$, filter, filter, downsample by $D$. The two filters merge into one that removes the replicas from upsampling and prefilters to avoid aliasing:
> $$H(e^{j\omega})=\begin{cases}L&0\le|\omega|\le\min(\pi/D,\ \pi/L)\\0&\text{else}\end{cases}$$
> Use: frame-rate or pixel-rate conversion, e.g. European video, 625 lines at 25 fps, versus USA video, 525 lines at 30 fps. Also useful for clock skew, though inefficient for large factors such as $L=1000$, $D=100$.

## Connections
- Aliasing mechanism: [[Aliasing]]; theorem: [[Sampling theorem]]; the next lecture quantizes the samples: [[ECE438 DSP.5 - Quantization]].
- Images use the same operations in 2D: [[ECE438 IP.2 - Sampling, quantization, interpolation]].

**Sources**: `Digital Signal Processing/Topic DSP.4.B Sampling DT.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Sampling theorem]] · [[Aliasing]] · [[DTFT]] · [[Digital filter]] · [[Convolution]] · [[Discrete-time signal]]
