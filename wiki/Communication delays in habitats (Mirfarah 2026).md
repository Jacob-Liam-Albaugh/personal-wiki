---
type: paper
area: habitats
areas: [habitats, bayesian]
source-ref: "Mirfarah et al 2026, Expert Syst. Appl. 331, 133138, secs. 2-5, Tables 1-8, App. A-D"
tags: [bayesian, uq]
authors: ["[[Motahareh Mirfarah]]", "[[Hyunjin Park]]", "[[Zhiwei Chu]]", "[[Sreehari Manikkan]]", "[[Manuel Salmeron]]", "[[Herta Montoya]]", "[[Seungho Rhee]]", "[[Christian E. Silva]]", "[[Ilias Bilionis]]", "[[Shirley J. Dyke]]"]
year: 2026
venue: "Expert Systems With Applications 331, 133138"
file: "[[papers/Space Habitats/Mirfarah, Bilionis, Dyke et al - Impact of long communication delays on autonomous decision-making in deep space habitats.pdf]]"
---

# Communication delays in habitats (Mirfarah 2026)

**Summary**: Full title "Experimental study on the impact of long communication delays on autonomous decision-making in deep space habitats". On the HARSH cyber-physical testbed, 15 ten-hour experiments vary where fault detection and diagnosis (FDD) runs (on-board vs on-ground with 10/20/30 min round-trip delay) and whether the repair agent can be interrupted. Delay degrades resilience at every level, more so system-wide, and in the compound-fault episode non-linearly. Interrupting the agent for a higher-priority fault did not raise system-level resilience.

**Authors**: Motahareh Mirfarah, Hyunjin Park, Zhiwei Chu, Sreehari Manikkan, Manuel Salmeron, Herta Montoya, Seungho Rhee, Christian E. Silva, Ilias Bilionis, Shirley J. Dyke · **Year**: 2026 · **File**: [[papers/Space Habitats/Mirfarah, Bilionis, Dyke et al - Impact of long communication delays on autonomous decision-making in deep space habitats.pdf]]

---

## Problem
- Mars-scale delays mean ground-based FDD answers late. Questions: how delay affects resilience, whether on-board FDD is worth it, whether interrupting the agent helps.

## Method

> [!definition] Testbed (Sec. 2)
> HARSH: physical structural dome (ST), interior environment (IE), thermal management (TM) plus nine lateral heat panels (cryogenic chiller); cyber SPL (structural protective layer, finite element), agent AG, power PW, disruptions DIS, in Simulink R2020b on Speedgoat. 1 Hz habitat sampling; 120 sensors, 21 used by FDD. Same CPT idea as [[Thermomechanical CPT for lunar habitats (Montoya 2025)]].

- Faults: SPL damage (75% thickness loss, 0.2 to 0.05 m, panels 7-9, at 60 min); TM refrigerant leak (about 0.05 g/s, charge about 1560 g, at 90 min in compound runs).
- FDD (Table 1): SPL with TM off, physics RC network with Bayesian inference (UQ), 40 min batch, 3-7 min compute, 12.5 min inference interval; SPL with TM on, statistical power threshold, 15 min, under 1 min, 3.0 min; TM leak, Bayesian switching model (UQ), 10 min, 2-3 min, 5.0 min.
- C2 policy: standby / inspect / repair / TM off / TM on / alarm, with a D-matrix diagnostic reasoner (states good/unknown/suspect/bad).

> [!definition] Interruption rule (eq. 4)
> Interrupt if $\pi(g(a_n)) > \pi(g(a_c))$, else queue; $\pi(TM)>\pi(SPL)$. Proposed cost-aware replacement (Sec. 5):
> ```
> C_n(t, r_c) >
>   S_{c->n}
>   + C_c(t, r_n + r_resume)
> ```

> [!definition] Resilience metrics (Sec. 2.6, Table 2)
> From a performance curve $P(t)$:
> ```
> HRM = P_r / P_i      [0, inf)
> DMN = 1/(t_r - t_i)  (0, inf)
> ABM = 1/(Tmax - t_i)
>   * int_{t_i}^{Tmax}
>     P(t)/P_i dt        [0, inf)
> ```
> HRM and ABM in %, DMN in $10^{-2}$/min; $T_{max}$ is the longest recovery over all experiments. Component curves are SPL thickness and TM refrigerant level. System curve (eq. 2-3): $P(t)=\sum_{ij}\mathbf 1_{i\times j}(T_t,R_t)V_{ij}$ with $V$ in Table 3 (temperature bins 14.0-21.5-24.1-27.1-30.0 C by power bins [0,0.9), [0.9,1.44), [1.44,3.6] kW; nominal $V_{31}=1.00$).

