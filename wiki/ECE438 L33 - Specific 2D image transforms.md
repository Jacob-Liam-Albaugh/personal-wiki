---
type: lecture
area: dsp
source-ref: "L33 Apr 14, 2025, front page"
course: ece438
lecture: L33
tags: [signals]
---

# ECE438 L33 - Specific 2D image transforms

**Summary**: Lecture 33 notes: orthonormal 2D transforms, basis images, and the specific DFT, DCT, DST, Walsh-Hadamard and Haar transforms, with figures from the textbook.

**Sources**: `Digital Signal Processing/front page/L33 Apr 14, 2025.pdf`.
**Last updated**: 2026-11-06

---

## Last time and this time

- Last time: General 2D image transforms
- This time: Specific 2D image transforms
(source: L33 Apr 14, 2025.pdf, p. 1)

## Review and notes

- All these orthonormal transforms are invertible and contain the same energy and information as the signal/image.
- 2D orthonormal (unitary) transform, all $N\times N$: forward $T=AFA^T$, inverse $F=A^{*T}TA^*$, because $A^{*T}=A^{-1}$.
- In words: premultiply by $A$ to apply the 1-D transform to columns, transpose, premultiply by $A$ to apply it to rows, transpose back: $(A(AF)^T)^T=AFA^T$.
- Basis images: if $s_u$ are the basis functions and $A=[s_0\,s_1\dots s_{N-1}]^T$, then $s_us_v^T$ are the $N\times N$ basis images (p. 1).
- DFT basis images (8x8): DC is the lowest-frequency basis image at $u=v=0$, highest frequency at $u=v=4$. It is an overcomplete representation: both real and imaginary parts are needed, even for a real signal (p. 3).
- DCT basis images: DC at $u=v=0$, highest frequency at $u=v=7$. $S(m,u)=\alpha(u)\cos\frac{(2m+1)u\pi}{2N}$ with $\alpha(0)=1/\sqrt N$ and $\alpha(u)=\sqrt{2/N}$ for $u=1,\dots,N-1$ (p. 3).
- Figure 6.11 (textbook): the periodicity implicit in the 1-D DFT has a discontinuity at the period boundary; the DCT uses a symmetric extension, so its period is $2N$ and there is no such discontinuity (p. 5).
- DST: $S(m,u)=\sqrt{\frac{2}{N+1}}\sin\frac{(m+1)(u+1)\pi}{N+1}$. No DC component (p. 5).
- Hadamard (Figure 6.16): the sequency-ordered Walsh-Hadamard transform for $N=8$ (not Hadamard order); entries are all $\pm0.35$; highest frequency at the end (p. 7).
- Haar (Figure 6.18): a wavelet transform shown as a block transform. The basis starts out very spread out and becomes increasingly localized (p. 7).

## Logistics

- Next time: Exam 3, here, 50 minutes; coverage up to and including general 2D image transforms.
(source: L33 Apr 14, 2025.pdf, p. 1)

## Related pages
- [[ECE438 IP.5 - Image transforms and wavelets]] · [[DFT]] · [[Wavelet transform]] · [[Principal component analysis]] · [[Karhunen-Loève expansion]] · [[ECE438 L32 - 2D image transforms and Exam 3 coverage]]
