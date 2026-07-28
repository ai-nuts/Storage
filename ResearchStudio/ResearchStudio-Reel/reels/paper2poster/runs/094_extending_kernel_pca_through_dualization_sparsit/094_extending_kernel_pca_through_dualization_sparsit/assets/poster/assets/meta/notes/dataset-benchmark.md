# Dataset / Benchmark

Core claim: Efficiency is measured on Synth 1 (n=7000), Protein (n=14895), RCV1 (n=20242), and CIFAR-10 (n=60000); robustness on a contaminated Iris dataset; sparsity via reconstruction error under ℓ²_ε and ℓ^∞_ε losses.

Supporting detail: Solvers are compared using a relative dual-cost residual stopping criterion at tolerances δ = 10⁻² and 10⁻⁴; a Laplace kernel is used for the timing study, a Gaussian kernel for the robustness study, and results are averaged over 5 runs.

Narration: The experiments span synthetic and real-world data. For efficiency, the authors time Kernel PCA on a synthetic 7,000-point problem, the Protein dataset with about 15,000 points, the RCV1 text collection with roughly 20,000 points, and CIFAR-10 with 60,000 images. Robustness is tested by artificially contaminating the Iris dataset with multiplicative Gaussian outliers, and sparsity is measured through reconstruction error under epsilon-insensitive losses. All solvers are compared fairly using a shared relative dual-cost residual as the stopping criterion at two tolerance levels, and the timing results are averaged over five runs.