> [!algorithm] Design of experiments (Tables 4, 6)
> FDD location (on-board 1, on-ground 2) x interruptibility (Activated A / Deactivated D); delays 10/20/30 min for on-ground. Episode 0 nominal (1 run); Episode 1 SPL damage (3 runs: (1,A), (2,A) 10 min, (2,A) 20 min); Episode 2 compound (11 runs: (1,A) x2, (2,A) 10 min x1, 20 min x2, (1,D) x2, (2,D) 10 min x1, 20 min x2, 30 min x1). 70 kWh battery, exterior -269 C, IE setpoint 22 C.

> [!definition] Statistics (Sec. 3.1, App. B-C)
> Normal likelihood with shared variance, weak Normal-Inverse-Gamma prior ($\alpha_0=1.5$, $\kappa_0,\beta_0$ from metric scale, about $\pm5$ SD); analytic posterior of delay contrasts $\Delta_{10-0}$, $\Delta_{20-10}$, reported as median and 95% central interval. App. C: Bayesian GLM with ARD, $y=\mu_0+\mu_1p+\mu_2d+\mu_3pd+\mu_4d^2+\mu_5pd^2+\epsilon$, relevance score $1/\alpha_j$.

## Results
- Episode 1: SPL FDD detects at 102.1 min (on-board) vs 96.7 min (on-ground, 20 min) local time, but effective on-ground detection is 116.7 min.
- Table 7 (Episode 1, DMN / ABM): SPL 0 min 124.82/86.46; 10 min 114.00/85.00; 20 min 105.56/83.65. System 44.98/89.82; 39.67/87.52; 38.29/85.13.
- Episode 2, 10 vs 20 min (D): HRM(TM) -3.7%; DMN -11.61 (SPL), -5.26 (system); ABM -1.92% (SPL), -2.04% (system).
- Interruption (0 min, D vs A): refrigerant charge stays higher but SPL damage lasts longer; system ABM falls 88.09 to 86.19% (-1.9%) and more energy is used.
- Table 8 posterior contrasts (median [95% CI]); weak prior ABM [-15.08, 15.08]. Examples: Ep 1 system ABM $\Delta_{10-0}$ -1.75 [-6.84, 3.35]; Ep 2 system ABM $\Delta_{20-10}$ -3.69 [-8.18, 0.83]; Ep 2 SPL HRM $\Delta_{20-10}$ -10.36 [-27.16, 6.45]. Most intervals include 0.
- Linearity: SPL ABM/DMN roughly linear in delay; Ep 2 system ABM is non-linear, curvature $\kappa=R_{10}-\tfrac12(R_0+R_{20})$ (App. A) stays non-zero over threshold sweeps and 2000 random value matrices, near zero in Ep 1.
- Outlier: (20 min, D) run where the TM leak was found during a 5-min SPL-inspection prep; first-come-first-served kept TM off through the whole SPL repair.

## Limitations
- The authors: only 15 runs, so contrasts are uncertain; conclusions may change with repeated disruption cycles or other fault severities; communication blackouts not studied.
- Wiki note: most 95% intervals in Table 8 contain 0, so "consistently degrade" rests on the sign pattern across metrics, not on any single contrast; the 30-min (2,D) run is a single run and is excluded from the interruptibility marginalization.

## Connections
- Same testbed family and NASA STRI funding as [[Thermomechanical CPT for lunar habitats (Montoya 2025)]]; leak FDD ideas in [[EKF leak severity (Mirfarah 2025)]].
- Bayesian UQ in FDD and the Bayesian GLM-ARD echo [[Hierarchical Bayesian model]] machinery.
- Cites Hao and Bilionis information-field work on state estimation; see [[Neural information field filter (Hao 2025)]] **[unverified which Hao paper is meant]**.

%% refs:start %%
**Cites in this wiki**: [[EKF leak severity (Mirfarah 2025)]], [[IFT state and parameter estimation (Hao 2024)]], [[Thermomechanical CPT for lunar habitats (Montoya 2025)]]
%% refs:end %%

**Sources**: `papers/Space Habitats/Mirfarah, Bilionis, Dyke et al - Impact of long communication delays on autonomous decision-making in deep space habitats.pdf`.
**Last updated**: 2026-11-19

---

## Related pages
- [[Thermomechanical CPT for lunar habitats (Montoya 2025)]]
- [[EKF leak severity (Mirfarah 2025)]]
- [[Hierarchical Bayesian model]]
- [[Information field theory]]
