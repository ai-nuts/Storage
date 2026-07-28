# Dataset / Benchmark

Core claim: Evaluated on four models: ResNet50 on ImageNet-1K, ViT and MLP-Mixer fine-tuned on Cifar10 (pretrained on ImageNet-21k), and an extreme multi-label classification (XML) model on Wiki10-31K.

Supporting detail: Testbed: 16 Nvidia Tesla V100-32GB GPUs (2 machines x 8 GPUs), 25Gbps network, CUDA 11.0, PyTorch 1.8.0, NCCL 2.7.8, Horovod 0.19.1, with memory-momentum error feedback.

Narration: The experiments span four models covering both vision and recommendation-style workloads: ResNet50 trained on ImageNet, Vision Transformer and MLP-Mixer fine-tuned on Cifar10 from ImageNet-21k pretraining, and an extreme multi-label classification model on the Wiki10-31K dataset. The testbed is sixteen Nvidia V100 GPUs across two machines connected by a twenty-five gigabit network, running PyTorch with Horovod and NCCL, and using memory-momentum error feedback to preserve accuracy across all sparsification methods.
