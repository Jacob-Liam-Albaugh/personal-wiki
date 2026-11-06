---
type: paper
area: stochastic
areas: [stochastic, math]
source-ref: "Xiu & Karniadakis 2002, SIAM J. Sci. Comput. 24(2), 619-644"
tags: [uq, pde]
authors: ["[[Dongbin Xiu]]", "[[George Em Karniadakis]]"]
year: 2002
venue: "SIAM J. Sci. Comput. 24(2), 619-644"
file: "Stochastic Methods/Karniadakis, Xiu - The Weiner - Askey Polynomial Chaos for Stochastic Differential Equations.pdf"
---

# Wiener-Askey chaos (Xiu 2002)

**Summary**: Generalises Wiener's Hermite chaos to the full Askey scheme of orthogonal polynomials. The polynomial family is matched to the input distribution (Gaussian with Hermite, gamma with Laguerre, and so on). A decay-rate ODE with random coefficient shows exponential convergence for every matched pair.

**Authors**: Dongbin Xiu, George Em Karniadakis · **Year**: 2002 · **File**: `Stochastic Methods/Karniadakis, Xiu - The Weiner - Askey Polynomial Chaos for Stochastic Differential Equations.pdf`

---

## Problem

Wiener's homogeneous chaos expands a random process in Hermite polynomials of Gaussian variables. It works for Gaussian inputs, and for some non-Gaussian ones via the Cameron-Martin theorem. For general non-Gaussian inputs the optimal exponential rate is lost, and sometimes the rate is badly degraded (source: Karniadakis-Xiu PDF, p. 7, §4).

## Idea

Use the polynomial family whose weight function equals the input density. The expansion of a second-order process is

$$X(\theta)=\sum_{j=0}^{\infty}\hat c_j\,\Phi_j(\zeta)$$

(source: eq. 4.2). The basis is orthogonal under the ensemble average:

$$\langle\Phi_i\Phi_j\rangle=\langle\Phi_i^2\rangle\,\delta_{ij}$$

(source: eq. 4.3). The inner product is an integral against the weight $W(\zeta)$ (continuous case, eq. 4.4) or a sum (discrete case, eq. 4.5).

Each Askey-scheme family is complete in its own weighted $L^2$ space. So each expansion converges in $L^2$ by a generalised Cameron-Martin theorem (source: p. 8, §4).

## Distribution to polynomial table

(source: Table 4.1, p. 8)

| Input $\zeta$ | Chaos | Support |
|---|---|---|
| Gaussian | Hermite | $(-\infty,\infty)$ |
| gamma | Laguerre | $[0,\infty)$ |
| beta | Jacobi | $[a,b]$ |
| uniform | Legendre | $[a,b]$ |
| Poisson | Charlier | $\{0,1,2,\dots\}$ |
| binomial | Krawtchouk | $\{0,\dots,N\}$ |
| negative binomial | Meixner | $\{0,1,2,\dots\}$ |
| hypergeometric | Hahn | $\{0,\dots,N\}$ |

- Hermite, Laguerre and Jacobi are continuous chaos. Charlier, Meixner, Krawtchouk and Hahn are discrete.
- Legendre is Jacobi with $\alpha=\beta=0$. It is listed separately because of the uniform distribution.
- Wiener's original chaos is the Hermite case, a subset of the scheme.

## Galerkin procedure

For a stochastic equation $L(x,t,\theta;u)=f$, expand the solution and truncate:

$$u=\sum_{i=0}^{P}u_i(x,t)\,\Phi_i(\zeta(\theta))$$

(source: eq. 5.2). With $n$ random variables and maximum order $p$:

$$P+1=\frac{(n+p)!}{n!\,p!}$$

(source: eq. 5.3). Project the residual onto each $\Phi_k$ (eq. 5.5). Randomness moves into the basis, so the equations for the modes $u_i$ are deterministic and coupled. Any standard solver can then be used, such as Runge-Kutta in time (source: p. 9, §5.1).

## Test problem

The ODE with random decay rate:

$$\frac{dy}{dt}=-k(\theta)\,y,\qquad y(0)=\hat y$$

(source: eq. 5.6). Expand $y$ and $k$ in the same basis. The projected modes obey

