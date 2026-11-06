---
type: method
area: me697
areas: [me697, mechanics, uq]
source-ref: "ME 697 book, reduced_order_modeling/ and homework/05"
tags: [ml, uq, pde, signals]
---

# Proper orthogonal decomposition

Optimal orthonormal basis for a family of fields $u(x)$, ordered by captured energy. The continuous form of [[Principal component analysis]]; computed with the [[Singular value decomposition]].

> [!definition] Operator form (source: reduced_order_modeling/)
> With the ensemble average $\langle\cdot\rangle$, the correlation operator is

$$
R\phi = \langle\, \langle \phi, u\rangle\, u \,\rangle,
$$

with kernel

$$
R(x,y) = \langle u(x)\,u(y)\rangle.
$$

The POD modes solve $R\phi_i=\lambda_i\phi_i$. $R$ is self-adjoint and non-negative, so the $\phi_i$ are orthonormal with $\lambda_i\ge 0$.

> [!algorithm] Snapshot computation
> Stack $n$ snapshots as rows of $X$ and take $X=U\Sigma V^T$. Then

$$
\lambda_i = \sigma_i^2 / n,
\qquad
Z = XV = U\Sigma.
$$

Columns of $V$ are the modes; $Z$ holds the coefficients. Truncating at rank $r$ gives the best rank-$r$ reconstruction in the mean-square sense **[unverified: Eckart-Young, standard]**.

> [!example] Homework 5
> Problem 1: show the operator properties above (self-adjoint, non-negative). Problem 2: POD of Navier-Stokes snapshot data (arXiv:2203.07404) (source: homework/05). The notebooks contain no solutions.

## Notes
- Energy captured by $r$ modes is $\sum_{i\le r}\lambda_i/\sum_i\lambda_i$.
- For a random field the POD basis is the [[Karhunen-Loève expansion]]; POD coefficients feed reduced-order models and [[Neural operator]] baselines.
- Contrast [[Dynamic mode decomposition]]: POD ignores time order, DMD uses it.

**Wiki note**: the book's `cumsum(s)/sum(s)` uses singular values, not their squares, so it does not equal captured energy. The claim "n much smaller than m" in the text is also unclear **[unverified]**.

**Sources**: `advanced-scientific-machine-learning/book/reduced_order_modeling/`, `homework/05`.
**Last updated**: 2026-11-06

---

## Related pages
- [[ME697 ROM - SVD, PCA and POD]] · [[Singular value decomposition]] · [[Principal component analysis]] · [[Karhunen-Loève expansion]]
- [[Dynamic mode decomposition]] · [[Surrogate model]]
