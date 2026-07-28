# Ablation Study

Core claim: Transfer ablations show that agents transferring encoder and memory from a NeuPL network trained to epoch 1,000 learn exploiters to strong Nash mixtures (n=4 and n=7 policies) that randomly-initialized agents fail to counter even with prolonged training.

Supporting detail: Against an easy mixture (n=2) even the random-init agent eventually succeeds, only slower; the gap widens sharply against competent opponents, and each transfer experiment is repeated five times.

Narration: "A key ablation isolates the role of transfer. NeuPL agents are re-initialized either from scratch or by transferring the encoder and memory components of a network trained to epoch one thousand, then tasked with beating fixed Nash mixtures of increasing strength. Against an easily exploitable two-policy mixture, even the from-scratch agent eventually finds a counter, just more slowly. But against competent mixtures over four or seven policies, the randomly initialized agent fails outright despite prolonged training, while the transferred agent readily discovers the exploit. This is NeuPL's most striking property: as the population expands, discovering new strategies becomes easier, not harder."
