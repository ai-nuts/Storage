# Contribution

Core claim: The paper adapts Score-based Likelihood Characterization (SLIC) to gravitational waves: a score-based diffusion model learns the empirical detector-noise distribution, which is combined with a differentiable waveform model to form an unbiased likelihood for parameter estimation.

Supporting detail: It demonstrates end-to-end that the learned model reproduces real LIGO noise (including fine spectral lines) and recovers true injected source parameters, validating the framework on real detector data.

Narration: The core contribution brings Score-based Likelihood Characterization, or SLIC, to gravitational waves. Originally developed for astronomical imaging, it learns the score of the noise distribution with a diffusion model instead of assuming its form. Coupled with a differentiable waveform, it yields an unbiased likelihood. They show it both generates realistic LIGO noise and recovers the true parameters of an injected signal.
