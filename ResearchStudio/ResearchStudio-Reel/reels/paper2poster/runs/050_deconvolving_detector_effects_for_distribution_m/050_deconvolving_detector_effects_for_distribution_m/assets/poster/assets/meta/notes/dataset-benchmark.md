# Dataset / Benchmark

Core claim: Two case studies: a Gaussian toy example (truth N(0,1), generation N(−0.5,1), Gaussian detector noise N(0,5), 10⁶ samples, 3:1 train–test split) and hadronic jet substructure from LHC simulations using the jet width observable w.

Supporting detail: The jet data are the Pythia/Herwig + Delphes samples from the OmniFold study, with one simulation acting as 'data' and the other as the synthetic dataset; two moments of the jet width are unfolded.

Narration: The method is tested on two problems. First, a Gaussian toy: the truth is a standard normal, the generation is shifted to mean minus one-half, and the detector adds wide Gaussian noise, with a million samples split three to one for training and testing. Because a Gaussian has only finitely many moments, unfolding its moments is equivalent to unfolding the whole density. Second, hadronic jets from simulated LHC collisions, using the jet width observable, drawn from the same Pythia and Herwig plus Delphes datasets used in the OmniFold paper, where one simulation stands in for data and the other for the synthetic reference.
