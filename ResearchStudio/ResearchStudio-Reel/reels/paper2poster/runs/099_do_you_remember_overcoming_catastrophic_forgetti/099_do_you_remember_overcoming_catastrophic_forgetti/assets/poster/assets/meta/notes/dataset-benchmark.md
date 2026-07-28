# Dataset / Benchmark

Core claim: Four fake audio datasets are used in sequence, trained on ASVspoof2019LA (S) then fine-tuned on ASVspoof2015 (T1), VCC2020 (T2), and In-the-Wild (T3); performance is measured by Equal Error Rate (EER, %).

Supporting detail: Generalization is tested on speech emotion recognition (MSP-Podcast → IEMOCAP, 4 emotions, accuracy) and image recognition (CLEAR-10 benchmark, 10 experiences, accuracy). Features come from a pre-trained Wav2vec 2.0 model for audio.

Narration: Experiments run on four fake audio datasets in a continual-learning sequence: ASVspoof 2019 LA as the source, then ASVspoof 2015, the Voice Conversion Challenge 2020 set, and the In-the-Wild dataset. Each is a distinct acoustic and linguistic condition, with In-the-Wild being real-world deepfakes of public figures. Detection quality is reported as Equal Error Rate. To show breadth, the method is also evaluated on speech emotion recognition and on the CLEAR-10 image recognition benchmark.
