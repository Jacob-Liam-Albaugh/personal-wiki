---
type: definition
area: dsl
source-ref: "Bilionis 2026, Def. 2.1; Spivak-Niu (cited)"
tags: [category-theory]
---

# Polynomial functor

> [!definition] Polynomial (Bilionis 2026, Def. 2.1)
> A polynomial is a sum of representables
> $$p = \sum_{o\in O} y^{A_o},\qquad p(X) = \sum_{o\in O} X^{A_o},$$
> an endofunctor of Set acting on maps by $p(u)(o,k) = (o, u\circ k)$.
> Its **positions** are $p(1)\cong O$; the **directions** at $o$ are $p[o] = A_o$.
> A constant polynomial on a set $C$ is $\sum_{c\in C} y^0$.
>
> (source: `Bilionis - Polynomial Equipment Interfaces and Experimental Protocols.pdf`, pp. 2-3)

**Intuition**: a polynomial is a menu that depends on what you see. Each position is a state you can observe; the directions at that position are the moves allowed there. Polynomials and [[Dependent lens]]es form the category **Poly**, with $\mathbf{Poly}(p,q)$ the set of lenses $p\to q$ (cited by Bilionis to Niu-Spivak).

## Equipment-interface reading

Bilionis calls a polynomial an **equipment interface**: positions $O$ are what the instrument reports, $A_o$ the requests it accepts when it reports $o$ (source: `Bilionis - Polynomial Equipment Interfaces and Experimental Protocols.pdf`, Def. 2.1).

> [!failure] Hidden state that changes the menu
> The menu must be a function of the reported position. If an unreported internal state changes which requests are admissible, the interface is wrong as stated: that state has to be exposed in the readout (source: `Bilionis - Polynomial Equipment Interfaces and Experimental Protocols.pdf`, p. 3).

## Notation

Juxtaposition is Cartesian product (`AB = A\times B`); $Sy^S = \sum_{s\in S} y^S$ is the state monomial used by [[Dynamical system as lens]].

## Where it appears
- [[Polynomial equipment interfaces (Bilionis 2026)]] — the interface type of every instrument and example.

## Building blocks: sums, products and distributivity

> [!definition] Sum and product of an indexed family (Defs 1.14, 1.15, p. 7)
> For $X : I \to \mathsf{Set}$, the sum $\sum_{i \in I} X_i$ is the set of pairs $(i, x)$ with $x \in X_i$. The product $\prod_{i \in I} X_i$ is the set of dependent functions: choices $i \mapsto x_i \in X_i$. (source: Polynomial Functors, p. 7)

- Ex 1.16 (p. 8): for $I = 2$, the sum is the disjoint union and the product is the cartesian product. Prop 1.18 (p. 8): the sum is the categorical coproduct in Set and the product is the categorical product. Def 1.20 (p. 9): the sum and product of functions. Ex 1.24 (p. 11): nested index sets $J(i)$, $K(i,j)$.

> [!theorem] Pushing a product past a sum (Prop 1.27, p. 12)
> For sets $I$, $J(i)$ and $X(i, j)$ there is a natural isomorphism
> $$ \prod_{i \in I} \sum_{j \in J(i)} X(i,j) \;\cong\; \sum_{\bar{j} \in \prod_{i} J(i)} \prod_{i \in I} X(i, \bar{j}(i)). $$
> (source: Polynomial Functors, p. 12)

- Cor 1.29 (p. 13): the case $J$ independent of $i$, with $\bar{j} : I \to J$ (equation 1.30, used to compute the composite in [[Poly composition product]]). Def 1.31 (p. 13): a category with all small products and coproducts is completely distributive if products distribute over coproducts this way; Cor 1.33 (p. 14) gives the formula there. Set is completely distributive.
- Limits and colimits of functors Set to Set (Prop 1.37, p. 15): $\mathsf{Set}^{\mathsf{Set}}$ has all small limits and colimits, computed pointwise. Cor 1.38 (p. 16): $F + G$ and $F \times G$ are pointwise. Cor 1.39: the constant functor $0$ is initial and $1$ is terminal. Prop 1.40: $\mathsf{Set}^{\mathsf{Set}}$ is completely distributive. The representable functors and the [[Yoneda lemma]] behind these are on their own page.

## Definition in the book and basic facts

