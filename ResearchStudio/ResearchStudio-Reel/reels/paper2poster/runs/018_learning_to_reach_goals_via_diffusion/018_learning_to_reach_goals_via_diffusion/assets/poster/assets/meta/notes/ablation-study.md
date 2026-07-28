# Ablation Study

Core claim: Ablations over the evaluation time horizon show that conditioning on a time horizon consistently beats not conditioning, and the optimal horizon depends on task difficulty, with easier tasks favoring short horizons (h=1 or h=5) and harder tasks favoring longer ones.

Supporting detail: The hindsight relabeling ratio and time horizon are the two tuned hyperparameters; HandReach is especially sensitive, performing far better at h=1 than at longer horizons or with no horizon conditioning.

Narration: The authors study two key hyperparameters: the hindsight relabeling ratio and the evaluation time horizon, which sets how far ahead the policy aims. Across all tasks, conditioning on a time horizon clearly beats leaving it out. The best value depends on the task: easier tasks like PointReach do well with a short horizon of one or five steps, while harder tasks benefit from longer horizons because they need more steps to reach the goal. The HandReach task is particularly sensitive, working dramatically better with a horizon of one than with any longer setting. These trends are visualized as heatmaps of returns across horizons for both expert and random datasets.
