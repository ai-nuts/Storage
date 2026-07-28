# Ablation Study

Core claim: On CIFAR-10, removing either signal hurts: predicting only patch rotations ("No ImageRot", 91.8%) or only image rotation ("No PatchRot", 91.0%) both trail full PatchRot (92.6%), confirming global and local signals are complementary.

Supporting detail: Rotating image and patches together in one pass ("Rotate Img & Patch", 90.7%), training at the original size instead of reduced size ("Original Size", 92.1%), and reusing the class-token head instead of new patch heads ("Reuse MLP head", 91.1%) all underperform the full method, validating each design choice.

Narration: The ablation study on CIFAR-10 confirms that every component of PatchRot matters. Training on patch rotations alone, without whole-image rotation, drops accuracy to ninety-one point eight percent because the model loses global context. Using only image rotation, essentially the RotNet approach adapted to a transformer, drops it to ninety-one point zero. Rotating the image and its patches together in a single pass, rather than in separate passes, hurts performance, as does training at the original resolution instead of the reduced resolution, and reusing the existing head instead of adding dedicated patch heads. Each of these lands below the full method's ninety-two point six percent, showing every design decision contributes.
