---
type: lecture
area: dsp
source-ref: "Topic DSP.3.C Python examples, pp. 1-2"
course: ece438
lecture: DSP.3.C
tags: [signals]
---

# ECE438 DSP.3.C - Spectral leakage Python examples

**Summary**: Two annotated pages of Python/FFT plots illustrating [[Spectral leakage]] for a sinusoid of period 14 observed over 64 samples, and the effect of zero padding the DFT.

**File**: `Digital Signal Processing/Topic DSP.3.C Python Examples Spectral Leakage Feb 6, 2025.pdf`

---

## Topics
- The test signal is periodic with period 14 but not with period 64, so a 64-sample record is not a whole number of periods (p. 1).
- $N=64$ DFT: two broad peaks with skirts, "demonstrates spectral leakage".
- $N=128$ (zero padding): more spectral samples, ripples appear around the peaks.
- $N=1024$: even more structure of the sampled DTFT is revealed (the sidelobes of the window's DTFT).
- Why: the DFT implicitly analyses the periodic extension of the 64 samples (p. 2), shown as a plot where the 64-sample block repeats and the waveform has a kink at each seam.

## Key results
- Zero padding does not remove leakage; it samples the same DTFT more densely, so it reveals the leakage rather than fixing it (matches the theory in [[ECE438 DSP.3.C - More on DFT]]).
- The leakage is unavoidable when a non-integer number of periods is analysed; the notes say there are ways to accommodate it (other windows).

**Sources**: `Digital Signal Processing/Topic DSP.3.C Python Examples Spectral Leakage Feb 6, 2025.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Spectral leakage]] · [[DFT]] · [[DTFT]] · [[FFT]] · [[ECE438 DSP.3.C - More on DFT]]
