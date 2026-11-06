---
type: paper
area: dsl
source-ref: "Niu-Spivak 2024, ch. 7"
authors: ["[[Nelson Niu]]", "[[David I. Spivak]]"]
year: 2024
venue: book draft
file: "text_books/Category Theory/Spivak, Niu - Polynomial Functors.pdf"
tags: [category-theory]
---

# Polynomial Functors ch7 - Polynomial comonoids and retrofunctors

**Summary**: Comonoids in (Poly, y, tri) are small categories (Ahman-Uustalu), with positions as objects and directions as morphisms; their morphisms are retrofunctors, and coalgebras of a comonoid are discrete opfibrations or copresheaves.

**Authors**: Nelson Niu, David I. Spivak · **Year**: 2024 · **File**: `text_books/Category Theory/Spivak, Niu - Polynomial Functors.pdf`

---
## Problem

State systems from ch. 4 carry extra structure: a do-nothing section and a transition lens. This chapter shows that structure is a comonoid for the composition product and that comonoids in general are exactly categories. (source: Polynomial Functors, ch. 7, pp. 227-289)

## State systems as comonoids (pp. 228-240)

- Ex 7.3 (p. 228): the do-nothing section in tree pictures. Ex 7.6 (p. 230): the transition lens $\delta : \mathfrak{s} \to \mathfrak{s} \triangleright \mathfrak{s}$ of $\mathfrak{s} = 3y^3$ in tree pictures. Ex 7.13 (p. 236): a system returning every other position.

> [!definition] Comonoid (Def 7.14, p. 237)
> In a monoidal category $(\mathcal{C}, y, \triangleright)$, a comonoid $(\mathfrak{c}, \epsilon, \delta)$ has a carrier $\mathfrak{c}$, an eraser $\epsilon : \mathfrak{c} \to y$ and a duplicator $\delta : \mathfrak{c} \to \mathfrak{c} \triangleright \mathfrak{c}$, obeying left and right erasure laws (7.15) and the coassociative law (7.16). A comonoid in Poly is a polynomial comonoid. (source: Polynomial Functors, p. 237)

- Ex 7.19 (p. 238): every state system $Sy^S$ with its do-nothing section and transition lens is a polynomial comonoid. Prop 7.20 (p. 238): $\delta^{(n)} : \mathfrak{c} \to \mathfrak{c}^{\triangleright n}$ defined inductively from $\delta^{(0)} = \epsilon$.
- Ex 7.22 (p. 239): not every polynomial comonoid is a state system. Ex 7.23 (p. 239): $y^2 + y$ is a comonoid but not a state system, since one direction-set has one fewer element than the position-set.

## Comonoids are categories (pp. 241-253)

> [!theorem] Ahman-Uustalu (Thm 7.28, p. 241)
> There is a one-to-one, isomorphism-preserving correspondence between polynomial comonoids and small categories. Positions are objects and directions are morphisms: $\mathfrak{c}(1) = \mathrm{Ob}\, C$ and $\mathfrak{c}[i]$ is the set of morphisms with domain $i$. (source: Polynomial Functors, pp. 241-242)

> [!definition] Polynomial carrier (Def 7.31, p. 242)
> For a category $C$, write $C[i] = \sum_{j \in \mathrm{Ob}\, C} C(i, j)$ for the morphisms out of $i$. The carrier of $C$ is
> $$ \sum_{i \in \mathrm{Ob}\, C} y^{C[i]}. $$
> (source: Polynomial Functors, p. 242)

- Ex 7.34 (p. 248): the walking arrow $\mathfrak{a} = \{s\}\,y^{\{\mathrm{id}_s, a\}} + \{t\}\,y^{\{\mathrm{id}_t\}} = y^2 + y$ as a category. Ex 7.38 (p. 249): state systems are the categories with one morphism between each pair of objects.
- Ex 7.40 (p. 251): a monoid is a representable comonoid $y^M$. Ex 7.42 (p. 252): cyclic lists, $\mathbb{Z}/n$ with carrier $y^{\mathbb{Z}/n}$. Ex 7.43 (p. 252): monoid actions. Ex 7.45 (p. 253): the category of $B$-streams.
- Def 7.47 (p. 254): the degree of an object is the set of arrows out of it; degree 1 is linear.

