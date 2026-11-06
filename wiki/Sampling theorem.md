---
type: theorem
area: dsp
source-ref: "ECE 438 Topic DSP.4.A, DSP.4.B, IP.2, IP.3"
tags: [signals]
---

# Sampling theorem

**Summary**: A bandlimited signal is determined by its samples if the sampling rate exceeds twice its highest frequency. Sampling replicates the spectrum; an ideal low-pass filter on the replicas reconstructs the signal; too low a rate overlaps the replicas, which is [[Aliasing]].

> [!theorem] Nyquist-Shannon
> If $X(j\omega)=0$ for $|\omega|>\omega_m$, then $x(t)$ is uniquely determined by $x(nT)$ provided
> $$\omega_s=\frac{2\pi}{T}>2\omega_m$$
> $2\omega_m$ is the Nyquist rate.
>
> (source: Topic DSP.4.A, p. 10)

## Mechanism
Model sampling as impulse-train multiplication $x_p(t)=x(t)\sum_k\delta(t-kT)$. Then
$$X_p(j\omega)=\frac1T\sum_kX\big(j(\omega-k\omega_s)\big)$$
Copies of $X$ at multiples of $\omega_s$ (pp. 9-10), see [[Fourier transform]].

> [!algorithm] Reconstruction
> Ideal low-pass with gain $T$ and cutoff $\omega_s/2$: $y_c(t)=x_p(t)*\frac{\sin(\omega_st/2)}{\pi t}$. The sinc is zero at the other sample times, so it interpolates exactly. It is not causal. (p. 11)

Non-ideal interpolators: zero-order hold (pulse, sinc spectrum lets replicas through) and linear interpolation (triangle, product of two sincs, better) (pp. 15-16). If the rate cannot be raised, prefilter with a low-pass of cutoff below $\omega_s/2$ (p. 17).

## DT counterparts
- CT to DT is a rescaling $\Omega=\omega T$ (DSP.4.A, pp. 21-22).
- Upsample by $L$: $X(e^{j\omega L})$, remove replicas with a gain-$L$ low-pass of cutoff $\pi/L$.
- Downsample by $D$: stretch by $D$, add $D$ replicas; prefilter with cutoff $\pi/D$ first (DSP.4.B, pp. 1-8).
- Rational rate change $L/D$: one filter with cutoff $\min(\pi/D,\pi/L)$ and gain $L$.
- Images apply the same theory in 2D: [[Image interpolation]], [[Digital image]], [[Fourier transform]].

Wiki note: the sampled signal is still continuous in amplitude; the amplitude side is [[Quantization]].

## System view and ITS spectrum
The chain is sample, $x_c(t)\to x_d[n]$, then a DT system $H_d(e^{j\Omega})$ (implemented with the [[FFT]] or in the time domain), then reconstruct $y_d[n]\to y_c(t)$. Analysis method: break the system apart, assume the pieces not under study are identity, then recombine. The question is what is needed for $y_c=x_c$, taking $H_d=1$ first (source: Topic DSP.4.A, pp. 1-3).

Sampling is $x[n]=x(nT)$, where $nT$ need not be an integer (e.g. $T=0.001$ s), with $\omega_s=2\pi/T$; it represents $x(t)$ by $\{x[n]\}$ and the value $T$. Reconstruction places the samples at $nT$ and connects the dots, e.g. by sample-and-hold or linear interpolation, both reasonable for small $T$ (pp. 5-7).

Impulse-train sampling (ITS) is the model $x_p(t)=x(t)p(t)$ with $p(t)=\sum_k\delta(t-kT)$, so $x_p(t)=\sum_kx(kT)\delta(t-kT)$. Technically it never creates $\{x[n]\}$ but makes the Fourier-domain effect clear; both $x$ and $x_p$ are CT signals (pp. 7-9). The Fourier transform of an impulse train in time is an impulse train in frequency, and with $x_1x_2\leftrightarrow\frac1{2\pi}X_1*X_2$:
$$P(j\omega)=\frac{2\pi}{T}\sum_k\delta(\omega-k\omega_s)$$
Each convolution with a shifted impulse shifts $X(j\omega)$, and $1/T$ is a scaling factor (pp. 9-10). The replicas do not overlap when $\omega_m<\omega_s-\omega_m$. The ideal reconstruction filter is an ideal low-pass filter, which is not realizable (not causal, infinite support in time); $h_{ideal}(nT)=0$ for $n\ne0$, so the sinc copies interpolate through the samples (L17 Feb 24, 2025.pdf, p. 1).

## CT frequency versus DT frequency
With $x_d[n]=x_c(nT)$ (A/D, and D/A for the reverse), applying the CTFT to $x_p$ gives $X_p(j\omega)=\sum_nx_c(nT)e^{-j\omega nT}$. Defining $\Omega=\omega T$ (radians/sample versus radians/second) this is the [[DTFT]] of $x_d$:
$$X_p(j\omega)=X_d(e^{j\omega T}),\qquad X_d(e^{j\Omega})=X_p\!\left(j\frac\Omega T\right)$$
DT is periodic in $\Omega$ with period $2\pi$; sampled CT is periodic in $\omega$ with period $2\pi/T=\omega_s$ (source: Topic DSP.4.A, pp. 21-22; L18 Feb 26, 2025.pdf, p. 1). Interpolation can be modelled as applying a non-ideal low-pass filter to the samples, and an ideal prefilter has cutoff $\omega_s/2$ (L18).

