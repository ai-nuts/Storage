# Method

Core claim: For each candidate node the oracle answers only "is the predicted label correct?" (yes/no), producing a normalized soft label. IGP estimates each node's influence magnitude on its neighbors, weights the information gain by that influence, and selects the budget-constrained node set that maximizes total propagated information gain.

Supporting detail: Pipeline loops Model Training (GNN on soft labels) → Node Selection (maximize IGP = influence magnitude × information gain) → Node Labeling (relaxed query → normalized label) → update. Influence magnitude uses feature-gradient / random-walk propagation over a k-layer GNN.

Narration: IGP runs in a loop. A graph network is first trained on the labeled nodes with their soft labels. For each candidate, the oracle is asked only whether the predicted label is correct, and that answer becomes a normalized soft label. To choose nodes, IGP measures how strongly each node influences its neighbors through propagation, the influence magnitude, and combines it with the information gain, the entropy reduction, of every influenced node. It then selects the budget-limited subset that maximizes total propagated information gain, updates the model, and repeats.
