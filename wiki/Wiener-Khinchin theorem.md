---
type: theorem
area: ift
areas: [ift, stochastic, math]
source-ref: "Enßlin IT & IFT, §8.2-8.3, pp. 98-101 (PDF pages)"
tags: [ift, signals, gp]
---

# Wiener-Khinchin theorem

**Summary**: for a statistically homogeneous (stationary) field, the covariance is diagonal in Fourier space, and its diagonal is the Fourier transform of the correlation function, which is the power spectrum.

Page numbers are PDF pages of the lecture notes (printed page = PDF page minus 6). The book spells the name "Wiener-Khintchin".

---

> [!theorem] Wiener-Khinchin (source: Ensslin - Information Theory & Information Field Theory.pdf, §8.3.2, p. 100)
> A statistically homogeneous signal $s$ over Cartesian space, with $S^x{}_y=\langle s^xs^{\dagger}{}_y\rangle=C_s(x-y)$, has a diagonal Fourier-space covariance
> $$S^k{}_{k'}=\langle s^ks^\dagger{}_{k'}\rangle=(2\pi)^u\delta(k-k')\,P_s(k),\qquad P_s(k)=\int d^ur\,e^{ikr}C_s(r).$$
> The diagonal is the power spectrum per volume,
> $$P_s(k)=\lim_{V\to\infty}\tfrac1V\Big\langle\Big|\int_Vdx\,s^xe^{ikx}\Big|^2\Big\rangle.$$

> [!proof] Sketch (source: §8.3, p. 99)
> Write $S^k{}_{k'}=\int dx\int dy\,e^{ikx}C_s(x-y)e^{-ik'y}$, substitute $y=x-r$, and use $\int dx\,e^{i(k-k')x}=(2\pi)^u\delta(k-k')$. What remains is $\int dr\,e^{ik'r}C_s(r)=P_s(k')$.

**Intuition**: translation invariance means no mode can be correlated with a different mode, so each Fourier mode is an independent Gaussian whose variance is the power in that mode. The "power spectrum" is the variance per mode.

## Consequences
- **Inverse and functions of covariance are trivial**: $(S^{-1})^k{}_q=(2\pi)^u\delta(k-q)/P_s(k)$, so $S^{-1}$ is the inverse power spectrum (§8.3.3, p. 100). This is what makes the [[Wiener filter]] a per-mode multiplication.
- **Maximum at zero lag**: $C_s(r)\le C_s(0)$ because $P_s\ge0$ and $|e^{-ikr}|\le1$ (p. 100).
- **Units**: $[P_s]=V[s_x]^2$ with $V$ the volume, so $P_s=\langle|s^k|^2\rangle/V$ (§8.3.1, p. 99).
- **White noise** $C_n(x-y)=\sigma_n^2\delta(x-y)$ has constant spectrum $P_n=\sigma_n^2$ (§8.3.5, p. 103).
- **Convolution** responses are diagonal too: $R^k{}_{k'}=(2\pi)^u\delta(k-k')b(k)$ (§8.3.6, p. 105).
- **Linear SDEs**: a stationary solution of a linear SDE has spectrum $P_s=P_R\,P_\xi$ with $P_R=|{\sum_na_n(-i\omega)^n}|^{-2}$; see [[Stochastic differential equation]] and [[Ornstein-Uhlenbeck process]].

**Notation**: the book uses $f(k)=\int d^ux\,e^{ikx}f(x)$ with $k$ the angular wave number (it first defines the symmetric $2\pi k$ convention and then absorbs the $2\pi$; the printed text there has a typo, "$k=2\pi/k$") (§8.2, pp. 97-98). See [[Fourier transform]] for conventions.

**Wiki note**: the classical statement (the power spectrum of a stationary process is the Fourier transform of its autocovariance) is the same result. For a deterministic or ergodic signal the time-average version needs extra assumptions **[unverified]**.

**Covered in**: Enßlin IT & IFT ch. 8 (pp. 97-111)
**Sources**: `text_books/Machine Learning & Statistics/Ensslin - Information Theory & Information Field Theory.pdf`.
**Last updated**: 2026-11-21

---

## Related pages
- [[Wiener filter]] · [[Fourier transform]] · [[Gaussian process]] · [[Convolution]] · [[Spectral leakage]]
- [[Stochastic differential equation]] · [[Ornstein-Uhlenbeck process]] · [[Information field theory]]
