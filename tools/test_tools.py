import tempfile

import fitz

from letter import convert, fingerprint, status
from authors import firsts, norm, split_names
from inbox import best_wanted, existing, filename, ref_surnames
from refs import matches, software, words

ddpm = dict(first="ho", title="DDPM Denoising diffusion probabilistic models", year="2020", file="x.pdf")
assert matches("Jonathan Ho, Ajay Jain, and Pieter Abbeel. Denoising diffusion probabilistic models. NeurIPS 2020", ddpm, "")
assert not matches("Alex Nichol and Prafulla Dhariwal. Improved denoising diffusion probabilistic models. 2021", ddpm, "")
assert not matches("Tero Karras, Samuli Laine. A style-based generator architecture. 2019", dict(first="kingma", title="Auto-encoding variational Bayes", year="2014", file="x.pdf"), "")

assert split_names("Max Welling and Yee Whye Teh (equal contribution)") == ["Max Welling", "Yee Whye Teh"]
assert split_names("A. Smith, B. Jones, et al.") == ["A. Smith", "B. Jones"]
assert split_names("Ben Mildenhall et al.") == ["Ben Mildenhall"]

zs = firsts(["Qi Zhang", "Qinsheng Zhang", "Yang Song"])
assert norm("Qi Zhang", zs) != norm("Qinsheng Zhang", zs)
assert norm("Y. Song", zs) == norm("Song", zs) == ("song", "yang")
assert norm("Q. Zhang", zs) == ("zhang", "q")
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
assert software("[35] James Bradbury, Roy Frostig. JAX: compos- able transformations of Python+NumPy programs, 2018.") == "JAX"
assert software("Fabian Pedregosa et al. Scikit- learn: Machine Learning in Python. JMLR 2011.") == "scikit-learn"
assert software("Shashank Vadyala. Physics-informed neural network method for advection using pytorch. Array 2022.") is None
with tempfile.TemporaryDirectory() as t:
    a4 = fitz.open()
    for _ in range(2):
        a4.new_page(width=595, height=842).insert_text((72, 72), "Letter test")
    a4[0].insert_image(fitz.Rect(100, 100, 200, 200), pixmap=fitz.Pixmap(fitz.csRGB, fitz.IRect(0, 0, 4, 4), 1))
    a4[0].insert_link(dict(kind=fitz.LINK_URI, uri="https://example.org", **{"from": fitz.Rect(72, 60, 150, 80)}))
    a4[0].insert_link(dict(kind=fitz.LINK_GOTO, page=1, to=fitz.Point(72, 72), **{"from": fitz.Rect(72, 300, 150, 320)}))
    a4.save(f"{t}/a4.pdf", deflate=True)
    convert(f"{t}/a4.pdf", f"{t}/letter.pdf")
    with fitz.open(f"{t}/a4.pdf") as a, fitz.open(f"{t}/letter.pdf") as b:
        assert status(a) == "convert" and status(b) == "letter"
        assert fingerprint(a) == fingerprint(b) and len(fingerprint(b)[2]) == 2
print("ok")