## Changing the rate of a DT signal
> [!definition] Upsampling by $L$
> Insert $L-1$ zeros between samples: $x_u[Ln]=x[n]$ and $x_u[Ln+1]=\dots=x_u[Ln+L-1]=0$. Then
> $$X_u(e^{j\omega})=\sum_nx[n]e^{-j\omega Ln}=X(e^{j\omega L})$$
> This squishes the spectrum. $X$ has period $2\pi$, so $X_u$ has period $2\pi/L$: $L$-fold replication. For $L=2$ the desired copy sits at the centre and replicas land at $\pm\pi$.
>
> (source: Topic DSP.4.B, pp. 1-2)

> [!definition] Interpolation filter
> The ideal digital low-pass removes the replicas:
> $$H(e^{j\omega})=\begin{cases}L&|\omega|<\pi/L\\0&\text{else}\end{cases}$$
> $$h[n]=\frac{\sin(\pi n/L)}{\pi n/L}=\mathrm{sinc}(n/L)$$
> with $h[0]=1$ and $h[n]=0$ at nonzero multiples of $L$. The output
> $$x_{int}[n]=x_u[n]*h[n]=\sum_mx_u[mL]\,\mathrm{sinc}\!\left(\frac{n-mL}L\right)$$
> only needs the nonzero samples, and closely resembles the CT reconstruction formula.
>
> (source: Topic DSP.4.B, pp. 2-4)

It is easier to design a good (not ideal) digital low-pass than an analog one, so one can interpolate by 3 in DT and then use a cheaper, less ideal CT reconstruction filter (p. 1).

> [!definition] Decimation by $D$
> Decimation is used under processing or memory constraints. Dropping to $y[m]=x[mD]$ with no prefilter could alias, so prefilter with $H_D(e^{j\omega})=1$ for $|\omega|\le\pi/D$ (period $2\pi$), $x_d[n]=h_D[n]*x[n]$, then $y[n]=x_d[nD]$. Downsampling is a time-varying system, unlike the filter.
>
> (source: Topic DSP.4.B, p. 4)

> [!theorem] Downsampling in frequency
> Sampling every $T$ then keeping every $D$th is as if sampled at $T'=DT$. Splitting the replica index $k=\ell D+i$ gives
> $$Y(e^{j\omega})=\frac1D\sum_{i=0}^{D-1}X_d\!\left(e^{j(\omega/D-2\pi i/D)}\right)$$
> The spectrum is stretched by $D$ and $D$ replicas are added. For $D=2$ the stretched copy and a shifted replica overlap (alias) unless prefiltered.
>
> (source: Topic DSP.4.B, pp. 5-6)

> [!theorem] Summary, assuming adequate prefiltering
> - Sample in CT: flattens the main frequency component and creates replicates.
> - Downsample in DT: stretches the main component and creates replicates; aliasing can occur without proper prefiltering.
> - Upsample in DT: squishes the main component and creates replicates.
> - Interpolation (DT and CT): apply a low-pass filter to remove replicates, then rescale.
>
> (source: Topic DSP.4.B, p. 7)

Rational resampling by $L/D$ chains upsample by $L$, filter, filter, downsample by $D$; the two filters merge into one with gain $L$ and cutoff $\min(\pi/D,\pi/L)$. Uses: frame-rate or pixel-rate conversion, e.g. European video (625 lines, 25 fps) versus USA video (525 lines, 30 fps), and clock skew, though it is inefficient for large factors such as $L=1000$, $D=100$ (source: Topic DSP.4.B, p. 8).

**Covered in**: ECE 438 DSP.4.A, DSP.4.B, L15-L18 (Topic DSP.4.A Sampling CT; Topic DSP.4.B Sampling DT; L15 Feb 19, L16 Feb 21, L17 Feb 24, L18 Feb 26, 2025 front pages)
**Sources**: `courses/ECE 438/Topic DSP.4.A Sampling CT.pdf`, `courses/ECE 438/Topic DSP.4.B Sampling DT.pdf`, `courses/ECE 438/Topic IP.3 Continuous-space FT Mar 25, 2025.pdf`, `courses/ECE 438/front page/L15 Feb 19, 2025.pdf`, `courses/ECE 438/front page/L16 Feb 21, 2025.pdf`, `courses/ECE 438/front page/L17 Feb 24, 2025.pdf`, `courses/ECE 438/front page/L18 Feb 26, 2025.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Aliasing]] · [[Fourier transform]] · [[DTFT]] · [[Digital filter]] · [[Quantization]] · [[Discrete-time signal]] · [[Digital image]] · [[Image interpolation]]
