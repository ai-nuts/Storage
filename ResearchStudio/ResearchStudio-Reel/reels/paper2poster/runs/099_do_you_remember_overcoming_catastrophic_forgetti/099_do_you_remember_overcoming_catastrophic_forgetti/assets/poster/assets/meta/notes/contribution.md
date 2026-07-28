# Contribution

Core claim: The paper proposes RAWM, a replay-free continual learning method with two parts: adaptive weight modification that steers the update direction by the genuine-versus-fake ratio, and a regularization term that forces the model to remember the old inference distribution.

Supporting detail: The method generalizes beyond fake audio detection to speech emotion recognition and image recognition (CLEAR benchmark), and is validated across four fake audio datasets averaged over seven runs.

Narration: The authors contribute Regularized Adaptive Weight Modification. It has two essential steps. First, adaptive weight modification introduces an extra projector that adjusts the update direction according to the ratio of classes with similar feature distribution, such as genuine utterances, to the others. Second, a regularization term, inspired by learning without forgetting, keeps the new inference distribution close to the old one. The method needs no previous samples, and the authors show it transfers to speech emotion recognition and image recognition.
