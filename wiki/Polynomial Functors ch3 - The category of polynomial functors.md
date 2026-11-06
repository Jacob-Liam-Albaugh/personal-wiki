---
type: paper
area: dsl
source-ref: "Niu-Spivak 2024, ch. 3"
authors: ["[[Nelson Niu]]", "[[David I. Spivak]]"]
year: 2024
venue: book draft
file: "text_books/Category Theory/Spivak, Niu - Polynomial Functors.pdf"
tags: [category-theory]
---

# Polynomial Functors ch3 - The category of polynomial functors

**Summary**: Dependent lenses as the morphisms of Poly, the formula for Poly(p,q), polyboxes, derivatives, sections, lenses between monomials, and the parallel (Dirichlet) product.

**Authors**: Nelson Niu, David I. Spivak · **Year**: 2024 · **File**: `text_books/Category Theory/Spivak, Niu - Polynomial Functors.pdf`

---
## Problem

Fix the morphisms of Poly as dependent lenses and show how to compute with them, draw them, and read special cases (lenses from linear polynomials, to constants, to representables, between monomials). Then add the first extra monoidal structure, $\otimes$. (source: Polynomial Functors, ch. 3, pp. 41-81)

## Lenses (pp. 41-50)

> [!definition] Dependent lens (Def 3.1, p. 41)
> A dependent lens $p \to q$ is a natural transformation $p \to q$. Poly is the full subcategory of $\mathsf{Set}^{\mathsf{Set}}$ on the polynomial functors. (source: Polynomial Functors, p. 41)

- Prop 3.3 (p. 42): Poly has all small coproducts, as in $\mathsf{Set}^{\mathsf{Set}}$. Cor 3.5 (p. 42): every $p$ is the coproduct of its representable summands $y^{p[i]}$.

> [!theorem] Lenses as pairs of maps (Prop 3.6, p. 43)
> A lens $p \to q$ is the same as an on-positions function and an on-directions family:
> $$ \mathsf{Poly}(p, q) \cong \prod_{i \in p(1)} \sum_{j \in q(1)} p[i]^{q[j]}. $$
> (source: Polynomial Functors, p. 43)

- Def 3.9 (p. 44): the pair $(f_1, f^\sharp)$, with $f_1 : p(1) \to q(1)$ and, for $i \in p(1)$, $f^\sharp_i : q[f_1(i)] \to p[i]$. Directions go backwards.
- Ex 3.10 (p. 44): the coin jar as an interaction protocol, a lens into $q$. Ex 3.11 (p. 46): lenses $y^3 + 2y \to y^4 + y^2 + 2$ drawn on forests. Ex 3.14 (p. 48): Caroline asks her parents for money, drawn in polyboxes. Ex 3.15 (p. 49): enumerating all lenses of Ex 3.11.
- Ex 3.22 (p. 51): the derivative $\dot{p} = \sum_{i \in p(1)} \sum_{a \in p[i]} y^{p[i] - \{a\}}$.

## Special cases of lenses (pp. 52-58)

- Ex 3.26 (p. 52): lenses from a linear polynomial $Iy$ to $p$ are a position of $p$ for each element of $I$. Ex 3.29 (p. 53): lenses $p \to I$ to a constant. Ex 3.32 (p. 53): lenses $p \to y^A$ to a representable are a direction-choice function on every position. Ex 3.33 (p. 54): $p \to y$.
- Def 3.36 (p. 54): a section of $p$ is a lens $p \to y$; write $\Gamma(p) = \mathsf{Poly}(p, y)$, a choice of direction at every position. Ex 3.38 (p. 55): sections of the money polynomial $\sum_{k \in (0,\infty)} y^{[0,k]}$.
- Prop 3.39 (p. 55): $\Gamma(0) \cong 1$ and $\Gamma(p + q) \cong \Gamma(p) \times \Gamma(q)$.
- Ex 3.41 (p. 56): lenses between monomials $Iy^A \to Jy^B$ are bimorphic lenses (a forward map and a backward map). Ex 3.43 (p. 56): very well-behaved lenses live on $Sy^S$.
- Prop 3.44 (p. 58): the pair $(f_1, f^\sharp)$ of (3.7) is the natural transformation sending $(i, g)$ to $(f_1 i, f^\sharp_i \mathbin{;} g)$. Cor 3.47 (p. 59): conversely $(f_1 i, f^\sharp_i) = f_{p[i]}(i, \mathrm{id}_{p[i]})$.
- Prop 3.50 (p. 61): a triangle of lenses commutes iff the on-positions triangle commutes in Set and, for each $i$, the on-directions triangle commutes in Set.

## Parallel product (pp. 65-76)

- Prop 3.56 (p. 65): Poly has arbitrary products, computed as in $\mathsf{Set}^{\mathsf{Set}}$ (see [[Poly product]]). Cor 3.58 (p. 65): Poly is completely distributive.

> [!definition] Parallel product (Def 3.65, p. 67)
> $$ p \otimes q = \sum_{i \in p(1)} \sum_{j \in q(1)} y^{p[i] \times q[j]}. $$
> (source: Polynomial Functors, p. 67)

- Ex 3.67 (p. 67): $B_1 y^{A_1} \otimes B_2 y^{A_2} \cong B_1 B_2\, y^{A_1 A_2}$. Ex 3.70 (p. 68): $(y^3 + y) \otimes (y^2 + 1) = y^6 + y^2 + 2$, drawn as forests.
- Prop 3.73 (p. 68): $(\mathsf{Poly}, y, \otimes)$ is symmetric monoidal. Prop 3.79 (p. 70): any monoidal structure $(I, \star)$ on Set gives $(y^I, \odot)$ on Poly by Day convolution, distributing over coproducts. For $(0, +)$ it returns $(1, \times)$ and for $(1, \times)$ it returns $(y, \otimes)$.

## Limitations

Read at statement level: all Defs, Props, Cors and Example headings of the chapter, with Defs 3.1, 3.9, 3.36, 3.65 and Props 3.6, 3.39, 3.73 opened in the text. Defs 3.1 and Props 3.44, 3.47, 3.50, 3.56, 3.58, 3.79 were also opened. Proofs and exercises were not read.

## Connections

- Previous: [[Polynomial Functors ch2 - Polynomial functors]]. Next: [[Polynomial Functors ch4 - Dynamical systems as dependent lenses]], which uses Ex 3.41 and 3.43 for Moore machines.
- Wiki pages: [[Dependent lens]], [[Poly parallel product]] (same operation, also called the Dirichlet product), [[Poly coproduct]], [[Poly product]].

**Sources**: Niu, Spivak, Polynomial Functors (2024), ch. 3; page numbers are printed pages.
**Last updated**: 2026-11-06

---

## Related pages
[[Dependent lens]] · [[Poly parallel product]] · [[Poly coproduct]] · [[Poly product]] · [[Polynomial functor]]
