---
type: paper
area: bayesian
areas: [bayesian, gp]
source-ref: "Gorbach, Bauer, Buhmann 2017, NIPS 30, secs. 2-5, Alg. 1"
tags: [vi, gp, bayesian, inverse-problems]
authors: ["[[Nico S. Gorbach]]", "[[Stefan Bauer]]", "[[Joachim M. Buhmann]]"]
year: 2017
venue: "NIPS 2017"
file: "[[papers/Bayesian/Gorbach, Bauer, Buhmann - Scalable Variational Inference for Dynamical Systems.pdf]]"
---

# Scalable VI for dynamical systems (Gorbach 2017)

**Summary**: Infers ODE parameters and states from sparse noisy data without solving the ODE. A [[Gaussian process]] on the states gives a distribution over derivatives, which is matched to the ODE (gradient matching). For mass-action ODEs the conditionals are Gaussian, so mean-field [[Variational inference]] has closed-form updates. It is far faster than earlier gradient matching and scales to 1000 states.

**Authors**: Nico S. Gorbach, Stefan Bauer, Joachim M. Buhmann · **Year**: 2017 · **File**: [[papers/Bayesian/Gorbach, Bauer, Buhmann - Scalable Variational Inference for Dynamical Systems.pdf]]

---

## Problem (Sec. 1-2)
- Parameter inference by numerical integration is slow and needs good initial values. Gradient matching avoids integration but was slow too.

> [!definition] Gradient matching (eq. 5-9)
> GP prior on each state; derivatives follow
> ```
> p(x'_k | X) = N(m_k, A_k)
> ```
> ODE expert:
> ```
> p(x'_k | X, theta)
>   = N(f_k(X, theta), gamma_k I)
> ```
> Multiply the two experts and integrate out $\dot x$. Dondelinger et al. 2013 (AGM) set the normaliser $Z_\theta(X)=1$; here it is found analytically.

## Method

> [!definition] Model class (eq. 10)
> Mass-action ODEs:
> ```
> f_k = sum_i theta_ki
>       prod_{j in M_ki} x_j
> ```
> Linear in the parameters and in each single state, so $p(\theta\mid X)$ and $p(x_u\mid\theta,X_{-u})$ are Gaussian.

> [!algorithm] Mean-field coordinate ascent (Alg. 1)
> ```
> Q = q(theta) prod_u q(x_u)
> lambda_hat = E_Q[eta_theta]
> psi_hat_u  = E_Q[eta_u]
> ```
> Each factor stays in the same exponential family as the true conditional. Cost $O(NK)$ per iteration.

- Grid-free; observations can be linear combinations $Y=AX+E$.

## Results

> [!example] Lotka-Volterra (Sec. 5.1)
> $\theta=(2,1,4,1)$, data on $[0,2]$ every 0.1, $\sigma^2=0.25$, RBF kernel. Median run time: mean-field 4.7 s, splines (Niu 2016) 48 s, AGM about 100× slower. Mean-field is more accurate (splines miss 3 of 4 parameters) and extrapolates to $t=4$.

> [!example] Protein signalling (Sec. 5.2)
> The Michaelis-Menten term is replaced by a latent $x_5=R_{pp}/(K_m+R_{pp})$, so the model is misspecified. Mean-field still gets 4 of 5 parameters and their ranking right at $\sigma^2=0.01$ and $0.1$. AGM is badly off when state $S$ is unobserved.

> [!example] Lorenz-96 (Sec. 5.3)
> Up to 1000 states, partly observed, under 400 s on a laptop.

## Limitations
- The authors: mean-field only; restricted to mass-action-like ODEs; deterministic ODEs; GP hyperparameters $\phi$ and $\gamma$ are fixed.
- Wiki note: mean-field factors understate posterior correlation between parameters and states.

## Connections
- An early ODE-without-solver method, like [[IFT state and parameter estimation (Hao 2024)]], which replaces the GP-derivative expert with a physics prior on the ODE residual.
- Inference: [[Variational inference]], [[ELBO]]; prior: [[Gaussian process]].

%% refs:start %%
**Cited by in this wiki**: [[IFT for UQ of differential equations (Hao 2024)]], [[IFT state and parameter estimation (Hao 2024)]]
%% refs:end %%

**Sources**: `papers/Bayesian/Gorbach, Bauer, Buhmann - Scalable Variational Inference for Dynamical Systems.pdf`.
**Last updated**: 2026-11-21

---

## Related pages
- [[Variational inference]]
- [[Gaussian process]]
- [[ELBO]]
- [[Identifiability]]
- [[IFT state and parameter estimation (Hao 2024)]]
