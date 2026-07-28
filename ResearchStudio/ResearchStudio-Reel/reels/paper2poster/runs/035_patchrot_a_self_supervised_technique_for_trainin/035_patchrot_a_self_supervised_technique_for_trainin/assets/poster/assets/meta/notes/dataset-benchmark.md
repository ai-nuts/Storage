# Dataset / Benchmark

Core claim: Evaluated on CIFAR-10, CIFAR-100, FashionMNIST (32×32), and Tiny-ImageNet (64×64), plus SVHN and MNIST for rotation-invariant objects. A compact ViT (6 encoder blocks, 256 embedding dim, 512 expansion) is used with patch size 4 (CIFAR/FashionMNIST) or 8 (Tiny-ImageNet).

Supporting detail: Buffer B is one quarter of the patch size. Training uses Adam (lr and weight decay 5e-4 and 3e-2), batch size 128 (effective 128×5), 300 self-supervised epochs and 200 supervised epochs. Transfer learning (CIFAR100↔CIFAR10) and semi-supervised CIFAR-10 (250-10000 labels) are also tested.

Narration: The authors test PatchRot on four standard image classification datasets: CIFAR-10, CIFAR-100, FashionMNIST at thirty-two by thirty-two resolution, and Tiny-ImageNet at sixty-four by sixty-four. They also study SVHN and MNIST to probe rotation-invariant objects like digits. The backbone is a compact vision transformer with six encoder blocks. Patch sizes are four pixels for the small datasets and eight for Tiny-ImageNet, with a buffer gap set to a quarter of the patch size. Beyond plain classification, they evaluate transfer learning between CIFAR-10 and CIFAR-100, and a semi-supervised setting on CIFAR-10 where only a handful of labels, from two hundred fifty up to ten thousand, are available.
