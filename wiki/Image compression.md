---
type: concept
area: dsp
source-ref: "ECE 438 Topic IP.6; Reibman DL 08 slides"
tags: [signals]
---

# Image compression

**Summary**: Reducing the bits needed for an image through entropy coding, prediction and transform coding, with fidelity judged by metrics such as MSE and PSNR. The Reibman slides show why PSNR alone is a poor guide to visual quality.

## Redundancy and rate
Compression ratio and the three redundancies it targets (source: Topic IP.6, pp. 1-4, Fig. 8.1):
- Coding redundancy: more bits per symbol than needed (8 bits when only 4 values occur).
- Spatial and temporal redundancy: neighbouring pixels and successive frames are correlated.
- Irrelevant information: details the human visual system does not perceive can be dropped.

> [!definition] Compression ratio, redundancy, average length
> $$C=b/b',\qquad R=1-1/C$$
> with $b,b'$ the bit counts before and after (written 10:1 etc.). For codeword lengths $l(r_k)$ and symbol pmf $p_r$:
> $$L_{avg}=\sum_{k=0}^{L-1}l(r_k)\,p_r(r_k)$$
>
> (source: Topic IP.6, pp. 2, 6)

> [!example] Typical sizes
> A 3024 x 4032 colour image is about 36.6 million bytes; down-sampling by 4 per axis (with a pre-filter, see [[Aliasing]]) and dropping 3 bit planes leaves about 1.43 million bytes (IP.6, p. 4).

## Entropy and Huffman coding
> [!definition] Information and entropy
> $$I(E)=\log\frac1{P(E)}=-\log P(E)$$
> in nats (natural log) or bits ($\log_2$); zero if $P(E)\in\{0,1\}$ and peaking at 1 bit at $P=\tfrac12$ for a binary event. Entropy is the average information per source output:
> $$H=-\sum_{i=1}^{n}P(a_i)\log P(a_i)$$
> For an image estimate it from the normalised histogram ([[Histogram equalization]]):
> $$\tilde H=-\sum_{i=0}^{L-1}p_r(r_i)\log p_r(r_i)$$
>
> (source: Topic IP.6, pp. 8-9; L36 Apr 23, 2025.pdf, p. 1)

> [!theorem] Shannon's noiseless coding theorem
> Entropy is a lower bound on the bits needed for a memoryless source, and can be approached by coding ever longer blocks of symbols (limited by complexity). If pixels are correlated the memoryless model fails and fewer bits than the memoryless entropy are possible.
>
> (source: Topic IP.6, pp. 9-10; L36, p. 1)

> [!algorithm] Huffman coding (1952)
> Codes symbols one at a time (pixels, transform coefficients, run lengths). A fixed number of symbols maps to a variable number of bits.
> 1. Sort $P(a_i)$ in descending order.
> 2. Merge the two least frequent; repeat until all are merged.
> 3. Label lower branches 0 and upper branches 1.
> 4. Read each codeword from the root to the symbol.
> The result is a prefix code (no codeword is a prefix of another), often implemented as a look-up table. Golomb codes suit exponentially decaying probabilities; arithmetic coding suits unknown sources.
>
> (source: Topic IP.6, p. 11; L35 Apr 21, 2025.pdf, p. 1)

> [!example] Variable-length code
> Values 87, 128, 186, 255 with probabilities 0.25, 0.47, 0.25, 0.03 get codes 01, 1, 000, 001:
> $$L_{avg}=1(0.47)+2(0.25)+3(0.28)=1.81\ \text{bpp}$$
> a ratio of $8/1.81=4.42$ against 8 bits and $2/1.81=1.10$ against a 2-bit code. The entropy as written is 1.6614 bpp, so the code sits above the bound.
>
> (source: Topic IP.6, pp. 6-7)

> [!example] Huffman tree, six symbols
> Probabilities 0.4, 0.3, 0.1, 0.1, 0.06, 0.04 get codewords 0, 10, 110, 1110, 11110, 11111 (lengths 1, 2, 3, 4, 5, 5). The slide states 2.14 bpp. Wiki note: the weighted lengths sum to 2.2 bpp, not 2.14.
>
> (source: Topic IP.6, p. 12)

