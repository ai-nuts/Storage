#!/usr/bin/env python3
import re, sys
from pathlib import Path

def drop_section(doc, sec):
    m = re.search(rf'<div\b[^>]*\bdata-section="{re.escape(sec)}"', doc)
    if not m: return doc
    start = doc.rfind("<div", 0, m.end())
    i, depth = start, 0
    while i < len(doc):
        o, c = doc.find("<div", i), doc.find("</div>", i)
        if c == -1: return doc
        if o != -1 and o < c:
            depth += 1; i = o + 4
        else:
            depth -= 1; i = c + len("</div>")
            if depth == 0:
                while i < len(doc) and doc[i] in " \t\r\n": i += 1
                return doc[:start] + doc[i:]
    return doc

target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("poster.html")
html = target.read_text(encoding="utf-8")

SUBS = {
    "{{TITLE}}": "Langevin Autoencoders for Learning Deep Latent Variable Models",
    "{{AUTHORS}}": "Shohei Taniguchi<sup>1</sup>, Yusuke Iwasawa<sup>1</sup>, Wataru Kumagai<sup>1</sup>, Yutaka Matsuo<sup>1</sup>",
    "{{AUTHOR_LEGEND}}": "<sup>1</sup> The University of Tokyo",
    "{{VENUE_NAME}}": "NeurIPS",
    "{{VENUE_YEAR}}": "2022",
    "{{VENUE_LOGO}}": "assets/logos/_venue.png",
    "{{CONTACT}}": "",
    "{{LOGO_1}}": "assets/logos/the-university-of-tokyo.png",
    "{{LOGO_2}}": "", "{{LOGO_3}}": "", "{{LOGO_4}}": "", "{{LOGO_5}}": "", "{{LOGO_6}}": "",
    "{{QR_PAPER}}": "assets/qr/paper.png",
    "{{QR_CODE}}": "assets/qr/code.png",

    "{{PROBLEM}}": "Langevin-dynamics MCMC can approximate the intractable posteriors of deep latent variable models, but its costly per-datapoint sampling iterations and slow convergence make it impractical for training.",

    "{{MOTIVATION_1}}": "Amortized VI (the VAE) is efficient — one encoder predicts latents for all data — but its accuracy is capped by the tractable variational family (e.g. Gaussians).",
    "{{MOTIVATION_2}}": "MCMC is flexible yet was never truly amortized: prior hybrids (Hoffman 2017) only warm-start per-datapoint Langevin chains with an encoder.",

    "{{METHOD_1}}": "Move the noise from the latent space to the encoder’s parameters φ: run a Langevin SDE on φ, not a separate per-datapoint chain on each z.",
    "{{METHOD_2}}": "With encoder f(x;Φ)=Φ g(x), its outputs are taken directly as posterior samples; Theorem 1 guarantees convergence to the true posterior when width d ≥ batch size n.",
    "{{METHOD_3}}": "The Langevin Autoencoder runs T ALD steps on the encoder’s last layer before each decoder update, with an optional Metropolis–Hastings correction.",
    "{{METHOD_FIGURE}}": "assets/figures/page2_figure1.png",
    "{{METHOD_CAPTION}}": "(a) VI approximates posteriors with tractable Gaussians; (b) Langevin dynamics runs per-datapoint MCMC; (c) Hoffman [2017] warm-starts LD with an encoder; (d) ALD (ours) updates the encoder itself, treating its output as a posterior sample.",

    "{{TEASER_FIGURE}}": "assets/figures/page8_figure3.png",
    "{{TEASER_CAPTION}}": "Ground-truth posterior vs. mean-field VI, full VI, and ALD (ours): the Gaussian family misses the multimodal, correlated posterior that ALD reproduces.",

    "{{DATASET_1}}": "Toy: a conjugate bivariate-Gaussian model (closed-form posterior) and a harder neural-network (neural-likelihood) posterior.",
    "{{DATASET_2}}": "Images: MNIST, SVHN, CIFAR-10, CelebA — identical FC networks across methods; quality measured by negative ELBO per dimension over 3 seeds.",

    "{{BASELINE}}": "VAE",
    "{{BASELINE_NUM}}": "1.189",
    "{{OURS}}": "LAE (ours)",
    "{{OURS_NUM}}": "1.177",
    "{{HEADLINE_DELTA}}": "Lowest −ELBO/dim on all four image datasets",
    "{{KEY_RESULT_CONCLUSION}}": "More accurate posterior sampling translates directly into better-trained deep generative models.",

    "{{ABLATION_1}}": "Encoder capacity confirms Theorem 1: with last-layer width d ≥ n samples match the true posterior; with d < n some datapoints’ samples collapse.",
    "{{ABLATION_2}}": "The Metropolis–Hastings rejection step is important to stabilize training, while the number of ALD iterations T barely matters once T ≥ 2.",
    "{{ABLATION_CONCLUSION}}": "The rank condition d ≥ n and the MH correction are the decisive design choices; T = 2 steps suffice.",

    "{{HERO_VAL}}": "4 / 4",
    "{{HERO_LABEL}}": "datasets — LAE beats the VAE",
    "{{HERO_NOTE}}": "lowest −ELBO per dim on every benchmark",
    "{{STAT_2_VAL}}": "1.177",
    "{{STAT_2_LBL}}": "MNIST −ELBO",
    "{{STAT_3_VAL}}": "4.412",
    "{{STAT_3_LBL}}": "SVHN −ELBO",
    "{{STAT_4_VAL}}": "2.24×",
    "{{STAT_4_LBL}}": "train time vs VAE",

    "{{TAKEAWAY}}": "Replacing per-datapoint MCMC with a Langevin update of a shared encoder’s parameters gives efficient yet flexible posterior sampling — turning a plain autoencoder into a provably valid MCMC-based generative model that outperforms VAEs on test likelihood.",
}

DROP_SECTIONS = ["contribution"]
for sec in DROP_SECTIONS:
    html = drop_section(html, sec)
    html = re.sub(rf'"{re.escape(sec)}"\s*,?\s*', "", html)

missing = [k for k in SUBS if k not in html]
if missing:
    sys.exit(f"placeholder(s) not in template: {missing}")
for token, value in SUBS.items():
    html = html.replace(token, value)

leftover = sorted(set(re.findall(r"\{\{[A-Z0-9_]+\}\}", html)))
if leftover:
    sys.exit(f"unreplaced placeholders remain: {leftover}")

target.write_text(html, encoding="utf-8")
print(f"wrote {target} ({len(html)} bytes)")
