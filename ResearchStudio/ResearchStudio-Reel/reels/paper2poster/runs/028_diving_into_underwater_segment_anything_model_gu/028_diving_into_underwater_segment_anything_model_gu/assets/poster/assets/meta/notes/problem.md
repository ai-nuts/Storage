# Problem

Core claim: Underwater salient instance segmentation suffers from low accuracy because complex underwater conditions distort images and no large-scale pixel-level salient dataset exists to train modern models.

Supporting detail: Segment Anything Model (SAM) generalizes poorly underwater and needs explicit point or box prompts, which are unavailable in an automatic salient-segmentation setting.

Narration: Underwater salient instance segmentation asks a model to find and separate the most important objects in a scene, a foundational step for marine exploration and robotics. But it is hard. Underwater images suffer light scattering, color distortion, and marine snow, so even top methods lose accuracy. The field has lacked a large-scale dataset with pixel-level salient annotations, stalling progress. Foundation models like SAM exist, but were trained on natural images and struggle underwater.
