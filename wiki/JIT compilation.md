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
- New shapes or dtypes trigger a recompile, which is why the course cares about [[Pytree|types]].

**Composes with** [[vmap]], `grad` ([[Automatic differentiation]]), and Equinox's `eqx.filter_jit`, which jits a function of a [[Pytree]] that also holds non-array leaves.

## Primer and GPU use
- JAX only transforms pure functions (no side effects, output depends only on input). The plain-Python background is `map`, `filter`, `reduce`, partial application and currying, function composition, and decorators as functions taking functions (source: `functional_programming/01_primer.ipynb`).
- JAX uses the GPU by default when one is present. The MNIST CNN of the optimization chapter (Equinox, optax, `eqx.filter_jit`) trained 5-10 times faster than on CPU (source: `optimization/09_gpu_training.ipynb`).

> [!example] Homework 1, problems 1-3 (source: homework/01_homework.ipynb)
> Fibonacci with tail recursion and no loops; `foldl` and its use for sum and product; Fibonacci again with `lax.scan` plus `jit`.

**Covered in**: ASML book ml-software/functional_programming (ME 697 1.1); ASML book ml-software/optimization (ME 697 1.4); homework 1
**Sources**: `courses/ME 697/advanced-scientific-machine-learning/book/ml-software/functional_programming/02_jit.ipynb`, `optimization/09_gpu_training.ipynb`, `courses/ME 697/advanced-scientific-machine-learning/book/ml-software/functional_programming/01_primer.ipynb`, `03_vectorization.ipynb`, `04_random.ipynb`, `courses/ME 697/advanced-scientific-machine-learning/book/ml-software/optimization/01_optimization_problems.md`.
**Last updated**: 2026-11-06

---

## Related pages
- [[vmap]] · [[JAX random keys]] · [[Pytree]]
