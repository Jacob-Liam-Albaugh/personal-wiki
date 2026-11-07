---
type: paper
area: ift
areas: [ift, inverse-problems, physics-informed]
source-ref: "Alberts & Bilionis 2025, arXiv 2401.14224v3 [math-ph]"
tags: [ift, bayesian, inverse-problems, physics-informed, gp, pde, uq]
year: 2025
venue: "arXiv 2401.14224v3"
file: "papers/IFT/Alberts, Bilionis - Uniqueness of MAP estimates for inverse problems under information field theory.pdf"
---

# Uniqueness of MAP estimates for inverse problems under IFT (Alberts 2025)

**Summary**: For an [[Information field theory]] inverse problem with a [[Physics-informed prior]] $p(\phi|\lambda)\propto e^{-\beta E(\phi;u)}$, the field is integrated out and the question is whether the parameter posterior $p(\lambda|d)$ has a unique mode. The paper calls this *weakly well-posed*. The gradient and Hessian of $-\log p(\lambda|d)$ are written as prior-vs-posterior field expectations and covariances, so the partition function $Z(\lambda)$ never has to be computed. The main theorem: if the field potential is linear in $\lambda$, the parameter prior is flat and the data are *informative*, then any stationary point is the unique MAP. A Poisson example shows the inferred model trust $\beta^*$ is infinite for a correct model and finite, growing as the model improves, under model-form error.

**Authors**: Alex Alberts, Ilias Bilionis (Purdue ME) · **Year**: 2025 (v1 2024) · **File**: `papers/IFT/Alberts, Bilionis - Uniqueness of MAP estimates for inverse problems under information field theory.pdf`

---

## Setting

- Prior (eq. 2.3): $p(\phi|u,\beta)=e^{-H(\phi;u,\beta)}/Z(u,\beta)$ with $H=\beta E(\phi;u)$ and $E$ a local field energy (eq. 2.2). $\beta$ is the **model trust**: $\beta\to\infty$ collapses onto the energy minimiser, $\beta\to0$ gives a flat prior (p. 5).
- Data: $d=R\phi+\gamma$, $\gamma\sim\mathcal N(0,\Gamma)$ (eq. 2.5). Parameters $\lambda=(u,\beta)$ with prior potential $H(\lambda)=-\log p(\lambda)$.
- Joint potential (eq. 2.6):
$$H(\phi,\lambda;d)=H(d;\phi)+H(\phi;\lambda)$$
$$\quad-\log Z(\lambda)+H(\lambda)$$
- **Free theory** (Def. 2.1): $p(\phi|\lambda)=\mathcal N(0,S_\lambda)$, so the posterior is Gaussian with
$$\tilde S_\lambda=(S_\lambda^{-1}+R^*\Gamma^{-1}R)^{-1}$$
$$\tilde m_\lambda=\tilde S_\lambda R^*\Gamma^{-1}d$$

## Results

> [!definition] Weakly well-posed (Def. 3.1, p. 8)
> The parameter posterior potential $H(\lambda;d)=-\log p(\lambda|d)$ has a unique minimum, i.e. $p(\lambda|d)$ is unimodal. Weaker than Hadamard and than Bayesian (Hellinger) well-posedness; unlike [[Identifiability]] it needs neither infinite data nor a correct model (Remark 3.1).

> [!theorem] Gradient (Lemma 3.1, p. 9; from Alberts 2023)
> $$\nabla_\lambda H(\lambda;d)=\mathbb E[\nabla_\lambda H(\phi;\lambda)|d,\lambda]$$
> $$\quad-\mathbb E[\nabla_\lambda H(\phi;\lambda)|\lambda]+\nabla_\lambda H(\lambda)$$
> The $Z(\lambda)$ term becomes the prior expectation via $\partial_i\log Z=-\mathbb E[\partial_i H|\lambda]$ (eq. 3.3).

> [!theorem] Hessian (Lemma 3.2, eq. 3.4; proof App. A)
> With $g=\nabla_\lambda H(\phi;\lambda)$:
> $$\nabla^2_\lambda H(\lambda;d)=C[g|\lambda]-C[g|d,\lambda]$$
> $$\quad-\mathbb E[\nabla^2_\lambda H(\phi;\lambda)|\lambda]$$
> $$\quad+\mathbb E[\nabla^2_\lambda H(\phi;\lambda)|d,\lambda]+\nabla^2_\lambda H(\lambda)$$
> All terms are field expectations, so they could be estimated from SGLD samples, e.g. as a preconditioner (p. 10).

> [!definition] Informative data (Def. 3.5, p. 11)
> For all $d$ in the data density's support and all $\lambda$ in the prior's support:
> $$C[g|\lambda]-C[g|d,\lambda]\succ0$$

