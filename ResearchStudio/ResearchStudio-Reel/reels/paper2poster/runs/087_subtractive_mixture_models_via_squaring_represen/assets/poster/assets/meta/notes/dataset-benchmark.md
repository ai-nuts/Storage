# Dataset / Benchmark

Core claim: Evaluation spans 2D synthetic continuous and discrete densities, five UCI multivariate datasets (Power, Gas, Hepmass, MiniBooNE, BSDS300), and distillation of sentences sampled from the GPT2 language model.

Supporting detail: Baselines include full-covariance Gaussian, normalizing flows (RealNVP, MADE, MAF, NSF), monotonic PCs (EiNet-LRS), and tensor-train density estimators (TTDE).

Narration: The experiments cover three regimes. First, two-dimensional synthetic densities, both continuous and discrete, where you can literally see how well each model captures rings and other holey shapes. Second, five standard UCI datasets: Power, Gas, Hepmass, MiniBooNE, and BSDS300. And third, distilling sentences sampled from the GPT2 language model. Baselines span full-covariance Gaussians, normalizing flows like RealNVP, MADE, MAF and NSF, monotonic probabilistic circuits, and tensor-train density estimators.
