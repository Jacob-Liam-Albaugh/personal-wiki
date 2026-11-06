---
type: definition
area: math
areas: [math, operators]
source-ref: "Cao, Goswami, Karniadakis 2023, eqs. 1-4, p. 2"
tags: [operators]
---

# Laplace transform

> [!definition] Laplace transform (Cao et al. 2023, eqs. 1-4, p. 2)
> $$\mathcal L\{x\}(s)=\int_0^\infty x(t)\,e^{-st}\,dt,\qquad s=\sigma+i\omega$$
> $$\mathcal L\{\dot x\}=s\,\mathcal L\{x\}-x(0)$$
> $$\mathcal L\{\ddot x\}=s^2\mathcal L\{x\}-s\,x(0)-\dot x(0)$$
>
> (source: `Operators/Karniadakis, Cao, Goswami - LNO - Laplace Neural Operators.pdf`, p. 2)

**Intuition**: a one-sided Fourier transform with an extra decay $e^{-\sigma t}$. It handles transients and growth, and its derivative rule carries the initial conditions.

Compare the Fourier transform, $\mathcal F\{x\}(\omega)=\int_{-\infty}^\infty x\,e^{-i\omega t}dt$, where $\mathcal F\{\dot x\}=i\omega\,\mathcal F\{x\}$ has no initial-value term.

> [!warning] Printed form
> The source paper prints $\mathcal L(\dot x)=\mathcal L\{x\}-x(0)$ (eq. 3, p. 2, checked on the page image), without the factor $s$, although the next line says differentiation corresponds to multiplying by $s$. This page states the standard identity (Wiki note).

## Where it appears
- [[LNO]]: the motivation for a pole-residue kernel.
- [[LNO (Cao 2023)]].

## Related / discrete-time counterpart
- [[Z-transform]] is the discrete-time analogue; on the unit circle it reduces to the [[DTFT]], and on the imaginary axis the Laplace transform reduces to the [[Fourier transform]]. (source: Digital Signal Processing/Topic DSP.6 z-transforms March 7, 2025.pdf, p. 1; ece301final_equation-sheet.pdf, p. 1)
- See [[ECE438 DSP.6 - z-transforms]].

**Sources**: `Operators/Karniadakis, Cao, Goswami - LNO - Laplace Neural Operators.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[LNO]] · [[FNO]]
- [[Poisson and Laplace equations]]: the Laplace PDE for the potential, not the Laplace transform; disambiguate (source: lect_12.pdf).
