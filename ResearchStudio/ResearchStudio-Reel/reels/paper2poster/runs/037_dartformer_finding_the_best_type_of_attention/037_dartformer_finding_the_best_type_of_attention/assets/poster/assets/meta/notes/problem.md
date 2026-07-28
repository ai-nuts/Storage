# Problem

Core claim: There are many efficient Transformer attention mechanisms and no single one is best across tasks, so practitioners lack an efficient way to pick the right attention for a given long-range task.

Supporting detail: Prior work (Tay et al., Long Range Arena) shows attention performance is highly task-dependent when models are trained from scratch without pretraining, leaving the choice unclear.

Narration: The Transformer's original dot-product attention scales quadratically with sequence length, so a large family of efficient alternatives has appeared, from Longformer and Bigbird to Performer, Reformer, and Synthesizer. The catch is that no single one wins everywhere: earlier long-range benchmarking showed that the best attention depends heavily on the task when there is no pretraining. That leaves practitioners with an awkward question, namely how to efficiently discover which attention is right for a given long-range task without simply training all of them.
