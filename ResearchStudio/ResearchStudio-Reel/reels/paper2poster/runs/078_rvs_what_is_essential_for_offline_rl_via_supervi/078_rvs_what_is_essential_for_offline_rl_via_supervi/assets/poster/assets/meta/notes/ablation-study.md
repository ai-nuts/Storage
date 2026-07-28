# Ablation Study

Core claim: Two design choices are decisive. Larger network width improves performance (up to 1024 hidden units), and dropout regularization helps or hurts depending on the dataset (boosts kitchen-complete, hurts hopper-medium-expert and antmaze-medium-play).

Supporting detail: A categorical distribution over discretized actions matches or beats a unimodal Gaussian across the GCSL suite, again favoring higher policy capacity; validation loss only loosely predicts final performance.

Narration: The ablations pin down what actually matters. First, capacity: the best architectures are notably larger than those used in standard online RL or imitation learning, and widening the network up to about a thousand hidden units generally helps. Second, regularization: dropout is not universally good. It boosts performance on the small, human-demonstration kitchen-complete dataset, but it hurts on hopper-medium-expert and on antmaze-medium-play. Third, the output distribution: a categorical distribution over discretized actions matches or beats a unimodal Gaussian across the GCSL tasks, which fits the broader theme that more policy capacity helps. Finally, validation loss correlates only loosely with final performance, so it is not a reliable tuning signal on its own.
