---
type: method
area: ml
areas: [ml, bayesian]
source-ref: "Kingma, Salimans & Welling 2015, §2.3, eqs. 4-8, Table 1"
tags: [vi, ml]
---

# Local reparameterization trick

> [!algorithm] Local reparameterization
> With $q_\phi(w_{ij})=N(\mu_{ij},\sigma_{ij}^2)$ and input activations $A$, the pre-activations are Gaussian:
> $$\gamma_{mj}=\textstyle\sum_i a_{mi}\mu_{ij},\qquad\delta_{mj}=\sum_i a_{mi}^2\sigma_{ij}^2$$
> $$b_{mj}=\gamma_{mj}+\sqrt{\delta_{mj}}\,\zeta_{mj},\quad\zeta_{mj}\sim N(0,1).$$
> Sample $b$ directly instead of $w$.
>
> (source: `Bayesian/Kingma, Welling, Salimans - Variational Dropout & Local Reparameterizing Trick.pdf`, eq. 6)

**Intuition**: sharing one weight sample across a minibatch correlates the per-example gradient terms, and that covariance does not shrink with batch size. Sampling the activations gives each example independent noise at the cost of one extra matrix product.

## Why it works
Minibatch estimator variance (eqs. 4-5):
$$\mathrm{Var}[L]=N^2\Big(\tfrac1M\mathrm{Var}[L_i]+\tfrac{M-1}M\mathrm{Cov}[L_i,L_j]\Big)$$
Local noise makes $\mathrm{Cov}[L_i,L_j]=0$.

## Results (Table 1, p. 7)
- Top-layer gradient variance after 10 epochs: $7.8\times10^3$ (local) vs $1.4\times10^4$ (per-datapoint weights) vs $4.9\times10^4$ (per-minibatch weights); $2.8\times10^3$ with no noise.
- Per-datapoint weight sampling: 1635 s/epoch vs 7.4 s/epoch local.

## Where it appears
- [[Variational dropout (Kingma 2015)]] (defines it).

**Sources**: `Bayesian/Kingma, Welling, Salimans - Variational Dropout & Local Reparameterizing Trick.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Reparameterization trick]] · [[Variational dropout]] · [[Bayesian neural networks]]
