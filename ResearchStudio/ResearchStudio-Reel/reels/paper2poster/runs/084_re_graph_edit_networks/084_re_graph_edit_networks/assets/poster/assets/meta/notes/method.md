# Method

Core claim: GEN is an output layer for GNNs that, given the current graph and a teaching signal derived from a reference mapping, predicts an edit script, a finite sequence of node insertions, deletions, replacements and edge insertions/deletions, that transforms the current graph into the next under a Markovian assumption.

Supporting detail: Reference pair mappings are obtained via graph-edit-distance approximators (exact distance is NP-hard), then converted into per-node teaching signals; the reproduction trains GEN variants with adapted hinge and cross-entropy losses, plus flexible and fixed edge filtering for large graphs, against a modified Variational Graph Autoencoder baseline.

Narration: A graph edit network attaches to a standard GNN backbone and predicts a script of edits: insert, delete or replace a node, or insert or delete an edge. Applying them in sequence maps the current graph to the next. Training uses reference mappings from graph-edit-distance approximators, with two loss variants, hinge and cross-entropy, and edge-filtering for citation graphs.
