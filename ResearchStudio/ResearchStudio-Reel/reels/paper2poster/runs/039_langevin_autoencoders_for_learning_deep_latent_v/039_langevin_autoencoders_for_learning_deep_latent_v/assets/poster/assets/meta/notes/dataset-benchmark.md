# Dataset / Benchmark

Core claim: Toy studies use a conjugate bivariate-Gaussian latent-variable model and a neural-network (neural-likelihood) posterior; image generation is evaluated on MNIST, SVHN, CIFAR-10, and CelebA.

Supporting detail: All methods share the same fully-connected networks; test performance is measured by the negative evidence lower bound (ELBO) per data dimension over three seeds.

Narration: Validation comes in two stages. First, toy problems with known answers: a conjugate bivariate-Gaussian posterior, and a harder posterior from a random network. Then image generation on MNIST, S-V-H-N, CIFAR-10, and CelebA, with shared architectures, quality measured by negative ELBO per dimension over three seeds.
