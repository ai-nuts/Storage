# Dataset / Benchmark

Core claim: Evaluated on indoor scenes ScanNet and NYU Depth, and outdoor scenes MegaDepth and ETH-3D; NeurHal is trained on ScanNet for the indoor setting and on MegaDepth for the outdoor setting, then tested on scenes unseen at training time.

Supporting detail: Absolute camera pose estimation is evaluated on the ScanNet test set over 2,500 source/target image pairs from held-out scenes.

Narration: The method is evaluated across both indoor and outdoor domains. Indoors, NeurHal is trained on ScanNet and also tested on the NYU Depth dataset; outdoors, it is trained on MegaDepth and tested on ETH three D. Crucially, every evaluation uses scenes that were never seen during training, so the results measure genuine generalization. For the downstream application, absolute camera pose estimation is measured on twenty five hundred source and target image pairs from held out ScanNet scenes.
