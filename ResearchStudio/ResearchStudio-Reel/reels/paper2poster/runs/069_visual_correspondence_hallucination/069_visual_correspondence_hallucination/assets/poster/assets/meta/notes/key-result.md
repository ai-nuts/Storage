# Key Result

Core claim: NeurHal hallucinates correspondences on unseen scenes for both inpainting (occluded) and outpainting (out-of-frame) tasks, with argmax errors concentrated far below the random-prediction average, while state-of-the-art matching methods (LoFTR, DRC-Net, S2DNet) produce poor inpainting and essentially zero outpainting.

Supporting detail: For absolute pose, NeurHal estimates the camera pose correctly significantly more often than any competitor on low-overlap pairs, because it is the only method able to outpaint correspondences.

Narration: The experiments confirm both research questions. NeurHal successfully hallucinates correspondences on scenes it never saw during training, for occluded points that must be inpainted and for out of frame points that must be outpainted, with prediction errors concentrated well below what random guessing would give. State of the art matching methods like LoFTR, DRC Net, and S two D Net do poorly on inpainting and essentially cannot outpaint at all, since they only ever search inside the image boundaries. And on absolute camera pose estimation, NeurHal is correct far more often than any competitor on low overlap pairs, precisely because it is the only method that can outpaint.
