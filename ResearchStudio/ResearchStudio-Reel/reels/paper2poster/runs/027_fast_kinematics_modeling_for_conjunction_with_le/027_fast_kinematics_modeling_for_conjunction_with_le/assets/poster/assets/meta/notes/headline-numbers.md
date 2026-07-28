# Headline Numbers

Core claim: - ~300× faster than JAM (≈50 ms per vrms image on GPU vs ~15 s for JAM image creation) - < 1% error within the innermost two-arcsecond region; median ~0.47%, 90th percentile ~1.1% across 500 test images

Supporting detail: - 8-dimensional input → d×d vrms image; ~7,065,451 trainable parameters - 5000 total samples (4000 train / 500 val / 500 test); trained ~1 day on 5× Tesla P100 GPUs

Narration: Here are the headline numbers. SKiNN runs about three hundred times faster than JAM, taking roughly fifty milliseconds per image on a GPU compared to about fifteen seconds for JAM. Its error is under one percent within the innermost two-arcsecond region, with a median absolute error around 0.47 percent and a ninetieth percentile of about 1.1 percent across five hundred test images. The network maps an eight-dimensional parameter vector to a velocity image and has about seven million trainable parameters. It was trained on five thousand samples, split four thousand for training and five hundred each for validation and testing, over roughly one day on five Tesla P100 GPUs.
