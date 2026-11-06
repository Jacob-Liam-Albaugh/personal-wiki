---
type: concept
area: bayesian
areas: [bayesian, me697]
source-ref: "ME 697 book, inverse/hbayes 01-02"
tags: [bayesian, inverse-problems, uq, mcmc]
---

# Hierarchical Bayesian model

**Summary**: A model in which each individual's parameters are drawn from a population distribution whose own parameters get a prior. Many related inverse problems are solved together, and the population level is learned from all of them.

**Sources**: `advanced-scientific-machine-learning/book/inverse/hbayes/intro.md`, `02_hbayes_example.ipynb`.
**Last updated**: 2026-11-06

---

## Structure (source: hbayes/02)
Population parameters $\theta_{pop}$ have a prior. Individual parameters follow
$$\theta_i\sim p(\theta_i|\theta_{pop}),\quad i=1..N.$$
Each individual's data follow
$$y_i\sim p(y_i|\theta_i).$$
The implied population distribution of the physical parameters is
$$p(\theta)=\int p(\theta|\theta_{pop})\,p(\theta_{pop})\,d\theta_{pop}.$$

> [!example] Cars on a bumpy road
> Each car is a damped oscillator $\ddot x+2\zeta\dot x+\omega^2x=0$ with an analytic solution. Conditional priors on $(\zeta_i,\omega_i)$ are lognormal given $(\mu_\zeta,\tau_\zeta,\mu_\omega,\tau_\omega)$. After sampling with [[NUTS]], the book predicts for a new car the probability of crossing a displacement threshold on a new bump.

## Practical points
- The hbayes intro says the hierarchical view "represents how data and model relate" (source: hbayes/intro.md).
- The notebook gives both centered and non-centered parameterizations of the individual parameters.
- Wiki note: hbayes/01 ("TODO: Write me.") and hbayes/03 ("bad posterior geometry", title only) are empty, so the book does not yet explain when each parameterization is preferred. Text and code in hbayes/02 disagree on several numbers; see [[ME697 4.4 - Hierarchical Bayes]].

## Amortized variant
[[Amortized VI]] with a network guide $q_\phi(\xi|y)$ shares one guide across datasets, an alternative way to reuse structure across problems (hbayes/04).

## Related pages
- [[Bayesian inverse problems]] · [[Markov chain Monte Carlo]] · [[Identifiability]]
- [[ME697 4.4 - Hierarchical Bayes]] · [[Gaussian process]]
