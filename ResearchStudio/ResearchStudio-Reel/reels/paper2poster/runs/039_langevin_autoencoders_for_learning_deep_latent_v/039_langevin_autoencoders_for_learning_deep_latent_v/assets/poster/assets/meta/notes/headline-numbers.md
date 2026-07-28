# Headline Numbers

Core claim: - MNIST negative ELBO/dim: 1.177 (LAE) vs 1.189 (VAE) - CIFAR-10: 4.773 (LAE) vs 4.820 (VAE) - CelebA: 4.636 (LAE) vs 4.671 (VAE) - SVHN: 4.412 (LAE) vs 4.442 (VAE); LAE trains ~2.24× slower than VAE

Supporting detail: Only T = 2 ALD iterations are used in the image experiments; LAE and Hoffman (2017) have nearly identical training speed.

Narration: The gains are consistent but modest. On MNIST, negative ELBO drops to one point one seven seven per dimension, versus one point one eight nine for the VAE. CIFAR-10, CelebA, and S-V-H-N show similar small improvements. The cost: about two-and-a-quarter times slower than a VAE, but the same speed as the encoder-initialized Langevin baseline.