> [!definition] Polynomial functor (Def 2.1, p. 25)
> A functor $p : \mathsf{Set} \to \mathsf{Set}$ for which there exist a set $I$ and an $I$-indexed family of sets $p[i]$ with $p \cong \sum_{i \in I} y^{p[i]}$. (source: Polynomial Functors, p. 25)

- Ex 2.4 (p. 26): $p = y^2 + 2y + 1$ applied to $X = \{a, b\}$ has 9 elements.
- Prop 2.6 (p. 27): $I \cong p(1)$, so $p \cong \sum_{i \in p(1)} y^{p[i]}$. Def 2.8 (p. 27): an element $i \in p(1)$ is a position; an element of $p[i]$ is a direction at $i$.
- Prop 2.10 (p. 27): the action on $f : X \to Y$ sends $(i, g)$ with $g : p[i] \to X$ to $(i, f \circ g)$. Ex 2.11 (p. 28) works one through.

### Special polynomials

> [!definition] Linear and monomial (Defs 2.14, 2.15, p. 29)
> $p$ is linear if $p \cong Iy$ for a set $I$. It is a monomial if $p \cong Iy^A$ for sets $I$ and $A$. (source: Polynomial Functors, p. 29)

- Ex 2.16 (p. 29): constants $I = Iy^0$, representables and linear polynomials are monomials ("linear" differs from the high-school sense). Ex 2.18 (p. 30): directions as menu options; $y^A$ has one position and $A$ as directions.
- Ex 2.19 (p. 30): a coin jar with a slot, $q = \{\text{open}\}\,y^{\{\text{penny, nickel, dime, quarter}\}} + \{\text{closed}\}\,y^0$. It reappears as an interaction protocol in [[Dependent lens]].
- Def 7.47 (p. 254): the degree of a position is the set of its directions; degree 1 is linear (see [[Polynomial comonoid]]).

### Trees and corolla forests

- Defs 2.21-2.22 (p. 31): rooted tree, rooted path, height. Def 2.23 (p. 32): a corolla is a rooted tree whose non-root vertices have height 1. Exs 2.24, 2.25: the corolla of $y^A$ has $|A|$ leaves; $y^0 = 1$ is a bare root.
- Def 2.26 (p. 32): the corolla forest of $p$ is the disjoint union of corollas, one per position. Ex 2.27 (p. 33): $y^2 + y + y + 1$ is a forest of 4 corollas. Ex 2.31 (p. 34): the 9 elements of $p(\{a,b\})$ as labelled forests. Ex 2.32 (p. 35): $\sum_{r \in \mathbb{R}} y^{[-|r|, |r|]}$, with continuum-sized positions and directions.

## The category Poly

Poly is the full subcategory of $\mathsf{Set}^{\mathsf{Set}}$ on the polynomial functors, with morphisms the natural transformations, i.e. [[Dependent lens]]es (Def 3.1, p. 41). It has all small coproducts (Prop 3.3), products (Prop 3.56), and is completely distributive (Cor 3.58); every $p$ is the coproduct of its representable summands $y^{p[i]}$ (Cor 3.5). Poly is cartesian closed, complete and cocomplete: [[Poly coproduct]], [[Poly product]]. Three monoidal structures: $+$ with unit $0$, $\otimes$ with unit $y$ ([[Poly parallel product]]), and $\triangleright$ with unit $y$ ([[Poly composition product]]). Relations to Set are in [[Adjunction]]. Overview of the setting: [[Poly (Spivak 2020)]].

## Where it appears
- [[Polynomial equipment interfaces (Bilionis 2026)]] — the interface type of every instrument and example.

## Open questions

Questions 1, 9, 10, 11 in the book's closing list concern the generality of the structure (non-polynomial functors, homotopy types, monads in Poly): see [[Polynomial comonoid]].

**Covered in**: Niu-Spivak, Polynomial Functors ch. 1 (pp. 7-17); ch. 2 (pp. 25-36); ch. 3 (pp. 41-43, 65)
**Sources**: `Bilionis - Polynomial Equipment Interfaces and Experimental Protocols.pdf`; `text_books/Category Theory/Spivak, Niu - Polynomial Functors.pdf`; page numbers are printed pages.
**Last updated**: 2026-11-06

---

## Related pages
- [[Dependent lens]] · [[Poly coproduct]] · [[Poly product]] · [[Poly parallel product]] · [[Poly composition product]] · [[Dynamical system as lens]] · [[Yoneda lemma]] · [[Polynomial comonoid]]
