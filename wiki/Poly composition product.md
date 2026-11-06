---
type: definition
area: dsl
source-ref: "Niu-Spivak 2024, ch. 6; Spivak 2020, §2"
tags: [category-theory]
---

# Poly composition product

**Summary**: The substitution product $p \circ q$ (also written $p \triangleright q$) of polynomial functors, defined as functor composition; a non-symmetric monoidal structure on Poly with unit $y$ whose comonoids are small categories.

---

> [!definition] Composition product (Def 6.1, p. 180)
> For polynomial functors $p, q$, the composition product $p \circ q : \mathsf{Set} \to \mathsf{Set}$ is their composite as functors. It sends a set $X$ to $p(q(X))$. (source: Polynomial Functors, Def 6.1, p. 180)

## Formula

> [!theorem] Composite is polynomial (Prop 6.2, eq 6.3 and 6.4; p. 180)
> $$ p \circ q \cong \sum_{i \in p(1)} \prod_{a \in p[i]} \sum_{j \in q(1)} \prod_{b \in q[j]} y. $$
> Pushing the products past the sums gives
> $$ p \circ q \cong \sum_{i \in p(1)} \sum_{j : p[i] \to q(1)} y^{\sum_{a \in p[i]} q[j(a)]}. $$
> (source: Polynomial Functors, Prop 6.2, p. 180)

Reading the second formula: a position of $p \circ q$ is a position $i$ of $p$ together with a position $j(a)$ of $q$ for each direction $a$ at $i$. A direction there is a pair $(a, b)$ with $b \in q[j(a)]$. (source: Polynomial Functors, p. 180)

Example, from Poly 2020:

$$(y^2+y)\circ(y^3+1) = y^6+3y^3+2$$

(source: Spivak - Poly.pdf, §2)

## Notation

> [!theorem] Monoidal structure (Cor 6.5, p. 180)
> $(\mathsf{Poly}, y, \circ)$ is monoidal with unit $y$, the identity functor. The book writes $p \triangleright q := p \circ q$, because $\circ$ also denotes composition in arbitrary categories and $\triangleright$ shows the asymmetry. (source: Polynomial Functors, Cor 6.5, p. 180)

- $p^{\triangleright n}$ is the $n$-fold composition product, with $p^{\triangleright 0} = y$ and $p^{\triangleright 1} = p$ (p. 181).
- Poly 2020 writes $\circ$ throughout. Both symbols name the same operation.

## Properties

- Left distributes over $+$ and $\times$ (Prop 6.47, p. 204).
- Preserves limits on the left (Prop 6.68, p. 209) and connected limits on both sides (Thm 6.80, p. 212).
- Duoidal with the parallel product $\otimes$ (Prop 6.87, p. 214). See [[Poly parallel product]]. A cartesian lens $p \otimes q \to p \triangleright q$ exists (Ex 6.85, p. 213).
- Preserves cartesian lenses (Prop 6.88, p. 215).

(source: Polynomial Functors, ch. 6)

## Examples and lenses

- Def 6.11 (p. 182): horizontal composition of natural transformations, which gives the action of $\triangleright$ on lenses.
- Ex 6.27 (p. 187): composing with constants, $p(X)$ for a set $X$. Ex 6.31 (p. 188): $p = q = y^2 + y$, $p' = y^3 + y$, $q' = y + 1$ drawn as forests.
- Ex 6.36 (p. 191): substitution products of dynamical systems as trees, using the halting automaton $p = y^A + 1$. Ex 6.38 (p. 193): composition products of dynamical systems can be misleading.
- Ex 6.40 (p. 195): a lens $\varphi : p \to q \triangleright r$ drawn in polyboxes; the cases $n = 0, 1, 2$ of lenses into $q_1 \triangleright \cdots \triangleright q_n$ recover earlier pictures (3.34), (3.13), (6.39). Ex 6.41 (p. 197): dynamical systems with composite interfaces.
- Ex 6.43 (p. 199): the $n$-fold product $\varphi^{\triangleright n}$ of a dynamical system $\varphi : Sy^S \to p$. Ex 6.44 (p. 200): transition lenses for state systems. See [[Dynamical system as lens]].
- Ex 6.67 (p. 208): taking $A = B = S$ in (6.65), dynamical systems $Sy^S \to p$ are coalgebras of the polynomial functor $p$.

## Algebraic properties in detail

- Prop 6.47 (p. 204): $-\triangleright r$ commutes with coproducts and products; Ex 6.53 (p. 205) pictures the case of $\times$.
- Prop 6.57 (Meyers, p. 206): $\triangleright$ is left coclosed, with a coclosure operation $\mathsf{Poly}^{\mathrm{op}} \times \mathsf{Poly} \to \mathsf{Poly}$.
- Def 6.71 (p. 209): a connected limit is one over a nonempty connected index category; equalizers, pullbacks and directed limits are examples (Ex 6.72). Prop 6.73 (p. 210): a natural isomorphism for lenses into $q \triangleright r$ over $q \triangleright 1$. Prop 6.83 (p. 213): tensoring with $q$ preserves connected limits.
- Ex 6.85 (p. 213): the cartesian lens $o_{p,q} : p \otimes q \to p \triangleright q$ orders the two operations; Prop 6.87 (p. 214): $(y, \otimes)$ and $(y, \triangleright)$ form a duoidal structure on Poly, the key being the natural lens (6.86).
- Comonoids for $(y, \triangleright)$ in other categories: Def 7.14 (p. 237) defines a comonoid in any monoidal category $(\mathcal{C}, y, \triangleright)$; the structure on $\mathsf{Cat}^\sharp$ and the cofree comonoid are in [[Cofree comonoid on a polynomial]] and [[Retrofunctor]]. Cartesian lenses: [[Vertical and cartesian lens]].

## Why it matters

- Comonoids for $(y, \triangleright)$ are small categories (Thm 7.28, p. 241); see [[Polynomial comonoid]]. Monoids are polynomial monads.
- A lens $Sy^S \to p$ (a [[Moore machine]] or [[Dynamical system as lens]]) has an $n$-step version into $p^{\triangleright n}$ (Ex 6.43, p. 199).
- Wiki note: $p \circ q$ models sequential interaction, a $p$-mode followed by a $q$-mode for each direction that comes back. Compare [[Sequential protocol composition]].

## Where it appears

[[Poly (Spivak 2020)]] · [[Polynomial equipment interfaces (Bilionis 2026)]]

**Covered in**: Niu-Spivak, Polynomial Functors ch. 6 (pp. 179-216)
**Sources**: Niu-Spivak, Polynomial Functors (2024), ch. 6; Spivak, Poly (2020), §2; `text_books/Category Theory/Spivak, Niu - Polynomial Functors.pdf`. Page numbers are printed pages. Proofs and exercises were not read.
**Last updated**: 2026-11-06

---

## Related pages
[[Polynomial functor]] · [[Dependent lens]] · [[Poly product]] · [[Poly coproduct]] · [[Poly parallel product]] · [[Monoidal category]] · [[Polynomial comonoid]] · [[Sequential protocol composition]] · [[Dynamical system as lens]] · [[Cofree comonoid on a polynomial]] · [[Vertical and cartesian lens]]
