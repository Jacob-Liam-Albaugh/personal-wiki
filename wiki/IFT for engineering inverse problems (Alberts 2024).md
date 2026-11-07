---
type: paper
area: ift
areas: [ift, bayesian, inverse-problems, physics-informed]
source-ref: "Alberts 2024, PhD dissertation, Purdue University (advisor I. Bilionis), May 2024"
tags: [ift, bayesian, inverse-problems, physics-informed, pde, uq, sampling, mcmc]
authors: ["[[Alexander Alberts]]"]
year: 2024
venue: "PhD dissertation, Purdue University"
file: "papers/IFT/Alberts - An Information Field Theory Approach to Engineering Inverse Problems.pdf"
---

# IFT for engineering inverse problems (Alberts 2024)

**Summary**: Dissertation that develops [[Information field theory]] as a Bayesian framework for infinite-dimensional inverse problems where a PDE is prior knowledge. The physics enters through a Boltzmann-type [[Physics-informed prior]] $p(\phi)\propto e^{-\beta U(\phi)}$, whose trust parameter $\beta$ is inferred from data. Chapters 3, 5 and 6 are the 2023 JCP paper ([[PIFT (Alberts 2023)]]) with fuller proofs; Chapter 4 is the well-posedness preprint ([[MAP uniqueness in IFT (Alberts 2025)]]). New here: the function-space background (Ch. 2), the free-theory operator calculus (Ch. 3), the PINN and B-PINN comparison with the Bayesian-asymptotics argument (Ch. 5), and four numerical examples (Ch. 6).

**Authors**: Alexander Alberts · **Year**: 2024 · **File**: `papers/IFT/Alberts - An Information Field Theory Approach to Engineering Inverse Problems.pdf`

Page numbers below are PDF page numbers (they equal the printed numbers). Chapters: 1 pp. 10-11, 2 pp. 12-35, 3 pp. 36-58, 4 pp. 59-86, 5 pp. 87-101, 6 pp. 102-118, 7 pp. 119-123, Appendix A p. 140 (derives eq. 4.20).

---

## Where each chapter lives in the wiki

| Chapter | Covered on |
|---|---|
| 2 Background | this page, [[Generalized random fields]] |
| 3 Free theory, physics-informed prior | [[Information field theory]], [[Physics-informed prior]], [[Operator calculus for free theory]] |
| 4 Well-posedness | [[MAP uniqueness in IFT (Alberts 2025)]], [[Model-form error detection]] |
| 5 Sampling, PINNs | [[Nested SGLD]], [[PINN]], [[SGLD]] |
| 6 Examples | this page (1-4), [[Model-form error detection]] |
| 7 Future work | this page |

## Problem

Reconstruct a field $\phi$ from noisy data $d=R\phi+\text{noise}$ when a PDE $L\phi=f$ is believed to govern it. Gaussian processes cannot encode a nonlinear PDE as a prior. Putting the PDE into the likelihood (B-PINN) makes the posterior collapse as data grows and gives no principled data-vs-physics weight. IFT puts the physics in the prior and the weight into a learnable $\beta$ (source: dissertation, pp. 13-25, 119).

## Ch. 2 Background (new material)

