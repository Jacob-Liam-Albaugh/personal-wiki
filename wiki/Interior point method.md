---
type: method
area: math
source-ref: "Bertsimas, Tsitsiklis 1997, ch. 9; Bazaraa, Jarvis, Sherali 2010, §8.4-8.6"
tags: [optimization]
---

# Interior point method

> [!definition] Barrier problem and central path (source: MIT (ch 1-5).pdf, pp. 419-421)
> For $\mu>0$,
> $$B_\mu(\mathbf x)=\mathbf c'\mathbf x-\mu\sum_j\log x_j$$
> $$\min\ B_\mu(\mathbf x)\ \ \text{s.t. }\mathbf A\mathbf x=\mathbf b$$
> Its minimizers $\mathbf x(\mu)$ form the central path, characterized by
> $$\mathbf A\mathbf x=\mathbf b,\ \ \mathbf x>\mathbf0$$
> $$\mathbf A'\mathbf p+\mathbf s=\mathbf c,\ \ \mathbf s>\mathbf0$$
> $$\mathbf X\mathbf S\mathbf e=\mu\mathbf e$$

**Intuition**: instead of walking along vertices like the [[Simplex method]], move through the interior of the feasible set. At $\mu\to0$ the last equation becomes complementary slackness ([[LP duality]]), and the limit of $\mathbf x(\mu)$ is an LP optimum.

## Key facts
- Three families in BT: affine scaling, potential reduction, path following (BT p. 393-395). All work on the standard-form pair and need a strictly positive start, obtained with an artificial variable and large cost $M$.
- Affine scaling: step to the best point in the ellipsoid $\|\mathbf Y^{-1}\mathbf d\|\le\beta$ inside the positive orthant, giving
$$\mathbf d^*=-\beta\frac{\mathbf Y^2(\mathbf c-\mathbf A'\mathbf p)}{\|\mathbf Y(\mathbf c-\mathbf A'\mathbf p)\|},\quad\mathbf p=(\mathbf A\mathbf Y^2\mathbf A')^{-1}\mathbf A\mathbf Y^2\mathbf c$$
  (BT Lemma 9.2, p. 397). Dual estimates $\mathbf p$ come for free.
- Path following applies Newton's method ([[Newton's method]]) to the barrier problem (primal) or to the perturbed optimality system (primal-dual), with the barrier weight decreasing (BT §9.4-9.5; BJS §8.6). Because the system is the perturbed [[KKT conditions]], the Newton step is the core computation.
- Complexity: potential reduction takes $O(\sqrt n\log\frac1\epsilon+n^2\log(nU))$ iterations at $O(n^3)$ work each (BT p. 418).
- Karmarkar's projective algorithm, the method that started the area, is developed in BJS §8.4-8.5 (only the setup was read here, see [[BJS ch8 - Complexity of the simplex algorithm and polynomial-time algorithms]]).
- BT describe interior point codes as competitive with the simplex method and often faster on large sparse problems (BT p. 393).

## Where it appears
- [[BT ch9 - Interior point methods]]: development of all three families.
- [[BJS ch8 - Complexity of the simplex algorithm and polynomial-time algorithms]]: Karmarkar, affine scaling, predictor-corrector.
- [[BT ch12 - The art in linear optimization]]: simplex versus interior point codes in practice.

**Sources**: `text_books/Linear Optimization/MIT (ch 1-5).pdf` (ch. 9, 12); `text_books/Linear Optimization/BJS full book.pdf` (ch. 8).
**Last updated**: 2026-11-06

---

## Related pages
- [[Linear programming]] · [[Ellipsoid method]] · [[Simplex method]] · [[KKT conditions]] · [[Newton's method]]
