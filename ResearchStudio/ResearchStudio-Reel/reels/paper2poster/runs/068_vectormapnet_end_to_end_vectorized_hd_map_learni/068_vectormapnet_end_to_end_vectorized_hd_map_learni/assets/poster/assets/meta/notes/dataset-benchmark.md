# Dataset / Benchmark

Core claim: Experiments run on nuScenes and Argoverse2, evaluating predicted polylines against ground truth with Chamfer-distance AP and a newly introduced Fréchet-distance AP (which accounts for vertex order) at thresholds of 0.5, 1.0, and 1.5 m.

Supporting detail: Map elements are pedestrian crossings, lane dividers, and road boundaries; Argoverse2 provides z-axis annotations, enabling 2D and 3D evaluation.

Narration: VectorMapNet is evaluated on nuScenes and Argoverse2. Following HDMapNet, predicted polylines are compared to ground truth for crosswalks, lane dividers, and road boundaries. It reports Chamfer-distance average precision and a new Fréchet-distance AP that respects vertex order, plus 3D evaluation on Argoverse2.
