---
type: concept
area: dsp
source-ref: "ECE 438 Topic DSP.3.C, pp. 4-10, and Python examples"
tags: [signals]
---

# Spectral leakage

**Summary**: A sinusoid whose frequency is not a [[DFT]] bin spreads its energy over every bin. Two equivalent explanations: the DFT implicitly analyses a periodic extension with a kink at the seam, and truncation multiplies by a rectangular window whose [[DTFT]] is a sinc-like kernel.

> [!theorem] DFT of an off-bin sinusoid
> For $x[n]=e^{j\omega_xn}$, $0\le n<N$, and $\omega_k=2\pi k/N$:
> $$X(k)=e^{j(\omega_x-\omega_k)(N-1)/2}\,\frac{\sin[(\omega_x-\omega_k)N/2]}{\sin[(\omega_x-\omega_k)/2]}$$
> If $\omega_x=\omega_k$ the result is $N$ at that bin and $0$ elsewhere; otherwise every bin is nonzero.
>
> (source: Topic DSP.3.C, pp. 5-6)

> [!theorem] Windowing view
> Truncation is $\tilde x=x\,w$, with rectangular $w$, so in frequency it is periodic convolution:
> $$\tilde X(e^{j\omega})=\tfrac12W(e^{j(\omega-\omega_x)})$$
> $$W(e^{j\omega})=e^{-j\omega(N-1)/2}\frac{\sin(\omega N/2)}{\sin(\omega/2)}$$
> (source: Topic DSP.3.C, pp. 8-9)

## Consequences
- Other windows change the shape of leakage but cannot remove it.
- Zero padding ($N=64\to128\to1024$ in the Python example, a period-14 sinusoid) samples the same DTFT more densely and reveals the sidelobes; it does not fix leakage.
- Leakage limits resolving two close frequencies.
- In the Python example the 64-sample record is not a whole number of periods of the period-14 signal, so the periodic extension has a seam.
- The signal itself is still recovered exactly by the inverse DFT; only the reading of $X(k)$ is affected.

(source: Topic DSP.3.C, p. 10; Python examples, pp. 1-2)

**Sources**: `Digital Signal Processing/Topic DSP.3.C more on DFT Feb 2, 2025.pdf`, `Digital Signal Processing/Topic DSP.3.C Python Examples Spectral Leakage Feb 6, 2025.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[ECE438 DSP.3.C - More on DFT]] · [[ECE438 DSP.3.C - Spectral leakage Python examples]]
- [[DFT]] · [[DTFT]] · [[FFT]] · [[Fourier transform]] · [[Convolution]] · [[Aliasing]]
