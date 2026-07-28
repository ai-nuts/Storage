# Problem

Core claim: Existing 3D-aware GANs produce high-quality images but entangle geometry with appearance, so they cannot separately control shape, camera pose, object texture, and background during synthesis.

Supporting detail: 3D morphable models (3DMMs) give this disentangled control, but building one classically demands extensive 3D scanning and manual alignment, restricting it to a few categories like faces.

Narration: The dream in 3D-aware image generation is a model you can steer, one where you change the pose without touching identity, or swap the background without disturbing the object. Today's best 3D-aware GANs make beautiful images, but their hybrid design fuses geometry and appearance together, so editing one factor bleeds into the others. Classical 3D morphable models solve the control problem elegantly, yet they require expensive 3D scanning and painstaking manual alignment, which is why they mainly exist for human faces. StyleMorph asks whether we can get morphable-model control for arbitrary object categories, learning everything from unstructured 2D images alone.
