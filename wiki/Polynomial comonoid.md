---
type: theorem
area: dsl
source-ref: "Niu-Spivak 2024, Thm. 7.28; Spivak 2020, §3"
tags: [category-theory]
---

# Polynomial comonoid

**Summary**: A comonoid in $(\mathrm{Poly},y,\circ)$ is a small category; their morphisms are retrofunctors (cofunctors), forming Cat$^\sharp$. Coalgebras of a comonoid are discrete opfibrations, equivalently copresheaves.

---

> [!definition] Comonoid (Def 7.14, p. 237)
> In a monoidal category $(\mathcal{C}, y, \triangleright)$, a comonoid $(\mathfrak{c}, \epsilon, \delta)$ has a carrier $\mathfrak{c}$, an eraser $\epsilon : \mathfrak{c} \to y$ and a duplicator $\delta : \mathfrak{c} \to \mathfrak{c} \triangleright \mathfrak{c}$, obeying left and right erasure laws (7.15) and the coassociative law (7.16). A comonoid in Poly is a polynomial comonoid. (source: Polynomial Functors, p. 237)

> [!theorem] Ahman-Uustalu (Thm 7.28, p. 241)
> There is a one-to-one, isomorphism-preserving correspondence between polynomial comonoids and small categories, under the [[Poly composition product]]. Positions are objects and directions are morphisms: $\mathfrak{c}(1) = \mathrm{Ob}\, C$ and $\mathfrak{c}[i]$ is the set of morphisms with domain $i$. (source: Polynomial Functors, pp. 241-242; Poly, Thm. 2.6)

> [!definition] Polynomial carrier (Def 7.31, p. 242)
> For a category $C$, write $C[i] = \sum_{j \in \mathrm{Ob}\, C} C(i, j)$ for the morphisms out of $i$. The carrier of $C$ is $\sum_{i \in \mathrm{Ob}\, C} y^{C[i]}$. (source: Polynomial Functors, p. 242)

## Intuition

Positions are objects, directions at an object are morphisms out of it, and carrier $= \sum_i y^{C[i]}$. The eraser picks the identity and the duplicator composes. A morphism of comonoids is a [[Retrofunctor]]: a map $F$ on objects and, for each $c$, $F^\sharp_c : C'[Fc]\to C[c]$ (Defs. 7.49, 7.55). The contractible groupoid $Sy^S$ is the store comonad (Poly 2020).

## State systems and examples

- Ex 7.3 (p. 228), Ex 7.6 (p. 230): the do-nothing section and the transition lens $\delta : \mathfrak{s} \to \mathfrak{s} \triangleright \mathfrak{s}$ of $\mathfrak{s} = 3y^3$ in tree pictures. Ex 7.13 (p. 236): a system returning every other position.
- Ex 7.19 (p. 238): every state system $Sy^S$ with its do-nothing section and transition lens is a polynomial comonoid; Ex 7.38 (p. 249): state systems are the categories with exactly one morphism between each pair of objects. Prop 7.20 (p. 238): $\delta^{(n)} : \mathfrak{c} \to \mathfrak{c}^{\triangleright n}$ defined inductively from $\delta^{(0)} = \epsilon$. See [[Moore machine]].
- Ex 7.22 (p. 239), Ex 7.23: not every polynomial comonoid is a state system; $y^2 + y$ is a comonoid but not a state system, since one direction-set has one fewer element than the position-set.
- Ex 7.34 (p. 248): the walking arrow $\mathfrak{a} = \{s\}\,y^{\{\mathrm{id}_s, a\}} + \{t\}\,y^{\{\mathrm{id}_t\}} = y^2 + y$.
- Ex 7.40 (p. 251): a monoid is a representable comonoid $y^M$. Ex 7.42 (p. 252): cyclic lists, $\mathbb{Z}/n$ with carrier $y^{\mathbb{Z}/n}$. Ex 7.43 (p. 252): monoid actions. Ex 7.45 (p. 253): the category of $B$-streams.
- Def 7.47 (p. 254): the degree of an object is the set of arrows out of it; degree 1 is linear.

## Coalgebras, opfibrations and copresheaves

- Def 7.96 (p. 271): a coalgebra for a polynomial comonoid. Prop 7.98 (p. 271): retrofunctors $Sy^S \nrightarrow C$ are $C$-coalgebras carried by $S$: [[Moore machine]], [[Dynamical system as lens]].
- Def 7.99 (p. 273): a discrete opfibration $\pi : S \to C$ lifts every morphism out of $\pi(s)$ uniquely. Prop 7.103 (p. 274): $C$-coalgebras are the same as $\mathrm{dopf}(C)$. Def 7.104 (p. 274): category of elements. Props 7.108, 7.109 (pp. 275-276): copresheaves $\mathsf{Set}^C$ are equivalent to discrete opfibrations, which are dynamical systems on $C$. Ex 7.111 (p. 276): a database schema from a dynamical system.
- Cartesian retrofunctors are discrete opfibrations (Prop 8.66): [[Vertical and cartesian lens]].

