# Ablation Study

Core claim: Ablations isolate each component: spatial convolution strongly improves supervised molecular representation learning (loss curves over 40 runs); removing innovation rewards (GAPN vs DGAPN) worsens top docking (−9.19 vs −10.07); and DGAPN even beats a CReM greedy oracle that sees intermediate docking rewards.

Supporting detail: Innovation bonuses improve docking but slightly worsen synthetic accessibility (SA), revealing a docking-vs-SA trade-off; a separate evaluation mode (DGAPN-eval) reaches −10.38 best and −7.73 mean docking.

Narration: The authors ablate each component. In a supervised setting on NSP15, loss curves over forty runs show spatial convolution strongly improves molecular representation learning. Comparing full DGAPN against GAPN without the innovation reward, the curiosity bonus lifts the best docking score, though it slightly worsens synthetic accessibility. Remarkably, DGAPN even beats a greedy CReM oracle that sees intermediate docking rewards.
