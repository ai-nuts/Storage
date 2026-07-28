# Dataset / Benchmark

Core claim: In-domain modeling uses WikiText-103 (103M training tokens, 250K validation and test tokens) with a 247M-parameter Transformer base LM. Domain adaptation uses the English side of Law-MT (19M tokens) with a 656M-parameter Transformer base LM.

Supporting detail: For WikiText-103 the datastore holds 103M entries clustered into 1M states; for Law-MT the datastore holds 19M entries clustered into 200K states, keeping an average cluster size near 100 in both. Baselines are the original kNN-LM and AdaptRet.

Narration: The method is evaluated in two settings. For standard in-domain language modeling the authors use WikiText-103, a Wikipedia benchmark with one hundred and three million training tokens, and a two hundred forty seven million parameter Transformer as the base model, producing a datastore of one hundred and three million entries clustered into one million states. For domain adaptation they use the law-domain corpus Law-MT with nineteen million tokens and a larger six hundred fifty six million parameter base model, clustered into two hundred thousand states. Throughout, RetoMaton is compared against the original kNN-LM and against Adaptive Retrieval.
