---
type: paper
area: bayesian
areas: [inverse-problems]
source-ref: "Tsilifis, Bilionis, Katsounaros, Zabaras 2014, arXiv:1410.5522"
tags: [bayesian, vi, inverse-problems]
authors: ["[[Panagiotis Tsilifis]]", "[[Ilias Bilionis]]", "[[Ioannis Katsounaros]]", "[[Nicholas Zabaras]]"]
year: 2014
venue: "arXiv:1410.5522 (stat.ML), submitted to Inverse Problems"
file: "Bayesian/Bilionis, Tsilifis - Variational Reformulation of Bayesian Inverse Problems.pdf"
---

# Variational reformulation of Bayesian inverse problems (Tsilifis 2014)

**Summary**: Casts the Bayesian solution of an inverse problem as an optimisation: maximise the [[ELBO]] over a Gaussian-mixture family, using analytic approximations that need only first and second derivatives of the forward model. On a catalysis calibration and a contaminant-source problem it matches MALA MCMC with about 50 forward solves instead of thousands, but slightly underestimates uncertainty.

**Authors**: Panagiotis Tsilifis (USC), Ilias Bilionis (Purdue), Ioannis Katsounaros, Nicholas Zabaras (Warwick) · **Year**: 2014 (arXiv, 21 Oct 2014; "Submitted to: Inverse Problems") · **File**: `Bayesian/Bilionis, Tsilifis - Variational Reformulation of Bayesian Inverse Problems.pdf`

Wiki note: the filename lists Bilionis first; the paper's first author is Tsilifis. Bilionis is the corresponding author (p. 1).

---

## Problem

Forward model $f:\mathbb R^{d_\xi}\to\mathbb R^{d_y}$ links unknown parameters $\xi$ to data $y$ through a likelihood $p(y\mid\xi,\theta)=p(y\mid f(\xi),\theta)$, where $\theta$ holds noise/discrepancy parameters (source: file, eq. 1). With $\omega=(\xi,\theta)$ the [[Bayesian inverse problems]] solution is the posterior $p(\omega\mid y)=p(y\mid\omega)p(\omega)/p(y)$ (eq. 6). MCMC needs many forward solves, and surrogate-based MCMC fails when the surrogate is inaccurate and surrogates get exponentially harder as dimension grows (p. 2). MAP and Laplace are cheap but need a single sharp, roughly Gaussian mode (p. 2). The paper wants a surrogate-free method that returns a full posterior at a small multiple of optimisation cost.

## Method

Choose the "best" $q$ in a family $\mathcal Q$ by minimising [[KL divergence]] to the posterior, which is equivalent to maximising the ELBO ([[Variational inference]]).

> [!definition] ELBO (source: file, eqs. 7-14)
> $$\log p(y)=\mathcal F[q]+\mathrm{KL}\big[q(\omega)\,\|\,p(\omega\mid y)\big]$$
> $$\mathcal F[q]=\mathbb E_q\!\left[\log\frac{p(y,\omega)}{q(\omega)}\right]=H[q]+\mathbb E_q[\log p(y,\omega)],\qquad \mathcal F[q]\le\log p(y)$$
> $$q^*=\arg\max_{q\in\mathcal Q}\mathcal F[q]$$

**Family**: Gaussian mixtures with $L$ components (eq. 15), as in nonparametric VI (Gershman, Hoffman, Blei 2012; cited, not read).

> [!definition] Gaussian-mixture variational family (source: file, eq. 15)
> $$q(\omega)=\sum_{i=1}^{L}w_i\,\mathcal N(\omega\mid\mu_i,\Sigma_i),\quad w_i\ge0,\ \sum_i w_i=1$$

**Analytic approximation of the ELBO** (no Monte Carlo, unlike the later [[Reparameterization trick]] approach in [[Amortized VI for inverse problems (Karumuri 2024)]]):

> [!theorem] Entropy lower bound (source: file, eqs. 16-18)
> Jensen's inequality plus Gaussian convolution give $H[q]\ge H_0[q]$ with
> $$H_0[q]=-\sum_{i=1}^L w_i\ln q_i,\qquad q_i=\sum_{j=1}^L w_j\,\mathcal N(\mu_i\mid\mu_j,\Sigma_i+\Sigma_j).$$

> [!definition] Taylor approximations of the expected log joint (source: file, eqs. 19-24)
> Expand $\log p(y,\omega)$ about each $\mu_i$ (eq. 21):
> $$\mathcal L_0[q]=\sum_i w_i\log p(y,\mu_i),\qquad
> \mathcal L_2[q]=\mathcal L_0[q]+\tfrac12\sum_i w_i\,\mathrm{Tr}\!\big(\Sigma_i\nabla^2_\omega\log p(y,\mu_i)\big)$$
> $$\mathcal F_a[q]=H_0[q]+\mathcal L_a[q],\quad a\in\{0,2\}$$

Design reasoning (p. 7): $\mathcal L_0$ does not depend on $\Sigma_i$ and $H_0$ grows without bound in $|\Sigma_i|$, so the lowest-order objective carrying information about $\Sigma_i$ is $\mathcal F_2$ (needs the Hessian of the forward model). Optimising $\mu_i$ with $\mathcal F_2$ would need third derivatives, so $\mu_i$ is optimised with $\mathcal F_0$ (first derivatives only; adjoints can supply them). Covariances are restricted to diagonal (eq. 25), which needs only the Hessian diagonal and avoids enforcing positive-definiteness.

