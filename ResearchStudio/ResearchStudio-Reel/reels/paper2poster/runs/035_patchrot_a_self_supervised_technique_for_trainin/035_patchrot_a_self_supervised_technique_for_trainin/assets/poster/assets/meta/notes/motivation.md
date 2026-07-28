# Motivation

Core claim: ViTs process an image as a sequence of patch tokens with self-attention, so they can produce an output for every patch, not just one global output like a ConvNet. A self-supervised task should exploit this to learn both global and local features.

Supporting detail: RotNet showed that predicting a single image-level rotation angle yields strong ConvNet features; extending rotation prediction to the patch level is a natural fit for a token-based architecture but has not been explored.

Narration: A vision transformer splits an image into patches and applies self-attention, so unlike a convolutional network it can produce a separate output for every patch, not just one output for the whole image. Prior work called RotNet showed that simply predicting the rotation angle of an image teaches a convolutional network surprisingly rich features. The natural question is: can we push rotation prediction down to the patch level, so the transformer learns local features for each patch as well as global structure for the whole image? That patch-level signal is exactly what a token-based model is built to exploit.
