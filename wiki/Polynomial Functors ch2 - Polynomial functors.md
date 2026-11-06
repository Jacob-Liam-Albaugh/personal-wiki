---
type: paper
area: dsl
source-ref: "Niu-Spivak 2024, ch. 2"
authors: ["[[Nelson Niu]]", "[[David I. Spivak]]"]
year: 2024
venue: book draft
file: "DSL/Spivak, Niu - Polynomial Functors.pdf"
tags: [category-theory]
---

# Polynomial Functors ch2 - Polynomial functors

**Summary**: Definition of polynomial functors as sums of representables, positions and directions, action on functions, linear and monomial polynomials, and corolla-forest pictures.

**Authors**: Nelson Niu, David I. Spivak · **Year**: 2024 · **File**: `DSL/Spivak, Niu - Polynomial Functors.pdf`

---
## Problem

Define the objects of Poly and give them a usable language: positions, directions, and pictures as forests of corollas. (source: Polynomial Functors, ch. 2, pp. 23-39)

## Definition and basic facts (pp. 25-29)

> [!definition] Polynomial functor (Def 2.1, p. 25)
> A functor $p : \mathsf{Set} \to \mathsf{Set}$ for which there exist a set $I$ and an $I$-indexed family of sets $p[i]$ with
> $$ p \cong \sum_{i \in I} y^{p[i]}. $$
> (source: Polynomial Functors, p. 25)

- Ex 2.4 (p. 26): $p = y^2 + 2y + 1$ applied to $X = \{a, b\}$; the book lists all 9 elements.
- Prop 2.6 (p. 27): $I \cong p(1)$, so $p \cong \sum_{i \in p(1)} y^{p[i]}$.
- Def 2.8 (p. 27): an element $i \in p(1)$ is a position of $p$; an element of $p[i]$ is a direction at $i$.
- Prop 2.10 (p. 27): the action on a function $f : X \to Y$ sends $(i, g)$ with $g : p[i] \to X$ to $(i, f \circ g)$. Ex 2.11 (p. 28) works one through.

## Special polynomials (pp. 29-30)

> [!definition] Linear and monomial (Defs 2.14, 2.15, p. 29)
> $p$ is linear if $p \cong Iy$ for a set $I$. It is a monomial if $p \cong Iy^A$ for sets $I$ and $A$. (source: Polynomial Functors, p. 29)

- Ex 2.16 (p. 29): constants $I = Iy^0$, representables and linear polynomials are monomials. A footnote says "linear" here differs from the high-school sense.
- Ex 2.18 (p. 30): directions as menu options. A representable $y^A$ has one position and $A$ as its directions.
- Ex 2.19 (p. 30): a coin jar with a slot. Positions {open, closed}; at "open" the directions are penny, nickel, dime, quarter, and at "closed" there are none: $q = \{\text{open}\}\,y^{\{\text{penny, nickel, dime, quarter}\}} + \{\text{closed}\}\,y^0$. This is reused in Ex 3.10 (p. 44).

## Trees and corolla forests (pp. 31-36)

- Defs 2.21-2.22 (p. 31): rooted tree, rooted path, height. Def 2.23 (p. 32): a corolla is a rooted tree whose non-root vertices have height 1. Examples 2.24, 2.25 (p. 32): the corolla of $y^A$ has $|A|$ leaves; $y^0 = 1$ is a bare root.
- Def 2.26 (p. 32): the corolla forest of $p$ is the disjoint union of corollas, one per position. Ex 2.27 (p. 33): $y^2 + 2y + 1$ is a forest of 4 corollas.
- Ex 2.31 (p. 34): the 9 elements of $p(\{a, b\})$ read as labelled forests. Ex 2.32 (p. 35): $\sum_{r \in \mathbb{R}} y^{[-|r|, |r|]}$, a polynomial with continuum-sized positions and directions.

## Limitations

Read at statement level: every Def, Prop and Example heading of the chapter; Defs 2.1, 2.8, 2.14, 2.15 and Props 2.6, 2.10 were opened in the text. The Ex 2.19 summary and the list of figures are from the text but the figure layouts were not rendered. Proofs and exercises were not read.

## Connections

- Previous: [[Polynomial Functors ch1 - Representable functors]]. Next: [[Polynomial Functors ch3 - The category of polynomial functors]], which defines the morphisms.
- Wiki pages: [[Polynomial functor]]; the coproduct of polynomials is [[Poly coproduct]].

**Sources**: Niu, Spivak, Polynomial Functors (2024), ch. 2; page numbers are printed pages.
**Last updated**: 2026-11-06

---

## Related pages
[[Polynomial functor]] · [[Dependent lens]] · [[Functor]] · [[Poly product]] · [[Poly coproduct]]
