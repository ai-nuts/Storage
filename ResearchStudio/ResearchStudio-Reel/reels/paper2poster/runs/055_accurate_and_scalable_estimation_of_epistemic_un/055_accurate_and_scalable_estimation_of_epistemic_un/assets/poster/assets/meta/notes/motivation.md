# Motivation

Core claim: A natural assumption is that more expressive architectures fix calibration; the authors show graph transformers and positional encodings do NOT reliably improve calibration under controlled shifts, motivating an explicit uncertainty-quantification approach instead.

Supporting detail: Increasing model width or depth can even worsen calibration, so scaling expressivity is not a substitute for principled epistemic uncertainty estimation.

Narration: There is a common expectation that adopting more advanced or expressive architectures will inherently improve calibration. Through a controlled case study on a structural distortion benchmark, the authors demonstrate this expectation is false: graph transformers and positional encodings do not meaningfully improve calibration over vanilla message-passing networks, and increasing model size can even make calibration worse. This finding motivates a different path. Rather than chasing expressivity, the paper advocates for epistemic uncertainty quantification to directly modulate confidence indicators.
