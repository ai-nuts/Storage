# Key Result

Core claim: In MiniGrid, random-mask training outperforms single-task on all tasks, and random-mask pretraining plus fine-tuning gives the best performance, beating single-task on every task except behavior cloning.

Supporting detail: In Maze2D, fine-tuning is critical: multi-task-plus-fine-tune and random-mask-plus-fine-tune Uni[MASK] models beat all baselines at context length 5, reaching reward around 2.73 to 2.74 versus 1.13 to 1.49 for Decision Transformer.

Narration: In the MiniGrid environment, a single model trained with random masking outperforms single-task models on all tasks, and adding task-specific fine-tuning on top of random-mask pretraining gives the best performance of all, beating single-task models on every task except behavior cloning. This means that even if you only care about one inference task, first training on many tasks generally helps. In the harder Maze2D environment, fine-tuning becomes critical: the fine-tuned Uni-MASK models reach rewards around two point seven, outperforming every baseline at context length five, including a Decision Transformer that scores only around one point one to one point five.
