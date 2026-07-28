# Headline Numbers

Core claim: - 0.93 best micro-averaged AUROC (fine-tuned model) - ~3 million (2,943,550) unlabeled Sentinel-1 images for contrastive pretraining - 2,300 expert-labeled, multi-label vignettes across 4 classes - WS AUROC 0.831-0.850 vs CmWV 0.727; MC 0.872-0.873 vs 0.793

Supporting detail: SwAV trained 65 epochs / ~10 days on 8× V100 GPUs; images 20×20 km at 5 m resolution.

Narration: A few numbers capture the study. Self-supervised training used almost three million unlabeled radar images. The labeled benchmark held twenty-three hundred expert vignettes across four classes. The best fine-tuned model reached a micro-averaged AUROC of about zero point nine three. And on the toughest classes, wind streaks and convection cells, the new models jumped from CmWV's roughly zero point seven three and zero point seven nine into the mid eighties, a substantial detection improvement.
