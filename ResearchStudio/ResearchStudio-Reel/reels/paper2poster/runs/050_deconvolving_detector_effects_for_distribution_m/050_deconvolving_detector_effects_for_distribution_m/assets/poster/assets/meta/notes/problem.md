# Problem

Core claim: Deconvolving ('unfolding') detector distortions is critical for comparing cross-section measurements with theory, yet most unfolding methods require histogram binning even though many theoretical predictions are stated at the level of moments.

Supporting detail: Binning the two-dimensional (X, Y) support to compute moments of X in bins of Y introduces discretization artifacts that limit precision.

Narration: Unfolding, also known as deconvolution, corrects the distortions a detector imprints on measured data so that experiments can be compared with each other and with theory. The usual recipe unfolds an entire spectrum after first discretizing it into a histogram, then computes moments from that histogram. But this binning step introduces discretization artifacts, and it is wasteful when the quantity you actually care about is just a small set of moments as a function of another observable. That mismatch between binned data and moment-level theory predictions is the gap this paper closes.
