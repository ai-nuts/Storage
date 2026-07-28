# Dataset / Benchmark

Core claim: Evaluated on OC20 (IS2RE invariant, IS2RS equivariant; 460,328 complexes), PCQM4Mv2 (~3.37M molecules), Molecule3D (~2.34M, random & scaffold splits), N-body simulation (3,000 training trajectories), and MD17 force-field modeling.

Supporting detail: Tasks span invariant prediction (energy, HOMO-LUMO gap) and equivariant prediction (relaxed structure, particle positions, forces), covering adsorbate-catalyst complexes, simple molecules, and particle systems.

Narration: The authors evaluate GeoMFormer across a broad suite of tasks that together stress both invariant and equivariant abilities. On the Open Catalyst 2020 dataset, spanning over four hundred sixty thousand adsorbate-catalyst complexes, they test both the Initial Structure to Relaxed Energy task, which is invariant, and the Initial Structure to Relaxed Structure task, which is equivariant. On the large quantum chemistry datasets PCQM4Mv2 and Molecule3D, with millions of molecules, they predict the HOMO-LUMO energy gap. They further use a synthetic five-particle N-body simulation to test equivariant position prediction, and the MD17 dataset for force-field modeling in the ablation studies. This breadth lets a single architecture be judged on both scalar and vector prediction.
