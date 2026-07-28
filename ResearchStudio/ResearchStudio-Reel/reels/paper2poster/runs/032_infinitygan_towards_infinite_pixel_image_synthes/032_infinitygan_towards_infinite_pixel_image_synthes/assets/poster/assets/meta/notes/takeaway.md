# Takeaway

Core claim: By disentangling global appearance, structure, and texture and removing all padding, InfinityGAN synthesizes seamless, globally-consistent images of arbitrary or infinite size from small patches at constant memory, with parallelizable inference.

Supporting detail: The same design unlocks spatial style fusion, multi-modal outpainting, and arbitrary-length cyclic panorama and inbetweening.

Narration: The takeaway: infinite-pixel synthesis becomes tractable once you stop tying generation to a fixed resolution. By separating global appearance, local structure via a coordinate-driven implicit function, and texture via a padding-free generator, InfinityGAN produces patches that are independent yet perfectly consistent, tiling into images of any size at constant memory and generated in parallel. The same framework unlocks spatial style fusion, multi-modal outpainting, and arbitrary-length panoramas, all from tiny patches.
