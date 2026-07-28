# Dataset / Benchmark

Core claim: Evaluated on three standard distillation benchmarks — CIFAR10 and CIFAR100 (32×32) and TinyImageNet (64×64) — and six high-resolution 128×128 ImageNet subsets (ImageNette, ImageWoof, ImageFruit, ImageMeow, ImageSquawk, ImageYellow), each with 10 classes, plus CIFAR100-C for corruption robustness.

Supporting detail: Storage is measured as parameters-per-class under IPC 1/10/50 budgets; the default backbone is a ConvNet with 128 channels and trajectory matching is the default objective, with cross-architecture eval on MLP, ResNet18, and ViT.

Narration: SPEED is tested broadly. On the standard side, it uses CIFAR-10 and CIFAR-100 at thirty-two by thirty-two resolution and TinyImageNet at sixty-four by sixty-four. To stress high-resolution performance, it uses six ImageNet subsets at one-twenty-eight by one-twenty-eight, each with ten classes: ImageNette, ImageWoof, ImageFruit, ImageMeow, ImageSquawk, and ImageYellow. Robustness is measured on CIFAR-100-C with fourteen corruption types at five severity levels. Everything is compared under equal storage budgets, counted in parameters per class, at one, ten, and fifty images per class. The default backbone is a ConvNet, the default matching objective is trajectory matching, and generalization is checked on MLP, ResNet18, and ViT.
