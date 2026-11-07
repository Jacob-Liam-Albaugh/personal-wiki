---
type: theorem
area: ml
areas: [ml, operators]
source-ref: "Hornik, Stinchcombe, White 1989, Thms 2.1-2.4, Thm 2.5, Cors 2.1-2.7"
tags: [ml]
---

# Universal approximation theorem

> [!theorem] Universal approximation (Hornik, Stinchcombe, White 1989)
> Let $\Sigma^r(\Psi)$ be the single-hidden-layer networks $f(x)=\sum_{j=1}^q\beta_j\Psi(w_j\cdot x+b_j)$ on $\mathbb R^r$.
> - For every squashing function $\Psi$ (non-decreasing, limits 0 and 1, not necessarily continuous), $\Sigma^r(\Psi)$ is uniformly dense on compacta in the continuous functions $C^r$: for every compact $K$, continuous $g$ and $\epsilon>0$ there is $f$ with $\sup_{x\in K}|f(x)-g(x)|<\epsilon$.
> - For every probability measure $\mu$ it is dense in the Borel measurable functions in the metric $\rho_\mu(f,g)=\inf\{\epsilon:\mu\{|f-g|>\epsilon\}<\epsilon\}$ (convergence in probability).
> - If $\Psi$ is only continuous and nonconstant (no squashing), the same holds for the class that also allows products of units ($\Sigma\Pi$ networks); the paper notes the result extends to any activation whose network class uniformly approximates some squashing function on compacta.
>
> (source: [[Universal approximation (Hornik 1989)]], Thms 2.1-2.4, pp. 3-4)

**Intuition**: with enough hidden units, shifted and scaled copies of one nonlinear bump can be combined into any shape. The statement is about the closure of a model class, so it only says an approximating network exists. It does not say how many units are needed, how to find the weights, or whether they generalize.

## Proof idea
For continuous $G$, the products-of-units class is an algebra on $K$ that separates points and vanishes nowhere, so Stone-Weierstrass gives density. The sum-only class for squashing functions follows by building cosines out of squashers and using that trigonometric polynomials are dense (Appendix, pp. 6-7). Measurable targets follow from Lusin's theorem and Lemma 2.2: uniform convergence on compacta implies convergence in probability.

## Variants in the paper
- Fit $n$ distinct points exactly with $n$ hidden units (Thm 2.5, p. 5).
- $L_p(\mu)$ density for compactly supported $\mu$ (Cor. 2.2); Boolean functions (Cor. 2.5).
- Multi-output and multi-hidden-layer networks (Cors 2.6-2.7, p. 5).

## Failure modes / non-examples
- No rate in the number of units and no dependence on the input dimension $r$ is given (authors' stated open problems, pp. 5-6). For lower bounds in the operator setting see [[Curse of parametric complexity]].
- Says nothing about optimization or the statistical error. [[DeepONet (Lu 2021)]] makes the same point: approximation error is only one of three errors, and optimization and generalization "are often dominant" (p. 3 there).
- A fixed-size network is not covered: density requires the width to grow.

## Where it appears
- [[Universal approximation (Hornik 1989)]] — the source.
- [[NTK (Jacot 2018)]] — cites this family of results to contrast approximation power with the open question of what training converges to, and expects last-layer features to be dense (Jacot, pp. 1, 6).
- [[Universal approximation for operators]] — the operator-valued analogue (Chen-Chen), used by [[DeepONet (Lu 2021)]] and [[Neural operator (Kovachki 2022)]].

**Sources**: `papers/ML/Hornik, Stinchcombe, White - Multilayer Feedforward Networks are Universal Approximators.pdf`.
**Last updated**: 2026-11-07

---

## Related pages
- [[Universal approximation (Hornik 1989)]] · [[Universal approximation for operators]] · [[Operator learning]]
- [[Neural tangent kernel]] · [[Spectral bias]] · [[Curse of parametric complexity]]
