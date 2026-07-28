# Title

Color is a powerful cue that convolutional networks readily exploit for object recognition, but it becomes a liability when the colors seen at test time differ from those in training. This paper introduces Color Equivariant Convolutions, or CEConvs, a new building block that shares shape features across the color spectrum while preserving discriminative color information. By hard-wiring parameter sharing over discrete hue shifts, CEConvs let networks like ResNets generalize to underrepresented colors and stay robust to test-time hue shifts, without throwing color away.