- **Data-driven field inference** (pp. 13-15): least squares loses the function-space view and has local minima. GP regression, MGVI and GeoVI are the main tools; the Milky Way dust map has 661 million degrees of freedom. MGVI and GeoVI need a generative-model formulation, which a differential-operator precision does not provide. Data-driven fits extrapolate poorly.
- **Physics-based approaches** (pp. 16-20): PINNs from Lagaris (1990s) on; strong for integro-differential equations, high dimension and parameter-as-input design. Surveyed: Kalman and particle filters, physics-guided deep Markov models, energy-functional PINNs, PI-GANs, B-PINNs (BNN with fictitious zero-residual likelihood, HMC or VI), GP-PDE solvers conditioned on collocation points.
- **Generalized random fields** (pp. 20-25): physics-informed GPs come from Green's-function kernels; no GP prior exists for a nonlinear PDE. The characteristic functional and Bochner-Minlos theorem give a discretisation-free definition. Wish list (pp. 23-25): no discretisation until the last moment, data fusion, and model-form uncertainty with an automatically adjusting "learning rate". See [[Generalized random fields]].
- **Path-integral history** (pp. 25-26): Daniell 1919, Feynman time-slicing, Wiener as the first Bayesian field inference, Feynman-Kac.
- **Function-space tools** (pp. 26-30): Sobolev space $W^{k}$ with $k=d_H+r$, $d_H>d_\Omega/2$, $0<r<1$ (p. 27); Schwartz kernel theorem (Thm 2.2.1); Riesz representation (Thm 2.2.2); Frechet and Gateaux derivatives (Defs 2.2.3-2.2.4); Volterra series (Def 2.2.5).
- **Integration on function spaces** (pp. 30-33): no nonzero translation-invariant finite measure exists on an infinite-dimensional Banach space (Thm 2.2.4, p. 31), so $\int\mathcal D\phi$ is formal and only ratios are meaningful. Semiclassical expansion about a minimiser $\phi^*$: Gaussian measure with the Hessian as precision, polynomial remainder by Wick/Isserlis (pp. 32-33).
- **Three working assumptions** (pp. 34-35): (1) the measure $\mu_H=\int\mathcal D\phi$ exists after Fourier truncation ("effective field theory"); (2) $\nabla_x$ commutes with $\int\mathcal D\phi$; (3) functional derivatives commute with $\int\mathcal D\phi$.

## Ch. 3 Method

