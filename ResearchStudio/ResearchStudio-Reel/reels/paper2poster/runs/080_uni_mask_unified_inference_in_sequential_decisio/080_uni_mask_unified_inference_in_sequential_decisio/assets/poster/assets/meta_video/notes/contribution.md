# Contribution

Core claim: The paper introduces Uni[MASK], a framework that expresses inference tasks in sequential decision problems as input masking schemes, letting one model be trained on many tasks at once.

Supporting detail: It shows a single Uni[MASK] model matches or beats single-task models across tasks, and consistently outperforms them after fine-tuning; it also introduces an improved GPT baseline, Decision-GPT.

Narration: The main contribution is the Uni-MASK framework, a unified way to specify models for sequential decision making by casting each inference task as a masking scheme over a trajectory of states, actions, and reward-to-go tokens. Because tasks are just maskings, a single model can be trained to perform behavior cloning, reward conditioning, dynamics modeling, and goal or waypoint conditioning together. The authors show this single model often matches or exceeds specialized single-task models, and consistently outperforms them after fine-tuning. Along the way they also introduce Decision-GPT, an improved GPT-based baseline.
