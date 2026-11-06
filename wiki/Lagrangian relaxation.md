---
type: method
area: math
source-ref: "Bertsimas, Tsitsiklis 1997, §11.4; Bazaraa, Jarvis, Sherali 2010, §11.7"
tags: [optimization]
---

# Lagrangian relaxation

> [!definition] Lagrangean dual of an integer program (source: MIT (ch 1-5).pdf, pp. 494-495, eqs. 11.5-11.7)
> $$\min\ \mathbf c'\mathbf x\quad\text{s.t. }\mathbf A\mathbf x\ge\mathbf b,\ \mathbf D\mathbf x\ge\mathbf d,\ \mathbf x\text{ integer}$$
> Let $X=\{\mathbf x\text{ integer}\mid\mathbf D\mathbf x\ge\mathbf d\}$, a set easy to optimize over (e.g. assignment). Dualize the hard constraints with $\mathbf p\ge\mathbf0$:
> $$Z(\mathbf p)=\min_{\mathbf x\in X}\big(\mathbf c'\mathbf x+\mathbf p'(\mathbf b-\mathbf A\mathbf x)\big),\qquad Z_D=\max_{\mathbf p\ge\mathbf0}Z(\mathbf p)$$

**Intuition**: a bound for [[Integer programming]] from relaxing complicating constraints into the objective; see [[Lagrangian duality]] for the convex theory. $Z(\mathbf p)$ is a minimum of finitely many linear functions of $\mathbf p$, so it is concave and piecewise linear (Fig. 11.6, p. 495). Lagrangian relaxation, [[Dantzig-Wolfe decomposition]] and [[Benders decomposition]] are equivalent for LPs (BJS p. 339).

## Bounds
> [!theorem] Lemma 11.1 and weak duality (BT p. 494-495)
> If the problem has an optimal solution and $\mathbf p\ge\mathbf0$, then $Z(\mathbf p)\le Z_{IP}$, hence $Z_D\le Z_{IP}$ (Thm 11.2). Proof idea: at an optimal $\mathbf x^*$, $\mathbf b-\mathbf A\mathbf x^*\le\mathbf0$ and $\mathbf x^*\in X$.

Unlike [[LP duality]] there is no strong duality in general (pp. 495-496, Example 11.8).

> [!theorem] Theorems 11.3-11.4 (BT p. 496)
> If $\mathbf D\mathbf x\ge\mathbf d$ is feasible with integer data, $\mathrm{CH}(X)$ is a polyhedron ([[Polyhedron]]). $Z_D$ equals the optimal cost of the LP $\min\mathbf c'\mathbf x$ s.t. $\mathbf A\mathbf x\ge\mathbf b$, $\mathbf x\in\mathrm{CH}(X)$.

The proof replaces $X$ by $\mathrm{CH}(X)$ in $Z(\mathbf p)$, writes it by extreme points and rays and applies LP duality (pp. 496-497). Hence (p. 499)
$$Z_{LP}\le Z_D\le Z_{IP}$$
Example 11.8 (pp. 498-500): minimizing $3x_1-x_2$ with the first constraint relaxed gives $Z_D=-1/3$ at $p=5/3$, against $Z_{LP}=-9/5$ and $Z_{IP}=1$. Corollary 11.1 (p. 500): (a) $Z_{IP}=Z_D$ for all costs iff $\mathrm{CH}(X\cap\{\mathbf A\mathbf x\ge\mathbf b\})=\mathrm{CH}(X)\cap\{\mathbf A\mathbf x\ge\mathbf b\}$; (b) $Z_{LP}=Z_D$ for all costs if $\mathrm{CH}(X)=\{\mathbf D\mathbf x\ge\mathbf d\}$. The Lagrangean master and the Dantzig-Wolfe master are views of the same convexified problem; Theorem 11.4 is the integer analogue of strong duality only after $X$ is replaced by $\mathrm{CH}(X)$.

**Held-Karp bound** (Example 11.10, pp. 501-502): the Lagrangean dual of the subtour-elimination TSP formulation ([[Integer programming]]), with $Z_D=Z_{LP}$ by Corollary 11.1(b); $Z(\mathbf p)$ is computed through minimum 1-trees.

## Subgradient optimization (BT pp. 502-507)
$Z(\mathbf p)$ is concave but not differentiable, so steepest ascent is replaced by subgradients: $\mathbf s$ with $Z(\mathbf q)\le Z(\mathbf p)+\mathbf s'(\mathbf q-\mathbf p)$ for all $\mathbf q$ (Lemma 11.4). The subdifferential at $\mathbf p$ is the convex hull of the gradients of the active pieces (Fig. 11.11, Exercise 11.10).

> [!algorithm] Subgradient ascent (BT p. 505)
> 1. Choose $\mathbf p^1$, $t=1$.
> 2. Pick a subgradient $\mathbf s^t$ at $\mathbf p^t$; stop if $\mathbf s^t=\mathbf0$.
> 3. Set $\mathbf p^{t+1}=\mathbf p^t+\theta_t\mathbf s^t$, $t\leftarrow t+1$.

Typical step $\theta_t=\alpha_t(\hat Z_D-Z(\mathbf p^t))/\|\mathbf s^t\|^2$ with $0<\alpha_t<1$ and $\hat Z_D$ an estimate of $Z_D$ (pp. 505-506, read from text, **[unverified]** exact form). To keep $\mathbf p\ge\mathbf0$ project onto the nonnegative orthant. Convergence is not monotone (Table 11.1). This is the [[Subgradient method]] (projected [[Gradient descent]] with nonsmooth steps) applied to a concave function.

## Relaxation algorithms for network flows (BJS §11.7)
For $\min\{\mathbf c\mathbf x:\mathbf A\mathbf x=\mathbf b,\ \mathbf0\le\mathbf x\le\mathbf u\}$ the dual function is $\theta(\mathbf w)=\mathbf w\mathbf b+\min\{(\mathbf c-\mathbf w\mathbf A)\mathbf x:\mathbf0\le\mathbf x\le\mathbf u\}$ and the inner minimum is solved arc by arc; see [[Out-of-kilter algorithm]].

**Covered in**: Bertsimas-Tsitsiklis ch. 11 §11.4 (pp. 494-507); Bazaraa-Jarvis-Sherali ch. 11 §11.7 (pp. 593-598)
**Sources**: `text_books/Linear Optimization/MIT (ch 1-5).pdf` (ch. 11; pdf 498 viewed as image); `text_books/Linear Optimization/BJS full book.pdf` (ch. 11).
**Last updated**: 2026-11-06

---

## Related pages
- [[Integer programming]] · [[Lagrangian duality]] · [[Subgradient method]] · [[LP duality]] · [[Branch and bound]] · [[Dantzig-Wolfe decomposition]]
- [[Gradient descent]] · [[Polyhedron]] · [[Out-of-kilter algorithm]]
