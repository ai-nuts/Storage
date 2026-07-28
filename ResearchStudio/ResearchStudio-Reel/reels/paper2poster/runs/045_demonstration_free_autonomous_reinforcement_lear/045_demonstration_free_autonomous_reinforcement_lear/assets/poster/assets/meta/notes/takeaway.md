# Takeaway

Core claim: By pairing a self-fading auxiliary agent with an optimal-transport-based bidirectional goal curriculum, IBC is the first method to learn robotic tasks autonomously with no resets and no demonstrations, matching approaches that rely on expert data.

Supporting detail: The approach is limited to reversible (ergodic) environments and still needs minimal human input to specify sparse rewards; a reward-free variant using C-learning shows early promise as future work.

Narration: The takeaway is simple to remember. IBC shows that an agent can learn robotic manipulation and locomotion tasks entirely on its own, with no environment resets and no demonstrations, by generating its own curriculum. It does this with two cooperating ideas: an auxiliary agent that anchors the learner early and then fades away, and a bidirectional goal curriculum built on optimal transport that keeps proposing achievable intermediate goals. The result matches methods that depend on expert data. The main caveats are that it assumes reversible environments and still needs a human to specify a sparse reward, and the authors point to a fully reward-free version, hinted at by their C-learning experiments, as the natural next step.
