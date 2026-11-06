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

## Seam picture and Python example
> [!definition] Why leakage appears
> For $N=6$ and $\omega_x=\pi/2$ the samples are $1,j,-1,-j,1,j$, whose periodic extension repeats $1,j$ at the seam: a little hiccup in the smooth sinusoid, whose frequency content must show up in the spectrum. The DFT implicitly assumes an $N$-periodic input, so any record that is not a whole number of periods has such a seam.
>
> (source: Topic DSP.3.C, pp. 6-8)

The DTFT of a product is the periodic convolution $\frac1{2\pi}\int_{2\pi}X_1(e^{j\theta})X_2(e^{j(\omega-\theta)})d\theta$. For $x=e^{j\omega_xn}$ the spectrum is $X=\pi\delta(\omega-\omega_x)$ (period $2\pi$), which with the window gives $\tilde X=\tfrac12W(e^{j(\omega-\omega_x)})$ above: a shifted copy of the window's DTFT, not a clean spike (source: Topic DSP.3.C, pp. 8-9).

Python example (source: Topic DSP.3.C Python Examples Spectral Leakage Feb 6, 2025.pdf, pp. 1-2): the test signal has period 14 but is observed over 64 samples, not a whole number of periods.
- $N=64$: two broad peaks with skirts, which demonstrates leakage.
- $N=128$ (zero padding): more spectral samples, with ripples around the peaks.
- $N=1024$: more structure of the sampled DTFT appears, the sidelobes of the window's DTFT.
- A plot of the periodic extension repeats the 64-sample block and shows a kink at each seam.
Zero padding therefore reveals the leakage rather than fixing it; there are ways to accommodate it by choosing other windows.

**Covered in**: ECE 438 DSP.3.C (Topic DSP.3.C more on DFT; Topic DSP.3.C Python Examples Spectral Leakage)
**Sources**: `courses/ECE 438/Topic DSP.3.C more on DFT Feb 2, 2025.pdf`, `courses/ECE 438/Topic DSP.3.C Python Examples Spectral Leakage Feb 6, 2025.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[DFT]] · [[DTFT]] · [[FFT]] · [[Fourier transform]] · [[Convolution]] · [[Aliasing]]
