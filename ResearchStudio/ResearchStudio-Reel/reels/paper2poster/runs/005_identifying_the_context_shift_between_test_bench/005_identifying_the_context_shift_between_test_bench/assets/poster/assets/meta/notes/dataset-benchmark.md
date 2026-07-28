# Dataset / Benchmark

Core claim: The paper analyzes three model-organism domains and their benchmarks: facial expression recognition (SFEW, MMI, DISFA, FER2013, FERA, CK+, MultiPie), deepfake detection (the DFDC dataset of 128,154 videos from 960 actors), and medical diagnosis (the Diverse Dermatology Images / DDI and Fitzpatrick 17k skin datasets).

Supporting detail: It points to context-aware benchmarks as the way forward: BREEDS (subpopulation shift), WILDS (in-the-wild distribution shifts with sub-population labels), and Dynabench (dynamic NLP benchmarking).

Narration: Rather than introducing a new dataset, the paper dissects existing benchmarks across three domains. In facial expression recognition it examines seven benchmarks, from SFEW and MMI to CK+ and MultiPie. In deepfake detection it centers on the DFDC dataset, the largest to date, with over one hundred twenty-eight thousand videos from nine hundred sixty consenting actors. In medical diagnosis it looks at store-and-forward teledermatology and the Diverse Dermatology Images dataset. Throughout, it holds up context-aware benchmarks like BREEDS, WILDS, and Dynabench as models for capturing the data-generation process instead of a single static snapshot.
