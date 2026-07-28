# Method

Core claim: USIS-SAM freezes SAM and adds an Underwater Adaptive ViT (UA-ViT) encoder that injects underwater visual prompts through channel and multi-scale-convolution adapters, plus a Salient Feature Prompt Generator (SFPG) that fuses multi-layer features to automatically produce salient prompt embeddings fed to SAM's mask decoder for end-to-end segmentation.

Supporting detail: The UA-ViT uses a channel adapter and multi-scale convolutions (3×3, 5×5, 7×7) balanced by average residuals; the SFPG's Salient Feature Fusion Module aggregates UA-ViT features so the decoder can focus attention on salient regions.

Narration: USIS-SAM keeps SAM's pretrained backbone frozen and adds two lightweight modules. The Underwater Adaptive ViT encoder injects domain knowledge through adapters: a channel adapter recalibrates features, while multi-scale convolutions of size three, five, and seven capture structures, balanced by average residuals to dampen noise. On top, the Salient Feature Prompt Generator replaces SAM's manual prompts. Its Salient Feature Fusion Module aggregates features from each UA-ViT block and produces salient prompt embeddings automatically, feeding SAM's mask decoder. It trains end-to-end with a combined region, classification, box, and mask loss.
