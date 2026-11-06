---
type: method
area: physics-informed
areas: [physics-informed, ml, generative]
source-ref: "Chen et al. 2018, eqs. 2-5; Greydanus 2019 eq. 1"
tags: [physics-informed, ml, optimization]
---

# Neural ODE

> [!definition] Neural ODE
> A model whose state evolves by an ODE with a learned right-hand side:
> $$\frac{dh(t)}{dt}=f_\theta(h(t),t).$$
> The output is $h(T)$ from a numerical solver; gradients come from the [[Adjoint sensitivity method]] or by differentiating through the solver.
>
> (source: Neural ODEs.pdf, eq. 2, p. 1)

**Intuition**: a residual block $h_{t+1}=h_t+f(h_t)$ is one Euler step. Take the number of layers to infinity with step size going to zero and you get the ODE. The solver, not the architect, then chooses how many "layers" (function evaluations) each input needs.

## Variants and uses
- **Continuous-depth classifier**: replaces residual blocks; MNIST error 0.42% at constant memory (source: [[Neural ODEs (Chen 2018)]], Table 1).
- **Continuous normalizing flow**: $\partial_t\log p(z(t))=-\operatorname{tr}(\partial f/\partial z)$, see [[Normalizing flows]].
- **Latent ODE**: encoder gives $z_{t_0}$, ODE gives the latent trajectory, decoder emits observations at arbitrary times; trained as a [[VAE]].
- **Structured right-hand sides**: the field $f$ is the gradient of a learned scalar, as in [[Hamiltonian neural network]] ($f=$ symplectic gradient of $H_\theta$) and [[Lagrangian neural network]] (accelerations from the Euler-Lagrange equation). [[SINDy]] fits the same $f$ as a sparse combination of library terms rather than a network.

## Failure modes
- Solver tolerance is a hyperparameter on both passes; reversing the dynamics can add error (checkpointing fixes it) (source: Neural ODEs.pdf, §6, p. 8).
- Uniqueness of solutions needs Lipschitz $f$ (Picard).
- Unstructured $f$ does not conserve anything; that is the motivation for HNN/LNN (source: [[HNNs (Greydanus 2019)]], Fig. 1).

## Where it appears
- [[Neural ODEs (Chen 2018)]] — origin.
- [[HNNs (Greydanus 2019)]], [[LNNs (Cranmer 2020)]] — integrate learned vector fields with Runge-Kutta.
- [[SINDy autoencoders (Champion 2019)]] — latent dynamics are a sparse ODE.
- ME 697 `inverse/data/04_nodes.ipynb` is a title-only stub "Neural ODEs"; [[ME697 4.7 - Data-driven modeling]].

**Sources**: `Physics Informed Architectures/Chen, Rubanova, Bettencourt, Duvenaud - Neural ODEs.pdf`, `Greydanus, Dzamba, Yosinski - HNNs.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Adjoint sensitivity method]] · [[Automatic differentiation]] · [[Normalizing flows]] · [[VAE]]
- [[Hamiltonian neural network]] · [[Lagrangian neural network]] · [[SINDy]] · [[Physics-informed machine learning]]
