# Title

Spiking Neural Networks promise low-power AI, but training them over many timesteps is expensive in memory, and running them repeats work at inference. This ICML 2024 paper introduces T-RevSNN, a Temporal Reversible architecture that turns off the temporal dynamics of most spiking neurons and makes the few remaining temporal connections reversible. The result is O(L) training memory and O(1) inference cost, with state-of-the-art accuracy among CNN-based SNNs on ImageNet and up to 8.6 times better memory efficiency, 2.0 times faster training, and 1.6 times lower inference energy.
