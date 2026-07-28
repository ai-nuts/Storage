# Problem

Core claim: When deep policies are behavior-cloned with minibatch SGD, long-horizon rollout reward oscillates violently across iterates even though the single-step behavior-cloning loss stays flat and stable.

Supporting detail: Because evaluating true task reward at every checkpoint is impractical, these hidden oscillations mean any given trained checkpoint carries high risk of poor deployed performance.

Narration: Imagine training a robot controller by imitation. You watch the training loss, and it drops smoothly and stays low. Everything looks fine. But if you actually deploy the policy and measure how well it walks, the score jumps around violently from one training step to the next. This paper is about that gap. The single-step imitation loss is calm and stable, yet the thing you truly care about, the long-horizon reward, is oscillating wildly. And because it is expensive to roll out and evaluate at every checkpoint, you usually never see these swings, which means whichever checkpoint you happen to grab could be a bad one.
