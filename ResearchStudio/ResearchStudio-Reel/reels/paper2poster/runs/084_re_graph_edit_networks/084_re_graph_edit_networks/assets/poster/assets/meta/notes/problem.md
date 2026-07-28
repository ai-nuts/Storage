# Problem

Core claim: Predicting how a graph evolves over time is hard: most graph neural networks output node or edge scores, not the explicit, interpretable sequence of structural changes needed to turn one graph into the next.

Supporting detail: Graph Edit Networks (GEN) address this with an output layer that emits edit scripts, but the original claims rest on lightly-described synthetic benchmarks and untested scaling arguments.

Narration: Graph time-series prediction asks a model to forecast the next graph in a sequence, not just a label. Standard graph networks emit node or edge probabilities, which can't naturally express the structural operations that transform one graph into the next.
