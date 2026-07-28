# Headline Numbers

Core claim: - +14.2 mAP over HDMapNet on nuScenes; +14.6 mAP on Argoverse2 - 53.7 mAP best (Fusion + fine-tune) on nuScenes vs. 31.0 for HDMapNet (Fusion) - +17.9 mAP (Camera), +9.9 mAP (LiDAR), +14.2 mAP (Fusion) gains on nuScenes - Bounding-box keypoints: +7.3 Chamfer mAP over alternatives; two-stage fine-tune: +8.5 mAP (Fusion)

Supporting detail: Downstream motion forecasting minADE improves 0.909 → 0.826 with predicted maps.

Narration: To summarize: VectorMapNet exceeds the previous state of the art by 14.2 mAP on nuScenes and 14.6 on Argoverse2. Its best configuration, fusion with fine-tuning, reaches 53.7 mAP where HDMapNet reaches 31. Gains span sensors: about eighteen for camera, ten for LiDAR, fourteen for fusion.
