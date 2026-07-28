# Key Result

Core claim: On the EOT/SB benchmark LightSB beats the best prior solver by a wide margin (cBW²₂-UVP of roughly 0.03–0.62% versus 1.04–18.05% for the best baseline). On MSCI it matches strong GPU solvers in energy distance while training in 65–146 seconds on 4 CPU cores instead of tens of minutes to over an hour on a V100 GPU.

Supporting detail: For image translation, LightSB performs male↔female and adult↔child face translation in the ALAE latent space (D=512), converging in under one minute on 4 CPU cores.

Narration: The results show both accuracy and speed. On the entropic optimal transport benchmark, where the ground truth is known, LightSB reduces the conditional Bures-Wasserstein error to well under one percent, often around a few hundredths, while the best previous solver sits between about one and eighteen percent. On the MSCI single-cell task, LightSB reaches energy distance comparable to strong GPU baselines, but it trains in roughly one to two and a half minutes on just four CPU cores, whereas competing continuous solvers need tens of minutes to over an hour on a V100 GPU. And on FFHQ faces, it performs realistic male-to-female and child-to-adult translation in a five-hundred-twelve-dimensional latent space, converging in under a minute on CPU.
