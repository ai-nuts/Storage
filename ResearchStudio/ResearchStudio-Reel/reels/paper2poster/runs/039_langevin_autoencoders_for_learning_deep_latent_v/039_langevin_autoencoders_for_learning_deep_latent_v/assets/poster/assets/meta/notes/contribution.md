# Contribution

Core claim: (1) Amortized Langevin Dynamics (ALD), which entirely replaces datapoint-wise MCMC with Langevin updates of an encoder's parameters, proven to keep the true posterior as its stationary distribution; (2) the Langevin Autoencoder (LAE), a deep latent-variable model realized as a small modification of a traditional autoencoder.

Supporting detail: Traditional Langevin dynamics is shown to be a special case of ALD, and the standard autoencoder is a special case of the LAE.

Narration: Two contributions. First, amortized Langevin dynamics: an MCMC algorithm that removes per-datapoint iterations by running Langevin updates on a shared encoder's parameters, proven to keep the true posterior stationary. Second, the Langevin autoencoder, a generative framework built on it that amounts to a small tweak of a standard autoencoder.
