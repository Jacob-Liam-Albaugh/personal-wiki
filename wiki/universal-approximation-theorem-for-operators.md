---
type: theorem
area: operators
source-ref: "Chen & Chen 1995, as Theorem 1 in Lu et al. 2021; Theorem 2, p. 3"
---

# Universal approximation theorem for operators

> [!theorem] Theorem 1 (Chen & Chen; Lu et al. 2021, eq. 1, p. 2)
> Let $\sigma$ be continuous and non-polynomial, $X$ Banach, $K_1\subset X$ and $K_2\subset\mathbb R^d$ compact, $V\subset C(K_1)$ compact, and $G:V\to C(K_2)$ continuous. For every $\epsilon>0$ there are $n,p,m$ and constants with
> $$\Big|G(u)(y)-\sum_{k=1}^p\sum_{i=1}^n c_i^k\,\sigma\Big(\sum_{j=1}^m\xi_{ij}^k u(x_j)+\theta_i^k\Big)\,\sigma(w_k\cdot y+\zeta^k)\Big|<\epsilon$$
> for all $u\in V$, $y\in K_2$.

> [!theorem] Theorem 2 — generalized form (Lu et al. 2021, p. 3)
> Under the same hypotheses there are continuous $g:\mathbb R^m\to\mathbb R^p$, $f:\mathbb R^d\to\mathbb R^p$ and sensors $x_1,\dots,x_m\in K_1$ with
> $$\big|G(u)(y)-\langle g(u(x_1),\dots,u(x_m)),\,f(y)\rangle\big|<\epsilon.$$
> $g$, $f$ may be any universal approximators (FNN, ResNet, CNN).

> [!proof]
> Proved in Lu et al.'s Supplementary Section 2, which is not in the PDF here. Chen & Chen 1995 (IEEE TNN) is cited, not read.

**Intuition / when to use it**: it guarantees existence only: no rate, no bound on $m$, $p$. Rates for ODE operators come from Theorem 3 on [[deeponet]].

## Where it appears
- [[lu-2021-deeponet]] — the basis of the architecture.
- [[bhattacharya-2023-markovian-homogenized-viscoelasticity]] — cited (p. 6, ref. [6]) in the literature review.

**Sources**: `26.10.22 - DeepONets.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[deeponet]] · [[operator-learning]]
