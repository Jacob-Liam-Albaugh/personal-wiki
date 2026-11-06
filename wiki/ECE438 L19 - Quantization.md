---
type: lecture
area: dsp
source-ref: "L19 Feb 28, 2025, front page"
course: ece438
lecture: L19
tags: [signals]
---

# ECE438 L19 - Quantization

**Summary**: Lecture 19 front page: review of DT interpolation and decimation, then the start of quantization.

**Sources**: `Digital Signal Processing/front page/L19 Feb 28, 2025.pdf`.
**Last updated**: 2026-11-06

---

## Last time and this time

- Last time: DT interpolation and decimation
- This time: Quantization
(source: L19 Feb 28, 2025.pdf, p. 1)

## Review and notes

- DT interpolation is upsampling plus filtering. Upsampling squishes the spectrum, which creates replicates: $X_u(e^{j\omega})=X_e(e^{j\omega L})$. Filtering removes the high-frequency replicates.
- DT decimation is filtering plus downsampling. The filter prevents aliasing; downsampling stretches the spectrum and creates replicates.
- Decimated spectrum, with filtered signal before downsampling by $D$:
(source: L19 Feb 28, 2025.pdf, p. 1)

$$Y(e^{j\omega})=\frac{1}{D}\sum_{i=0}^{D-1}X\!\left(e^{j(\frac{\omega}{D}-\frac{2\pi}{D}i)}\right)$$

## Related pages
- [[ECE438 DSP.4.B - Sampling DT]] · [[ECE438 DSP.5 - Quantization]] · [[Quantization]] · [[Aliasing]] · [[Digital filter]]
