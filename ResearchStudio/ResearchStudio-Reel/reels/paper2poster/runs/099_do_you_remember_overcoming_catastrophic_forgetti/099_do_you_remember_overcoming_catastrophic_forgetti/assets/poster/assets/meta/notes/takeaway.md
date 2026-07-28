# Takeaway

Core claim: By adapting the weight-update direction to the genuine-versus-fake ratio and regularizing against the old distribution, RAWM overcomes catastrophic forgetting in fake audio detection without replaying any past data, and the idea transfers to other classification tasks.

Supporting detail: The recipe is practical for released pre-trained detectors that cannot access their original training data.

Narration: The takeaway is simple: you can teach a fake audio detector new datasets without it forgetting the old, and without keeping any of the old data around. RAWM does this by making the weight update adapt to how genuine-heavy each batch is and by regularizing the model to remember its previous behavior. Because the underlying regularity, some classes staying similar across datasets, appears in many problems, the same recipe extends to speech emotion recognition and image recognition.
