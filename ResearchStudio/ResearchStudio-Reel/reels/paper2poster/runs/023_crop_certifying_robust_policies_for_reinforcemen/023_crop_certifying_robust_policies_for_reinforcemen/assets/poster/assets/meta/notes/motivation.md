# Motivation

Core claim: Empirical robustness offers no guarantees, so a policy that resists known attacks may still fail against a stronger, unseen adversary; safety-critical RL needs provable certificates.

Supporting detail: Randomized smoothing gives certified robustness in classification, but Q-learning breaks its assumptions: the output range is unbounded and outputs are not probabilities.

Narration: The core motivation is trust. If you cannot prove a policy is robust, then passing today's attacks tells you little about tomorrow's. Randomized smoothing has become a leading tool for certifying image classifiers, but reinforcement learning does not fit its mold. In classification the confidence output lives in a known zero-to-one range and behaves like a probability; in Q-learning the value function has an unknown range and its outputs are not probabilities at all. On top of that, a single action decision is not the whole story: what ultimately matters is the reward accumulated along an entire trajectory of decisions. CROP is designed to overcome both obstacles.
