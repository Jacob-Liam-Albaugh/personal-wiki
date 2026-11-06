---
type: lecture
area: dsp
source-ref: "Digital Signal Processing/Topic IP.6 Image compression Apr 23, 2025.pdf (ECE 438 handwritten slides, Gonzalez ch. 8, Yao Wang 2003)"
course: ece438
lecture: IP.6
tags: [signals]
---

# ECE438 IP.6 - Image compression

**Summary**: Three kinds of data redundancy (coding, spatial/temporal, irrelevant), entropy and Huffman coding, predictive coding, fidelity metrics (MSE, PSNR, SSIM), and the JPEG pipeline of DCT, zigzag, quantisation, run-length and Huffman.

**File**: `Digital Signal Processing/Topic IP.6 Image compression Apr 23, 2025.pdf`

---

## Topics
- Compression ratio, redundancy, and the three redundancy categories (source: Topic IP.6 Image compression Apr 23, 2025.pdf, p. 1-4).
- Variable-length coding; information and entropy; Shannon's noiseless coding theorem (p. 7-10).
- Huffman coding; joining symbols (p. 11-12).
- Fidelity metrics (p. 13-17).
- Predictive coding (p. 17-21).
- Block transform coding, bit allocation, JPEG, run-length coding, standards (p. 22-32).

## Key results

> [!definition] Compression ratio and redundancy
> $$C = b/b'$$
> $b$ and $b'$ are bit counts before and after compression (written 10:1 etc.).
> $$R = 1 - 1/C$$
> is the data redundancy of the original representation (p. 2).

Three categories, all targetable (p. 2-4; Fig. 8.1):
- Coding redundancy: more bits per symbol than needed (e.g. 8 bits when only 4 values occur).
- Spatial and temporal redundancy: neighbouring pixels, or successive frames, are correlated.
- Irrelevant information: details the human visual system does not perceive can be dropped.

> [!definition] Average code length
> $$L_{avg} = \sum_{k=0}^{L-1} l(r_k)\,p_r(r_k)$$
> $l(r_k)$ is the codeword length and $p_r$ the pmf of the symbols (p. 6).

> [!definition] Information and entropy
> Information of an event with probability $P(E)$:
> $$I(E) = \log\frac{1}{P(E)} = -\log P(E)$$
> Units are nats for the natural log and bits for $\log_2$. It is 0 if $P(E)\in\{0,1\}$ and the slide plots $I(E)$ peaking at 1 bit when $P=\tfrac12$ (p. 8).
> Entropy is the average information per source output:
> $$H = -\sum_{i=1}^{n} P(a_i)\log P(a_i)$$
> For an image, estimate with the normalised histogram:
> $$\tilde H = -\sum_{i=0}^{L-1} p_r(r_i)\log p_r(r_i)$$
> (p. 9).

> [!theorem] Shannon's noiseless coding theorem
> Entropy is a lower bound on the bits needed for a memoryless source.
> It can be approached by coding blocks of symbols together, in the limit of infinitely long blocks; complexity limits this in practice (p. 9-10).
> If pixels are correlated, the memoryless model no longer holds and fewer bits than the memoryless entropy are possible (p. 10).

> [!algorithm] Huffman coding (1952)
> Codes symbols one at a time; applies to pixels, transform coefficients, run lengths, etc.
> 1. Sort $P(a_i)$ in descending order.
> 2. Merge the two least frequent, and repeat until all are merged.
> 3. Label lower branches 0 and upper branches 1.
> 4. Read each codeword from the tree root to the symbol.
> The result is a prefix code: no codeword is a prefix of another. Often implemented as a look-up table (p. 11).
> Others: Golomb codes for exponentially decaying probabilities, arithmetic coding for unknown sources (p. 11).

> [!definition] Predictive coding
> $$\hat f(m,n) = \mathrm{round}\Big[\sum_i \alpha_i\,f(m_i,n_i)\Big]$$
> over a neighbourhood $N(m,n)$. The neighbourhood should be causal, so the decoder has the same pixels. With $N$ pixels it is an $N$-th order predictor (p. 17).
> Simplest predictor: $\hat x_i = \tilde x_{i-1}$. The encoder sends the quantised error $Q(x_i-\hat x_i)=e_i$, and encoder and decoder reconstruct
> $$\tilde x_i = \hat x_i + Q(x_i-\hat x_i)$$
> (p. 18).
> Quantisation error is $\Delta^2/12$ with $\Delta=\text{range}/2^b$, so smaller error variance means smaller range and smaller $\Delta$ for the same $b$ (p. 19).
> Fig. 8.30 is the lossless model (no quantiser). Fig. 8.31: prediction error cuts the entropy (from 7.25 to 3.89 as printed) (p. 20).

> [!definition] Objective fidelity metrics
> With error $e(m,n)=f(m,n)-\hat f(m,n)$:
> $$\mathrm{MSE} = \frac{1}{MN}\sum_m\sum_n e(m,n)^2$$
> $$e_{rms} = \sqrt{\mathrm{MSE}}$$
> $$\mathrm{PSNR} = 10\log_{10}\frac{\max(f^2)}{\mathrm{MSE}} = 10\log_{10}\frac{L^2}{\mathrm{MSE}}$$
> $L=256$ for 8-bit images. A mean-squared SNR is also given but not commonly used for images (p. 14).
> Rules of thumb: 40 dB is each pixel off by 1%, 30 dB by 3.2%, 20 dB by 10% (p. 15).
> These are pixel-based: they ignore spatial correlation of the error, cannot measure enhancement, and cannot measure resolution effects (p. 15-16).

