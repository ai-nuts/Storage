# Problem

Core claim: Multi-timestep simulation of SNNs costs O(L×T) training memory and O(T) inference energy; existing training methods reduce one but never both at once.

Supporting detail: Training a spiking ResNet-19 at 10 timesteps needs about 20× the memory of a plain ResNet-19, blocking SNNs from scaling to large models.

Narration: Spiking Neural Networks are appealing because they promise brain-inspired, low-power computation. But to work well they are simulated over many timesteps, and that comes at a steep cost. During training, memory grows with both the number of layers and the number of timesteps, on the order of L times T. At inference, repeating the input over T steps makes the energy scale with T as well. The frustrating part is that current training methods can relieve one of these pressures but not the other at the same time, leaving SNNs stuck with a training memory and inference energy dilemma.
