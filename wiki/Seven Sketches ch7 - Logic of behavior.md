---
type: paper
area: dsl
source-ref: "Fong-Spivak 2019, ch. 7"
authors: ["[[Brendan Fong]]", "[[David I. Spivak]]"]
year: 2019
venue: book (Cambridge University Press)
file: "text_books/Category Theory/Spivak, Fong - Seven Sketches in Compositionality.pdf"
tags: [category-theory]
---

# Seven Sketches ch7 - Logic of behavior

**Summary**: Sheaves on topological spaces, sheaf toposes and their internal logic, modalities, and the topos BT of behavior types on the interval domain, with behavior contracts for safety proofs.

**Authors**: Brendan Fong, David I. Spivak · **Year**: 2019 · **File**: `text_books/Category Theory/Spivak, Fong - Seven Sketches in Compositionality.pdf`

---
## Problem

Systems interact over time and each carries guarantees about its behavior over intervals. The chapter builds a logic that can state and combine such guarantees: sheaves on a space of time intervals form a topos, whose higher-order logic is the language of behavior contracts. (source: Seven Sketches, ch. 7, pp. 221-257)

## Subobjects and presheaves (pp. 225-233)

- Prop 7.3 (p. 225): pasting pullback squares. Def 7.5 (p. 226): monomorphism and epimorphism.
- Def 7.12 (p. 228): in a category $E$ with finite limits, a subobject classifier is an object $\Omega$ with a point $\mathrm{true} : 1 \to \Omega$ such that every subobject $A \hookrightarrow X$ is the pullback of $\mathrm{true}$ along a unique $X \to \Omega$ (the book remarks that the definition is hard to digest). In Set, $\Omega = \{\text{false}, \text{true}\}$.
- Def 7.22 (p. 232): a presheaf on $C$ is a functor $P : C^{\mathrm{op}} \to \mathsf{Set}$. Ex 7.23 (p. 233): the arrow-shape category whose presheaves are graphs.

## Topology and sheaves (pp. 234-247)

> [!definition] Topology (Def 7.25, p. 234)
> A topology on a set $X$ is a collection $Op$ of subsets (the open sets) containing $\emptyset$ and $X$, closed under arbitrary unions and finite intersections. Exs 7.26-7.30 (pp. 234-235): $\epsilon$-balls on $\mathbb{R}^2$, the coarsest (and discrete) topology, the four topologies on $\{1, 2\}$. Remark 7.33 (p. 236): $(Op, \subseteq)$ is a preorder. (source: Seven Sketches, p. 234)

> [!definition] Sheaf (Def 7.35, p. 237)
> A presheaf $P : Op^{\mathrm{op}} \to \mathsf{Set}$ such that every matching family over an open cover $(U_i)$ of $U$ has a unique gluing in $P(U)$. Ex 7.36 (p. 237): the empty cover. (source: Seven Sketches, p. 237)

- Ex 7.45 (p. 240): sections of a continuous map. Ex 7.46 (p. 241): vector fields on a manifold. Ex 7.48 (p. 242): the topos of sheaves on a point is Set. Ex 7.54 (p. 244): graphs form a presheaf topos. Ex 7.61 (p. 246): sections of a vector bundle.

## Logic in a topos (pp. 247-251)

- Truth values in $\mathrm{Shv}(X)$ are open subsets: $\Omega(U)$ is the set of open subsets of $U$ (p. 254 recalls this). Ex 7.65 (pp. 248-249): a predicate $p : S \times T \to \Omega$ returns, for sections over $U$, the open subset of $U$ on which the relation holds; the worked case is the news cycle ("worried about the news").
- Def 7.69 (p. 250): a modality is a sheaf morphism $j : \Omega \to \Omega$ satisfying three properties (as printed on p. 250). Prop 7.71 (p. 250): for fixed $p$, the maps $q \mapsto (p \Rightarrow q)$ and others are modalities; the book lists them as items (a), (b), ...
- Ex 7.74 (p. 251): in any topos a morphism is epi iff a certain existence statement holds.

