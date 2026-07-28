# Problem

Core claim: Deep neural networks usually cannot tell how far a new input lies from their training data, so they give overconfident predictions on out-of-distribution or hard examples.

Supporting detail: Probabilistic models like Gaussian Processes are naturally distance-aware, but reliable, efficient uncertainty estimation for real-world deep learning is still missing.

Narration: A trustworthy model should know when it is operating far from what it has seen. Deep neural networks, however, often make confident predictions even on inputs that are wildly different from their training data. Classical probabilistic models such as Gaussian Processes have a built-in sense of distance from the training set, but standard deep networks do not, and reliable, efficient uncertainty estimation for real deployments remains an open problem.
