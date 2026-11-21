---
type: concept
area: ift
areas: [ift, bayesian]
tags: [ift, bayesian]
source-ref: "Alberts & Bilionis 2023, eqs. 2-11, 18, pp. 4-7"
---

# Information field theory

**Summary**: Bayesian inference over fields, written as path integrals. A quadratic action gives a closed-form free theory equal to Wiener filtering / GP regression; physics enters through the prior energy.

**Covered in**: ASML book ift/calibration (ME 697 IFT.1); ASML book ift/fields (ME 697 IFT.2); Eastman statmech ch. 2, 4, 6 (background for the dictionary); Enßlin IT & IFT ch. 5-17 (pp. 77-184, PDF pages)
**Sources**: `papers/IFT/Bilionis, Alberts - IFT.pdf`, `papers/IFT/Bilionis, Alberts - IFT Thermal Conductivity.pdf`, `text_books/Machine Learning & Statistics/advanced-scientific-machine-learning/book/ift/intro.md`, `ift/calibration/intro.md`, `text_books/Machine Learning & Statistics/advanced-scientific-machine-learning/book/ift/intro.md`, `ift/fields/intro.md`, `text_books/Machine Learning & Statistics/Ensslin - Information Theory & Information Field Theory.pdf`.
**Last updated**: 2026-11-21

---

## Free theory
> [!definition] Gaussian field and generating functional (eqs. 2-6, p. 4)
> $$p(\phi)\propto e^{-\frac12\phi^\dagger S\phi},\qquad Z[q]=\int\mathcal D\phi\,e^{-\frac12\phi^\dagger S\phi+\phi^\dagger q}=C\det(S)^{-1/2}e^{\frac12q^\dagger S^{-1}q}$$
> so $\mathbb E[\phi]=0$, $\mathrm{Cov}[\phi]=S^{-1}$.

> [!theorem] Posterior of the free theory (eqs. 8-11, pp. 5-6)
> With data $d=R\phi+n$, $n\sim\mathcal N(0,N)$:
> $$\tilde S=S+R^\dagger N^{-1}R,\quad \tilde m=\tilde S^{-1}R^\dagger N^{-1}d=S^{-1}R^\dagger K^{-1}d,\quad K=N+RS^{-1}R^\dagger.$$
> With Dirac measurement functionals $R$ this is GP regression.

## Fields beyond Gaussian processes
The book's takeaway (ift/fields) is that Feynman path integrals give a formal generalization of Gaussian processes (Wiki note on the reading). A [[Gaussian process]] is a Gaussian measure on functions, equivalently a field with quadratic energy. Allowing a non-quadratic energy, the prior over a field $u$ is written as a path integral

$$
p[u] \propto e^{-H[u]},
$$

and the normalizing integral is the partition function. [[Brownian motion]] is the simplest field with a path-integral (Wiener measure) description.

## Information Hamiltonian
> [!definition] (p. 6; eq. 18, p. 7)
> $H[\phi|d]=-\log p(\phi|d)$ up to a constant. Gaussian case: $\tfrac12[\phi^\dagger S\phi+(R\phi-d)^\top N^{-1}(R\phi-d)]$. General: $H[\phi|d]=\ell(d,R\phi)+\beta U[\phi]$.

## Statistical-mechanics dictionary
Wiki note: IFT borrows its language from statistical mechanics at kT = 1. Physics side from Eastman's book; the identifications are standard but **[unverified]** against an IFT source.

