# Motivation

Core claim: The abundant normal and abnormal cues implicit in the unlabeled test images themselves are ignored by prior methods, yet they are enough to determine anomalies without any labels or prompts.

Supporting detail: Key observation: a normal image patch finds many similar patches across other unlabeled images, while an abnormal patch finds only a few, giving a discriminative, training-free signal.

Narration: The authors make a simple observation. In a batch of unlabeled test images of one product, a normal patch finds many similar patches across the others, because normal appearance repeats. An abnormal patch finds only a few, since defects are rare. That asymmetry is a signal already inside the test set.
