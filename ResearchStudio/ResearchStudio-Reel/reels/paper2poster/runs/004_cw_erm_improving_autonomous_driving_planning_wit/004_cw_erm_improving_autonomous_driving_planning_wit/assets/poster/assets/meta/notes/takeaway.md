# Takeaway

Core claim: Simply using a simulator to find and upsample a policy's own failure scenes, then retraining, meaningfully improves closed-loop driving safety without any differentiable simulator, extra human oracle, or added inference latency.

Supporting detail: CW-ERM is metric-agnostic and connects reweighting-by-failure to density-ratio covariate-shift correction, pointing to a theoretically grounded, easy-to-adopt direction for imitation-learned planners.

Narration: "The takeaway is refreshingly practical. You do not need a differentiable simulator, a human in the loop, or expensive closed-loop training to get closed-loop benefits. You just need to run your policy once in a simulator, note where it fails, upsample those scenes, and retrain. That simple recipe delivers significant reductions in collisions and other non-differentiable metrics, works with any closed-loop metric, and adds no inference latency. And it comes with a clean theoretical story: weighting scenes by failure is closely connected to correcting covariate shift through density-ratio estimation, a promising direction for making imitation-learned planners both simpler and safer."
