# Motivation

Core claim: If mechanistically dissimilar minimizers were freely connected, naive fine-tuning could silently preserve a model's reliance on spurious attributes, undermining robustness even when clean data is used.

Supporting detail: Fine-tuned models often stay linearly connected to their pretraining solution, hinting that fine-tuning may fail to change the underlying mechanism at all.

Narration: Why does this matter now? In practice we constantly fine-tune pretrained models on downstream data, assuming this fixes undesirable behavior. But prior work shows fine-tuned models often remain linearly connected to their pretraining solution. If linear connectivity is tied to shared mechanisms, then naive fine-tuning on clean data might never remove a model's reliance on spurious cues. Understanding the relationship between connectivity and mechanism is therefore directly relevant to robustness and safe adaptation of models.
