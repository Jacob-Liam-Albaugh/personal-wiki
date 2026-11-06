---
type: method
area: physics-informed
areas: [physics-informed, operators, ml]
source-ref: "Pan, Brunton, Kutz 2023, §2"
tags: [physics-informed, operators, ml, pde]
---

# Neural implicit flow

> [!definition] Neural implicit flow (NIF)
> A hypernetwork for fields $u(x;t,\mu)$. A spatial MLP (ShapeNet) takes only $x$. Its weights and biases are the output of a second MLP (ParameterNet) of $(t,\mu)$ or sensor readings:
> $$u(x;t,\mu)=u_{\mathrm{MLP}}\big(x;\,W(t,\mu;\Theta),\,B(t,\mu;\Theta)\big).$$
> The bottleneck width $r$ of ParameterNet is the latent dimension.
>
> (source: NIF.pdf, eq. 2, p. 8)

**Intuition**: a trained coordinate-MLP is an implicit (mesh-free) description of one snapshot. Letting a second network emit that MLP's weights makes each snapshot a point in a low-dimensional latent space, so the representation compresses like an autoencoder but is evaluated at any location on any mesh.

## Key properties
- **Mesh-agnostic**: training uses scattered samples $(x_i,t_i,\mu_i,u_i)$ with a plain least-squares loss (eq. 4); no projection to a uniform grid.
- **Spatial complexity isolated**: queries over many points $x$ reuse one ShapeNet evaluation per snapshot; time and parameters enter only through the weights.
- **Contains other architectures**: with only the last ShapeNet layer produced by ParameterNet it reduces to a [[DeepONet]]-style basis expansion $\sum_i a_i(t)\varphi_i(x)$, a mesh-free analogue of [[Proper orthogonal decomposition]] (eq. 6).
- **Needs a multi-scale ShapeNet**: [[SIREN]]-type sine activations counter [[Spectral bias]] (compare [[Fourier features]]).

## Variants used in the paper
Data-fit parametric surrogate (input $t,\mu$); compressed representation (input $t$); linear subspace for [[Dynamic mode decomposition]] on adaptive meshes; sparse reconstruction from sensors (input: sensor values).

## Failure modes
Hand-tuned sizes, long training, wide output layer (see [[NIF (Pan 2023)]], §4.1).

## Where it appears
- [[NIF (Pan 2023)]]; contrast with [[Neural operator]] / [[Operator learning]] which learn solution operators between function spaces, and [[Surrogate model]] more generally.

**Sources**: `papers/Physics Informed Architectures/Brunton, Pan, Kutz - NIF - Neural Implicit Flow.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[NIF (Pan 2023)]] · [[DeepONet]] · [[Operator learning]] · [[Neural operator]] · [[SIREN]]
- [[Surrogate model]] · [[Physics-informed machine learning]] · [[PINN]]
- [[SIREN]] (implicit neural representations).
