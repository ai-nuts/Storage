# Motivation

Core claim: Online map learning from onboard sensors avoids the localization errors and labor of offline HD maps, and a truly end-to-end system should output the vectorized primitives downstream tasks use directly, without a rasterize-then-vectorize detour.

Supporting detail: HDMapNet, the prior state of the art, still predicts rasterized semantic/instance/direction maps and stitches them with a hand-crafted post-processing algorithm, which caps its scalability and accuracy.

Narration: The authors argue mapping should happen online, from the car's own sensors, avoiding the annotation burden and localization errors, and the model should output the final representation directly. Prior methods rasterize then vectorize with a hand-designed step; VectorMapNet removes that detour and predicts geometry end to end.
