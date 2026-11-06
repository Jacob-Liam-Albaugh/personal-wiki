---
type: definition
area: dsl
source-ref: "Bilionis 2026, Def. 2.2; Spivak-Niu (cited)"
tags: [category-theory]
---

# Dependent lens

> [!definition] Lens $f:p\to q$ (Bilionis 2026, Def. 2.2)
> A forward map on positions $f_1: p(1)\to q(1)$, and for each $o\in p(1)$ a backward map on directions
> $$f^\sharp_o: q[f_1(o)] \to p[o].$$
> On $X$: $f_X(o,k) = \big(f_1(o),\ d\mapsto k(f^\sharp_o(d))\big)$.
> Composition: $(f;g)_1 = g_1\circ f_1$, $(f;g)^\sharp_o = f^\sharp_o\circ g^\sharp_{f_1(o)}$.
>
> (source: `Bilionis - Polynomial Equipment Interfaces and Experimental Protocols.pdf`, p. 3)

**Intuition**: positions flow forward, directions flow back. A lens $p\to q$ says how to *present* each $p$-observation as a $q$-observation, and how to *translate* a $q$-request back into a $p$-request. Every natural transformation between polynomial functors has this form (Bilionis cites Niu-Spivak).

## Uses
- **System as a lens** out of a state monomial: [[Dynamical system as lens]].
- **Policy restriction**: [[Same-position restriction lens]] — raw interface → restricted one.
- **Device translation**: a lens from a vendor interface to a common one lets a protocol written once run on several devices, via [[Protocol transport along a lens]].
- **Protocols themselves** are lenses into a terminal-reason polynomial: [[Protocols are lenses]].

## In the book: lenses as natural transformations

> [!definition] Dependent lens (Def 3.1, p. 41)
> A dependent lens $p \to q$ is a natural transformation $p \to q$. Poly is the full subcategory of $\mathsf{Set}^{\mathsf{Set}}$ on the polynomial functors. (source: Polynomial Functors, p. 41)

> [!theorem] Lenses as pairs of maps (Prop 3.6, p. 43)
> $$ \mathsf{Poly}(p, q) \cong \prod_{i \in p(1)} \sum_{j \in q(1)} p[i]^{q[j]}. $$
> (source: Polynomial Functors, p. 43)

- Def 3.9 (p. 44): the pair $(f_1, f^\sharp)$ with $f_1 : p(1) \to q(1)$ and $f^\sharp_i : q[f_1(i)] \to p[i]$; directions go backwards.
- Prop 3.44 (p. 58): the pair is the natural transformation sending $(i, g)$ to $(f_1 i, f^\sharp_i \mathbin{;} g)$. Cor 3.47 (p. 59): conversely $(f_1 i, f^\sharp_i) = f_{p[i]}(i, \mathrm{id}_{p[i]})$. This is [[Yoneda lemma]] at work.
- Prop 3.50 (p. 61): a triangle of lenses commutes iff the on-positions triangle commutes in Set and, for each $i$, the on-directions triangle commutes in Set.
- Ex 3.10 (p. 44): the coin jar of [[Polynomial functor]] as an interaction protocol, a lens into $q$. Ex 3.11 (p. 46): lenses $y^3 + 2y \to y^4 + y^2 + 2$ drawn on forests. Ex 3.14 (p. 48): Caroline asks her parents for money, drawn in polyboxes. Ex 3.15 (p. 49): enumerating all lenses of Ex 3.11.

## Special cases

- Ex 3.26 (p. 52): lenses from a linear polynomial $Iy$ to $p$ are a position of $p$ for each element of $I$. Ex 3.29 (p. 53): lenses $p \to I$ to a constant. Ex 3.32 (p. 53): lenses $p \to y^A$ to a representable are a direction-choice function at every position. Ex 3.33 (p. 54): $p \to y$.
- Ex 3.41 (p. 56): lenses between monomials $Iy^A \to Jy^B$ are bimorphic lenses (forward map, backward map). Ex 3.43 (p. 56): very well-behaved lenses live on $Sy^S$.
- Lenses into composites $q_1 \triangleright \cdots \triangleright q_n$ (Exs 6.40, 6.41, pp. 195-197): [[Poly composition product]].
- Special classes: vertical, cartesian, mono and epi lenses: [[Vertical and cartesian lens]].

> [!definition] Sections (Def 3.36, p. 54)
> A section of $p$ is a lens $p \to y$; write $\Gamma(p) = \mathsf{Poly}(p, y)$, a choice of direction at every position. (source: Polynomial Functors, p. 54)

- Ex 3.38 (p. 55): sections of the money polynomial $\sum_{k \in (0,\infty)} y^{[0,k]}$. Prop 3.39 (p. 55): $\Gamma(0) \cong 1$ and $\Gamma(p + q) \cong \Gamma(p) \times \Gamma(q)$. Sections of $p \otimes q$ (Prop 4.54): [[Poly parallel product]]. $\Gamma$ is adjoint to the Yoneda embedding (Prop 5.12): [[Adjunction]].
- Ex 3.22 (p. 51): the derivative $\dot{p} = \sum_{i \in p(1)} \sum_{a \in p[i]} y^{p[i] - \{a\}}$.

## Where it appears
- [[Polynomial equipment interfaces (Bilionis 2026)]] — systems, protocols, restriction, device-to-common translations.
- Hom-set formula in [[Poly (Spivak 2020)]].
- Lenses between monomials are Hedges' bimorphic lenses (source: Spivak - Poly.pdf, §2).

**Covered in**: Niu-Spivak, Polynomial Functors ch. 3 (pp. 41-61)
**Sources**: `Bilionis - Polynomial Equipment Interfaces and Experimental Protocols.pdf`; `text_books/Category Theory/Spivak, Niu - Polynomial Functors.pdf`; page numbers are printed pages.
**Last updated**: 2026-11-06

---

## Related pages
- [[Polynomial functor]] · [[Dynamical system as lens]] · [[Protocol transport along a lens]] · [[Vertical and cartesian lens]] · [[Poly parallel product]] · [[Poly composition product]]
