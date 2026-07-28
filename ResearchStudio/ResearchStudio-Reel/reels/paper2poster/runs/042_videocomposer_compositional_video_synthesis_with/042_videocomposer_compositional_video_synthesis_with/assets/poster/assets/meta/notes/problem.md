# Problem

Core claim: Controllable video synthesis is far harder than controllable image synthesis: temporal dynamics vary widely and generated frames must stay temporally consistent, so image-style controls do not transfer directly.

Supporting detail: Prior progress in customizable image generation gives spatial control, but offers no principled way to steer how content moves and evolves over time.

Narration: Diffusion models made image generation highly controllable, but video is much harder. Video adds a temporal axis: motion patterns vary enormously across clips, and every frame must stay consistent with its neighbours. Reusing the spatial controls designed for images gives no reliable handle on temporal dynamics, so controllable video synthesis stayed an open challenge.
