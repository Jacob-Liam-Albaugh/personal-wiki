---
type: concept
area: bayesian
areas: [bayesian, me697]
source-ref: "ME 697 book, inverse/odes 02; inverse/hbayes 04"
tags: [inverse-problems, bayesian, uq, mcmc]
---

# Identifiability

**Summary**: Parameters are identifiable when the data determine them uniquely (for infinite data). If only a combination is determined, the likelihood is flat along other directions and the posterior is a ridge governed by the prior.

**Sources**: `advanced-scientific-machine-learning/book/inverse/odes/02_identifiability.ipynb`, `hbayes/04_amortized_vi.ipynb`.
**Last updated**: 2026-11-06

---

## Harmonic oscillator example (source: odes/02)
The model
$$m\ddot x=-kx$$
has oscillating solutions in $\cos(\sqrt{k/m}\,t)$ (the book's stated form), so the data depend on $m$ and $k$ only through
$$\omega^2=k/m.$$
Truth $m=k=1.5$, noise $0.05$, 50 observations. Priors $m\sim U(1,2)$, $k\sim U(0.5,3)$.
- NUTS traces of $m$ and $k$ look like random walks.
- The joint posterior is a band along the line $m=k$.
- Reparameterizing with $\omega^2$ gives an identifiable problem.

Wiki note: the book writes $m\ddot x=kx$, whose solutions are exponentials, not cosines; the sign is a typo.

## Inverse kinematics (source: hbayes/04)
The text discusses non-identifiability of the joint angles given the end position, mode seeking by VI, and the variational versus amortization gap. Wiki note: a redundant arm generally has several joint configurations for one end position, so the posterior can be multimodal. **[unverified]**

## Consequences
- Sampling: slow mixing, large ESS loss; see [[NUTS]].
- Laplace: singular Hessian along the flat direction; see [[Laplace approximation]].
- VI: a Gaussian guide cannot represent a curved ridge or multiple modes; see [[Variational inference]].
- Check by plotting the pairwise posterior, or reparameterize in the identifiable combination.

## Related pages
- [[Bayesian inverse problems]] · [[ME697 4.5 - ODE inverse problems]] · [[ME697 4.4 - Hierarchical Bayes]]
- [[Sensitivity analysis]] · [[Hierarchical Bayesian model]]
