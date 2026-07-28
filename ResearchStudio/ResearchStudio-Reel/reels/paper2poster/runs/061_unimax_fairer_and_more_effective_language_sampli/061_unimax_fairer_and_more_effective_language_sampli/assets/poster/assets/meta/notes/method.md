# Method

Core claim: UniMax (uniform + max) starts from a fixed character budget C and distributes it as uniformly as possible across languages, processed from lowest to highest resource. At each step it checks whether the remaining per-language budget can be split uniformly; if a language would exceed N epochs over its corpus, it is capped at N epochs and the freed budget is redistributed uniformly among the rest.

Supporting detail: This delivers more uniform coverage of head languages than temperature sampling while preventing tail languages from being repeated more than N times. Default N=1 disallows any repeats.

Narration: Here is how UniMax works. The name means uniform plus max. You start from a fixed character budget, C, and distribute it as uniformly as possible across the languages, processing them from lowest to highest resource. At each step, the algorithm checks whether the remaining per-language budget can still be split evenly. If a language would exceed N epochs over its own corpus, it is capped at N epochs, and the freed budget is redistributed uniformly among the languages that remain. The result is more uniform coverage of the head languages, while no tail language is ever repeated more than N times. With the default of N equals one, nothing repeats at all.
