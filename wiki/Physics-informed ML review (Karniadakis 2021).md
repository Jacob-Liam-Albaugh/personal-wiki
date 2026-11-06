---
type: paper
area: physics-informed
areas: [physics-informed, pde, uq]
source-ref: "Karniadakis, Kevrekidis, Lu, Perdikaris, Wang, Yang 2021, Nature Reviews Physics 3:422-440 [unverified pages]"
tags: [physics-informed, pde, ml, uq]
authors: ["[[George Em Karniadakis]]", "[[Ioannis G. Kevrekidis]]", "[[Lu Lu]]", "[[Paris Perdikaris]]", "[[Sifan Wang]]", "[[Liu Yang]]"]
year: 2021
venue: "Nature Reviews Physics"
file: "Physics Informed Architectures/Karniadakis, Lu, Kevrekidis, Perdikaris - Physics-Informed Machine Learning.pdf"
---

# Physics-informed machine learning review (Karniadakis 2021)

**Summary**: Review of how to build physical knowledge into learning, organized by three kinds of bias (observational, inductive, learning), with [[PINN]]s as the main example of a learning bias. Covers connections to kernels and classical numerics, strengths and limits, uncertainty, applications, software and an outlook (source: review.pdf, abstract, p. 2). The concept hub is [[Physics-informed machine learning]].

**Authors**: George Em Karniadakis, Ioannis G. Kevrekidis, Lu Lu, Paris Perdikaris, Sifan Wang, Liu Yang · Page numbers below are PDF pages (page 1 is a ResearchGate cover sheet).

---

## Motivation and data regimes (p. 2-3, Box 1)

Data are abundant while assimilation is not; purely data-driven models can be physically implausible. Physics-informed learning is "the process by which prior knowledge ... can be leveraged to improve the performance of a learning algorithm" (p. 3). Box 1 distinguishes three regimes: small data with all physics known (classical PDE solve), the common middle regime with partial physics plus scattered data (inferring parameters or missing terms), and big data with unknown physics (operator regression to discover it).

## Three routes to physical bias (p. 3-4, Box 2)

| Bias | Mechanism | Strength | Limit |
|---|---|---|---|
| Observational | data that embody the physics, augmentation | simplest | needs lots of data for over-parameterized nets |
| Inductive | architectures that satisfy constraints exactly | strict satisfaction | only simple, known symmetry groups; hard to scale |
| Learning | loss terms and constraints (soft penalties) | flexible: integral, differential, fractional laws | only approximate satisfaction |

They can be combined (Box 2, p. 4).

**Inductive examples (pp. 4-5):** CNNs, [[Graph neural network]]s, [[Equivariance]] networks, [[Kernel methods]] and [[Gaussian process]]es; anti-symmetric nets via determinants; Galilean-invariant tensor bases for turbulence; symplectic networks for Hamiltonian systems (see [[Hamiltonian neural network]]); hard-coded initial, Dirichlet, Neumann, Robin, periodic and interface conditions; a Lax-Oleinik two-layer net whose output is a viscosity solution of a Hamilton-Jacobi PDE (eqs. 1-2).

**Learning-bias example, the PINN (Box 3, p. 5):** a network $u(x,t)$ and a residual network share parameters, with loss
$$L=w_{data}L_{data}+w_{PDE}L_{PDE}.$$
The example is viscous Burgers ([[Burgers equation]]). The weights matter for trainability and may be set automatically; optimizers named are [[Adam]] and L-BFGS; the recommended library is DeepXDE. Other soft-constraint uses: statistically constrained GANs, Lyapunov-stable autoencoders, InvNet (p. 6-7).

**Link to Bayes:** a soft-penalty solution is equivalent to a MAP estimate under a physics-based likelihood; full treatment by MCMC or [[VAE]]-style variational inference gives uncertainty (p. 7). This is the reading used by [[Physics-informed prior]] and [[PIFT (Alberts 2023)]].

## Hybrids and connections (pp. 7-8)

- Non-dimensional numbers (Reynolds, Froude, Mach) as physics bias; PINN-trained [[DeepONet]] for real-time prediction; multi-fidelity learning and data augmentation from cheap models; networks embedded in finite-element codes.
- **Kernel view:** PINN training dynamics are kernel regression as width goes to infinity ([[Neural tangent kernel]]); PINNs can be seen as solving PDEs in an [[RKHS]] whose feature map is learned.
- **Classical numerics:** CNNs resemble finite-difference stencils and multigrid; ResNets resemble forward Euler (see [[ResNet]], [[Neural ODE]]); RK4 resembles recurrent nets; ReLU networks equal piecewise-linear finite elements. The discrete-time PINN uses an implicit Runge-Kutta integrator with up to 500 stages ([[PINNs (Raissi 2019)]]).

## Merits and limits (p. 8)

- PINNs excel at ill-posed and inverse problems and incomplete models, are mesh-free, and generalize from small data by restricting to a lower-dimensional manifold.
- For well-posed forward problems without data assimilation, grid-based solvers currently outperform PINNs.
- Domain decomposition lets subdomain networks sit on different GPUs.

## Uncertainty, dimensionality and applications (pp. 9-13)

- Three uncertainty sources: the physics (stochastic PDEs), the data (aleatoric vs epistemic, handled by Bayesian methods; B-PINNs give bounds of the same order as the error, priors are open), and the learner (hard to quantify) (p. 9).
- High dimension: DNNs help when targets are hierarchical compositions; backward-SDE methods for high-dimensional parabolic PDEs; GANs; DeepONets (p. 8-9).
- Applications: 3D velocity and pressure from Schlieren temperature video (espresso cup), 4D-flow MRI denoising, edge plasma in fusion devices, seismic inversion, and more (pp. 9-12).
- Software: DeepXDE, SimNet, PyDEns, NeuroDiffEq, NeuralPDE (Julia), SciANN, ADCME (Julia); GPyTorch and Neural Tangents for kernel analyses (pp. 12-13).

## Outlook (pp. 16-17)

Digital twins; transformations between models (nonlinear dynamics to Koopman, Poisson to Hamiltonian, Nesterov to ODE); discovering intrinsic variables with manifold learning, autoencoders and [[SINDy]]-style dictionaries; active learning; and a changing meaning of "understanding". Open needs: standardized benchmarks and new mathematics.

%% refs:start %%
**Cited by in this wiki**: [[IFT thermal conductivity (Alberts 2026)]], [[NIF (Pan 2023)]], [[Respecting causality (Wang 2022)]]
%% refs:end %%

**Sources**: `Physics Informed Architectures/Karniadakis, Lu, Kevrekidis, Perdikaris - Physics-Informed Machine Learning.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Physics-informed machine learning]] · [[PINN]] · [[PINNs (Raissi 2019)]] · [[Neural tangent kernel]] · [[Operator learning]]
- [[Neural ODE]] · [[SINDy]] · [[Hamiltonian neural network]] · [[Lagrangian neural network]] · [[Equivariance]]
