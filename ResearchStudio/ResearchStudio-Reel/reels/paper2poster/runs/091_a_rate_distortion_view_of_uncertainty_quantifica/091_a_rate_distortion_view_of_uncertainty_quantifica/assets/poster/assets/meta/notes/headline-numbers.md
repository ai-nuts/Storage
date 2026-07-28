# Headline Numbers

Core claim: CIFAR-10 → SVHN OOD: AUROC 0.986 (best). CIFAR-10 → CIFAR-100 OOD: AUROC 0.922 (best). CIFAR-10 misclassification: Calibration AUROC 0.930.

Supporting detail: ImageNet-1K: DAB (fine-tuned ResNet-50) beats a 5-model ensemble on misclassification (Calibration AUROC 0.868 vs 0.861) and OOD detection (ImageNet-O AUROC 0.743 vs 0.642) with far fewer trainable parameters (~36.6M vs ~117.7M).

Narration: To summarize the numbers: on CIFAR-10, DAB achieves a best-in-class OOD AUROC of 0.986 against SVHN and 0.922 against CIFAR-100, and a misclassification calibration AUROC of 0.930. At ImageNet scale, DAB built on a fine-tuned ResNet-50 beats a five-model ensemble on misclassification, 0.868 versus 0.861, and on out-of-distribution detection against ImageNet-O, 0.743 versus 0.642, all while using far fewer trainable parameters, roughly thirty-six million versus one hundred and eighteen million.
