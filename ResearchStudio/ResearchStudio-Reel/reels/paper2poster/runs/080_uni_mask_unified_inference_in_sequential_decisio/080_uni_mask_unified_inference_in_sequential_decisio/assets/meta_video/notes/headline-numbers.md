# Headline Numbers

Core claim: - Maze2D reward (context length 5, BC): Uni[MASK] multi-task + finetune 2.73 vs Decision Transformer 1.13 - Maze2D reward (context length 5, RC): Uni[MASK] finetune 2.73 vs Decision Transformer 1.49 - One model performs behavior cloning, reward conditioning, dynamics, goal and waypoint conditioning

Supporting detail: - Results averaged over 6 seeds (MiniGrid) and 5 seeds / 1000 rollouts (Maze2D) - Random-mask + finetune beats single-task on all MiniGrid tasks except behavior cloning

Narration: A few numbers capture the impact. In Maze2D at context length five, the fine-tuned Uni-MASK models reach reward around two point seven three on both behavior cloning and reward conditioning, compared to just one point one three and one point four nine for the Decision Transformer, and around one point five to one point seven for a feedforward network. These results are averaged over five seeds and one thousand rollouts. And critically, a single Uni-MASK model handles behavior cloning, reward conditioning, dynamics modeling, and goal and waypoint conditioning all at once.
