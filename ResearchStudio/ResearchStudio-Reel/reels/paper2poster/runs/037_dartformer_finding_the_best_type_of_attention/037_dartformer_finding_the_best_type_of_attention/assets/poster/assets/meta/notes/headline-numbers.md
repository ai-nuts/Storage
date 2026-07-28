# Headline Numbers

Core claim: - ListOps: Reformer masked-validation-drop score = 11.85 vs < 0.5 for all eight other attentions — a clean, decisive selection signal. - Document matching: best homogeneous (Synthesizer) 71.1% vs NAS Prune 67.0% and NAS One-shot 64.7% — heterogeneous loses by ~4–6 points. - Text classification: best homogeneous (Performer) 64.5% vs NAS Prune 63.9% and NAS One-shot 64.4% — heterogeneous never ahead.

Supporting detail: 9 candidate attention mechanisms searched across 3 LRA tasks with sequence lengths of 1k / 2k / 4k.

Narration: To put concrete numbers on it: on ListOps, Reformer earns a masked-validation-drop score of eleven point eight five, dwarfing every other attention's score of under half a point, a strikingly clean selection signal. On document matching, the best homogeneous model, Synthesizer, reaches seventy-one point one percent, while the heterogeneous NAS Prune and NAS One-shot models trail at sixty-seven and sixty-four point seven percent. On text classification the best homogeneous Performer hits sixty-four point five percent, and again neither heterogeneous variant edges ahead. Across nine attention mechanisms and three tasks, the pattern is consistent.
