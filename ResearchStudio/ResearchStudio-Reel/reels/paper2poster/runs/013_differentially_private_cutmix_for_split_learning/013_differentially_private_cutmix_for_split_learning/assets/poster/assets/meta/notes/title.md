# Title

Vision transformers are overtaking convolutional networks, but their size makes privacy-preserving distributed training hard. Federated learning must move whole models, and split learning leaks privacy because a transformer's smashed data still resembles the raw input. From Yonsei, Deakin, M.I.T., and Oulu, at NeurIPS 2022, this paper proposes DP-CutMixSL, pairing a Gaussian differential-privacy mechanism with a patch-level randomized CutMix that mixes masked patches across clients. It strengthens privacy while improving accuracy.
