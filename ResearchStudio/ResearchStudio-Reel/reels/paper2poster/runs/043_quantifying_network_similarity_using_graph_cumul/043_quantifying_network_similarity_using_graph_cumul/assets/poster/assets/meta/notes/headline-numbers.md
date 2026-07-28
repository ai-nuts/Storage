# Headline Numbers

Core claim: Moment test requires s ≥ 4 graphs per sample to be defined; cumulant test works down to s = 1. Both tests use connected subgraphs up to r = 3 edges at identical O(n^ω) complexity. The cumulant test statistic closely matches a χ² distribution (5 degrees of freedom) even for small s, while the moment statistic deviates.

Supporting detail: Real-network experiments span organisms with ~1.1×10⁴ to ~1.6×10⁴ nodes and ~7.9×10⁵ to ~1.39×10⁶ edges, all density-matched.

Narration: A few numbers capture the impact. The moment test needs at least four graphs per sample just to be defined; the cumulant test works with as few as one. Both use connected subgraphs up to three edges and share the same order-n-to-the-omega computational complexity, so the gain is free. And under the null hypothesis, the cumulant statistic hugs a chi-squared distribution with five degrees of freedom even for small samples, where the moment statistic visibly deviates. The real networks tested range from about eleven thousand to sixteen thousand nodes and hundreds of thousands of edges, all matched in density.
