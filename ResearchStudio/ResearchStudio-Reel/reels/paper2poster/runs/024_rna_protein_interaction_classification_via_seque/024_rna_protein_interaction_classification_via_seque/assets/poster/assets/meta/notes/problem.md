# Problem

Core claim: Predicting whether an arbitrary non-coding RNA and protein interact, from sequence alone, is largely unsolved: most methods are protein-specific and need large per-protein interaction datasets that exist for only a few hundred of the ~2,000 human RNA-binding proteins.

Supporting detail: Experimental assays like SELEX and CLIP-seq are time-consuming and expensive, and RNA structural features that drive interactions are not available at scale.

Narration: Non-coding RNAs regulate the cell largely through their interactions with proteins, but mapping these interactions experimentally is slow and costly. Most computational predictors sidestep the general problem by training one model per protein, which requires a large interaction dataset for that specific protein. Such datasets exist for only a few hundred of the roughly two thousand human RNA-binding proteins. What is missing is a method that decides, for any given RNA and protein pair, whether they interact using nothing but their sequences.
