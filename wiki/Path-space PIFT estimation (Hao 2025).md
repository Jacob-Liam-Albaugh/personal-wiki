---
type: paper
area: ift
areas: [ift, bayesian, inverse-problems, physics-informed]
source-ref: "Hao, Bilionis 2025, in Model Validation and Uncertainty Quantification Vol. 3 (Proc. IMAC), Springer, pp. 31–35"
tags: [ift, vi, sampling, bayesian, inverse-problems, physics-informed, uq]
authors: ["[[Kairui Hao]]", "[[Ilias Bilionis]]"]
year: 2025
venue: "Model Validation and Uncertainty Quantification, Vol. 3 (Conf. Proc. SEM IMAC), Springer"
file: "[[papers/IFT/Hao, Bilionis - Physics-informed information field theory approach to dynamical system parameter and state estimation in path space.pdf]]"
---

# Physics-informed IFT for dynamical-system estimation in path space (Hao 2025)

**Summary**: Five-page conference chapter restating [[IFT state and parameter estimation (Hao 2024)]] in path-space notation, $x=(x_0,x_{-0})$, and comparing the two inference routes: SGLD from [[PIFT (Alberts 2023)]] and stochastic VI. On Duffing both give similar posteriors, VI about 35× faster. It repeats the misspecified Lotka–Volterra result that the learned $\beta$ falls as model error grows.

**Authors**: Kairui Hao, Ilias Bilionis · **Year**: 2025 · **File**: [[papers/IFT/Hao, Bilionis - Physics-informed information field theory approach to dynamical system parameter and state estimation in path space.pdf]]

---

## Method
- Prior on the path minus its start, conditioned on $x_0$ and $\theta$:
```
p(x_{−0} | x0, θ)
  ∝ exp(−β ∫‖ẋ − f‖² dt)
```
  with the same $\theta$-dependent partition function as the JCP paper.
- Inference by [[SGLD]] (nested, as in [[Nested SGLD]]) or by stochastic [[Variational inference]].

## Results
> [!example] [[Duffing oscillator]]
> 101 Fourier bases. SGLD: 5M steps, 321 s. SVI: 0.1M steps, 9 s. Posteriors are similar.

> [!example] Misspecified Lotka–Volterra
> Truth adds $\alpha x_1x_3$; learned $\beta$ decreases as $\alpha$ grows. See [[Model-form error detection]].

## Limitations
- Wiki note: no new method; the comparison is one example with no accuracy metric beyond visual agreement.

## Connections
- Cites [[PIFT (Alberts 2023)]] (arXiv 2301.07609), the JCP preprint (2306.02150) and Lund, Bilionis, Dyke 2021.
- The SGLD-vs-VI trade-off is developed into NSVI vs NPSGLD in [[Neural information field filter (Hao 2025)]].
- Not identifiable as a chapter of [[IFT for UQ of differential equations (Hao 2024)]]; closest to Ch. 3.

%% refs:start %%
**Cites in this wiki**: [[IFT state and parameter estimation (Hao 2024)]], [[PIFT (Alberts 2023)]], [[SGLD (Welling 2011)]]
**Cited by in this wiki**: [[Neural information field filter (Hao 2025)]]
%% refs:end %%

**Sources**: `papers/IFT/Hao, Bilionis - Physics-informed information field theory approach to dynamical system parameter and state estimation in path space.pdf`.
**Last updated**: 2026-11-15

---

## Related pages
- [[Information field theory]]
- [[Physics-informed prior]]
- [[Nested SGLD]]
- [[Variational inference]]
- [[Model-form error detection]]
