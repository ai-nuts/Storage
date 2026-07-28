# Takeaway

Core claim: Predicting the rotation of both an image and its individual patches is a simple, ViT-native self-supervised task that learns global and local features and reliably beats supervised-from-scratch and RotNet across datasets, transfer, and low-label settings.

Supporting detail: The buffer-gap trick and reduced-resolution pretraining are cheap, general components that make patch-level rotation prediction work in practice.

Narration: The takeaway is that a very simple idea, predicting the rotation of both the whole image and each individual patch, turns out to be a self-supervised task perfectly suited to vision transformers. Because the class token learns global structure and the patch heads learn local detail, PatchRot teaches the transformer rich features without any labels, and those features reliably beat supervised training from scratch and the RotNet baseline across four datasets, in transfer learning, and especially when labeled data is scarce. It is a lightweight, practical recipe for pretraining vision transformers on limited data.