SSIM is a weighted MSE that also accounts for darkening or lightening. It has a luminance term (means), a contrast term (variances) and a structure term (normalised signals). Each term has the form $\frac{2\,a\,b+\epsilon}{a^2+b^2+\epsilon}$ (luminance with means $\bar f_1,\bar f_2$, contrast with $\sigma_1,\sigma_2$), and the structure term is $\frac{s_{xy}+\epsilon_3}{s_xs_y+\epsilon_3}$ (p. 17).
Fidelity is not the same as quality; subjective quality is not treated (p. 12-13).

> [!algorithm] Block-based transform coding
> Divide the image into non-overlapping square blocks, apply an invertible 2-D transform, quantise and encode the coefficients, then decode, inverse quantise, inverse transform and store the blocks back (p. 22).
> It works when the transform packs the pixel information into a few strong coefficients and decorrelates them.
> Design choices: the transform (DCT: good compaction and decorrelation), block size (8x8 typical), quantiser size per coefficient (bit allocation), and codebook.
> Blocks are used because images are not stationary, and it localises quantisation errors.
> Bit allocation (p. 23): zonal coding assigns bits by expected coefficient energy (for $N=8$ the DCT puts 79% of the energy in DC and 0.6% in the last coefficient; assumes known statistics); threshold coding sends only coefficients above a threshold, with run-length coding to mark their locations; it adapts at image, block or coefficient level.

JPEG pipeline (p. 5, 24-25): 8x8 block, DCT (spatial redundancy), zigzag scan (2-D to 1-D), quantisation (irrelevancy reduction; step sizes aligned with the visual system via a perceptual matrix), run-length encoding, Huffman code, channel. This is the core method behind many image and video standards.
Run-length coding for transform images maps the zigzagged quantised DCT coefficients to (zeros-run, value) pairs ending in EOB. Example: coefficients $[5\,0\,0\,2\,3\,0\,0\,4\,\dots]$ become $5,(2,2),(0,3),(2,4),(6,1),\mathrm{EOB}$ (p. 25-26).

## Examples

> [!example] Variable-length code (p. 6-7)
> Four values 87, 128, 186, 255 with probabilities 0.25, 0.47, 0.25, 0.03 get codes 01, 1, 000, 001.
> $$L_{avg} = 1(0.47)+2(0.25)+3(0.28) = 1.81\ \text{bpp}$$
> That is $8/1.81=4.42$ relative to 8 bits and $2/1.81=1.10$ relative to a 2-bit code. The entropy is $1.6614$ bpp as written, so the code is above the bound.

> [!example] Huffman tree, six symbols (p. 12)
> Probabilities 0.4, 0.3, 0.1, 0.1, 0.06, 0.04 get codewords 0, 10, 110, 1110, 11110, 11111 (lengths 1, 2, 3, 4, 5, 5). The slide states 2.14 bpp.
> Wiki note: the weighted lengths sum to 2.2 bpp, not 2.14; flagged in the report.

> [!example] Joining symbols (p. 13)
> $P(a_1)=0.8$, $P(a_2)=0.2$: best one-symbol code is 1 bit. Pair them: $b_1..b_4$ with probabilities 0.64, 0.16, 0.16, 0.04 and codewords 1, 01, 001, 000 give 1.56 bits per 2 symbols, 0.78 bit/symbol. Entropy is 0.72 bit/symbol; three-symbol blocks reach 0.728; one cannot beat entropy.

> [!example] Typical sizes (p. 4)
> A 3024 x 4032 colour image is about 36.6 million bytes; down-sampling by 4 in each direction (with a pre-filter) and dropping 3 bit planes gives about 1.43 million bytes.

> [!example] Run-length (p. 27)
> The bit string 0000 1 00 11 000 111 00 becomes runs of 4, 1, 2, 2, 3, 3, 2; the run values can then be Huffman coded.

## Connections
- Compaction by the DCT is from [[ECE438 IP.5 - Image transforms and wavelets]]; quantisation is [[Quantization]] ([[ECE438 DSP.5 - Quantization]]).
- Down-sampling with a pre-filter avoids [[Aliasing]] ([[ECE438 IP.2 - Aliasing]]).
- The histogram as pmf is from [[ECE438 IP.4.A - Histograms]].
- JPEG-2000 uses a wavelet transform: see [[Wavelet transform]] and [[ECE438 IP.7 - Multiresolution image processing]].
- Standards define only the decoder behaviour for a well-formed bitstream (p. 28); Fig. 8.6 and Tables 8.3-8.5 list JPEG, JPEG-LS, JPEG-2000, H.261-H.265, MPEG and formats such as PNG and WebP (p. 29-31). The margin note says H.266 (VVC) was finalised in July 2020.

**Sources**: Digital Signal Processing/Topic IP.6 Image compression Apr 23, 2025.pdf
**Last updated**: 2026-11-06

---

## Related pages
[[ECE438 IP.5 - Image transforms and wavelets]] | [[ECE438 IP.7 - Multiresolution image processing]] | [[ECE438 IP.4.A - Histograms]] | [[Quantization]] | [[Aliasing]] | [[DFT]] | [[Wavelet transform]]
