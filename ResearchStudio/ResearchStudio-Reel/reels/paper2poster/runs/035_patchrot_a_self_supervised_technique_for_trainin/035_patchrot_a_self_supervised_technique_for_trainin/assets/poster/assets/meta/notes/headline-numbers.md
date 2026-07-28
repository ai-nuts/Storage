# Headline Numbers

Core claim: - CIFAR-10 top-1: 92.6% (PatchRot) vs 83.9% (supervised from scratch), +8.7 points - CIFAR-100 top-1: 70.6% vs 50.2% supervised (+20.4); top-5: 90.2% vs 81.6% - FashionMNIST top-1: 94.1% vs 89.8% supervised - Tiny-ImageNet top-5: 73.4% vs 66.4% supervised

Supporting detail: - Semi-supervised CIFAR-10 with only 4000 labels: 81.1% (vs 53.7% supervised on same labels) - Rotation angles: 4-way (0°/90°/180°/270°); buffer B = 1/4 patch size; 300 SSL + 200 supervised epochs

Narration: The numbers tell a clear story. On CIFAR-10, PatchRot reaches ninety-two point six percent top-one accuracy, an improvement of eight point seven points over supervised training from scratch. On CIFAR-100 the improvement is over twenty points, from fifty point two to seventy point six percent top-one, and ninety point two percent top-five. FashionMNIST improves to ninety-four point one percent and Tiny-ImageNet's top-five rises to seventy-three point four percent. In the semi-supervised setting with only four thousand labeled CIFAR-10 images, PatchRot reaches eighty-one percent accuracy, versus roughly fifty-four percent for supervised training on the same labels, showing how valuable the self-supervised features are when labels are scarce.
