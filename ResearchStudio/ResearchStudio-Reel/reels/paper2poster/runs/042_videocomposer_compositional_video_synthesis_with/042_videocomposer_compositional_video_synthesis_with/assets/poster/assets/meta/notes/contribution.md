# Contribution

Core claim: (1) VideoComposer, a compositional framework that generates video from arbitrary combinations of textual, spatial, and temporal conditions; (2) the use of compressed-video motion vectors as an explicit temporal control signal; (3) the Spatio-Temporal Condition encoder (STC-encoder), a unified interface that embeds diverse sequential conditions while improving inter-frame consistency.

Supporting detail: VideoComposer supports text, single image, single sketch, motion vectors, depth sequences, mask sequences, sketch sequences, and style, and can even animate simple hand-crafted strokes.

Narration: VideoComposer makes three contributions. First, it frames video generation as compositional: a user supplies any subset of textual, spatial, and temporal conditions, and the model recomposes a video obeying all of them. Second, it introduces motion vectors from compressed video as an explicit temporal control signal. Third, it proposes the Spatio-Temporal Condition encoder, a lightweight module that turns every sequential condition into a shared representation while boosting temporal consistency.
