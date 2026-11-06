---
type: lecture
area: dsp
source-ref: "L37 Apr 25, 2025, front page"
course: ece438
lecture: L37
tags: [signals]
---

# ECE438 L37 - Block transform coding and multiresolution processing

**Summary**: Lecture 37 notes: predictive coding encoder/decoder review, PSNR/MSE limits, DCT coefficient variance, and the contrast sensitivity curve.

**Sources**: `Digital Signal Processing/front page/L37 Apr 25, 2025.pdf`.
**Last updated**: 2026-11-06

---

## Last time and this time

- Last time: Predictive coding; image fidelity (MSE, PSNR)
- This time: Block-based transform coding; multiresolution image processing
(source: L37 Apr 25, 2025.pdf, p. 1)

## Review and notes

- Predictive coding encoder: the difference $x_i-\hat x_i$ between the input and the prediction is quantized and encoded; the quantized difference $Q(x_i-\hat x_i)=e_i$ is added back to the prediction to form $\tilde x_i$, which feeds the predictor/delay. The decoder adds $e_i$ to the prediction from the same predictor/delay (p. 1).
- PSNR/MSE are fairly effective when comparing one image (content) compressed different amounts with the same algorithm. PSNR is known to perform less well when comparing different image content or different artifact types (p. 1).
- Slide (Yao Wang, 2003): energy/variance of DCT coefficients in typical images on a log scale falls steeply with the zigzag index; low horizontal and low vertical frequencies come earlier in the zigzag order (p. 3).
- Slide: a chirp image and the contrast sensitivity curve, showing the visual system is most sensitive at mid frequencies (p. 5).

## Logistics

- Final exam review: Bruce (TA), Sunday 5/4 at 2 pm, room TBA.
(source: L37 Apr 25, 2025.pdf, p. 1)

## Related pages
- [[ECE438 IP.6 - Image compression]] · [[ECE438 IP.7 - Multiresolution image processing]] · [[Quantization]] · [[DFT]]
