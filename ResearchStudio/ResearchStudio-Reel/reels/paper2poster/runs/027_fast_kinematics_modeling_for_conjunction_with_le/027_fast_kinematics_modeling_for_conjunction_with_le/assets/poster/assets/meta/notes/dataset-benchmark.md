# Dataset / Benchmark

Core claim: A dataset of 5000 input-output pairs was generated with JAM: 4000 for training, 500 for validation, and 500 for testing. Each vrms image is 551×551 pixels, and a single JAM image takes about 15 seconds to create.

Supporting detail: Parameter ranges are physically motivated. The network is implemented in PyTorch with PyTorch Lightning and trained on 5 Tesla P100 GPUs (16 GB each) in about one day.

Narration: The training set is constructed entirely with JAM, the physics code SKiNN is meant to imitate. The authors created five thousand input-output pairs, using four thousand for training, five hundred for validation, and five hundred held out for testing. Each velocity image is 551 by 551 pixels, generated at higher resolution than real data. Creating a single image with JAM takes about fifteen seconds, which underscores why emulation is worthwhile. The network is implemented in PyTorch with PyTorch Lightning and trained on five Tesla P100 GPUs, each with sixteen gigabytes of memory, over roughly one day.
