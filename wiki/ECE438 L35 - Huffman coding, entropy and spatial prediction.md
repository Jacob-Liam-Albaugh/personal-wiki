---
type: lecture
area: dsp
source-ref: "L35 Apr 21, 2025, front page"
course: ece438
lecture: L35
tags: [signals]
---

# ECE438 L35 - Huffman coding, entropy and spatial prediction

**Summary**: Lecture 35 front page: Huffman coding, entropy and spatial prediction, with the three redundancy types and the JPEG-style encoder chain.

**Sources**: `Digital Signal Processing/front page/L35 Apr 21, 2025.pdf`.
**Last updated**: 2026-11-06

---

## Last time and this time

- Last time: Data compression overview and basics
- This time: Huffman coding, entropy; spatial prediction
(source: L35 Apr 21, 2025.pdf, p. 1)

## Review and notes

- Three types of redundancy to be reduced: coding/representation, spatial (and temporal), and irrelevancy.
- Variable length coding: fewer bits for frequent symbols, more for infrequent. A prefix code has no codeword that is a prefix of any other codeword.
- Encoder chain for an 8x8 image block: DCT (spatial redundancy), zigzag scan (2D to 1D), quantize Q (irrelevancy reduction), run-length encoding, variable length encoding (coding-redundancy reduction), producing the image bitstream.
(source: L35 Apr 21, 2025.pdf, p. 1)

## Related pages
- [[ECE438 IP.6 - Image compression]] · [[Quantization]] · [[DFT]] · [[ECE438 L36 - Fidelity, block transform coding and JPEG]]
