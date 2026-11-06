---
type: definition
area: dsl
source-ref: "Fong-Spivak 2019, §6.5, Def. 6.97, Def. 6.99"
tags: [category-theory]
---

# Operad

**Summary**: A structure with types and multi-input operations that substitute into each other; the algebra of wiring diagrams, where each box is a type and a diagram is an operation.

---

> [!definition] Operad algebra
> An algebra for an operad $O$ is an operad functor $F : O \to \mathrm{Set}$, which assigns to each box type a set of fillings. (source: Seven Sketches, Def. 6.99)

## Intuition

Every symmetric monoidal category $C$ has an underlying operad $O_C$: types are objects, operations of arity $(C_1,\dots,C_n;D)$ are morphisms $C_1\otimes\cdots\otimes C_n \to D$, and substitution is composition (Def. 6.97).

## Examples

- Cospan-algebras are equivalent to hypergraph props (Prop. 6.101). Varying the operad (e.g. cobordisms) changes the composition rules.
- Wiring diagrams of dynamical systems in Poly: [[Poly (Spivak 2020)]].

## Where it appears

[[Seven Sketches ch6 - Electric circuits]]; relies on [[Monoidal category]] and [[Functor]].

**Sources**: Fong, Spivak, Seven Sketches (2019), ch. 6.
**Last updated**: 2026-11-06

---

## Related pages
[[Monoidal category]] · [[Functor]] · [[Category]] · [[Poly parallel product]]
