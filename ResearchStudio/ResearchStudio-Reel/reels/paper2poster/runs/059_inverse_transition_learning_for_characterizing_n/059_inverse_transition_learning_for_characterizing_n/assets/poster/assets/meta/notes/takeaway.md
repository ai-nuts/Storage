# Takeaway

Core claim: By clipping a Bayesian posterior over transition dynamics with expert-derived constraints, you get gradient-free offline policies that are provably safe, can outperform the expert, and have dramatically lower variance than MLE.

Supporting detail: The same constraints-plus-uncertainty recipe yields an action ranking in uncertain states, making the learned policies more informative for high-stakes planning such as healthcare.

Narration: By clipping a Bayesian posterior over the transition dynamics with constraints derived from a near optimal expert, you obtain gradient free offline policies that are provably safe, can outperform the expert who generated the data, and carry dramatically lower variance than maximum likelihood. The same recipe of constraints plus uncertainty also yields a ranking of actions in the uncertain states, making the learned policies more informative for high stakes planning such as clinical decision making.
