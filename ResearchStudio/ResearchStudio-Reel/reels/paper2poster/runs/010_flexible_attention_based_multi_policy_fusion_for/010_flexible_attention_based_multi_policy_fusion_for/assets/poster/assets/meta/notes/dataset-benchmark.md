# Dataset / Benchmark

Core claim: KIAN is evaluated on two benchmark suites: MiniGrid (discrete action spaces, tasks like Empty-Random, Unlock, DoorKey, Dynamic-Obstacles, LavaCrossing, MultiRoom, KeyCorridor) and OpenAI-Robotics (continuous control: Push, Slide, Pick-and-Place, Reach).

Supporting detail: Every method shares the same initial external knowledge set of sub-optimal if-else programs (e.g. pickup_a_key, move_forward_to_the_goal) that cannot solve tasks alone. All runs use ten random seeds with 95% confidence-interval error bands.

Narration: The experiments span two families of environments. MiniGrid provides discrete-action grid-world tasks of increasing difficulty, from empty rooms to door-key puzzles, dynamic obstacles, lava crossings, multi-room mazes, and key corridors. OpenAI-Robotics provides continuous-control manipulation tasks such as Push, Slide, Pick-and-Place, and Reach. Crucially, every method starts from the same initial knowledge set built from simple if-else programs that are deliberately sub-optimal and cannot complete any task on their own. Each experiment is repeated with ten random seeds, and the reported learning curves show ninety-five percent confidence intervals.
