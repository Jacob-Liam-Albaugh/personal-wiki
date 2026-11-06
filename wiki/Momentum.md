---
type: method
area: ml
areas: [me697, ml]
source-ref: "ME 697 book, ml-software/optimization/03_momentum, 04_optax"
tags: [optimization, ml]
---

# Momentum

> [!algorithm] Heavy-ball momentum (Sutskever et al. 2013, via the book)
> $$v_{t+1}=\beta v_t-\alpha\nabla f(x_t)$$
> $$x_{t+1}=x_t+v_{t+1}$$
> $\beta$ is typically 0.9.

**Derivation** (book, 03): a particle of mass $m$ with friction $\gamma$,
$$m\ddot x=-\nabla f(x)-\gamma\dot x$$
Euler steps of size $\Delta t$ give the update above with
$$\alpha=\Delta t^2/m,\quad \beta=1-\Delta t\,\gamma/m$$

**Nesterov**: take the gradient at the look-ahead point,
$$v_{t+1}=\beta v_t-\alpha\nabla f(x_t+\beta v_t)$$

**Behaviour**: carries the iterate across plateaus and damps zig-zag in narrow valleys. Started exactly on a saddle with zero velocity it does not move; in optax a small initial `trace` (e.g. `[0.1, 0]`) escapes.

**Link to samplers** (Wiki note): add Gaussian noise scaled to the friction and this is [[SGHMC]], the stochastic-gradient version of underdamped [[Langevin dynamics]]. Momentum is the noise-free limit.

**In optax**: `optax.sgd(lr, momentum=β)`; the state's `trace` is the velocity, a [[Pytree]] like the parameters.

**Sources**: `advanced-scientific-machine-learning/book/ml-software/optimization/03_momentum.ipynb`, `04_optax.ipynb`.
**Last updated**: 2026-11-06

---

## Related pages
- [[ME697 1.4 - Optimization]] · [[Gradient descent]] · [[Adam]] · [[SG-MCMC]]
