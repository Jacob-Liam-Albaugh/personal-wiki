---
type: definition
area: dsl
source-ref: "Fong-Spivak 2019, Defs. 6.97, 6.99, Prop. 6.101"
tags: [category-theory]
---

# Operad

**Summary**: A structure with types and multi-input operations that substitute into each other; the algebra of wiring diagrams, where each box is a type and a diagram is an operation.

---

Operads describe wiring-diagram patterns more flexibly than cospan categories: a diagram with $n$ inner boxes and one outer box is an operation of arity $n$, and plugging one into another is substitution.

## Examples

- Context-free grammars versus operads (Ex. 6.92); the operad $\mathrm{Set}$ of sets and functions (Ex. 6.93); the operad $\mathrm{Cospan}$ (Ex. 6.94) (pp. 214-215).
- Wiring diagrams of dynamical systems in Poly: [[Poly (Spivak 2020)]].

## The operad of a monoidal category

Every symmetric monoidal category $C$ has an underlying operad $O_C$: types are objects, operations of arity $(C_1,\dots,C_n;D)$ are morphisms $C_1\otimes\cdots\otimes C_n\to D$, and substitution $f\circ_i g$ is composition (Def. 6.97, p. 216). See [[Monoidal category]].

## Algebras

> [!definition] Operad algebra
> An algebra for an operad $O$ is an operad functor $F : O\to\mathrm{Set}$, which assigns to each box type a set of fillings. (source: Seven Sketches, Def. 6.99, p. 217)

- Ex. 6.100: circuits with finite-set types.
- Cospan-algebras are equivalent to hypergraph props (Prop. 6.101, p. 218): [[Hypergraph category]]. Varying the operad (e.g. cobordisms) changes the composition rules.
- Operad functors are the [[Functor]]s of this setting; the signal-flow wiring diagrams are morphisms of a free prop: [[Signal flow graph]].

**Covered in**: Fong-Spivak (Seven Sketches) ch. 6 (pp. 213-219, operads and their algebras)
**Sources**: Fong, Spivak, Seven Sketches (2019), ch. 6; file `text_books/Category Theory/Spivak, Fong - Seven Sketches in Compositionality.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
[[Monoidal category]] · [[Functor]] · [[Category]] · [[Hypergraph category]] · [[Poly parallel product]]