| Stat mech | IFT / Bayes |
|---|---|
| energy E(s) | information Hamiltonian H[φ\|d] |
| [[Boltzmann distribution]] exp(−βE)/Z | posterior exp(−H)/Z |
| [[Partition function]] Z | evidence p(d) |
| log Z derivatives = averages | generating functional Z[q], cumulants |
| [[Free energy]] −kT log Z | −log evidence; variational free energy = −ELBO |
| [[Mean-field theory]] | mean-field VI |
| temperature T | tempering, β ≠ 1 |
| [[Phase transition]], metastability | multimodal posteriors, poor mixing ([[Ergodicity]]) |
| [[Fluctuation-dissipation theorem]] | Langevin sampler noise scale ([[SGLD]]) |
| [[Liouville's theorem]] | HMC volume preservation |

## Enßlin's lecture notes
Enßlin's book builds IFT from probability theory up; its content is held on the topic pages below (source: Ensslin - Information Theory & Information Field Theory.pdf, ch. 5-17, PDF pp. 77-184).

Notation: Enßlin writes $S$, $N$, $D$ for the prior, noise and posterior **covariances**, so $D^{-1}=S^{-1}+R^\dagger N^{-1}R$, $j=R^\dagger N^{-1}d$, $m=Dj$; this page (after Alberts & Bilionis) uses $S$ as a precision. Enßlin's $H(d,s)=-\ln P(d,s)$ is the joint, and his $\beta=1/T$ tempers the whole Hamiltonian, while the $\beta$ above multiplies only the physics energy $U$.

- Foundations: [[Information Hamiltonian]] · [[Signal response]] · [[Wiener filter]] · [[Wiener-Khinchin theorem]] · [[Free theory (IFT)]]
- Non-Gaussian problems: [[Lognormal Poisson model]] · [[Interacting information field theory]] (Feynman diagrams; MAP is tree level) · [[Gibbs free energy]] (thermodynamical inference)
- Unknown spectra and dynamics: [[Critical filter]] · [[Power spectrum estimation]] · [[Correlated field model]] · [[Information field dynamics]]
- Numerics: [[Conjugate gradient]] · [[Metric Gaussian variational inference]] · [[Geometric variational inference]]
- Probability background from Part I: [[Cox's theorem]] · [[Bayesian inference]] · [[Bayesian decision theory]] · [[Achieved information gain]] · [[Fisher information]] · [[Maximum entropy principle]] · [[Multivariate Gaussian]]

The stat-mech dictionary above is used explicitly in the book: evidence as partition function (ch. 5, 11), $G=\mathrm{KL}-\ln P(d)$ at $T=1$ (ch. 12).

## Physics-informed IFT
- Prior from a PDE energy: [[Physics-informed prior]].
- Sampling: [[SGLD]]; hyperparameters by [[Nested SGLD]].
- PINNs as a limit: [[PINN]].
- The book's `ift/` folder gives takeaways only: held here and on [[Physics-informed prior]] (source: ift/*/).

## Where it appears
- [[PIFT (Alberts 2023)]] — develops PIFT.
- [[IFT thermal conductivity (Alberts 2026)]] — applies it to temperature-dependent conductivity.
- [[IFT for engineering inverse problems (Alberts 2024)]] — dissertation: adds function-space background, full free-theory proofs and operator calculus (Chs. 2-3, pp. 12-58). Note: its Sec. 3.1 uses $S$ as covariance in the Gaussian density, unlike the precision convention above (pp. 37-44).
- [[Generative priors for turbulence (Wang 2026)]] — Wiki note: generative priors play the role a physics prior plays here; the paper does not mention IFT.
- ME 697 book, `ift/`: three takeaway-only sub-chapters (calibration, fields, physics); no derivations or code beyond headings (source: ift/).
- [[IFT state and parameter estimation (Hao 2024)]] — extends PIFT to ODE initial-value problems with stochastic VI.
- [[Neural information field filter (Hao 2025)]] — neural path parameterizations; NSVI and NPSGLD.
- [[IFT for UQ of differential equations (Hao 2024)]] — Hao's dissertation: noisy inputs, 1D BVPs, analytic GP prior.

## Related pages
- [[MAP uniqueness in IFT (Alberts 2025)]]
- [[IFT for engineering inverse problems (Alberts 2024)]] · [[Operator calculus for free theory]] · [[Generalized random fields]]
- [[Karhunen-Loève expansion]] · [[SGLD (Welling 2011)]]
- Wiki note: the Riemannian metric in RMHMC (Fisher plus prior curvature) is a natural preconditioner for field posteriors. Link [[Riemannian manifold HMC]]. No source cite.