## A topos of behavior types (Section 7.5, pp. 252-256)

> [!definition] The interval domain (7.5.1, p. 252)
> $\mathbb{IR}$ has as points all finite closed intervals $[d, u]$ with $d \le u$. For $a < b$ the basic open set is
> $$ o_{[a,b]} = \{[d,u] : a < d \le u < b\}, $$
> and the open sets are unions of these. (source: Seven Sketches, p. 252)

- $o_{[0,5]} \cup o_{[4,8]} \ne o_{[0,8]}$: the interval $[2,6]$ lies in the right side only (Exercise 7.76, pp. 252-253). This is why intervals, not points, are the right base space.
- $\mathbb{R} \subset \mathbb{IR}$ via $d = u$, and its subspace topology is the usual one (Exercise 7.77, p. 253). The topos of behavior types is $\mathsf{BT} := \mathrm{Shv}(\mathbb{IR}, Op)$.
- A sheaf $S$ gives for each open $U$ the set $S(U)$ of events happening throughout $U$, with restriction to sub-intervals and unique gluing of matching events. $S$ is determined by its values on the $o_{[a,b]}$, and $S(o_{[a,b]}) = \lim_{\epsilon > 0} S(o_{[a-\epsilon, b+\epsilon]})$ (7.5.2, p. 253).
- Examples: the constant sheaf on a set $A$, for behavior that never changes (Ex 7.78, p. 253); local continuous functions into a space $X$, on $\mathbb{IR}$ or on $\mathbb{R} \subseteq \mathbb{IR}$ (Ex 7.79, p. 254); sheaves from open hybrid dynamical systems (Ex 7.81, p. 254, construction deferred to 7.6).
- The subobject classifier $\Omega$ sends $U$ to its open subsets, so a proposition such as "Bob likes the weather" returns the open set of times it holds throughout. True on $(0,5)$ and on $(4,8)$ implies true on $(0,8)$ for that statement, but not for "a single watcher stayed at position $p$" or "the market did not fall by more than 10 points" (pp. 254-255).
- Safety proofs (7.5.3, pp. 255-256): the underlying project was joint between MIT, Honeywell and NASA (the book cites [SSV18]). Components carry behavior contracts, predicates $p : \mathrm{dials} \times \mathrm{thrusters} \to \Omega$, for example (7.82): whenever the dials show a bad position, within a second the pilot engages the thrusters for five seconds. The modality $@_t$ (of type 3 in Prop 7.71) says "true on a small enough neighborhood of $t$". Contracts are axioms from which system-level safety, such as separation of aircraft when enough components meet their contracts, is derived; details are in the cited [SS18].
- Summary and reading (7.6, pp. 256-257): toposes originate with Grothendieck (1960s); Lawvere and Tierney recognised their logic; references named are McLarty, Mac Lane-Moerdijk, Johnstone; domain theory (Scott) matters for the deeper temporal type theory; other categorical approaches to dynamics are cited.

## Limitations

Section 7.5 (pp. 252-256) and the summary were read in full from the text; the rest of the chapter was read at statement level (Defs 7.12, 7.22, 7.25, 7.35, 7.69, Prop 7.71 and example headings). The wording of Def 7.12 and the content of items (a)-(c) of Prop 7.71 are paraphrased and not checked line by line. Proofs and exercises were not read.

## Connections

- Previous: [[Seven Sketches ch6 - Electric circuits]]. Galois connections and closure operators (ch. 1, Ex 1.123) return as modalities here.
- Poly-side counterpart: dynamical systems as coalgebras and their logic, open questions 2-3 in [[Polynomial Functors ch9 - New horizons]].
- Concept pages: [[Category]], [[Preorder]], [[Natural transformation]].

**Sources**: Fong, Spivak, Seven Sketches in Compositionality (2019), ch. 7; page numbers are printed pages.
**Last updated**: 2026-11-06

---

## Related pages
[[Category]] · [[Functor]] · [[Natural transformation]] · [[Preorder]] · [[Universal property]]
