# Ablation Study

Core claim: Even though the first and second moments of the reweighted generation match the truth well, the full jet-width distributions remain not statistically identical, because higher moments differ between truth and generation and are not constrained by unfolding only two moments.

Supporting detail: This highlights the intended scope of the method: it targets a chosen small set of moments rather than the entire density, so residual differences appear in the uncontrolled higher moments.

Narration: One instructive observation concerns the limits of unfolding only a couple of moments. After Moment Unfolding matches the first and second moments of the jet width, the full distributions of truth and reweighted generation still are not statistically identical. The reason is simply that higher moments remain relevant and were not part of the fit. This is expected behavior, and it clarifies that the technique deliberately controls the specific moments you ask for, leaving the rest free.
