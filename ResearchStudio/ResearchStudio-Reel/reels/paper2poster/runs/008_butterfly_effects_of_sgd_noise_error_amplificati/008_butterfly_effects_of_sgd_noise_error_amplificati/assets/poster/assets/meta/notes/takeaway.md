# Takeaway

Core claim: SGD noise is harmless for the one-step training loss but, through feedback loops, gets amplified into chaotic long-horizon failures (GVA); averaging the weights with an EMA is a cheap, broadly effective stabilizer.

Supporting detail: EMA deserves to be a standard "stabilizer" in any pipeline where a model acts inside a feedback loop, from robotic control to language generation.

Narration: The takeaway is simple and actionable. Stochastic gradient noise is completely harmless for the one-step training loss you watch, but once your model sits inside a feedback loop, that same noise gets amplified into chaotic, catastrophic failures over long horizons. They call this gradient variance amplification. The good news is that the fix is almost free. Keep an exponential moving average of your weights, and you get a cheap, broadly effective stabilizer. Whether you are training a robot controller or a language model, iterate averaging deserves to be a standard part of the pipeline, right next to your optimizer and your learning rate schedule.
