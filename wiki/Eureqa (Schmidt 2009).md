---
type: paper
area: ml
areas: [ml, physics-informed, mechanics]
source-ref: "Schmidt, Lipson 2009, Science 324, pp. 81-85"
tags: [ml, physics-informed, mechanics, optimization]
authors: ["[[Michael Schmidt]]", "[[Hod Lipson]]"]
year: 2009
venue: "Science 324(5923)"
file: "papers/ML/Schmidt, Lipson - Distilling Free-Form Natural Laws from Experimental Data.pdf"
---

# Eureqa (Schmidt 2009)

**Summary**: Uses evolutionary [[Symbolic regression]] to find conservation laws and equations of motion from motion-tracking data of physical systems, with no physics prior. The key idea is a fitness criterion, partial-derivative pairs, that rejects trivially invariant expressions. Recovers Hamiltonians, Lagrangians and momentum laws for oscillators and a chaotic double pendulum, and reports a Pareto front of accuracy against complexity.

**Authors**: Michael Schmidt, Hod Lipson · **Year**: 2009 · **File**: `papers/ML/Schmidt, Lipson - Distilling Free-Form Natural Laws from Experimental Data.pdf`

(The paper does not name its software; the wiki and [[Symbolic models from deep learning (Cranmer 2020)]] call the tool Eureqa.)

---

## Problem

Many natural laws are conserved quantities or invariants. Searching for them is hard because infinitely many expressions are numerically invariant but meaningless, e.g. $\sin^2x_1+\cos^2x_1$ or $4.56+1/(100+x_1^2)$ (source: Schmidt 2009, p. 1). Ordinary symbolic regression fits a target signal, so it cannot readily find an invariant or Lagrangian, which "may or may not be constant" (p. 1). Need a principle for non-triviality.

## Method

> [!definition] Partial-derivative-pairs criterion
> A candidate law $f(x,y)$ is non-trivial if it predicts relations among the time derivatives of the variables. From data, the estimated ratio is $\dot x/\dot y\approx\Delta x/\Delta y$. From a candidate, the same ratio follows by differentiation: $\dfrac{\partial f/\partial y}{\partial f/\partial x}\approx\dfrac{dx}{dy}$ (and the reciprocal $\dfrac{\partial f/\partial x}{\partial f/\partial y}\approx\dfrac{dy}{dx}$). Fitness is agreement between the data ratios and the symbolic ratios. Higher-dimensional systems use many variable pairings and higher-order derivatives (SOM S2-S3).
>
> (source: Schmidt 2009, p. 2)

Consequences: the criterion also accepts manifolds and Lagrangians (which summarize dynamics but are not invariant), not only conserved quantities (p. 2). The variables supplied steer the law type: positions give a manifold equation, adding velocities biases to energy laws, adding accelerations biases to force and equation-of-motion laws (p. 2).

> [!algorithm] Search
> Evolutionary symbolic regression: expressions are stored as lists of operations (a graph of operators, constants and state variables), recombined and mutated; candidates that fit better are retained (Fig. 2, p. 2). Building blocks: $\{+,-,\div,\times\}$, sine, cosine, constants, variables. The output is a short list (about 10) of equations on the accuracy-parsimony **Pareto front**: parsimony is the inverse of number of terms, accuracy is error on withheld data under the derivative-pairs criterion. A human then selects the final equation (p. 2, p. 4).

Pareto front shape: a "cliff" where predictive ability jumps at some minimal complexity, then improves marginally. The equation at the cliff was an exact theoretical law in every experiment (p. 4).

**Bootstrapping**: seed the initial population with terms from laws of simpler systems (shuffled variables, randomized constants). This cut the double-pendulum search from 30-40 h to 7-8 h and suggests an "emergent alphabet" of useful sub-expressions such as squared velocities (kinetic energy) and trig terms (potential energy) (p. 4).

## Results

- Systems: air-track oscillator (one and two masses), pendulum, double pendulum, tracked by video; velocities and accelerations by numerical differentiation (p. 2).
- Given positions and velocities it found the energy laws (Hamiltonian, Lagrangian); with accelerations, Newton's second law for the oscillator and pendulum; with positions only, the circle the pendulum lives on (p. 3).
- Without sine/cosine operators it approximated the pendulum invariant as $\omega^2+k_1q^2-k_2q^4$, using a 4th-order cosine Taylor series (p. 3).
- Data from only chaotic (high-energy) double-pendulum runs made it fixate on approximate conservation of angular momentum; combining chaotic and low-energy data gave the exact energy law after several hours (p. 3).
- Time to converge is exponential in law complexity (worst case) and roughly quadratic in the number of variable pairings; 32 cores: minutes for the harmonic oscillator, about 30 h for the double pendulum (p. 4).
- Re-running the search across data sets with different masses and lengths found formulas for the fitted constants (e.g. $19.6=2g$ as the only absolute constant) (p. 4).

## Limitations

As stated: meaning and units of discovered constants remain ambiguous; the law may involve unobservable quantities such as total energy; cost grows rapidly with complexity, dimension and noise; a human must interpret and select among Pareto equations (p. 4).

Wiki note: the later [[SINDy (Brunton 2016)]] paper cites this work as the symbolic-regression baseline and trades free-form search for a fixed library plus sparse regression, gaining scale at the cost of expressiveness. [[HNNs (Greydanus 2019)]] cite it as inspiration for learning conserved quantities.

## Connections

- Origin of the Eureqa-style genetic [[Symbolic regression]] used as engine in [[Symbolic models from deep learning (Cranmer 2020)]]; open-source successor [[PySR (Cranmer 2023)]].
- Discovered Hamiltonians and Lagrangians are what [[Hamiltonian neural network]] and [[Lagrangian neural network]] learn with a neural parameterization instead.
- Competing dictionary-based approach: [[SINDy]].

%% refs:start %%
**Cited by in this wiki**: [[Deep Koopman (Lusch 2018)]], [[HNNs (Greydanus 2019)]], [[PySR (Cranmer 2023)]], [[SINDy autoencoders (Champion 2019)]], [[SINDy delay autoencoders (Bakarji 2022)]], [[Symbolic models from deep learning (Cranmer 2020)]]
%% refs:end %%

**Sources**: `papers/ML/Schmidt, Lipson - Distilling Free-Form Natural Laws from Experimental Data.pdf`.
**Last updated**: 2026-11-07

---

## Related pages
- [[Symbolic regression]] · [[SINDy]] · [[SINDy (Brunton 2016)]]
- [[PySR (Cranmer 2023)]] · [[Symbolic models from deep learning (Cranmer 2020)]]
- [[Hamiltonian neural network]] · [[Lagrangian neural network]] · [[HNNs (Greydanus 2019)]]
