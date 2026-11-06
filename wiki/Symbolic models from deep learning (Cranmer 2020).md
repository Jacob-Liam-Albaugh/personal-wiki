---
type: paper
area: ml
areas: [ml]
source-ref: "Cranmer et al. 2020, NeurIPS, §2-4"
tags: [ml, physics-informed, mechanics]
authors: ["[[Miles Cranmer]]", "[[Alvaro Sanchez-Gonzalez]]", "[[Peter Battaglia]]", "[[Kyle Cranmer]]", "[[David Spergel]]", "[[Shirley Ho]]"]
year: 2020
venue: "NeurIPS 2020"
file: "ML/Cranmer, Gonzalez, Ho - Discovering Symbolic Models from DL with Inductive Biases.pdf"
---

# Symbolic models from deep learning (Cranmer 2020)

**Summary**: Trains a Graph Network with a sparse (compact) latent message space, then fits [[Symbolic regression]] separately to its internal functions (edge, node, global). This extends symbolic regression to high-dimensional data and recovers known force laws and Hamiltonians. On a dark matter simulation it finds a new formula for halo overdensity that beats a hand-designed one and generalizes out of distribution better than the network it came from.

**Authors**: Miles Cranmer, Alvaro Sanchez-Gonzalez, Peter Battaglia, Kyle Cranmer, David Spergel, Shirley Ho · **Year**: 2020 · **File**: `ML/Cranmer, Gonzalez, Ho - Discovering Symbolic Models from DL with Inductive Biases.pdf`

---

## Problem

Symbolic models are compact and generalize well, but genetic-algorithm search scales exponentially with the number of variables and operators. Deep nets handle high-dimensional data but are black boxes and extrapolate linearly (ReLU) (p. 1-2).

## Method

Four steps (p. 2):

1. Pick a model with separable internal structure matching the data's inductive bias (here a [[Graph neural network]]).
2. Train end to end.
3. Fit symbolic expressions to each learned internal function.
4. Replace those functions by the expressions; refit the constants to the data once more to avoid accumulated error.

> [!definition] Graph Network components
> Edge model $\phi^e$ maps a node pair (plus edge data) to a message. Messages are summed per receiving node. Node model $\phi^v$ takes the node and the summed message and returns an update. Global model $\phi^u$ aggregates everything into a global property. Each is an MLP (source: Cranmer 2020, p. 3).

The sum over messages makes the model permutation equivariant, which is the inductive bias physics wants (see [[Equivariance]]).

### Why factorizing helps

If the truth is $z=f\big(\sum_j g(x_j)\big)$ and each of $f,g$ needs $10^9$ candidate equations, joint search needs $(10^9)^2=10^{18}$ but separate search after training only $2\times10^9$ (p. 4).

### Compact latents

Regularize the messages (an $L_1$ penalty with weight $10^{-2}$, or a KL penalty to a Gaussian prior, or a bottleneck of the true spatial dimension). If a law exists in a linear latent space of dimension $D$, a trained GN with $D$ message components learns a rotation of the true vectors (p. 4, with the argument in the appendix).

### Hamiltonian variant

"FlatHGN": the global energy is a sum of scalar pairwise terms $H_{\text{pair}}$ and per-particle terms $H_{\text{self}}$. The dynamics follow from derivatives of $H$ with respect to $q$ and $p$ (p. 5). This combines a Hamiltonian neural network with a GN; see [[Hamiltonian neural network]].

## Results

- Newtonian N-body with six force laws (1/r, 1/r², charged, damped spring, discontinuous, spring), 4 or 8 particles in 2D and 3D. $L_1$-regularized GN has the best prediction in most cases (p. 6).
- Standard GN (100 message components) gives messages weakly correlated with the true force. Bottleneck, KL and $L_1$ models give messages that are linear combinations of the true force components; $L_1$ best (Table 1, p. 7).
- Eureqa recovers forms such as the spring force and the `IF(r > 2, ...)` discontinuous law from the top message component. Selection rule: maximize $-\Delta\log(\text{MAE})/\Delta c$ over complexity $c$ (p. 7).
- Hamiltonian case: charged-particle pair energy recovered as a multiple of $q_1q_2/r$ (p. 8).
- Cosmology: 215,854 halos, 30,437,218 edges (halos within 50 units, about 71 neighbors each). The found formula gets loss $0.0882$ against $0.121$ for the hand-designed formula (p. 8).
- Generalization: with halos of $\delta>1$ masked in training, the GN error is $0.0634$ train and $0.142$ out of distribution; the symbolic formula is $0.0811$ and $0.0892$ (p. 9).

## Limitations

- Reconstruction fails for training strategies that do not find a compact latent of the right dimension (p. 7).
- Symbolic regression here is Eureqa (closed source); the authors name [[PySR (Cranmer 2023)]] as a drop-in replacement (p. 4).
- The better generalization is shown on one dataset; the paper calls for follow-up study (p. 10).

## Connections

- Hub: [[Symbolic regression]]; software: [[PySR (Cranmer 2023)]].
- Message passing: [[Graph neural network]] and [[Variational graph auto-encoder (Kipf 2016)]].
- Hamiltonian structure: [[Hamiltonian neural network]], [[Lagrangian neural network]].
- A different route to interpretable dynamics is [[SINDy]].

%% refs:start %%
**Cites in this wiki**: [[Adam paper (Kingma 2015)]], [[HNNs (Greydanus 2019)]], [[LNNs (Cranmer 2020)]]
**Cited by in this wiki**: [[LNNs (Cranmer 2020)]], [[PySR (Cranmer 2023)]]
%% refs:end %%

**Sources**: `ML/Cranmer, Gonzalez, Ho - Discovering Symbolic Models from DL with Inductive Biases.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Symbolic regression]]
- [[PySR (Cranmer 2023)]]
- [[Graph neural network]]
- [[Hamiltonian neural network]]
- [[Lagrangian neural network]]
- [[SINDy]]
- [[Equivariance]]
- [[Physics-informed machine learning]]
