# Contribution

Core claim: (1) A novel training- and prompt-free zero-shot AC/AS method, MuSc, that lets unlabeled test images mutually score each other. (2) A Local Neighborhood Aggregation with Multiple Degrees (LNAMD) module and a Mutual Scoring Mechanism (MSM) for patch-level scoring. (3) A Re-scoring with Constrained Image-level Neighborhood (RsCIN) module that refines image-level classification and also boosts existing methods.

Supporting detail: MuSc requires no training, no prompts, and no normal reference images, and is a plug-in improvement for other AC methods via RsCIN.

Narration: MuSc is a training-free, prompt-free pipeline with three pieces. First, local neighborhood aggregation at multiple degrees, representing each patch at several scales to capture tiny and large defects. Second, mutual scoring, where every test image scores every other. Third, re-scoring with a constrained image-level neighborhood that cleans the final decision.
