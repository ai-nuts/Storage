# Ablation Study

Core claim: Training NeurHal on all three tasks (identification + inpainting + outpainting) gives the best pose-estimation robustness; adding outpainting is critical for low-overlap pairs, while adding inpainting brings little improvement.

Supporting detail: A pose is counted correct when rotation error < 20° and translation error < 1.5 m, evaluated as a function of the maximum image-pair overlap on ScanNet.

Narration: An ablation on ScanNet isolates what each task contributes to pose robustness. Training NeurHal on all three tasks together, identification, inpainting, and outpainting, gives the best results. The key finding is that adding the outpainting task is what drives the improvement on low overlap pairs, where most correspondents fall outside the target's field of view. Adding inpainting, by contrast, brings little additional benefit to camera pose estimation. Here a pose counts as correct when rotation error is under twenty degrees and translation error under one point five meters.
