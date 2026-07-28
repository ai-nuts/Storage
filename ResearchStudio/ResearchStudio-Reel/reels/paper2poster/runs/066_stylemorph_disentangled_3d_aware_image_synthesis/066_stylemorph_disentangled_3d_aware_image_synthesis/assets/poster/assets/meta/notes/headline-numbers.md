# Headline Numbers

Core claim: - FFHQ 256² FID: 7.91 (vs Disentangled3D 28.18, the only other template-based method) - AFHQ FID: 4.29 Cats, 3.49 Wild, 13.95 Dogs - Disentangles 4 factors: shape, camera pose, foreground appearance, background appearance - TOCS vs NOCS ablation: FID 8.31 → 8.90, with better disentanglement from TOCS

Supporting detail: Trained entirely from unstructured 2D images across 4 datasets with no 3D supervision, pose labels, or predefined template.

Narration: A few numbers capture the impact. On FFHQ faces StyleMorph scores a seven point nine one FID, versus twenty-eight point one eight for the only competing template-based method. On animals it reaches four point two nine on cats, three point four nine on wild, and thirteen point nine five on dogs. It disentangles four independent factors: shape, camera pose, foreground appearance, and background appearance. And the core TOCS-versus-NOCS ablation shows template coordinates improving FID from eight point nine to eight point three while also sharpening disentanglement. All of this is learned from unstructured 2D images, with no 3D supervision at all.
