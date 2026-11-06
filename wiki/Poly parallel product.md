---
type: definition
area: dsl
source-ref: "Bilionis 2026, §3.1"
tags: [category-theory]
aliases: [Dirichlet product]
---

# Parallel product $p\otimes q$

> [!definition] Parallel product $p\otimes q$
> For $p=\sum_{i\in I} y^{A_i}$ and $q=\sum_{j\in J} y^{B_j}$:
> $$p\otimes q = \sum_{(i,j)\in IJ} y^{A_i B_j}$$
> Unit: $y$.
>
> (source: `Bilionis - Polynomial Equipment Interfaces and Experimental Protocols.pdf`, §3.1, p. 4)

**Intuition**: show both positions; request **one direction from each** in one semantic step. Bilionis claims no wall-clock simultaneity or independence of effects.

## Comparison

| | positions | directions at $(i,j)$ | unit |
|---|---|---|---|
| [[Poly coproduct]] $p+q$ | one of $I+J$ | that component's | $0$ |
| [[Poly product]] $p\times q$ | pairs $IJ$ | $A_i + B_j$ (either) | $1$ |
| [[Poly parallel product]] $p\otimes q$ | pairs $IJ$ | $A_iB_j$ (both) | $y$ |

Wiki note: Poly also has the composition product $\triangleright$ ([[Poly composition product]]), which Bilionis 2026 does not use (its $\triangleright$ is [[Sequential protocol composition]], a different operation). The parallel product is the Dirichlet product.

## Where it appears
- [[Polynomial equipment interfaces (Bilionis 2026)]] — $p\otimes(Ky^K)$ in [[Protocols are lenses]] (a continuing direction is an equipment direction paired with the next protocol state) and $f\otimes\mathrm{id}_{Ky^K}$ in [[Protocol transport along a lens]].

## Definition and basic facts
- Def 3.65, p. 67: $p \otimes q = \sum_{i,j} y^{p[i] \times q[j]}$. Ex 3.67, p. 67: $B_1 y^{A_1} \otimes B_2 y^{A_2} \cong B_1 B_2\, y^{A_1 A_2}$. Ex 3.70, p. 68: $(y^3+y) \otimes (y^2+1) = y^6+y^2+2$.
- Prop 3.73, p. 68: $(\mathsf{Poly}, y, \otimes)$ is symmetric monoidal. (source: Polynomial Functors, pp. 67-68)
- Prop 3.79, p. 70: Day convolution of a monoidal structure $(I, \star)$ on Set gives $(y^I, \odot)$ on Poly. The structure $(0, +)$ gives $(1, \times)$ and $(1, \times)$ gives $(y, \otimes)$. (source: Polynomial Functors, p. 70)

## Closure and sections
- Closure: $\mathsf{Poly}(p \otimes q, r) \cong \mathsf{Poly}(p, [q, r])$ with $[q, r] = \prod_{j \in q(1)} r \circ (q[j]\, y)$ (Prop 4.85, p. 126). This is an [[Adjunction]]. Ex 4.81, p. 126: $[y^A, y] = Ay$, $[Ay, y] = y^A$ and $[p, y] = \Gamma(p)\, y^{p(1)}$.
- Prop 4.54, p. 113: $\Gamma(p \otimes q) \cong \mathsf{Set}(q(1), \Gamma(p)) \times \mathsf{Set}(p(1), \Gamma(q))$, with $\Gamma(p) = \mathsf{Poly}(p, y)$ the sections.

- Ex 4.92 (p. 127): a robot with interface $q$ does not know its environment; $f : p \otimes q \to r$ induces $f' : p \to [q, r]$ with $f = \mathrm{eval} \circ (f' \otimes q)$. Ex 4.93 (p. 128): "Chu &", $\varphi_1 \,\&\, \varphi_2 : (p_1 \times p_2) \otimes (q_1 + q_2) \to r$ ([[Poly product]], [[Poly coproduct]]). Wiring of systems by parallel-product interfaces: [[Dynamical system as lens]].

## Interaction with other structure
- Prop 5.49, p. 157: $p \otimes q$ is a pushout of $p(1)y \otimes q$ and $p \otimes q(1)y$ over $p(1)y \otimes q(1)y$. Cor 5.50, p. 158: the $n$-fold version is a wide pushout.
- Prop 5.63, p. 162: $\otimes$ preserves vertical and cartesian lenses. Thm 5.73, p. 165: $\otimes$ preserves op-cartesian arrows, so the base-change fibration is a monoidal bifibration.
- Prop 6.83, p. 213: tensoring with $q$ preserves connected limits. Ex 6.85, p. 213: a cartesian lens $p \otimes q \to p \triangleright q$. Prop 6.87, p. 214: $(y, \otimes)$ and $(y, \triangleright)$ form a duoidal structure; see [[Poly composition product]].
- Prop 8.77, p. 326: $(y, \otimes)$ extends to $\mathsf{Cat}^\sharp$ and there is the product of categories. See [[Polynomial comonoid]].
- Wiki note on notation: the book and Poly 2020 write the composition product $\circ$ (the book also $\triangleright$); see [[Poly composition product]].

**Covered in**: Niu-Spivak, Polynomial Functors ch. 3 (pp. 65-70); ch. 4 (pp. 113, 126-128); ch. 5 (pp. 157-165); ch. 6 (pp. 213-214); ch. 8 (pp. 326-327)
**Sources**: `Bilionis - Polynomial Equipment Interfaces and Experimental Protocols.pdf`; `text_books/Category Theory/Spivak, Niu - Polynomial Functors.pdf`; page numbers are printed pages.
**Last updated**: 2026-11-06

---

## Related pages
- [[Polynomial functor]] · [[Poly coproduct]] · [[Poly product]] · [[Poly composition product]] · [[Vertical and cartesian lens]] · [[Retrofunctor]] · [[Dependent lens]]
