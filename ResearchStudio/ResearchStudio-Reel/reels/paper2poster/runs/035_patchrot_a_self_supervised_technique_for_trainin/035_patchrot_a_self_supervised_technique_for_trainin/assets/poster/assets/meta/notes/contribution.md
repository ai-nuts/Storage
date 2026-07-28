# Contribution

Core claim: The paper proposes PatchRot, a self-supervised technique tailored to ViTs that trains the network to predict the rotation angle of both the whole image (via the class token) and every individual patch (via new per-patch MLP heads), learning global and local features jointly.

Supporting detail: It introduces a buffer-gap patch-partitioning trick that prevents the network from cheating on patch rotations through edge continuity, and shows PatchRot outperforms supervised-from-scratch and RotNet across four datasets plus transfer-learning and semi-supervised settings.

Narration: The paper makes three main contributions. First, it introduces PatchRot, a self-supervised technique crafted for vision transformers that predicts rotation angles at two levels: the class token predicts the whole-image rotation for global context, and new per-patch heads predict each patch's rotation for local detail. Second, it introduces a buffer gap between patches during training so the network cannot cheat by matching continuous edges, forcing it to learn genuine content. Third, it demonstrates through extensive experiments that PatchRot beats both supervised training from scratch and the RotNet baseline across multiple datasets, and that its features transfer well and help in semi-supervised settings.
