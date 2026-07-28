# Motivation

Core claim: Amortized variational inference (the VAE) is efficient because an encoder predicts latents for all data, but its accuracy is capped by the tractable variational family; MCMC is flexible yet has never been truly amortized.

Supporting detail: Prior encoder-plus-MCMC hybrids (e.g. Hoffman 2017) only use the encoder to initialize sampling, so they still pay for datapoint-wise Langevin iterations at train and test time.

Narration: Variational inference dominates thanks to amortization: a shared encoder predicts the latents for all data, like the variational autoencoder. But it relies on tractable Gaussians, limiting accuracy. MCMC has no such limit, yet nobody truly amortized it; earlier hybrids only warm-started per-datapoint chains. The goal: amortized efficiency with MCMC flexibility.
