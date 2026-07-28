# Problem

Core claim: Autonomous driving needs vectorized HD semantic maps, but offline manual annotation does not scale and existing learning-based methods only output dense rasterized segmentations that require heuristic post-processing to vectorize.

Supporting detail: Rasterized maps lack per-instance information, cannot enforce spatial consistency, and are incompatible with downstream modules that consume instance-level 2D/3D vectorized maps.

Narration: Self-driving cars need HD maps marking lanes, boundaries, and crosswalks. Today these are annotated by hand, which is costly and does not scale. Learning methods instead predict a dense pixel grid, but a grid carries no individual elements and needs brittle post-processing before a planner can use it.
