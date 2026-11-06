---
type: method
area: operators
areas: [operators, ml]
source-ref: "Cao, Goswami, Karniadakis 2023, eqs. 8-18, pp. 5-6"
tags: [operators, ml]
---

# Laplace neural operator (LNO)

> [!algorithm] Laplace layer (Cao et al. 2023, eqs. 8-9, p. 5)
> The kernel is a rational transfer function with $N$ trainable poles $\mu_n$ and residues $\beta_n$:
> $$K_\phi(s)=\sum_{n=1}^N\frac{\beta_n}{s-\mu_n}$$
> Architecture (Fig. 1, pp. 3-4): lift with $P$, apply one Laplace layer plus a local linear map $W$, project with $Q$.
>
> (source: `Operators/Karniadakis, Cao, Goswami - LNO - Laplace Neural Operators.pdf`, p. 5)

**Intuition**: an FNO multiplier is a set of numbers on fixed frequencies. A pole-residue kernel is the transfer function of a linear system, so its output has a decaying transient term as well as a steady-state term. The [[Laplace transform]] also carries initial conditions, which the Fourier transform does not.

> [!warning] Name clash
> In the FNO and Neural Operator papers "LNO" means the low-rank neural operator; see [[Neural operator#Low-rank neural operator|low-rank neural operator]].

## Pole-residue method
Write the input as a periodic excitation, $V(s)=\sum_\ell\alpha_\ell/(s-i\omega_\ell)$. The product $U=K_\phi V$ re-expands into partial fractions (eqs. 12-18, pp. 5-6):
$$U(s)=\sum_n\frac{\gamma_n}{s-\mu_n}+\sum_\ell\frac{\lambda_\ell}{s-i\omega_\ell}$$
$$\gamma_n=\beta_nV(\mu_n),\qquad\lambda_\ell=\alpha_\ell K_\phi(i\omega_\ell)$$
$$u(t)=\sum_n\gamma_ne^{\mu_nt}+\sum_\ell\lambda_\ell e^{i\omega_\ell t}$$
The first sum is the transient, the second the steady state. The idea comes from structural dynamics (the paper's refs. [6, 7]).

## Results and limits
- 3 ODEs and 3 PDEs. One Laplace layer is compared with a 4-layer [[FNO]] and a GRU.
- The text gives no error table. The paper says the beam error is "over an order of magnitude" lower than FNO's, and the diffusion error "two orders" lower.
- By the reader's eye-readings of Fig. 3 (p. 8, **[unverified]**, ±0.02), the GRU beats LNO on both damped ODE cases and on Lorenz with $\rho=5$.
- The abstract claims "exponential convergence", but the text never analyses it.
- When the layer input is an initial condition rather than a source term, there is no significant gain (p. 17).

## Where it appears
- [[LNO (Cao 2023)]]: introduces it.

**Sources**: `Operators/Karniadakis, Cao, Goswami - LNO - Laplace Neural Operators.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Neural operator]] · [[FNO]] · [[Laplace transform]] · [[Kernel integral operator]]
