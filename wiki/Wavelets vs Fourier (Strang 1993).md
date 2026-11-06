---
type: paper
area: math
areas: [math, stochastic]
source-ref: "Strang, Bull. AMS 28(2):288-305, 1993, arXiv:math/9304214"
tags: [signals]
authors: ["[[Gilbert Strang]]"]
year: 1993
venue: "Bulletin of the AMS 28(2), 288-305; arXiv:math/9304214"
file: "Transforms/Strang - Wavelet Transforms vs Fourier Transforms.pdf"
---

# Wavelets vs Fourier (Strang 1993)

**Summary**: An elementary introduction to wavelets. It starts from the Haar basis, compares the fast wavelet transform (FWT) with the FFT, builds smoother Daubechies wavelets through the dilation equation, and ends with the compression contest between Fourier-based and wavelet-based standards.

**Authors**: Gilbert Strang · **Year**: 1993 · **File**: `Transforms/Strang - Wavelet Transforms vs Fourier Transforms.pdf`

---

## Haar wavelet

The scaling function $\phi(x)$ and wavelet $W(x)$ are piecewise constant. The basis is built by translation and dilation (source: §1, p. 2):

$$W_{jk}(x)=W(2^jx-k)$$

For $j\ge0$ and $0\le k<2^j$ these, with $\phi$, form a basis of $L^2[0,1]$ and are mutually orthogonal.

- Fourier and Walsh functions have global support. A local signal then needs extreme cancellation and many terms; wavelets give a local basis (source: p. 2).
- Example: values $9,1,2,0$ on four quarter-intervals have Haar coefficients $3,2,4,1$ (source: p. 2).
- Both transforms are matrices with orthogonal columns: $y=W_4b$ and $y=F_4a$. The inverse has the same form as the original (source: p. 3).

## Fast transforms

- $F_n$ is full, so a direct product costs $n^2$. The FFT factorises it into half-size transforms and costs $\tfrac12 n\log_2 n$ (source: §2, pp. 3-5). For $n=1024$ that is about 200 times fewer multiplications.
- $W_n$ is sparse, with $n(\log_2 n+1)$ nonzeros. The pyramid scheme (Burt-Adelson, Mallat) halves the work at each level, so the total factor is $1+\tfrac12+\tfrac14+\dots<2$ and the FWT costs $O(n)$ (source: p. 4).
- Choosing $W_{2^k}$ or $I_{2^k}$ in the third factors gives a family of orthogonal bases, a wavelet packet, with a "best basis" search for compression (source: p. 4).
- The short-time Fourier transform blocks the signal into windows. Blocking breaks fingerprint ridges (source: p. 5).

## Multiresolution and the dilation equation

Spaces $V_j$ (translates of $\phi(2^jx-k)$) are nested, and $W_j$ is the orthogonal complement of $V_j$ in $V_{j+1}$ (source: §3, pp. 6-7):

$$V_{j+1}=V_j\oplus W_j$$

Dilation is built in by $f(x)\in V_j\iff f(2x)\in V_{j+1}$, so $\phi$ is a combination of translates of $\phi(2x)$ (source: p. 7):

$$\phi(x)=\sum_k c_k\,\phi(2x-k)$$

Haar has $c_0=c_1=1$. The wavelet reuses the coefficients in reverse order with alternating signs (source: eq. 8):

$$W(x)=\sum_k(-1)^k c_{1-k}\,\phi(2x-k)$$

Convolution with $\phi$ averages (blurs); convolution with $W$ differences (picks out detail) (source: p. 8).

## Solving the dilation equation

- Fourier route: $\hat\phi(\xi)=P(\xi/2)\hat\phi(\xi/2)$ with symbol $P(\xi)=\tfrac12\sum c_ke^{ik\xi}$. Then $\sum c_k=2$, and $\hat\phi$ is an infinite product (source: p. 8).
- Matrix route: $\phi$ at the integers is an eigenvector with eigenvalue 1. Dyadic values follow from products of two matrices $A,B$, one per binary digit (source: p. 9, eq. 11).
- Convergence for all digit orders is governed by the joint spectral radius $\rho(A,B)$. Continuity holds if $\rho<1$, and $\phi,W\in C^\alpha$ for $\alpha<-\log_2\rho$ (source: pp. 9-10).

## Daubechies wavelets

Haar approximates poorly: it only reproduces constants, like Euler's method or the rectangle rule (source: p. 5-6). Orthogonality and compact support conflict with reproducing $ax+b$. Daubechies found four coefficients that give both (source: p. 6, 11):

$$c_0,c_1,c_2,c_3=\tfrac14\big(1+\sqrt3,\;3+\sqrt3,\;3-\sqrt3,\;1-\sqrt3\big)$$

- Accuracy of order $p$ (Condition $A_p$): $\sum(-1)^kk^mc_k=0$ for $m<p$ (source: eq. 14). The error is $O(h^p)$ with $h=2^{-j}$.
- Each extra order costs two more coefficients. Daubechies uses the minimum $2p$ (source: p. 11, 14).
- Orthogonality is Condition O on the symbol, plus a technical simple-eigenvalue hypothesis (source: pp. 12-13).
- For $D_4$ the Hölder exponent is 0.55 (source: p. 10).

## The contest

- JPEG is Fourier-based, using 8 by 8 blocks of the discrete cosine transform. For fingerprints, the FBI archive has more than 30 million cards, about $10^7$ bytes each, with a 20:1 compression goal; the blocks break ridges, and wavelet methods compete (source: §6, p. 15).
- Video and HDTV compression targets are about 100:1; the paper gives the bit rates and says the standards were still undecided in 1992 (source: p. 16).

## Wiki note

Wavelets trade Fourier's perfect frequency localisation for space-time localisation. See [[Wavelet transform]] for the hub and [[Fourier transform]], [[FFT]], [[Convolution]] for the Fourier side.

**Sources**: Strang PDF (pp. 1-16).
**Last updated**: 2026-11-06

---

## Related pages
- [[Wavelet transform]]
- [[Fourier transform]]
- [[FFT]]
- [[DFT]]
- [[Convolution]]
- [[Digital filter]]
