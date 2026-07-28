# Key Result

Core claim: Against the strongest baseline (ERM with perturbation), CW-ERM significantly reduces collisions across metrics, with improvements around 35% on some metrics; front collisions drop from 14 to 9 and side collisions from 55 to 47 when the matching metric is upsampled.

Supporting detail: Improving one metric often helps related ones (upsampling side collisions also reduces rear collisions), and variance is lower than the baseline in several cases; multi-metric upsampling trades off metrics along a Pareto front.

Narration: "The results are strong. Compared against the best baseline, behavioral cloning with ERM and perturbation, CW-ERM significantly reduces collisions across the board, with improvements reaching about thirty-five percent on some metrics. When the model upsamples front-collision scenes, front collisions fall from fourteen to nine. When it upsamples side-collision scenes, side collisions fall from fifty-five to forty-seven. There is a nice side effect too: improving one metric often improves related ones. Upsampling side collisions also reduces rear collisions, evidence that the policy is becoming less passive rather than just gaming a single number. Variance is also lower than the baseline in several cases, so the gains are stable."
