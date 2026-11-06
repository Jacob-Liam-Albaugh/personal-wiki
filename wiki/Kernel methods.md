---
type: concept
area: gp
areas: [gp, ml]
source-ref: "Kanagawa et al. 2018 §2-3; Duvenaud 2014 ch. 2; Greengard-O'Neil 2022 §2"
tags: [gp, ml]
---

# Kernel methods

**Summary**: Methods that touch data only through a positive definite kernel $k(x,x')$, a similarity function that equals an inner product of (possibly infinite) feature vectors. The same kernel defines a [[Gaussian process]] prior and a function space ([[RKHS]]), so one fit can be read as Bayesian inference or as regularised regression.

---

## Core idea

A kernel is symmetric and positive semidefinite: every Gram matrix $K_{ij}=k(x_i,x_j)$ is PSD. By Moore-Aronszajn it is the reproducing kernel of a unique RKHS (see [[RKHS]]), and by Mercer it has an eigen-expansion
$$k(x,x')=\sum_i\lambda_i\phi_i(x)\phi_i(x'),$$
so $k(x,x')=\langle h(x),h(x')\rangle$ with $h_i=\sqrt{\lambda_i}\phi_i$ (source: Kanagawa 2018, Thm 4.1, p. 30; Duvenaud 2014, §2.6, p. 21). Methods never form $h$; they use only Gram matrices ("kernel trick").

## Kernel ridge regression

> [!definition] Kernel ridge regression (KRR)
> $$\hat f=\arg\min_{f\in H_k}\tfrac1n\sum_i(f(x_i)-y_i)^2+\lambda\|f\|^2_{H_k}.$$
> By the representer theorem the solution is
> $$\hat f(x)=k_{xX}(k_{XX}+n\lambda I)^{-1}Y.$$
>
> (source: Kanagawa 2018, Thm 3.4, p. 19)

The GP posterior mean with noise variance $\sigma^2$ equals this when $\sigma^2=n\lambda$, so noise acts as the regulariser (source: Kanagawa 2018, Prop 3.6, p. 21).

## What a kernel buys you

- Smoothness and shape priors: squared exponential, Matern, periodic, linear. Sums and products build new kernels ([[Kernel composition]]).
- Uncertainty: the GP posterior standard deviation equals the worst-case error over the RKHS unit ball (source: Kanagawa 2018, Prop 3.10, p. 26).
- Distribution comparison: maximum mean discrepancy is the RKHS distance between kernel means (source: Kanagawa 2018, §6.1, p. 43).
- Quadrature: kernel quadrature weights equal Bayesian quadrature (source: Kanagawa 2018, Prop 6.3).

## Cost and approximations

Exact fit costs $O(N^3)$. Cheaper routes:
- Random Fourier features give finite feature vectors with $k\approx h^\top h$ ([[Random features model]]).
- Truncated [[Karhunen-Loève expansion]] on a bounded domain, $O(Nm^2)$ (source: Greengard-O'Neil 2022, §4, p. 8; [[Reduced-rank GPs (Greengard 2022)]]).

## Where it appears in this wiki

- [[Gaussian processes and kernel methods (Kanagawa 2018)]]: the Bayesian-frequentist dictionary.
- [[Duvenaud thesis (Duvenaud 2014)]]: designing and searching kernel structure.
- [[Kernel integral operator]]: the operator whose eigenpairs give Mercer.

**Sources**: Kanagawa et al. 2018 (`Guassian Processes/Kanagawa, Hennig, Sejdinovic, Sriperumbudur - GPs & Kernel Methods.pdf`); Duvenaud 2014; Greengard and O'Neil 2022.
**Last updated**: 2026-11-06

---

## Related pages
- [[RKHS]] · [[Kernel composition]] · [[Gaussian process]] · [[Kernel integral operator]]
- [[Random features model]] · [[Karhunen-Loève expansion]] · [[Surrogate model]]
- [[Gaussian processes and kernel methods (Kanagawa 2018)]] · [[Duvenaud thesis (Duvenaud 2014)]] · [[Reduced-rank GPs (Greengard 2022)]]
- [[Fourier features]].
