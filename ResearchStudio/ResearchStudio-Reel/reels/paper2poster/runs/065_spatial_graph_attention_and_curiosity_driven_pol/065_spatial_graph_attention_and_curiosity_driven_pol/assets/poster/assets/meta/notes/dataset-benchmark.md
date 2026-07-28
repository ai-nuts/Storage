# Dataset / Benchmark

Core claim: Experiments target designing inhibitors for the SARS-CoV-2 NSP15 protein, using a dataset of purchasable molecules (Kiss et al., 2012) with docking scores against NSP15. The method is also evaluated on the standard QED and penalized LogP optimization tasks.

Supporting detail: Molecular docking scores are computed with a GPU-accelerated automated docking tool using the protein's 3D structure and the coordinates of a targeted functional site; molecules failing conformer generation get a docking score of 0 under an "adjusted validity" criterion.

Narration: The primary benchmark designs novel inhibitors binding the NSP15 site of SARS-CoV-2. Binding affinity is estimated by molecular docking, using a GPU-accelerated tool on the protein's 3D structure, starting from a dataset of purchasable molecules with NSP15 docking scores. The method is also tested on standard QED and penalized LogP optimization tasks.
