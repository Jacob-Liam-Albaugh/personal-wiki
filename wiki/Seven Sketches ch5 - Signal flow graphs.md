---
type: paper
area: dsl
source-ref: "Fong-Spivak 2019, ch. 5"
authors: ["[[Brendan Fong]]", "[[David I. Spivak]]"]
year: 2019
venue: book (Cambridge University Press)
file: "text_books/Category Theory/Spivak, Fong - Seven Sketches in Compositionality.pdf"
tags: [category-theory]
---

# Seven Sketches ch5 - Signal flow graphs

**Summary**: Props and presentations: free props from signatures, rigs, signal flow graphs and their matrix semantics, a complete equational presentation, monoid objects, and the prop of relations with feedback.

**Authors**: Brendan Fong, David I. Spivak · **Year**: 2019 · **File**: `text_books/Category Theory/Spivak, Fong - Seven Sketches in Compositionality.pdf`

---
## Problem

Signal flow graphs (wires, copy, add, scalars) are used in control theory. The chapter makes them a prop, shows that they present exactly the prop of matrices, and adds feedback by passing to relations. (source: Seven Sketches, ch. 5, pp. 147-181)

## Props (pp. 149-151)

> [!definition] Prop (Def 5.2, p. 149)
> A symmetric strict monoidal category $(\mathcal{C}, 0, +)$ whose objects are $\mathbb{N}$, with unit $0$ and product on objects given by addition. Object $n$ is $n$ copies of the generating object $1$. (source: Seven Sketches, p. 149)

- Examples (p. 150): FinSet with functions $m \to n$ (Ex 5.3), the prop of bijections (Ex 5.6), the compact closed prop Corel (Ex 5.7), the prop Rel of relations (Ex 5.8).
- Def 5.11 (p. 151): a prop functor is identity-on-objects and strict symmetric monoidal. Ex 5.12 (p. 151): $\mathrm{Bij} \to \mathrm{FinSet}$ inclusion.

## Port graphs and free props (pp. 151-159)

- Def 5.13 (p. 151): an $(m,n)$-port graph is vertices with in and out degrees, with a bijection $\iota : m \sqcup O \to I \sqcup n$ obeying an acyclicity condition (no loops in the internal flow graph). Ex 5.14 (p. 152): a $(2,3)$ example.
- Free-structure analogies: free preorder on a relation (Ex 5.19, p. 153), free category on a graph (Ex 5.22, p. 154).
- Def 5.25 (p. 155): a prop signature $(G, s, t)$ with in- and out-arities; $\mathrm{Free}(G)$ has $G$-labelled port graphs as morphisms. Ex 5.27 (p. 156): free prop on the empty signature is Bij.
- Prop 5.29 (p. 156): prop functors $\mathrm{Free}(G) \to \mathcal{C}$ correspond one-to-one with functions sending each generator $g$ to a morphism $s(g) \to t(g)$ in $\mathcal{C}$.
- Def 5.30 (p. 157): $G$-generated prop expressions, built from generators with $\mathbin{;}$, $+$, identities and symmetries; Ex 5.31 (p. 157) works one through. Remark 5.34 (p. 158): a presented prop $\langle G \mid E \rangle$ also has a universal property.

## Rigs and signal flow graphs (pp. 159-171)

> [!definition] Rig (Def 5.36, p. 159)
> A tuple $(R, 0, +, 1, *)$ with $(R,0,+)$ a commutative monoid, $(R,1,*)$ a monoid, $*$ distributing over $+$, and $0$ annihilating. Exs 5.37-5.42 (pp. 159-160): $\mathbb{N}$, Booleans, quantales, square matrices, rings such as $\mathbb{R}$. (source: Seven Sketches, p. 159)

- Def 5.45 (p. 163): the generators are copy, discard, add, zero and a scalar $a$ for each $a \in R$; $\mathrm{SFG}_R := \mathrm{Free}(G_R)$. Ex 5.44 (p. 162): a linear ODE system as a signal flow graph.
- Def 5.50 (p. 164): $\mathrm{Mat}(R)$ has $(m \times n)$-matrices as morphisms, composition by matrix product, and direct sum as the monoidal product.
- Thm 5.53 (p. 166): a prop functor $S : \mathrm{SFG}_R \to \mathrm{Mat}(R)$ on the generators. Prop 5.54 (p. 166): $S(g)_{ij}$ is the amplification of input $i$ that contributes to output $j$.
- Prop 5.56 (p. 169): $S$ is full, every matrix comes from a signal flow graph.
- Thm 5.60 (p. 170): $\mathrm{Mat}(R)$ is isomorphic to the prop presented by $G_R$ with equations: commutative monoid laws for add/zero, cocommutative comonoid laws for copy/discard, bialgebra laws, scalar multiplication and addition laws. The proof rewrites to a normal form (black nodes left, scalars middle, white nodes right). Ex 5.61 (p. 171): two graphs, one matrix.

## Monoid objects and feedback (pp. 172-181)

- Def 5.65 (p. 172): a monoid object $(M, \mu, \eta)$ in a symmetric monoidal category; commutative if $\sigma ; \mu = \mu$. Exs 5.66-5.73 (pp. 172-173): ordinary monoids in $(\mathsf{Set}, 1, \times)$, symmetric monoidal preorders as commutative monoid objects in Cat, rigs as monoid objects; Remark 5.74 (p. 173): a prop presented by $\mu, \eta$ and the three equations.
- Def 5.79 (p. 175): the prop $\mathrm{Rel}_R$ has subsets $B \subseteq R^m \times R^n$ as morphisms; the "full" signal flow graphs with feedback map to linear relations. Section near p. 177: a sound and complete presentation for linear relations.
- Thm 5.87 (p. 178): $\mathrm{Rel}_R$ is compact closed, every object self-dual (cup, cap). The chapter closes with a car-speed control example over $R[s, s^{-1}]$ (p. 178).

## Limitations

Read at statement level (all Defs/Props/Thms and example headings; Defs 5.2, 5.13, 5.25, 5.45, 5.50, 5.65, 5.79 and Thms 5.60, 5.87 opened in the text). The listing of the Thm 5.60 equations is summarised from the text's garbled diagram notation, not transcribed. Proofs and exercise solutions were not read.

## Connections

- Previous: [[Seven Sketches ch4 - Collaborative design]]. Next: [[Seven Sketches ch6 - Electric circuits]] (cospans give hypergraph categories, where Frobenius structure replaces the bialgebra structure).
- Concept pages: [[Monoidal category]], [[Operad]], [[Universal property]].

**Sources**: Fong, Spivak, Seven Sketches in Compositionality (2019), ch. 5; page numbers are printed pages.
**Last updated**: 2026-11-06

---

## Related pages
[[Monoidal category]] · [[Category]] · [[Functor]] · [[Universal property]] · [[Operad]]
