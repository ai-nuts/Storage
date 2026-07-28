# Method

Core claim: Building on spin-weighted spherical CNNs, the authors introduce a phase collapse nonlinearity (which uses the modulus to collapse phase and recover rotation invariance), spectral batch normalization, spectral pooling, and an efficient residual block whose skip connection lives in Fourier space (Figure 2). Fourier transforms are computed as dense matrix multiplications (DFT) rather than FFTs for speed on TPUs.

Supporting detail: The complete rewrite in JAX runs distributed across up to 32 TPUs; molecules are encoded as sets of spherical functions built from physically-based, power-law interactions between atom pairs (Figure 3).

Narration: The method builds on spin-weighted spherical CNNs. Its centerpiece is a set of new components that all live in the spectral domain. A phase collapse nonlinearity takes the modulus of the features to collapse their phase, which restores rotation invariance while losing no information in the nonzero spins. Batch normalization and pooling are also moved into the spectral domain, and the residual block adds its skip connection directly between Fourier coefficients. On the implementation side, the authors compute the Fourier transforms as dense matrix multiplications rather than fast Fourier transforms, because on TPUs matrix multiplies are extremely fast while memory reshuffling is the bottleneck.
