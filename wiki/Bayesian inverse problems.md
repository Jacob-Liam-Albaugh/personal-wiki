---
type: concept
area: bayesian
source-ref: "Tsilifis et al. 2014, eqs. 1-6; Karumuri et al. 2024, §2.1"
tags: [bayesian, inverse-problems]
---

# Bayesian inverse problems

**Summary**: infer the unknown inputs $\xi$ of a forward model $f$ from noisy data $y$ by computing a posterior, rather than a single best fit.

## Where it appears
- Book treatment in five steps: classical least squares, Bayesian posterior, [[Laplace approximation]], sampling, VI. (source: `inverse/basics/03_bayesian_formulation.md`)
- The book calls the Bayesian formulation the "gold standard": the solution is a distribution, always exists, is unique, quantifies uncertainty, and is conditional on the model being correct. (source: `inverse/basics/03_bayesian_formulation.md`)
- Worked examples: [[Catalysis problem]], [[Duffing oscillator]], [[Identifiability]], [[Hierarchical Bayesian model]]; samplers [[Markov chain Monte Carlo]], [[Hamiltonian Monte Carlo]], [[NUTS]].
- Prior view of regularization: an L1 penalty is the negative log posterior under a Laplace prior, see [[LASSO]]. (source: `inverse/data/01_lasso.ipynb`)
- [[EWARS leak estimation (Rautela 2023)]]: deterministic leak-area inversion by adaptive search, no UQ.
- [[Embedded model bias with noise (Andres Arcones 2025)]]: when the forward model is wrong, embeds the error in the parameters so the posterior does not collapse and can be pushed to unobserved QoIs ([[Embedded model inadequacy]]).

**Covered in**: ASML book inverse/basics (ME 697 4.1); ASML book inverse/pdes (ME 697 4.6); Enßlin IT & IFT ch. 2 (pp. 33-41)
**Sources**: `papers/Bayesian/Bilionis, Tsilifis - Variational Reformulation of Bayesian Inverse Problems.pdf`, `papers/Bayesian/Bilionis, Karumuri - Learning to solve Baysian inverse problems An Amortizeed Variational Inferece approach useing Gaussian and Flow guides.pdf`, `text_books/Machine Learning & Statistics/advanced-scientific-machine-learning/book/inverse/intro.md`, `inverse/basics/intro.md`, `01_classic_formulation.md`, `02_classic_example.ipynb`, `03_bayesian_formulation.md`, `04_laplace_approximation_gen.ipynb`, `05_laplace_example.ipynb`, `text_books/Machine Learning & Statistics/advanced-scientific-machine-learning/book/inverse/pdes/intro.md`, `01_reading.md`, `02_thermal.ipynb`, `03_contamination.ipynb`, `papers/Bayesian/Andres Arcones, Weiser, Koutsourelakis, Unger - Embedded Model Bias Quantification with Measurement Noise for Bayesian Model Calibration.pdf`, `text_books/Machine Learning & Statistics/Ensslin - Information Theory & Information Field Theory.pdf`.
**Last updated**: 2026-11-21

---

## Setup
Likelihood through the forward model (Tsilifis eqs. 1-2), with noise scale $\theta$:
$$p(y\mid\xi,\theta)=N\big(y\mid f(\xi),e^{2\theta}I\big)$$
Posterior over $\omega=(\xi,\theta)$ (eq. 6):
$$p(\omega\mid y)=\frac{p(y\mid\omega)\,p(\omega)}{p(y)}$$
Karumuri fixes the noise: $p(y\mid\xi)=N(y\mid f(\xi),\gamma^2I)$.

## Ways to solve it
- MAP and Laplace: cheap but crude summaries (both lab papers).
- MCMC: the costly gold standard; Karumuri compares against NUTS via KS statistics.
- [[Variational inference]] per dataset (Tsilifis) or [[Amortized VI]] across datasets (Karumuri).
- Field-valued unknowns: [[Information field theory]] and [[Physics-informed prior]].

## Estimators from decision theory (Enßlin)
Which point estimate to report from a posterior depends on the loss: quadratic gives the mean, absolute the median, delta the MAP (source: Ensslin - Information Theory & Information Field Theory.pdf, §2.3, eqs. 77-94, pp. 38-39; PDF page). See [[Bayesian decision theory]], [[Bayesian inference]].

## Related pages
- [[MAP uniqueness in IFT (Alberts 2025)]]
- [[IFT for engineering inverse problems (Alberts 2024)]]
- [[Variational inverse problems (Tsilifis 2014)]] · [[Amortized VI for inverse problems (Karumuri 2024)]] · [[PIFT (Alberts 2023)]] · [[Karhunen-Loève expansion]]
- [[Bayesian decision theory]] · [[Bayesian inference]]
