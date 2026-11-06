---
type: paper
area: gp
areas: [gp, ml]
source-ref: "Lee, Bilionis, Buganza Tepole 2020, CMAME 359:112724, eqs. 13-23"
tags: [gp, uq, bayesian, ml]
authors: ["[[Taeksang Lee]]", "[[Ilias Bilionis]]", "[[Adrian Buganza Tepole]]"]
year: 2020
venue: "Computer Methods in Applied Mechanics and Engineering 359 (2020) 112724"
file: "Guassian Processes/Bilionis, Lee, Buganza - Propagation of Uncertainty in Tissues Reponse via multi-fidelity GP Regression.pdf"
---

# Multi-fidelity GP for tissue expansion (Lee 2020)

**Summary**: Trains a [[Multi-fidelity Gaussian process]] surrogate on finite element (FE) simulations of skin growth under a balloon expander, using three mesh refinements as three fidelity levels. The multi-fidelity surrogate beats single-fidelity GPs on held-out high-fidelity runs, and is then used for uncertainty propagation and Sobol sensitivity analysis. Lab paper (Bilionis is a co-author).

**Authors**: Taeksang Lee, Ilias Bilionis, Adrian Buganza Tepole · **Year**: 2020 · **File**: `Guassian Processes/Bilionis, Lee, Buganza - Propagation of Uncertainty in Tissues Reponse via multi-fidelity GP Regression.pdf`

---

## Problem

Tissue expansion inflates a balloon under skin to grow new skin for reconstructive surgery. Growth and remodeling models are deterministic FE simulations with fixed parameters, yet skin properties and biological response vary between patients (p. 1-2). Clinical decisions need the probability of the growth outcome, but each FE run is costly (about 6 h on 1 CPU at the finest mesh, about 10 min at the coarsest, p. 8), so plain Monte Carlo is out of reach. Standard single-fidelity GP regression "becomes unattainable" as model cost rises (p. 18).

## Method

**Mechanics (§2.1-2.4).** Growth by multiplicative split of the deformation gradient (p. 3):
$$F=F_eF_g,\qquad \vartheta=\vartheta_e\,\vartheta_g.$$
Here $\vartheta$ is area deformation and $\vartheta_g$ the area growth. For a thin membrane, growth is in-plane only. The growth rate is a Hill function of elastic area stretch (eq. 6, p. 5):
$$\dot\vartheta_g=\frac{k(\vartheta_e-\vartheta_{cr})^n}{K^n+(\vartheta_e-\vartheta_{cr})^n}.$$
Skin is Neo-Hookean (eq. 7) with shear modulus $\mu$. FE in Abaqus with a user subroutine, domain $10\times10\times0.3$ cm, expander $4.5\times8$ cm, inflated to volume $V$. Fidelity = mesh: 800, 3200 or 20000 trilinear brick elements (p. 6).

**Uncertain inputs (Table 1, p. 9).**
- $\mu\in[0.10,1.00]$ MPa (mechanics)
- $K\in[0.02,0.06]$, $k\in[0.10,1.00]$, $n\in[0.80,1.20]$ (biology; $\vartheta_{cr}$ fixed at 1.1)
- time $t$ is added as a fifth input; $V\in\{40,50,60\}$ cc gets one GP each (later $V$ is an input too).

**Single-fidelity GP (§2.5).** Prior $f\sim\mathcal{GP}(m,k)$ with zero mean and squared-exponential kernel with per-dimension length scales (eq. 14). Hyperparameters by maximising the log marginal likelihood (eq. 15); predictive mean and variance in eqs. 18-19. See [[Gaussian process]].

