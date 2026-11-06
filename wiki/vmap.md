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

> [!example] RBF features with vmap (03)
> One radial basis function
> 23923\phi(x;c)=\exp\big(-\|x-c\|^2/\sigma^2\big)23923
> written for a single centre, then `vmap(rbf, in_axes=(None,0,None))` maps over a stack of centres. Same model as the [[Random features model]].

**Patterns**
- Stack as decorators: `@jit` over `@partial(vmap, in_axes=...)` ([[JIT compilation]]).
- On an Equinox module's `__call__`: `in_axes=(None, 0)` keeps the parameters fixed and maps over inputs ([[Pytree]]).
- Wiki note: per-example gradients are `vmap(grad(loss), in_axes=(None, 0))`, used for minibatch estimators in [[SGD]] and [[SGLD]].

> [!example] Homework 1, problem 4: logistic map (source: homework/01_homework.ipynb)
> $x_{n+1}=r\,x_n(1-x_n)$ vectorized over $r$ and $x_0$ with `vmap`; output shape (1000, 100, 10000); period-doubling plot.

**Covered in**: ASML book ml-software/functional_programming (ME 697 1.1); homework 1
**Sources**: `text_books/advanced-scientific-machine-learning/book/ml-software/functional_programming/03_vectorization.ipynb`, `types_and_models/03_haskell.md`, `types_and_models/04_pytrees.ipynb`, `text_books/advanced-scientific-machine-learning/book/ml-software/functional_programming/01_primer.ipynb`, `02_jit.ipynb`, `04_random.ipynb`.
**Last updated**: 2026-11-06

---

## Related pages
- [[JIT compilation]] · [[Pytree]]
