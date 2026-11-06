---
type: method
area: bayesian
areas: [bayesian, stochastic, me697]
source-ref: "ME 697 book, sinverse/cali/04_pmcmc_example.ipynb (03_pmcmc_theory.md is headings only)"
tags: [mcmc, inverse-problems, bayesian, sampling]
---

# Particle MCMC

[[Markov chain Monte Carlo]] over the parameters $\theta$ of a [[Stochastic state-space model]], where the intractable likelihood $p_\theta(y_{1:T})$ is replaced by a [[Particle filter]] estimate $\hat Z$.

> [!algorithm] Particle marginal Metropolis-Hastings (source: sinverse/cali/04_pmcmc_example.ipynb)
> At iteration $i$:
> 1. Propose $\theta'\sim q(\cdot\mid\theta^{(i-1)})$.
> 2. Run a particle filter at $\theta'$ to get $\hat Z'$.
> 3. Accept with probability

$$
\alpha = \min\Big(1,\ 
\frac{\hat Z'\,p(\theta')\,q(\theta^{(i-1)}\mid\theta')}
{\hat Z^{(i-1)}\,p(\theta^{(i-1)})\,q(\theta'\mid\theta^{(i-1)})}\Big).
$$

> 4. If accepted store $(\theta',\hat Z')$, otherwise keep the old pair and its old $\hat Z$.

Reusing the stored $\hat Z$ is what keeps the chain exact when $\hat Z$ is unbiased **[unverified: standard result, not stated in the source]**. See [[Metropolis-Hastings correction]].

> [!example] Duffing oscillator
> Flat prior, start $\alpha_0=-1.5$, $\beta_0=1.5$, $\delta_0=0.5$, $s_0=1.0$. 1000 particles, proposal scale 0.01, 10,000 iterations, 381.48 s. "Not amazing, but the true parameters are in the range of the posterior." Far more expensive than [[Expectation-maximization]]. The notebook asks whether the system is [[Identifiability|identifiable]] (source: 04_pmcmc_example.ipynb).

## Notes
- Gives a posterior, so it can reveal weak identifiability (wide or ridge-shaped marginals); the notebook asks "Do you think this system is identifiable?" See [[Identifiability]].
- Cost per iteration is a full particle filter run.

**Wiki note**: in the notebook the code passes `s_0` in the control slot of `Duffing(...)`, and the markdown ratio has a stray parenthesis and no hat on $Z'$.

**Covered in**: ASML book sinverse/cali (ME 697 6.3)
**Sources**: `courses/ME 697/advanced-scientific-machine-learning/book/sinverse/cali/04_pmcmc_example.ipynb`, `03_pmcmc_theory.md`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Expectation-maximization]] · [[Particle filter]] · [[Markov chain Monte Carlo]]
- [[Metropolis-Hastings correction]] · [[Stochastic state-space model]] · [[Bayesian inverse problems]]
