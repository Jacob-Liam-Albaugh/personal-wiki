---
type: definition
area: math
areas: [math, optimization]
source-ref: "Basu 2018 ch. 3, Defs 3.1-3.17, Thms 3.11, 3.15, 3.27, 3.30"
tags: [optimization]
---

# Convex function

**Summary**: A function lying below its chords, equivalently with a convex epigraph. Every local minimiser is global, and first- and second-order tests are simple.

---

> [!definition] Convex function
> $f:\mathbb R^d\to\mathbb R\cup\{\infty\}$ is convex if for $\lambda\in(0,1)$:
> $$f(\lambda x+(1-\lambda)y)\le\lambda f(x)+(1-\lambda)f(y).$$
> Strongly convex with modulus $c$: $f-\tfrac c2\|x\|^2$ is convex.
>
> (source: Basu 2018, Defs 3.1, 3.3, pp. 41-42)

## Equivalent forms

- The epigraph $\{(x,t):f(x)\le t\}$ is a [[Convex set]] (Prop 3.6, p. 42).
- Jensen: $f(\sum\lambda_ix_i)\le\sum\lambda_if(x_i)$ (Thm 3.11).
- First order, for differentiable $f$ (Thm 3.27, p. 51):
$$f(y)\ge f(x)+\langle\nabla f(x),y-x\rangle.$$
- Second order (Thm 3.30, p. 52): convex iff $\nabla^2f\succeq0$ everywhere; $\nabla^2f\succ0$ implies strictly convex (not conversely, $x^4$); strongly convex with modulus $c$ iff $\nabla^2f-cI\succeq0$.
- A closed convex function is the supremum of its affine supports (Thm 3.15, p. 46).

## Building convex functions (Thm 3.12, p. 44)

Nonnegative sums, pointwise supremum, composition with an affine map. Norms, indicators of convex sets, maxima of affine functions and the sum of the $k$ largest eigenvalues are convex.

## Subgradients

$s$ is a subgradient at $x$ if $f(y)\ge f(x)+\langle s,y-x\rangle$ for all $y$; the set $\partial f(x)$ is closed convex (Thm 3.18). $f$ is differentiable at $x$ iff $\partial f(x)=\{\nabla f(x)\}$ (Thm 3.61). The directional derivative $f'(x;\cdot)$ is the support function of $\partial f(x)$ (Thm 3.60).

## Why it matters

A point $x^*$ minimises $f$ iff $0\in\partial f(x^*)$ (and $0\in\partial f+N_C$ with constraints), and the projected subgradient method converges at rate $MR/\sqrt N$ regardless of dimension ([[Basu ch4 - Convex optimization]]). Full treatment: [[Basu ch3 - Convex functions]].

## Where it appears
- Piecewise linear convex costs reduce to LPs, and the optimal value as a function of $\mathbf b$ is piecewise linear and convex: [[BT ch1 - Introduction]] (§1.3), [[BT ch5 - Sensitivity analysis]] (pp. 213-214).
- The Lagrangean dual function of an integer program is concave and piecewise linear: [[BT ch11 - Integer programming]] (p. 495, Fig. 11.6).
- Convex functions and parametric LP value functions: [[BJS ch2 - Linear algebra convex analysis and polyhedral sets]], [[BJS ch6 - Duality and sensitivity analysis]] (§6.8).

**Sources**: `Math/Convexity/Basu - Intro to Convexity.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Convex set]] · [[Linear programming]] · [[LP duality]]
- [[Basu ch3 - Convex functions]] · [[Basu ch4 - Convex optimization]]
