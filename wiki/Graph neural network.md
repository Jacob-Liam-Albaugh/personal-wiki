---
type: concept
area: ml
areas: [ml]
source-ref: "Kipf & Welling 2016; Cranmer et al. 2020; Zaheer et al. 2017"
tags: [ml, symmetry]
---

# Graph neural network

**Summary**: A network whose layers pass messages along the edges of a graph and aggregate them with a permutation-invariant operation (usually a sum). Node and edge functions are shared across the whole graph, so the model works for any graph size and respects relabelling of nodes.

## Forms in the sources

- **Graph convolutional network (GCN)** (source: Kipf 2016, p. 1):
  $$\mathrm{GCN}(X,A) = \tilde A\,\mathrm{ReLU}(\tilde A X W_0)\,W_1$$
  with $\tilde A=D^{-1/2}AD^{-1/2}$. Each layer averages over neighbours then applies a shared linear map. Used as the encoder of [[Variational graph auto-encoder (Kipf 2016)]].
- **Graph network with $\phi^e,\phi^v,\phi^u$** (source: Cranmer 2020): edge function $\phi^e$ builds messages from node pairs, messages are summed at each node, and $\phi^v$ updates the node. The learned messages can be turned into formulas by [[Symbolic regression]]; see [[Symbolic models from deep learning (Cranmer 2020)]].
- **Set functions** as the edgeless case: sum over elements, $\rho(\sum_x\phi(x))$ ([[Deep Sets]]). Neighbour aggregation in a graph is a set function over the neighbours.

## Key points

- Permutation symmetry is built in: relabelling nodes permutes outputs ([[Equivariance]]).
- Sum aggregation matches pairwise-force structure in physics, which is why graph networks suit particle systems (Cranmer 2020).
- Wiki note: over-smoothing and scalability limits are known in the wider literature but are not covered in these sources. **[unverified]**

**Sources**: `papers/ML/Welling, Kipf - Variational Graph Auto-Encoders.pdf`; `papers/ML/Cranmer, Gonzalez, Ho - Discovering Symbolic Models from DL with Inductive Biases.pdf`; `papers/ML/Zaheer, Kottur, Ravanbhakhsh, Poczos, Salakhutdinov, Smola - Deep Sets.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Variational graph auto-encoder (Kipf 2016)]]
- [[Symbolic models from deep learning (Cranmer 2020)]]
- [[Deep Sets]]
- [[Deep Sets paper (Zaheer 2017)]]
- [[Equivariance]]
- [[Symbolic regression]]
- [[Hamiltonian neural network]]
