---
type: paper
area: physics-informed
areas: [physics-informed, ml, mechanics]
source-ref: "Lusch, Kutz, Brunton 2018, Nat. Commun. 9:4950, eqs. 1-4, 11-15"
tags: [physics-informed, ml, mechanics]
authors: ["[[Bethany Lusch]]", "[[J. Nathan Kutz]]", "[[Steven L. Brunton]]"]
year: 2018
venue: "Nature Communications 9:4950"
file: "papers/Physics Informed Architectures/Lusch, Kutz, Brunton - Deep learning for universal linear embeddings of nonlinear dynamics.pdf"
---

# Deep Koopman (Lusch 2018)

**Summary**: A modified autoencoder learns coordinates $y=\varphi(x)$ in which nonlinear dynamics advance by a linear map $K$, approximating Koopman eigenfunctions. An auxiliary network makes the eigenvalues depend on the state, so systems with a continuous spectrum (e.g. the pendulum) need only one conjugate pair of eigenfunctions instead of a long harmonic series.

**Authors**: Bethany Lusch, J. Nathan Kutz, Steven L. Brunton · **Year**: 2018 · **File**: `papers/Physics Informed Architectures/Lusch, Kutz, Brunton - Deep learning for universal linear embeddings of nonlinear dynamics.pdf`

---

## Problem

Linear systems have a universal solution by eigen-decomposition, nonlinear ones do not. The [[Koopman operator]] gives a linear but infinite-dimensional description, and its eigenfunctions are intrinsic linearizing coordinates, but they are hard to find and often intractably complex. [[Dynamic mode decomposition]] uses $g(x)=x$ and misses nonlinear transients; extended DMD adds nonlinear observables but faces closure problems because there is no guarantee they span an invariant subspace (source: Lusch 2018, p. 3). Systems with continuous spectra make a finite approximation impossible with fixed eigenvalues.

Setting: discrete-time $x_{k+1}=F(x_k)$ (eq. 1), $x\in\mathbb R^n$.

## Method

> [!definition] Koopman operator and eigenfunctions
> $\mathcal K g=g\circ F$, so $\mathcal K g(x_k)=g(x_{k+1})$ (eq. 2). Eigenfunctions satisfy $\varphi(x_{k+1})=\mathcal K\varphi(x_k)=\lambda\varphi(x_k)$ (eq. 3) and span an invariant subspace on which $\mathcal K$ is a matrix.
>
> (source: Lusch 2018, pp. 3, eqs. 2-3)

Network: encoder $\varphi:\mathbb R^n\to\mathbb R^p$, decoder $\varphi^{-1}$, and a linear matrix $K$ on the $p$-dimensional latent space, $y_{k+1}=Ky_k$ (Figs. 1-2). Three losses:

> [!algorithm] Training losses (Methods, eqs. 11-15)
> $$\mathcal L=\alpha_1(\mathcal L_{\rm recon}+\mathcal L_{\rm pred})+\mathcal L_{\rm lin}+\alpha_2\mathcal L_\infty+\alpha_3\|W\|_2^2$$
> - Reconstruction: $\|x_1-\varphi^{-1}(\varphi(x_1))\|$.
> - Prediction: $\frac1{S_p}\sum_{m=1}^{S_p}\|x_{m+1}-\varphi^{-1}(K^m\varphi(x_1))\|$.
> - Linearity: $\frac1{T-1}\sum_{m=1}^{T-1}\|\varphi(x_{m+1})-K^m\varphi(x_1)\|$.
> - $\mathcal L_\infty$ penalizes the largest-error point (no outliers in the data); all norms are mean-squared error; $\ell_2$ on weights.
>
> Multi-step terms ($K^m$) are used in training. Hidden layers are ReLU, output layers linear, Adam optimizer, TensorFlow (Methods).
>
> (source: Lusch 2018, p. 4 and Methods)

