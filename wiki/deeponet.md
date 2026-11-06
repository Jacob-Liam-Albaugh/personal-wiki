---
type: method
area: operators
areas: [operators, ml]
source-ref: "Lu et al. 2021, Fig. 1, p. 3; Theorem 3, p. 5"
---

# DeepONet

> [!algorithm] DeepONet (Lu et al. 2021, p. 3)
> Branch net $[u(x_1),\dots,u(x_m)]\mapsto[b_1,\dots,b_p]$ encodes the input function at $m$ fixed sensors; trunk net $y\mapsto[t_1,\dots,t_p]$ encodes the output location. Merge by dot product:
> $$G(u)(y)\approx\sum_{k=1}^p b_k\big(u(x_1),\dots,u(x_m)\big)\,t_k(y)+b_0.$$
> Train by MSE on triplets $(u, y, G(u)(y))$; a dataset is $P$ locations × $\#u$ input functions.
>
> (source: `26.10.22 - DeepONets.pdf`, p. 3)

**Intuition**: the trunk learns a basis $t_k(y)$ for the output functions and the branch learns the coefficients from the input. It is the network form of Theorem 2 in [[universal-approximation-theorem-for-operators]].

## Variants
- **Stacked**: $p$ separate branch nets. **Unstacked**: one branch net with $p$ outputs. Unstacked with bias $b_0$ performed best (source: `26.10.22 - DeepONets.pdf`).

## How many sensors
> [!theorem] Theorem 3 (Lu et al. 2021, p. 5)
> For $\dot s=g(s,u,x)$, $s(a)=s_0$, with $g$ Lipschitz (constant $c$) and input interpolation error $\max_x|u-u_m|\le\kappa(m,V)$: if
> $$c(b-a)\,\kappa(m,V)\,e^{c(b-a)}<\epsilon$$
> then a one-hidden-layer net on the $m$ sensor values approximates $G(u)(d)$ to $\epsilon$ for all $u\in V$.
> For GRF inputs with Gaussian kernel of length scale $l$, $\kappa(m,V)\sim 1/(m^2l^2)$.

## Stochastic inputs
> [!example] Stochastic ODE / elliptic PDE (Problems 5-6, p. 9)
> The random coefficient is truncated with the [[karhunen-loeve-expansion]], $N=5$ modes (99.9% energy, $l\in[1,2]$) or $N=8$ ($l\in[0.2,2]$). The branch takes the scaled eigenfunctions, the trunk takes $[t,\xi_1,\dots,\xi_N]$.

## As a special neural operator
Kovachki et al. 2022, Prop. 5 (pp. 25-26): a [[neural-operator]] with a pointwise first kernel and discretized integrals reduces to a DeepONet. That DeepONet is not [[discretization-invariance|discretization invariant]], since its parameter count grows with the number of sensors. Its output lies in $\mathrm{span}\{\varphi_1,\dots,\varphi_p\}$, so it is a linear method limited by the Kolmogorov $n$-width.

The review (Kovachki et al. 2024) writes it as an [[encoder-decoder-architecture]]: a linear encoder, a branch network and a trunk basis.

## Benchmarks (Kovachki et al. 2022, Tables 2-3)
- [[darcy-flow]]: 0.0462-0.0487, versus FNO 0.0098-0.0109.
- [[burgers-equation]]: 0.0569-0.0857, versus FNO 0.0018-0.0020.

## Lower bound
For Lipschitz or $C^r$ operators, a ReLU DeepONet needs size $\ge\exp(c\,\varepsilon^{-1/(\alpha r)})$ (review Prop. 5.4). See [[curse-of-parametric-complexity]].

## Where it appears
- [[lu-2021-deeponet]] — introduces it.
- [[kovachki-2022-neural-operator]], [[kovachki-2024-operator-learning-review]], [[li-2021-fno]] (its low-rank baseline is "similar to unstacked DeepONet").
- [[bhattacharya-2023-markovian-homogenized-viscoelasticity]] — the recurrent model there is set against DeepONet-style operator learning.

**Sources**: `26.10.22 - DeepONets.pdf`, `Operators/Li, Kovachki, Stuart, Anandkumar - Neural Operators.pdf`, `Operators/Stuart - Operator Leraning - Algorithms and Analysis.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[universal-approximation-theorem-for-operators]] · [[operator-learning]] · [[karhunen-loeve-expansion]]