## Retrofunctors (pp. 254-270)

- Def 7.49 (p. 255): a comonoid morphism is a lens commuting with $\epsilon$ and $\delta$.

> [!definition] Retrofunctor (Def 7.55, p. 256)
> For small categories $C, C'$, a retrofunctor $F : C \nrightarrow C'$ is a function $F : \mathrm{Ob}\, C \to \mathrm{Ob}\, C'$ and, for each $c$, a backward function $F^\sharp_c : C'[Fc] \to C[c]$, with three laws: identities are preserved ($F^\sharp_c(\mathrm{id}_{Fc}) = \mathrm{id}_c$), codomains are preserved ($F(\mathrm{cod}\, F^\sharp_c g) = \mathrm{cod}\, g$), and composites are preserved (eq. 7.58). The category of small categories and retrofunctors is $\mathsf{Cat}^\sharp$, equal to $\mathrm{Comon}(\mathsf{Poly})$. (source: Polynomial Functors, p. 256)

- Prop 7.61 (p. 258): if $g : Fc \to \_$ is an isomorphism in $D$, then $F^\sharp_c g$ is an isomorphism in $C$. Ex 7.63 (p. 259): retrofunctors to discrete categories. Ex 7.65 (p. 260): to the walking arrow. Ex 7.68 (p. 260): to the walking commutative square.
- Ex 7.71 (p. 262): retrofunctors $C \nrightarrow y^{\mathbb{N}}$ are arrow fields, called admissible sections in earlier literature. Ex 7.77 (p. 263): groups $G$ and $y^G$. Prop 7.79 (p. 264): a fully faithful $\mathsf{Mon}^{\mathrm{op}} \to \mathsf{Cat}^\sharp$ onto categories with representable carriers. Prop 7.80 (p. 264): $\mathsf{Cat}^\sharp(C, Ay) \cong \mathsf{Set}(\mathrm{Ob}\, C, A)$.
- Ex 7.82 (p. 265): systems of ODEs. Ex 7.84 (p. 266): retrofunctors from state categories to $C$ are $C$-coalgebras. Ex 7.85 (p. 266): retrofunctors between state categories are very well-behaved lenses. Ex 7.88 (p. 268), Ex 7.90 (p. 269): objects are not representable in $\mathsf{Cat}^\sharp$.

## Coalgebras and opfibrations (pp. 271-277)

- Def 7.96 (p. 271): a coalgebra for a polynomial comonoid. Prop 7.98 (p. 271): retrofunctors $Sy^S \nrightarrow C$ are $C$-coalgebras carried by $S$.
- Def 7.99 (p. 273): a discrete opfibration $\pi : S \to C$ lifts every morphism out of $\pi(s)$ uniquely. Prop 7.103 (p. 274): $C$-coalgebras are the same as $\mathrm{dopf}(C)$. Def 7.104 (p. 274): category of elements. Props 7.108, 7.109 (pp. 275-276): copresheaves $\mathsf{Set}^C$ are equivalent to discrete opfibrations, which are dynamical systems on $C$.

## Limitations

Read at statement level: every Def, Prop, Thm and Example heading of the chapter. Defs 7.14, 7.31, 7.47, 7.55, 7.99 and Thm 7.28 were opened in the text. Ex 7.111 (database schema from a dynamical system, p. 276) and the summary section 7.4 are not summarised. Proofs and exercises were not read.

## Connections

- Previous: [[Polynomial Functors ch6 - The composition product]]. Next: [[Polynomial Functors ch8 - Categorical properties of polynomial comonoids]].
- Concept pages: [[Polynomial comonoid]], [[Poly composition product]], [[Category]]. Naming: the book calls these maps retrofunctors; the same notion elsewhere is a cofunctor, and Cat-sharp is the category of categories and retrofunctors.

**Sources**: Niu, Spivak, Polynomial Functors (2024), ch. 7; page numbers are printed pages.
**Last updated**: 2026-11-06

---

## Related pages
[[Polynomial comonoid]] · [[Poly composition product]] · [[Category]] · [[Functor]] · [[Moore machine]]
