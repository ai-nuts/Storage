# Dataset / Benchmark

Core claim: Generalization is evaluated by kernel regression with the TNTK on 90 real-world datasets, compared against the MLP-induced NTK and the RBF kernel. Convergence and dynamics are also studied on synthetic inputs.

Supporting detail: For timing, a synthetic dataset of 300 samples with 10 i.i.d. Gaussian features is used; tree depth is tuned from d = 1 to 29 and the split-hardness α is swept from 0.5 to 64.

Narration: The empirical study uses two kinds of data. For generalization, the authors run kernel regression with the Tree NTK on ninety real-world datasets, comparing against the kernel of an infinitely wide multi-layer perceptron and the classic radial basis function kernel. Tree depth is tuned from one up to twenty-nine, and the split-hardness parameter alpha is swept widely. For measuring computational cost, they use a synthetic dataset of three hundred samples with ten Gaussian features.
