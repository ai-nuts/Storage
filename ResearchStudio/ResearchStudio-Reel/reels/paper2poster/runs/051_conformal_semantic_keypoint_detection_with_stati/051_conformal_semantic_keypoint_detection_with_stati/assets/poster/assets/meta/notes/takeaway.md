# Takeaway

Core claim: By marrying conformal prediction with geometric uncertainty propagation, the two-stage pose pipeline becomes the first to output an estimate carrying a provable, computable worst-case error bound, without sacrificing accuracy.

Supporting detail: The framework is detector-agnostic (wraps any heatmap keypoint network) and points toward statistically guaranteed perception for other geometric vision problems.

Narration: The lasting message: you can turn a standard two-stage pose estimator into one that tells you how wrong it might be, with a real statistical guarantee, and pay little in accuracy. Conformal prediction supplies coverage on the keypoints, geometry propagates it to the pose as PURSE, and semidefinite relaxation converts the set into concrete worst-case bounds. Because it wraps any heatmap keypoint detector, the approach points toward provably correct perception wherever safety matters.
