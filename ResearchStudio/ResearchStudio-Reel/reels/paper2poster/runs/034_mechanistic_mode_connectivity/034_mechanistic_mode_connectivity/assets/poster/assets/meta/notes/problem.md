# Problem

Core claim: Prior mode-connectivity work ignores what mechanisms the connected minimizers use, so it cannot tell whether two low-loss solutions rely on the same or different input attributes for prediction.

Supporting detail: In vision datasets, backgrounds correlate with object categories, so models can succeed via either spurious cues or robust shape features, yet both are equally reachable minimizers.

Narration: Modern deep networks have infinitely many global minimizers, and the mode-connectivity literature shows these minimizers are joined by surprisingly simple, low-loss paths. But this literature has ignored a crucial question: what mechanisms do the connected models actually use? Two models can both reach low loss while relying on entirely different attributes of the input, such as an object's background versus its shape. The paper argues we cannot understand loss landscapes, or safely fine-tune models, without accounting for these prediction mechanisms.
