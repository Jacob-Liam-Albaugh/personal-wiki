---
type: paper
area: ml
areas: [ml]
source-ref: "Hornik, Stinchcombe, White 1989, Neural Networks 2, Thms 2.1-2.5, Cors 2.1-2.7"
tags: [ml]
authors: ["[[Kurt Hornik]]", "[[Maxwell Stinchcombe]]", "[[Halbert White]]"]
year: 1989
venue: "Neural Networks 2"
file: "papers/ML/Hornik, Stinchcombe, White - Multilayer Feedforward Networks are Universal Approximators.pdf"
---

# Universal approximation (Hornik 1989)

**Summary**: Proves that a feedforward network with one hidden layer and an arbitrary squashing (or, more generally, any continuous nonconstant) activation can approximate any continuous function on a compact set uniformly, and any Borel measurable function in probability, provided enough hidden units are allowed. The proof is a short application of the Stone-Weierstrass theorem. The paper gives no rate: it says nothing about how many units are needed.

**Authors**: Kurt Hornik, Maxwell Stinchcombe, Halbert White · **Year**: 1989 · **File**: `papers/ML/Hornik, Stinchcombe, White - Multilayer Feedforward Networks are Universal Approximators.pdf`

---

Page numbers below are PDF pages 1-8 (journal pages 359-366).

## Problem

Minsky and Papert showed that the two-layer perceptron cannot represent a wide class of functions. Multilayer networks then worked well in practice, and the paper asks whether that success is "some deep and fundamental approximation capability" or luck (p. 1). Kolmogorov's superposition theorem does not answer it, because it needs a different unknown inner function for each target and fixes the number of units (p. 1). Earlier work (le Cun; Lapedes-Farber) used two hidden layers; Gallant-White covered only the cosine squasher (p. 2).

## Method

**Classes of networks** (Defs 2.1-2.4, p. 2). Let $A^r$ be the affine maps $A(x)=w\cdot x+b$ on $\mathbb R^r$.

> [!definition] Sigma and Sigma-Pi networks
> For a Borel measurable $G:\mathbb R\to\mathbb R$,
> $$\Sigma^r(G)=\Big\{f(x)=\sum_{j=1}^q\beta_j\,G(A_j(x))\Big\},\qquad
> \Sigma\Pi^r(G)=\Big\{f(x)=\sum_{j=1}^q\beta_j\prod_{k=1}^{l_j}G(A_{jk}(x))\Big\}.$$
> $\Sigma^r(G)$ is the single-hidden-layer network with no squashing on the output; $\Sigma\Pi$ is the special-product case ($l_j=1$ gives $\Sigma$).
>
> (source: Defs 2.2, 2.4, p. 2)

> [!definition] Squashing function
> $\Psi:\mathbb R\to[0,1]$ non-decreasing with $\lim_{\lambda\to\infty}\Psi=1$ and $\lim_{\lambda\to-\infty}\Psi=0$. Examples: threshold, ramp, logistic-type, and the Gallant-White cosine squasher.
>
> (source: Def. 2.3, p. 2)

**Notions of closeness** (Defs 2.7-2.9, p. 3). Uniform on compacta: $\rho_K(f,g)=\sup_{x\in K}|f(x)-g(x)|$ for every compact $K$. For a probability measure $\mu$ on $\mathbb R^r$: $\rho_\mu(f,g)=\inf\{\epsilon>0:\mu\{|f-g|>\epsilon\}<\epsilon\}$, which metrizes convergence in probability.

### Main theorems

> [!theorem] Theorem 2.1 (continuous activations)
> If $G$ is any continuous nonconstant function, $\Sigma\Pi^r(G)$ is uniformly dense on compacta in $C^r$.
>
> (source: p. 3)

> [!theorem] Theorems 2.2-2.4 (measurable targets, squashing functions)
> - Thm 2.2: for continuous nonconstant $G$ and every probability measure $\mu$, $\Sigma\Pi^r(G)$ is $\rho_\mu$-dense in the Borel measurable functions $M^r$.
> - Thm 2.3: for every squashing function $\Psi$ (continuous or not), $\Sigma\Pi^r(\Psi)$ is uniformly dense on compacta in $C^r$ and $\rho_\mu$-dense in $M^r$.
> - Thm 2.4: the same holds for the plain single-hidden-layer class $\Sigma^r(\Psi)$.
>
> The result holds "regardless of the squashing function, the dimension of the input space, and the input space environment $\mu$".
>
> (source: pp. 3-4)

See [[Universal approximation theorem]] for the consolidated statement.

### Corollaries (pp. 4-5)

