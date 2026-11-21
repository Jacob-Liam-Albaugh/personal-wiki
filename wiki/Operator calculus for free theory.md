---
type: method
area: ift
areas: [ift, bayesian]
source-ref: "Alberts 2024 dissertation, Secs. 3.1-3.1.1, 4.2.2, pp. 37-46, 71-75"
tags: [ift, bayesian, gp]
---

# Operator calculus for free theory

**Idea**: In a Gaussian ("free") theory every expectation reduces to a differential operator acting on the constant 1, which turns moment and covariance computations into algebra (method of Leike and Enßlin, dissertation ref. [131]).

> [!definition] Field operator (pp. 45-46)
> $$\Phi=m+\int dy\,S(x,y)\,\frac{\delta}{\delta m(y)}$$
> Creation $b_x=m$ and annihilation $c_x=\int dy\,S(x,y)\,\delta/\delta m(y)$, with
> $$E[F(\phi)]=F(\Phi)\,1,\quad c_x1=0,\quad [c_x,b_y]=S(x,y)$$
> Example: $c_xb_y1=S(x,y)$.

- **Moments from the partition function** (pp. 38-41): with $Z(q)=C[\det S]^{-1/2}\exp\{\tfrac12q^\dagger Sq\}$ (covariance convention), $\delta Z/\delta q(x)=Z\,(Sq)(x)$ gives $E[\phi]=0$ (Prop. 3.1.1). A second derivative, $\delta^2Z/\delta q\,\delta q'=Z[(Sq)(Sq)'+s]$, gives $E[\phi(x)\phi(x')]=s(x,x')$ (Prop. 3.1.2).
- **Use in well-posedness** (Lemma 3, pp. 71-75): the covariance of $\nabla_\lambda H$ under the free prior and posterior,
$$C_{\text{prior}}=\tfrac12\mathrm{Tr}(\nabla S^{-1}S\nabla S^{-1}S)$$
$$C_{\text{post}}=\tilde m^\dagger\nabla S^{-1}\tilde S\nabla S^{-1}\tilde m$$
$$\quad+\tfrac12\mathrm{Tr}(\nabla S^{-1}\tilde S\nabla S^{-1}\tilde S)$$
Eq. 4.20 (Gaussian expectation of $\nabla H^\top\nabla H$) is derived in Appendix A, p. 140. See [[MAP uniqueness in IFT (Alberts 2025)]].
- **Convention**: the dissertation switches between $S$ as covariance and $S$ as precision; Lemma 3 uses the precision form $\nabla S^{-1}$ in the Hamiltonian.

## Where it appears
- [[IFT for engineering inverse problems (Alberts 2024)]] — Ch. 3 and Lemma 3.

## Enßlin's operator version (IT & IFT §12.2, pp. 138-145)
Enßlin's book builds the same calculus on a different footing, with the Gaussian itself as the object acted on. Here $D$ is the covariance of the Gaussian and $m$ its mean (the notes above use precision-style conventions; compare before mixing formulas).
- Field operator $\Phi=D\,	frac{d}{dm}+m$ acting on the vacuum $1$, with $[a_x,a_y^\dagger]=D_{xy}$ for annihilation and creation operators $a=D\,d/dm$ and $a^\dagger=m$-multiplication.
- Moments of the free theory follow by applying $\Phi$ repeatedly; exponentials of $\Phi$ are handled with the Baker-Campbell-Hausdorff formula, giving for example $\langle e^{s_x}
angle=e^{m_x+D_{xx}/2}$ (the lognormal mean used in [[Lognormal Poisson model]]).
- Perturbation theory in [[Interacting information field theory]] is the same algebra applied to the interaction terms.

(source: Ensslin - Information Theory & Information Field Theory.pdf, §12.2, pp. 138-145; p. = PDF page)

**Covered in**: Enßlin IT & IFT §12.2 (pp. 138-145)
**Sources**: `papers/IFT/Alberts - An Information Field Theory Approach to Engineering Inverse Problems.pdf`, `text_books/Machine Learning & Statistics/Ensslin - Information Theory & Information Field Theory.pdf`.
**Last updated**: 2026-11-21

---

## Related pages
- [[Information field theory]]
- [[Gaussian process]]
- [[MAP uniqueness in IFT (Alberts 2025)]]
- [[Generalized random fields]]
- [[IFT for engineering inverse problems (Alberts 2024)]]
- [[Free theory (IFT)]] · [[Interacting information field theory]]
