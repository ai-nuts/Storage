# Contribution

Core claim: The paper presents a systematic approach to scale spherical CNNs one order of magnitude larger: a TPU-optimized JAX implementation of spin-weighted spherical harmonic transforms, new general-purpose layers and activations, and application-specific input representations for molecules and weather.

Supporting detail: Naively increasing depth and width is shown insufficient; scaling required redesigning the nonlinearity, normalization, and residual block, each improving both efficiency and accuracy.

Narration: The authors contribute a systematic recipe for scaling spherical CNNs by an order of magnitude. It has three parts. First, an efficient implementation of spin-weighted spherical harmonic transforms in JAX, tuned to run fast and distributed on TPUs. Second, new general-purpose layers and activations that improve both expressivity and efficiency. And third, application-specific input representations designed for molecules and for weather data. A key finding is that naive scaling, just adding depth and width, is not enough; the core components themselves had to be redesigned.
