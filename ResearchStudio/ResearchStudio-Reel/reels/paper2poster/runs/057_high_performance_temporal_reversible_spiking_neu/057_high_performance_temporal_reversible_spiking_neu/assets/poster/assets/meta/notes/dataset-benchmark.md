# Dataset / Benchmark

Core claim: Evaluated on static ImageNet-1K (224×224) and neuromorphic CIFAR10-DVS and DVS128 Gesture, with training memory and time measured on 6 NVIDIA A100-40GB GPUs under float16 mixed precision.

Supporting detail: Memory is reported as peak GPU memory per image (MB/img) following S-RevSNN; baselines span spiking ResNets, spiking Transformers, and training-optimization SNNs (OTTT/SLTT/S-RevSNN).

Narration: The method is evaluated on both static and neuromorphic vision. For static images they use ImageNet-1K at a resolution of 224 by 224. For event-based data they use CIFAR10-DVS and the DVS128 Gesture dataset. Crucially, they report not just accuracy but the real training cost, measuring peak GPU memory per image and per-epoch training time on six NVIDIA A100 GPUs under mixed precision. They compare against a broad set of baselines, including spiking ResNets, spiking Transformers, and other training-optimization methods such as OTTT, SLTT, and the spatially reversible S-RevSNN.
