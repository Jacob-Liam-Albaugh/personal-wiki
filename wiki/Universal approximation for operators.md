---
type: theorem
area: operators
source-ref: "Chen & Chen 1995, as Theorem 1 in Lu et al. 2021; Theorem 2, p. 3"
tags: [operators]
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

**Intuition / when to use it**: it guarantees existence only: no rate, no bound on $m$, $p$. Rates for ODE operators come from Theorem 3 on [[DeepONet]].

## Later forms
> [!theorem] Neural operators (Kovachki et al. 2022, Thms 11-14, pp. 50-51)
> - Thm 11: for continuous $\mathcal G^\dagger$ and compact $K$, some [[Neural operator]] is within $\varepsilon$ uniformly on $K$.
> - Thm 12: the same for inputs in $C^{m_1}$, with derivative inputs.
> - Thm 13: approximation in $L^2_\mu$ for measurable $\mathcal G^\dagger$.
> - Thm 14: the $L^2_\mu$ analogue for $C^{m_1}$ inputs.

> [!theorem] Review statements (Kovachki et al. 2024, §4, pp. 12-15)
> - Thm 4.1: [[Encoder-decoder operators|encoder-decoder nets]] are universal between Banach spaces with the approximation property.
> - Thm 4.2: Chen-Chen restated with sensor encoder, shallow branch and trunk.
> - Thm 4.4: [[PCA-Net]] is universal.
> - Thm 4.5 and Cor. 4.6: neural operators are universal, which covers [[FNO|FNO]].

> [!warning]
> The review prints Thm 4.1's composition as $F_U\circ\alpha\circ G_V$. Read it as $G_V\circ\alpha\circ F_U$.

None of these give rates. For lower bounds see [[Curse of parametric complexity]].

## Where it appears
- [[DeepONet (Lu 2021)]] — the basis of the architecture.
- [[Neural operator (Kovachki 2022)]], [[Operator learning review (Kovachki 2024)]].
- [[Markovian homogenized viscoelasticity (Bhattacharya 2023)]] — cited (p. 6, ref. [6]) in the literature review.

**Sources**: `26.10.22 - DeepONets.pdf`, `papers/Operators/Li, Kovachki, Stuart, Anandkumar - Neural Operators.pdf`, `papers/Operators/Stuart - Operator Leraning - Algorithms and Analysis.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[DeepONet]] · [[Operator learning]] · [[Neural operator]]
