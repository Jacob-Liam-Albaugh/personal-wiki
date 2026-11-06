---
type: concept
area: gp
areas: [gp, ml]
source-ref: "Duvenaud 2014 ch. 2 (§2.3-2.8), ch. 3, ch. 6"
tags: [gp, ml]
---

# Kernel composition

**Summary**: Building a new valid kernel from simpler ones by sums, products, changepoints, warping and symmetrisation. Each operation has a plain meaning for the functions the [[Gaussian process]] prior favours, so a kernel expression reads as a statement about structure.

---

## Basic kernels (source: Duvenaud 2014, §2.2, p. 9)

| Kernel | Favours |
|---|---|
| squared exponential (SE) | smooth, local variation |
| periodic (Per) | exact repetition |
| linear (Lin) | linear trends |
| rational quadratic (RQ) | variation at several length scales |
| white noise (WN) | independent noise |

## Operations

> [!theorem] Closure under sum and product
> If $k_a,k_b$ are kernels, so are $k_a+k_b$ and $k_ak_b$. For independent GPs
> $$f_a+f_b\sim GP(\mu_a+\mu_b,\ k_a+k_b).$$
>
> (source: Duvenaud 2014, §2.3-2.4, eq. 2.7, p. 14)

- **Sum**: functions that are a sum of independent parts. Kernels on separate inputs give additive functions that can extrapolate, where a product of SE kernels reverts to the mean (source: Duvenaud 2014, Figs. 2.5-2.6, pp. 15-16).
- **Product**: AND of the properties. Lin x Lin gives quadratics; SE x Per gives locally periodic; Lin x Per gives growing amplitude. Products of one-dimensional SE kernels give SE-ARD (eq. 2.4, p. 12).
- **Changepoint**: with a sigmoid $\sigma$ (eq. 2.19, p. 20),
$$CP(k_1,k_2)=\sigma k_1\sigma+\bar\sigma k_2\bar\sigma.$$
- **Multiplication by a known function**: $a(x)g(x)\sim GP(0,\ a(x)k(x,x')a(x'))$ (eq. 2.21).
- **Feature view**: sum concatenates feature vectors; product takes all pairwise products of features (source: Duvenaud 2014, §2.6, p. 21).
- **Symmetry**: to enforce $f(x)=f(g(x))$ for group elements $g$, sum or multiply the kernel over the orbit, or project to a fundamental domain (§2.7, eqs. 2.36-2.39). The periodic kernel is SE applied to $(\sin x,\cos x)$ (eq. 2.41). Related: [[Equivariance]].
- **Additive of order $n$**: a sum over $n$-subsets of products of 1D kernels, evaluated cheaply with Newton-Girard identities (source: Duvenaud 2014, ch. 6, eq. 6.14, p. 85).

## Automatic search

The ABCD search starts from base kernels and greedily applies replace, add and multiply operators, scoring by BIC, then describes the winner in English (source: Duvenaud 2014, ch. 3, pp. 32-38; ch. 4).

## Use in surrogate modelling

- Multi-fidelity models compose a kernel on the input with a kernel linking fidelity levels ([[Multi-fidelity Gaussian process]]).
- Wiki note: the RKHS of a sum kernel is the sum of the RKHSs; this follows from standard theory and is not proved in the sources here. **[unverified]**

**Sources**: `papers/Guassian Processes/Duvenaud - Thesis - Automatic Model Construction with Gaussian Processes.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Kernel methods]] · [[RKHS]] · [[Gaussian process]] · [[Equivariance]]
- [[Multi-fidelity Gaussian process]] · [[Surrogate model]]
- [[Duvenaud thesis (Duvenaud 2014)]]
