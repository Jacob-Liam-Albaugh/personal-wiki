---
type: paper
area: stochastic
areas: [stochastic, bayesian]
source-ref: "Chopin, Jacob, Papaspiliopoulos 2013, JRSS-B 75(3):397-426, secs. 2-5"
tags: [sampling, mcmc, bayesian, inverse-problems]
authors: ["[[Nicolas Chopin]]", "[[Pierre E. Jacob]]", "[[Omiros Papaspiliopoulos]]"]
year: 2013
venue: "Journal of the Royal Statistical Society Series B 75(3)"
file: "[[papers/Stochastic Methods/Chopin, Jacob, Papaspiliopoulos - SMC2 An efficient algorithm for sequential analysis of state space models.pdf]]"
---

# SMC² (Chopin 2013)

**Summary**: Sequential Bayesian inference for both the parameters and the hidden states of a state-space model. An outer sequential Monte Carlo runs over parameters; each parameter particle carries its own [[Particle filter]] over states, whose likelihood estimate is unbiased. Rejuvenation uses a particle marginal Metropolis-Hastings move from [[Particle MCMC]], so the method is exact for any number of state particles. The model evidence comes for free.

**Authors**: Nicolas Chopin, Pierre E. Jacob, Omiros Papaspiliopoulos · **Year**: 2013 (received 2011) · **File**: [[papers/Stochastic Methods/Chopin, Jacob, Papaspiliopoulos - SMC2 An efficient algorithm for sequential analysis of state space models.pdf]]

---

## Problem (Sec. 1-2)
- Target, updated at each new observation:
```
p(theta, x_{1:t} | y_{1:t})
p(y_{1:t})   (evidence)
```
- IBIS (Chopin 2002) does SMC in $\theta$, reweighting by $p(y_t\mid y_{1:t-1},\theta)$. For a [[Stochastic state-space model]] that increment is intractable.

## Method

> [!algorithm] SMC² (Sec. 3)
> - $N_\theta$ parameter particles, each with a particle filter of $N_x$ state particles.
> - Reweight each $\theta_m$ by its filter's estimate $\hat p(y_t\mid y_{1:t-1},\theta_m)$.
> - When the effective sample size drops below a threshold, resample and move with a PMMH kernel: run a fresh filter for the proposal $\tilde\theta$ and accept with the ratio of $p(\theta)\hat Z_t$ times the proposal ratio.

> [!definition] Exactness
> The filter estimates are unbiased, so SMC² targets the right posterior for any $N_x$. $N_x=\infty$ recovers IBIS; $N_x=1$ is importance sampling.

> [!definition] Evidence (Sec. 3.3)
> ```
> L_t = sum_m w_m p(y_t | ..., theta_m)
>       / sum_m w_m
> ```

- State estimates are Rao-Blackwellized over all state particles; smoothing uses the PMCMC extended target.
- PMMH needs $N_x=O(t)$, so $N_x$ grows automatically through an exchange step (PMMH-type or conditional-SMC / particle-Gibbs-type).
- Inputs needed: a sampler for the transition (its density is not needed), the observation likelihood, and the prior.

> [!definition] Cost (Prop. 2)
> Memory $O(N_\theta N_x)$. With $N_x=\lceil\eta t\rceil$, resampling occurs at geometrically spaced times, and a move at time $t$ costs $O(tN_\theta N_x)$. Sequential, but not online: cost grows with $t$.

## Results
- Lévy-driven stochastic volatility models, including model comparison through the evidence.

> [!example] Athletics records (Sec. 5)
> Women's 3000 m records with a GEV model. $N_\theta=1000$, $N_x=250$, 30-70 s per run.
> ```
> P(486.11 s in 1993
>   | record beats 502.62)
>   = 9.4e-4  (sd 3.3e-4)
> ```

- Extensions: intractable densities with unbiased estimates; a tempering variant, which loses unbiasedness.

## Limitations
- The authors: cost grows with $t$, so it is not suited to long online runs; PMMH moves need $N_x$ to grow with $t$.
- Wiki note: as a filter it gives filtering, not smoothing, state estimates unless the extended target is used.

## Connections
- Fulop and Li (2011) found a similar algorithm independently. Software: py-smc2.
- Baseline in [[IFT state and parameter estimation (Hao 2024)]] (500 θ × 1000 x particles).
- Builds on [[Particle filter]] and [[Particle MCMC]].

%% refs:start %%
**Cited by in this wiki**: [[IFT for UQ of differential equations (Hao 2024)]], [[IFT state and parameter estimation (Hao 2024)]], [[Neural information field filter (Hao 2025)]]
%% refs:end %%

**Sources**: `papers/Stochastic Methods/Chopin, Jacob, Papaspiliopoulos - SMC2 An efficient algorithm for sequential analysis of state space models.pdf`.
**Last updated**: 2026-11-21

---

## Related pages
- [[Particle filter]]
- [[Particle MCMC]]
- [[Stochastic state-space model]]
- [[Markov chain Monte Carlo]]
- [[IFT state and parameter estimation (Hao 2024)]]
