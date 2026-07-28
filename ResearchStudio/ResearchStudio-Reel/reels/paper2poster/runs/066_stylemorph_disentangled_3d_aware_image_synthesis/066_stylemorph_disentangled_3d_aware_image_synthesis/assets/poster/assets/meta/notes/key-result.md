# Key Result

Core claim: StyleMorph reaches FID 7.91 on FFHQ and 4.29 / 3.49 / 13.95 on AFHQ Cats / Wild / Dogs at 256², competitive with the best non-disentangled 3D-GANs while adding full four-way disentanglement and a learned deformable template.

Supporting detail: Against Disentangled3D — the only prior 3D-GAN that also uses a deformable template — StyleMorph's FFHQ FID of 7.91 dramatically beats its 28.18, and unlike it StyleMorph also models foreground/background separation.

Narration: The headline finding is that disentanglement does not have to cost image quality. StyleMorph reaches a Frechet Inception Distance of seven point nine one on FFHQ faces, and four point two nine on cats, three point four nine on wild animals, and thirteen point nine five on dogs, all at two-fifty-six resolution. These numbers sit right alongside the strongest 3D-aware GANs that offer none of StyleMorph's control. The comparison that matters most is against Disentangled3D, the only prior method that also represents shape with a deformable template: StyleMorph's FFHQ score of seven point nine one is far ahead of its twenty-eight point one eight, and StyleMorph additionally separates foreground from background, which that method does not.
