# Motivation

Core claim: Token-level highlighting, like in-line spell-check, could draw operator attention to code regions that most need human oversight, but it is unknown which signal to highlight or whether highlighting helps at all.

Supporting detail: The existing strategy, highlighting the model's lowest-probability tokens, has been proposed in past work and ships in OpenAI's Playground, yet its assumption that low-probability equals likely-error was untested against human editing behavior.

Narration: One natural idea is to highlight uncertain tokens, much like a spell-checker underlines suspect words, so the programmer's eye is drawn to the spots that most need review. The obvious signal to use is the model's own generation probability: tokens the model was least sure about get highlighted. This is an existing strategy, and it even ships in OpenAI's Playground. But nobody had really tested whether low probability actually lines up with where humans need to make edits, and that gap is exactly what this paper set out to probe.
