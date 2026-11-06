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

**Compared with** finite differences ($n+1$ evaluations, truncation vs round-off error) and symbolic differentiation (no loops or branches, expression swell).

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

## Where it appears
- PINN residuals need derivatives of the network output with respect to inputs, taken by AD ([[PINNs (Raissi 2019)]]; [[Physics-informed ML review (Karniadakis 2021)]], Box 3).
- Neural ODE gradients use the adjoint method instead of backprop through the solver: [[Adjoint sensitivity method]], [[Neural ODEs (Chen 2018)]].

## Alternatives to autodiff (book, differentiation 01-02)
- **Forward difference**:
  $$f'(x)\approx\frac{f(x+h)-f(x)}{h}$$
  Truncation error falls with $h$ and round-off error grows as $h\to0$, so a log-log error plot shows an optimal $h$. A gradient in $n$ dimensions costs $n+1$ evaluations.
- **Symbolic** (sympy expression trees): cannot differentiate through loops or conditionals, and expressions swell; nested softplus $\log(1+e^{wx+b})$ grows quickly.

> [!example] RBF regression with grad (04)
> Generalized linear model on [[Random features model|RBF features]], squared loss. `grad(loss, argnums=0)` differentiates in the weights and `argnums=(0, 1, 2)` returns a tuple of gradients. A plain [[Gradient descent]] loop fits it.

**Covered in**: ASML book ml-software/differentiation (ME 697 1.3)
**Sources**: `courses/ME 697/advanced-scientific-machine-learning/book/ml-software/differentiation/03_autodiff.ipynb`, `04_jax_grad.ipynb`, `types_and_models/03_haskell.md`, `courses/ME 697/advanced-scientific-machine-learning/book/ml-software/differentiation/01_numerical.ipynb`, `02_symbolic.ipynb`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Pytree]] · [[JIT compilation]]
