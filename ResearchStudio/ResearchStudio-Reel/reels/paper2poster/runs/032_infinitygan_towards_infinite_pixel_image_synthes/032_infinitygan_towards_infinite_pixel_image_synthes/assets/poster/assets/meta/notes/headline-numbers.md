# Headline Numbers

Core claim: - 4× ScaleInv FID: 61.41 (InfinityGAN) vs 79.83 (best baseline); 8×: 121.18 vs 189.65 - >90% human preference for InfinityGAN over all baselines - Up to 7.20× inference speed-up via parallel batching (19.09s vs 137.44s per image at 8192×8192) - Outpainting FID 9.11 (Places365) / 15.31 (Flickr-Scenery) for In&Out+InfinityGAN vs 23.57 / 30.34 for In&Out

Supporting detail: Constant O(1) memory at any output size; trained on 101×101 patches on a single GTX TITAN X GPU; 1024×1024 image composed from 121 seamless patches.

Narration: The headline numbers: scale-invariant FID of sixty-one at four-times and one twenty-one at eight-times, both beating the strongest baseline. Over ninety percent human preference. Up to seven point two times faster inference through parallel batching, cutting eight-thousand-pixel synthesis from one hundred thirty-seven seconds to nineteen. Paired with In-and-Out for outpainting, FID drops to nine on Places365 and fifteen on Flickr-Scenery, halving previous best.
