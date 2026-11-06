from authors import split_names
from refs import matches

ddpm = dict(first="ho", title="DDPM Denoising diffusion probabilistic models", year="2020", file="x.pdf")
assert matches("Jonathan Ho, Ajay Jain, and Pieter Abbeel. Denoising diffusion probabilistic models. NeurIPS 2020", ddpm, "")
assert not matches("Alex Nichol and Prafulla Dhariwal. Improved denoising diffusion probabilistic models. 2021", ddpm, "")
assert not matches("Tero Karras, Samuli Laine. A style-based generator architecture. 2019", dict(first="kingma", title="Auto-encoding variational Bayes", year="2014", file="x.pdf"), "")

assert split_names("Max Welling and Yee Whye Teh (equal contribution)") == ["Max Welling", "Yee Whye Teh"]
assert split_names("A. Smith, B. Jones, et al.") == ["A. Smith", "B. Jones"]
assert split_names("Ben Mildenhall et al.") == ["Ben Mildenhall"]
glorot = dict(first="glorot", title="Glorot init", year="2010", file="papers/ML/Glorot, Bengio - Understanding the Difficulty of Training DFFNN.pdf")
assert matches("Xavier Glorot and Yoshua Bengio. Understanding the difficulty of training deep feedforward neural networks. AISTATS 2010", glorot, "")
odes = dict(first="chen", title="Neural ODEs", year="2018", file="P/Chen, Rubanova, Bettencourt, Duvenaud - Neural ODEs.pdf")
assert not matches("Nanxin Chen, Yu Zhang, Heiga Zen. WaveGrad: Estimating gradients for waveform generation. 2021", odes, "")
print("ok")
