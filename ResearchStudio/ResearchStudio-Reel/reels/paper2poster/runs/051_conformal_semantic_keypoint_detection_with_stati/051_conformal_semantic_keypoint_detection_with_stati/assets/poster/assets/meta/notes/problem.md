# Problem

Core claim: Two-stage object pose estimators (detect keypoints, then solve PnP) perform well on benchmarks but offer no provable guarantee on the quality or uncertainty of the estimated 6D pose.

Supporting detail: Safety-critical uses (autonomous driving, robotic manipulation, space robotics) need provably correct estimates with formal worst-case error bounds, which prior pipelines lack.

Narration: Estimating an object's 6D pose from an image underlies augmented reality, autonomous driving, robotic manipulation, and space robotics. The dominant recipe is two stages: first detect semantic keypoints, then recover the pose by minimizing reprojection error through Perspective-n-Points. These methods score well on benchmarks, yet they return a single pose with no statement about how trustworthy it is. For safety-critical systems that is a serious gap: no guarantee on the keypoints, no guarantee the optimizer found the right pose, and no formal bound on the worst-case error against the truth.
