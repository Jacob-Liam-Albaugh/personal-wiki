---
type: theorem
area: dsl
source-ref: "Niu-Spivak 2024, Thm 8.45"
tags: [category-theory]
---

# Cofree comonoid on a polynomial

**Summary**: The forgetful functor from polynomial comonoids to Poly has a right adjoint sending $p$ to the category $\mathbb{T}_p$ of $p$-trees. Retrofunctors into $\mathbb{T}_p$ are the same as lenses into $p$, which is how dynamical systems with interface $p$ become comonoid morphisms.

---

> [!definition] Tree on a polynomial (Def 8.2, p. 292)
> A $p$-tree is a rooted tree in which every vertex $v$ is assigned a $p$-position $i$ and a bijection from the children of $v$ to $p[i]$. The set of $p$-trees is $\mathrm{tree}_p$. (source: Polynomial Functors, p. 292)

- Ex 8.3 (p. 293): partial $p$-trees (pretrees). Def 8.6 (p. 294): a stage-$n$ pretree is an element of $p^{\triangleright n}(1)$ (see [[Poly composition product]]). Ex 8.8 (p. 294): trimming. Ex 8.10 (p. 295): actual $p$-trees.
- Prop 8.18 (p. 299): the polynomial $\mathfrak{t}_p = \sum_{T \in \mathrm{tree}_p} y^{\mathrm{vtx}(T)}$ has $p$-trees as positions and rooted paths as directions, with projections $\epsilon^{(n)}_p : \mathfrak{t}_p \to p^{\triangleright n}$ (Ex 8.20, p. 299).
- Prop 8.33 (p. 308): $(\mathfrak{t}_p, \epsilon_p, \delta_p)$ is a [[Polynomial comonoid]], the category $\mathbb{T}_p$ whose objects are $p$-trees. Ex 8.34 (p. 309): states and transitions for the cofree case.

> [!theorem] Cofree comonoid (Thm 8.45, p. 315)
> The forgetful functor $U : \mathsf{Cat}^\sharp \to \mathsf{Poly}$ has a right adjoint $\mathbb{T}_- : \mathsf{Poly} \to \mathsf{Cat}^\sharp$. The carrier $\mathfrak{t}_p$ is the limit of the diagram (8.1) $\cdots \to p^{\triangleright 3} \to p^{\triangleright 2} \to p \to y$, whose maps apply $p^{\triangleright n} \triangleright !$ to trim the last stage. For any category $C$ with carrier $\mathfrak{c}$,
> $$ \mathsf{Poly}(\mathfrak{c}, p) \cong \mathsf{Cat}^\sharp(C, \mathbb{T}_p). $$
> (source: Polynomial Functors, p. 315)

See [[Adjunction]] and [[Retrofunctor]].

## Examples

- Ex 8.35 (p. 311): $p = 1$ gives the category of 1-trees. Ex 8.37 (p. 311): $p = y$ gives a single ray. Ex 8.38 (p. 312): $p = By$ gives $B$-streams. Ex 8.39 (p. 313): $p = \mathbb{N}y^2$ gives $\mathbb{N}$-labelled binary trees.
- Prop 8.49 (p. 317): for a system $\varphi : Sy^S \to p$ ([[Dynamical system as lens]]), the induced retrofunctor commutes with $\delta^{(n)}$, $\epsilon^{(n)}_p$ and $\varphi^{\triangleright n}$. Ex 8.50 (p. 317): a halting automaton on three states with $p = y^2 + 1$. Ex 8.51 (p. 318): languages recognised by deterministic automata. Ex 8.52 (p. 318): direction sequences to position sequences.

## Properties

- Prop 8.55 (p. 319): $\mathbb{T}_p$ is free on a graph. Cor 8.56 (p. 320): every morphism of it is monic and epic.
- Prop 8.70 (p. 324): $\mathbb{T}$ sends cartesian lenses to cartesian retrofunctors ([[Vertical and cartesian lens]]).
- Prop 8.79 (p. 327): $p \mapsto \mathbb{T}_p$ is lax monoidal for $\otimes$ ([[Poly parallel product]]).
- Cor 8.76 (p. 326): with Thm 5.33, this gives all small limits in $\mathsf{Cat}^\sharp$.

**Covered in**: Niu-Spivak, Polynomial Functors ch. 8 (pp. 292-320, 324-327)
**Sources**: `text_books/Category Theory/Spivak, Niu - Polynomial Functors.pdf`; page numbers are printed pages. Proofs and exercises were not read.
**Last updated**: 2026-11-06

---

## Related pages
[[Polynomial comonoid]] · [[Retrofunctor]] · [[Poly composition product]] · [[Dynamical system as lens]] · [[Adjunction]] · [[Moore machine]]
