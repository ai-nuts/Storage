# Key Result

Core claim: On VPAM test settings DDT reaches success rates of 0.86 (Train), 0.84 (Non-Obstacle), and 0.73 (Unforeseen Obstacle), beating DCRL (0.71/0.62/0.57), CbMRL (0.62/0.47/0.36), and Trans4OSIL (0.33/0.28/0.16) across all settings.

Supporting detail: Going from Train to Unforeseen Obstacle, DDT degrades only -15% versus -20%, -33%, and -52% for the baselines — at least 5% better performance retention. On Meta-World with disturbance, DDT reaches 0.61 on unseen demos versus ≤0.12 for baselines.

Narration: Across the VPAM benchmark, DDT consistently leads. On the training set it reaches a success rate of 0.86, on non-obstacle test settings 0.84, and even under unforeseen obstacles 0.73 — well above every baseline, with the closest competitor DCRL at 0.57 under obstacles and behavior-cloning Trans4OSIL as low as 0.16. Just as important is stability: moving from the training condition to unforeseen obstacles, DDT's performance drops only fifteen percent, while the baselines drop twenty, thirty-three, and fifty-two percent respectively. On the Meta-World robotics tasks with added disturbance, DDT still succeeds sixty-one percent of the time on unseen demonstrations, whereas the strongest baseline manages only about twelve percent. The meta-RL mechanism is what gives DDT this robustness to change.
