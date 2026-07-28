# Contribution

Core claim: The paper introduces the task of correspondence hallucination and NeurHal, a network that, given a source/target image pair and source keypoints, outputs for every keypoint a probability distribution over its correspondent's location regardless of visibility, unifying identifying, inpainting, and outpainting.

Supporting detail: It analyzes the specific features of this novel learning task, which motivate the loss and the non-siamese, cross-attention architecture, and shows the ability benefits absolute camera pose estimation.

Narration: The paper introduces the task of visual correspondence hallucination and a network to solve it, called NeurHal, for Neural Hallucinations. Given a pair of overlapping images and keypoints in the source image, NeurHal outputs, for each keypoint, a probability distribution over its correspondent's location in the target image, whether that location is visible, occluded, or outside the field of view. This unifies three tasks the authors name identifying, inpainting, and outpainting. Because learning to hallucinate is unexplored territory, they first analyze what makes the task distinctive, and let that analysis drive the choice of loss and architecture.
