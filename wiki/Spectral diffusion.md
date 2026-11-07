---
type: method
area: ml
areas: [ml, physics-informed, pde]
source-ref: "Gallon 2026, Sec. 3.4, Lemma 3.2, App. A"
tags: [diffusion, generative, pde, operators]
---

# Spectral diffusion (scaled spectral latents)

Diffusion run on truncated spectral coefficients of a function instead of on grid values. If each coefficient is divided by its standard deviation over the data, the Gaussian noise of the forward process is a smooth random function rather than white noise. Differential operators then stay defined at every noise level.

> [!definition] Scaled spectral encoding (Gallon 2026, eqs. 6–8, p. 4)
> Fourier basis on $\mathbb T^d$:
> $$\phi_n(x)=e^{2\pi i\langle n,x\rangle}$$
> Per-mode data scale:
> $$s_n^2=\mathrm{Var}(\widehat{X_{data}}(n))$$
> For a truncation set $K$, $|K|=l$:
> $$E(f)(n)=\hat f(n)/s_n$$
> $$I(\alpha)=\sum_{n\in K}s_n\,\alpha(n)\,\phi_n$$

> [!theorem] Lemma 3.2 (Gallon 2026, p. 4; proof App. A, p. 11)
> If $\mathbb E\|X_{data}\|^2_{H^k}<\infty$ and $Z_n$ are i.i.d. $\mathcal N(0,1)$, then the latent noise mapped to function space,
> $$N=\sum_{n\in\mathbb Z^d}s_nZ_n\phi_n,$$
> satisfies $\mathbb E\|N\|^2_{H^k}<\infty$.
>
> Proof: $\|f\|^2_{H^k}\simeq\sum_n|\hat f(n)|^2\|n\|^{2k}$. Then
> $$\mathbb E\|N\|^2_{H^k}\simeq\sum_n s_n^2\|n\|^{2k}$$
> and, since $s_n^2=\mathrm{Var}\le\mathbb E|\hat X(n)|^2$, this is $\lesssim\mathbb E\|X_{data}\|^2_{H^k}$.

So the forward process stays in $H^k$, the regularity of the data. Grid diffusion tends to spatial white noise as resolution grows, and white noise is not differentiable (Fig. 2, p. 5).

## Choices
- **Basis**: sine series for zero Dirichlet BCs, which then hold by construction; complex Fourier series on periodic domains. Non-vanishing fields are first padded so they decay smoothly to zero (Gallon 2026, App. B.1).
- **Truncation**:
  - Cube: $\|n\|_\infty\le c$.
  - Hyperbolic: $|n_1\cdots n_d|\le c$. It keeps a low-frequency core plus axis strips of high modes, folded into a square array for the network. At equal size it beats the cube (Remark 3.3; Table 15).
- **Dimension**: 128² grid → 44² or 32² modes, the main source of the 3–15× speedup.
- **Derivatives**: exact in the basis, e.g. $\widehat{\Delta u}(k)=-\pi^2\|k\|^2\hat u(k)$.

## Related approaches (as cited by Gallon 2026, pp. 2–3; not read)
- Phillips et al. 2022: spectral diffusion without the data scaling.
- Kerrigan et al. 2023: discrete-time diffusion in function space with prescribed Sobolev regularity.
- FunDPS (Yao 2025): DPS in function space.
- Wavelet diffusion neural operator (Hu 2024): wavelet coefficients, aimed at sharp features.

Wiki note: dividing by $s_n$ is a diagonal whitening in the Fourier basis, so the latent prior is $\mathcal N(0,I)$ while the function-space prior is $\mathcal N(0,\mathrm{diag}(s_n^2))$, a stationary GP whose spectrum is fitted to the data. Compare the spectral GP priors in [[Information field theory]].

## Where it appears
- [[PISD (Gallon 2026)]]: physics-guided sampling for Poisson, Helmholtz and Navier–Stokes.

**Sources**: `papers/Operators/Gallon, Wurstemberger, Cheridito, Jentzen - Physics-Informed Diffusion Models in Spectral Space.pdf`.
**Last updated**: 2026-11-07

---

## Related pages
- [[Diffusion models]] · [[Diffusion posterior sampling]] · [[Fourier transform]] · [[FNO]] · [[Spectral bias]] · [[Information field theory]]
