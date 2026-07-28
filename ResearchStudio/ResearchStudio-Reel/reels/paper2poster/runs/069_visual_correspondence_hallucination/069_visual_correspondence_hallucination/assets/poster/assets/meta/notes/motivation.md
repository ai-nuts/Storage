# Motivation

Core claim: State-of-the-art localization relies on keypoint matches, yet these matching methods collapse on low-overlap image pairs where most locations are occluded or outside the field of view.

Supporting detail: Geometric reasoning has only been used a posteriori (RANSAC-style outlier removal), never to actively predict correspondences at non-covisible locations.

Narration: Humans do not give up in these situations. Faced with an occluded or out of frame point, a person reasons about the geometry of the scene and predicts, or hallucinates, where the match should be. Classical vision does use geometric reasoning, but only after the fact, to filter out bad matches with models like epipolar geometry. No prior method actually predicts correspondences at locations that are not covisible. That gap is exactly what this work targets.
