# Dataset / Benchmark

Core claim: Claims are validated on synthetic linear and nonlinear functional targets with exponential vs. polynomial decaying memory, on randomly-initialized RNN teacher-student setups (hidden dimension up to m=256), and on real tasks: IMDB sentiment analysis and MNIST image classification.

Supporting detail: Perturbation-error curves are swept over hidden dimensions m from 2 to 64 to expose the shifting stability radius.

Narration: The experiments span synthetic and real data. On the synthetic side, the authors build linear and nonlinear functional targets with either exponential or polynomial decaying memory and sweep the hidden dimension from about two up to sixty four to watch how the perturbation-stability radius behaves. They also construct randomly initialized RNN teacher models with a large hidden dimension of two hundred fifty six and approximate them with student RNNs to test the stability filter. On real data, they query the memory function of LSTM models on IMDB movie-review sentiment analysis, and they train nonlinear RNNs on MNIST image classification to test the optimization benefits of stable reparameterization.