**Multi-fidelity construction.** Levels $t=1,\dots,S$, increasing fidelity.
> [!definition] Autoregressive scheme (Kennedy-O'Hagan, cited as [63])
> $$f_t(x)=\rho_{t-1}f_{t-1}(x)+\delta_t(x),\quad \delta_t\sim\mathcal{GP}.$$
> Full covariance over all levels is too costly (p. 8).
>
> (source: eq. 21, p. 8)

> [!definition] Recursive scheme (Le Gratiet, cited as [64])
> Replace the prior of $f_{t-1}$ by its posterior $f^*_{t-1}$. Levels decouple: cost is $\sum_t O(n_t^3)$ rather than $O((\sum_t n_t)^3)$. Needs nested inputs $X_t\subseteq X_{t-1}$.
>
> (source: p. 8)

> [!definition] Nonlinear (deep) multi-fidelity GP (Perdikaris, cited as [31])
> The previous level's posterior is an extra input dimension:
> $$f_t(x)=g_t\big(x,f^*_{t-1}(x)\big).$$
> The matching kernel is
> $$k_{g_t}=k_{\rho_t}(x,x')\,k_{f_t}\big(f^*_{t-1}(x),f^*_{t-1}(x')\big)+k_{\delta_t}(x,x').$$
> This paper uses it, with squared-exponential kernels. For $t\ge3$ the posterior is no longer Gaussian ("a GP of a GP is not a GP"), so mean and variance come from Monte Carlo integration.
>
> (source: eqs. 22-23, p. 8)

Software: GPy and the multi-fidelity code of [31] (p. 9).

**Training design (§3.1).** Nested sets built from [[Latin hypercube sampling]] of $[\mu,K,k,n]$: 100 + 50 + 10 points. Low fidelity runs on all 160, medium on 60, high on 10, so 230 simulations in total. Each run gives the growth field on a $10\times10$ grid over 7 days; one surrogate per grid point, time as input. (The paper chose independent grid surrogates over the PCA reduction used in earlier work, p. 9; see [[Principal component analysis]].)

## Results

- **Validation (§3.2, Figs. 3-5).** 30 fresh LHS points, high fidelity only, taken as truth. The multi-fidelity GP has lower average relative error than a GP on high-fidelity data only or low-fidelity data only. The low-fidelity GP is "completely inaccurate" but still helps the fused model. Standardized residuals of the multi-fidelity GP lie within $[-3,3]$ and cluster near 0 (p. 11-12).
- **Number of high-fidelity runs (Figs. 6-7).** With $M_h=5$ both surrogates are poor. With $M_h=20$ multi-fidelity still wins, but the authors note that with enough high-fidelity data the low-fidelity information is no longer needed (p. 12-13). No clear threshold was found (p. 18).
- **Uncertainty propagation (§3.3, Fig. 8).** $\mu$ for young skin $\sim N(0.3,0.051)$, old skin $\sim N(0.75,0.026)$ (old about 2.5 times stiffer, from suction-device data). 100 samples per group pushed through the surrogate. Young skin grows more at apex and middle, with larger spread; growth equilibrates by day 3 (p. 14).
- **Biological parameters (Fig. 9).** Setting $K,k,n$ to their 10th or 90th percentile changes mostly the transient (first 5 days), little the day-7 contour. $K$ sets saturation, $k$ the adaptation speed, $n$ the nonlinearity (p. 14-15).
- **Volume as input (§3.4, Fig. 10).** Adding $V\in\{30,40,50,60\}$ cc: growth at day 7 rises with $V$, most at the apex. Variance from material uncertainty is roughly constant in $V$ (p. 15).
- **Sensitivity (§3.5, Fig. 11).** [[Sobol indices]] (SALib, Saltelli sampling, $N(2d+2)=12{,}000$ surrogate evaluations, $N=1000$, $d=5$). At apex and middle, $\mu$, $k$ and time matter, $n$ and $K$ less. As $V$ grows, $\mu$ matters less than $k$ and time, because strains become homogeneous and exceed $\vartheta_{cr}$ (p. 17-18).
- Conclusion on protocol: waiting 7 days between inflations looks reasonable since growth has stabilised (p. 19).

## Limitations

Stated by the authors (p. 19):
- simulation data only, assumed noiseless; noise would be needed for experimental data
- training design is arbitrary, number of high-fidelity runs hard to anticipate
- one inflation step and one expander shape
- isotropic Neo-Hookean skin; real skin is anisotropic

Wiki note: spatial correlation is ignored by the 100 independent grid-point GPs; a GP over (space, time) or a reduced basis would share information. **[unverified]** as a recommendation.

## Connections

- Instance of the [[Surrogate model]] / [[Multi-fidelity modeling]] workflow: cheap models plus few expensive ones, validated against held-out expensive runs.
- Kernel choice: squared-exponential, see [[Kernel methods]] and [[Kernel composition]] (the product-plus-sum kernel in eq. 23 is a composition).
- Hyperparameters via marginal likelihood as in [[Gaussian process]]; the GP literature background is in [[Gaussian processes and kernel methods (Kanagawa 2018)]] and [[Duvenaud thesis (Duvenaud 2014)]].
- Same lab line as [[Bayesian DenseED surrogate (Zhu 2018)]] (surrogate for uncertainty propagation, there a neural network).

**Sources**: `Guassian Processes/Bilionis, Lee, Buganza - Propagation of Uncertainty in Tissues Reponse via multi-fidelity GP Regression.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Multi-fidelity Gaussian process]] · [[Gaussian process]] · [[Multi-fidelity modeling]] · [[Surrogate model]]
- [[Latin hypercube sampling]] · [[Sobol indices]] · [[Principal component analysis]]
- [[Kernel methods]] · [[Kernel composition]]
- [[Bayesian DenseED surrogate (Zhu 2018)]]
