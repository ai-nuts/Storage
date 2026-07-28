---
title: Visual Correspondence Hallucination
authors: Hugo Germain¹, Vincent Lepetit¹, Guillaume Bourmaud²
institutes: ¹LIGM, École des Ponts, Univ Gustave Eiffel, CNRS, Marne-la-Vallée, France; ²IMS, University of Bordeaux, Bordeaux INP, CNRS, Bordeaux, France
venue: ICLR 2022
paper_url: https://arxiv.org/abs/2106.09711
code_url:
title_audio_script: Given two partially overlapping images and a keypoint in the first, where does its match land in the second? Local feature matching only answers when the point is visible. But humans can also guess, or hallucinate, where an occluded or out of frame point should be, using geometric reasoning. This paper, Visual Correspondence Hallucination from ICLR 2022, trains a single network called NeurHal to output a peaked probability distribution over the correspondent's location whether it is visible, occluded, or outside the field of view, and shows this makes absolute camera pose estimation far more robust.
---

## Problem
**Necessary:** Local feature matching only locates a keypoint's correspondent when it is visible; occluded or out-of-frame correspondents are treated as noise, so matching fails when few keypoints are covisible.
**Additional:** Humans instead reason geometrically to predict, or hallucinate, where non-covisible correspondents lie, a capability prior methods lack.
**Audio script:** Establishing correspondences between two overlapping images underlies much of computer vision, from localization to reconstruction. But local feature matching only works when a keypoint is actually visible in both images. When the correspondent is occluded, or when it falls outside the field of view of the second image, these methods have nothing to say, and they simply treat those regions as noise. So whenever two images share little overlap, matching breaks down.

## Motivation
**Necessary:** State-of-the-art localization relies on keypoint matches, yet these matching methods collapse on low-overlap image pairs where most locations are occluded or outside the field of view.
**Additional:** Geometric reasoning has only been used a posteriori (RANSAC-style outlier removal), never to actively predict correspondences at non-covisible locations.
**Audio script:** Humans do not give up in these situations. Faced with an occluded or out of frame point, a person reasons about the geometry of the scene and predicts, or hallucinates, where the match should be. Classical vision does use geometric reasoning, but only after the fact, to filter out bad matches with models like epipolar geometry. No prior method actually predicts correspondences at locations that are not covisible. That gap is exactly what this work targets.

## Contribution
**Necessary:** The paper introduces the task of correspondence hallucination and NeurHal, a network that, given a source/target image pair and source keypoints, outputs for every keypoint a probability distribution over its correspondent's location regardless of visibility, unifying identifying, inpainting, and outpainting.
**Additional:** It analyzes the specific features of this novel learning task, which motivate the loss and the non-siamese, cross-attention architecture, and shows the ability benefits absolute camera pose estimation.
**Audio script:** The paper introduces the task of visual correspondence hallucination and a network to solve it, called NeurHal, for Neural Hallucinations. Given a pair of overlapping images and keypoints in the source image, NeurHal outputs, for each keypoint, a probability distribution over its correspondent's location in the target image, whether that location is visible, occluded, or outside the field of view. This unifies three tasks the authors name identifying, inpainting, and outpainting. Because learning to hallucinate is unexplored territory, they first analyze what makes the task distinctive, and let that analysis drive the choice of loss and architecture.

## Method
**Necessary:** A siamese CNN backbone produces dense descriptor maps for source and target; the target map is padded with a learnable vector λ to represent locations outside the field of view. A cross-attention backbone with positional encoding lets source and target descriptors communicate, producing a per-keypoint feature dS,n and dense target features; each correspondence map CT,n is formed by a 1×1 convolution of the target features using dS,n as filter followed by a 2D softmax.
**Additional:** Training minimizes a sum of Neural Reprojection Error (NRE) terms by SGD with early stopping; there is no covisibility assumption and no need to label keypoints as visible/occluded/outside — the network only ever outputs correspondence maps. Maps are kept low resolution (e.g. 160×120 for a 640×480 target with stride 8, γ=50%).
**Key equation:** `$\mathrm{NRE}(p_S, C_T, R_{TS}, t_{TS}, d_S) := -\ln C_T(x_T)\ \text{where}\ x_T = K_C\,\omega(d_S, p_S, R_{TS}, t_{TS})$`
**Audio script:** Here is how NeurHal works. A siamese convolutional backbone turns both images into dense descriptor maps. To allow correspondents outside the target's field of view, the target map is padded with a learnable vector, initializing descriptors beyond the image borders. A cross attention backbone with positional encoding then lets source and target descriptors exchange information, which is what enables the network to hallucinate peaked distributions for occluded and out of frame points. Each keypoint's feature is convolved over the target features and passed through a two D softmax to produce a correspondence map. Training minimizes a sum of Neural Reprojection Error terms, the negative log likelihood of the true reprojected location, with no covisibility assumption and no need to label points as visible or hidden.

