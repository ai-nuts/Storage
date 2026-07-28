# Motivation

Core claim: Equivariance has been extended to many geometric transformations, but photometric transformations like hue shifts remain largely unexplored, despite early CNN layers learning highly color-selective filters.

Supporting detail: Prior work either applies color invariants as preprocessing or uses quaternion/offset-equivariant networks, none of which share features across colors while retaining color information.

Narration: Group equivariant convolutions taught networks to share parameters across rotations and flips, dramatically improving data efficiency for geometric transformations. Yet photometric changes, such as shifts in hue, had been left aside. Studies of trained CNNs show that early layers learn strongly color-selective neurons, which suggests color is a natural axis for equivariance. This motivates treating a hue shift the same way prior work treated a rotation: as a symmetry the network should respect by design, rather than something it must relearn from data.