**Continuous spectrum.** An auxiliary network $\lambda=\Lambda(y)$ lets eigenvalues vary over phase space. For a conjugate pair $\lambda_\pm=\mu\pm i\omega$ the block of $K(\mu,\omega)$ is
$$B(\mu,\omega)=e^{\mu\Delta t}\begin{pmatrix}\cos\omega\Delta t&-\sin\omega\Delta t\\ \sin\omega\Delta t&\cos\omega\Delta t\end{pmatrix}\quad(4)$$
(p. 4; checked against the page image). The eigenvalues are parameterized by the radius $\|y\|_2^2$ to impose circular symmetry; an unconstrained version "did not converge to a unique and interpretable solution" (p. 5). Real eigenvalues use a separate map from $y_j$ to $\lambda$ (Methods). The authors conjecture that earlier high-dimensional deep Koopman models were approximating the harmonic series of the frequency shift (p. 4).

## Results

Table 1 (relative MSE, train/val/test about equal): discrete spectrum $\sim1.4\times10^{-7}$, pendulum $\sim10^{-7}$, fluid flow $5.4\times10^{-7}$ (slow manifold) and $2.9\times10^{-6}$ (off-manifold) (p. 5).

- **Discrete spectrum**, $\dot x_1=\mu x_1$, $\dot x_2=\lambda(x_2-x_1^2)$, $\mu=-0.05,\lambda=-1$: network flattens the slow manifold $x_2=x_1^2$ and recovers the true eigenvalues, even with the auxiliary net left free (p. 5).
- **Pendulum** $\ddot x=\sin x$: one conjugate eigenfunction pair, orbits become concentric circles in $y$, frequency drops with energy; magnitude traces Hamiltonian level sets, consistent with action-angle Koopman eigenfunctions of Mezic (Figs. 4-5). Prediction horizon (10% error) shrinks as energy grows (p. 5).
- **Cylinder wake mean-field model** (Re 100, $\mu=0.1,\omega=1,A=-0.1,\lambda=10$): frequency learned as nearly constant, damping $\mu(R)$ varies with radius and changes sign outside the limit cycle, matching Loiseau-Brunton. Trajectories starting off the attractor are reconstructed, provided transients appear in training data (p. 6).
- Data: 5000 test and 5000 validation initial conditions, 5000-20,000 training, ODEs solved with MATLAB `ode45` (Methods).

## Limitations

As stated: needs large, diverse data and heavy training; deep nets are interpolation engines with limited extrapolation; the latent dimension $p$ is a hyperparameter and its automatic choice (and detecting continuous vs discrete spectra) is open; examples are low-dimensional (pp. 6-7).

Wiki note: the model is deterministic with no uncertainty on $K$ or $\varphi$. Unlike [[SINDy autoencoders (Champion 2019)]], latent dynamics are linear rather than a sparse nonlinear library.

## Connections

- Replaces the fixed observables of [[Dynamic mode decomposition]] / extended DMD with a learned dictionary.
- Sibling of [[SINDy autoencoders (Champion 2019)]] (same group, same autoencoder skeleton, sparse nonlinear vs linear latent dynamics); the linear-vs-sparse trade is the same coordinate question raised in [[SINDy (Brunton 2016)]] ("right coordinates and basis").
- Related to [[Neural ODE]] latent models; the loss uses discrete-time rollouts instead of an ODE solver.
- Mentions a generalized Noether link: conserved Koopman eigenfunctions correspond to conservation laws (p. 8).

%% refs:start %%
**Cites in this wiki**: [[Adam paper (Kingma 2015)]], [[AlexNet (Krizhevsky 2012)]], [[Eureqa (Schmidt 2009)]], [[SINDy (Brunton 2016)]], [[Universal approximation (Hornik 1989)]]
**Cited by in this wiki**: [[NIF (Pan 2023)]], [[PySR (Cranmer 2023)]], [[SINDy autoencoders (Champion 2019)]], [[SINDy delay autoencoders (Bakarji 2022)]]
%% refs:end %%

**Sources**: `papers/Physics Informed Architectures/Lusch, Kutz, Brunton - Deep learning for universal linear embeddings of nonlinear dynamics.pdf`.
**Last updated**: 2026-11-07

---

## Related pages
- [[Koopman operator]] · [[Dynamic mode decomposition]]
- [[SINDy autoencoders (Champion 2019)]] · [[SINDy (Brunton 2016)]] · [[SINDy]]
- [[Neural ODE]] · [[Physics-informed machine learning]] · [[VAE]]
