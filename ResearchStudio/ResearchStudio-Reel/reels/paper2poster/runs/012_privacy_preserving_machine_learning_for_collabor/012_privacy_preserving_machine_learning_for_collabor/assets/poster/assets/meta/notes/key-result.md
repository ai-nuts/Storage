# Key Result

Core claim: Swapping raw features for shared latent embeddings preserves downstream accuracy: on the House Pricing test set the R² only drops from 90.29% (raw baseline) to 89.33% with two individual autoencoders (Scenario 2), and Buzz test R² stays at 89–91% versus a 96.19% baseline.

Supporting detail: MNIST classification test accuracy moves from 92% (baseline) to 84–88% under encoding, and the non-naive multitask variant (Scenario 3) recovers much of the gap, reaching 91% accuracy and 94.03% R² on Buzz.

Narration: The central finding is that sharing encoded representations instead of raw features barely hurts predictive performance. On House Pricing, the raw-data baseline reaches a test R-squared of about ninety percent, and the two-peer scenario using individual autoencoders still reaches about eighty-nine percent, an almost negligible drop despite the data being obfuscated. On Buzz in Social Media, the baseline R-squared is around ninety-six percent and the encoded scenarios stay in the high eighties to low nineties. For MNIST digit classification, test accuracy moves from ninety-two percent at baseline down to the mid-eighties under encoding. Importantly, the non-naive multitask scenarios, where the autoencoder is guided by the target variable, recover much of this gap, showing that shaping the latent space with the downstream task improves results.
