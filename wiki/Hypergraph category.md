---
type: concept
area: dsl
source-ref: "Fong-Spivak 2019, Defs. 6.43, 6.52, 6.60, 6.75, Thms. 6.58, 6.77"
tags: [category-theory]
---

# Hypergraph category

**Summary**: A symmetric monoidal category with a compatible Frobenius monoid on every object; cospans (circuits glued at terminals) are the main example, and decorating cospan apexes with circuit data gives more.

---

Circuits compose by gluing terminals. Gluing is a pushout, so the setting is cospans over a category with colimits ([[Universal property]]); decorating the apex with circuit data gives a hypergraph category.

## Cospans

> [!definition] Cospan category
> A cospan $A\to N\leftarrow B$ has feet $A,B$ and apex $N$. If $C$ has finite colimits, $\mathrm{Cospan}_C$ has the objects of $C$ and equivalence classes of cospans as morphisms, composed by pushout; it is symmetric monoidal with unit the initial object and product the coproduct. (source: Seven Sketches, Defs. 6.43, 6.45, p. 196)

See [[Monoidal category]], [[Category]].

## Frobenius monoids

> [!definition] Frobenius monoid
> An object $X$ with a commutative monoid $(\mu,\eta)$ and cocommutative comonoid $(\delta,\epsilon)$ satisfying the Frobenius law and the special law ($\mu\mathbin{;}\delta=\mathrm{id}$). (source: Seven Sketches, Def. 6.52, p. 198)

- The spider $s_{m,n}$ is built from $(m-1)$ multiplications and $(n-1)$ comultiplications (Def. 6.54, p. 199). A connected diagram of spiders and symmetries equals the spider of its type (Thm. 6.55).
- The free prop on the four generators with the nine Frobenius equations is equivalent to $\mathrm{Cospan}_{\mathsf{FinSet}}$ (Thm. 6.58, p. 200). Compare the bialgebra structure of [[Signal flow graph]].

## Hypergraph categories

> [!definition] Hypergraph category
> A symmetric monoidal category with a Frobenius structure on each object, compatible with $\otimes$ (Def. 6.60, p. 201).

- $\mathrm{Cospan}_C$ is one (Ex. 6.61); so is $\mathsf{Corel}$ (Ex. 6.64). Hypergraph categories are self-dual compact closed (Prop. 6.66, p. 203).

## Decorated cospans

> [!definition] Decorated cospan
> For $(F,\phi):(C,+)\to(\mathsf{Set},\times)$ symmetric monoidal, an $F$-decorated cospan is a cospan in $C$ with an element $s\in F(N)$ of the apex's decoration set. (source: Seven Sketches, Def. 6.75, p. 206)

- $\mathrm{Cospan}_F$ is a hypergraph category (Thm. 6.77, p. 207). The power-set functor gives sets of decorations (Ex. 6.69); circuits of resistors are the running example (Def. 6.83, Eq. 6.83, p. 209). The decorating map is a lax monoidal [[Functor]]. The circuit examples (pp. 208-212) are summarised from headings and first lines.

## Operads

Cospan-algebras are equivalent to hypergraph props (Prop. 6.101): [[Operad]].

**Covered in**: Fong-Spivak (Seven Sketches) ch. 6 (pp. 194-212, cospans, Frobenius monoids, hypergraph categories, decorated cospans)
**Sources**: Fong, Spivak, Seven Sketches (2019), ch. 6; file `text_books/Category Theory/Spivak, Fong - Seven Sketches in Compositionality.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
[[Monoidal category]] · [[Universal property]] · [[Signal flow graph]] · [[Operad]] · [[Category]] · [[Functor]]
