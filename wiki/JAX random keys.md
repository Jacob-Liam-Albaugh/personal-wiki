---
type: concept
area: me697
areas: [me697, ml]
source-ref: "ME 697 book, ml-software/functional_programming/04_random"
tags: [software, sampling]
---

# JAX random keys

> [!definition] Explicit PRNG state
> `key = jax.random.PRNGKey(0)` is a pair of uint32. Every sampler takes a key as an argument; the same key gives the same draw. New randomness comes from `key, subkey = jax.random.split(key)`.

**Why**: a global seed is hidden state, which breaks purity and therefore [[JIT compilation]] and [[vmap]]. Passing keys keeps random functions pure and reproducible.

> [!example] Random walk with scan (04)
> Split one key into many, then `lax.scan` over them to take 100,000 random-walk steps inside one compiled loop.

**Never reuse a key** for two draws that should be independent. Wiki note: this matters for the injected noise in [[SGLD]], [[SGHMC]] and [[Langevin dynamics]], and for the noise in the [[Reparameterization trick]].

**Covered in**: ASML book ml-software/functional_programming (ME 697 1.1)
**Sources**: `advanced-scientific-machine-learning/book/ml-software/functional_programming/04_random.ipynb`.
**Last updated**: 2026-11-06

---

## Related pages
- [[JIT compilation]] · [[vmap]]
