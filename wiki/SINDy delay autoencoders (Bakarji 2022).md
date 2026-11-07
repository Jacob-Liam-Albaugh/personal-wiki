---
type: paper
area: physics-informed
areas: [physics-informed, ml]
source-ref: "Bakarji, Champion, Kutz, Brunton 2022, arXiv 2201.05136, eqs. 5-15"
tags: [physics-informed, ml, optimization]
authors: ["[[Joseph Bakarji]]", "[[Kathleen Champion]]", "[[J. Nathan Kutz]]", "[[Steven L. Brunton]]"]
year: 2022
venue: "arXiv 2201.05136"
file: "papers/Physics Informed Architectures/Brunton, Bakarji, Champion, Kutz -SINDy - Discovering Governing Equations Deep Delay Autoencoders.pdf"
---

# Discovering governing equations from partial measurements with deep delay autoencoders (Bakarji 2022)

**Summary**: When only a scalar $y(t)$ of a larger state is measured, time-delay embedding (Takens) gives a diffeomorphic copy of the attractor, but in unknown coordinates. This paper extends the [[SINDy autoencoders (Champion 2019)]] to learn a map from the delay-embedded vector to coordinates where the dynamics are sparse, adding three delay-specific losses. Tested on Lorenz, Rossler, Lotka-Volterra and a video of a chaotic waterwheel.

**Authors**: Joseph Bakarji, Kathleen Champion, J. Nathan Kutz, Steven L. Brunton · **Year**: 2022 · **File**: `papers/Physics Informed Architectures/Brunton, Bakarji, Champion, Kutz -SINDy - Discovering Governing Equations Deep Delay Autoencoders.pdf`

---

## Problem

Measurements $y=g(x)+\eta$ with $\dim y<\dim x$ leave hidden variables, so no closed-form model exists in $y$ (the closure problem, p. 4). Takens' theorem says the delay vector
$$h(t;n,\tau)=[y(t),y(t+\tau),\dots,y(t+(n-1)\tau)]$$
has an attractor diffeomorphic to the full-state one if $n>2m$ ($m$ = state dimension), but gives no recipe for the map (p. 4). Learning that map and a sparse model together has been open since 1981 (abstract).

## Method

Delay vectors form a Hankel matrix $H=U\Sigma V^\top$ (eq. 5). The first $p$ columns $U_p$ give an optional linear reduction ([[Singular value decomposition]]), as in HAVOK. SINDy minimizes $\|\dot Z-\Theta(Z)\Xi\|^2+\lambda\|\Xi\|_0$ (eq. 6), relaxed to $\ell_1$ or thresholding.

> [!algorithm] Delay SINDy autoencoder (§3)
> Encoder $\varphi$ maps $h^{\top}U_p$ to $z\in\mathbb R^m$; decoder $\psi$ returns to $h$. Standard SINDy-autoencoder losses (eqs. 10a, 10b, 11), plus three new ones:
> - **Loss 1**: SVD projection in front of the autoencoder (denoising, cheaper).
> - **Loss 2** (eq. 12): first latent component equals the measurement,
> $$\mathcal L_{z_1}=\|h_{i1}-z_{i1}\|^2.$$
> This cuts permutation ambiguity of $z$ and ties the model to the measured quantity.
> - **Loss 3** (eq. 14): integrate the SINDy model from $\hat z(t_1)$ with RK4 (a recurrent layer) and require the first component to match $h_i$:
> $$\mathcal L_{\mathrm{cons}}=\sum_{j}\Big\|h_{ij}-\Big(\int_{t_1}^{t_j}\Theta\,\Xi\,dt\Big)_1\Big\|^2.$$
> Total (eq. 15): $\mathcal L_{\mathrm{recon}}+\lambda_1\mathcal L_{\dot h}+\lambda_2\mathcal L_{\dot z}+\lambda_3\mathcal L_{z_1}+\lambda_4\mathcal L_{\mathrm{cons}}+\lambda_5\mathcal L_{\mathrm{reg}}$.
>
> (source: eqs. 5-15, pp. 5-9)

Training is staged as four sub-problems of growing hypothesis class (§4): (1) supervised with known $x$; (2) known equation, fixed $\Xi$; (3) $\Xi$ initialised near the truth; (4) random initialisation. Delay settings follow HAVOK: $n\tau\approx0.1$ for Lorenz (App. A). Running a separate SINDy fit on $z$ every $k\approx20$-$40$ epochs improved sparsity and escaped local minima (p. 13).

## Results

- **Lorenz from $x_1$ only** (§4.1): sub-problems 1-2 solved accurately. With random $\Xi$ the run found $\dot z_1=-16z_1+2.5z_2z_3$, $\dot z_2=8z_2-16z_1z_3$, $\dot z_3=8z_2^2-1.4z_3^2$ (eq. 17): 6 terms vs 7 in Lorenz, but 4 nonlinear terms vs 2, with a two-lobe attractor (p. 13).
- Large random perturbations of $\Xi$ around Lorenz coefficients still converge to Lorenz-like attractors; fully random init is hyperparameter-sensitive (p. 12-13).
- **Rossler**: model less sparse than the original, bursting captured. **Lotka-Volterra**: structurally similar (Fig. 9). **Waterwheel video**: angular velocity extracted by Hough transform + k-means; a third-degree polynomial library reproduces two-lobe chaos from 24 fps data (App. B, Table 1).
- Without SINDy terms the autoencoder reconstructs well (error about $7\times10^{-7}$) but its latent space is unlikely to be sparse (Fig. 14).

## Limitations

Authors: optimizer prone to local minima and over-fitting; unknown whether any loss recovers the exact original system from 1-D data with random init; the SINDy step is basic ($\ell_1$), and probabilistic or weak SINDy would help noisy video; not every scalar measurement works (the third Lorenz coordinate violates the Takens condition) (§4-5). Discovered models need not match the original (non-unique coordinates).

## Connections

- Direct extension of [[SINDy autoencoders (Champion 2019)]]; uses [[SINDy]] throughout.
- Related to [[Dynamic mode decomposition]] on delay coordinates (HAVOK, linear closure), and to [[Symbolic regression]] (genetic programming) as the earlier parsimonious-model route.
- Suggests invertible networks to enforce the diffeomorphism by construction.

%% refs:start %%
**Cites in this wiki**: [[Deep Koopman (Lusch 2018)]], [[Eureqa (Schmidt 2009)]], [[PINNs (Raissi 2019)]], [[SINDy (Brunton 2016)]], [[SINDy autoencoders (Champion 2019)]], [[Tensor basis NN turbulence (Ling 2016)]]
%% refs:end %%

**Sources**: `papers/Physics Informed Architectures/Brunton, Bakarji, Champion, Kutz -SINDy - Discovering Governing Equations Deep Delay Autoencoders.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[SINDy (Brunton 2016)]] · [[SINDy]] · [[SINDy autoencoders (Champion 2019)]] · [[Singular value decomposition]] · [[Dynamic mode decomposition]]
- [[Neural ODE]] · [[Physics-informed machine learning]] · [[Symbolic regression]]
