from authors import split_names
from inbox import best_wanted, existing, filename, ref_surnames
from refs import matches, words

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
assert ref_surnames("Bethany Lusch, J Nathan Kutz, and Steven L Brunton. Deep learning for universal linear embeddings.") == ["Lusch", "Kutz", "Brunton"]
assert ref_surnames("Kingma, D. P. and Welling, M. Auto-encoding variational Bayes. ICLR 2014.") == ["Kingma", "Welling"]
assert filename(["Ho", "Jain", "Abbeel"], "Denoising: diffusion?") == "Ho, Jain, Abbeel - Denoising diffusion.pdf"
assert filename(list("abcde"), "T").startswith("a et al - ")
alex = dict(sur="krizhevsky", by=["A", "B"], ws=words("Alex Krizhevsky, Ilya Sutskever. Imagenet classification with deep convolutional neural networks. NeurIPS 2012"))
assert best_wanted("ImageNet Classification with Deep Convolutional Neural Networks", "Alex Krizhevsky University of Toronto", [alex])
assert not best_wanted("Deep Residual Learning for Image Recognition", "Kaiming He ... Krizhevsky", [alex])
known = [("papers/Diffusion/x.pdf", words("Score-Based Generative Modeling through Stochastic Differential Equations"))]
assert existing("SCORE-BASED GENERATIVE MODELING STOCHASTIC DIFFERENTIAL EQUATIONS", known)
assert not existing("Generative Modeling by Estimating Gradients of the Data Distribution", known)
print("ok")
