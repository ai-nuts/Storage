# Headline Numbers

Core claim: - 99.4% of target nodes (K = 1.0, B_deg+2 threat model) admit a perturbed graph with changed semantic content. - 43% over-robustness for a maximally robust classifier at K = 0.1 under the ℓ₂-weak attack.

Supporting detail: - GCN+LP over-robustness falls to 20.9% at K = 0.5. - Under Nettack, a GCN at K = 0.5 still has 11.4% over-robustness; an MLP at K = 2 still has 19.2%.

Narration: A few numbers summarize the impact. Up to ninety-nine-point-four percent of target nodes have perturbations that change their true label under a common threat model. A perfectly robust classifier shows forty-three percent over-robustness at low signal strength. Label propagation cuts a GCN's over-robustness to roughly twenty-one percent, and even under the strong Nettack attack over-robustness never fully disappears, sitting around eleven to nineteen percent depending on the model.
