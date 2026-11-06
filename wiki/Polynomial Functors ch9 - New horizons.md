---
type: paper
area: dsl
source-ref: "Niu-Spivak 2024, ch. 9"
authors: ["[[Nelson Niu]]", "[[David I. Spivak]]"]
year: 2024
venue: book draft
file: "DSL/Spivak, Niu - Polynomial Functors.pdf"
tags: [category-theory]
---

# Polynomial Functors ch9 - New horizons

**Summary**: Fourteen open questions the authors pose about comonoids in functor categories, the logic of the topos of dynamical systems, monoid structures, databases, and limits and monos in Cat-sharp.

**Authors**: Nelson Niu, David I. Spivak · **Year**: 2024 · **File**: `DSL/Spivak, Niu - Polynomial Functors.pdf`

---
## Problem

The last chapter is a list of questions rather than results. The authors say the questions may or may not be known, are not organised and are not complete. (source: Polynomial Functors, ch. 9, pp. 349-350)

## Open questions (pp. 349-350)

1. What can be said about comonoids in the category of all functors $\mathsf{Set} \to \mathsf{Set}$, including non-polynomial ones?
2. The internal logic of the topos $[\mathbb{T}_p, \mathsf{Set}]$ of dynamical systems with interface $p$.
3. How the logic of the topos $\mathbb{T}_p$ helps in reasoning about dynamical systems.
4. A morphism $p \to q$ in Poly gives a left adjoint $[\mathbb{T}_p, \mathsf{Set}] \to [\mathbb{T}_q, \mathsf{Set}]$ that preserves connected limits. These are not geometric morphisms: they are worse because they do not preserve the terminal object, and better because they preserve every connected limit, not only finite ones. How do they translate statements from the internal language of $p$ to that of $q$?
5. $\times$-monoids and $\otimes$-monoids in three categories: Poly, $\mathsf{Cat}^\sharp$ and $\mathsf{Mod}$. Find examples, and perhaps characterise them or build a theory.
6. Poly has pullbacks, so one can form the bicategory of spans in Poly. Is there a functor from it to $\mathsf{Mod}$ sending $p \mapsto \mathbb{T}_p$?
7. How databases (static) and dynamical systems interact: can a system read from or write to a database?
8. Database aggregation done dynamically.
9. In the theory of sums of representables, what happens if sets are replaced by homotopy types: how much goes through, and is anything improved?
10. Non-polynomial functors that carry a $(y, \triangleright)$ comonoid structure.
11. Characterise the monads in Poly. They generalise one-object operads (the cartesian ones).
12. A combinatorial description of limits in $\mathsf{Cat}^\sharp$.
13. $U : \mathsf{Cat}^\sharp \to \mathsf{Poly}$ is faithful, so it reflects monos. Are all monos in $\mathsf{Cat}^\sharp$ of that form?
14. Are there polynomials $p$ for which Godel-number-like codes let propositions of the topos $[\mathrm{tree}_p, \mathsf{Set}]$ be encoded in a language that $p$-dynamical systems can work with?

## Grouping (Wiki note)

- Theme A, generality of the structure: questions 1, 9, 10, 11. Theme B, logic and semantics of systems: 2, 3, 4, 14. Theme C, structure of $\mathsf{Cat}^\sharp$ and $\mathsf{Mod}$: 5, 6, 12, 13. Theme D, databases: 7, 8.
- The grouping is the wiki's, not the book's. The book itself is flat and numbered as above.

## Limitations

The whole chapter (pp. 349-350) was read in full; the wording above is a close paraphrase. Chapter intro: the questions may or may not be known, were not known to the authors at the time of writing, are not organised in any way and are not complete. Questions 5 and 6 use $\mathsf{Mod}$, which the chapter does not define; I did not look up where the book defines it **[unverified]**.

## Connections

- Previous: [[Polynomial Functors ch8 - Categorical properties of polynomial comonoids]]. Questions 2-3 relate to the sheaf-topos logic in [[Seven Sketches ch7 - Logic of behavior]].
- Concept pages: [[Polynomial comonoid]], [[Poly composition product]], [[Poly parallel product]].

**Sources**: Niu, Spivak, Polynomial Functors (2024), ch. 9; page numbers are printed pages.
**Last updated**: 2026-11-06

---

## Related pages
[[Polynomial comonoid]] · [[Poly composition product]] · [[Poly parallel product]] · [[Dynamical system as lens]] · [[Category]]
