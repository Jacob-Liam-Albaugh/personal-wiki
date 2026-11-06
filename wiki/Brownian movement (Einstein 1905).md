---
type: paper
area: stochastic
areas: [stochastic]
source-ref: "Einstein 1905, Ann. d. Phys. 17, 549, §3-5 (Dover translation, eq. 10-12)"
tags: [uq]
authors: ["[[Albert Einstein]]"]
year: 1905
venue: "Annalen der Physik 17, 549 (Dover translation by Cowper, 'Investigations on the Theory of the Brownian Movement')"
file: "papers/Stochastic Methods/Einstein - Brownian Movement.pdf"
---

# Brownian movement (Einstein 1905)

**Summary**: Argues from the molecular-kinetic theory of heat that microscopically visible particles suspended in a liquid must move irregularly by thermal agitation, with a mean displacement growing as the square root of time. Links the diffusion coefficient to viscosity and particle size, which makes the atomic size (Avogadro's number) measurable from the motion.

**Authors**: Albert Einstein · **Year**: 1905 · **File**: `papers/Stochastic Methods/Einstein - Brownian Movement.pdf`

---

Wiki note: the PDF is a scan of the Dover edition (11 pp.). It holds the first paper and only the opening of the 1906 follow-up. Equations are images in the scan; the ones below were read from the page images (pp. 10-11 of the PDF) and the rest of the argument from the text layer, which is partly garbled.

## Problem

If the molecular-kinetic theory of heat is right, suspended particles of visible size should show thermal motion; if no such motion is found, "a weighty argument would be provided against" that theory (p. 3). Einstein notes he cannot tell whether his motions are the same as the already known Brownian motion, because his information on it is too imprecise (p. 2).

## Method

1. **Osmotic pressure of suspended particles** (§1-2, pp. 3-6). Classical thermodynamics assigns no pressure to suspended particles, but the kinetic theory treats a suspended particle like a dissolved molecule. Using the entropy and free energy of the system, Einstein derives that a dilute suspension exerts the same osmotic pressure as a solution with as many solute molecules.
2. **Diffusion as balance of two fluxes** (§3, pp. 6-8). Put a force $K$ on each particle. Equilibrium is the osmotic pressure gradient balancing $K$ per unit volume. The same state is read as two opposed processes: drift under $K$ at the Stokes velocity (viscosity $k$, particle radius $P$), and diffusion with coefficient $D$. Eliminating the force gives
$$D=\frac{RT}{N}\cdot\frac1{6\pi kP}\qquad\text{(§5, p. 17)}$$
with $N$ the number of molecules in a gram-molecule. $D$ depends only on temperature, the liquid's viscosity and the particle size.
3. **Irregular motion as random steps** (§4, pp. 8-10). Pick a time interval $\tau$ short on the observation scale but long enough that successive displacements of one particle are independent. Displacements $\Delta$ follow a symmetric law $\phi(\Delta)$. Expanding the density $f(x,t+\tau)$ in $\tau$ and $\Delta$ gives the diffusion equation
$$\frac{\partial f}{\partial t}=D\frac{\partial^2f}{\partial x^2},\qquad D=\frac1\tau\int\frac{\Delta^2}2\phi(\Delta)\,d\Delta.$$
4. For a point source the solution is the normal density (eq. 10, p. 17)
$$f(x,t)=\frac n{\sqrt{4\pi D}}\frac{e^{-x^2/4Dt}}{\sqrt t}$$
so the displacement distribution is the one for "fortuitous error".

> [!theorem] Mean displacement (eq. 11-12, p. 17)
> The root-mean-square displacement along one axis is
> $$\lambda_x=\sqrt{\overline{x^2}}=\sqrt{2Dt},$$
> proportional to $\sqrt t$. The root mean square of the total displacement is $\lambda_x\sqrt3$.
>
> (source: Einstein - Brownian Movement.pdf, eq. 11-12, p. 17)

Eliminating $D$ gives the formula for $\lambda_x$ in terms of $T$, viscosity and radius, and inverted, a formula for $N$ from the measured displacement (§5, p. 18).

## Results

Numerical example (p. 18): with $N=6\times10^{23}$ (from the kinetic theory of gases), water at 17 °C, viscosity $k=1.35\times10^{-2}$, particle diameter $0.001$ mm, the paper gets $\lambda_x\approx8\times10^{-5}$ cm $=0.8\,\mu$ in one second, about $6\,\mu$ in one minute (digits read from the page image). The paper closes the first article hoping someone will measure this to test the theory.

The 1906 article opens (p. 19) by noting that Siedentopf and Gouy had meanwhile concluded by direct observation that Brownian motion is caused by thermal motion of the liquid's molecules, with path sizes matching the theory's order of magnitude.

## Limitations

Stated assumptions: particles independent of each other, liquid homogeneous with no force on the particles, concentration low, and time intervals long enough for independent steps (pp. 6, 8). The argument gives a distribution of displacements, not a continuous-time path model.

Wiki note: the mathematical object Einstein describes, independent Gaussian increments with variance proportional to $t$, is what became the [[Wiener process]]. Einstein's $2D$ plays the role of the variance rate; for standard [[Brownian motion]] $2D=1$. The diffusion equation is the [[Fokker-Planck equation]] of that process.

## Connections

- Mathematical construction and path properties: [[Brownian motion construction (Li n.d.)]]. Invariance principle in that note is the "random steps in the limit" picture of §4.
- The same $\sqrt t$ scaling appears as the noise in [[Langevin dynamics]] and [[SGLD]].

**Sources**: `papers/Stochastic Methods/Einstein - Brownian Movement.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Brownian motion]] · [[Wiener process]] · [[Fokker-Planck equation]] · [[Langevin dynamics]]
- [[Brownian motion construction (Li n.d.)]] · [[KL expansions of the Wiener process (Deheuvels 2006)]]
