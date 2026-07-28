# Method

Core claim: Under standard in-context learning (K=10 simple-task examples plus one test input), the authors evaluate four settings per composite task: each simple task alone, composite (simple-task demos, composite test), and composite in-context (composite demos, the gold-standard upper bound). They test Llama-1/2/3 and GPT families across scales on word-level and arithmetic tasks. Theoretically, they analyze a one-layer single-head linear self-attention network and show composition succeeds when the two simple tasks have "confined support", occupying separate feature subspaces of the input embedding.

Supporting detail: Separable composite tasks (sub-tasks on distinct input parts) are contrasted with compose-by-step tasks (chained multi-step reasoning that shares embedding support). The theory formalizes compositional ability and links per-task accuracy gains under scale to the separable case.

Narration: Two halves. Empirically, each composite task is tested in four settings with ten in-context examples: each simple task alone, a composite test with simple-task demos, and an all-composite gold standard. Theoretically, a linear self-attention model shows composition succeeds under confined support.
