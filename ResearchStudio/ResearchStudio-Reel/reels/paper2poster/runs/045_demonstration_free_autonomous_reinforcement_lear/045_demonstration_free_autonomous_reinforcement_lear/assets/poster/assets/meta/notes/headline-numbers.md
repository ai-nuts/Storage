# Headline Numbers

Core claim: - 6 sparse-reward environments (2 from the EARL benchmark + 4 modified MuJoCo/Gym tasks), evaluated over 5 random seeds. - ~10 target states (sometimes a single example) needed to specify ρ_tar(s), versus the thousands of demonstration transitions required by prior ARL methods. - IBC matches episodic oracle RL success rates while using 0 demonstrations and 0 manual resets.

Supporting detail: K curriculum candidates (default 50 trajectories) are matched into K forward + K auxiliary goals; the curriculum buffer holds up to 1000 trajectories and updates once every 20 episodes.

Narration: A few numbers capture the impact. IBC was tested on six sparse-reward environments, two from the established EARL benchmark and four adapted MuJoCo tasks, each run over five random seeds. To define its target distribution, it needs only about ten example states, and sometimes just one, compared with the thousands of demonstration transitions that prior autonomous methods require. And despite using zero demonstrations and zero manual resets, it reaches success rates comparable to an oracle agent trained in the far easier episodic setting. In short: none of the usual crutches, and roughly the same performance.
