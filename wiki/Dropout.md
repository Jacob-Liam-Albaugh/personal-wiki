---
type: concept
area: ml
areas: [ml]
source-ref: "Srivastava et al. 2014, §4-5, §9"
tags: [ml, optimization, bayesian]
---

# Dropout

**Summary**: A regularizer that multiplies hidden activations by random Bernoulli masks during training, so each step trains a random thinned subnetwork. At test time the full net is used with scaled weights, approximating an average over exponentially many subnetworks.

**Sources**: `papers/ML/Hinton, Srivastava, Krizhevsky, Sutskever, Salakhutdinov - Dropout.pdf`.
**Last updated**: 2026-11-06

---

## Definition

> [!definition] Dropout
> With retention probability $p$ and activations $y$:
> $$r_j\sim\mathrm{Bernoulli}(p)$$
> $$\tilde y=r*y$$
> Test time: use all units and weights $pW$. (source: Dropout paper, §4-5)

Inverted form: keep $\tilde y = r*y/p$ in training and leave weights unchanged at test time (source: Dropout paper, §10).

## Why it works (as argued by the paper)

- Prevents co-adaptation: no unit can rely on a specific partner being present (§7.1).
- Model averaging: a net with $n$ units holds $2^n$ weight-sharing subnets (§2).
- Implicit sparsity: activations become sparse without a penalty (§7.2).

## Mathematical view

For linear regression, marginalizing the mask gives an $L_2$ penalty weighted by the input scale:
$$\min_w\ \|y-pXw\|^2+p(1-p)\|\Gamma w\|^2$$
This is ridge regression with $\Gamma=\mathrm{diag}(X^\top X)^{1/2}$ (source: Dropout paper, §9.1).

Wiki note: reading dropout as approximate Bayesian inference (a variational posterior over weights) is a later result, covered on [[Variational dropout]] and [[Bayesian neural networks]], not in this paper. The paper itself says dropout weights submodels equally and is not Bayesian (§6.4).

## Variants and settings

- Gaussian dropout: multiply by $N(1,\sigma^2)$ with $\sigma^2=(1-p)/p$ (§10).
- Hidden units $p\approx0.5$, inputs $p\approx0.8$; use at least $n/p$ units; learning rate 10 to 100 times larger; momentum 0.95 to 0.99; max-norm $c=3$ to $4$ (App. A).
- Dropout RBMs apply the same mask idea to the hidden units of an RBM (§8).

## Related pages
- [[Dropout paper (Srivastava 2014)]]
- [[Variational dropout]]
- [[Bayesian neural networks]]
- [[Weight initialization]]
- [[Momentum]]
- [[Adam]]
- [[ResNet]]
- [[SGLD]]
