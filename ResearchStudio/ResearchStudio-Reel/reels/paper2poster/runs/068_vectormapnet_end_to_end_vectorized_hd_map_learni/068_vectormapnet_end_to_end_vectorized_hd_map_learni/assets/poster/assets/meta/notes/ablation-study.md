# Ablation Study

Core claim: Among three keypoint representations, the Bounding Box (k=2) design is best, outperforming SME and Extreme Points by 2.0 Fréchet mAP and 7.3 Chamfer mAP; the two-stage teacher-forcing-then-fine-tune training adds +6.9 mAP (camera) and +8.5 mAP (fusion).

Supporting detail: Feeding VectorMapNet's predicted maps into a downstream motion-forecasting baseline lowers minADE from 0.909 (trajectory only) to 0.826, nearly matching the ground-truth map (0.779) and within 0.2% MR of it.

Narration: Two ablations stand out. Representing each element by a bounding box with two keypoints beats start-middle-end and extreme-point alternatives by two Fréchet and over seven Chamfer points. Two-stage training, teacher forcing then fine-tuning on predicted keypoints, adds about seven mAP for camera and over eight for fusion.
