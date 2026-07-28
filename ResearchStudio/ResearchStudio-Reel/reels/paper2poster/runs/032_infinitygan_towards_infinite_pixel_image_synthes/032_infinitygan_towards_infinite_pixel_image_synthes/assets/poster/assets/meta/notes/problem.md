# Problem

Core claim: Generating arbitrarily large, even infinite-pixel, images is bottlenecked because existing high-resolution GANs tie computation, memory, and training-data field-of-view directly to the output resolution.

Supporting detail: State-of-the-art generators cap out around 1024×1024 and cannot extend beyond their training resolution without losing global structure or exhausting memory.

Narration: Modern generative models keep improving in resolution and detail, but every gain costs more training time, a bigger model, and large field-of-view images that are hard to collect. Worse, existing generators are locked to their training resolution. Push them larger, and compute and memory explode quadratically while global structure falls apart. InfinityGAN asks how to escape this coupling and synthesize arbitrary, even infinite images from finite data on modest hardware.
