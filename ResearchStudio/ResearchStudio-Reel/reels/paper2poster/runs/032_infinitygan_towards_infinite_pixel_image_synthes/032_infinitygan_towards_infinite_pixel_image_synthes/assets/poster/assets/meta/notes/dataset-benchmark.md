# Dataset / Benchmark

Core claim: Arbitrary-size synthesis is evaluated on Flickr-Landscape (450,000 high-quality landscape images); outpainting is evaluated on scenery subsets of Places365 (62,500 images) and Flickr-Scenery (54,710 images).

Supporting detail: All models train on 101×101 patches cropped from 197×197 real images; outpainting data is split 80/10/10 for train/validation/test.

Narration: The authors introduce Flickr-Landscape, four hundred fifty thousand high-quality landscape images crawled from Flickr, to evaluate synthesis at extended sizes. For outpainting they use scenery subsets of Places365, sixty-two thousand five hundred images, and Flickr-Scenery, about fifty-four thousand. Remarkably, every InfinityGAN model trains on tiny one-hundred-one-pixel patches, and both training and any-size inference run on a single GTX TITAN X GPU.
