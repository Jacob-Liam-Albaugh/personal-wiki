---
type: paper
area: dsl
source-ref: "Niu-Spivak 2024, ch. 6"
authors: ["[[Nelson Niu]]", "[[David I. Spivak]]"]
year: 2024
venue: book draft
file: "text_books/Category Theory/Spivak, Niu - Polynomial Functors.pdf"
tags: [category-theory]
---

# Polynomial Functors ch6 - The composition product

**Summary**: The composition product p composed with q (written p tri q), its closed formulas, lenses into composites, dynamical systems as coalgebras, distributivity, coclosure, connected limits, and the duoidal structure with the parallel product.

**Authors**: Nelson Niu, David I. Spivak · **Year**: 2024 · **File**: `text_books/Category Theory/Spivak, Niu - Polynomial Functors.pdf`

---
## Problem

Polynomials are functors, so they compose. The chapter defines that composition as a monoidal product, computes it as a polynomial, and studies lenses into and out of it. (source: Polynomial Functors, ch. 6, pp. 179-216)

## Definition and formulas (pp. 180-182)

> [!definition] Composition product (Def 6.1, p. 180)
> For polynomial functors $p, q$, the composition product $p \circ q : \mathsf{Set} \to \mathsf{Set}$ is their composite as functors: it sends a set $X$ to $p(q(X))$. (source: Polynomial Functors, p. 180)

> [!theorem] Composite is polynomial (Prop 6.2, eq. 6.3, 6.4; p. 180)
> $$ p \circ q \cong \sum_{i \in p(1)} \prod_{a \in p[i]} \sum_{j \in q(1)} \prod_{b \in q[j]} y. $$
> Pushing the products past the sums with (1.30) gives
> $$ p \circ q \cong \sum_{i \in p(1)} \sum_{j : p[i] \to q(1)} y^{\sum_{a \in p[i]} q[j(a)]}. $$
> (source: Polynomial Functors, p. 180)

> [!theorem] Monoidal structure (Cor 6.5, p. 180)
> $(\mathsf{Poly}, y, \circ)$ is monoidal, with $y$ the identity functor. The book writes $p \triangleright q := p \circ q$ for this product, since $\circ$ is also used for composition in arbitrary categories and $\triangleright$ displays the asymmetry. (source: Polynomial Functors, p. 180)

- On p. 181: $p^{\triangleright n}$ is the $n$-fold composition product, with $p^{\triangleright 0} = y$ and $p^{\triangleright 1} = p$.
- In words (read off the second formula): a position of $p \triangleright q$ is a position $i$ of $p$ together with a position $j(a)$ of $q$ for each direction $a$ at $i$; a direction there is a pair $(a, b)$ with $b \in q[j(a)]$.
- Def 6.11 (p. 182): horizontal composition of natural transformations, which gives the action of $\triangleright$ on lenses.

## Examples and lenses (pp. 187-200)

- Ex 6.27 (p. 187): composing with constants, $p(X)$ for a set $X$. Ex 6.31 (p. 188): $p = q = y^2 + y$, $p' = y^3 + y$, $q' = y + 1$ drawn as forests. Ex 6.36 (p. 191): substitution products of dynamical systems as trees, using the halting automaton $p = y^A + 1$. Ex 6.38 (p. 193): composition products of dynamical systems can be misleading.
- Ex 6.40 (p. 195): a lens $\varphi : p \to q \triangleright r$ drawn in polyboxes; the cases $n = 0, 1, 2$ of lenses into $q_1 \triangleright \cdots \triangleright q_n$ recover earlier pictures (3.34), (3.13), (6.39). Ex 6.41 (p. 197): dynamical systems with composite interfaces.
- Ex 6.43 (p. 199): the $n$-fold product $\varphi^{\triangleright n}$ of a dynamical system $\varphi : Sy^S \to p$, revisited. Ex 6.44 (p. 200): transition lenses for state systems.

## Algebraic properties (pp. 204-216)

- Prop 6.47 (p. 204): $-\triangleright r$ commutes with coproducts and products (left distributivity); Ex 6.53 (p. 205) pictures the case of $\times$.
- Prop 6.57 (Meyers, p. 206): $\triangleright$ is left coclosed, with a coclosure operation $\mathsf{Poly}^{\mathrm{op}} \times \mathsf{Poly} \to \mathsf{Poly}$.
- Ex 6.67 (p. 208): taking $A = B = S$ in (6.65), dynamical systems $Sy^S \to p$ are coalgebras of the polynomial functor $p$ (natural isomorphism stated on p. 208).
- Prop 6.68 (p. 209): $\triangleright$ preserves limits on the left. Def 6.71 (p. 209): a connected limit is one over a nonempty connected index category; equalizers, pullbacks and directed limits are examples (Ex 6.72). Prop 6.73 (p. 210): a natural isomorphism for lenses into $q \triangleright r$ over $q \triangleright 1$. Thm 6.80 (p. 212): $\triangleright$ preserves connected limits on both sides. Prop 6.83 (p. 213): tensoring with $q$ preserves connected limits.
- Ex 6.85 (p. 213): a cartesian lens $o_{p,q} : p \otimes q \to p \triangleright q$ that orders the two operations. Prop 6.87 (p. 214): $(y, \otimes)$ and $(y, \triangleright)$ together form a duoidal structure on Poly; the key is the natural lens of (6.86). Prop 6.88 (p. 215): $\triangleright$ preserves cartesian lenses.

## Limitations

Read in full from the text: Def 6.1, Prop 6.2, Cor 6.5 and the first lines of the following page (the displayed formulas above are the book's, transcribed). Read at statement level: everything else (Defs 6.11, 6.71; Props 6.47, 6.57, 6.68, 6.73, 6.83, 6.87, 6.88; Thm 6.80; example headings). The wording of Prop 6.57's coclosure and the isomorphism of Prop 6.73 are not reproduced. Proofs and exercises were not read.

## Connections

- Previous: [[Polynomial Functors ch5 - More categorical properties]]. Next: [[Polynomial Functors ch7 - Polynomial comonoids and retrofunctors]], where comonoids in $(y, \triangleright)$ are categories.
- Concept pages: [[Poly composition product]], [[Polynomial comonoid]], [[Monoidal category]], [[Moore machine]]. The duoidal Prop 6.87 pairs with [[Poly parallel product]].

**Sources**: Niu, Spivak, Polynomial Functors (2024), ch. 6; page numbers are printed pages.
**Last updated**: 2026-11-06

---

## Related pages
[[Poly composition product]] · [[Polynomial comonoid]] · [[Poly parallel product]] · [[Moore machine]] · [[Monoidal category]]
