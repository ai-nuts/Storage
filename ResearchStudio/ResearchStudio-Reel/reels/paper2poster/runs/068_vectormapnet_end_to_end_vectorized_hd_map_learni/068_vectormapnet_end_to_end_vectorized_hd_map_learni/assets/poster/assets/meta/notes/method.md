# Method

Core claim: VectorMapNet has three stages: a BEV feature extractor lifts camera (ResNet + IPM) and LiDAR (PointPillars) features into a shared bird's-eye-view space; a DETR-style map element detector uses learnable element queries and deformable attention to predict element keypoints and class labels; and an autoregressive Transformer polyline generator decodes each detected element into an ordered sequence of vertices.

Supporting detail: Vertex coordinates are quantized into discrete tokens and modeled with a categorical distribution (following PolyGen); polylines are generated in parallel, and a two-stage strategy fine-tunes the generator on predicted keypoints to reduce exposure bias.

Narration: VectorMapNet has three stages. A bird's-eye-view extractor maps each modality into a shared top-down space: cameras through a ResNet and inverse perspective mapping, LiDAR through PointPillars, fused by concatenation. A detection transformer with element queries locates each element as keypoints. An autoregressive polyline generator then emits ordered vertices, trained with a matching detection loss and a generation loss.
