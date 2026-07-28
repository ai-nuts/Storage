# 01_title

This is a reproducibility study of Graph Edit Networks, a graph neural network output layer that predicts how a graph changes over time as a sequence of interpretable edits. The reproduction re-implements the model and re-tests the paper's four experimental claims.

---

# 02_problem

Graph time-series prediction asks a model to forecast the next graph in a sequence, not just a label. Standard graph networks emit node or edge probabilities, which can't naturally express the structural operations that transform one graph into the next.

---

# 03_motivation

Graph Edit Networks close this gap by predicting an explicit, human-readable edit script. The original work claims it beats every baseline, reaches perfect accuracy on trees, and scales to large graphs, but those claims rest on briefly-described benchmarks, where independent reproduction adds value.

---

# 04_contribution

The reproduction contributes four things: it re-runs the model and baseline to check each claim; it documents the synthetic data generators the paper omitted; it adds a cleaner setup separating training and test series; and it shows some benchmarks let the model win by memorising seen transitions.

---

# 05_method

A graph edit network attaches to a standard GNN backbone and predicts a script of edits: insert, delete or replace a node, or insert or delete an edge. Applying them in sequence maps the current graph to the next. Training uses reference mappings from graph-edit-distance approximators, with two loss variants, hinge and cross-entropy, and edge-filtering for citation graphs.

---

# 06_dataset-benchmark

Benchmarks span three families: dynamical graph systems like Edit Cycles, Degree Rules and Game of Life; tree systems for Boolean-formula simplification and Peano addition; and, for scaling, an arXiv citation network of about twenty-seven thousand papers yielding fifteen hundred sub-graphs up to nearly three thousand nodes.

---

# 07_key-result

Three of the four original claims hold: the model beats the variational-autoencoder baseline on every dynamical task, reaches near-perfect accuracy on trees, and its forward pass grows sub-quadratically. The fourth fails: backward passes were claimed to scale linearly, but the fitted exponent is clearly above one.

---

# 08_ablation-study

Two robustness checks: swapping the ad-hoc initialisation for Erdős–Rényi and configuration-model generators barely changes any metric, and adding a proper held-out test set lowers scores slightly. But a deeper diagnostic finds the tree generators mostly produce unsimplifiable trees, only thirteen percent of Boolean and twenty-six percent of Peano samples are usable, undercutting those tasks.

---

# 09_takeaway

The verdict is nuanced: Graph Edit Networks are reproducible, elegant and interpretable, and most claims hold. But one scaling claim is wrong, backward passes are super-linear, and several benchmarks reward memorising seen transitions rather than genuine generalisation.