- Cor. 2.1: for measurable $g$ and $\epsilon>0$ there is $f\in\Sigma^r(\Psi)$ and a compact $K$ with $\mu(K)>1-\epsilon$ and $|f-g|<\epsilon$ on $K$ (via Lusin's theorem).
- Cor. 2.2-2.3: density in $L_p(\mu)$, $p\in[1,\infty)$, when $\mu$ has compact support (or lives on $[0,1]^r$).
- Cor. 2.4-2.5: on a finite set of inputs, or for Boolean functions, a single hidden layer fits to any tolerance.
- Thm 2.5: $n$ distinct points can be fitted exactly by a network with $n$ hidden units (stated for squashing functions that attain 0 and 1; general case "with some tedious modifications").
- Cor. 2.6-2.7: multi-output networks, and networks with several hidden layers (at least one hidden layer, $l\ge2$), are universal approximators of vector-valued functions.

### Proof idea (Appendix, pp. 6-7)

> [!proof]
> **Theorem 2.1.** Apply the Stone-Weierstrass theorem: an algebra of continuous functions on a compact $K$ that separates points and vanishes nowhere is uniformly dense in $C(K)$.
> - $\Sigma\Pi^r(G)$ is an algebra because products of products of $G(A_j)$ are again of that form.
> - It separates points: for $x\neq y$ pick $a\neq b$ with $G(a)\neq G(b)$ ($G$ nonconstant) and an affine $A$ with $A(x)=a$, $A(y)=b$.
> - It vanishes nowhere: choose $b$ with $G(b)\neq0$ and the constant affine map $A\equiv b$.
>
> **Theorem 2.4 (squashing, sum only).** Lemma A.2 approximates any continuous squashing function by a finite sum of shifted copies of an arbitrary squashing function $\Psi$; then the cosine squasher gives $\cos(A(\cdot))$ on any bounded interval (Lemma A.3); trigonometric polynomials, which are dense by Thm 2.1, can be rewritten as sums of cosines via $\cos a\cos b=\cos(a+b)-\cos(a-b)$ (Lemma A.5), so no products are needed.
>
> (source: Appendix, pp. 6-7; Thm 2.1 proof is complete in the paper, the later lemmas are summarized)

## Results

No experiments: the paper is purely theoretical. Its stated consequence is that failures of feedforward networks "can be attributed to inadequate learning, inadequate numbers of hidden units, or the presence of a stochastic rather than a deterministic relation between input and target" (p. 2).

## Limitations

Stated by the authors (pp. 2, 5-6):
- The theorems "do not address the issue of how many units are needed" for a given accuracy, nor how that number scales with the input dimension $r$; both are listed as open "degree of approximation" and "scaling up" questions.
- Learning (consistent estimation of the weights) is separate; the authors point to the method of sieves and metric entropy as the route (White 1988b, cited not read here).

Wiki note: existence only. It says nothing about whether gradient descent finds the approximating weights, or about generalization.

## Connections

- Cited by [[NTK (Jacot 2018)]] as the classical guarantee that wide networks can approximate any function, contrasted with the open question of what training converges to (Jacot p. 1, refs 7 and 10). Jacot also expects the limiting NTK to be positive definite because last-layer features should be dense in function space by theorems of this kind (p. 6).
- The operator version (Chen and Chen 1995) is [[Universal approximation for operators]], which [[DeepONet (Lu 2021)]] builds on; its "classical universal approximation theorem" for feedforward networks is presumably this family of results **[unverified]**.
- Width-to-infinity viewpoint on random networks: [[Wide networks as GPs (Matthews 2018)]] (Gaussian process limit rather than approximation).

%% refs:start %%
**Cited by in this wiki**: [[Deep Koopman (Lusch 2018)]], [[DeepONet (Lu 2021)]], [[FNO (Li 2021)]], [[NIF (Pan 2023)]], [[NTK (Jacot 2018)]], [[Neural operator (Kovachki 2022)]], [[Operator learning review (Kovachki 2024)]], [[PINNs (Raissi 2019)]], [[SINDy autoencoders (Champion 2019)]], [[Spectral bias (Rahaman 2019)]]
%% refs:end %%

**Sources**: `papers/ML/Hornik, Stinchcombe, White - Multilayer Feedforward Networks are Universal Approximators.pdf`.
**Last updated**: 2026-11-07

---

## Related pages
- [[Universal approximation theorem]] · [[Universal approximation for operators]] · [[DeepONet (Lu 2021)]]
- [[NTK (Jacot 2018)]] · [[Neural tangent kernel]] · [[Spectral bias]]
