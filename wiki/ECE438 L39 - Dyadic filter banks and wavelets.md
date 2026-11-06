---
type: lecture
area: dsp
source-ref: "L39 Apr 30, 2025, front page"
course: ece438
lecture: L39
tags: [signals]
---

# ECE438 L39 - Dyadic filter banks and wavelets

**Summary**: Lecture 39 front page: Gaussian and Laplacian pyramid recap, dyadic filter banks and wavelets, and final exam logistics.

**Sources**: `Digital Signal Processing/front page/L39 Apr 30, 2025.pdf`.
**Last updated**: 2026-11-06

---

## Last time and this time

- Last time: Gaussian and Laplacian pyramids
- This time: Dyadic filter banks and wavelets
(source: L39 Apr 30, 2025.pdf, p. 1)

## Review and notes

- Gaussian pyramid: $g_\ell=\mathrm{REDUCE}(g_{\ell-1})$, filter plus downsample, giving many blurrier and blurrier images.
- Laplacian pyramid: $L_\ell=g_\ell-\mathrm{EXPAND}(g_{\ell+1})$, one blurry image and many difference images.
- Both are overcomplete representations. Pixels at the same location can be analyzed at different resolutions.
(source: L39 Apr 30, 2025.pdf, p. 1)

## Logistics

- Exam review Sunday 5/4 at 2 pm with Bruce in Hampton 1113. Final exam Tuesday 5/6 at 8 am, BHEE 222, 2 hours, about 6 questions, some T/F or multiple choice, some not.
(source: L39 Apr 30, 2025.pdf, p. 1)

## Related pages
- [[ECE438 IP.7 - Multiresolution image processing]] · [[Wavelet transform]] · [[Digital filter]] · [[ECE438 L38 - Gaussian and Laplacian pyramids]]
