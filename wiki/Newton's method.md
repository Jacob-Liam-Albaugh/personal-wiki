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

## Where it appears
- Newton's method on the log-barrier problem and on the perturbed optimality system gives primal and primal-dual path-following interior point methods: [[Interior point method]], [[BT ch9 - Interior point methods]] (§9.4-9.5), [[BJS ch8 - Complexity of the simplex algorithm and polynomial-time algorithms]] (§8.6).

**Covered in**: ASML book ml-software/optimization (ME 697 1.4)
**Sources**: `advanced-scientific-machine-learning/book/ml-software/optimization/07_second_order.ipynb`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Gradient descent]] · [[Adam]]
