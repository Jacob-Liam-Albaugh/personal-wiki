---
type: lecture
area: dsp
source-ref: "Topic DSP.4.A, pp. 1-22"
course: ece438
lecture: DSP.4.A
tags: [signals]
---

# ECE438 DSP.4.A - Sampling CT

**Summary**: Sampling a continuous-time signal, analysed with impulse-train sampling. Replicas of the spectrum appear every $\omega_s$, giving the [[Sampling theorem]] ($\omega_s>2\omega_m$), ideal reconstruction, [[Aliasing]], and the link between DT and CT frequency.

**File**: `Digital Signal Processing/Topic DSP.4.A Sampling CT.pdf`

---

## Topics
- **Big picture (pp. 1-4)**: the chain is sample, $x_c(t)\to x_d[n]$, then a DT system $H_d(e^{j\Omega})$ (implemented with the [[FFT]] or in the time domain), then $y_d[n]\to y_c(t)$ via reconstruction. Analysis method: break the system apart, assume the pieces not under study are identity, then recombine. Question: what is needed for $y_c(t)=x_c(t)$? Take $H_d=1$ first (source: pp. 1-3).
- **Sampling (p. 5)**: $x[n]=x(nT)$, where $nT$ need not be an integer (e.g. $T=0.001$ s). Sampling frequency $\omega_s=2\pi/T$. Sampling represents $x(t)$ by $\{x[n]\}$ and the value $T$.
- **Reconstruction (p. 6-7)**: place the samples $x[n]$ at $x(nT)$, then "connect the dots", e.g. linear interpolation or sample-and-hold (zeroth-order hold). Both are reasonable if $T$ is small.
- **Can $y=x$ exactly? (p. 7)** Yes, if $x(t)$ is bandlimited: there is a sampling rate and a reconstruction method that recover it exactly.
- **Impulse train sampling, ITS (pp. 7-9)**: model $x_p(t)=x(t)p(t)$ with $p(t)=\sum_k\delta(t-kT)$.
$$x_p(t)=\sum_{k=-\infty}^{\infty}x(kT)\,\delta(t-kT)$$
Technically it never creates $\{x[n]\}$, but it makes the Fourier-domain effect of sampling clear. Both $x$ and $x_p$ are continuous-time signals.

## Key results
> [!theorem] ITS in frequency (pp. 9-10)
> The [[Fourier transform]] of an impulse train in time (spacing $T$) is an impulse train in frequency (spacing $2\pi/T$). With the multiplication property $x_1x_2\leftrightarrow\frac1{2\pi}X_1*X_2$:
> $$P(j\omega)=\frac{2\pi}{T}\sum_k\delta\!\left(\omega-k\omega_s\right)$$
> $$X_p(j\omega)=\frac1T\sum_{k=-\infty}^{\infty}X\big(j(\omega-k\omega_s)\big)$$
> Each convolution with a shifted impulse shifts $X(j\omega)$. $1/T$ is a scaling factor.

> [!theorem] Sampling theorem (p. 10)
> If $x(t)$ is bandlimited, $X(j\omega)=0$ for $|\omega|>\omega_m$, then $x(t)$ is uniquely determined by its samples $x(nT)$, $n=0,\pm1,\dots$, provided
> $$\omega_s>2\omega_m,\qquad \omega_s=\frac{2\pi}{T}$$
> The Nyquist rate is $2\omega_m$. The replicas do not overlap when $\omega_m<\omega_s-\omega_m$.

> [!algorithm] Ideal reconstruction (p. 11)
> Pass $x_p(t)$ through an ideal low-pass filter (gain $1$ for $|\omega|<\omega_s/2$) and scale by $T$:
> $$y_c(t)=T\,x_p(t)*h_{ideal}(t)$$
> $$h_{ideal}(t)=\frac{\sin(\omega_st/2)}{\pi t}$$
> The ideal filter is not causal. $h_{ideal}(nT)=0$ for $n\ne0$, so the sinc copies interpolate through the samples: perfect reconstruction.

> [!theorem] Aliasing (pp. 12-13)
> If $\omega_s<2\omega_m$ the replicas overlap and add. High-frequency components "masquerade" as low frequencies, so they are aliased. This also happens when the signal is not bandlimited. Once introduced, aliasing cannot be perfectly removed (p. 14).
> Example $x(t)=\cos\omega_0t$: if $\omega_s>2\omega_0$ the spectrum is fine. If $\omega_s<2\omega_0$ a replica falls at lower frequency $\omega_s-\omega_0$, and the signal looks like $\cos((\omega_s-\omega_0)t)$ (p. 13).
> Everyday cases: downsampling a digital image without filtering first, and car wheels turning backwards in commercials, because the time sampling rate (typically 30 samples/s) is too slow for the wheel's rotation (p. 14).

> [!definition] Non-ideal reconstruction filters (pp. 15-16)
> $\hat x(t)=x_p(t)*h(t)$, with the factor $T$ absorbed into $h$.
> - Sample-and-hold (zeroth-order hold): $h_{zero}(t)=1$ for $0\le t<T$, else $0$. A pulse in time is a sinc in frequency, so it lets through many high-frequency replicas.
> - Linear interpolation (first-order hold): $h_{lin}(t)=1-|t|/T$ for $|t|<T$. A triangle is the convolution of two square pulses, so its spectrum is a product of two sincs, better at removing high-frequency replicas than sample-and-hold.

> [!algorithm] Prefilter (p. 17)
> If you cannot sample fast enough, knowingly remove the high frequencies first rather than let them irrecoverably distort the low ones. If the fastest sampling rate is $\omega_s$, prefilter with a low-pass filter of cutoff $\omega_0<\omega_s/2$.

> [!theorem] DT frequency versus CT frequency (pp. 21-22)
> With $x_d[n]=x_c(nT)$ (A/D converter, and D/A converter for the reverse), applying the CTFT to $x_p(t)=\sum_nx_c(nT)\delta(t-nT)$ gives
> $$X_p(j\omega)=\sum_nx_c(nT)e^{-j\omega nT}$$
> Define $\Omega=\omega T$. Then this is the [[DTFT]] of $x_d[n]$:
> $$X_p(j\omega)=X_d\big(e^{j\omega T}\big)$$
> $$X_d(e^{j\Omega})=X_p\!\left(j\frac{\Omega}{T}\right)$$
> $\Omega$ has units radians/sample and $\omega$ radians/second. The CT-to-DT step is just a rescaling of the frequency axis, $\Omega=\omega T$.

## Connections
- Sampling a DT signal (up/down sampling) continues in [[ECE438 DSP.4.B - Sampling DT]]. Quantizing the samples is [[ECE438 DSP.5 - Quantization]].
- Image counterpart: [[ECE438 IP.2 - Sampling, quantization, interpolation]] and [[ECE438 IP.2 - Aliasing]].
- Reconstruction filters are [[Digital filter]] ideas in continuous time; the reconstruction kernels are [[Convolution]] with the sample impulses.

**Sources**: `Digital Signal Processing/Topic DSP.4.A Sampling CT.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Sampling theorem]] · [[Aliasing]] · [[Fourier transform]] · [[DTFT]] · [[Convolution]] · [[Digital filter]] · [[LTI system]] · [[Quantization]]
