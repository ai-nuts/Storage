# Motivation

Core claim: Masked language modeling shows that predicting randomly masked tokens yields representations transferable across many downstream tasks; the authors observe decision-making inferences are just different maskings of a trajectory.

Supporting detail: Predicting a masked last action given prior states and actions is exactly a behavior-cloning inference, so the whole family of tasks fits one bidirectional masked-prediction objective.

Narration: Masked language modeling, the technique behind BERT, trains models to predict randomly masked tokens in a sequence, producing rich bidirectional representations that transfer to many tasks. The authors observe that this idea maps directly onto decision making. If you treat states and actions as tokens and mask the last action, predicting it is exactly a behavior cloning inference. Different tasks are simply different masking patterns over the same trajectory, so a single masked-prediction objective can, in principle, express them all.
