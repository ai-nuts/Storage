# Headline Numbers

Core claim: - 60 scenes; about 60K images and 12K point cloud frames - About 470K 2D annotations and 320K 3D annotations - Best trajectory prediction (NSP-SFM + map): ADE20 0.517, FDE20 0.925 - Best 3D detection (TransFusion-V, camera+LiDAR): mAP 0.531

Supporting detail: Best tracking CenterPoint tracker sAMOTA 0.6070 / AMOTA 0.2007; sensors: 2 LiDARs, 5 cameras (360°), 2 IMUs, RTK; 20 s clips at 10 Hz, 9 s trajectories.

Narration: Here are the numbers worth remembering. SiT has sixty scenes, about sixty thousand images and twelve thousand point cloud frames, with roughly four hundred and seventy thousand two-dimensional and three hundred and twenty thousand three-dimensional annotations. On the trajectory benchmark, the best model with the semantic map reaches an ADE-twenty of about 0.52 and an FDE-twenty of about 0.93. On detection, the best camera-plus-LiDAR fusion model reaches a mean average precision of about 0.53. And on tracking, the CenterPoint tracker leads with an sAMOTA around 0.61.
