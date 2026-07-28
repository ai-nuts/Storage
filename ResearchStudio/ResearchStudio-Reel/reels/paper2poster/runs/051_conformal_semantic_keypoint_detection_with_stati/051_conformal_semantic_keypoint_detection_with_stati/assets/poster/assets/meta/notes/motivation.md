# Motivation

Core claim: Neural keypoint detectors can be arbitrarily wrong (outliers), robust back-ends like RANSAC give no optimality guarantee and can fail silently, and no prior method certifies a worst-case error bound between the estimate and the groundtruth.

Supporting detail: Three challenges: (C1) keypoints may be far from groundtruth, (C2) outlier rejection is nonconvex and heuristics lack global optimality, (C3) no provably correct uncertainty quantification exists.

Narration: Why is this hard? The authors name three challenges. First, neural keypoint detectors can be arbitrarily wrong, producing outliers. Second, rejecting those outliers is a nonconvex optimization; fast heuristics like RANSAC are common but cannot guarantee global optimality and can fail silently. Third, and most fundamental, there is no provably correct uncertainty quantification, no formal worst-case error bound between estimate and groundtruth. Certifying that the optimizer is globally optimal still gives no probabilistic guarantee on the pose itself. This paper delivers exactly that guarantee, end to end.
