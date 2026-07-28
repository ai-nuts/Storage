# Problem

Core claim: Local feature matching only locates a keypoint's correspondent when it is visible; occluded or out-of-frame correspondents are treated as noise, so matching fails when few keypoints are covisible.

Supporting detail: Humans instead reason geometrically to predict, or hallucinate, where non-covisible correspondents lie, a capability prior methods lack.

Narration: Establishing correspondences between two overlapping images underlies much of computer vision, from localization to reconstruction. But local feature matching only works when a keypoint is actually visible in both images. When the correspondent is occluded, or when it falls outside the field of view of the second image, these methods have nothing to say, and they simply treat those regions as noise. So whenever two images share little overlap, matching breaks down.