$$\frac{dy_l}{dt}=-\frac{1}{\langle\Phi_l^2\rangle}\sum_{i,j}e_{ijl}\,k_i\,y_j$$

with $e_{ijl}=\langle\Phi_i\Phi_j\Phi_l\rangle$ (source: eq. 5.11).

Errors in the mean and variance are measured relative to the exact solution (eq. 5.12). Integration runs to $t=1$ with $\hat y=1$, using second-order Runge-Kutta (source: p. 10-11).

Cases tested, each with the matching chaos (source: §5.3.1-5.3.7):

- Gaussian, zero mean, unit variance: exact mean $\hat y\,e^{t^2/2}$ (eq. 5.14).
- Gamma (including exponential at $\alpha=0$): exact mean $\hat y/(1+t)^{\alpha+1}$ (eq. 5.16).
- Beta (including uniform): see §5.3.3.
- Poisson: exact mean $\hat y\,e^{-\lambda+\lambda e^{-t}}$ (eq. 5.19).
- Binomial, negative binomial, hypergeometric: exact means in eq. 5.21 and 5.23.

In every case the semilog error plots show exponential decay in the order $P$. Larger spread of the input (larger $\alpha$ for gamma) gives larger error at fixed order, but the rate stays exponential (source: p. 12).

## Cost against Monte Carlo

- An order of $P=2$ to $4$ typically brings the mean error to about $10^{-3}$ (source: §5.4, p. 16).
- The cost is slightly more than $(P+1)$ deterministic solves.
- Monte Carlo needs about $10^4$ to $10^5$ samples for the same error. For exponential input, the error was $4.0\times10^{-2}$ at $10^2$ samples and $6.5\times10^{-4}$ at $10^5$ (source: Table 5.1).
- The paper estimates a speed-up of $10^3$ to $10^4$ for this ODE, with no variance reduction.
- Caveat in the paper: with many random dimensions the number of terms grows fast (eq. 5.3), which erodes the advantage.

## Arbitrary input distributions

If the input law is not one of the basic types, project it onto the basis (source: §6):

$$k=\sum_i k_i\Phi_i,\qquad k_i=\frac{\langle k\,\Phi_i\rangle}{\langle\Phi_i^2\rangle}$$

(source: eq. 6.1). The variables $k$ and $\zeta$ live on different probability spaces. The fix is to map both to a uniform variable $u$:

$$u=F(k)=G(\zeta)$$

(source: eq. 6.5). Then

$$k_i=\frac{1}{\langle\Phi_i^2\rangle}\int_0^1 h(u)\,\Phi_i(l(u))\,du$$

with $h=F^{-1}$ and $l=G^{-1}$ (source: eq. 6.7). Evaluate by Gauss quadrature. When the inverse CDFs are unknown, use Monte Carlo with each pair $(k,\zeta)$ generated from the same uniform seed (source: §6.2).

Numerical examples approximate gamma and beta inputs with Hermite chaos. They show that Hermite chaos converges but does not reach the optimal exponential rate (source: §6.3).

## Conclusion of the paper

For any random input the Wiener-Askey chaos converges in general. The exponential rate is lost if the optimal chaos is not chosen. The authors state that extension to PDEs presents no fundamental difficulty (source: §7, p. 21).

## Wiki note

- This is the standard source for the "match the polynomials to the input law" rule used in [[Polynomial chaos]].
- The Hermite case sits next to the [[Karhunen-Loève expansion]] in practice: a KL expansion of a random field supplies the Gaussian variables $\xi_i$ that Hermite chaos then expands. See [[KL expansion note (Alexanderian 2015)]].
- The Wiener-Hermite chaos refers back to the [[Wiener process]].

%% refs:start %%
**Cited by in this wiki**: [[Amortized VI for inverse problems (Karumuri 2024)]], [[Bayesian DenseED surrogate (Zhu 2018)]]
%% refs:end %%

**Sources**: Karniadakis-Xiu PDF, §2-7 and Appendix A (appendix recurrences not summarised here).

**Last updated**: 2026-11-06

---

## Related pages
- [[Polynomial chaos]]
- [[Karhunen-Loève expansion]]
- [[KL expansion note (Alexanderian 2015)]]
- [[Wiener process]]
- [[Brownian motion]]
- [[Gaussian process]]
