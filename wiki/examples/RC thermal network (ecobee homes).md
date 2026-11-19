---
type: example
area: me697
areas: [me697, me539]
source-ref: "Planned example; not from an ingested source"
tags: [inverse-problems]
status: lead
data-origin: [real]
tasks: [system identification, state estimation]
uses: 0
---

# RC thermal network (ecobee homes)

**Summary**: Planned example, not built yet. Fills the gap "Hybrid / non-smooth" in the [[Dynamical systems table]]. Data: real. Tasks: system identification, state estimation.

Lead page written from web search and background knowledge, not from an ingested source. The model and the papers named are **[unverified]**.

**Sources**: the links below.
**Last updated**: 2026-11-19

---

## RC thermal network (ecobee homes)

- **Source**: planned, not in the books or lab papers
- **Gap filled**: Hybrid / non-smooth
- **Class**: switched ODE
- **Forward model**: C dT/dt = (T_out - T)/R + Q u(t), with u switched on or off by a thermostat with a deadband.
- **Data**: 1,000 homes for 2017 at 5-minute resolution: indoor and outdoor temperature, set points, equipment run time.
- **Data origin**: real
- **Links** (each opened by script on 2026-11-19; "resolved" means the page loaded, not that the contents were read):
  - [ecobee Donate Your Data (OSTI record)](https://www.osti.gov/biblio/1854924): resolved
- **Notes**: The best fit for a switched RC model. Column names and whether a login is needed are not confirmed.

## Related pages
- [[Examples catalogue]]
- [[Dynamical systems table]]
- [[Kalman filter]] · [[RC thermal network (NIST Net-Zero house)]]
