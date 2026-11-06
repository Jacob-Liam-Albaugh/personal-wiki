---
type: method
area: ml
areas: [me697, ml]
source-ref: "ME 697 book, ml-software/optimization/02_gradient_descent"
tags: [optimization, ml]
---

# Gradient descent

> [!algorithm] Gradient descent
> $$x_{k+1}=x_k-\alpha\nabla f(x_k)$$
> The negative gradient is the steepest-descent direction: the directional derivative $\nabla f\cdot d$ over unit $d$ is smallest when $\cos\theta=-1$.

**Armijo backtracking** (book, 02): accept $\alpha$ when
$$f(x-\alpha\nabla f)\le f(x)-c_1\alpha\|\nabla f\|^2$$
otherwise shrink $\alpha\leftarrow c_2\alpha$ and retry.

**Continuous limit**: gradient flow $\dot x=-\nabla f(x)$. Wiki note: add noise $\sqrt2\,dW$ and this becomes overdamped [[Langevin dynamics]], whose density evolves by the [[Fokker-Planck equation]].

**Failure modes** (book, 01): slow on plateaus and ill-conditioned valleys, stuck exactly on saddles. Fixes are [[Momentum]], adaptive rates ([[Adam]]), curvature ([[Newton's method]]).

**Variants**: minibatch gradients give [[SGD]]; SGD plus Gaussian noise gives [[SGLD]].

**Sources**: `advanced-scientific-machine-learning/book/ml-software/optimization/01_optimization_problems.md`, `02_gradient_descent.ipynb`, `03_momentum.ipynb`.
**Last updated**: 2026-11-06

---

## Related pages
- [[ME697 1.4 - Optimization]] · [[Automatic differentiation]] · [[Pytree]]
