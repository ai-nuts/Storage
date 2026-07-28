# Key Result

Core claim: On ground-truth simulations Neuroformer's attention recovers directed connectivity and hub neurons that Pearson correlation cannot; on real data it predicts population responses more accurately than a GLM (t-test p=0.0196) and decodes mouse behavior with pretrained few-shot models reaching Pearson r up to 0.97.

Supporting detail: A model pretrained on neural responses and fine-tuned on just 1% of behavior data outperforms a non-pretrained model trained on 10% of the data, evidence of transferable, behaviorally meaningful representations.

Narration: On the simulated network, Neuroformer's attention reveals directed connectivity and identifies the hub neurons, which plain correlation misses for lack of directionality. On real cortex, it reproduces responses to gratings and natural videos, with population predictions significantly beating a GLM, p around 0.02. Fine-tuned to decode running, it reaches Pearson correlations up to 0.97.
