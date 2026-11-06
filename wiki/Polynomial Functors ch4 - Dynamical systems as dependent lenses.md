---
type: paper
area: dsl
source-ref: "Niu-Spivak 2024, ch. 4"
authors: ["[[Nelson Niu]]", "[[David I. Spivak]]"]
year: 2024
venue: book draft
file: "text_books/Category Theory/Spivak, Niu - Polynomial Functors.pdf"
tags: [category-theory]
---

# Polynomial Functors ch4 - Dynamical systems as dependent lenses

**Summary**: Moore machines as lenses Sy^S to Iy^A, automata, dependent dynamical systems with polynomial interfaces, graphs, wiring by parallel product interfaces, and the closure of the parallel product.

**Authors**: Nelson Niu, David I. Spivak · **Year**: 2024 · **File**: `text_books/Category Theory/Spivak, Niu - Polynomial Functors.pdf`

---
## Problem

Show that the lenses of ch. 3 are state machines. A Moore machine is a lens out of a state system $Sy^S$ into an interface; allowing the interface to be any polynomial makes interactions depend on the output. (source: Polynomial Functors, ch. 4, pp. 83-130)

## Moore machines (pp. 83-88)

> [!definition] Moore machine (Def 4.1, p. 83)
> Three sets: a state-set $S$, a position-set (output-set) $I$ and a direction-set (input-set) $A$; two functions $\mathrm{return} : S \to I$ and $\mathrm{update} : S \times A \to S$. It is an $(A, I)$-Moore machine with states $S$. The input/output terms are standard; position/direction is the book's own. (source: Polynomial Functors, p. 83)

> [!definition] Moore machine, version 2 (Def 4.4, p. 85)
> An $(A, I)$-Moore machine with states $S$ is a lens
> $$ \varphi : S y^S \to I y^A \quad \text{in Poly.} $$
> The domain $Sy^S$ is the state system, the codomain $Iy^A$ the interface, $\varphi_1$ is the return function and $\varphi^\sharp : S \times A \to S$ the update function. (source: Polynomial Functors, p. 85)

- Ex 4.2 (p. 84): a transition diagram with $A = \{\text{orange, green}\}$, $I = \{0, 1\}$ and 3 states; feeding a word of directions traces a trajectory of outputs.
- Ex 4.6 (p. 86): the counter, a $(1, \mathbb{N})$-Moore machine $\mathbb{N}y^{\mathbb{N}} \to \mathbb{N}y$ with identity on positions and $n \mapsto n + 1$ on directions. Ex 4.7 (p. 86): moving in the plane, $\mathbb{R}^2 y^{\mathbb{R}^2} \to \mathbb{R}^2 y^{[0,\infty) \times [0, 2\pi)}$, update $(x, y) \mapsto (x + r\cos\theta, y + r\sin\theta)$.
- Ex 4.9 (p. 87): a function $f : A \to I$ is a memoryless Moore machine $Iy^I \to Iy^A$.

## Automata (pp. 89-93)

- Def 4.15 (p. 89): a deterministic state automaton has states $S$, symbols $A$, update $u : S \times A \to S$, initial state $s_0$ and accept states $F \subseteq S$. Prop 4.17 (p. 89): it is a pair of lenses $y \to Sy^S \to 2y^A$.

> [!definition] Dependent dynamical system (Def 4.18, p. 90)
> A lens $\varphi : Sy^S \to p$ for any set $S$ and polynomial $p$. The interface $p$ now has positions and direction-sets that vary with the position. (source: Polynomial Functors, p. 90)

- Ex 4.21 (p. 91): halting automata, $Sy^S \to y^A + 1$, where the position "accept" has no directions.
- Def 4.25, Ex 4.26 (p. 93): a graph $E \rightrightarrows V$ has the emanation polynomial $\sum_{v \in V} y^{s^{-1}(v)}$, positions vertices and directions outgoing edges.

## Interfaces, products and wiring (pp. 103-128)

- Ex 4.43 (p. 103): the do-nothing section; the book points out how a system's states are treated only through labels, motivating sections.
- Ex 4.46 (p. 107): the repeater, which turns silences into repeated outputs. Ex 4.47 (p. 108): paddling, a machine with interface $\mathbb{N}y$ built from two intermediate constraints.
- Prop 4.54 (p. 113): sections of a parallel product, namely
  $$ \Gamma(p \otimes q) \cong \mathsf{Set}(q(1), \Gamma(p)) \times \mathsf{Set}(p(1), \Gamma(q)). $$
  A section for both interfaces is a section of $p$ for every output $q$ might return and a section of $q$ for every output $p$ might return.
- Ex 4.66 (p. 118): graphs as wiring diagrams and cellular automata, with a set $\tau(v)$ attached to each vertex.

## Closure of the parallel product (pp. 126-128)

> [!definition] Closure (Ex 4.81, Prop 4.85; p. 126)
> $[y^A, y] \cong Ay$, $[Ay, y] \cong y^A$ and $[p, y] \cong \Gamma(p)\, y^{p(1)}$ (Ex 4.81). The internal hom satisfies
> $$ \mathsf{Poly}(p \otimes q, r) \cong \mathsf{Poly}(p, [q, r]), $$
> with $[q, r] = \prod_{j \in q(1)} r \circ (q[j]\, y)$. (source: Polynomial Functors, p. 126)

- Ex 4.92 (p. 127): a robot with interface $q$ does not know its environment; $f : p \otimes q \to r$ induces $f' : p \to [q, r]$ with $f = \mathrm{eval} \circ (f' \otimes q)$. Ex 4.93 (p. 128): "Chu &", $\varphi_1 \,\&\, \varphi_2 : (p_1 \times p_2) \otimes (q_1 + q_2) \to r$.

## Limitations

Read at statement level: every Def, Prop and Example heading of the chapter. Defs 4.1, 4.4, 4.15, 4.18, 4.25 and Exs 4.2, 4.6, 4.7, 4.9, 4.21, 4.26, 4.43, 4.46, 4.47, 4.66, 4.81, 4.92, 4.93 and Props 4.17, 4.54, 4.85 were opened. The sections on products of systems and on wiring diagrams (pp. 94-125) were read only through their headings. Proofs and exercises were not read.

## Connections

- Previous: [[Polynomial Functors ch3 - The category of polynomial functors]]. Next: [[Polynomial Functors ch5 - More categorical properties]].
- Concept pages: [[Moore machine]], [[Dynamical system as lens]] (existing wiki page), [[Poly parallel product]] (the closure above).
- Earlier treatment of the same material: [[Poly (Spivak 2020)]].

**Sources**: Niu, Spivak, Polynomial Functors (2024), ch. 4; page numbers are printed pages.
**Last updated**: 2026-11-06

---

## Related pages
[[Moore machine]] · [[Dynamical system as lens]] · [[Dependent lens]] · [[Poly parallel product]] · [[Polynomial functor]]
