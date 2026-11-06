---
type: paper
area: dsl
source-ref: "Spivak 2020, arXiv 2005.01894"
authors: ["[[David I. Spivak]]"]
year: 2020
venue: arXiv math.CT
file: "DSL/Spivak - Poly.pdf"
tags: [category-theory]
---

# Poly: An abundant categorical setting for mode-dependent dynamics

**Summary**: Introduces the category Poly of polynomial functors Set -> Set and its four monoidal structures, and shows that mode-dependent dynamical systems (Moore machines, wiring diagrams, categories as comonoids) all live there as lenses and comonoids.

**Authors**: David I. Spivak · **Year**: 2020 · **File**: `DSL/Spivak - Poly.pdf`

---

## Problem

Systems whose interface changes with their state (the "mode") do not fit a fixed-interface wiring-diagram setting. Poly is proposed as one setting in which interface, dynamics and composition of systems are all expressible. (source: Spivak - Poly.pdf, §1)

## Method

**Polynomials.** A polynomial functor is written

$$p = \sum_{i \in p(1)} y^{p[i]}$$

Elements of $p(1)$ are *positions* (modes); $p[i]$ is the set of *directions* at $i$. See [[Polynomial functor]]. (source: Spivak - Poly.pdf, §2)

**Morphisms.** Maps in Poly are natural transformations, i.e. [[Dependent lens|dependent lenses]]:

$$\mathrm{Poly}(p,q) = \prod_{i \in p(1)} \sum_{j \in q(1)} p[i]^{q[j]}$$

A lens is a map $f$ on positions plus, for each $i$, a backwards map $q[f(i)] \to p[i]$ on directions. (source: Spivak - Poly.pdf, §2)

**Four monoidal structures.** Poly carries $(+,0)$, $(\times,1)$, $(\otimes,y)$ and $(\circ,y)$:

$$p \times q = \sum_{i,j} y^{p[i]+q[j]}$$

$$p \otimes q = \sum_{i,j} y^{p[i]\,q[j]}$$

These are the [[Poly product]], the [[Poly parallel product]] (also called the Dirichlet product), and, for the last, the [[Poly composition product]]. Sums: [[Poly coproduct]]. Both $\times$ and $\otimes$ are monoidal closed. (source: Spivak - Poly.pdf, §2)

Worked examples in the paper:

$$(y^3+y)\otimes(y^2+1) = y^6+y^2+2$$

$$(y^2+y)\circ(y^3+1) = y^6+3y^3+2$$

(source: Spivak - Poly.pdf, §2)

**Structure of Poly.**
- Completely distributive ("axiom of choice"), has all small limits, and is extensive.
- Two factorization systems: epi/mono and vertical/cartesian.
- A monoidal *-bifibration Poly -> Set sending $\otimes$ to $\times$.
- An adjoint quadruple with Set: $A \mapsto A$, $A \mapsto Ay$, $p \mapsto p(0)$, $p \mapsto p(1)$.
- $\mathrm{Poly}(Ap,q) \cong \mathrm{Poly}(p,q^A)$.
- Lenses between monomials $By^A$ are Hedges' bimorphic lenses.

(source: Spivak - Poly.pdf, §2 to §3)

## Results

**Comonoids are categories.** Comonoids for $\circ$ are small categories (Ahman-Uustalu); comonoid morphisms are *cofunctors* (called retrofunctors in the later book). The contractible groupoid $Sy^S$ is the store comonad. See [[Polynomial comonoid]]. (source: Spivak - Poly.pdf, §3)

**Moore machines.** A Moore machine with states $S$, outputs $I$, inputs $A$ is a lens

$$Sy^S \to Iy^A$$

(source: Spivak - Poly.pdf, Prop. 3.1; Polynomial Functors, Def. 4.4, p. 85). The book names the sets the other way round: state-set $S$, position-set $I$, direction-set $A$. See [[Moore machine]].

**Mode-dependent dynamical systems.** A system is a comonoid $C$ with a map $C \to p$ (Def. 3.2). This generalizes the lens $Sy^S \to p$ of [[Dynamical system as lens]].

**Wiring.** The product of interfaces overlays two interfaces on one state system. Wiring diagrams are lenses such as $By^C \otimes Cy^{AB} \to Cy^A$; mode-dependent wiring is possible, e.g. $2y^W \otimes Wy \otimes Wy \to y$. (source: Spivak - Poly.pdf, §3)

## Limitations

A short extended abstract: proofs are mostly cited. The book [[Polynomial Functors ch1 - Representable functors]] onward supplies full statements. Notation differs: this paper writes $\circ$ for composition; the book defines $p \circ q$ (Def. 6.1, p. 180) and also writes it $p \triangleright q$ (Cor. 6.5, p. 180).

## Connections

- Book treatment: [[Polynomial Functors ch3 - The category of polynomial functors]], [[Polynomial Functors ch6 - The composition product]], [[Polynomial Functors ch7 - Polynomial comonoids and retrofunctors]].
- Applied use: [[Polynomial equipment interfaces (Bilionis 2026)]], [[Protocols are lenses]].
- Background: [[Category]], [[Functor]], [[Natural transformation]], [[Monoidal category]].

%% refs:start %%
**Cited by in this wiki**: [[Polynomial equipment interfaces (Bilionis 2026)]]
%% refs:end %%

**Sources**: Spivak, "Poly: An abundant categorical setting for mode-dependent dynamics", arXiv 2005.01894.
**Last updated**: 2026-11-06

---

## Related pages
[[Polynomial functor]] · [[Dependent lens]] · [[Poly product]] · [[Poly coproduct]] · [[Poly parallel product]] · [[Poly composition product]] · [[Dynamical system as lens]] · [[Moore machine]] · [[Polynomial comonoid]]
