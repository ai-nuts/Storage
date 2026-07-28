# Method

Core claim: Instead of simulating the latent SDE per datapoint, ALD defines a deterministic encoder f(x;φ) and runs a Langevin SDE on its parameters φ; the encoder's outputs are taken directly as posterior samples. When the encoder has the form f(x;Φ)=Φg(x) with a fixed feature extractor and a trainable last linear layer whose width exceeds the batch size, Theorem 1 guarantees the induced latent samples converge to the true posterior. The LAE trains a decoder by running T ALD steps on the encoder's last layer before each parameter update, with an optional Metropolis-Hastings rejection step to remove discretization error.

Supporting detail: ALD amortizes MCMC across all data through the shared encoder, so a warmed-up encoder can also accelerate sampling for new test data.

Narration: The key idea: move randomness from latent space to encoder parameters. A deterministic encoder maps observations to latents, and Langevin dynamics runs on its parameters, whose outputs become posterior samples. Convergence is guaranteed when a fixed feature extractor feeds a trainable linear layer exceeding the batch size. The autoencoder runs a few steps before each decoder update, with optional Metropolis-Hastings correction.
