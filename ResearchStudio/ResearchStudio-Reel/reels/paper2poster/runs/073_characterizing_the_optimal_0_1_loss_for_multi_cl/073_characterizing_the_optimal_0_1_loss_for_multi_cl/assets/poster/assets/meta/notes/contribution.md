# Contribution

Core claim: (1) Extends the conflict-graph framework to multi-class, expressing the optimal 0-1 loss as a linear program on a conflict hypergraph; (2) develops efficient upper and lower bounds that determine the range of the optimal loss; (3) an extensive empirical analysis of the gap between adversarially trained classifiers and the optimum.

Supporting detail: The bounds are cast as classifier-attacker games, connecting truncated-hypergraph lower bounds, aggregated binary lower bounds, and a generalized Caro-Wei upper bound.

Narration: The paper makes three contributions. First, it generalizes the conflict-graph framework from binary to multi-class classification, showing the optimal 0-1 loss is the solution of a linear program built on a conflict hypergraph. Second, because that exact program can become computationally prohibitive, it develops several more efficient bounds, both lower and upper, that bracket the range in which the true optimal loss must lie. Third, it delivers an extensive empirical study, giving the first analysis of the gap to optimal robustness for classifiers in the multi-class setting on benchmark datasets.
