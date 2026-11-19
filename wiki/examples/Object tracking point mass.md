---
type: example
area: me539
areas: [me539]
source-ref: "Intro SciML (ME 539)"
tags: [bayesian, signals]
data-origin: [synthetic]
tasks: [state estimation]
uses: 2
---

# Object tracking point mass

**Summary**: 2 uses in Intro SciML (ME 539). Data: synthetic. Tasks: state estimation.

**Covered in**: Intro SciML (ME 539)
**Sources**: `text_books/Machine Learning & Statistics/intro-to-scientific-machine-learning/notebooks/19 - State Space Models - Filtering Basics/hands-on-19.1.ipynb` and the notebooks listed below.
**Last updated**: 2026-11-18

---

## Object tracking, point mass with GPS-like position sensor

`text_books/Machine Learning & Statistics/intro-to-scientific-machine-learning/notebooks/19 - State Space Models - Filtering Basics/hands-on-19.1.ipynb`

- **Source**: Intro SciML (ME 539), lecture, complete
- **Problem**: state-space simulation
- **Technique**: simulate linear Gaussian SSM
- **Data**: 50 steps seed 12345; observations 50x2, true trajectory 51x4; Dt=0.5, m=1, sigma_r=0.1, sigma_q=1e-2, force 0.1 rotating at omega=2pi/5
- **Data origin**: synthetic
- **Forward model**: x_{n+1}=A x_n+B u_n+w_n, state [rx,ry,vx,vy], y_n=C x_n+noise (2D position), Newton point mass
- **Unknown dimension**: 4 (state)
- **Data dimension**: 2 per step
- **Ground truth**: simulated true trajectory
- **What makes it hard**: easy, linear Gaussian
- **Libraries**: numpy

## Kalman filtering and RTS smoothing of the tracked point mass

`text_books/Machine Learning & Statistics/intro-to-scientific-machine-learning/notebooks/20 - State Space Models - Kalman Filters/hands-on-20.1.ipynb`

- **Source**: Intro SciML (ME 539), lecture, complete
- **Problem**: state estimation
- **Technique**: Kalman filter predict/update, batch_filter, rts_smoother
- **Data**: same model as 19.1 with sigma_r=0.05 and force 0.01
- **Data origin**: synthetic
- **Forward model**: linear Gaussian SSM, 4D state, 2D position observations
- **Unknown dimension**: 4 (state)
- **Data dimension**: 2 per step
- **Ground truth**: simulated true trajectory; exact posterior
- **What makes it hard**: easy, exact posterior
- **Libraries**: filterpy, numpy

## Related pages
- [[Examples catalogue]]
- [[Kalman filter]] · [[Stochastic state-space model]] · [[Newton's method]]
