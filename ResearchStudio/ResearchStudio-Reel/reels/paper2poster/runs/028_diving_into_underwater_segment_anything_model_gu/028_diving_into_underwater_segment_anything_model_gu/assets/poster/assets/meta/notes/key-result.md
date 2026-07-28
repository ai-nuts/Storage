# Key Result

Core claim: On USIS10K, USIS-SAM reaches 59.7 mAP class-agnostic and 43.1 mAP multi-class, surpassing every prior method, including a 1.5 mAP gain over the SAM-based RSPrompter and a 0.7 mAP gain over the underwater method WaterMask on the class-agnostic task.

Supporting detail: In the multi-class setting USIS-SAM leads WaterMask and RSPrompter by 4.4 and 5.1 mAP respectively and beats the SIS baseline OQTR by 3.1 mAP class-agnostic; it also generalizes, improving over prior methods when retrained on the land SIS10K dataset.

Narration: Across both settings, USIS-SAM sets a new state of the art on USIS10K. In the class-agnostic task, localizing and masking salient objects regardless of category, it reaches 59.7 mAP, beating the best salient method OQTR by 3.1 points, the underwater WaterMask by 0.7, and the SAM-based RSPrompter by 1.5. In the harder multi-class task it scores 43.1 mAP, extending its lead to 4.4 points over WaterMask and 5.1 over RSPrompter. It also generalizes: retrained on the land-based SIS10K dataset, it still outperforms prior approaches.
