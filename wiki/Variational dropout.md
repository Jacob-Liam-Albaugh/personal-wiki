---
type: method
area: ml
areas: [ml, bayesian]
source-ref: "Kingma, Salimans & Welling 2015, §3, eqs. 9-12"
tags: [vi, bayesian, ml]
---

# Variational dropout

> [!algorithm] Variational dropout
> Gaussian dropout $B=(A\circ\xi)\theta$, $\xi\sim N(1,\alpha)$, $\alpha=p/(1-p)$, read as a weight posterior $w_{ij}\sim N(\theta_{ij},\alpha\theta_{ij}^2)$. Maximise over $\theta$ **and** $\alpha$:
> $$\mathbb E_{q_\alpha}[L_D(\theta)]-\mathrm{KL}\big(q_\alpha(w)\,\|\,p(w)\big).$$
>
> (source: `papers/Bayesian/Kingma, Welling, Salimans - Variational Dropout & Local Reparameterizing Trick.pdf`, eq. 12)

**Intuition**: dropout already injects multiplicative noise; with the right prior that noise is a variational posterior, so the dropout rate can be learned instead of tuned.

## Ingredients
- **Gaussian dropout**: multiplicative $N(1,\alpha)$ noise in place of Bernoulli. Type A is on inputs (correlated weight noise, eq. 11); type B on weights (independent, eq. 10), whose activation marginals are
  $$\gamma_{mj}=\textstyle\sum_ia_{mi}\theta_{ij},\quad\delta_{mj}=\alpha\sum_ia_{mi}^2\theta_{ij}^2.$$
- **Scale-invariant log-uniform prior** $p(\log|w_{ij}|)\propto\text{const}$: the only prior that makes the KL term independent of $\theta$ (§3.3; proof in a missing appendix).
- KL approximation (p. 6):
  $$-\mathrm{KL}\approx c+\tfrac12\log\alpha+c_1\alpha+c_2\alpha^2+c_3\alpha^3$$
  with $c_1=1.16145124$, $c_2=-1.50204118$, $c_3=0.58629921$.
- Gradients via the [[Local reparameterization trick]].

## Failure modes
- The approximation is fitted for $\alpha\le1$ (dropout rate 0.5), so $\alpha$ is clipped there (p. 6).
- Best results downscale the KL by 3 (variant "A2"), so the method is not exact VI as run.

## Where it appears
- [[Variational dropout (Kingma 2015)]] (defines it) · [[Intro to VAEs (Kingma 2019)]] (cites the sparsifying follow-up).

**Sources**: `papers/Bayesian/Kingma, Welling, Salimans - Variational Dropout & Local Reparameterizing Trick.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Bayesian neural networks]] · [[Variational inference]]
