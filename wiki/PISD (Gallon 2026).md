---
type: paper
area: physics-informed
areas: [physics-informed, ml, pde, inverse-problems]
source-ref: "Gallon, von Wurstemberger, Cheridito, Jentzen 2026, ICML (PMLR 306)"
tags: [diffusion, generative, physics-informed, inverse-problems, pde, operators]
year: 2026
venue: "ICML 2026, PMLR 306"
file: "papers/Operators/Gallon, Wurstemberger, Cheridito, Jentzen - Physics-Informed Diffusion Models in Spectral Space.pdf"
---

# Physics-informed diffusion models in spectral space (Gallon 2026)

**Summary**: PISD (physics-informed spectral diffusion) trains a diffusion model on truncated Fourier or sine coefficients of (coefficient, solution) pairs, each coefficient divided by its standard deviation over the data. With this scaling, Gaussian noise in the latent space maps to a function with the same Sobolev regularity as the data, so the PDE residual is well defined at every noise level. At inference, observation and PDE-residual gradients are applied at every step, as in [[Diffusion posterior sampling]], but through a frequency-aware [[Adam]] update instead of plain gradient descent. On Poisson, Helmholtz and Navier–Stokes with sparse observations, it matches or beats DiffusionPDE and FunDPS on error, with PDE residuals 100–10 000× lower and 3–15× faster inference.

**Authors**: Davide Gallon, Philippe von Wurstemberger, Patrick Cheridito, Arnulf Jentzen (ETH Zurich, Münster, CUHK-Shenzhen) · **Year**: 2026 · **File**: `papers/Operators/Gallon, Wurstemberger, Cheridito, Jentzen - Physics-Informed Diffusion Models in Spectral Space.pdf` · **Code**: github.com/deeplearningmethods/PISD

---

## Problem

The goal is to sample $f\in\mathcal F$ (a Hilbert space) with $L_{PDE}(f)=0$, conditioned on measurements $M(f)=y$. The prior $\nu$ is assumed to be supported on PDE solutions, $\nu(\{L_{PDE}=0\})=1$, and is sampled with a classical solver (source: Sec. 3.1, p. 3).

One generative model covers three settings: forward (sparse $a$ → $u$), inverse (sparse $u$ → $a$), and joint reconstruction (sparse $a$ and $u$). With sparse data these are ill-posed; the learned prior makes the posterior well defined (p. 1).

> [!example] Poisson setting (Example 3.1, p. 3)
> $\Omega=(0,1)^2$, $\mathcal F=(H^2\cap H^1_0)\times L^2$:
> $$L_{PDE}(u,a)=\|\Delta u-a\|^2_{L^2}$$

## Method

### Spectral latent diffusion
The encoder is $E:\mathcal F\to\mathbb R^l$ with approximate inverse $I$, $I(E(f))\approx f$ (eq. 1). Following EDM (Karras 2022), the denoiser satisfies
$$D_{\theta^*}(\hat X+\sigma N,\sigma)\approx\hat X$$
with $\hat X=E(X_{data})$ (eq. 2). Sampling runs the probability-flow ODE (eq. 3):
$$d\hat x_t=-\dot\sigma_t\sigma_t^{-1}(D_{\theta^*}(\hat x_t,\sigma_t)-\hat x_t)\,dt$$

The encoding divides each Fourier coefficient by its data standard deviation $s_n$ (eqs. 7–8). Lemma 3.2 shows the scaled noise stays in $H^k$. Details are on [[Spectral diffusion]].

### Physics and measurement guidance
The guided ODE adds two DPS terms evaluated at the denoised estimate (eq. 5, p. 4):
$$\lambda_{obs}\nabla_{\hat x}\|y-M(I(D(\hat x)))\|^2$$
$$\lambda_{PDE}\nabla_{\hat x}L_{PDE}(I(D(\hat x)))$$
Under an Euler step these terms are gradient-descent steps, so they are replaced by Adam steps (Alg. 1, lines 4–7).

> [!algorithm] PISD inference (Alg. 1, p. 4)
> 1. $\hat x\sim\mathcal N(0,\sigma_{max}^2 I)$; initialise Adam on $\mathbb R^l$.
> 2. For $n=1..N$: compute $G_{obs}$, $G_{pde}$ at $D(\hat x,\sigma_n)$.
> 3. Euler step: $\hat x\leftarrow\hat x-\sigma_n^{-1}(D-\hat x)(\sigma_{n-1}-\sigma_n)$.
> 4. $\hat x\leftarrow\hat x-\mathrm{ADAM}(\lambda_{obs}G_{obs}+\lambda_{PDE}G_{pde})$.
> 5. Return $I(\hat x)$.

**Frequency-aware Adam** (App. B.3, p. 14): the moments persist across diffusion steps. The step size $\eta_k$ is `lr_low` for low modes and `lr_high` for high modes, with a smooth transition band. Low modes move aggressively and high modes are damped. Typical values: $\beta_1=0.97$–$0.985$, $\beta_2=0.98$, `lr_low` 0.1–0.2, `lr_high` 0.01 (Table 9).

