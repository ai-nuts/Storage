---
kind: deck
title: Langevin Autoencoders for Learning Deep Latent Variable Models
lang: en
---

# Design Spec — Langevin Autoencoders (NeurIPS 2022)

## I. Brief & Audience
- Purpose: a ~3-minute narrated conference-style talk deck summarizing the paper.
- Audience: ML researchers familiar with VAEs and MCMC.
- Content divergence: faithful to the paper; concise spoken narrative.

## II. Narrative Mode
- mode: narrative — problem → motivation → contribution → method → experiments → results → takeaway.

## III. Visual Style
- swiss-minimal: generous whitespace, strong left grid, thin rules, restrained accent use.
- Palette: white canvas, deep indigo primary (#1E3A8A), red (#B91C1C) and teal (#0E7490) accents echoing the paper's posterior figures.

## IV. Font Plan
- Per-role font stacks:
  - title_family: Georgia, "Times New Roman", serif
  - body_family: Arial, "Helvetica Neue", Helvetica, sans-serif
  - code_family: Consolas, "Courier New", monospace
- Sizes (px): body 22, title 40, subtitle 28, lead 24, annotation 18, footnote 15, hero_number 52.

## V. Layout System
- 1280×720, left content margin 96, top band for titles, thin accent rule under each title.

## VIII. Image Resource List
- fig1_comparison (Figure 1): VI / LD / Hoffman / ALD comparison — Status: Ready — Type: Paper figure.
- fig2_capacity (Figure 2): encoder-capacity ablation (d>n, d=n, d<n) — Status: Ready.
- fig3_toy (Figure 3): toy posterior GT vs MF-VI vs Full-VI vs ALD — Status: Ready.
- fig4_samples (Figure 4): generated image samples — Status: Ready.
- logo_utokyo: University of Tokyo logo — Status: Ready.
- qr_code / qr_paper: code and paper QR tiles — Status: Ready.

## IX. Content Outline
- P01 title — cover, authors, venue, logo, QR.
- P02 problem — intractable posterior expectation; Langevin too slow.
- P03 motivation — VI amortization vs MCMC flexibility; the gap.
- P04 contribution — amortized Langevin dynamics + Langevin autoencoder.
- P05 method — move noise to encoder params; convergence theorem; a few steps + MH.
- P06 dataset-benchmark — toy problems + four image datasets; negative ELBO/dim.
- P07 key-result — toy posteriors reproduced; lowest ELBO on all four.
- P08 ablation-study — encoder capacity; MH step; iteration count.
- P09 headline-numbers — ELBO table and training-cost.
- P10 takeaway — efficient + flexible; provably valid; beats VAE.
