---
type: concept
area: ml
areas: [ml, math]
source-ref: "Gu & Dao 2023, §2"
tags: [ml, signals]
---

# State space model

**Summary**: Any recurrent process with a latent state. The word spans control (linear dynamical systems, [[Kalman filter]]), hidden Markov models, reinforcement learning, and, in deep learning, structured SSMs (S4) used as sequence layers (source: Gu & Dao 2023, p. 4).

---

## Continuous-time form

$$h'(t)=Ah(t)+Bx(t)$$

$$y(t)=Ch(t)$$

(source: Gu & Dao 2023, eq. 1). After discretisation with step $\Delta$ it is a linear recurrence, which is also a convolution with kernel $(C\bar B,C\bar A\bar B,\dots)$ (source: eqs. 2-3). With fixed parameters this is a [[LTI system]], and the output is a [[Convolution]].

## In deep learning

- Training in convolution mode (parallel), inference in recurrent mode (constant memory per step).
- Diagonal $A$ keeps cost linear in sequence length.
- Strong on continuous signals (audio, vision); weaker on text, until input-dependent parameters were added ([[Mamba (Gu 2023)]]).
- Contrast with [[Attention]]: the SSM compresses context into a fixed state, attention stores all of it.

## Terminology caution

Wiki note: in filtering pages ([[Kalman filter]], [[Particle filter]]) the state is hidden and observed through noise, and the goal is inference. In SSM layers the state is a learned feature and there is no observation noise model. Same equations, different purpose.

**Sources**: Gu & Dao 2023.
**Last updated**: 2026-11-06

---

## Related pages
- [[Mamba (Gu 2023)]]
- [[Transformer]]
- [[Attention]]
- [[Kalman filter]]
- [[Particle filter]]
- [[LTI system]]
- [[Convolution]]