- **Lemma 3.3** (free theory, via the operator calculus of Leike & Enßlin 2016, App. B): closed forms for both covariances as traces of $\nabla_\lambda S_\lambda^{-1}S_\lambda\nabla_\lambda S_\lambda^{-1}S_\lambda$, plus a $\tilde m^\dagger(\cdot)\tilde m$ term for the posterior.
- **Prop. 3.2**: under free theory, if the posterior covariance kernel vanishes as $n\to\infty$, the data are informative given enough data. Teckentrup's (2020) GP convergence theorems (Thms. 3.1–3.2) supply sufficient conditions: space-filling design, true field in a high enough Sobolev space, and a prior [[RKHS]] isomorphic to a Sobolev space. Green's-function kernels of many PDEs satisfy the last (Fasshauer & Ye 2011, p. 14).

> [!theorem] Main result (Thm. 3.3, p. 14)
> If $H(\phi;\lambda)=\sum_i\lambda_iF_i(\phi)$ (linear in $\lambda$, $F_i$ may be nonlinear in $\phi$), $p(\lambda)$ is constant, the data are informative, and $\nabla_\lambda H(\lambda^*;d)=0$ has a root, then $\lambda^*$ is the unique MAP.
>
> Proof: the three expectation-of-Hessian terms in Lemma 3.2 vanish, leaving a positive definite covariance difference, so $H(\lambda;d)$ is strictly convex (Prop. 3.1).

Holds outside free theory, but informativeness is then hard to check. Linearity covers variational energies of heat, wave, linear elasticity and Allen–Cahn. It **fails** for squared-residual energies with several parameters, and whenever $\beta$ is inferred jointly with a physical parameter (e.g. heat equation: $\beta$ times conductivity) (p. 15).

## Example: model-form error for Poisson (Sec. 4)

Prior from Dirichlet's principle, $E(\phi)=\tfrac12(\nabla\phi)^\dagger\nabla\phi-q^\dagger\phi$, gives a GP:
$$p(\phi|\beta)=\mathcal N(Gq,\ \beta^{-1}G)$$
with $G=L^{-1}$ the Green's function of $-\nabla^2$ (Dirichlet BCs). Only $\beta$ is inferred, flat prior, so Thm. 3.3 applies. The stationarity condition says the optimal $\beta$ equalises expected prior and posterior energies (eq. 4.2). As $n\to\infty$ (eq. 4.4):
$$\beta^{*-1}=\frac{(\phi^*-Gq)^\dagger L(\phi^*-Gq)}{\mathrm{tr}(I)}$$

- Correct model ($\phi^*=Gq$): no finite root, $\beta^*=\infty$, so solve the PDE.
- Model-form error: $\beta^*$ finite and positive, larger the closer the physics is to the truth.
- $\mathrm{tr}(I)$ is the dimension of the truncated (renormalised) field space, so finer discretisations raise $\beta^*$.
- **Jeffreys prior** $p(\beta)\propto1/\beta$: Thm. 3.3 no longer applies; with $\mathrm{tr}(I)-2$ in the denominator instead, and curvature $\tfrac12\beta^{*-2}(\mathrm{tr}(I)-1)$, the problem is weakly well-posed iff $\mathrm{tr}(I)>2$ (p. 19).

## Limitations (Sec. 5)
- Most GP kernels (e.g. Matérn) are nonlinear in their hyperparameters, so only Prop. 3.1 applies.
- Vanishing posterior covariance is assumed, which does not hold for general GP priors.
- Squared-residual energies and joint $(\beta,u)$ inference are left open.

## Connections
- Lemma 3.1 is the gradient used by the nested SGLD sampler in [[PIFT (Alberts 2023)]]; this paper adds the Hessian and the uniqueness theory.
- Chapter 4 of [[IFT for engineering inverse problems (Alberts 2024)]] restates these results.
- Wiki note: under free theory with a flat trust prior this is type-II maximum likelihood for one GP scale parameter; the $\mathrm{tr}(I)$ dependence is the usual "number of effective modes" in evidence maximisation for [[Gaussian process]] amplitude.
- Wiki note: compare the Bayesian well-posedness framework in [[Bayesian inverse problems]], which this deliberately weakens to MAP uniqueness.

%% refs:start %%
**Cites in this wiki**: [[PIFT (Alberts 2023)]], [[PINNs (Raissi 2019)]], [[Physics-informed ML review (Karniadakis 2021)]]
%% refs:end %%

**Sources**: `papers/IFT/Alberts, Bilionis - Uniqueness of MAP estimates for inverse problems under information field theory.pdf`.
**Last updated**: 2026-11-07

---

## Related pages
- [[Information field theory]]
- [[Physics-informed prior]]
- [[PIFT (Alberts 2023)]]
- [[IFT for engineering inverse problems (Alberts 2024)]]
- [[IFT thermal conductivity (Alberts 2026)]]
- [[Identifiability]]
- [[Bayesian inverse problems]]
- [[Gaussian process]]
- [[RKHS]]
- [[Poisson and Laplace equations]]
- [[SGLD]]
