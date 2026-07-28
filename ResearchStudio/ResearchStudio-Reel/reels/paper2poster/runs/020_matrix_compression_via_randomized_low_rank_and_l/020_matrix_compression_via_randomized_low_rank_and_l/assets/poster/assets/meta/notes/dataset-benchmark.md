# Dataset / Benchmark

Core claim: Evaluation spans the Shepp-Logan phantom and other test images, CIFAR-10 and CIFAR-100 embeddings from MobileNetV3, IMDB and Emotion text embeddings from BERT, and the weight matrices of LlaMa-7b.

Supporting detail: For embeddings, a k-nearest-neighbor classifier measures downstream accuracy and weighted F1; matrix reconstruction quality is measured by relative Frobenius norm error under matched (parity) bit budgets across methods.

Narration: Experiments span a deliberately diverse set of matrices. For images: the Shepp-Logan phantom, a Hubble image of Jupiter, and an MR brain scan. For embeddings: CIFAR-10 and CIFAR-100 from MobileNetV3, and IMDB and Emotion text from BERT, scored by a three-nearest-neighbor classifier. And for LLMs, the weight matrices of LlaMa-7b. Every method gets the same total bit budget, reporting relative Frobenius error.
