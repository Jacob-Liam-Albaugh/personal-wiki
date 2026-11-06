---
type: definition
area: dsl
source-ref: "Fong-Spivak 2019, Def. 1.30"
tags: [category-theory]
---

# Preorder

**Summary**: A set with a reflexive, transitive relation $\le$; equivalently a category with at most one morphism between any two objects.

---

> [!definition] Preorder
> A set $X$ with a relation $\le$ such that $x\le x$ and $x\le y,\ y\le z \Rightarrow x\le z$. A partial order also has antisymmetry ($a\le b\le a$ forces $a=b$, Remark 1.43). (source: Seven Sketches, Def. 1.30, p. 13)

## Background: relations and partitions

- A relation between $X$ and $Y$ is a subset of $X\times Y$ (Def. 1.12, p. 8). A partition of $A$ is a set of nonempty parts covering $A$ disjointly (Def. 1.14, p. 9). An equivalence relation is reflexive, symmetric and transitive (Def. 1.18).
- Prop. 1.19 (p. 10): partitions of $A$ correspond one-to-one with equivalence relations on $A$. The quotient $A/{\sim}$ is the set of equivalence classes (Def. 1.21). Functions are subsets of $S\times T$ with exactly one $t$ per $s$ (Def. 1.22), and compose (Def. 1.28).
- A graph $(V,A,s,t)$ (Def. 1.36, p. 14) generates a preorder; Hasse diagrams draw a preorder as a graph with reflexive and composite arrows suppressed.

## Examples

- Naturals (Ex. 1.45), reals (Ex. 1.47), the partition induced by a preorder (Ex. 1.49), the power set $\mathcal P(X)$ under inclusion (Ex. 1.50), partitions ordered by coarseness (Ex. 1.52, Prop. 1.19), upper sets (Ex. 1.54), product preorder (Ex. 1.56), opposite preorder (Ex. 1.58) (pp. 15-17).
- Open sets of a space form a preorder $(Op,\subseteq)$ (Remark 7.33): see [[Topos]].

## Monotone maps

> [!definition] Monotone map
> A function $f : A\to B$ between preorders with $a\le a' \Rightarrow f(a)\le f(a')$. (source: Seven Sketches, Def. 1.59, p. 18)

- Identities are monotone and monotone maps compose (Prop. 1.70, p. 21). Isomorphism of preorders (Def. 1.75). Examples: the tree of life (Ex. 1.61), the power set as a map (Ex. 1.62), partitions of a set (Ex. 1.68).
- Prop. 1.78 (p. 22): monotone maps $P\to\mathbb B$ correspond to upper sets of $P$; a Yoneda lemma for preorders appears in the exercises (p. 20). See [[Yoneda lemma]].
- Monotone maps are the [[Functor]]s between preorders (Ex. 3.42). Preorders are Bool-categories (Thm. 2.49); replacing Bool by Cost gives Lawvere metric spaces: see [[Enriched category]].

## Meets and joins

> [!definition] Meet and join
> A meet of $A\subseteq P$ is a greatest lower bound; a join is a least upper bound. (source: Seven Sketches, Def. 1.81, p. 23)

- Meets or joins may fail to exist or may be non-unique in a preorder (Exs. 1.83-1.84, p. 24). In $\mathcal P(X)$ the meet is intersection, in $\mathbb B$ it is AND, in a total order it is the infimum (Exs. 1.87-1.89).
- Prop. 1.91 (p. 25): for $A\subseteq B$ with meets, $\bigwedge B\le\bigwedge A$.
- In a preorder, all joins exist iff all meets exist (Prop. 2.96, p. 72).

> [!definition] Generative effect
> A monotone map preserves meets if $f(a\wedge b)=f(a)\wedge f(b)$ (Def. 1.92). It has a generative effect if some $a,b$ give
> $$f(a)\vee f(b)\ne f(a\vee b).$$
> Observing the combined system shows something not obtainable by combining the observations. (source: Seven Sketches, Defs. 1.92-1.93, p. 26)

Generative effects are the failure of a map to preserve joins; whether a map has them is decided by whether it is a left adjoint: see [[Galois connection]].

## Where it appears

Maps between preorders can be [[Galois connection]]s. A preorder with a compatible product is a [[Monoidal category]] (resource theory). Adjoint-preserving structure and closure operators: [[Galois connection]].

**Covered in**: Fong-Spivak (Seven Sketches) ch. 1 (pp. 1-26, relations, preorders, monotone maps, meets and joins, generative effects)
**Sources**: Fong, Spivak, Seven Sketches (2019), ch. 1, 2; file `text_books/Category Theory/Spivak, Fong - Seven Sketches in Compositionality.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
[[Category]] · [[Galois connection]] · [[Enriched category]] · [[Quantale]] · [[Functor]] · [[Monoidal category]] · [[Topos]]
