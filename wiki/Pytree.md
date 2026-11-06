---
type: definition
area: me697
areas: [me697, ml]
source-ref: "ME 697 book, ml-software/types_and_models/04_pytrees"
tags: [software, ml]
---

# Pytree

> [!definition] Pytree
> A nested container of lists, tuples, dicts and namedtuples (or registered classes) whose leaves are arrays. JAX transformations accept and return pytrees.

**Operations**
- `tree_structure`, `tree_leaves`
- `tree_flatten` / `tree_unflatten`
- `tree_map(f, t1, t2, ...)` applies `f` leaf by leaf
- `tree_reduce(op, t)` folds over leaves

**Why it matters**: the gradient of a scalar loss in a pytree of parameters is a pytree of the same shape ([[Automatic differentiation]]). So an optimizer step is one `tree_map`:
```
tree_map(lambda x, g: x - lr*g,
         params, grads)
```
That is [[Gradient descent]]; optax's [[Momentum]] and [[Adam]] states are pytrees too.

**Equinox**: an `eqx.Module` is a pytree, so a model is its own parameter container. Chosen in the course over Flax and Haiku for that reason. `eqx.filter_jit` jits functions of modules that hold non-array leaves ([[JIT compilation]]).

**Sources**: `advanced-scientific-machine-learning/book/ml-software/types_and_models/04_pytrees.ipynb`.
**Last updated**: 2026-11-06

---

## Related pages
- [[ME697 1.2 - Types and pytrees]] · [[vmap]] · [[Neural operator]] (parameters are pytrees in a JAX build)