## Comodules, bicomodules and prafunctors

- Defs 8.81, 8.84 (p. 328): left and right $C$-comodules over a comonoid in $(\mathcal{C}, y, \triangleright)$. Prop 8.88 (p. 329): left $C$-comodules are functors $C \to \mathsf{Poly}$. Prop 8.89 (p. 330): a right $D$-comodule is a functor $D \to \mathsf{Set}^{m(1)}$. Props 8.90, 8.91 (p. 330), Props 8.94, 8.95 (p. 331): coproducts and products of comodules.
- Def 8.96 (p. 332): a $(C, D)$-bicomodule is a left $C$-comodule and a right $D$-comodule with a coherence law (8.97).

> [!theorem] Coalgebras, opfibrations, copresheaves (Thm 8.100, p. 333)
> For a polynomial comonoid $C$, the following are equivalent (all but the first isomorphic): functors $C \to \mathsf{Set}$; discrete opfibrations over $C$; cartesian retrofunctors to $C$; $C$-coalgebras; constant left $C$-comodules; $(C, 0)$-bicomodules; linear left comodules; representable right comodules (opposite). (source: Polynomial Functors, p. 333)

- Prop 8.104 (Garner, p. 336): $(C, D)$-bicomodules are parametric right adjoints $\mathsf{Set}^D \to \mathsf{Set}^C$. Def 8.105 (p. 336): a prafunctor is such a parametric right adjoint. Ex 8.106 (p. 337): cellular automata as bicomodules; Ex 8.108 (p. 338): running one.

## The category Cat-sharp

- Cofree comonoids (trees, Thm 8.45): [[Cofree comonoid on a polynomial]]. Retrofunctors, factorizations, limits, colimits, monoids and arrow fields (Props 8.57-8.77): [[Retrofunctor]], [[Vertical and cartesian lens]]. The parallel product extends to Cat$^\sharp$ (Prop 8.77): [[Poly parallel product]].

## Open questions

The book closes with fourteen unorganised questions (the authors say they may or may not be known and are not complete). Grouped by the wiki (the book's list is flat):

- Generality: (1) comonoids in all functors $\mathsf{Set} \to \mathsf{Set}$, including non-polynomial ones; (9) replacing sets by homotopy types in the theory of sums of representables; (10) non-polynomial functors carrying a $(y, \triangleright)$ comonoid structure; (11) characterise the monads in Poly, which generalise one-object (cartesian) operads.
- Logic and semantics of systems: (2) the internal logic of the topos $[\mathbb{T}_p, \mathsf{Set}]$ of dynamical systems with interface $p$; (3) how that logic helps reason about dynamical systems; (4) a morphism $p \to q$ gives a left adjoint $[\mathbb{T}_p, \mathsf{Set}] \to [\mathbb{T}_q, \mathsf{Set}]$ preserving connected limits, which is worse than a geometric morphism (no terminal object) and better (all connected limits), so how does it translate internal-language statements?; (14) are there polynomials whose proposition-topos $[\mathrm{tree}_p, \mathsf{Set}]$ can be Godel-encoded in a language $p$-systems can use? Related: sheaf-topos logic in Seven Sketches ch. 7.
- Structure of $\mathsf{Cat}^\sharp$ and $\mathsf{Mod}$: (5) $\times$-monoids and $\otimes$-monoids in Poly, $\mathsf{Cat}^\sharp$ and $\mathsf{Mod}$; (6) a functor from the bicategory of spans in Poly to $\mathsf{Mod}$ sending $p \mapsto \mathbb{T}_p$; (12) a combinatorial description of limits in $\mathsf{Cat}^\sharp$; (13) whether all monos in $\mathsf{Cat}^\sharp$ are detected by the faithful $U$. The chapter does not define $\mathsf{Mod}$; the wiki did not check where the book does **[unverified]**.
- Databases: (7) how static databases and dynamical systems interact (reading and writing); (8) database aggregation done dynamically.

**Covered in**: Niu-Spivak, Polynomial Functors ch. 7 (pp. 228-277); ch. 8 (pp. 328-338); ch. 9 (pp. 349-350)
**Sources**: Niu, Spivak, Polynomial Functors (2024), ch. 7, 8, 9; Spivak, Poly (2020); `text_books/Category Theory/Spivak, Niu - Polynomial Functors.pdf`. Page numbers are printed pages.
**Last updated**: 2026-11-06

---

## Related pages
[[Poly composition product]] · [[Category]] · [[Functor]] · [[Polynomial functor]] · [[Moore machine]] · [[Retrofunctor]] · [[Cofree comonoid on a polynomial]] · [[Vertical and cartesian lens]] · [[Dynamical system as lens]] · [[Poly parallel product]]
