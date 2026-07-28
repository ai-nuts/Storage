# Key Result

Core claim: Second-order ICFG improves the FID–CLIP-Score balance over CFG on MS-COCO: at w = 2.0 with v = 0.25 in the full condition space Call, it reaches FID 15.28 and CLIP Score 26.11, beating CFG's FID 15.42 / CLIP 25.80 at the same guidance strength.

Supporting detail: The optimal balance is found at w = 2.0, v = 0.25; the best absolute FID appears in the noun subspace Cnouns, while Call offers a more favorable "cone" structure for balancing the two metrics. On U-ViT, ICFG lowers FID versus CFG across sampling budgets.

Narration: The headline finding is that the second-order term genuinely helps. On MS-COCO, at guidance strength two with the second-order weight at a quarter, ICFG reaches an FID of fifteen point two eight and a CLIP score of twenty six point one one. That beats classifier-free guidance at the same setting, with a worse FID of fifteen point four two and a lower CLIP score of twenty five point eight. So the method improves both fidelity and alignment at once, without touching training. The authors identify the sweet spot at w equals two and v equals one quarter, and note the full condition space trades off the two metrics more favorably.
