# Method

Core claim: RvS trains an outcome-conditioned policy πθ(a | s, ω) with a two-layer feedforward MLP by maximizing the log-likelihood of observed actions, using hindsight relabeling so each action is a demonstration for the outcome it achieved.

Supporting detail: Outcomes are either a future goal state (RvS-G) or an average future return (RvS-R), formed by concatenating the outcome onto the input state; no advantage weighting or Transformer is used.

Narration: The method is deliberately simple. RvS assumes an agent in a Markov decision process and trains a policy conditioned on an outcome, which can be either a future goal state or an average future return. Given an offline dataset of trajectories, it applies hindsight relabeling: every observed action becomes a demonstration for whatever outcome actually occurred later in that same trajectory. The policy itself is just a feedforward multilayer perceptron with two fully connected layers, and the outcome is fed in simply by concatenating it onto the input state. Training then maximizes the log-likelihood of the observed actions under the conditioned policy. There is no advantage weighting, no temporal-difference bootstrapping, and no Transformer, only a maximum-likelihood objective over relabeled experience.
