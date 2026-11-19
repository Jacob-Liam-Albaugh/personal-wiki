---
type: paper
area: habitats
areas: [habitats, inverse-problems]
source-ref: "Rautela et al 2023, Acta Astronaut. 203, 385-391, eq. 7-8, Alg. 1, Table 2"
tags: [inverse-problems, optimization, pde]
authors: ["[[Mahindra Rautela]]", "[[Motahareh Mirfarah]]", "[[Christian E. Silva]]", "[[Shirley J. Dyke]]", "[[Amin Maghareh]]", "[[S. Gopalakrishnan]]"]
year: 2023
venue: "Acta Astronautica 203, 385-391"
file: "[[papers/Space Habitats/Rautela, Mirfarah, Silva, Dyke et al - Real-time rapid leakage estimation for deep space habitats using exponentially-weighted adaptively-refined search.pdf]]"
---

# EWARS leak estimation (Rautela 2023)

**Summary**: Estimates the effective leak area of a pressure chamber by fitting a lumped gas-dynamics forward model to the measured pressure. Brute-force search is made fast by adaptive refinement (ARS, 300 evaluations instead of 10 000) and noise-robust by an exponentially weighted objective (EW). Tested on a lab chamber with constant and step-varying leaks; mean absolute percent error is below 1% and run time drops about 7x.

**Authors**: Mahindra Rautela, Motahareh Mirfarah, Christian E. Silva, Shirley J. Dyke, Amin Maghareh, S. Gopalakrishnan · **Year**: 2023 · **File**: [[papers/Space Habitats/Rautela, Mirfarah, Silva, Dyke et al - Real-time rapid leakage estimation for deep space habitats using exponentially-weighted adaptively-refined search.pdf]]

---

## Problem
- Real-time leak severity for a habitat from pressure data, using a physics model rather than a learned one.

## Method

> [!definition] Forward model (eq. 1-6)
> Lumped, isentropic ideal-gas two-stage ODE. Stage I (choked) has a closed form for $\gamma=1.4$; Stage II (unchoked) is solved with RK4.

> [!algorithm] EWARS (eq. 7-8, Alg. 1)
> ```
> F_t = [P_phy(A_e, theta, t)
>        - P_exp(t)]^2
> S_t = alpha F_t
>       + (1 - alpha) S_{t-1}
> ```
> At each step ARS coarsely grids the $A_e$ range ($N_1=100$), refines around the minimum ($N_2=200$ more, $\pm\Delta$) until $\Delta\le\epsilon$; $A_e$ minimizes the smoothed $S_t$. $S_0=F_0$ in eq. 8 (Alg. 1 initializes $S_0=0$). Convexity of the objective is asserted, not proved.

## Results
- Chamber 800 x 400 x 400 mm, 1020 cold-rolled steel, about 2 atm inside; offline data at 20 kHz, online at 1 kHz (Speedgoat). Search bounds [1e-3, 1] mm$^2$, $\epsilon=5\mathrm{e}{-5}$ mm$^2$; $T_{01}\approx300$ K.
- Constant leaks (4.1, Fig. 5): $A_e=0.16, 0.22, 0.28$ mm$^2$, $N=150$, $\alpha=0.125$; converges in about 2.5-3 min, faster for small leaks.
- Variable leaks (4.2, Fig. 6): three 3-min steps, 0.08 to 0.16 and 0.16 to 0.08 mm$^2$, $N=250$, $\alpha=0.01$; decreasing leaks tracked better.
- Compute time (Table 2, minutes, i9-10920X): constant leak fBFS 8.67 vs EWARS 1.27; variable leak 31.60 vs 4.79.
- Accuracy: mean absolute percent error below 1% in all scenarios (below 0.5% at 0.08 mm$^2$, 1% at 0.28 mm$^2$); stated only in prose (Sec. 5), no formula. Fig. 7: EWARS gives a less noisy estimate than fBFS at 0.25 mm$^2$, $\alpha=0.125$.

## Limitations
- The authors: isentropic, no heat transfer or friction losses; aleatoric uncertainty in $p_{atm}$, $T_{atm}$ and initial fill ignored; future work on heat transfer and UQ.
- Wiki note: no uncertainty on $A_e$ and the only comparator is the full brute-force search (fBFS) on the same objective, so there is no comparison to a recursive estimator; [[EKF leak severity (Mirfarah 2025)]] later supplies one.

## Connections
- Superseded for uncertainty by [[EKF leak severity (Mirfarah 2025)]] (same test bed).
- Leak severity is the fault parameter that [[Communication delays in habitats (Mirfarah 2026)]] reasons about at the system level.

%% refs:start %%
**Cited by in this wiki**: [[EKF leak severity (Mirfarah 2025)]]
%% refs:end %%

**Sources**: `papers/Space Habitats/Rautela, Mirfarah, Silva, Dyke et al - Real-time rapid leakage estimation for deep space habitats using exponentially-weighted adaptively-refined search.pdf`.
**Last updated**: 2026-11-19

---

## Related pages
- [[EKF leak severity (Mirfarah 2025)]]
- [[Bayesian inverse problems]]
- [[Convex function]]