> [!example] Joining symbols
> $P(a_1)=0.8$, $P(a_2)=0.2$: the best one-symbol code is 1 bit. Pairing gives $b_1..b_4$ with probabilities 0.64, 0.16, 0.16, 0.04 and codewords 1, 01, 001, 000: 1.56 bits per 2 symbols, 0.78 bit/symbol. Entropy is 0.72 bit/symbol; three-symbol blocks reach 0.728. One cannot beat entropy.
>
> (source: Topic IP.6, p. 13)

## Predictive coding
> [!definition] Spatial prediction
> $$\hat f(m,n)=\mathrm{round}\Big[\sum_i\alpha_if(m_i,n_i)\Big]$$
> over a causal neighbourhood $N(m,n)$ so the decoder has the same pixels; $N$ pixels make an $N$-th order predictor. The simplest predictor is $\hat x_i=\tilde x_{i-1}$. The encoder sends the quantised error $Q(x_i-\hat x_i)=e_i$ and both sides reconstruct
> $$\tilde x_i=\hat x_i+Q(x_i-\hat x_i)$$
> The decoder adds $e_i$ to the prediction from the same predictor and delay. Quantisation error is $\Delta^2/12$ with $\Delta=\text{range}/2^b$, so a smaller error variance allows a smaller range and finer $\Delta$ at the same $b$ (see [[Quantization]]). Fig. 8.30 is the lossless model (no quantiser); Fig. 8.31: prediction error cuts entropy from 7.25 to 3.89 as printed.
>
> (source: Topic IP.6, pp. 17-20; L37 Apr 25, 2025.pdf, p. 1)

## Block transform coding and JPEG
> [!algorithm] Block-based transform coding
> Divide the image into non-overlapping square blocks, apply an invertible 2D transform ([[Image transforms]]), quantise and encode the coefficients; decode by inverse quantising, inverse transforming and storing the blocks back. It works when the transform packs information into a few strong coefficients and decorrelates them. Design choices: the transform (DCT: good compaction and decorrelation), block size (8x8 typical), per-coefficient quantiser size (bit allocation) and codebook. Blocks are used because images are not stationary and they localise quantisation error. Keeping few coefficients is the best-approximation idea from the [[DFT]].
>
> (source: Topic IP.6, p. 22)

Bit allocation (IP.6, p. 23): zonal coding assigns bits by expected coefficient energy (for $N=8$ the DCT puts 79% of the energy in DC and 0.6% in the last coefficient; needs known statistics); threshold coding sends only coefficients above a threshold and uses run-length coding to mark their positions; it can adapt at image, block or coefficient level. The variance of DCT coefficients on a log scale falls steeply along the zigzag index, low horizontal and vertical frequencies coming first (Yao Wang slide, L37 p. 3). The contrast sensitivity curve (chirp image) shows the eye is most sensitive at mid frequencies (L37, p. 5).

> [!algorithm] JPEG pipeline (8x8 block)
> DCT (spatial redundancy), zigzag scan (2D to 1D), quantisation (irrelevancy reduction, step sizes shaped by a perceptual matrix), run-length encoding, Huffman code (coding redundancy), bitstream. This is the core of many image and video standards.
>
> (source: Topic IP.6, pp. 5, 24-25; L35, p. 1)

> [!example] Run-length coding
> Zigzagged quantised DCT coefficients map to (zeros-run, value) pairs ending in EOB: $[5\,0\,0\,2\,3\,0\,0\,4\,\dots]$ becomes $5,(2,2),(0,3),(2,4),(6,1),\mathrm{EOB}$ (pp. 25-26). The bit string 0000 1 00 11 000 111 00 becomes runs 4, 1, 2, 2, 3, 3, 2, which can then be Huffman coded (p. 27).

Standards define only decoder behaviour for a well-formed bitstream (p. 28). Fig. 8.6 and Tables 8.3-8.5 list JPEG, JPEG-LS, JPEG-2000, H.261-H.265, MPEG and formats such as PNG and WebP (pp. 29-31); the margin note says H.266 (VVC) was finalised in July 2020. JPEG-2000 replaces the DCT with a wavelet transform: see [[Wavelet transform]]. DFT overcompleteness versus the real, complete DCT, Hadamard and Haar are on [[Image transforms]] (L34, p. 1).

