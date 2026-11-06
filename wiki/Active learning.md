---
type: concept
area: me697
areas: [me697, gp]
tags: [uq, gp, ml, bayesian]
---

# Active learning

**Summary**: Training a model on data it chooses itself. Start from a few labeled points, score every candidate input with an acquisition function, evaluate the best one, update, repeat. In surrogate modeling it cuts the number of expensive simulations or experiments.

---

## Definition
> [!definition] Acquisition-driven loop
> Given the posterior $p(f\mid\mathcal D_t)$, choose
> $$\mathbf x_{t+1}=\arg\max_{\mathbf x}\alpha_t(\mathbf x)$$
> query the true function, add the pair to $\mathcal D_t$, re-condition. Stop when the best $\alpha_t$ falls below a threshold or the budget runs out.
> (source: ME 697 book, `up/al/01_al_basics.md`)

## Acquisition functions
- **Uncertainty sampling**: expected information gain (MacKay 1992), approximately proportional to the predictive variance $\sigma_t^2(\mathbf x)$ over the noise variance. Pushes samples to the domain boundary.
- **Value of information**: expected utility $\mathbb E[v_t(y)-c_t(\mathbf x)]$; expected improvement is a special case.
- **Multi-fidelity**: acquisition $\alpha_t(s,\mathbf x)$ also picks a fidelity $s$ and balances information against cost.
- **Multi-objective**: hypervolume improvement.

## Notes
- Needs a model with a usable predictive uncertainty: [[Gaussian process]] (closed form), generalized linear models, or neural networks with a Laplace approximation or samples.
- Candidate points are found by random or space-filling search ([[Latin hypercube sampling]]) when the argmax is not analytic.
- Wiki note: the information gain in the book is the small-variance form of $\tfrac12\log(1+\sigma_t^2/\sigma^2)$; the argmax is the same. See [[ME697 2.5 - Active learning]].

**Sources**: ME 697 book `up/al/` (see [[ME697 2.5 - Active learning]]).
**Last updated**: 2026-11-06

---

## Related pages
- [[ME697 2.5 - Active learning]] · [[ME697 2.4 - Multi-fidelity modeling]]
- [[Surrogate model]] · [[Multi-fidelity modeling]] · [[Gaussian process]] · [[KL divergence]]
