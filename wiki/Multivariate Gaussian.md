---
type: definition
area: bayesian
areas: [bayesian, ift, gp]
source-ref: "Enßlin, IT & IFT, ch. 4, §4.1-4.3, eqs. 225-282"
tags: [bayesian, ift, gp]
---

# Multivariate Gaussian

> [!definition] Gaussian distribution
> One dimension: $\mathcal G(x-m,\sigma^2)=\frac1{\sqrt{2\pi\sigma^2}}\exp\!\big(-\tfrac{(x-m)^2}{2\sigma^2}\big)$. In $n$ dimensions, for a symmetric (Hermitian) positive definite covariance $Y$,
> $$\mathcal G(y,Y)=\frac{1}{\sqrt{\lvert2\pi Y\rvert}}\exp\!\Big(-\tfrac12\,y^\dagger Y^{-1}y\Big)$$
> It is normalized, has mean $\langle y\rangle=0$ and $\langle y\,y^\dagger\rangle=Y$.
>
> (source: Ensslin - Information Theory & Information Field Theory.pdf, §4.1-4.2, eqs. 225, 243-259, pp. 71-74; p. is the PDF page)

**Intuition**: a product of independent 1-D Gaussians is a Gaussian with a diagonal covariance; rotate to the eigenbasis of $Y$ and any correlated Gaussian looks like that product. Mean and covariance determine everything.

Notation: the book writes $\mathcal G(x-m,\sigma^2)\equiv\mathcal N(x\mid m,\sigma^2)$ and defines $|2\pi Y|$ as the determinant of $2\pi Y$. It uses $y^\dagger$ for the conjugate transpose, so the formulas cover the complex case.

## Why it is used (§4.1, p. 71)
- It is the maximum-entropy law for known first and second moments (below).
- It is the limit of sums of many small independent contributions, by the [[Central limit theorem]].
- It is mathematically convenient in high dimension and infinitely divisible.

## Construction and moments (§4.2, pp. 71-74)
- Independent coordinates give $\prod_iG(x_i,\sigma_i^2)=\mathcal G(x,X)$ with $X=\mathrm{diag}(\sigma_i^2)$ (eqs. 226-231).
- An orthonormal change $y=Ox$ keeps the unit Jacobian and gives $Y=OXO^\dagger$, $|Y|=|X|$ (eqs. 232-243). Positive definite $Y$ is exactly the condition that such an $O$ (its eigenvectors) exists with strictly positive eigenvalues.
- Odd moments vanish by symmetry (eqs. 246-251); $\langle y\,y^\dagger\rangle=OXO^\dagger=Y$ (eqs. 252-259).
- **Wick's theorem** (stated without proof, eq. 260): a moment of $2n$ factors is the sum over all pairings of products of covariances. Examples: $\langle y_i^4\rangle=3Y_{ii}^2$, $\langle y_i^6\rangle=15Y_{ii}^3$, and $\langle y_i^{2n}\rangle=\frac{(2n)!}{2^nn!}Y_{ii}^n$ (eq. 261).

## MaxEnt with known mean and covariance (§3.4.5, §4.3, pp. 64, 74-76)
Unknown signal $s$ in a vector space, flat prior, message $J$: $\langle s\rangle=m$ and $\langle(s-m)(s-m)^\dagger\rangle=S$. Applying the [[Maximum entropy principle]] with multipliers $\mu$ (first moment) and $\Lambda$ (second moment):
1. $\mathcal Z(\mu,\Lambda)=\int ds'\exp\big[\mu^\dagger s'+s'^\dagger\Lambda s'-\mathrm{Tr}[\Lambda S]\big]$ with $s'=s-m$.
2. $\partial\ln\mathcal Z/\partial\mu=0$ gives $\mu=0$ by antisymmetry; $\partial\ln\mathcal Z/\partial\Lambda=0$ gives $S=-\tfrac12\Lambda^{-1}$, so $\Lambda=-\tfrac12S^{-1}$ (eqs. 268-278).
3. $P(s\mid J,I)=\mathcal G(s-m,S)$ (eqs. 281-282).

So when only mean and covariance are known, "the safest assumption" is the Gaussian with those moments. The 1-D version, solved by completing the square for $\beta<0$, gives $\alpha=0$, $\beta=-1/(2\sigma^2)$ and $\mathcal Z=\sqrt{2\pi\sigma^2}$ (eqs. 186-200, p. 64).

## Where it appears
- [[Gaussian process]]: the infinite-dimensional case; the book's $V$ may be $C(\mathbb R^n)$ (a function space), the setting of [[Information field theory]].
- [[Laplace approximation]]: Gaussian posterior from the Hessian.
- [[Bayesian inference]]: Gaussian approximation of the coin posterior (eq. 43).

Wiki note: the information Hamiltonian, Wiener filter and Gaussian fields built on this distribution are Part II of the book and are not covered here.

**Covered in**: Enßlin IT & IFT ch. 4 (pp. 71-76); ch. 3 §3.4.5 (p. 64)
**Sources**: `text_books/Machine Learning & Statistics/Ensslin - Information Theory & Information Field Theory.pdf`.
**Last updated**: 2026-11-21

---

## Related pages
- [[Maximum entropy principle]] · [[Central limit theorem]] · [[Gaussian process]] · [[Information field theory]]
