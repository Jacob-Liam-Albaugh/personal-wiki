---
type: definition
area: dsl
source-ref: "Bilionis 2026, §3.1"
tags: [category-theory]
---

# Product $p\times q$

> [!definition] Product $p\times q$
> For $p=\sum_{i\in I} y^{A_i}$ and $q=\sum_{j\in J} y^{B_j}$:
> $$p\times q = \sum_{(i,j)\in IJ} y^{A_i+B_j}$$
> Unit: $1$.
>
> (source: `Bilionis - Polynomial Equipment Interfaces and Experimental Protocols.pdf`, §3.1, p. 4)

**Intuition**: show **both** positions; accept **one** tagged direction from either component. The interface does not decide which component acts next: the protocol does.

## Comparison

| | positions | directions at $(i,j)$ | unit |
|---|---|---|---|
| [[Poly coproduct]] $p+q$ | one of $I+J$ | that component's | $0$ |
| [[Poly product]] $p\times q$ | pairs $IJ$ | $A_i + B_j$ (either) | $1$ |
| [[Poly parallel product]] $p\otimes q$ | pairs $IJ$ | $A_iB_j$ (both) | $y$ |

Wiki note: Poly also has the composition product $\triangleright$ ([[Poly composition product]]), which Bilionis 2026 does not use (its $\triangleright$ is [[Sequential protocol composition]], a different operation). The parallel product is the Dirichlet product.

## Limits, products and cartesian closure in Poly

- Prop 1.37 (p. 15), Cor 1.38 (p. 16): $\mathsf{Set}^{\mathsf{Set}}$ has all small limits, computed pointwise; $F \times G$ is pointwise and $1$ is terminal (Cor 1.39). Prop 1.40: $\mathsf{Set}^{\mathsf{Set}}$ is completely distributive.
- Prop 3.56 (p. 65): Poly has arbitrary products, computed as in $\mathsf{Set}^{\mathsf{Set}}$. Cor 3.58 (p. 65): Poly is completely distributive.

> [!theorem] Cartesian closed (Thm 5.31, p. 152)
> Poly is cartesian closed: $\mathsf{Poly}(p, r^q) \cong \mathsf{Poly}(p \times q, r)$, where $r^q = \prod_{j \in q(1)} r \circ (y + q[j])$ (eq. 5.28). (source: Polynomial Functors, p. 152)

- Thm 5.33 (p. 153): Poly has all small limits (products plus equalizers). Ex 5.35 (p. 154): positions of a limit are the limit of the positions; the direction-set at a position is the colimit of the corresponding direction-sets. Ex 5.38 (p. 154): pullbacks in Poly.
- Prop 5.63, 5.64 (p. 162): $\times$ and pullbacks preserve vertical and cartesian lenses ([[Vertical and cartesian lens]]). Prop 6.47 (p. 204): $-\triangleright r$ distributes over $\times$ ([[Poly composition product]]).
- Ex 4.93 (p. 128): "Chu &", $\varphi_1 \,\&\, \varphi_2 : (p_1 \times p_2) \otimes (q_1 + q_2) \to r$ ([[Poly parallel product]]).
- Cor 8.76 (p. 326): limits in $\mathsf{Cat}^\sharp$ come from this and the cofree comonoid ([[Retrofunctor]]). The right adjoint to $- \times q$ is exponentiation; compare the closure of $\otimes$.

## Where it appears
- [[Polynomial equipment interfaces (Bilionis 2026)]] — the raw joint interface $p_{raw} = p_{TC}\times p_H$ of thermocycler and handler, and the lens $f\times\mathrm{id}$.
- Contrast with [[Poly parallel product]], which is closed but not cartesian.

**Covered in**: Niu-Spivak, Polynomial Functors ch. 3 (p. 65); ch. 5 (pp. 152-154)
**Sources**: `Bilionis - Polynomial Equipment Interfaces and Experimental Protocols.pdf`; `text_books/Category Theory/Spivak, Niu - Polynomial Functors.pdf`; page numbers are printed pages.
**Last updated**: 2026-11-06

---

## Related pages
- [[Polynomial functor]] · [[Poly coproduct]] · [[Poly parallel product]] · [[Poly composition product]] · [[Adjunction]]
