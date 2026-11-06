---
type: concept
area: dsl
source-ref: "Fong-Spivak 2019, Defs. 7.12, 7.22, 7.25, 7.35, 7.69, Prop. 7.71, §7.5"
tags: [category-theory]
---

# Topos

**Summary**: Sheaves on a topological space form a topos with a subobject classifier whose internal logic supports modalities; sheaves on the interval domain give a topos of behavior types for contracts on systems over time.

---

Systems interact over time and each carries guarantees about its behavior over intervals. Sheaves on a space of time intervals form a topos, whose higher-order logic is the language of behavior contracts.

## Subobjects and presheaves

- Pasting pullback squares (Prop. 7.3); monomorphism and epimorphism (Def. 7.5).
- In a [[Category]] $E$ with finite limits, a subobject classifier is an object $\Omega$ with a point $\mathrm{true}:1\to\Omega$ such that every subobject $A\hookrightarrow X$ is the pullback of $\mathrm{true}$ along a unique $X\to\Omega$ (Def. 7.12, p. 228; the book notes it is hard to digest). In Set, $\Omega=\{\text{false},\text{true}\}$. A [[Universal property]] of this kind is the source of logic.
- A presheaf on $C$ is a [[Functor]] $P:C^{op}\to\mathsf{Set}$ (Def. 7.22). Ex. 7.23: the arrow-shape category whose presheaves are graphs; graphs form a presheaf topos (Ex. 7.54).

## Topology and sheaves

> [!definition] Topology
> A topology on a set $X$ is a collection $Op$ of subsets (open sets) containing $\emptyset$ and $X$, closed under arbitrary unions and finite intersections. (source: Seven Sketches, Def. 7.25, p. 234)

Exs. 7.26-7.30: $\epsilon$-balls on $\mathbb R^2$, the coarsest and discrete topologies, the four topologies on $\{1,2\}$. $(Op,\subseteq)$ is a [[Preorder]] (Remark 7.33).

> [!definition] Sheaf
> A presheaf $P:Op^{op}\to\mathsf{Set}$ such that every matching family over an open cover $(U_i)$ of $U$ has a unique gluing in $P(U)$. (source: Seven Sketches, Def. 7.35, p. 237)

Ex. 7.36: the empty cover. Exs. 7.45-7.61: sections of a continuous map, vector fields on a manifold, the topos of sheaves on a point is Set (Ex. 7.48), sections of a vector bundle. Sheaves and their morphisms are [[Natural transformation]]s of presheaves.

## Logic in a topos

- Truth values in $\mathrm{Shv}(X)$ are open subsets: $\Omega(U)$ is the set of open subsets of $U$. A predicate $p:S\times T\to\Omega$ returns, for sections over $U$, the open subset of $U$ on which the relation holds (Ex. 7.65, the news cycle example).
- A modality is a sheaf morphism $j:\Omega\to\Omega$ satisfying three properties (Def. 7.69, p. 250). For fixed $p$ the maps $q\mapsto(p\Rightarrow q)$ and others are modalities (Prop. 7.71; items paraphrased, not checked line by line). Closure operators ([[Galois connection]], Def. 1.120) return as modalities.
- In any topos a morphism is epi iff a certain existence statement holds (Ex. 7.74).

## A topos of behavior types

> [!definition] The interval domain
> $\mathbb{IR}$ has as points all finite closed intervals $[d,u]$ with $d\le u$. For $a<b$ the basic open set is
> $$o_{[a,b]}=\{[d,u]: a<d\le u<b\},$$
> and the open sets are unions of these. (source: Seven Sketches, §7.5.1, p. 252)

- $o_{[0,5]}\cup o_{[4,8]}\ne o_{[0,8]}$: the interval $[2,6]$ lies only in the right side (Exercise 7.76). Intervals, not points, are the right base space.
- $\mathbb R\subset\mathbb{IR}$ via $d=u$, with the usual subspace topology (Exercise 7.77). The topos of behavior types is $\mathsf{BT}:=\mathrm{Shv}(\mathbb{IR},Op)$.
- A sheaf $S$ gives for each open $U$ the set $S(U)$ of events happening throughout $U$, with restriction to sub-intervals and unique gluing. It is determined by its values on the $o_{[a,b]}$, with $S(o_{[a,b]})=\lim_{\epsilon>0}S(o_{[a-\epsilon,b+\epsilon]})$ (§7.5.2, p. 253).
- Examples: the constant sheaf on a set $A$ (Ex. 7.78); local continuous functions into a space $X$ (Ex. 7.79); sheaves from open hybrid dynamical systems (Ex. 7.81).
- $\Omega$ sends $U$ to its open subsets, so "Bob likes the weather" returns the open set of times it holds throughout. True on $(0,5)$ and $(4,8)$ implies true on $(0,8)$ for that statement, but not for "a single watcher stayed at position $p$" or "the market did not fall by more than 10 points".
- Safety proofs (§7.5.3): components carry behavior contracts, predicates $p:\mathrm{dials}\times\mathrm{thrusters}\to\Omega$, for example (7.82): whenever the dials show a bad position, within a second the pilot engages the thrusters for five seconds. The modality $@_t$ (type 3 of Prop. 7.71) says "true on a small enough neighborhood of $t$". Contracts are axioms from which system-level safety, such as aircraft separation, is derived (joint MIT, Honeywell and NASA project; details in the book's cited [SS18]).
- Background: toposes originate with Grothendieck; Lawvere and Tierney recognised their logic; domain theory (Scott) matters for deeper temporal type theory.

## Where it appears

Dynamical systems as coalgebras and their logic are open questions in the Poly literature: [[Dynamical system as lens]].

**Covered in**: Fong-Spivak (Seven Sketches) ch. 7 (pp. 221-257, subobjects, presheaves, sheaves, logic in a topos, modalities, topos of behavior types)
**Sources**: Fong, Spivak, Seven Sketches (2019), ch. 7; file `text_books/Category Theory/Spivak, Fong - Seven Sketches in Compositionality.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
[[Category]] · [[Functor]] · [[Natural transformation]] · [[Preorder]] · [[Universal property]] · [[Galois connection]] · [[Dynamical system as lens]]
