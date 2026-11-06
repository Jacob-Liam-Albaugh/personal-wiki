---
type: definition
area: me697
areas: [me697, ml]
source-ref: "ME 697 book, ml-software/functional_programming/02_jit"
tags: [software]
---

# JIT compilation

> [!definition] jax.jit
> `jit(f)` traces a pure function with abstract inputs of fixed shape and dtype, builds a graph, and compiles it with XLA. Later calls with the same shapes and dtypes reuse the compiled code.

**Rules that follow from tracing**
- Only pure functions are safe. A `print` or other side effect runs once, at trace time.
- Python loops are unrolled. For long loops use `lax.fori_loop`, `lax.while_loop`, `lax.scan`.
- `if` on a traced value fails. Use `lax.cond` / `lax.switch`, or `static_argnums` (one recompile per new value).
- New shapes or dtypes trigger a recompile, which is why the course cares about [[ME697 1.2 - Types and pytrees|types]].

**Composes with** [[vmap]], `grad` ([[Automatic differentiation]]), and Equinox's `eqx.filter_jit`, which jits a function of a [[Pytree]] that also holds non-array leaves.

**Sources**: `advanced-scientific-machine-learning/book/ml-software/functional_programming/02_jit.ipynb`, `optimization/09_gpu_training.ipynb`.
**Last updated**: 2026-11-06

---

## Related pages
- [[ME697 1.1 - Functional programming in JAX]] · [[vmap]] · [[JAX random keys]] · [[Pytree]]
