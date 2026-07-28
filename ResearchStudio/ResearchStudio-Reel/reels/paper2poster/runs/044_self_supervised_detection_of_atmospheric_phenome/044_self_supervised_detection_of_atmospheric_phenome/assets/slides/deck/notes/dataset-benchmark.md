# Dataset / Benchmark

Core claim: The unlabeled pretraining set holds 2,943,550 Sentinel-1 A/B Wave-mode images from 2017-2019 (each 20 km × 20 km at 5 m resolution). The labeled benchmark has 2,300 expert-consensus, multi-label vignettes over four classes, MC, WS, NV, and OT, split 60/20/20 for train, validation, and test.

Supporting detail: Images are freely available from ESA's Sentinel Open Access Hub with no licensing restrictions; unlabeled images are zero-padded to 450×450 pixels with no further preprocessing.

Narration: Two datasets drive the study. The pretraining pool is nearly three million unlabeled Wave-mode images from Sentinel-1 A and B over 2017 to 2019, each covering a twenty by twenty kilometer patch of ocean at five meter resolution, ninety percent used for training and ten percent held out for validation. The labeled benchmark contains twenty-three hundred vignettes annotated by experts into a consensus multi-label ground truth across four classes: mesoscale convection cells, wind streaks, negligible variability, and other. This set is stratified and split sixty, twenty, twenty into training, validation, and held-out test data.
