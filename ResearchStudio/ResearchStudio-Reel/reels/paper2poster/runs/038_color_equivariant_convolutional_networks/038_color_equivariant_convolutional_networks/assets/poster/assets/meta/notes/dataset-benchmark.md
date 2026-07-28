# Dataset / Benchmark

Core claim: Two controlled MNIST variants (long-tailed ColorMNIST, 30 classes; biased ColorMNIST, 10 classes) plus eight natural-image classification benchmarks: CIFAR-10, CIFAR-100, Flowers-102, STL-10, Oxford-IIIT Pet, Caltech-101, Stanford Cars, and ImageNet.

Supporting detail: Robustness is measured on hue-shifted test sets spanning -180° to 180°; ResNet-18 is used for high-resolution datasets and ResNet-44 for CIFAR, all trained on a single NVIDIA A40 GPU.

Narration: The evaluation spans two scales. First, two synthetic MNIST variants isolate the phenomenon: a long-tailed ColorMNIST with strong class imbalance, and a biased ColorMNIST where each class has a characteristic hue with tunable spread. Then, eight standard image classification benchmarks, from CIFAR and STL-10 to Flowers-102, Stanford Cars, and ImageNet, test the method in realistic settings. To probe robustness, every test image is re-rendered under a gradual hue shift from minus one-hundred-eighty to plus one-hundred-eighty degrees, and accuracy is averaged across the full sweep.
