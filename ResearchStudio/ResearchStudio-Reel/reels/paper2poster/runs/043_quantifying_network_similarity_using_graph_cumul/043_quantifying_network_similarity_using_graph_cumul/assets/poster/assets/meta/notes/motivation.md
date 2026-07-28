# Motivation

Core claim: Network analysis routinely characterizes structure with subgraph or motif densities, but these raw densities are strongly correlated across orders and yield statistically weak comparisons, especially with few observed graphs.

Supporting detail: Prior tests often require expensive sampling from fitted models (configuration, exponential-random-graph, geometric models) to assess significance; this work computes significance analytically instead.

Narration: Analysts commonly summarize a network by counting small substructures, called subgraphs or motifs. But the raw densities of these motifs are heavily entangled: the density of an edge is strongly correlated with the density of a wedge, and so on. This redundancy weakens any test built directly on the densities, and many existing methods must resort to costly resampling to judge whether an observed difference is significant. The authors ask whether a better set of coordinates, one that removes lower-order redundancy, can make these tests both stronger and cheaper.
