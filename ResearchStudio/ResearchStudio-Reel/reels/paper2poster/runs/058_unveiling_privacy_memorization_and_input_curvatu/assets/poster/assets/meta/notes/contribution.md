# Contribution

Core claim: Three theorems: (1) input loss curvature upper-bounds memorization; (2) the differential-privacy parameter upper-bounds average input loss curvature; (3) privacy upper-bounds memorization, all validated empirically.

Supporting detail: The analysis makes no assumptions about Hessian convexity or definiteness, unlike influence-function theory, making it suitable for deep networks.

Narration: The paper proves three links in a triangle connecting memorization, input loss curvature, and differential privacy. First, curvature upper-bounds memorization. Second, the privacy parameter upper-bounds average curvature. Third, privacy bounds memorization directly. None assume Hessian convexity, so they hold for real deep networks, and all three are validated empirically.
