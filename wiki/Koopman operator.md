---
type: definition
area: physics-informed
areas: [physics-informed, ml, mechanics]
source-ref: "Lusch, Kutz, Brunton 2018, eqs. 2-4; Koopman 1931 cited, not read"
tags: [physics-informed, ml, mechanics]
---

# Koopman operator

> [!definition] Koopman operator
> For $x_{k+1}=F(x_k)$, the Koopman operator acts on measurement functions $g$ by composition:
> $$\mathcal K g=g\circ F,\qquad \mathcal K g(x_k)=g(x_{k+1}).$$
> It is linear but infinite-dimensional. An eigenfunction satisfies
> $$\varphi(x_{k+1})=\mathcal K\varphi(x_k)=\lambda\,\varphi(x_k).$$
>
> (source: [[Deep Koopman (Lusch 2018)]], eqs. 2-3, p. 3)

**Intuition**: instead of tracking the state, track functions of the state. Nonlinear dynamics on $x$ become linear dynamics on $g(x)$, at the price of an infinite-dimensional space. If you find a few eigenfunctions, $y=\varphi(x)$ evolves as $y_{k+1}=\lambda y_k$ and linear prediction, estimation and control tools apply.

## Finite-dimensional approximations
- [[Dynamic mode decomposition]]: observables $g(x)=x$ only; captures coherent structures but not nonlinear transients (source: Lusch 2018, p. 3).
- Extended DMD / variational approach of conformation dynamics: add nonlinear observables; the dictionary need not be Koopman-invariant, so models close badly or become huge (p. 3).
- Direct eigenfunction search: eigenfunctions span an invariant subspace and $\mathcal K$ restricted to it is a matrix. Deep nets learn them in [[Deep Koopman (Lusch 2018)]] (VAMPnets cited, not read).

## Continuous spectrum
Systems like the nonlinear pendulum shift frequency with energy, giving a continuous range of frequencies. A fixed finite eigenfunction set cannot represent this; a fixed-eigenvalue model needs a harmonic series $(2n-1)\omega$ (Jacobi elliptic expansion). Fix: let $\lambda=\Lambda(y)$ depend on the state, one conjugate pair $\mu\pm i\omega$ with $\omega(R)$ (source: Lusch 2018, pp. 3-4). Eigenfunctions may not exist in some cases (p. 4).

## Failure modes
- Observables outside an invariant subspace give closure errors (above).
- Finite-data learned embeddings extrapolate poorly beyond training data (Lusch 2018, p. 7).

## Where it appears
- [[Deep Koopman (Lusch 2018)]]: autoencoder with a linear latent map.
- [[SINDy autoencoders (Champion 2019)]]: related latent-coordinate idea with sparse nonlinear latent dynamics.
- [[Dynamic mode decomposition]]: linear-observable special case.
- [[SINDy (Brunton 2016)]]: cites Koopman/DMD spectral analysis as a linear alternative to sparse nonlinear regression (p. 3).

**Sources**: `papers/Physics Informed Architectures/Lusch, Kutz, Brunton - Deep learning for universal linear embeddings of nonlinear dynamics.pdf`; `papers/ML/Brunton, Proctor, Kutz - Discovering governing equations from data by sparse identification of nonlinear dynamical systems.pdf`.
**Last updated**: 2026-11-07

---

## Related pages
- [[Deep Koopman (Lusch 2018)]] · [[Dynamic mode decomposition]] · [[SINDy]]
- [[SINDy autoencoders (Champion 2019)]] · [[Neural ODE]] · [[Physics-informed machine learning]]
