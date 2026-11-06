---
type: paper
area: ml
areas: [ml]
source-ref: "Cranmer 2023, arXiv:2305.01582v3, §2.1, Alg. 1-4, §3.2"
tags: [ml, optimization]
authors: ["[[Miles Cranmer]]"]
year: 2023
venue: "arXiv:2305.01582v3 (astro-ph.IM)"
file: "ML/Cranmer - PySR.pdf"
---

# PySR (Cranmer 2023)

**Summary**: Describes PySR and its Julia backend SymbolicRegression.jl, an open-source symbolic regression library built on a multi-population evolutionary search with an evolve-simplify-optimize loop. It also introduces EmpiricalBench, nine historical empirical laws used to test whether a method can rediscover them from noisy original data. PySR recovered 7 of 9 laws in all 5 trials.

**Authors**: Miles Cranmer · **Year**: 2023 (arXiv v3, 5 May 2023) · **File**: `ML/Cranmer - PySR.pdf`

---

## Problem

[[Symbolic regression]] searches the space of analytic expressions for a model that balances accuracy and simplicity. Science needs more than synthetic-benchmark SR. The paper lists nine requirements (p. 2-3): unknown real constants (so the search space is uncountably infinite), insight through simplicity, noisy and heteroscedastic data, non-differentiable piecewise forms, known constraints, field-specific operators, high-dimensional inputs, non-tabular data, and an open, easy-to-use package.

## Method

PySR is a multi-population evolutionary algorithm run asynchronously on "islands" of expressions (§2.1, Fig. 3-4).

> [!algorithm] Inner loop (tournament evolution)
> 1. Draw a random subset of $n_s$ expressions (default $n_s=12$).
> 2. Pick the fittest with probability $p_{\text{tournament}}=0.9$, else drop it and repeat.
> 3. Copy the winner and apply a random mutation or (with probability $p_{\text{cross}}=0.01$) a crossover.
> 4. Replace the *oldest* member of the population, not the weakest (age-regularized evolution).
> (source: PySR, §2.1, Alg. 2 and 4)

Three changes to the classic scheme (§2.1):

1. **Simulated annealing** on the mutation step. A mutation is accepted with probability tied to the fitness change, with a temperature $T=1-n/n_c$ falling over the evolve call, so the search alternates diversity and refinement.
2. **Evolve-simplify-optimize loop.** After many mutations (default $n_c=300000$ per call) each expression is algebraically simplified and its constants tuned by a few BFGS iterations. Simplifying only occasionally keeps redundant intermediates such as $x*x-x*x$ reachable, which a mutation may turn into $x*x-x*y$.
3. **Adaptive parsimony.** Instead of a constant penalty $\ell_{\text{pred}}+\text{parsimony}\cdot C(E)$, fitness is rescaled by how crowded each complexity is:
$$\ell(E)=\ell_{\text{pred}}(E)\,\exp\big(\text{frecency}[C(E)]\big)$$
   "Frecency" counts how often and how recently expressions of complexity $C$ appeared in the population. Complexity defaults to the node count and is user-configurable.

Outer loop (Alg. 1): 40 populations of 1000 expressions each; each iteration evolves them in parallel, then migrates: with probability $0.05$ an expression is replaced from the global hall of fame $H$, and with probability $0.05$ from another island's best. The output is the most accurate expression at each complexity, i.e. a Pareto front.

Mutation types (Alg. 3): perturb a constant, swap an operator, add or insert a node, delete a subtree, simplify, new random tree, or no change.

### Features (§2.1-2.5)

- Denoising by a Gaussian process (Gaussian kernel + white noise + constant) before search, per-point weights, and arbitrary custom losses and likelihoods, since MSE is only a Gaussian likelihood with equal variances (§2.5).
- Custom operators: any scalar $\mathbb R\to\mathbb R$ or $\mathbb R^2\to\mathbb R$ function, compiled in Julia, including discontinuous ones such as a broken power law (§2.4).
- Hard constraints: size, depth, per-operator argument size and operator nesting.
- Feature selection by gradient-boosted trees for high-dimensional data.
- Export to SymPy, NumPy, PyTorch (constants as trainable parameters) and JAX (§2.3), so a found expression can be refit or used in a larger model. See [[Symbolic models from deep learning (Cranmer 2020)]] for the distillation use.
- Backend: JIT-compiled Julia; operators are fused into SIMD kernels to depth two (§2.2).

## Results

EmpiricalBench (§3.2, Table 2): Hubble, Kepler, Newton gravitation, Planck, Leavitt, Schechter, Bode, ideal gas, Rydberg. Original data are used where available. Physical constants are not given to the algorithm. Each of six methods got 8 cores and 1 hour, 5 trials per law, and the whole Pareto front was inspected by eye (p. 14-17).

- PySR found the true law in 5/5 trials on 7 laws (Hubble, Kepler, Newton, Leavitt, Schechter, Bode, ideal gas) and 0/5 on Planck and Rydberg (Table 3).
- Operon, DSR, EQL, QLattice and SR-Transformer did worse overall. The two pure deep-learning methods, EQL and SR-Transformer, recovered the fewest laws (§3.3).
- The paper notes a bias: the author wrote PySR and so ran it in a stable setting (p. 17).

## Limitations

- Evolutionary search is evaluation-hungry; the benchmark does not measure number of evaluations (p. 17).
- The benchmark has nine laws and manual judging **[Wiki note: small sample]**.
- Planck and Rydberg were not recovered by any method.

## Connections

- [[Symbolic regression]] hub page.
- Complements [[SINDy]], which fits a sparse linear combination of a fixed dictionary; PySR searches free-form trees (§1).
- GP denoising uses a [[Gaussian process]] with a Gaussian kernel.
- Part of the physics-discovery line with [[Physics-informed machine learning]].





%% refs:start %%
**Cites in this wiki**: [[SINDy autoencoders (Champion 2019)]], [[Symbolic models from deep learning (Cranmer 2020)]]
%% refs:end %%

**Sources**: `ML/Cranmer - PySR.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Symbolic regression]]
- [[Symbolic models from deep learning (Cranmer 2020)]]
- [[SINDy]]
- [[Gaussian process]]
- [[Physics-informed machine learning]]
