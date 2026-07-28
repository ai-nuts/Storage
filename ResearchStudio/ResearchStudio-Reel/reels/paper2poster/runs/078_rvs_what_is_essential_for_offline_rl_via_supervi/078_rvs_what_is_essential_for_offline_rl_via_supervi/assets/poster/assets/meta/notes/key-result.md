# Key Result

Core claim: A simple two-layer MLP is state-of-the-art on AntMaze (RvS-G 53.5 average vs 50.6 for the best baseline), Kitchen (RvS-G 54.0), and GCSL (RvS-G 62.0 vs 58.0 for online GCSL), and on Gym RvS-R matches Decision Transformer using only an MLP.

Supporting detail: RvS-G surprisingly matches dynamic-programming methods on subtrajectory-stitching tasks (mixed Kitchen, all AntMaze), where value-based methods were thought essential.

Narration: The headline result is striking. Using nothing but a two-layer feedforward network trained with maximum likelihood, RvS reaches state-of-the-art performance across several suites. On AntMaze, goal-conditioned RvS scores fifty-three point five on average, edging out the best value-based baseline at fifty point six. On Franka Kitchen it reaches fifty-four. On the GCSL suite it scores sixty-two, beating the online GCSL method at fifty-eight, despite using only offline data. And on Gym Locomotion, reward-conditioned RvS matches Decision Transformer while using a simple multilayer perceptron instead of a large Transformer. Even on stitching tasks, long thought to demand dynamic programming, goal-conditioned RvS keeps pace.
