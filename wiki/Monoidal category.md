---
type: definition
area: dsl
source-ref: "Fong-Spivak 2019, Def. 2.2, Def. 4.58, Def. 5.65; Niu-Spivak 2024, ch. 3 and 6"
tags: [category-theory]
---

# Monoidal category

**Summary**: A category with a tensor product of objects and a unit object, associative and unital up to coherent isomorphism; symmetric if the tensor commutes.

---

> [!definition] Monoidal category
> A category $C$ with $\otimes : C\times C \to C$ and a unit $I$ satisfying associativity and unit laws. Fong-Spivak state the preorder case first: a symmetric monoidal preorder. (source: Seven Sketches, Def. 2.2)

> [!definition] Symmetric monoidal preorder
> A preorder $(X,\le)$ with a unit $I\in X$ and a product $\otimes : X\times X\to X$ that is monotone in both arguments, unital, associative and symmetric. (source: Seven Sketches, Def. 2.2, pp. 41-42)

## Resource theories (monoidal preorders)

Objects are resources, $x\le y$ reads "$y$ can be made from $x$" and $\otimes$ means "side by side". See [[Preorder]].

- Ex. 2.4: reals with $+$. Ex. 2.6: a monoid is a one-object structure, and a commutative monoid gives a discrete symmetric monoidal preorder.
- Wiring diagrams (pp. 45-47): a box $x_0\le x_1$ with series and parallel wiring proves inequalities. Ex. 2.14 draws proofs in $(\mathbb R,\le,0,+)$; Ex. 2.19 is the lemon meringue pie.
- Further examples (pp. 52-54): Booleans with AND (Ex. 2.27), naturals with $+$ (Ex. 2.30), divisibility with multiplication (Ex. 2.32), power set with intersection.
- Ex. 2.37: Lawvere's $\mathsf{Cost}=([0,\infty],\ge,0,+)$. The order is reversed: a smaller cost is "bigger".
- Prop. 2.38: the opposite of a symmetric monoidal preorder is again one.
- A monoidal monotone preserves $\le$, the unit and the product up to the order (Def. 2.41); Ex. 2.42: $\mathbb N\to\mathbb R$.
- Closedness and quantales: [[Quantale]]. Enrichment over a monoidal preorder: [[Enriched category]].

## Monoidal categories and categorification

- Passing from monoidal preorders to monoidal categories replaces equalities by coherence isomorphisms (Section 4.4, pp. 134-138). Strict versus non-strict: Remarks 4.46-4.47. Example: $(\mathsf{Set},1,\times)$ (Ex. 4.49). V-categories for $\mathcal V$ a monoidal category: Remark 4.53.
- Monoid objects: $(M,\mu,\eta)$ in a symmetric monoidal category, commutative if $\sigma;\mu=\mu$ (Def. 5.65, p. 172). Ordinary monoids in $(\mathsf{Set},1,\times)$, symmetric monoidal preorders as commutative monoid objects in $\mathsf{Cat}$, rigs as monoid objects (Exs. 5.66-5.73). Comonoid objects are dual; Frobenius monoids combine both: [[Hypergraph category]].
- A prop is a symmetric strict monoidal category on $\mathbb N$ (Def. 5.2): [[Signal flow graph]].

## Duals and compact closed categories

> [!definition] Dual
> A dual of $c$ in a symmetric monoidal category: $c^*$ with unit $\eta_c : I\to c^*\otimes c$ and counit $\epsilon_c : c\otimes c^*\to I$ satisfying the snake equations. If every object has a dual the category is compact closed. (source: Seven Sketches, Def. 4.58, p. 141)

- A compact closed category is monoidal closed (Prop. 4.60). $\mathsf{Corel}$, finite sets with partitions of the disjoint union as morphisms, is compact closed (Ex. 4.61).
- For skeletal $\mathcal V$, $\mathsf{Prof}_{\mathcal V}$ is compact closed (Thm. 4.63), which licenses cups and caps in wiring diagrams: [[Profunctor]]. Hypergraph categories are self-dual compact closed (Prop. 6.66); $\mathrm{Rel}_R$ is compact closed with every object self-dual (Thm. 5.87).

## Examples elsewhere

- Poly has four: $(+,0)$, $(\times,1)$, $(\otimes,y)$, $(\circ,y)$: [[Poly (Spivak 2020)]], [[Poly parallel product]], [[Poly composition product]].
- Comonoids for $(\circ,y)$ are categories: [[Polynomial comonoid]].
- Wiring diagrams: [[Operad]].

**Covered in**: Fong-Spivak (Seven Sketches) ch. 2 (pp. 41-56, monoidal preorders), ch. 4 (pp. 134-146, monoidal categories and duals), ch. 5 (monoid objects); Niu-Spivak ch. 3, 6
**Sources**: Fong, Spivak, Seven Sketches (2019), ch. 2, 4, 5; Spivak (2020); file `text_books/Category Theory/Spivak, Fong - Seven Sketches in Compositionality.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
[[Category]] · [[Enriched category]] · [[Operad]] · [[Quantale]] · [[Profunctor]] · [[Signal flow graph]] · [[Hypergraph category]] · [[Poly parallel product]] · [[Poly composition product]] · [[Polynomial comonoid]]
