---
type: paper
area: dsl
source-ref: "Niu-Spivak 2024, ch. 8"
authors: ["[[Nelson Niu]]", "[[David I. Spivak]]"]
year: 2024
venue: book draft
file: "DSL/Spivak, Niu - Polynomial Functors.pdf"
tags: [category-theory]
---

# Polynomial Functors ch8 - Categorical properties of polynomial comonoids

**Summary**: Cofree comonoids on trees, the adjunction between Cat-sharp and Poly, monoids and arrow fields, factorizations and limits in Cat-sharp, and comodules, bicomodules and prafunctors.

**Authors**: Nelson Niu, David I. Spivak · **Year**: 2024 · **File**: `DSL/Spivak, Niu - Polynomial Functors.pdf`

---
## Problem

Study the category $\mathsf{Cat}^\sharp$ of polynomial comonoids: build the cofree comonoid on a polynomial, compute limits, colimits and factorizations, and add comodules, which model functors, opfibrations and bimodule-like maps. (source: Polynomial Functors, ch. 8, pp. 291-340)

## Cofree comonoids (pp. 292-320)

> [!definition] Tree on a polynomial (Def 8.2, p. 292)
> A $p$-tree is a rooted tree in which every vertex $v$ is assigned a $p$-position $i$ and a bijection from the children of $v$ to $p[i]$. The set of $p$-trees is $\mathrm{tree}_p$. (source: Polynomial Functors, p. 292)

- Ex 8.3 (p. 293): partial $p$-trees (pretrees). Def 8.6 (p. 294): a stage-$n$ pretree is an element of $p^{\triangleright n}(1)$. Ex 8.8 (p. 294): trimming. Ex 8.10 (p. 295): actual $p$-trees.
- Prop 8.18 (p. 299): the polynomial $\mathfrak{t}_p = \sum_{T \in \mathrm{tree}_p} y^{\mathrm{vtx}(T)}$ has $p$-trees as positions and rooted paths as directions, with projections $\epsilon^{(n)}_p : \mathfrak{t}_p \to p^{\triangleright n}$ (Ex 8.20, p. 299).
- Prop 8.33 (p. 308): $(\mathfrak{t}_p, \epsilon_p, \delta_p)$ is a polynomial comonoid, the category $\mathbb{T}_p$ whose objects are $p$-trees. Ex 8.34 (p. 309): states and transitions for the cofree case.
- Ex 8.35 (p. 311): $p = 1$ gives the category of 1-trees. Ex 8.37 (p. 311): $p = y$ gives a single ray. Ex 8.38 (p. 312): $p = By$ gives $B$-streams. Ex 8.39 (p. 313): $p = \mathbb{N}y^2$ gives $\mathbb{N}$-labelled binary trees.

> [!theorem] Cofree comonoid (Thm 8.45, p. 315)
> The forgetful functor $U : \mathsf{Cat}^\sharp \to \mathsf{Poly}$ has a right adjoint $\mathbb{T}_- : \mathsf{Poly} \to \mathsf{Cat}^\sharp$. The carrier $\mathfrak{t}_p$ is the limit of the diagram (8.1) $\cdots \to p^{\triangleright 3} \to p^{\triangleright 2} \to p \to y$, whose maps apply $p^{\triangleright n} \triangleright !$ to trim the last stage. For any $C$ with carrier $\mathfrak{c}$,
> $$ \mathsf{Poly}(\mathfrak{c}, p) \cong \mathsf{Cat}^\sharp(C, \mathbb{T}_p). $$
> (source: Polynomial Functors, p. 315)

- Prop 8.49 (p. 317): the induced retrofunctor commutes with $\delta^{(n)}$, $\epsilon^{(n)}_p$ and $\varphi^{\triangleright n}$. Ex 8.50 (p. 317): a halting automaton on $S = \{\bullet, \bullet, \bullet\}$ and $p = y^2 + 1$. Ex 8.51 (p. 318): languages recognised by deterministic automata. Ex 8.52 (p. 318): direction sequences to position sequences.
- Prop 8.55 (p. 319): $\mathbb{T}_p$ is free on a graph. Cor 8.56 (p. 320): every morphism of it is monic and epic.

## Monoids and structure on Cat-sharp (pp. 320-326)

