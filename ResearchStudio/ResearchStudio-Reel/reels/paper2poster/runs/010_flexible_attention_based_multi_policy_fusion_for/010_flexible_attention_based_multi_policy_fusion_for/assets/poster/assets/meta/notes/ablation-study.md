# Ablation Study

Core claim: Ablating the entropy-imbalance fix (comparing KIAN with and without the modified policy distributions) shows the modifications are essential: without them performance drops sharply on harder tasks like Dynamic-Obstacles-16x16, MultiRoom-N4-S5, and continuous Pick-and-Place, Push, and Slide.

Supporting detail: Compositional and incremental experiments show KIAN reuses previously learned knowledge keys and inner policies to learn two tasks sequentially with fewer samples than learning them separately.

Narration: A key ablation isolates the paper's fix for entropy imbalance. When KIAN runs with the original policy fusion, an agent maximizing entropy for exploration collapses onto a single policy and struggles, especially on demanding tasks like dynamic obstacles, multi-room mazes, and the robotic manipulation tasks. Switching on the modified policy distributions restores efficient exploration and recovers strong performance. Separate compositional and incremental experiments confirm the modular design pays off: KIAN reuses its learned keys and inner policy to acquire new tasks sequentially with fewer samples than training each task from scratch.
