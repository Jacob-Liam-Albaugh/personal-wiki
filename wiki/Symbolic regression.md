---
type: concept
area: ml
areas: [ml]
source-ref: "Cranmer 2023, §1; Cranmer et al. 2020, §1-2"
tags: [ml, optimization, physics-informed]
---

# Symbolic regression

**Summary**: Supervised learning where the model space is closed-form analytic expressions. It is usually posed as a multi-objective search that trades prediction error against expression complexity, and returns a Pareto front of candidate formulas.

**Sources**: `papers/ML/Schmidt, Lipson - Distilling Free-Form Natural Laws from Experimental Data.pdf`; `papers/ML/Cranmer - PySR.pdf`; `papers/ML/Cranmer, Gonzalez, Ho - Discovering Symbolic Models from DL with Inductive Biases.pdf`.
**Last updated**: 2026-11-06

---

## Definition

> [!definition] Symbolic regression
> Given data $\{(x_i,y_i)\}$, search over expression trees $E$ built from chosen operators, variables and real constants, to minimize prediction loss and complexity jointly. The output is the best expression at each complexity (source: PySR, §1, Alg. 1).

Why bother: the search space is discrete in structure but continuous in constants, so it is uncountably infinite. Scientific use needs equations that are simple and insightful, not just accurate (source: PySR, p. 2-3).

## Approaches in the sources

- **Eureqa**: the original physics-law demonstration is [[Eureqa (Schmidt 2009)]], which scores candidates by partial-derivative pairs and reports an accuracy-parsimony Pareto front.
- **Genetic search on trees** (Eureqa, PySR): tournament selection, mutation, crossover. [[PySR (Cranmer 2023)]] adds simulated annealing, an evolve-simplify-optimize loop with BFGS on constants, and adaptive parsimony.
- **Dictionary regression**: a sparse linear combination of fixed nonlinear terms, as in [[SINDy]] (PySR, §1).
- **Distillation from a neural net**: train a [[Graph neural network]] with a compact latent, then fit symbolic regression to each internal function. This makes high-dimensional problems tractable and is an add-on to any SR engine (source: Cranmer 2020, p. 4; see [[Symbolic models from deep learning (Cranmer 2020)]]).
- Pre-trained transformers and generative proposers are surveyed in PySR §1 but were weaker on the EmpiricalBench test (PySR, §3.3).

## Choosing an expression

Pick the model on the front where the log error drops most per unit complexity: maximize $-\Delta\log(\text{MAE})/\Delta c$ (source: Cranmer 2020, p. 7). PySR instead defaults to a balance of complexity and error (PySR, §2.2).

## Wiki note

Symbolic regression returns a deterministic formula with no posterior over structure. For a probabilistic treatment of model uncertainty see [[Gaussian process]] and [[Bayesian neural networks]].

## Related pages
- [[PySR (Cranmer 2023)]]
- [[Symbolic models from deep learning (Cranmer 2020)]]
- [[SINDy]] · [[SINDy (Brunton 2016)]]
- [[Eureqa (Schmidt 2009)]]
- [[Graph neural network]]
- [[Physics-informed machine learning]]
- [[Surrogate model]]
