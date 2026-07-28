# Contribution

Core claim: They (1) formulate down-scaling in the discrete domain as ideal downsampling with anti-aliasing, (2) propose a family of truly scale-equivariant deep nets built from Fourier layers with a simple frequency-dependency condition, and (3) show absolute zero end-to-end equivariance error with competitive accuracy on MNIST-scale and STL-10.

Supporting detail: They design scale-equivariant versions of every module (convolution, non-linearity, pooling), plus a per-scale classifier and a consistency loss tailored to scale-consistent prediction.

Narration: The paper makes three contributions. First, it formulates the down-scaling operation directly in the discrete domain as ideal downsampling, properly accounting for anti-aliasing. Second, it proposes a whole family of deep nets that are truly scale-equivariant, by rethinking every component, convolution layers, non-linearities, and pooling, and re-expressing them as Fourier layers that obey a simple frequency-dependency rule. Third, through extensive experiments on MNIST-scale and STL-10, it shows the model attains an absolute zero end-to-end scale-equivariance error while remaining competitive in classification accuracy and more data-efficient in low-resource settings.
