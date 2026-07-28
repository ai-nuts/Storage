# Takeaway

Core claim: By formulating down-scaling as ideal (anti-aliased) downsampling and enforcing a frequency-dependency rule via Fourier layers, the network becomes exactly scale-equivariant, zero error, not merely approximately, while staying accurate and data-efficient.

Supporting detail: Getting the signal-processing right, treating down-scaling as a discrete anti-aliased operation, is what turns approximate equivariance into provable, absolute equivariance.

Narration: The lasting takeaway is that scale-equivariance should be treated as a signal-processing problem. Once you formulate down-scaling as ideal, anti-aliased downsampling and require every output frequency to depend only on equal or lower input frequencies, you can build networks from Fourier layers that are exactly scale-equivariant, with provably zero error rather than the small residual errors that plagued earlier methods. And this theoretical guarantee comes at no practical cost: the model matches or beats prior scale-equivariant CNNs on accuracy and is more data-efficient, especially on challenging natural images.
