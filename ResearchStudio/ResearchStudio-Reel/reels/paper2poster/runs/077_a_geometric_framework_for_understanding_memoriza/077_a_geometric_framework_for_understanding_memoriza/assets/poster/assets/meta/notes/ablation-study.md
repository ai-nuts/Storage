# Ablation Study

Core claim: For mitigation, sweeping the number of perturbed tokens k over {1,2,3,4,6,8} traces the trade-off between memorization (SSCD similarity, lower is better) and fidelity (CLIP score, higher is better); attribution-based token selection beats a uniform-random-selection ablation.

Supporting detail: New differentiable attribution metrics based on the CFG-adjusted score norm and on FLIPD perform on par with the original CFG-vector-norm metric of Wen et al. (2023); all attribution-based variants keep higher CLIP score at equal memorization reduction than random token perturbation.

Narration: To mitigate memorization, the method attributes it to specific prompt tokens and rephrases them with GPT-4. Ablating the number of perturbed tokens shows a clean trade-off: perturbing more tokens reduces memorization but also reduces fidelity. Importantly, choosing tokens by attribution beats choosing them at random — attribution-based selection reaches lower training-image similarity while keeping a higher CLIP score. New attribution metrics built on the score norm and on FLIPD work about as well as the original guidance-based metric.