### Spectral PDE residuals
- **Poisson and Helmholtz**: $u$ uses a sine series, so Dirichlet BCs hold automatically. The coefficient $a$ does not vanish at the boundary, so it is padded with four layers decaying to zero before the sine transform; this avoids Gibbs artifacts (p. 6, App. B.1). Laplacian:
$$\widehat{\Delta u}(k)=-\pi^2\|k\|^2\hat u(k)$$
- **Navier–Stokes**: vorticity form on $\mathbb T^2$ with $\nu=10^{-3}$, generating $w$ at 10 time steps jointly. Velocity comes from the Biot–Savart law in Fourier space (eq. 10), so $\nabla\cdot v=0$ holds by construction. The residual uses central differences in time; advection is computed pseudo-spectrally (p. 7).

**Setup**: DiffusionPDE datasets at 128×128. A ViT denoiser with 2M parameters, versus 54M for the baselines. Kept modes: 44×44 with hyperbolic truncation (Poisson and Helmholtz) and 32×32 low modes (Navier–Stokes) (App. B).

## Results

Relative errors from 100 runs (Tables 1–4):

| Task (500 obs.) | PISD | DiffusionPDE | FunDPS |
|---|---|---|---|
| Forward Poisson | 3.08% | 4.06% | 2.23% |
| Inverse Poisson | 13.8% | 22.2% | 21.1% |
| Inverse Helmholtz | 12.8% | 19.3% | 16.3% |
| PDE residual (inverse Poisson) | 0.45 | 178 | 588 |

- **Forward**: comparable to the baselines; FunDPS is better with sparse $a$. With full observations PISD reaches 0.05%.
- **Inverse**: PISD is best in every regime.
- **Joint reconstruction**: best on $u$. On the Helmholtz coefficient $a$, DiffusionPDE is slightly better.
- **Runtime** (RTX 2080 Ti): 52 s, versus 802 s for DiffusionPDE and 153 s for FunDPS (Table 7).
- **Navier–Stokes**: PISD generates the full 10-step trajectory and can condition on intermediate times. The baselines produce only the initial and terminal states, and PISD is more accurate on both (Table 4).
- **Ablations** (App. C):
  - Optimiser: on inverse Poisson, Adam gives 13.8%, plain GD 49% and momentum 50% (Tables 11–12).
  - FunDPS + Adam also beats FunDPS + GD (17.4% vs 21.1%, Table 10).
  - Guidance weights: error is stable across orders of magnitude, which the authors credit to Adam's step rescaling (Tables 13–14).
  - Truncation: hyperbolic beats square at the same size (Table 15).

## Limitations

As stated by the authors (Sec. 6, p. 8):
- A spectral basis must be chosen for each PDE. This suits regular domains with periodic, Dirichlet or Neumann BCs; irregular geometry needs domain decomposition or another basis.
- Training needs a dataset of solver outputs.

Possible extension: learned encoder–decoders, e.g. neural operators as in FunDiff (Wang 2025).

## Connections

- Grid-based physics guidance (DiffusionPDE, CoCoGen) applies only in the last ~10% of steps, because grid noise tends to white noise, where the residual is undefined. PISD's scaling allows guidance throughout (pp. 2, 5; Fig. 2, Fig. 7).
- Concurrent work (Belardi et al. 2026) proposes the same Adam-for-GD swap in DPS, for images (p. 3).
- Wiki note: the encoder is a fixed, data-scaled [[Fourier transform]] truncation, the same mode truncation an [[FNO]] layer uses, but applied to the generated field rather than inside a network.
- Wiki note: the residual guidance is the [[PINN]] loss used as a likelihood at sampling time, not as a training loss; compare the soft-penalty-as-MAP view in [[Physics-informed ML review (Karniadakis 2021)]].
- Wiki note: [[Generative priors for turbulence (Wang 2026)]] notes that learned priors can violate physics pointwise. PISD answers this with residual guidance plus a basis that enforces BCs and incompressibility.

%% refs:start %%
**Cites in this wiki**: [[DDPM (Ho 2020)]], [[DeepONet (Lu 2021)]], [[FNO (Li 2021)]], [[Neural operator (Kovachki 2022)]], [[PINNs (Raissi 2019)]], [[Score SDE (Song 2021)]]
%% refs:end %%

**Sources**: `papers/Operators/Gallon, Wurstemberger, Cheridito, Jentzen - Physics-Informed Diffusion Models in Spectral Space.pdf`.
**Last updated**: 2026-11-07

---

## Related pages
- [[Spectral diffusion]]
- [[Diffusion posterior sampling]]
- [[Diffusion models]]
- [[Adam]]
- [[PINN]]
- [[Poisson and Laplace equations]]
- [[Navier-Stokes equations]]
- [[Fourier transform]]
- [[FNO]]
- [[Generative priors for turbulence (Wang 2026)]]
