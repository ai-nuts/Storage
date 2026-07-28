# Dataset / Benchmark

Core claim: Validation is on two synthetic finite-rank kernels: the truncated Neural Tangent Kernel (tNTK) and a low-rank kernel (LK), with KRR run over a range of sample sizes N (about 10 to 200) and ridge values, repeated over 10 random trials.

Supporting detail: No natural-image dataset is used; the paper is theoretical and uses controlled kernels where the eigenspectrum and target decomposition are known, so the bounds can be checked directly against measured test error.

Narration: Being a theory paper, the experiments use controlled synthetic settings. The authors test two finite-rank kernels: a truncated neural tangent kernel and a constructed low-rank kernel. For each they sweep sample sizes from ten to two hundred and many ridge values, averaging ten trials with median and quartile bars.
