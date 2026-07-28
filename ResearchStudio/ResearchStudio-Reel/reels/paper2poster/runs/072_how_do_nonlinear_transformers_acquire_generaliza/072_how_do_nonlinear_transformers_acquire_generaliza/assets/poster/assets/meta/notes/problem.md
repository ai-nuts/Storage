# Problem

Core claim: Transformers show strong in-context learning (ICL), yet why training yields ICL and how well the trained model generalizes is largely unknown, because nonlinear self-attention and nonlinear MLP make the training objective nonconvex and hard to analyze.

Supporting detail: No prior theory characterizes how to train a model to reach ICL under distribution-shifted data, nor how model pruning affects ICL performance.

Narration: In-context learning lets a pretrained Transformer handle new tasks by simply padding the query with a handful of example input-output pairs, no fine-tuning required. Despite its empirical success, the mechanics of how a Transformer is actually trained to acquire this ability, and how far that ability generalizes, remain elusive. The core difficulty is technical: the self-attention layer is nonlinear through the softmax, and the MLP is nonlinear through the ReLU activation, so the training problem is nonconvex and resists the tools used for simpler models.
