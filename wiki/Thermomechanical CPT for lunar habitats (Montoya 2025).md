---
type: paper
area: habitats
areas: [habitats, mechanics]
source-ref: "Montoya et al 2025, Acta Astronaut. 234, 644-659, secs. 3-5, Tables 2-4"
tags: [mechanics, pde, uq]
authors: ["[[Herta Montoya]]", "[[Manuel Salmeron]]", "[[Christian E. Silva]]", "[[Motahareh Mirfarah]]", "[[Shirley J. Dyke]]"]
year: 2025
venue: "Acta Astronautica 234, 644-659"
file: "[[papers/Space Habitats/Montoya, Salmeron, Silva, Mirfarah, Dyke - Experimental validation of thermomechanical cyber-physical testing for lunar habitats.pdf]]"
---

# Thermomechanical CPT for lunar habitats (Montoya 2025)

**Summary**: Full title "Experimental validation of thermomechanical cyber-physical testing for the assessment of lunar habitats". Extends a 2D conduction-only real-time hybrid simulation to 3D conduction, convection, radiation and linear thermoelasticity. A regolith protective layer (SPL) is simulated in real time while a physical pressure box (ST layer plus interior air) is driven through a thermal transfer system. Micrometeorite damage to the SPL is injected cyber-side; the CPT reveals convection behaviour the numerical reference misses.

**Authors**: Herta Montoya, Manuel Salmeron, Christian E. Silva, Motahareh Mirfarah, Shirley J. Dyke · **Year**: 2025 · **File**: [[papers/Space Habitats/Montoya, Salmeron, Silva, Mirfarah, Dyke - Experimental validation of thermomechanical cyber-physical testing for lunar habitats.pdf]]

---

## Problem
- Analog habitats ignore multi-system thermomechanics; numerical studies isolate the structure from thermal and pressure systems. Lunar surface swings 100-400 K and regolith conductivity is 1e-4 to 1e-2 W/m K, so SPL depth loss changes the heat balance.

## Method

> [!definition] Reference model (Sec. 3.1)
> 3D FE transient heat transfer (eq. 1-12): conduction, convection at the IE surface, radiation at the exterior surface. Thermoelastic model (eq. 13-19, Hooke's law, $\epsilon_H=\alpha_{th}\Delta T\delta_{ij}$). Two-way coupling: temperature gives thermal strain; a damage index switches the $M,K$ matrices between nominal (0) and damaged (1). Lumped IE model (eq. 22-24):
> ```
> dTair/dt = (Qgain - Qconv)
>            / (m_air Cp_air)
> Qgain = mdot Cp (Tpress - Tair)
> Qconv = h A (Ts - Tair)
> ```

> [!algorithm] Partitioning (Sec. 3.2, eq. 25-29)
> Cyber: SPL (heat eq. 25, mechanics eq. 28). Physical: ST lid and IE (eq. 26, 29). Heat interface: a thermal transfer system imposes the cyber interface temperature (cryogenic chiller, piping, flat thermal panel; interacting-multiple-model observer and switching PID with feedforward). Mechanics: no mechanical actuator, so a mechanical state estimator solves eq. 29 from measured pressure and heat; contact is a penalty rigid link. A thermal state observer localizes non-uniform damage.

- Setup: SPL 0.465 x 0.2 x 0.865 m (8x4x10 mesh), ST 0.465 x 0.013 x 0.865 m (8x2x10), IE 0.07 m$^3$; Matlab/Simulink R2020b on Speedgoat, thermal loop at 1 Hz, pressure actuation at 5 Hz; 17 thermocouples. Initial SPL profile $T=T_L-(T_L-T_U)e^{-y/\ell}$ with $T_L=300$ K, $T_U=100$ K, $\ell=0.06$.
- Scenarios (Table 3), impact at 0.35 h: Damage 1 uniform to 0.1 m (50%), Damage 2 uniform to 0.05 m (75%), Damage 3 uniform to 0.025 m (87.5%), Damage 4 localized, max 87.5%. After impact $E=1$ Pa in the SPL.

## Results
- Metrics. Framework validation uses three performance metrics from Montoya et al. 2023: PM1 (NRMSE, second norm), PM2 (normalized maximum amplitude error), PM3 (normalized energy error); closer to 1 is better and above 90% is acceptable. Control metrics: J1, J2 (two NRMSE), J3 (normalized peak absolute error), J4 (integral absolute error, K-hour). Formulas live in the earlier papers, not here.
- Sec. 5.1 (Damage 3): SPL exterior and IE responses match the numerical reference with NRMSE below 1%; ST interfaces differ strongly. Lowering the convection coefficient near the ST-IE surface by 5% brings that interface under 1% NRMSE but a difference of about 10 K remains at the SPL-ST interface. A constant-heat-load reference agrees worse. All PM1-PM3 distributions (Fig. 10) exceed 90%; PM3 is lower near the panel edges.
- Table 4 (J1, J2, J3 %, max J4 K-hour): Nominal 0.50/0.50/2.03/0.20; Damage 1 0.41/0.40/1.40/0.14; Damage 2 0.45/0.42/1.27/0.11; Damage 3 2.00/1.12/4.56/0.46; Damage 4 1.29/0.74/4.07/0.30. All $J_i<5\%$.
- Interface temperature envelope between desired and measured differs by at most 3 K (scalar chiller command).
- Mechanics: after SPL crushing, SPL stress collapses while ST stress rises; localized damage keeps undamaged SPL elastic and widens the ST stress distribution.

## Limitations
- The authors: no mechanical actuator; scalar thermal command; no humidity or vacuum correction; Earth gravity convection (no gravitational scaling); constant material properties; impact is a prescribed geometric change; plasticity not modelled; proof-of-concept scale.
- Wiki note: the numerical reference is itself uncertain (the 5% convection tuning was chosen to fit), so "validation" is agreement with a tuned model, not with lunar data.

## Connections
- Testbed used for the decision-making experiments in [[Communication delays in habitats (Mirfarah 2026)]].
- Same pressure-box hardware family as [[EKF leak severity (Mirfarah 2025)]] and [[EWARS leak estimation (Rautela 2023)]].

%% refs:start %%
**Cited by in this wiki**: [[Communication delays in habitats (Mirfarah 2026)]]
%% refs:end %%

**Sources**: `papers/Space Habitats/Montoya, Salmeron, Silva, Mirfarah, Dyke - Experimental validation of thermomechanical cyber-physical testing for lunar habitats.pdf`.
**Last updated**: 2026-11-19

---

## Related pages
- [[Communication delays in habitats (Mirfarah 2026)]]
- [[EKF leak severity (Mirfarah 2025)]]
- [[EWARS leak estimation (Rautela 2023)]]
