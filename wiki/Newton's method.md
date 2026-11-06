---
type: method
area: ml
areas: [me697, ml, math]
source-ref: "ME 697 book, ml-software/optimization/07_second_order"
tags: [optimization]
---

# Newton's method

> [!algorithm] Newton step
> $$x_{k+1}=x_k-\alpha\,[\nabla^2f(x_k)]^{-1}\nabla f(x_k)$$
> On a quadratic with $\alpha=1$ it reaches the minimum in one step.

**Cost**: forming and solving with the $n\times n$ Hessian is $O(n^3)$ per step, too much for neural networks. JAX gives the Hessian directly (`hessian`, [[Automatic differentiation]]), or Hessian-vector products without forming it.

**Quasi-Newton**
- BFGS: builds an inverse-Hessian approximation from gradient differences; stores an $n\times n$ matrix.
- L-BFGS: keeps only the last few gradient pairs. In JAX, `jaxopt.LBFGS`.
- Book's advice: L-BFGS for small datasets and problems with a unique solution; otherwise run several restarts. A stochastic L-BFGS-B exists.

**Saddles**: the Newton step moves toward any stationary point, including saddles (Wiki note); first-order methods with noise ([[SGD]]) are preferred in deep learning partly for this reason.

**Wiki note**: L-BFGS is common for the final stage of [[PINN]] training, after [[Adam]].

## Newton steps in interior point methods
Newton's method on the log-barrier problem and on the perturbed optimality system gives the primal and primal-dual path-following interior point methods ([[Path-following interior point methods]], [[Interior point method]]; BT §9.4-9.5, BJS §8.6). Two uses:
- Newton step on the barrier: minimize the second-order Taylor model of $B_\mu(\mathbf x+\mathbf d)$ subject to $\mathbf A\mathbf d=\mathbf0$, a linear system.
- Newton root finding $\mathbf F(\mathbf z^k)+\mathbf J(\mathbf z^k)\mathbf d=\mathbf0$ applied to the perturbed KKT system in $\mathbf z=(\mathbf x,\mathbf p,\mathbf s)$ ([[KKT conditions]]).

**Covered in**: ASML book ml-software/optimization (ME 697 1.4); Bertsimas-Tsitsiklis ch. 9 §9.4-9.5 (pp. 419-437); Bazaraa-Jarvis-Sherali ch. 8 §8.6 (pp. 433-434)
**Sources**: `text_books/advanced-scientific-machine-learning/book/ml-software/optimization/07_second_order.ipynb`; `text_books/Linear Optimization/MIT (ch 1-5).pdf` (ch. 9); `text_books/Linear Optimization/BJS full book.pdf` (ch. 8).
**Last updated**: 2026-11-06

---

## Related pages
- [[Gradient descent]] · [[Adam]] · [[Interior point method]] · [[Path-following interior point methods]]
