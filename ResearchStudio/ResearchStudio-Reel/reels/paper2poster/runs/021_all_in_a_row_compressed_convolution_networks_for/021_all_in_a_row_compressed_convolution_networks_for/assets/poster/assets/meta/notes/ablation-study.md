# Ablation Study

Core claim: Increasing the number of learnable permutations steadily improves accuracy on MUTAG, Chameleon, Cornell and Wisconsin, and enlarging the diagonal-convolution kernel size and receptive field further boosts performance without degradation.

Supporting detail: A graph-reconstruction test with an autoencoder shows the relaxed permutations cause almost no information loss even at moderate relaxation factors, confirming the regularization is nearly lossless.

Narration: Several ablations show why CoCN works. First, permutation heads matter: with more permutations, accuracy rises consistently on MUTAG, Chameleon, Cornell, and Wisconsin, since each exposes different node arrangements. Second, larger diagonal kernels give a bigger receptive field and better performance, without over-smoothing. Third, an information-loss study finds the relaxed permutations preserve almost all information, so the regularization is lossless.
