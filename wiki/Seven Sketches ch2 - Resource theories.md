---
type: paper
area: dsl
source-ref: "Fong-Spivak 2019, ch. 2"
authors: ["[[Brendan Fong]]", "[[David I. Spivak]]"]
year: 2019
venue: book (Cambridge University Press)
file: "DSL/Spivak, Fong - Seven Sketches in Compositionality.pdf"
tags: [category-theory]
---

# Seven Sketches ch2 - Resource theories

**Summary**: Monoidal preorders as resource theories, wiring diagrams, enrichment (V-categories, Bool, Cost), V-functors and products, closed structure, quantales and V-matrices.

**Authors**: Brendan Fong, David I. Spivak · **Year**: 2019 · **File**: `DSL/Spivak, Fong - Seven Sketches in Compositionality.pdf`

---
## Problem

Model "can I make b from a?" questions where resources combine, using a preorder with a compatible product, and then let the preorder be replaced by other value-carrying structures (costs, distances). (source: Seven Sketches, ch. 2, pp. 36-76)

## Monoidal preorders (pp. 41-56)

> [!definition] Symmetric monoidal preorder (Def 2.2, p. 41)
> A preorder $(X, \le)$ with a unit $I \in X$ and a product $\otimes : X \times X \to X$ that is monotone in both arguments, unital, associative and symmetric. (source: Seven Sketches, pp. 41-42)

- Ex 2.4 (p. 42): reals with $+$. Ex 2.6 (p. 42): a monoid is a one-object structure; a commutative monoid gives a discrete symmetric monoidal preorder.
- Wiring diagrams (pp. 45-47): Ex 2.14 draws proofs in $(\mathbb{R}, \le, 0, +)$; Ex 2.19 is the lemon meringue pie. A box $x_0 \le x_1$ and series/parallel wiring prove inequalities.
- Examples (pp. 52-54): Booleans with AND Ex 2.27, naturals with $+$ Ex 2.30, divisibility with multiplication Ex 2.32, power set with intersection (p. 54).
- Ex 2.37 (p. 54): Lawvere's $\mathsf{Cost} = ([0,\infty], \ge, 0, +)$. Note the order is reversed: a smaller cost is "bigger".
- Prop 2.38 (p. 55): the opposite of a symmetric monoidal preorder is again one.
- Def 2.41 (p. 55): a monoidal monotone preserves $\le$, the unit and the product up to the order. Ex 2.42 (p. 56): $\mathbb{N} \to \mathbb{R}$.

## Enrichment (pp. 57-68)

> [!definition] V-category (Def 2.46, p. 57)
> For a symmetric monoidal preorder $\mathcal{V}$: a set of objects and a hom-object $X(x,y) \in \mathcal{V}$ for each pair, with
> $$ I \le X(x,x) $$
> $$ X(x,y) \otimes X(y,z) \le X(x,z) $$
> (source: Seven Sketches, p. 57)

> [!theorem] Preorders are Bool-categories (Thm 2.49, p. 58)
> Preorders correspond one-to-one with $\mathsf{Bool}$-categories. (source: Seven Sketches, p. 58)

- Def 2.51 (p. 59): a metric space. Def 2.53 (p. 61): a Lawvere metric space is a $\mathsf{Cost}$-category, where the triangle inequality and $d(x,x)=0$ are the two axioms; Ex 2.54 (p. 61) puts $\mathbb{R}$ here, and distance need not be symmetric.
- Ex 2.65 (p. 65): a monoidal monotone $[0,\infty] \to \{\text{true}, \text{false}\}$ turns distances into a preorder.
- Def 2.69 (p. 65): a V-functor $F : X \to Y$ with $X(x,x') \le Y(Fx, Fx')$. Exs 2.70-2.72 (p. 66): Bool-functors are monotone maps; Cost-functors are non-expanding maps. Remark 2.71: preorders and Bool-categories are equivalent categories.
- Def 2.74 (p. 67): the V-product $X \times Y$ with hom $X(x,x') \otimes Y(y,y')$. Ex 2.76 (p. 67): product of weighted graphs.

## Closed structure and quantales (pp. 69-76)

> [!definition] Closed (Def 2.79, p. 69)
> $\mathcal{V}$ is closed if each pair $v, w$ has a hom-element $v \multimap w$ with
> $$ a \otimes v \le w \iff a \le (v \multimap w). $$
> (source: Seven Sketches, p. 69)

- Ex 2.83 (p. 69): Cost is closed (truncated subtraction). Ex 2.85 (p. 70): $(\mathbb{B}, \le, \text{false}, \vee)$ is a non-example. Prop 2.87 (p. 70): properties of $\multimap$. Remark 2.89 (p. 71): $\mathcal{V}$ is enriched in itself.
- Def 2.90 (p. 71): a unital commutative quantale is a closed symmetric monoidal preorder with all joins. Ex 2.91 (p. 71): Cost is a quantale. Remark 2.95 (p. 72): the "navigator" reading.
- Prop 2.96 (p. 72): in a preorder, all joins exist iff all meets exist. Prop 2.98 (p. 73): a symmetric monoidal preorder with all joins is closed iff $\otimes$ distributes over joins.
- Def 2.100 (p. 73): a V-matrix $M : X \times Y \to \mathcal{V}$. Product
 $$ (M \ast N)(x,z) = \bigvee_y M(x,y) \otimes N(y,z). $$
 Ex 2.102 (p. 74): Boolean matrix multiplication. Remark 2.97 (p. 73): Hausdorff distance generalises to any quantale.

## Limitations

Read at statement level (every Def/Prop/Thm and example headings, with Defs 2.2, 2.46, 2.49, 2.79, 2.90, 2.100 checked in the text). Proofs and exercise solutions were not read; the descriptions of the power-set example, Exs 2.65, 2.83 are from headings and first lines.

## Connections

- Previous: [[Seven Sketches ch1 - Generative effects]]. Next: [[Seven Sketches ch3 - Databases]], then V-profunctors in [[Seven Sketches ch4 - Collaborative design]].
- Concept pages: [[Monoidal category]], [[Enriched category]], [[Quantale]].

**Sources**: Fong, Spivak, Seven Sketches in Compositionality (2019), ch. 2; page numbers are printed pages.
**Last updated**: 2026-11-06

---

## Related pages
[[Monoidal category]] · [[Enriched category]] · [[Quantale]] · [[Preorder]] · [[Profunctor]]