- Prop 8.57 (p. 320): the additive monoid $y^{\mathbb{N}}$ has a $\times$-monoid structure in $\mathsf{Cat}^\sharp$. Cor 8.58 (p. 320): $\mathsf{Cat}^\sharp(C, y^{\mathbb{N}})$, the arrow fields, is a monoid. Thm 8.59 (p. 321): the arrow-fields functor $\mathsf{Cat}^\sharp \to \mathsf{Mon}^{\mathrm{op}}$ is right adjoint to the inclusion of Prop 7.79.
- Props 8.60, 8.61 (pp. 321-322): a commutative square of left adjoints; $y^-$ gives an isomorphism between representable-carrier categories and $\mathsf{Mon}^{\mathrm{op}}$. Prop 8.63 (p. 322): the inclusion of linear comonoids (discrete categories) has a left adjoint.
- Prop 8.64 (p. 323): every retrofunctor factors as a vertical retrofunctor followed by a cartesian one. Prop 8.66 (p. 323): cartesian retrofunctors correspond to discrete opfibrations in Cat. Prop 8.67 (p. 324): vertical maps are the opposite of bijective-on-objects functors. Prop 8.70 (p. 324): $\mathbb{T}$ sends cartesian lenses to cartesian retrofunctors.
- Prop 8.71 (Porst, p. 325): $U : \mathsf{Cat}^\sharp \to \mathsf{Poly}$ is comonadic. Cor 8.72 (p. 325): $\mathsf{Cat}^\sharp$ has all small colimits, created by $U$; Ex 8.73: coproducts are the usual disjoint union. Cor 8.76 (p. 326): it has all small limits, via Thm 8.45 and Thm 5.33.

> [!theorem] Parallel product on Cat-sharp (Prop 8.77, p. 326)
> $(y, \otimes)$ on Poly extends to $\mathsf{Cat}^\sharp$, with $U$ strong monoidal, and the parallel product of two categories is their product in Cat. (source: Polynomial Functors, p. 326)

- Prop 8.79 (p. 327): the cofree functor $p \mapsto \mathbb{T}_p$ is lax monoidal.

## Comodules, bicomodules and prafunctors (pp. 328-338)

- Defs 8.81, 8.84 (p. 328): left and right $C$-comodules over a comonoid in $(\mathcal{C}, y, \triangleright)$. Prop 8.88 (p. 329): left $C$-comodules are functors $C \to \mathsf{Poly}$. Prop 8.89 (p. 330): a right $D$-comodule is a functor $D \to \mathsf{Set}^{m(1)}$. Props 8.90, 8.91 (p. 330); Props 8.94, 8.95 (p. 331): coproducts and products of comodules.
- Def 8.96 (p. 332): a $(C, D)$-bicomodule is a left $C$-comodule and a right $D$-comodule with a coherence law (8.97).

> [!theorem] Coalgebras, opfibrations, copresheaves (Thm 8.100, p. 333)
> For a polynomial comonoid $C$, the following are equivalent (all but the first isomorphic): functors $C \to \mathsf{Set}$; discrete opfibrations over $C$; cartesian retrofunctors to $C$; $C$-coalgebras; constant left $C$-comodules; $(C, 0)$-bicomodules; linear left comodules; representable right comodules (opposite). (source: Polynomial Functors, p. 333)

- Prop 8.104 (Garner, p. 336): $(C, D)$-bicomodules are parametric right adjoints $\mathsf{Set}^D \to \mathsf{Set}^C$. Def 8.105 (p. 336): a prafunctor is such a parametric right adjoint. Ex 8.106 (p. 337): cellular automata as bicomodules; Ex 8.108 (p. 338): running one.

## Limitations

Read at statement level: every Def, Prop, Thm and Example heading of the chapter. Defs 8.2, 8.96 and Thms 8.45, 8.100 and Prop 8.77 were opened in the text. The labels for Props 8.60, 8.61, 8.63, 8.89-8.95 are from the statement listing and are not checked line by line. Proofs and exercises were not read.

## Connections

- Previous: [[Polynomial Functors ch7 - Polynomial comonoids and retrofunctors]]. Next: [[Polynomial Functors ch9 - New horizons]], whose open questions 5, 12 and 13 concern $\mathsf{Cat}^\sharp$ directly.
- Concept pages: [[Polynomial comonoid]], [[Poly composition product]], [[Poly parallel product]] (Prop 8.77), [[Adjunction]].

**Sources**: Niu, Spivak, Polynomial Functors (2024), ch. 8; page numbers are printed pages.
**Last updated**: 2026-11-06

---

## Related pages
[[Polynomial comonoid]] · [[Poly composition product]] · [[Poly parallel product]] · [[Adjunction]] · [[Universal property]]
