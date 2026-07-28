# Key Result

Core claim: In a noiseless setting (Table 1), CutMixSL attains the highest top-1 accuracy in every case but one, reaching 73.77% on CIFAR-10 with ViT-Tiny versus 57.21% for plain SL and 67.88% for SplitFed, and 71.26% with PiT-Tiny versus 55.63% for SplitFed.

Supporting detail: The single exception is CIFAR-10 with VGG-16, where SL with Mixup (68.20%) edges out CutMixSL (67.53%), consistent with CNNs suffering more information loss from patch replacement than transformers do.

Narration: Without noise, CutMixSL gives the best top-1 accuracy in every configuration but one. On CIFAR-10 with ViT-Tiny it reaches seventy-three point seven seven percent, versus fifty-seven for plain split learning and sixty-eight for SplitFed. With PiT-Tiny it hits seventy-one point two six. On Fashion-MNIST it tops eighty-nine percent across all three architectures. The exception is VGG-16, where Mixup edges ahead, because CNNs focus locally, so replacing whole patches costs them more information than it costs transformers.
