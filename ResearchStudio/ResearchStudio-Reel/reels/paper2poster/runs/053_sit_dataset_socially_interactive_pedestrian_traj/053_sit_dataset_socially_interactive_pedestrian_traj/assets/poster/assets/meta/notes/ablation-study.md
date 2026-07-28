# Ablation Study

Core claim: Adding the semantic map as scene context improves every trajectory-prediction model that can use it: Y-Net improves from ADE20 0.836 / FDE20 1.878 to 0.675 / 1.547, and NSP-SFM from 0.634 / 1.087 to 0.517 / 0.925.

Supporting detail: On detection, camera-LiDAR fusion beats single-modality models, with TransFusion-V (0.531 mAP) over CenterPoint-V (0.518) and camera-only FCOS3D (0.244); voxel backbones (SECOND) outperform PointPillar backbones.

Narration: The most informative comparison in the paper is turning the semantic map on and off for trajectory prediction. For Y-Net, adding the map lowers the ADE-twenty from about 0.84 down to 0.68 and the FDE-twenty from about 1.88 to 1.55. For NSP-SFM, the map brings ADE-twenty from about 0.63 to 0.52 and FDE-twenty from about 1.09 to 0.93. In both cases the map helps, confirming the value of the scene context that SiT provides. On the detection side, models that fuse camera and LiDAR outperform single-sensor models, and voxel-based backbones outperform pillar-based ones, with TransFusion using a voxel backbone giving the best detection score.
