# Key Result

Core claim: The LAE consistently achieves the best (lowest) negative ELBO per dimension on all four image datasets, beating the VAE, VAE-flow, and Hoffman (2017), showing that ALD's more accurate posterior sampling yields better DLVM training.

Supporting detail: On toy posteriors, ALD captures multimodal, correlated posteriors that mean-field and full VI cannot, matching the ground-truth density.

Narration: On toy problems, amortized Langevin dynamics reproduces multimodal, correlated posteriors that variational inference misses. On images, the Langevin autoencoder achieves the lowest negative ELBO on all four datasets. The lesson: more accurate posterior sampling yields better generative models.
