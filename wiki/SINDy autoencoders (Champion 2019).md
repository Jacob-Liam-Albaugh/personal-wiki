---
type: paper
area: physics-informed
areas: [physics-informed, ml]
source-ref: "Champion, Lusch, Kutz, Brunton 2019, PNAS, eqs. 1-7"
tags: [physics-informed, ml, optimization]
authors: ["[[Kathleen Champion]]", "[[Bethany Lusch]]", "[[J. Nathan Kutz]]", "[[Steven L. Brunton]]"]
year: 2019
venue: "PNAS (arXiv 1904.02107)"
file: "Physics Informed Architectures/Brunton, Champion, Lusch, Kutz - SINDy - Data-Driven Discovery of Coordinates and Governing Equations.pdf"
---

# Data-driven discovery of coordinates and governing equations (Champion 2019)

**Summary**: Trains an autoencoder and a [[SINDy]] model jointly, so the latent coordinates $z=\phi(x)$ are ones in which the dynamics are sparse in a chosen function library. Demonstrated on a 128-dimensional field built from the Lorenz system, a reaction-diffusion spiral wave, and a video of a nonlinear pendulum.

**Authors**: Kathleen Champion, Bethany Lusch, J. Nathan Kutz, Steven L. Brunton · **Year**: 2019 · **File**: `Physics Informed Architectures/Brunton, Champion, Lusch, Kutz - SINDy - Data-Driven Discovery of Coordinates and Governing Equations.pdf`

---

## Problem

SINDy finds the fewest terms in a library describing $\dot x=f(x)$, but only works if the measured coordinates admit a sparse description. Autoencoders and PCA find reduced coordinates but ignore dynamics; Koopman methods linearize but cannot capture all nonlinear behaviour. The paper puts coordinate discovery and model discovery "on equal footing" (source: SINDy autoencoders.pdf, pp. 1-2).

## Method

Background (§2.1, p. 3): stack snapshots into $X,\dot X\in\mathbb R^{m\times n}$, build a library $\Theta(X)=[\theta_1(X)\cdots\theta_p(X)]$, and solve $\dot X=\Theta(X)\Xi$ with sparse $\Xi\in\mathbb R^{p\times n}$ by sequentially thresholded least squares (a proxy for $\ell_0$).

> [!algorithm] SINDy autoencoder (§3, eqs. 2-7)
> Encoder $\phi$, decoder $\psi$, latent $z=\phi(x)\in\mathbb R^d$, $d\ll n$, with latent model
> $$\dot z=g(z)=\Theta(z)\Xi.$$
> Loss terms (derivatives by chain rule through the networks):
> $$\mathcal L_{\mathrm{recon}}=\|x-\psi(\phi(x))\|_2^2$$
> $$\mathcal L_{dx/dt}=\|\dot x-(\nabla_z\psi(\phi(x)))\,\Theta(\phi(x)^{\top})\Xi\|_2^2$$
> $$\mathcal L_{dz/dt}=\|\nabla_x\phi(x)\,\dot x-\Theta(\phi(x)^{\top})\Xi\|_2^2$$
> $$\mathcal L_{\mathrm{reg}}=\|\Xi\|_1$$
> Total (eq. 7): $\mathcal L_{\mathrm{recon}}+\lambda_1\mathcal L_{dx/dt}+\lambda_2\mathcal L_{dz/dt}+\lambda_3\mathcal L_{\mathrm{reg}}$.
>
> (source: eqs. 2-7, pp. 5-6, Fig. 1)

$\Xi$ is trained with the network weights (Adam). In addition, sequential thresholding is applied at fixed intervals during training: coefficients below a magnitude threshold are set to zero and training continues on the remaining terms (pp. 6-7). The pendulum uses a second-order SINDy model (library of $z,\dot z$ predicting $\ddot z$), which also needs second derivatives of encoder and decoder (p. 10).

## Results

- **Lorenz in 128-d** (§4.1): data $x=\sum u_i z_i + \dots$ (eq. 9) with six Legendre spatial modes mixing $z_i$ and $z_i^3$. Discovered model has 7 active terms, and after a variable rescaling/shift has the Lorenz sparsity pattern with coefficients close to the originals (Fig. 3). Test decoder error under $3\times10^{-5}$ of variance; unexplained variance of $\dot x$ and $\dot z$ were $2\times10^{-4}$ and $7\times10^{-4}$; simulated trajectory within 1% over the training duration, then diverges as expected for chaos (pp. 7-8).
- **Reaction-diffusion** (§4.2): $n=10^4$ pixels, $d=2$; unexplained variance 0.016 for $x$ and $\dot x$, 0.002 for $\dot z$, $1\times10^{-4}$ for simulated $z$ (pp. 9-10).
- **Nonlinear pendulum video** (§4.3): $d=1$, PCA cannot find a 1-D representation, the autoencoder does; 5 of 10 training runs identified the pendulum equation $\ddot z\approx-\sin z$ (Fig. 2 shows coefficient about $-0.99$) (p. 10).

## Limitations

Stated (§5, pp. 10-11): needs clean, nearly noise-free data because derivatives are required; noise-robust derivative estimation, a discrete-time variant or the integral SINDy formulation are suggested fixes. The coordinate map may not generalize far from training data (retrain with fixed latent terms). Wiki note: only 5 of 10 pendulum runs succeed, so results depend on initialization and the weights $\lambda_i$; the discovered Lorenz coordinates are unique only up to transformation.

## Connections

- Extended to partial observations in [[SINDy delay autoencoders (Bakarji 2022)]].
- The latent ODE is a sparse analogue of a [[Neural ODE]] vector field; compare structured fields in [[Hamiltonian neural network]].
- Related to [[Dynamic mode decomposition]] / Koopman (linear latent dynamics) and to [[Principal component analysis]] (linear coordinates).

%% refs:start %%
**Cites in this wiki**: [[Adam paper (Kingma 2015)]], [[Glorot init (Glorot 2010)]]
**Cited by in this wiki**: [[Energy-based kernels for viscoelastic flow (Otto 2024)]], [[NIF (Pan 2023)]], [[PySR (Cranmer 2023)]], [[SINDy delay autoencoders (Bakarji 2022)]]
%% refs:end %%

**Sources**: `Physics Informed Architectures/Brunton, Champion, Lusch, Kutz - SINDy - Data-Driven Discovery of Coordinates and Governing Equations.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[SINDy]] · [[SINDy delay autoencoders (Bakarji 2022)]] · [[Neural ODE]] · [[Physics-informed machine learning]]
- [[Dynamic mode decomposition]] · [[Principal component analysis]] · [[LASSO]] · [[Symbolic regression]]
