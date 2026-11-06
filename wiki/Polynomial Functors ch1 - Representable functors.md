---
type: paper
area: dsl
source-ref: "Niu-Spivak 2024, ch. 1"
authors: ["[[Nelson Niu]]", "[[David I. Spivak]]"]
year: 2024
venue: book draft
file: "text_books/Category Theory/Spivak, Niu - Polynomial Functors.pdf"
tags: [category-theory]
---

# Polynomial Functors ch1 - Representable functors

**Summary**: Representable functors y^S on Set, the Yoneda lemma, sums and products of indexed sets, the distributive law pushing products past sums, and limits and colimits of functors Set to Set.

**Authors**: Nelson Niu, David I. Spivak · **Year**: 2024 · **File**: `text_books/Category Theory/Spivak, Niu - Polynomial Functors.pdf`

---
## Problem

Polynomials in this book are functors Set to Set. Before defining them, the chapter fixes the building blocks: the representable functors, the sum and product of indexed families of sets, and the rule for swapping the two. (source: Polynomial Functors, ch. 1, pp. 1-17)

## Representable functors (pp. 3-7)

> [!definition] Representable functor (Def 1.1, p. 3)
> For a set $S$, the functor $y^S : \mathsf{Set} \to \mathsf{Set}$ sends a set $X$ to $X^S = \mathsf{Set}(S, X)$ and a function $h : X \to Y$ to post-composition with $h$. (source: Polynomial Functors, p. 3)

- Ex 1.2 (p. 4): $X \mapsto X \times X$ is representable, by $S = 2$.
- Prop 1.4 (p. 4): a function $f : R \to S$ induces a natural transformation $y^f : y^S \to y^R$, by precomposition with $f$. So $S \mapsto y^S$ is contravariant.

> [!theorem] Yoneda lemma (Lemma 1.10, p. 5)
> For a functor $F : \mathsf{Set} \to \mathsf{Set}$ and a set $S$,
> $$ F(S) \cong \mathsf{Set}^{\mathsf{Set}}(y^S, F). $$
> The isomorphism is natural; the exercises (p. 6) ask for the naturality and the two-sided inverse. (source: Polynomial Functors, p. 5)

- Wiki note: this is the form used throughout. It says a natural transformation out of $y^S$ is the same as an element of $F(S)$.

## Sums and products of sets (pp. 7-13)

> [!definition] Sum and product of an indexed family (Defs 1.14, 1.15, p. 7)
> For $X : I \to \mathsf{Set}$, the sum $\sum_{i \in I} X_i$ is the set of pairs $(i, x)$ with $x \in X_i$. The product $\prod_{i \in I} X_i$ is the set of dependent functions: choices $i \mapsto x_i \in X_i$. (source: Polynomial Functors, p. 7)

- Ex 1.16 (p. 8): for $I = 2$, the sum is the disjoint union and the product is the cartesian product.
- Prop 1.18 (p. 8): the sum is the categorical coproduct in Set and the product is the categorical product. Def 1.20 (p. 9): the corresponding sum and product of functions.
- Ex 1.24 (p. 11): a worked example with nested index sets $J(i)$ and $K(i, j)$, preparing the swap rule.

> [!theorem] Pushing a product past a sum (Prop 1.27, p. 12)
> For sets $I$, $J(i)$ and $X(i, j)$ there is a natural isomorphism
> $$ \prod_{i \in I} \sum_{j \in J(i)} X(i,j) \;\cong\; \sum_{\bar{j} \in \prod_{i} J(i)} \prod_{i \in I} X(i, \bar{j}(i)). $$
> (source: Polynomial Functors, p. 12)

- Cor 1.29 (p. 13): the special case $J$ not depending on $i$, with $\bar{j} : I \to J$. This is the equation (1.30) the book later cites for rewriting composites (it is used in the proof of Prop 6.2, p. 180).
- Def 1.31 (p. 13): a category with all small products and coproducts is completely distributive if products distribute over coproducts in this sense. Cor 1.33 (p. 14): the formula in any completely distributive category. Set is completely distributive.

## Limits and colimits in functor categories (pp. 15-17)

- Prop 1.37 (p. 15): $\mathsf{Set}^{\mathsf{Set}}$ has all small limits and colimits, computed pointwise.
- Cor 1.38 (p. 16): the sum $F + G$ and product $F \times G$ of functors are computed pointwise. Cor 1.39 (p. 16): the constant functor $0$ is initial and the constant functor $1$ is terminal.
- Prop 1.40 (p. 16): $\mathsf{Set}^{\mathsf{Set}}$ is completely distributive.

## Limitations

Read at statement level: every Def, Prop, Lemma and Cor of the chapter, with Defs 1.1, 1.14, 1.15, Lemma 1.10 and Prop 1.27 opened in the text. Proofs and exercises were not read. The Yoneda "Wiki note" above is a gloss, not a quotation.

## Connections

- Next: [[Polynomial Functors ch2 - Polynomial functors]], where sums of representables become the objects of Poly.
- Concept pages: [[Yoneda lemma]], [[Functor]], [[Natural transformation]]. The wiki's existing [[Polynomial functor]] page builds on Def 2.1.

%% refs:start %%
**Cited by in this wiki**: [[Polynomial equipment interfaces (Bilionis 2026)]]
%% refs:end %%

**Sources**: Niu, Spivak, Polynomial Functors (2024), ch. 1; page numbers are printed pages.
**Last updated**: 2026-11-06

---

## Related pages
[[Yoneda lemma]] · [[Functor]] · [[Natural transformation]] · [[Universal property]] · [[Polynomial functor]]
