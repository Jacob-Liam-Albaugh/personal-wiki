---
type: definition
area: me697
areas: [me697, ml]
source-ref: "ME 697 book, ml-software/functional_programming/03_vectorization; types_and_models/03_haskell"
tags: [software]
---

# vmap

> [!definition] jax.vmap
> ```
> vmap :: (a -> b) -> ([a] -> [b])
> ```
> Turns a function of one example into a function of a batch. `in_axes` says which argument is batched and along which axis; `None` means broadcast.

**Example** (book, 03): an RBF written for one centre,
$$\phi(x;c)=\exp(-\|x-c\|^2/\sigma^2)$$
becomes a feature map over all centres with `vmap(rbf, in_axes=(None, 0, None))`. That feature map is the [[Random features model]] with fixed centres.

**Patterns**
- Stack as decorators: `@jit` over `@partial(vmap, in_axes=...)` ([[JIT compilation]]).
- On an Equinox module's `__call__`: `in_axes=(None, 0)` keeps the parameters fixed and maps over inputs ([[Pytree]]).
- Wiki note: per-example gradients are `vmap(grad(loss), in_axes=(None, 0))`, used for minibatch estimators in [[SGD]] and [[SGLD]].

**Sources**: `advanced-scientific-machine-learning/book/ml-software/functional_programming/03_vectorization.ipynb`, `types_and_models/03_haskell.md`, `types_and_models/04_pytrees.ipynb`.
**Last updated**: 2026-11-06

---

## Related pages
- [[ME697 1.1 - Functional programming in JAX]] · [[JIT compilation]] · [[Pytree]]
