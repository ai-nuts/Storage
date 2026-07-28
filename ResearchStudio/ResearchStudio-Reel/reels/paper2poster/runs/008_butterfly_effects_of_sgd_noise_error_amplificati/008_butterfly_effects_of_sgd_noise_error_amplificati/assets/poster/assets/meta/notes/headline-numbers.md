# Headline Numbers

Core claim: 278 distinct interventions in the continuous-control study; horizon H = 1000 rollouts; error amplification constant is exponential in the horizon.

Supporting detail: 270M-parameter Transformers on TinyStories; rewards averaged over 20 initial conditions; theory bound grows as $\Omega(H)(e^{\Omega(H\delta)}-1)$ in reward gap versus $O(H\delta^2)$ in BC loss.

Narration: A few numbers anchor the study. The empirical investigation covers two hundred and seventy-eight distinct interventions in continuous control. The rollouts run over a horizon of one thousand steps, and the theory shows the error amplification constant grows exponentially in that horizon. On the language side, the models are two hundred and seventy million parameter Transformers trained on TinyStories. The key contrast in the theory is that a perturbation changes the behavior cloning loss by only order H delta squared, but can change the rollout reward by order H times e to the H delta minus one, an exponential gap.
