---
type: definition
area: dsl
source-ref: "Bilionis 2026, §3.1"
tags: [category-theory]
---

# Coproduct $p+q$

> [!definition] Coproduct $p+q$
> For $p=\sum_{i\in I} y^{A_i}$ and $q=\sum_{j\in J} y^{B_j}$:
> $$p+q = \sum_{x\in I+J} y^{C_x},\quad C_{\iota_I(i)}=A_i,\ C_{\iota_J(j)}=B_j$$
> Unit: $0$.
>
> (source: `Bilionis - Polynomial Equipment Interfaces and Experimental Protocols.pdf`, §3.1, p. 4)

**Intuition**: choose **one** tagged component position; accept a direction from that component only.

## Comparison

| | positions | directions at $(i,j)$ | unit |
|---|---|---|---|
| [[Poly coproduct]] $p+q$ | one of $I+J$ | that component's | $0$ |
| [[Poly product]] $p\times q$ | pairs $IJ$ | $A_i + B_j$ (either) | $1$ |
| [[Poly parallel product]] $p\otimes q$ | pairs $IJ$ | $A_iB_j$ (both) | $y$ |

Wiki note: Poly also has the composition product $\triangleright$ ([[Poly composition product]]), which Bilionis 2026 does not use (its $\triangleright$ is [[Sequential protocol composition]], a different operation). The parallel product is the Dirichlet product.

## Coproducts and colimits in Poly

- Prop 3.3 (p. 42): Poly has all small coproducts, as in $\mathsf{Set}^{\mathsf{Set}}$. Cor 3.5 (p. 42): every polynomial is the coproduct of its representable summands, $p = \sum_{i} y^{p[i]}$. Cor 1.38 (p. 16): $F + G$ is computed pointwise; $0$ is initial (Cor 1.39).
- Prop 3.39 (p. 55): sections satisfy $\Gamma(0) \cong 1$ and $\Gamma(p + q) \cong \Gamma(p) \times \Gamma(q)$ ([[Dependent lens]]).
- Thm 5.43 (p. 156): Poly has all small colimits (coproducts plus coequalizers). Ex 5.45 (p. 156): general colimits in Poly can differ from colimits in $\mathsf{Set}^{\mathsf{Set}}$, since every functor is a colimit of representables but a colimit in Poly must be polynomial; limits and coproducts agree.
- Prop 5.49 (p. 157), Cor 5.50 (p. 158): $p \otimes q$ is a pushout of $p(1)y \otimes q$ and $p \otimes q(1)y$ over $p(1)y \otimes q(1)y$, so a lens out of $p \otimes q$ is a pair of lenses agreeing on the shared part ([[Poly parallel product]]).
- Ex 4.21 (p. 91): the halting-automaton interface $y^A + 1$ is a coproduct ([[Dynamical system as lens]]). Cor 8.72 (p. 325), Ex 8.73: coproducts of categories in $\mathsf{Cat}^\sharp$ are disjoint unions ([[Retrofunctor]]).
- Preserves vertical and cartesian lenses (Prop 5.63): [[Vertical and cartesian lens]].

## Where it appears
- [[Polynomial equipment interfaces (Bilionis 2026)]] — the contrast case when comparing the three products fiber by fiber.
- Poly is extensive (source: Spivak - Poly.pdf, §2).

**Covered in**: Niu-Spivak, Polynomial Functors ch. 3 (pp. 42, 55); ch. 5 (pp. 156-158)
**Sources**: `Bilionis - Polynomial Equipment Interfaces and Experimental Protocols.pdf`; `text_books/Category Theory/Spivak, Niu - Polynomial Functors.pdf`; page numbers are printed pages.
**Last updated**: 2026-11-06

---

## Related pages
- [[Polynomial functor]] · [[Poly product]] · [[Poly parallel product]] · [[Poly composition product]] · [[Dependent lens]]
