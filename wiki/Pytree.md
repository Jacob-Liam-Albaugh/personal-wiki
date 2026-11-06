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

## Types and signatures (book, types_and_models 01-03)
Compilation needs static types, so the book reads JAX transformations as typed higher-order functions in Haskell notation.
```
map     :: (T -> U) -> [T] -> [U]
filter  :: (T -> Bool) -> [T] -> [T]
compose :: (U -> V) -> (T -> U)
           -> (T -> V)
vmap    :: (a -> b) -> ([a] -> [b])
grad    :: ([a] -> a) -> ([a] -> [a])
jacobian:: ([a] -> [a])
           -> ([a] -> [[a]])
hessian :: ([a] -> a) -> ([a] -> [[a]])
fori_loop :: Int -> Int
  -> ((Int, a) -> a) -> a -> a
```
Currying: a two-argument function has type `T -> U -> V`. Python annotations such as `List[int]` and `Callable[[int], int]` carry the same information. The arrows read like those of [[Polynomial functor]] and [[Dependent lens]], informally.

> [!failure] jvp signature
> The book gives `jvp :: ([a] -> a) -> [a] -> [a] -> [a]`. Wiki note: `jax.jvp(f, primals, tangents)` returns the pair `(f(x), J v)`, so the result type is a tuple, not a single list.

> [!example] Hand-built network (04)
> Parameters in a dict of weight and bias arrays; one gradient step by `tree_map` as above. An L2 penalty is `tree_reduce` of `tree_map(lambda x: x**2)`. `value_and_grad` returns loss and gradient together.

> [!example] Equinox SimpleNN (04)
> An `eqx.Module` with `eqx.nn.Linear` layers; `__call__` decorated with `@partial(vmap, in_axes=(None, 0))` so it maps over a batch.

**Covered in**: ASML book ml-software/types_and_models (ME 697 1.2)
**Sources**: `advanced-scientific-machine-learning/book/ml-software/types_and_models/04_pytrees.ipynb`, `advanced-scientific-machine-learning/book/ml-software/types_and_models/01_why.md`, `02_typing.md`, `03_haskell.md`.
**Last updated**: 2026-11-06

---

## Related pages
- [[vmap]] · [[Neural operator]] (parameters are pytrees in a JAX build)
