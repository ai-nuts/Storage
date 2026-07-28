# Dataset / Benchmark

Core claim: Evaluation uses the offline goal-conditioned benchmark of Yang et al. (2021): 10 control tasks with maximum trajectory length T=50, a sparse binary reward, and both "expert" and "random" dataset settings.

Supporting detail: The suite spans easier tasks (PointReach, PointRooms, Reacher, SawyerReach, SawyerDoor, FetchReach, 2000 trajectories each) and harder tasks (FetchPush, FetchPick, FetchSlide, HandReach, 40000 trajectories each), with both state-space and pixel-space observation variants.

Narration: The authors evaluate Merlin on a standard offline goal-conditioned benchmark of ten control tasks, ranging from simple point navigation and reacher tasks to harder Fetch manipulation tasks like pushing, picking, and sliding, plus the high-dimensional HandReach task. Every task uses a sparse binary reward and a maximum trajectory length of fifty steps. Each task comes in two flavors: an expert dataset collected by a trained policy with added noise for diversity, and a random dataset collected by sampling random actions. They test both low-dimensional state observations and high-dimensional pixel observations, and average all results over ten random seeds.
