---
type: lecture
area: dsp
source-ref: "Topic DSP.3.C more on DFT, pp. 1-10"
course: ece438
lecture: DSP.3.C
tags: [signals]
---

# ECE438 DSP.3.C - More on DFT

**Summary**: Spectral analysis with the [[DFT]]. Shows the DFT as samples of the [[DTFT]] of a truncated signal, and explains [[Spectral leakage]]: a sinusoid whose frequency is not a DFT bin spreads over every bin, because the DFT implicitly analyses a periodic extension and because truncation is multiplication by a rectangular window.

**File**: `Digital Signal Processing/Topic DSP.3.C more on DFT Feb 2, 2025.pdf`

---

## Topics
- **DTFT recap (p. 2)**: $X(e^{j\omega})=\sum_n x[n]e^{-j\omega n}$, inverse $\frac1{2\pi}\int_{-\pi}^{\pi}$; exists if absolutely or square summable; periodic in $\omega$ with period $2\pi$. Two differences from the DFT: infinite-duration $x[n]$ (infinite sum) and continuous frequency.
- **Making the DTFT computable (p. 3)**: (1) truncate: $\tilde x[n]=x[n]$ for $0\le n\le N-1$, else 0; (2) sample frequency at $\omega_k=2\pi k/N$. Then $\tilde X(k)=\sum_{n=0}^{N-1}\tilde x[n]e^{-j2\pi kn/N}$, the forward DFT of $\tilde x$.
- **Non-bin sinusoids (pp. 4-6)**: DFT of $x[n]=e^{j\omega_xn}$, $n=0..N-1$, with $\omega_x\ne 2\pi k/N$.
- **DFT vs DTFS (p. 6)**: the DTFS is only for $N$-periodic signals and its coefficients are $N$-periodic; the same holds for DFT coefficients. So the DFT implicitly assumes the input is $N$-periodic.
- **Windowing view (pp. 8-10)**: truncation is multiplication by the rectangular window $w[n]$, which becomes periodic convolution in frequency.

## Key results
> [!theorem] DFT of a sinusoid
> With $\omega_k=2\pi k/N$,
> $$X(k)=\sum_{n=0}^{N-1}e^{j(\omega_x-\omega_k)n}=\frac{1-e^{j(\omega_x-\omega_k)N}}{1-e^{j(\omega_x-\omega_k)}}$$
> Using $1-e^{j\theta}=e^{j\theta/2}(-2j)\sin(\theta/2)$ on top and bottom,
> $$X(k)=e^{j(\omega_x-\omega_k)(N-1)/2}\,\frac{\sin[(\omega_x-\omega_k)N/2]}{\sin[(\omega_x-\omega_k)/2]}$$
> If $\omega_x=\omega_k$ for some $k$: $X(k)=N$ there and $0$ elsewhere. Otherwise $X(k)\ne0$ for every $k$. The original signal can still be recovered by the inverse DFT; the issue is interpreting $X(k)$. (source: pp. 5-6)

> [!definition] Spectral leakage
> The spreading of a sinusoid's energy over all DFT bins when $\omega_x\ne2\pi k/N$. For $N=6$, $\omega_x=\pi/2$ the samples are $1,j,-1,-j,1,j$, whose periodic extension repeats $1,j$ at the seam: "a little hiccup in the smooth sinusoid" whose frequency content must show up in the spectrum. (source: pp. 7-8)

> [!theorem] Leakage via the multiplication property
> The DTFT of $x_1[n]x_2[n]$ is the periodic convolution $\frac1{2\pi}\int_{2\pi}X_1(e^{j\theta})X_2(e^{j(\omega-\theta)})d\theta$. Truncation gives $\tilde x=x\,w$ with $w[n]=1$ on $0\le n\le N-1$ and
> $$W(e^{j\omega})=e^{-j\omega(N-1)/2}\frac{\sin(\omega N/2)}{\sin(\omega/2)}$$
> For $x=e^{j\omega_xn}$, $X=\pi\delta(\omega-\omega_x)$ (period $2\pi$), so $\tilde X(e^{j\omega})=\tfrac12 W(e^{j(\omega-\omega_x)})$: a shifted copy of the window's DTFT, not a clean spike. (source: pp. 8-9)

Consequences (p. 10): other, nicer windows can be used but leakage always remains; sampling the DTFT more densely (larger $N$ by zero padding) does not remove it, since the leakage is in the DTFT itself. Leakage limits the ability to resolve two nearby frequencies, e.g. $\cos\omega_0n+\cos\omega_1n$.

## Connections
- Numerical illustration: [[ECE438 DSP.3.C - Spectral leakage Python examples]]. Fast evaluation: [[ECE438 DSP.3.E - FFT]]. Linear-algebra view: [[ECE438 DSP.3.A - DT frequency analysis 1]].

**Sources**: `Digital Signal Processing/Topic DSP.3.C more on DFT Feb 2, 2025.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[DFT]] · [[DTFT]] · [[Spectral leakage]] · [[FFT]] · [[Fourier transform]] · [[ECE438 DSP.3.D - Convolution with DFT]]
