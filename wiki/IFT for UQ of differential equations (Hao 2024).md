---
type: paper
area: ift
areas: [ift, bayesian, inverse-problems, physics-informed, sampling]
source-ref: "Hao 2024, PhD dissertation, Purdue University"
tags: [ift, vi, sampling, mcmc, bayesian, inverse-problems, physics-informed, uq, gp]
authors: ["[[Kairui Hao]]"]
year: 2024
venue: "PhD dissertation, Purdue University (advisor Ilias Bilionis)"
file: "[[papers/IFT/Hao - Information field theory approach to uncertainty quantification for differential equations.pdf]]"
---

# IFT approach to UQ for differential equations (Hao 2024)

**Summary**: Kairui Hao's dissertation (213 pp). It collects the IFT-for-dynamics work: Ch. 3 is [[IFT state and parameter estimation (Hao 2024)]], Ch. 6 is [[Neural information field filter (Hao 2025)]], and two chapters appear in neither paper: Ch. 4 (IFT with noisy system inputs, applied to a thermal RC digital twin of a lunar-habitat testbed) and Ch. 5 (1D boundary value problems, including conductivity reconstruction for fibrous insulation and an analytical GP form of the IFT prior). Motivation is fault detection for uncrewed extraterrestrial habitats (RETHi).

**Authors**: Kairui Hao · **Year**: 2024 · **File**: [[papers/IFT/Hao - Information field theory approach to uncertainty quantification for differential equations.pdf]] · **Code**: JAX (no repository in the text)

---

## Structure
| Ch | Pages | Topic |
|---|---|---|
| 2 | 20–44 | Review: MH, MALA, HMC/[[NUTS]], VI, [[Kalman filter]], EKF, [[Particle filter]], SMC² |
| 3 | 45–87 | IFT for ODE state and parameter estimation (= JCP paper) |
| 4 | 88–132 | Noisy system inputs; thermal RC digital twin |
| 5 | 133–150 | 1D boundary value problems |
| 6 | 151–185 | NIFF (= MSSP paper) |
| App A | 202–211 | Derivations and proofs |

The mapping of chapters to papers is a wiki inference; the dissertation cites only the JCP preprint (ref [138]).

## Material beyond the papers

### Prior convergence (App. A.3, p. 205)
Prop. 2: for globally Lipschitz $f$, the prior path concentrates on the ODE solution:
```
‖E X(t) − x(t)‖² ≤ C1/β
Var X(t) → 0  as β → ∞
```
App. A.8 (p. 211): normalizing time by $T$ rescales $\beta_\tau=\beta/T$. App. A.7: the inner/outer VI scheme is a max–min problem.

### Noisy inputs (Ch. 4)
Model $\dot x=f(x,t,u;\theta)$ with input $u$ observed only as noisy $y_u$. Two steps (pp. 92–95):
```
1) p(w_u) ∝ exp(−β_u ∫‖u̇‖² dt)
   fit q(w_u | y_u) by SVI
2) IFT prior on x given w_u;
   average over q(w_u)
```
Maximizing the expected conditional ELBO minimizes a KL upper bound (Prop. 1, Lemma 1, pp. 104–106).

> [!example] Thermal RC digital twin (pp. 109–131)
> Lunar-habitat testbed: linear $\dot x=Ax+Bu$ with 12 states, 13 inputs, 7 outputs, $\theta\in\mathbb R^{35}_+$ (resistances, capacitances). Panels without interior sensors get priors tied to measured twins. $\beta_u=1000$, $\beta_x=10^4$. Trained on one of four excitation datasets; posterior predictive judged acceptable on all four, qualitatively (no error metric).

