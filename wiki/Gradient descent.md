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

## Where it appears
- [[Neural tangent kernel]] — gradient-descent dynamics of a network in function space are governed by the NTK; [[When and why PINNs fail (Wang 2022)]].
- Subgradient optimization of the concave piecewise linear Lagrangean dual of an integer program, with step $\theta_t=\alpha_t(\hat Z_D-Z(\mathbf p^t))/\|\mathbf s^t\|^2$ (form read from text, unverified): [[BT ch11 - Integer programming]] (pp. 502-507).
- Affine scaling takes a steepest-descent-like step on the cost inside a scaling ellipsoid: [[Interior point method]], [[BT ch9 - Interior point methods]] (Lemma 9.2, p. 397).

> [!example] 1D and 2D test functions (02-03)
> $f(x)=x^4-3x^3+2$ from $x_0=2$, and the saddle function
> $$f(x)=x_0^4-2x_0^2+x_1^2$$
> used for gradient descent, momentum and Nesterov.

**Covered in**: ASML book ml-software/optimization (ME 697 1.4)
**Sources**: `advanced-scientific-machine-learning/book/ml-software/optimization/01_optimization_problems.md`, `02_gradient_descent.ipynb`, `03_momentum.ipynb`, `09_gpu_training.ipynb`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Automatic differentiation]] · [[Pytree]]
- [[Init and momentum (Sutskever 2013)]], [[Adam paper (Kingma 2015)]].
- Large-model training recipes: [[DeepSeek-V2 (DeepSeek-AI 2024)]] (AdamW, stepwise learning rate decay).
