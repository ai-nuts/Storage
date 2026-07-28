# Headline Numbers

Core claim: - Robustness thresholds: rotation error < 20°, translation error < 1.5 m. - Pose evaluation over 2,500 held-out ScanNet source/target pairs. - Correspondence maps at γ = 50%, effective CNN stride s = 8 (640×480 target → 160×120 map).

Supporting detail: NeurHal is the only evaluated method capable of outpainting correspondents outside the target field of view.

Narration: A few numbers anchor the setup. Pose estimates are judged correct under a rotation threshold of twenty degrees and a translation threshold of one point five meters, measured over twenty five hundred held out ScanNet image pairs. NeurHal produces deliberately low resolution correspondence maps, using an effective stride of eight and an output ratio of fifty percent, so a six hundred forty by four hundred eighty target yields a one hundred sixty by one hundred twenty map. And across all the methods tested, NeurHal is the only one able to outpaint, to place correspondents beyond the target image's borders.
