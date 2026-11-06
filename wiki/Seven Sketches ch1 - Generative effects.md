---
type: paper
area: dsl
source-ref: "Fong-Spivak 2019, ch. 1"
authors: ["[[Brendan Fong]]", "[[David I. Spivak]]"]
year: 2019
venue: book (Cambridge University Press)
file: "text_books/Category Theory/Spivak, Fong - Seven Sketches in Compositionality.pdf"
tags: [category-theory]
---

# Seven Sketches ch1 - Generative effects

**Summary**: Builds orders from sets and relations: preorders, monotone maps, upper sets, meets and joins, generative effects, Galois connections and closure operators.

**Authors**: Brendan Fong, David I. Spivak · **Year**: 2019 · **File**: `text_books/Category Theory/Spivak, Fong - Seven Sketches in Compositionality.pdf`

---
## Problem

A whole can have properties its parts lack ("generative effects"). The chapter models this with the simplest structure that has composition, the order. (source: Seven Sketches, ch. 1, pp. 1-34)

## Background: sets, relations, partitions (pp. 7-12)

> [!definition] Relation, partition, equivalence relation
> A relation between X and Y is a subset of X x Y (Def 1.12, p. 8). A partition of A is a set of nonempty parts covering A disjointly (Def 1.14, p. 9). An equivalence relation is reflexive, symmetric, transitive (Def 1.18, p. 9). (source: Seven Sketches, p. 8-9)

- Prop 1.19 (p. 10): partitions of A correspond one-to-one with equivalence relations on A. Def 1.21 (p. 10): the quotient A/~ is the set of equivalence classes.
- Def 1.22 (p. 10): a function is a subset of S x T with exactly one t for each s. Def 1.28 (p. 12): composite of functions.

## Preorders (pp. 13-22)

> [!definition] Preorder (Def 1.30, p. 13)
> A preorder is a set X with a binary relation $\le$ that is reflexive and transitive. (source: Seven Sketches, p. 13)

- Def 1.36 (p. 14): a graph $(V, A, s, t)$; Hasse diagrams draw a preorder as a graph with reflexive and composite arrows suppressed.
- Remark 1.43 (p. 15): a partial order is a preorder where $a \le b \le a$ forces $a = b$.
- Examples (pp. 15-17): naturals Ex 1.45, reals Ex 1.47, the partition induced by a preorder Ex 1.49, the power set $\mathcal{P}(X)$ ordered by inclusion Ex 1.50, partitions ordered by coarseness Ex 1.52, upper sets Ex 1.54, product preorder Ex 1.56, opposite preorder Ex 1.58.

> [!definition] Monotone map (Def 1.59, p. 18)
> A function $f : A \to B$ between preorders with $a \le a'$ implying $f(a) \le f(a')$. (source: Seven Sketches, p. 18)

- Prop 1.70 (p. 21): identities are monotone and monotone maps compose. Def 1.75 (p. 21): isomorphism of preorders.
- Prop 1.78 (p. 22): monotone maps $P \to \mathbb{B}$ correspond to upper sets of $P$ (a Yoneda lemma for preorders appears in the exercises on p. 20).
- Examples (pp. 19-21): the tree of life Ex 1.61, the power set as a map Ex 1.62, partitions of a set Ex 1.68.

## Meets and joins (pp. 22-26)

> [!definition] Meet (Def 1.81, p. 23)
> A meet of $A \subseteq P$ is a greatest lower bound; a join is a least upper bound. (source: Seven Sketches, p. 23)

- Examples 1.83-1.84 (p. 24): meets or joins may fail to exist, or be non-unique in a preorder. Exs 1.87-1.89 (p. 25): meet in $\mathcal{P}(X)$ is intersection, in $\mathbb{B}$ it is AND, in a total order it is the infimum.
- Prop 1.91 (p. 25): for $A \subseteq B$ with meets, $\bigwedge B \le \bigwedge A$.

> [!definition] Generative effect (Defs 1.92-1.93, p. 26)
> A monotone map preserves meets if $f(a \wedge b) = f(a) \wedge f(b)$ (Def 1.92). It has a generative effect if some $a, b$ give
> $$ f(a) \vee f(b) \ne f(a \vee b). $$
> Reading: observing the combined system shows something you cannot get by combining the observations. (source: Seven Sketches, p. 26)

## Galois connections (pp. 27-34)

> [!definition] Galois connection (Def 1.95, p. 27)
> A pair of monotone maps $f : P \to Q$, $g : Q \to P$ with
> $$ f(p) \le q \iff p \le g(q) $$
> for all $p, q$. Then $f$ is the left adjoint, $g$ the right adjoint. (source: Seven Sketches, p. 27)

- Ex 1.97 (p. 27): $3 \times - : \mathbb{Z} \to \mathbb{R}$ has left adjoint $\lceil x/3 \rceil$; Ex 1.102 and Ex 1.104 (p. 29): for a function $g : S \to T$, image $g_!$ and preimage $g^*$ are adjoint.
- Prop 1.107 (p. 30): equivalent characterisations of a Galois connection.
- Prop 1.111 (p. 31): right adjoints preserve meets; left adjoints preserve joins. Ex 1.113 (p. 31): right adjoints need not preserve joins.
- Thm 1.115 (p. 32): adjoint functor theorem for preorders, if Q has all meets, a monotone $g : Q \to P$ preserves meets iff it is a right adjoint; dually for joins and left adjoints.
- Ex 1.117 (pp. 32-33): apples and buckets; preimage $f^*$ on power sets has both a left adjoint (direct image $f_!$) and a right adjoint.

> [!definition] Closure operator (Def 1.120, p. 33)
> A monotone $j : P \to P$ with $p \le j(p)$ and $j(j(p)) = j(p)$ (as printed on p. 33). (source: Seven Sketches, p. 33)

- Ex 1.121 (p. 34): computational closure operators. Ex 1.122 (p. 34): every adjunction gives a closure operator and vice versa. Ex 1.123 (p. 34): logic, revisited in ch. 7.

## Limitations

Read at statement level (every Def/Prop/Thm and the example headings) with Defs 1.93, 1.120, Thm 1.115 and Exs 1.97, 1.117 checked in the text. Proofs and exercise solutions were not read.

## Connections

- Next: [[Seven Sketches ch2 - Resource theories]]. Orders are the base case of enrichment; Galois connections reappear as adjunctions in [[Seven Sketches ch3 - Databases]] and as V-adjoints in ch. 4.
- Concept pages: [[Preorder]], [[Galois connection]], [[Adjunction]].

**Sources**: Fong, Spivak, Seven Sketches in Compositionality (2019), ch. 1; page numbers are printed pages.
**Last updated**: 2026-11-06

---

## Related pages
[[Preorder]] · [[Galois connection]] · [[Adjunction]] · [[Category]] · [[Monoidal category]]