## Dataset / Benchmark
**Necessary:** Evaluated on indoor scenes ScanNet and NYU Depth, and outdoor scenes MegaDepth and ETH-3D; NeurHal is trained on ScanNet for the indoor setting and on MegaDepth for the outdoor setting, then tested on scenes unseen at training time.
**Additional:** Absolute camera pose estimation is evaluated on the ScanNet test set over 2,500 source/target image pairs from held-out scenes.
**Audio script:** The method is evaluated across both indoor and outdoor domains. Indoors, NeurHal is trained on ScanNet and also tested on the NYU Depth dataset; outdoors, it is trained on MegaDepth and tested on ETH three D. Crucially, every evaluation uses scenes that were never seen during training, so the results measure genuine generalization. For the downstream application, absolute camera pose estimation is measured on twenty five hundred source and target image pairs from held out ScanNet scenes.

## Key Result
**Necessary:** NeurHal hallucinates correspondences on unseen scenes for both inpainting (occluded) and outpainting (out-of-frame) tasks, with argmax errors concentrated far below the random-prediction average, while state-of-the-art matching methods (LoFTR, DRC-Net, S2DNet) produce poor inpainting and essentially zero outpainting.
**Additional:** For absolute pose, NeurHal estimates the camera pose correctly significantly more often than any competitor on low-overlap pairs, because it is the only method able to outpaint correspondences.
**Audio script:** The experiments confirm both research questions. NeurHal successfully hallucinates correspondences on scenes it never saw during training, for occluded points that must be inpainted and for out of frame points that must be outpainted, with prediction errors concentrated well below what random guessing would give. State of the art matching methods like LoFTR, DRC Net, and S two D Net do poorly on inpainting and essentially cannot outpaint at all, since they only ever search inside the image boundaries. And on absolute camera pose estimation, NeurHal is correct far more often than any competitor on low overlap pairs, precisely because it is the only method that can outpaint.

## Ablation Study
**Necessary:** Training NeurHal on all three tasks (identification + inpainting + outpainting) gives the best pose-estimation robustness; adding outpainting is critical for low-overlap pairs, while adding inpainting brings little improvement.
**Additional:** A pose is counted correct when rotation error < 20° and translation error < 1.5 m, evaluated as a function of the maximum image-pair overlap on ScanNet.
**Audio script:** An ablation on ScanNet isolates what each task contributes to pose robustness. Training NeurHal on all three tasks together, identification, inpainting, and outpainting, gives the best results. The key finding is that adding the outpainting task is what drives the improvement on low overlap pairs, where most correspondents fall outside the target's field of view. Adding inpainting, by contrast, brings little additional benefit to camera pose estimation. Here a pose counts as correct when rotation error is under twenty degrees and translation error under one point five meters.

## Headline Numbers
**Necessary:**
- Robustness thresholds: rotation error < 20°, translation error < 1.5 m.
- Pose evaluation over 2,500 held-out ScanNet source/target pairs.
- Correspondence maps at γ = 50%, effective CNN stride s = 8 (640×480 target → 160×120 map).
**Additional:** NeurHal is the only evaluated method capable of outpainting correspondents outside the target field of view.
**Audio script:** A few numbers anchor the setup. Pose estimates are judged correct under a rotation threshold of twenty degrees and a translation threshold of one point five meters, measured over twenty five hundred held out ScanNet image pairs. NeurHal produces deliberately low resolution correspondence maps, using an effective stride of eight and an output ratio of fifty percent, so a six hundred forty by four hundred eighty target yields a one hundred sixty by one hundred twenty map. And across all the methods tested, NeurHal is the only one able to outpaint, to place correspondents beyond the target image's borders.

## Takeaway
**Necessary:** A single network can learn to hallucinate keypoint correspondences — visible, occluded, or outside the field of view — and this hallucination makes absolute camera pose estimation markedly more robust on low-overlap image pairs.
**Additional:** Correspondence hallucination reframes non-covisible regions as signal to be predicted rather than noise to be discarded.
**Audio script:** The takeaway is simple but powerful. A single network can learn to hallucinate keypoint correspondences whether the match is visible, occluded, or entirely outside the field of view, and this ability makes absolute camera pose estimation much more robust when images barely overlap. In effect, NeurHal reframes non covisible regions not as noise to be thrown away, but as signal to be predicted through learned geometric reasoning.