> [!algorithm] Algorithm 1: variational inference (source: file, p. 8)
> Initialise $w_i$, $\Sigma_i=I$, $\mu_i$ random. Repeat until the change in $\mathcal F_2[q]$ is below $\epsilon=10^{-2}$:
> 1. $\{\mu_i\}\leftarrow\arg\max \mathcal F_0[q]$
> 2. $\{w_i\}\leftarrow\arg\max \mathcal F_2[q]$
> 3. $\{\Sigma_i\}\leftarrow\arg\max_{\text{diag}}\mathcal F_2[q]$
>
> Each sub-problem uses L-BFGS-B with bounds (p. 7). Wiki note: the printed initialisation says $w_i=1/N$; from context it should be $1/L$.

Appendix A gives the gradients of $H_0$, $\mathcal L_0$, $\mathcal L_2$ w.r.t. $w_i,\mu_{ij},\Sigma_{ijk}$ (eqs. A.3-A.17) and the chain rule through the forward model (A.26-A.30), which needs the Jacobian and (diagonal) Hessian of $f$. For ODE models these come from sensitivity equations (A.33-A.34); for the diffusion PDE from PDEs with differentiated source terms (A.35-A.36).

## Results

Reference method: MALA MCMC (step $dt=0.1$, 1,000 burn-in, thin by 100, 100,000 steps; p. 7-8).

**Nitrate-reduction kinetics** (5 rate constants, $d_y=30$, data from Katsounaros et al. 2012; pp. 8-13). Parameters $\xi_i=\log\kappa_i$ with $N(0,1)$ priors, $p(\theta)=N(-1,1)$. One Gaussian ($L=1$).
- Table 2 (means, $\pm2$ sd): e.g. $\xi_1$ VAR $1.359\pm0.055$ vs MCMC $1.356\pm0.072$; $\theta$ $-3.840\pm0.204$ vs $-3.757\pm0.251$. Means agree closely; VAR uncertainty is smaller throughout, but the ordering of parameters by uncertainty is the same (p. 11).
- Table 3: VAR medians match Katsounaros (2012) rates, e.g. $k_1$ 0.0216 (same), $k_2$ 0.0291 vs 0.0292, $k_4$ 0.0020 vs 0.0021. Noise $\sigma$ estimated at about 2.15% (95%: 0.0176-0.0262), which the earlier paper did not estimate (p. 13).
- Cost: **37 forward model evaluations** vs thousands for MALA (p. 12).

**Contaminant source identification** (2D diffusion, Gaussian source of width 0.05, 25x25 grid for inference, 110x110 grid for synthetic data, true source $\xi^*=(0.09,0.23)$, noise $\sigma^*=0.05$; pp. 14-17).
- Case 1, four corner sensors, unimodal posterior, $L=1$: **48 forward evaluations**; about 15 min on one node vs about 3 days for MALA (p. 16). Noise level recovered; uncertainty underestimated.
- Case 2, two mid-boundary sensors: symmetry $\xi_1\leftrightarrow1-\xi_1$ makes the posterior bimodal. $L=2$ recovers both modes with **62 evaluations** (p. 17). The authors note MALA only works here because the proposal was hand-tuned to allow mode jumps.

## Limitations

As stated by the authors (pp. 17-18):
- Systematically underestimates posterior uncertainty.
- $L$ must be at least the true number of modes, which is unknown; two initial means that start close together collapse onto the same mode, attributed to the local nature of the Taylor approximation. Random restarts fix this in the example.
- Needs forward-model gradients and Hessians (diagonal Hessian in practice); third derivatives are avoided only by switching objectives for $\mu_i$.
- The stochastic, approximation-free ELBO maximisation and dimensionality reduction are listed as future work.

Wiki note: the examples are low dimensional (6 to 7 unknowns) and the ELBO is a crude local approximation; no high-dimensional test is given.

## Connections

- Direct ancestor of [[Amortized VI for inverse problems (Karumuri 2024)]], which cites it as the VI-for-inverse-problems precedent (ref. [41]) and replaces the Gaussian-mixture, Taylor-expansion scheme by neural-network guides trained with the [[Reparameterization trick]]. It also moves from one-posterior-per-dataset to [[Amortized VI]], removing the need to rerun optimisation for each new $y$.
- Both lab papers use the same likelihood form (Gaussian around $f(\xi)$) and the same contaminant-style/PDE benchmarks with MCMC as ground truth.
- The per-dataset optimisation here is the "F-VI-like" setting studied in [[Amortized VI when and why (Margossian 2024)]]; there the question is when one shared inference function can reproduce per-observation optima.
- Related lab-adjacent method pages: [[SGLD]] (alternative gradient-based posterior sampler), [[Information field theory]] (field-valued Bayesian inference).

%% refs:start %%
**Cited by in this wiki**: [[Amortized VI for inverse problems (Karumuri 2024)]]
%% refs:end %%

**Sources**: `Bayesian/Bilionis, Tsilifis - Variational Reformulation of Bayesian Inverse Problems.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Variational inference]]
- [[ELBO]]
- [[KL divergence]]
- [[Bayesian inverse problems]]
- [[Amortized VI for inverse problems (Karumuri 2024)]]
- [[Amortized VI when and why (Margossian 2024)]]
- [[SGLD]]
- [[Information field theory]]
- Its example 3.1 (catalysis, Katsounaros 2012 experiment) is the running example of Part 4 of the book: [[Catalysis problem]]. (source: `inverse/basics/02_classic_example.ipynb`)
