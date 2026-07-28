# Key Result

Core claim: On ImageNet-1K, T-RevSNN (ResNet-18, 512 ch, 29.8M params, T=4) reaches 73.2% top-1 at 85.7 MB/img and 2.8 mJ, the best accuracy among CNN-based spiking ResNets with the lowest memory, training time, and inference energy.

Supporting detail: Versus the Spike-driven Transformer (74.6%), T-RevSNN improves memory efficiency 8.6×, training-time 2.0×, and inference energy 1.6×, at comparable accuracy; a smaller 15.2M variant hits 69.8% at just 57.5 MB/img.

Narration: The results on ImageNet are strong. With about 30 million parameters and four timesteps, T-RevSNN reaches 73.2 percent top-1 accuracy while using only 85.7 megabytes of memory per image and 2.8 millijoules of inference energy. That is the best accuracy among convolutional spiking ResNets, and it comes with the lowest training memory, the fastest training time, and the lowest inference energy in its class. Compared against a leading spiking Transformer at similar accuracy, T-RevSNN uses 8.6 times less memory, trains 2 times faster, and spends 1.6 times less inference energy. A lighter 15 million parameter version still reaches nearly 70 percent accuracy at under 60 megabytes per image.
