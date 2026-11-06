---
type: concept
area: dsl
source-ref: "Fong-Spivak 2019, Defs. 5.2, 5.25, 5.36, 5.45, 5.50, 5.65, 5.79, Thms. 5.60, 5.87"
tags: [category-theory]
---

# Signal flow graph

**Summary**: Props and their presentations: signal flow graphs (wires, copy, add, scalars) form the free prop on a signature whose semantics is the prop of matrices; passing to relations adds feedback.

---

Signal flow graphs are used in control theory. They are made a prop, shown to present exactly the prop of matrices, and extended with feedback by passing to relations.

## Props

> [!definition] Prop
> A symmetric strict [[Monoidal category]] $(\mathcal C,0,+)$ whose objects are $\mathbb N$, with unit $0$ and product on objects given by addition. Object $n$ is $n$ copies of the generating object $1$. (source: Seven Sketches, Def. 5.2, p. 149)

- Examples (p. 150): FinSet with functions $m\to n$ (Ex. 5.3), the prop of bijections (Ex. 5.6), the compact closed prop Corel (Ex. 5.7), the prop Rel of relations (Ex. 5.8).
- A prop functor is identity-on-objects and strict symmetric monoidal (Def. 5.11); Ex. 5.12: $\mathrm{Bij}\to\mathrm{FinSet}$. See [[Functor]].

## Port graphs and free props

- An $(m,n)$-port graph is vertices with in and out degrees and a bijection $\iota : m\sqcup O\to I\sqcup n$ obeying an acyclicity condition (no loops in the internal flow graph) (Def. 5.13, p. 151; example Ex. 5.14).
- A prop signature $(G,s,t)$ has in- and out-arities; $\mathrm{Free}(G)$ has $G$-labelled port graphs as morphisms (Def. 5.25, p. 155). The free prop on the empty signature is Bij (Ex. 5.27).
- Prop. 5.29 (p. 156): prop functors $\mathrm{Free}(G)\to\mathcal C$ correspond one-to-one with functions sending each generator $g$ to a morphism $s(g)\to t(g)$ in $\mathcal C$. A presented prop $\langle G\mid E\rangle$ also has a universal property (Remark 5.34): [[Universal property]].
- $G$-generated prop expressions are built from generators with $\mathbin{;}$, $+$, identities and symmetries (Def. 5.30, Ex. 5.31). Analogies: free preorder on a relation (Ex. 5.19), free category on a graph (Ex. 5.22, [[Category]]).

## Rigs and signal flow graphs

> [!definition] Rig
> A tuple $(R,0,+,1,*)$ with $(R,0,+)$ a commutative monoid, $(R,1,*)$ a monoid, $*$ distributing over $+$, and $0$ annihilating. Examples: $\mathbb N$, Booleans, quantales, square matrices, rings such as $\mathbb R$ (Exs. 5.37-5.42). (source: Seven Sketches, Def. 5.36, p. 159)

- Generators: copy, discard, add, zero and a scalar $a$ for each $a\in R$; $\mathrm{SFG}_R:=\mathrm{Free}(G_R)$ (Def. 5.45, p. 163). Ex. 5.44: a linear ODE system as a signal flow graph.
- $\mathrm{Mat}(R)$ has $(m\times n)$-matrices as morphisms, composition by matrix product and direct sum as the monoidal product (Def. 5.50, p. 164).
- Semantics: a prop functor $S:\mathrm{SFG}_R\to\mathrm{Mat}(R)$ defined on generators (Thm. 5.53, p. 166). $S(g)_{ij}$ is the amplification of input $i$ that contributes to output $j$ (Prop. 5.54). $S$ is full: every matrix comes from a signal flow graph (Prop. 5.56, p. 169).

> [!theorem] Complete presentation of matrices
> $\mathrm{Mat}(R)$ is isomorphic to the prop presented by $G_R$ with equations: commutative monoid laws for add/zero, cocommutative comonoid laws for copy/discard, bialgebra laws, and scalar multiplication and addition laws. The proof rewrites to a normal form (black nodes left, scalars middle, white nodes right). (source: Seven Sketches, Thm. 5.60, p. 170)

Ex. 5.61: two graphs, one matrix. The equations are summarised, not transcribed, from the book's diagram notation. Over cospans the bialgebra structure is replaced by Frobenius structure: [[Hypergraph category]].

## Monoid objects and feedback

- A monoid object $(M,\mu,\eta)$ in a symmetric monoidal category, commutative if $\sigma;\mu=\mu$ (Def. 5.65, p. 172). Exs. 5.66-5.73: ordinary monoids in $(\mathsf{Set},1,\times)$, symmetric monoidal preorders as commutative monoid objects in Cat, rigs as monoid objects. A prop presented by $\mu,\eta$ and the three equations (Remark 5.74).
- The prop $\mathrm{Rel}_R$ has subsets $B\subseteq R^m\times R^n$ as morphisms (Def. 5.79, p. 175); "full" signal flow graphs with feedback map to linear relations, with a sound and complete presentation (p. 177).
- $\mathrm{Rel}_R$ is compact closed, every object self-dual (cup, cap) (Thm. 5.87, p. 178). The chapter closes with a car-speed control example over $R[s,s^{-1}]$.

## Where it appears

Compact closed structure of the same kind arises for profunctors: [[Profunctor]]. The operad version of wiring: [[Operad]].

**Covered in**: Fong-Spivak (Seven Sketches) ch. 5 (pp. 147-181, props, port graphs, free props, rigs, signal flow graphs, matrices, monoid objects, relations with feedback)
**Sources**: Fong, Spivak, Seven Sketches (2019), ch. 5; file `text_books/Category Theory/Spivak, Fong - Seven Sketches in Compositionality.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
[[Monoidal category]] · [[Category]] · [[Functor]] · [[Universal property]] · [[Operad]] · [[Hypergraph category]] · [[Profunctor]]