### Boundary value problems (Ch. 5)
> [!example] Conductivity of fibrous insulation (pp. 133–144)
> Steady $\frac{d}{dx}[k(T)\frac{dT}{dx}]=0$ with
> ```
> H = ∫ ( d/dx[k(T) dT/dx] )² dx
> ```
> $T(x)$ polynomial with boundary-solved coefficients; $k(T)$ a sigmoid-gated polynomial. Six Daryabeigi datasets (hot side 792–1805 K). $k(T)$ agrees with the original study, with UQ; learned $\beta$ about 100–250 (read off figures). Here $\beta$ is called the model-form-uncertainty hyperparameter, cf. [[Model-form error detection]].

> [!definition] IFT prior as a GP (pp. 145–149)
> For $\dot x-ax=0$ with both ends fixed, $H=\int(\dot x-ax)^2dt$ is quadratic, so the prior is a [[Gaussian process]]:
> ```
> mean = x*(t)
> cov(t,t') = G(t,t') / β
> (−2D² + 2a²) G = δ
> G = 0 at t = 0, T
> ```
> $x^*$ solves $(-D^2+a^2)x^*=0$ with the boundary values; $G$ comes from the Wronskian formula. Wiki note: this is the [[Physics-informed prior]] made explicit for a linear operator, the same Green's-function covariance as in [[Information field theory]]'s free theory.

### Ch. 6 differences from the paper
Duffing uses Fourier $K=50$ and 5 SGLD chains; a "neural state function" example shows $K=10$ Fourier alone fails and the residual net fixes it (p. 176). No Bouc–Wen or energy-sink examples.

## Limitations
- Stated: inner-loop VI estimator biased; relaxation adds $\beta_2$; Ch. 5 is only 1D and first-order linear for the analytic case.
- Wiki note: Ch. 4 and Ch. 5 results are qualitative; the conclusions (pp. 186–187) list no future work.

## Connections
- Advisor [[Ilias Bilionis]]; builds on [[PIFT (Alberts 2023)]], whose author wrote [[IFT for engineering inverse problems (Alberts 2024)]] in the same group.
- Short version of the SGLD-vs-VI comparison: [[Path-space PIFT estimation (Hao 2025)]].
- App. A.2 derives the prior as the path density of $dX=f\,dt+(2\beta)^{-1/2}dB$; see [[Stochastic differential equation]].

%% refs:start %%
**Cites in this wiki**: [[Adam paper (Kingma 2015)]], [[Attention is all you need (Vaswani 2017)]], [[DDPM (Ho 2020)]], [[Fourier features (Tancik 2020)]], [[GAN paper (Goodfellow 2014)]], [[Glorot init (Glorot 2010)]], [[Hidden fluid mechanics (Raissi 2020)]], [[IFT state and parameter estimation (Hao 2024)]], [[Neural ODEs (Chen 2018)]], [[PIFT (Alberts 2023)]], [[PINNs (Raissi 2019)]], [[SGLD (Welling 2011)]], [[SMC² (Chopin 2013)]], [[Scalable VI for dynamical systems (Gorbach 2017)]], [[Score SDE (Song 2021)]], [[Spectral bias (Rahaman 2019)]], [[U-Net paper (Ronneberger 2015)]], [[VAE paper (Kingma 2014)]], [[When and why PINNs fail (Wang 2022)]]
**Cited by in this wiki**: [[IFT for engineering inverse problems (Alberts 2024)]]
**Software cited**: [[software#JAX|JAX]], [[software#NumPyro|NumPyro]], [[software#PyTorch|PyTorch]], [[software#Pyro|Pyro]], [[software#TensorFlow|TensorFlow]]
%% refs:end %%

**Sources**: `papers/IFT/Hao - Information field theory approach to uncertainty quantification for differential equations.pdf`.
**Last updated**: 2026-11-15

---

## Related pages
- [[Information field theory]]
- [[Physics-informed prior]]
- [[IFT state and parameter estimation (Hao 2024)]]
- [[Neural information field filter (Hao 2025)]]
- [[Gaussian process]]
- [[Model-form error detection]]
- [[Kalman filter]]
- [[Particle filter]]
