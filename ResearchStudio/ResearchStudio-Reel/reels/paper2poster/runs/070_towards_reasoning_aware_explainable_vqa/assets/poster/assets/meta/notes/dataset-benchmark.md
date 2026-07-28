# Dataset / Benchmark

Core claim: Experiments use two VQA datasets with annotated explanations: GQA-REX (about 1.04M QA pairs over 82K images, explanations for ~98% of GQA-balanced samples) and VQA-E (explanations for ~40% of VQA2.0 QA pairs).

Supporting detail: GQA-REX explanations follow a scene-graph reasoning format and are not fully human-readable; VQA-E explanations resemble image captions containing the answer. Both are acknowledged as imperfect.

Narration: Because very few datasets provide annotated explanations alongside answers, the authors chose the two largest available. GQA-REX contains explanations for roughly ninety-eight percent of the samples in the GQA-balanced dataset, about 1.04 million question-answer pairs spanning eighty-two thousand images, with one explanation per pair. However, its explanations follow the reasoning-format of prior work and are not fully human-readable, sometimes containing grammatical inaccuracies. VQA-E provides explanations for about forty percent of the question-answer pairs in VQA 2.0, and because those explanations are built by matching captions to the question-answer pair, they tend to read more like image captions than genuine reasoning. Both datasets have limitations, which the authors are transparent about.
