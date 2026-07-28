# Problem

Core claim: Most VQA models optimize only answer accuracy and reach the answer as a black box, giving no human-readable evidence for how the answer was derived.

Supporting detail: Very few models both answer correctly and produce a self-contained explanation that actually corresponds to the correct answer (the paper's "Model type 3").

Narration: In the classic visual question answering task, a model takes an image and a question and returns an answer. The field has poured enormous effort into raising accuracy, thanks to large pre-trained vision-language models, but almost no attention is paid to how a model actually reaches its answer. The result is a black box: the prediction may be right, yet there is no evidence explaining the reasoning behind it. The authors distinguish three kinds of models: those that give only an answer, those that add a generic caption of the image, and the rare third kind that produces a logically self-contained explanation matching the answer. Almost all state-of-the-art VQA models fall into the first two categories, which motivates this work.
