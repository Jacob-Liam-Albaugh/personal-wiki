---
type: concept
area: stochastic
areas: [stochastic, math]
source-ref: "Einstein 1905, §3-5; Li, Lecture 12"
tags: [uq, sampling]
---

# Brownian motion

**Summary**: The irregular motion of small particles suspended in a liquid, explained by Einstein as thermal agitation, and its idealisation as the [[Wiener process]].

---

## Physical picture

Einstein treated displacements over short intervals as independent random steps. The density then obeys the diffusion equation (source: Einstein 1905, §4, eq. 10):

$$\frac{\partial f}{\partial t}=D\frac{\partial^2f}{\partial x^2}$$

with root-mean-square displacement (eq. 11-12)

$$\lambda_x=\sqrt{2Dt}$$

and $D$ fixed by temperature, viscosity and particle size (§5). The measured displacement gives Avogadro's number.

## Mathematical object

The limit of a random walk with space step $1/\sqrt n$ and time step $1/n$ is the [[Wiener process]] (source: Li, Thm 1.1). Constructions: random-walk limit, KL series, Haar basis (source: Li, §1).

Wiki note: the same $\sqrt t$ growth appears as the noise term in [[Langevin dynamics]] and [[SGLD]]; the density's diffusion equation is a special case of the [[Fokker-Planck equation]].

**Covered in**: ASML book sinverse/sodes (ME 697 6.1)
**Sources**: Einstein 1905; Li.
**Last updated**: 2026-11-06

---

## Related pages
- [[Wiener process]]
- [[Brownian movement (Einstein 1905)]]
- [[Brownian motion construction (Li n.d.)]]
- [[Karhunen-Loève expansion]]
- [[Quantum option pricing KL (Prakash 2025)]]
- [[Stochastic differential equation]], [[Euler-Maruyama method]], [[Geometric Brownian motion]], [[Ornstein-Uhlenbeck process]], [[Stochastic differential equation]].
