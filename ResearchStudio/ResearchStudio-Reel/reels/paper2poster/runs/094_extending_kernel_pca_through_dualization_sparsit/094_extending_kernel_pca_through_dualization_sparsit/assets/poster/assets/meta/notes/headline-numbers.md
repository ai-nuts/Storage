# Headline Numbers

Core claim: - 9.17× speedup over randomized SVD on CIFAR-10 (n=60000) at tolerance δ = 10⁻² - ≥3× faster than randomized SVD on every task at δ = 10⁻² - O(s³) per-iteration SVD cost, replacing the classical O(n³) Gram-matrix SVD - 6.83 vs 7.59 MSE (Huber H²_κ vs squared loss) on contaminated Iris at τ=10

Supporting detail: Evaluated on datasets up to n = 60000; full SVD exceeded a 30-minute cap on RCV1 and CIFAR-10.

Narration: A few numbers capture the impact. On CIFAR-10 the method delivers a nine-point-one-seven times speedup over randomized SVD, and it is at least three times faster than randomized SVD on every efficiency task. The key complexity change is that each iteration costs order s-cubed for a small s-by-s singular value decomposition, replacing the classical order n-cubed decomposition of the full Gram matrix. On the robustness side, the Huber loss cuts the mean squared error on contaminated Iris from about seven-point-five-nine down to six-point-eight-three at the tested corruption level. And these results scale to datasets with sixty thousand points, where full SVD could not finish within thirty minutes.