> [!definition] Free theory (eqs. 3.2-3.4, pp. 37-39)
> $$p(\phi)=\tfrac1Z\exp\{-\tfrac12\phi^\dagger S^{-1}\phi\}$$
> $$Z(q)=C[\det S]^{-1/2}\exp\{\tfrac12 q^\dagger Sq\}$$
> Here $S$ is the covariance. Moments follow from Gateaux derivatives of $Z(q)$: $E[\phi]=0$ (Prop. 3.1.1, p. 38) and $E[\phi(x)\phi(x')]=s(x,x')$ (Prop. 3.1.2, p. 40), both proved in full.

- **Posterior** (eqs. 3.9-3.14, p. 44): Woodbury form with $K=N+RS^{-1}R^\dagger$; Dirac measurements give GP regression. With hyperparameters $\lambda$ (Def. 3.1.1):
$$\tilde S_\lambda=(S_\lambda^{-1}+R^\dagger N^{-1}R)^{-1}$$
$$\tilde m_\lambda=\tilde S_\lambda R^\dagger N^{-1}d$$
- **Interactive theory** (p. 45): non-Gaussian priors; approximated by sampling (Ch. 5), SVI or GeoVI.
- **Operator calculus** (pp. 45-46): $E[F(\phi)]=F(\Phi)1$ with creation and annihilation operators. See [[Operator calculus for free theory]].
- **Physics-informed prior** (Sec. 3.2.1, pp. 47-51): energy $U=\int u(x,\phi,\nabla\phi,\dots)$ (eq. 3.16), squared-residual energy (eq. 3.17), Boltzmann prior (eq. 3.18) with $\beta$ called the *trust*. Posterior Hamiltonian $H(\phi|d)=\ell+\beta U$ (p. 51); $\beta$ acts as a learning rate and can "turn the physics off".
- **Klein-Gordon** (Sec. 3.2.2, pp. 52-56): full integration-by-parts proof that $U=\tfrac12\phi^\dagger S\phi-q^\dagger\phi$ (p. 53). $S^{-1}$ is the Green's function (eq. 3.23); the prior is $\mathcal G(S^{-1}q,\beta^{-1}S^{-1})$. Its partition function diverges unless the field is truncated at the smallest physical scale (p. 55); the prior is unimodal only with boundary conditions fixed. Posterior (eq. 3.24) matches the 2023 paper's eqs. 20-21.
- **Inverse problems** (Sec. 3.2.3, pp. 57-58): parameters in the likelihood alone leave $Z$ untouched. Parameters in the energy, or $\beta$, enter through $Z(\lambda,\beta)$ (eqs. 3.25-3.26), so $Z$ cannot be dropped, which motivates [[Nested SGLD]].

> [!warning] Notation
> Sec. 3.1 uses $S$ as covariance ($S^{-1}$ in the exponent). Sec. 3.2, the information Hamiltonian on p. 43 and the Klein-Gordon section use $S$ as precision, as does [[PIFT (Alberts 2023)]]. Check which convention a formula uses before comparing.

## Ch. 4 Well-posedness (short; see [[MAP uniqueness in IFT (Alberts 2025)]])

- Setting (pp. 59-63): $\lambda=(\gamma,\beta)$, posterior Hamiltonian $H(\phi,\lambda|d)=H(d|R\phi)+H(\phi|\lambda)+H(\lambda)$ (eq. 4.4). Well-posed means $H(\lambda|d)$ has a unique minimum (Def. 4.2.1, p. 64).
- Gradient (Lemma 1, p. 65, proof pp. 66-67) and Hessian (Lemma 2, p. 67, proof pp. 68-70). Lemma 3 (p. 71) gives the free-theory covariances; the proof uses the operator calculus, and eq. 4.20 is derived in Appendix A (p. 140).
- Informative data (Def. 4.2.5): $C[\nabla H|\lambda]-C[\nabla H|d,\lambda]\succ0$. Convergence of posterior mean and covariance (Thm 4.2.1, p. 76, from [145] Thms 3.5, 3.8) holds for Matern kernels and even-type Green's functions.
- Main result (Thm 4.2.2, p. 78): linear-in-parameters energy, flat parameter prior, informative data, existing root: unique MAP. Caution (p. 79): inferring $\beta$ with a physics parameter breaks linearity.
- Sec. 4.4 (pp. 85-86): Matern-type kernels are nonlinear in hyperparameters; interactive theory and the partition function are open, with Feynman diagrams suggested.

> [!theorem] Optimal trust, 2D Poisson (Sec. 4.3, pp. 79-85)
> Energy $U=\tfrac12\phi^\dagger L\phi-q^\dagger\phi$, $L=-\nabla^2$, $G=L^{-1}$, prior $\mathcal G(Gq,\beta^{-1}G)$. With a flat prior on $\beta$ the stationarity condition (eq. 4.25) equates the expected prior and posterior energies:
> $$E[U|\beta]=E[U|d,\beta]$$
> Eq. 4.26 and its $n\to\infty$ limit (eq. 4.27):
> $$\beta^{*-1}=\frac{(\phi^*-Gq)^\dagger L(\phi^*-Gq)}{\mathrm{Tr}(I)}$$
> Exact physics gives $\beta^*=\infty$; model-form error gives finite $\beta^*$, larger for better models. $\mathrm{Tr}(I)$ is the dimension of the truncated subspace, so $\beta^*$ grows with mesh refinement.
> Jeffreys prior: the denominator becomes $\mathrm{Tr}(I)-2$ and
> $$\partial^2_\beta H(\beta^*|d)=\tfrac12(\beta^{*-1})^2(\mathrm{Tr}(I)-1)$$
> so $\mathrm{Tr}(I)>2$ is sufficient (p. 85).

## Ch. 5 Sampling and PINNs

- **Field sampling** (Sec. 5.1.1, pp. 87-92): NIFTy does not apply to a differential-operator $S$. Parameterise $\hat\phi(x;\theta)$ by a truncated Fourier basis or neural network, $H(\theta|d)=\ell+\beta U(\theta)$, and use an importance-sampled unbiased energy gradient with uniform $q$. SGLD (eq. 5.1) uses noise $\eta_t\sim\mathcal N(0,\sqrt{\epsilon_t})$, $\epsilon_t=\alpha_0/t^{\alpha_1}$, $\alpha_1\in(0.5,1]$. Algorithm 1 samples the prior, Algorithm 2 the posterior with data subsampling (eq. 5.2).
- **Initialisation matters** (pp. 90-91): a random Fourier series with standard-normal coefficients is almost surely not in $L^2$; start from least-squares interpolation or PINN pre-training.
- **Settings** (p. 92): $m=b=1$, $\alpha_1=0.51$, prior $\alpha_0=0.1/\beta$, posterior $\alpha_0=\hat\alpha_0/\max\{\beta,\sigma^{-2}\}$. SGLD suits strictly convex energies; for multimodal posteriors use [[Cyclical SG-MCMC]], contour SGLD, or HMCECS ([[Hamiltonian Monte Carlo]] with subsampling). Prefer HMC unless unimodality is strongly suspected.
- **Nested SGLD** (Sec. 5.1.2, pp. 93-96): outer loop on $\lambda$ with the gradient of Lemma 1 written as an importance-sampled expectation (eq. 5.4, Algorithm 3). Settings: $10^6$ field warm-up steps, $T=10$ prior and $\tilde T=1$ posterior steps per outer step, $m=\tilde m=1$, $\alpha_1=0.51$. $\tilde T=1$ is justified only because the field posterior was insensitive to the calibrated parameters; it would fail if they entered the likelihood (p. 96).
- **Classical PINN is a MAP** (Sec. 5.2.1, pp. 97-98): with squared-residual energy and Gaussian noise, the information Hamiltonian equals the PINN loss when $r_d=n/(2\sigma^2)$, $r_p=\beta$ (eq. 5.5). Joint field-and-parameter MAP (eqs. 5.6-5.7) equals PINN parameter estimation only if the parameter prior is flat and $\log Z(\lambda)$ is constant.
- **B-PINN differs** (Sec. 5.2.2, pp. 99-101): the fictitious residual likelihood (eq. 5.8) gives the same field posterior $p(\theta|d,\lambda)$ as IFT only if (i) the integral uses the B-PINN collocation points, (ii) the weight prior is flat, and (iii) $\sigma_r^2=m/(2\beta)$ (eq. 5.9). B-PINN has no $Z(\lambda)$ term, so energy-parameter posteriors differ. By Bayesian asymptotics the B-PINN field posterior collapses to one function as $m\to\infty$ for any fixed $\sigma_r$ (pp. 100-101); IFT's spread stays controlled by $\beta$. See [[PINN]].

## Ch. 6 Examples (new material)

Examples 1-3 run in C++ for nested SGLD; Example 4 in NumPyro. Code: `PredictiveScienceLab/pift-paper-2023` (p. 102).

1. **Posterior collapse as trust grows** (pp. 102-104). 1D heat equation $D\phi''+q=0$, $D=1/4$, $q=e^{-x}$, $\phi(0)=1$, $\phi(1)=0.1$; Dirichlet energy (eq. 6.2); boundary conditions built into $\hat\phi$ (eq. 6.3) with a 20-term Fourier $\hat\psi$. Posterior bands shrink to the truth as $\beta$ goes $10^2\to10^5$ (Fig. 6.1).
2. **Trust tracks model-form error** (pp. 104-109). Nonlinear $D\phi''-\kappa\phi^3=f$, $D=0.1$, $\kappa=1$, $f=\cos 4x$, 40 observations, noise 0.01. Prop. 6.2.1 (pp. 105-107) proves the energy (eq. 6.6) is the right functional: first variation gives the ODE, second variation is positive by the Poincare inequality, so the minimiser is unique. Two experiments with a correctness knob $\gamma$: (a) source term mixed as $\gamma\cos 4x+(1-\gamma)e^{-x}$; (b) energy mixing the cubic term with a linear one (eq. 6.9). Jeffreys prior, sampling $\log\beta$. The $\beta$ posterior quantiles rise with $\gamma$ in both (Fig. 6.2). See [[Model-form error detection]].
3. **Inverse problem with nonlinear PDE** (pp. 109-113). Same physics, $\beta=10^5$ fixed, Jeffreys priors on $D,\kappa$ in log space. (3a) $D$ is identified tightly, $\kappa$ weakly and its marginal shifts between runs, so SGLD mixes slowly (100,000 iterations take about 1 s on an M1 Max). The *fitted prior predictive* $\int d\lambda\,p(\phi|\lambda)p(\lambda|d)$ and the posterior predictive $\int d\lambda\,p(\phi|d,\lambda)p(\lambda|d)$ are shown (pp. 110-111). (3b) The source gets a GP prior (squared exponential, variance 1, lengthscale 0.3), truncated to 10 [[Karhunen-Loève expansion]] terms (>99% of energy). With a less informative source prior, many $(D,\kappa,f)$ give identical predictives: not identifiable without observing the source. A common factor in the energy terms lets IFT move the effective $\beta$ away from nominal (p. 113).
4. **Ill-posed 2D forward problem** (pp. 113-118). Allen-Cahn $\varepsilon\nabla^2\phi-\phi(\phi^2-1)+f=0$, $\varepsilon=0.01$, on $[-1,1]^2$, energy (eq. 6.11) with several critical points. A one-parameter basis gives a bimodal prior (Fig. 6.5, $\beta=100$). Data on only 3 of 4 boundaries (15 noisy points each) leave the posterior bimodal. Fourier basis with 9 terms per dimension, HMCECS with NUTS inner kernel, minibatch 8, 100,000 samples, $\beta=50$ (high enough to enforce physics, low enough to keep the minor mode). A Gaussian-mixture split of the posterior shows one mode recovers the truth while the second, the mean and the median fail (Figs. 6.7-6.8). With very high energy barriers the chain may not jump between modes (p. 115).

## Ch. 7 Future work (pp. 119-123)

- **Rigour** (pp. 120-122): path integrals are perturbative and usually divergent, so another measure may be needed. Existence of the posterior would follow from Radon-Nikodym if the physics-informed prior is made rigorous. The prior's unnormalised density $e^{-U(\phi)}$ satisfies the Bochner-Minlos conditions, so it is the characteristic functional of some generalized random field (p. 121).
- **Dynamics** (p. 121): use an action, $p(\phi)\propto e^{-S}$ with Lagrangian $L$, or the Euclidean action, so field-theory samplers such as symplectic quantization carry over.
- **Parameterisation** (pp. 121-122): the induced finite-dimensional measure should be shown to converge to the function-space measure. Paley-Zygmund shows random Fourier series may fail to converge in $L^p$, so other bases may be better.
- **Numerics** (pp. 122-123): precondition SGLD with the Hessian of Lemma 2, which needs a third-order correction for convergence, with a proof analogous to Lemmas 1-2. Remove the nesting by approximating $Z$ via the semiclassical expansion (Laplace-like at Gaussian order, Wick corrections beyond), at the price of solving the PDE per sample.
- **Unification**: PINNs and GP regression are limiting cases of IFT; the B-PINN gap comes from dropping $Z$, which matters when $Z$ dominates the posterior (p. 123).

## Limitations

- Only a Fourier basis and SGLD are demonstrated; slow mixing is reported in Example 3 (p. 110).
- Nested sampling limits scalability (p. 122).
- Uniqueness theory needs energies linear in parameters and fails when $\beta$ is inferred jointly with a physics parameter (p. 79).
- Examples are 1D except Example 4, and the 2D case is forward-only.

## Connections
- Earlier journal version: [[PIFT (Alberts 2023)]]. Application: [[IFT thermal conductivity (Alberts 2026)]].
- Wiki note: the beta behaviour in Example 2 is the same empirical-Bayes logic as marginal-likelihood hyperparameter fitting in a [[Gaussian process]], with $\beta$ as an amplitude.

%% refs:start %%
**Cites in this wiki**: [[Adam paper (Kingma 2015)]], [[Cardiac activation PINN (Sahli Costabal 2020)]], [[Cardiovascular flow PINNs (Kissas 2020)]], [[Cyclical SG-MCMC (Zhang 2020)]], [[DeepONet (Lu 2021)]], [[PIFT (Alberts 2023)]], [[PINNs (Raissi 2019)]], [[RMHMC (Girolami 2011)]], [[SGLD (Welling 2011)]], [[SINDy (Brunton 2016)]], [[VAE paper (Kingma 2014)]]
**Cited by in this wiki**: [[IFT thermal conductivity (Alberts 2026)]]
**Software cited**: [[software#NumPyro|NumPyro]]
%% refs:end %%

**Sources**: `papers/IFT/Alberts - An Information Field Theory Approach to Engineering Inverse Problems.pdf`.
**Last updated**: 2026-11-07

---

## Related pages
- [[Information field theory]]
- [[Physics-informed prior]]
- [[Generalized random fields]]
- [[Operator calculus for free theory]]
- [[Model-form error detection]]
- [[MAP uniqueness in IFT (Alberts 2025)]]
- [[PIFT (Alberts 2023)]]
- [[IFT thermal conductivity (Alberts 2026)]]
- [[Nested SGLD]]
- [[SGLD]]
- [[PINN]]
- [[Karhunen-Loève expansion]]
- [[Bayesian inverse problems]]
- [[Identifiability]]
