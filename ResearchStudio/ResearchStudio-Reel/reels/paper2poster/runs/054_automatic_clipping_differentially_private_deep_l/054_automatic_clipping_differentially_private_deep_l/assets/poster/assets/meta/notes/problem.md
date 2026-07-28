# Problem

Core claim: Differentially private deep learning depends on per-example gradient clipping, but the clipping threshold R is a fragile, task-specific hyperparameter whose value strongly determines final accuracy.

Supporting detail: On ImageNet, ResNet18 accuracy can fall from 45% to 31% if R is set 2x too large; SOTA results often need very small R (e.g. R=1 or R=0.1), found only by expensive search.

Narration: In differentially private deep learning, every per-sample gradient is clipped to a fixed norm R before noise is added, and that single threshold R turns out to be decisive for accuracy. Picking it wrong is costly: on ImageNet, ResNet18 accuracy can collapse from forty-five percent to thirty-one percent when R is merely doubled. State-of-the-art private models tend to need very small clipping thresholds that can only be found through careful, expensive tuning.
