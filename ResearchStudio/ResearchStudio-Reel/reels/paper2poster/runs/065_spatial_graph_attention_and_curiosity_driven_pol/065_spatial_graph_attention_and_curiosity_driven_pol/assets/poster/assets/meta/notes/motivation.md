# Motivation

Core claim: Prior generative models under-encode molecular information, ignoring spatial structure and rich edge attributes, and rely on inefficient node-by-node action spaces that produce hard-to-synthesize molecules and explore poorly.

Supporting detail: Spatial structure matters because molecular volume and the geometry of interaction sites govern how well a candidate complements a receptor binding site, which is essential for antiviral efficacy.

Narration: Prior methods leave value on the table twice. First, most graph networks encode only atom attributes and adjacency, ignoring bond features and 3D geometry, even though shape and complementarity to the receptor pocket make a good binder. Second, building molecules atom by atom gives long, unstable trajectories and hard-to-synthesize products. This motivates encoding spatial structure while acting over whole fragments.
