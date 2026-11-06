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
- Images apply the same theory in 2D: [[ECE438 IP.2 - Sampling, quantization, interpolation]], [[ECE438 IP.3 - Continuous-space FT]].

Wiki note: the sampled signal is still continuous in amplitude; the amplitude side is [[Quantization]].

**Sources**: `Digital Signal Processing/Topic DSP.4.A Sampling CT.pdf`, `Digital Signal Processing/Topic DSP.4.B Sampling DT.pdf`, `Digital Signal Processing/Topic IP.3 Continuous-space FT Mar 25, 2025.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[ECE438 DSP.4.A - Sampling CT]] · [[ECE438 DSP.4.B - Sampling DT]] · [[ECE438 L15 - Sampling a CT signal]] · [[ECE438 L17 - Anti-aliasing prefilter and non-ideal interpolation]]
- [[Aliasing]] · [[Fourier transform]] · [[DTFT]] · [[Digital filter]] · [[Quantization]] · [[Discrete-time signal]]
