# Method

Core claim: GCB learns two encoders: a paired state-goal encoder φ trained so that ℓ₁ distance matches an on-policy goal-conditioned bisimulation metric, and a state encoder ψ trained so that the difference ψ(g) − ψ(s) equals φ(s, g), which makes goals composable by arithmetic. At test time an analogous pair (sₐ, gₐ) is added to the current state via ψ(s) + φ(sₐ, gₐ), and the nearest neighbor in ψ space yields the inferred goal.

Supporting detail: Both encoders are six-layer CNNs mapping to 256-dim latent spaces; the policy π(ψ(s), φ(s, g)) is trained on top of Implicit Q-Learning (IQL) in an offline RL setting, with φ, ψ, and the policy learned concurrently.

Narration: GCB learns two encoders together. Phi encodes a state-goal pair so its L1 distance matches an on-policy bisimulation metric, capturing how differently two tasks behave. Psi encodes a state so the goal embedding minus the state embedding equals phi. That makes goals composable: add an analogous pair to your state, then take the nearest neighbor in psi space. Training is offline on Implicit Q-Learning.
