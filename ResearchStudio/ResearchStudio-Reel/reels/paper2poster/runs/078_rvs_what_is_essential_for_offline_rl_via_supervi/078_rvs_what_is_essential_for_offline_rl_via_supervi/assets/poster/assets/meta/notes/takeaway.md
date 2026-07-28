# Takeaway

Core claim: A plain two-layer MLP trained to maximize likelihood is a state-of-the-art offline RL method, provided you carefully tune capacity and regularization and choose the right conditioning variable (goals vs rewards).

Supporting detail: RvS remains comparatively weak on random data, where TD learning still wins, marking a clear open problem.

Narration: The takeaway is essentially a practitioner's field guide. You do not need advantage weighting or a Transformer to do offline RL by supervised learning. A plain two-layer feedforward network, trained simply to maximize likelihood, is competitive with the state of the art, as long as you get two things right: carefully tune the model's capacity and its regularization, and choose the right thing to condition on, goals or rewards. The concrete recipe is to grow the network width until performance saturates, then add a little dropout. The honest caveat is that on purely random data, temporal-difference methods still win, which the authors flag as an open problem for future work.
