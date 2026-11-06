---
type: method
area: ml
areas: [me697, ml]
source-ref: "ME 697 book, ml-software/differentiation/03_autodiff, 04_jax_grad"
tags: [software, optimization, ml]
---

# Automatic differentiation

> [!algorithm] Forward and reverse mode
> Write $f=f_L\circ\cdots\circ f_1$ with Jacobians $J_\ell$. Then
> $$J_f=J_L\cdots J_1$$
> - Forward mode (JVP): push a tangent $v$ through, $J_L(\cdots(J_1v))$. One pass per input direction.
> - Reverse mode (VJP): pull a cotangent $u$ back, $((u^\top J_L)\cdots)J_1$. One pass per output.

**Cost**: for a scalar loss of $n$ parameters, forward mode needs $n$ passes and reverse mode one. Reverse mode is backpropagation; it stores every intermediate of the forward pass. No Jacobian is ever formed, only products with one.

**General graphs**: a DAG of primitives becomes a chain using a fanout $x\mapsto(x,x)$ with Jacobian $[I;I]$. Example: $x^2+x$ is `add ∘ (sqr, id) ∘ fanout`.

**Compared with** finite differences ($n+1$ evaluations, truncation vs round-off error) and symbolic differentiation (no loops or branches, expression swell); see [[ME697 1.3 - Differentiation]].

**In JAX**
```
grad     :: ([a] -> a) -> ([a] -> [a])
jacobian :: ([a] -> [a])
            -> ([a] -> [[a]])
hessian  :: ([a] -> a)
            -> ([a] -> [[a]])
```
`grad(f, argnums=(0, 1))` returns a tuple; `value_and_grad` returns both. Gradients of [[Pytree|pytree]] arguments are pytrees.

**Where it is used**: every optimizer ([[Gradient descent]], [[Adam]], [[Newton's method]]); the [[Reparameterization trick]] and [[ELBO]] gradients; input derivatives in [[PINN]] residuals; score and drift networks in [[Score matching]].

**Further reading** (named in the book): Matt Johnson's Autodidact.

**Sources**: `advanced-scientific-machine-learning/book/ml-software/differentiation/03_autodiff.ipynb`, `04_jax_grad.ipynb`, `types_and_models/03_haskell.md`.
**Last updated**: 2026-11-06

---

## Related pages
- [[ME697 1.3 - Differentiation]] · [[ME697 1.2 - Types and pytrees]] · [[JIT compilation]]
