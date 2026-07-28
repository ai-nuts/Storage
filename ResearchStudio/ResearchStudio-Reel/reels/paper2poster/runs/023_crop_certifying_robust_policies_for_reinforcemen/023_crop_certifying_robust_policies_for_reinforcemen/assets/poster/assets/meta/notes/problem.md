# Problem

Core claim: Reinforcement learning agents deployed in safety-critical settings are vulnerable to adversarial perturbations of their input states, yet no method could certify their robustness with theoretical guarantees.

Supporting detail: Prior defenses (adversarial training, smoothness regularization) only offer empirical robustness, which stronger adaptive attacks repeatedly break.

Narration: Reinforcement learning has moved into domains where failure is costly, such as autonomous driving and trading. But researchers have shown that an adversary who slightly perturbs the state observations fed to an RL agent can reliably change its decisions. A wave of empirical defenses followed, only to be defeated by newer adaptive attacks. What has been missing is certification: a way to prove, rather than just observe, that a trained policy stays reliable under every perturbation within a bounded budget. This paper tackles exactly that gap for reinforcement learning.
