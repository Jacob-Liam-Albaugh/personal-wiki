---
type: example
area: me697
areas: [me697]
source-ref: "ASML (ME 697)"
tags: [physics-informed, pde]
data-origin: [analytic]
tasks: [physics-informed]
uses: 3
---

# Manufactured 2D Poisson

**Summary**: 3 uses in ASML (ME 697). Data: analytic. Tasks: physics-informed.

**Covered in**: ASML (ME 697)
**Sources**: `text_books/advanced-scientific-machine-learning/book/pinns/basics/forward.ipynb` and the notebooks listed below.
**Last updated**: 2026-11-18

---

## Manufactured 2D Poisson / steady heat (residual PINN)

`text_books/advanced-scientific-machine-learning/book/pinns/basics/forward.ipynb`

- **Source**: ASML (ME 697), lecture, complete
- **Problem**: PINN forward solve
- **Technique**: Residual-loss PINN; non-dimensionalisation/scaling of f and u (fs=9.96e6, us=4.40e4, length scales 4.415 and 0.04415) to make the loss trainable
- **Data**: No data; 256 collocation points in the domain plus boundary points; exact solution known in closed form.
- **Data origin**: analytic
- **Forward model**: Steady heat/Poisson -k\*Lap(u)=f on [0,0.1]x[0,1], k=10, u0=500, manufactured exact u=u0 sin^2(pi x/Lx) sin^2(pi y/Ly). Residual loss on PDE + Dirichlet BC; JAX/Equinox MLP, Optax Adam.
- **Unknown dimension**: network weights (MLP width 128, depth 4, tanh)
- **Data dimension**: 256 collocation points
- **Ground truth**: Exact analytic solution
- **What makes it hard**: Badly scaled: unscaled loss ~1.7e12 and does not decrease; high aspect ratio domain (0.1 x 1)
- **Libraries**: jax, equinox, optax
- **References**: Wang et al. 2023 (arXiv 2308.08468) on PINN training
- **Notes**: Adam lr 1e-3. Scaled loss falls 0.178 -> 4.26e-4 in 2000 iterations. Markdown says sin(10 pi y) but code uses sin(pi y).

## Manufactured 2D Poisson / steady heat (Ritz energy PINN)

`text_books/advanced-scientific-machine-learning/book/pinns/basics/energy.ipynb`

- **Source**: ASML (ME 697), lecture, complete
- **Problem**: PINN forward solve
- **Technique**: Variational (Ritz) energy PINN with Fourier-feature MLP (100 features, width 256, depth 4); scaling fs=1.364e4, us=6.414e4, kx=4702, ky=47.02
- **Data**: No data; same manufactured problem as forward.ipynb.
- **Data origin**: analytic
- **Forward model**: Steady heat/Poisson -k\*Lap(u)=f on [0,0.1]x[0,1], k=10, u0=500, manufactured exact u=u0 sin^2(pi x/Lx) sin^2(pi y/Ly). Minimises energy functional E[u]=int k/2/grad u/^2 - f u with BCs enforced; JAX.
- **Unknown dimension**: network weights
- **Data dimension**: random collocation points (count unclear)
- **Ground truth**: Exact analytic solution
- **What makes it hard**: Anisotropic, badly scaled domain
- **Libraries**: jax, equinox, optax
- **Notes**: 5000 iterations; energy loss about -0.387. Notebook reports it as less accurate than the residual loss.

## Manufactured 2D Poisson / steady heat (Fourier-feature residual PINN)

`text_books/advanced-scientific-machine-learning/book/pinns/basics/spectral_bias.ipynb`

- **Source**: ASML (ME 697), lecture, complete
- **Problem**: PINN forward solve
- **Technique**: Residual PINN with Fourier features (sigma=6), fs=9.96e6, us=2.69e4
- **Data**: Same heat problem as forward.ipynb.
- **Data origin**: analytic
- **Forward model**: Steady heat/Poisson -k\*Lap(u)=f on [0,0.1]x[0,1], k=10, u0=500, manufactured exact u=u0 sin^2(pi x/Lx) sin^2(pi y/Ly).
- **Unknown dimension**: network weights
- **Ground truth**: Exact analytic solution
- **What makes it hard**: Spectral bias / scaling
- **Libraries**: jax, equinox, optax
- **References**: Tancik et al. 2020
- **Notes**: Loss 0.274 -> 1.18e-5.

## Related pages
- [[Examples catalogue]]
- [[PINN]] · [[Fourier features]] · [[Spectral bias]] · [[Poisson and Laplace equations]] · [[Adam]] · [[Energy functional]]