## Fidelity
> [!definition] Objective fidelity metrics
> With error $e(m,n)=f(m,n)-\hat f(m,n)$:
> $$\mathrm{MSE}=\frac1{MN}\sum_m\sum_ne(m,n)^2,\qquad e_{rms}=\sqrt{\mathrm{MSE}}$$
> $$\mathrm{PSNR}=10\log_{10}\frac{\max(f^2)}{\mathrm{MSE}}=10\log_{10}\frac{L^2}{\mathrm{MSE}}$$
> $L=256$ for 8-bit images. Rules of thumb: 40 dB is each pixel off by 1%, 30 dB by 3.2%, 20 dB by 10%. These metrics are pixel-based: they ignore spatial correlation of the error and cannot measure enhancement or resolution effects.
>
> (source: Topic IP.6, pp. 14-16)

PSNR and MSE work reasonably when comparing one image compressed by different amounts with the same algorithm, and worse across different content or artifact types (L37, p. 1). SSIM is a weighted MSE that also accounts for darkening or lightening, with a luminance term (means), a contrast term (variances) and a structure term (normalised signals). The first two have the form $\frac{2ab+\epsilon}{a^2+b^2+\epsilon}$ (means $\bar f_1,\bar f_2$ or deviations $\sigma_1,\sigma_2$) and the structure term is $\frac{s_{xy}+\epsilon_3}{s_xs_y+\epsilon_3}$ (IP.6, p. 17). Fidelity is not quality; subjective quality is not treated (pp. 12-13).

## Reibman examples: why PSNR is not enough
> [!example] PSNR versus rate, JPEG-2000, two test images
> Plot of PSNR against bits per pixel (axis 0 to 0.1) for "Harbor" and "Bridge". Harbor rises from about 25 dB at the lowest rate to about 39 dB at 0.1 bpp; Bridge from about 19 dB to about 29 dB. Values read off the plot, except the labelled ones: Harbor 25.35 dB (lowest rate) and 34.61 dB (0.05 bpp); Bridge 19.09 dB and 25.25 dB at the same two rates. The same codec gives much lower PSNR on the texture-rich Bridge image.
>
> (source: reibman_purdue08-examples.pdf, pp. 1-6, slides "PSNR for image encoding: JPEG-2000")

> [!example] Why not PSNR: shift, and equal PSNR on unlike images
> Example 1: a 2-pixel shifted copy of the Harbor image has a relative PSNR of 20.11 dB, though the two look identical (pp. 7-8). Example 4: a resized version of Harbor is also shown against the original (pp. 9-10). Example 5: a heavily blurred Harbor at 25.36 dB and a good-looking Bridge at 25.25 dB have almost equal PSNR but very different quality (p. 11).
>
> (source: reibman_purdue08-examples.pdf, pp. 7-11)

Lesson: PSNR compares pixels, so it penalises harmless geometric changes and is content-dependent. Wiki note: the slide text gives no explanation for example 4 beyond the images; the reading of the resizing is mine. **[unverified]**



**Covered in**: ECE 438 IP.6, L34-L37 (Digital Signal Processing/Topic IP.6 Image compression Apr 23, 2025.pdf); Reibman examples
**Sources**: `Digital Signal Processing/Topic IP.6 Image compression Apr 23, 2025.pdf`, `Digital Signal Processing/reibman_purdue08-examples.pdf`, `Digital Signal Processing/front page/L34 Apr 18, 2025.pdf`, `Digital Signal Processing/front page/L35 Apr 21, 2025.pdf`, `Digital Signal Processing/front page/L36 Apr 23, 2025.pdf`, `Digital Signal Processing/front page/L37 Apr 25, 2025.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Quantization]] · [[DFT]] · [[Wavelet transform]] · [[Histogram equalization]] · [[Principal component analysis]] · [[Karhunen-Loève expansion]] · [[Image transforms]] · [[Aliasing]]
