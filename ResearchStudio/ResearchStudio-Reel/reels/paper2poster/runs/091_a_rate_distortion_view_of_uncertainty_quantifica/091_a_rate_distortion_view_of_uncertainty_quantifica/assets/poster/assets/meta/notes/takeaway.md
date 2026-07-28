# Takeaway

Core claim: Casting uncertainty as compressing training data into a learned codebook lets a single deterministic network measure how far new inputs are from what it has seen, matching or beating expensive ensembles.

Supporting detail: DAB provides a unified, GP-like notion of uncertainty for both classification and regression that can even be attached post-hoc to large pre-trained models.

Narration: The takeaway is that recasting uncertainty as the problem of compressing training data into a learned codebook gives a single deterministic network a genuine sense of distance from what it has seen, letting it match or beat expensive ensembles at a fraction of the cost. Because the notion of distance is statistical rather than geometric, DAB offers a unified, Gaussian-Process-like view of uncertainty that works for both classification and regression, and can even be attached after the fact to large pre-trained models.
