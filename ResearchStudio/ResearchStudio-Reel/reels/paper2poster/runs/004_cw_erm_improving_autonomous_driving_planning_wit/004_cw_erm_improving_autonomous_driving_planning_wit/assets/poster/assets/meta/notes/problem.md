# Problem

Core claim: Behavioral-cloning driving policies are trained open-loop with Empirical Risk Minimization, matching only per-step expert actions, so they perform poorly closed-loop where small errors compound into covariate shift and collisions.

Supporting detail: Non-differentiable safety metrics like collisions are ignored by the surrogate loss, so open-loop training and closed-loop deployment optimize different objectives.

Narration: "Imitation learning for self-driving cars is usually done through behavioral cloning, where the network is trained to reproduce an expert's next action. The catch is that this is done open-loop: the model never sees the consequences of its own actions. But when the policy actually drives, every action changes the future state it will see. Small prediction errors accumulate, pushing the car into out-of-distribution situations the model was never trained on. And the metrics that truly matter, like collisions, are non-differentiable, so they are effectively invisible to the standard training loss. The result is a policy that looks great open-loop but drives poorly in closed-loop evaluation."
