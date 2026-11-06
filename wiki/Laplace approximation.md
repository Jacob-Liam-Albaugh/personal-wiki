---
type: method
area: bayesian
areas: [bayesian, me697]
source-ref: "ME 697 book, inverse/basics 04-05"
tags: [bayesian, inverse-problems, uq, optimization]
---

# Laplace approximation

> [!algorithm] Laplace approximation
> 1. Find the mode $x_0=\arg\max_x\log p(x|y)$.
> 2. Evaluate the Hessian of $\log p$ at $x_0$.
> 3. Approximate the posterior by
> $$p(x|y)\approx\mathcal N\big(x_0,\,\Sigma\big),$$
> $$\Sigma=-\big(\nabla^2\log p(x_0|y)\big)^{-1}.$$
>
> (source: `inverse/basics/04_laplace_approximation_gen.ipynb`)

**Intuition**: Expand $\log p$ to second order around its peak. A quadratic log density is a Gaussian, so the posterior becomes a Gaussian whose curvature is the Hessian. It costs one optimization and one Hessian, far less than [[Markov chain Monte Carlo]] or [[Variational inference]], and is exact if the posterior is Gaussian.

## Inverse problem with Gaussian noise
For $y=f(x)+\text{noise}$ with variance $\sigma^2$ and prior $\mathcal N(0,\gamma^2I)$, the negative-log-posterior Hessian is
$$\frac1{\sigma^2}J^TJ-\frac1{\sigma^2}\sum_i(y_i-f_i)\nabla^2f_i+\frac1{\gamma^2}I.$$
$J$ is the Jacobian of $f$ at $x_0$. The second term is often dropped (Gauss-Newton) when residuals are small. **[unverified]** whether the book drops it; the notebook computes the full Hessian.

## Estimating the noise level
Put a Jeffreys prior $p(\sigma)\propto1/\sigma$ on $\sigma$. With $\theta=\log\sigma$ the prior is flat, so $(x,\theta)$ gets a joint Laplace approximation. The mixed second derivative with respect to $x_j$ and $\theta$ involves $e^{-2\theta}\sum_i(y_i-f_i)\partial f_i/\partial x_j$ (source: `basics/05_laplace_example.ipynb`).

> [!example] Catalysis
> $\sigma=5$, $\gamma=10$, 300 Adam iterations to the mode, Hessian by finite differences because diffrax is awkward to differentiate twice. See [[Catalysis problem]].

> [!example] 1D check
> A Gamma(10) density approximated at its mode, to check the formula.

## Failure modes
- Only captures one mode; multimodal or [[Identifiability|non-identifiable]] posteriors (flat ridges) give a singular or misleading Hessian.
- Wiki note: the book's text gives the sign of the $x$-$\theta$ mixed derivative of the log posterior as $+2e^{-2\theta}\cdots$; for $L=\log p$ it is negative, and $+$ is correct for $-L$, which the code uses. See [[Bayesian inverse problems]].
- Wiki note, basics/05 code: `var_post_sigma` uses the fixed-noise covariance, not the noise-augmented one; it prints "variance" but computes a standard deviation; samples use `mu`, not `mu_noise`. The text says $x\in\mathbb R^5$ but the code vectors have 6 entries.
- Wiki note, basics/04: the Jacobian definition repeats $\partial/\partial x_1$ at its end, the Taylor term has a typo `(x-x_{0j})`, and `find_minimum` overwrites `status`, so "converged" is never reported.

## Where it appears
- [[Bayesian inverse problems]]: derivation and catalysis example.
- [[Variational inference]]: the same problem solved by a full-rank Gaussian guide, a natural comparison.

**Covered in**: ASML book inverse/basics (ME 697 4.1)
**Sources**: `courses/ME 697/advanced-scientific-machine-learning/book/inverse/basics/04_laplace_approximation_gen.ipynb`, `05_laplace_example.ipynb`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Bayesian inverse problems]] · [[Variational inference]] · [[Markov chain Monte Carlo]] · [[Catalysis problem]]
- [[Newton's method]] · [[Automatic differentiation]] · [[KL divergence]]
