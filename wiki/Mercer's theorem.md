---
type: theorem
area: math
areas: [math, stochastic]
source-ref: "Alexanderian 2015, Thm 3.1; Li, Thm 1.5"
tags: [gp, uq]
---

# Mercer's theorem

**Summary**: A continuous, symmetric, positive kernel on a compact interval is a uniformly convergent sum of its integral operator's eigenpairs. It is the step that makes the [[Karhunen-Loève expansion]] converge uniformly.

---

## Statement

> [!theorem] Mercer (source: Alexanderian 2015, Thm 3.1, p. 5)
> Let $k$ be continuous on $D\times D$ with $D=[a,b]$, and let its integral operator $K$ be positive with eigenpairs $(\lambda_i,e_i)$. Then
> $$k(s,t)=\sum_i\lambda_ie_i(s)e_i(t)$$
> with absolute and uniform convergence on $D\times D$.

## Use in KL

The mean-square error of the truncated expansion is

$$\varepsilon_n(t)=k(t,t)-\sum_{i\le n}\lambda_ie_i(t)^2$$

Mercer sends it to zero uniformly in $t$ (source: Alexanderian 2015, proof of Thm 5.3). Li uses it for the Cauchy property of the series (source: Li, Thm 1.5).

Wiki note: the operator is compact and self-adjoint, so it has a real eigenbasis whose eigenvalues accumulate only at 0 (source: Alexanderian 2015, Thm 2.11). A [[Gaussian process]] covariance is such a kernel.

**Sources**: Alexanderian 2015; Li (lecture notes).
**Last updated**: 2026-11-06

---

## Related pages
- [[Karhunen-Loève expansion]]
- [[KL expansion note (Alexanderian 2015)]]
- [[Brownian motion construction (Li n.d.)]]
- [[Wiener process]]
