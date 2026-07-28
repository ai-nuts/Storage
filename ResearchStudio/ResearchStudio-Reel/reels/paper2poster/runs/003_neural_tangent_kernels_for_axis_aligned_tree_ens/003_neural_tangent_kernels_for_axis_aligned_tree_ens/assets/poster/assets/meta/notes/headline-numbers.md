# Headline Numbers

Core claim: - TNTK beats the MLP-induced NTK on more than 30% of the 90 real-world datasets. - Peak dataset-wise win rate 34.9% (α = 32) vs 11.8% for the RBF kernel. - Kernel cost is independent of tree depth d (vs linear-in-depth for the MLP-induced NTK). - Evaluated across depths d = 1 to 29 on 90 datasets.

Supporting detail: Win rate rises monotonically from 13.6% (α = 0.5) to the 32–34.9% range for hard splits.

Narration: A few numbers capture the impact. Across ninety real-world datasets, the tree kernel beats the multi-layer perceptron kernel on more than thirty percent, peaking near thirty-five percent when splits are hard, versus under twelve percent for the radial basis function kernel. Most striking, the tree kernel's cost is independent of tree depth, while the MLP kernel scales linearly. The depths studied span one to twenty-nine.
