# Dataset / Benchmark

Core claim: Three synthetic cue-augmented benchmarks: CIFAR-10 with 3×3 box cues located by label, CIFAR-100 with box cues colored and located by label digits, and Dominoes concatenating CIFAR-10 with class-matched Fashion-MNIST. Cue proportion is varied from 60% to 100%.

Supporting detail: Each benchmark ships counterfactual test splits, No Cue, With Cue, Randomized Cue, Randomized Image, so reliance on spurious versus natural attributes is directly measurable.

Narration: To measure mechanisms quantitatively, the authors build synthetic datasets by embedding easily separable spurious cues into standard vision data. CIFAR-10 gets small box cues placed according to the label, CIFAR-100 gets cues colored and positioned by label digits, and the Dominoes dataset stacks CIFAR-10 images with class-matched Fashion-MNIST images. They vary the fraction of cued samples from sixty to one hundred percent, and pair every dataset with counterfactual test sets that remove, keep, randomize, or scramble the cue. These counterfactuals reveal exactly how much a model leans on the spurious cue versus the natural image.
