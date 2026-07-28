# Contribution

Core claim: (1) A case study showing GNN expressivity does not fix confidence-indicator calibration under shift; (2) G-∆UQ, a new single-model UQ method extending stochastic centering to graphs with partial stochasticity, including a pretrained-model variant; (3) extensive evaluation across three shift types and three safety tasks.

Supporting detail: The method supports three anchoring variants (node-feature, intermediate MPNN, and READOUT), trading off the level of stochasticity and enabling reuse of pretrained backbones.

Narration: The paper makes three contributions. First, a rigorous case study establishing that improving graph neural network expressivity does not mitigate poor calibration under distribution shift. Second, G-Delta-UQ, a novel single-model uncertainty method that extends the stochastic centering framework to structured graph data and, crucially, supports partial stochasticity so that only part of the network is made stochastic. Third, an extensive empirical evaluation spanning covariate, concept, and graph size shifts, across the safety-critical tasks of calibration, generalization gap prediction, and out-of-distribution detection.
