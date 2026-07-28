#!/usr/bin/env python3
"""All-native SVG deck builder for StyleMorph paper2video (10 slides, 39 cue anchors)."""
import json, os, html, textwrap

HERE = os.path.dirname(os.path.abspath(__file__))
BUNDLE = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
CONTRACT = json.load(open(os.path.join(BUNDLE, "assets/meta/visual_anchor_contract.json")))
OUT = os.path.join(HERE, "svg_output")
os.makedirs(OUT, exist_ok=True)

W, H = 1280, 720
BG = "#0e1320"
PANEL = "#1a2236"
PANEL2 = "#212c45"
STROKE = "#2e3d5e"
ACCENT = "#5b8cff"     # cobalt
TEAL = "#33d6c0"
GREEN = "#48d982"
RED = "#ff6b6b"
GOLD = "#ffcf5c"
TEXT = "#eaf0fb"
MUTE = "#9db0d0"
FONT = "Arial, 'Helvetica Neue', Helvetica, sans-serif"

def esc(s): return html.escape(str(s), quote=True)

def wrap(text, width):
    return textwrap.wrap(text, width=width)

def tlines(x, y, lines, size=15, lh=21, color=TEXT, weight="400", anchor="start"):
    out = []
    for i, ln in enumerate(lines):
        out.append(
            f'<text x="{x}" y="{y+i*lh}" font-family="{FONT}" font-size="{size}" '
            f'fill="{color}" font-weight="{weight}" text-anchor="{anchor}">{esc(ln)}</text>'
        )
    return "\n".join(out)

def card(x, y, w, h, fill=PANEL, stroke=STROKE, rx=14, sw=1.5):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')

def accent_bar(x, y, w=6, h=30, color=ACCENT):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="3" fill="{color}"/>'

def header(title, kicker):
    # inset accent (not full-bleed) to avoid edge_touch
    return (
        accent_bar(64, 46, 6, 34, ACCENT) +
        f'<text x="84" y="60" font-family="{FONT}" font-size="15" fill="{TEAL}" '
        f'font-weight="700" letter-spacing="2">{esc(kicker)}</text>' +
        f'<text x="84" y="88" font-family="{FONT}" font-size="30" fill="{TEXT}" '
        f'font-weight="800">{esc(title)}</text>'
    )

def cue_group(anchor_id, keywords, inner):
    kw = " ".join(keywords)
    return (f'<g id="{anchor_id}" data-cue-label="{esc(kw)}">'
            f'<title>{esc(kw)}</title><desc>{esc(kw)}</desc>{inner}</g>')

def svg_open():
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
            f'viewBox="0 0 {W} {H}" font-family="{FONT}">'
            f'<rect x="0" y="0" width="{W}" height="{H}" fill="{BG}"/>')

def svg_close():
    return "</svg>"

# ------- per-anchor visible content (heading + body lines) -------
# keyed by anchor_id -> (icon_label, heading, [body lines])
C = {}
def put(aid, head, body, extra=None):
    C[aid] = (head, body, extra)

# SLIDE 1 title
put("cue_s01_c1_stylemorph_3_d_aware_generative_pull", "Disentangles 4 factors",
    ["Independent control over 3D shape,", "camera pose, object appearance,", "and the scene backdrop."])
put("cue_s01_c2_does_learning_3_morphable_nothing", "Learns from 2D photos only",
    ["Builds a 3D morphable model with", "no 3D scans, no pose labels, and", "no hand-supplied template."])
put("cue_s01_c3_trick_morph_single_canonical_3", "The core trick",
    ["Morph one canonical 3D template into", "a purely geometric 2D map (TOCS),", "then condition a StyleGAN renderer."])
put("cue_s01_c4_faces_cats_dogs_wild_animals", "Works across categories",
    ["Faces, cats, dogs, and wild animals", "— SOTA image quality with full,", "fine-grained factor control."])

# SLIDE 2 problem
put("cue_s02_c1_dream_3_d_aware_image_generation", "The dream: steerable synthesis",
    ["Change pose without touching identity;", "swap the backdrop without disturbing", "the object being generated."])
put("cue_s02_c2_today_best_3_d_aware_gans", "Today's 3D-aware GANs entangle",
    ["Beautiful images, but geometry and", "appearance are fused, so editing one", "factor bleeds into the others."])
put("cue_s02_c3_classical_3_morphable_models_solve", "3DMMs solve control...",
    ["Classical morphable models give clean", "separate dials, but need 3D scanning", "and painstaking manual alignment."])
put("cue_s02_c4_stylemorph_asks_whether_get_morphabl", "...but only for faces",
    ["StyleMorph asks: can we get 3DMM-style", "control for arbitrary categories,", "learned from 2D images alone?"])

# SLIDE 3 motivation
put("cue_s03_c1_morphable_models_workhorse_visual_ef", "Why morphable control matters",
    ["3DMMs are the workhorse of VFX and AR,", "handing creators clean separate dials", "for pose, expression, appearance."])
put("cue_s03_c2_question_motivates_work_simple_get", "The driving question",
    ["Can we get that same control inside a", "modern 3D-aware GAN — without any of", "the 3D supervision 3DMMs require?"])
put("cue_s03_c3_prior_work_added_3_deformations", "Limits of prior deformation work",
    ["Earlier methods stayed on a single", "dynamic scene, or leaned on a template", "that already existed for the category."])
put("cue_s03_c4_stylemorph_instead_turns_morphable_i", "StyleMorph's shift",
    ["It turns the morphable model itself into", "something the network discovers from", "unlabeled 2D images — first-class."])

# SLIDE 4 contribution
put("cue_s04_c1_stylemorph_makes_three_linked_contri", "1 · Learned 3D morphable model",
    ["Learns non-rigid shape variation for a", "category from 2D images only, morphing", "a canonical template by backprop."])
put("cue_s04_c2_second_introduces_template_object_co", "2 · Template Object Coordinates",
    ["TOCS: a deformable cousin of Normalized", "Object Coordinates giving each surface", "point a stable template identity."])
put("cue_s04_c3_third_feeds_2_tocs_maps", "3 · Geometry-conditioned renderer",
    ["Feeds 2D TOCS maps as a purely geometric", "signal into a StyleGAN deferred neural", "renderer, separating shape from look."])
put("cue_s04_c4_together_these_deliver_disentangled", "Together: joint disentanglement",
    ["Disentangled control of pose, shape,", "object appearance, and scene appearance", "— all at high resolution."])

# SLIDE 5 method
put("cue_s05_c1_method_two_halves_geometry_side", "Geometry: Morphable Renderer",
    ["A SIREN deformation field, driven by a", "shape code, warps each camera ray from", "world space into canonical template space."])
put("cue_s05_c2_integrating_template_coordinates_alo", "Bottleneck: the TOCS map",
    ["Integrating template coordinates along", "each ray yields a 2D TOCS map — encodes", "shape, pose, projection; not appearance."])
put("cue_s05_c3_synthesis_side_stylegan2_based_defer", "Synthesis: StyleGAN2 DNR",
    ["A deferred neural renderer takes TOCS +", "two appearance codes (object, scene) and", "alpha-composites a high-res image."])
put("cue_s05_c4_proceeds_two_stages_first_deformable", "Two-stage training",
    ["Stage 1: deformable volume renderer at", "64² with weak silhouette supervision.", "Stage 2: freeze it, train the DNR full-res."])

# SLIDE 6 dataset-benchmark
put("cue_s06_c1_stylemorph_evaluated_four_widely_use", "Four standard datasets",
    ["Evaluated on FFHQ faces plus the three", "AFHQ animal splits, spanning faces and", "varied animal shape and topology."])
put("cue_s06_c2_ffhq_contributes_seventy_thousand_ce", "FFHQ · 70k faces",
    ["Seventy thousand centered human face", "photos with challenging backdrops and", "a wide range of head poses."])
put("cue_s06_c3_afhq_collection_adds_animal_faces", "AFHQ · animal faces",
    ["Three splits: ~5,653 cats, ~5,239 dogs,", "and ~5,238 wild animals — well beyond", "the categories classical 3DMMs cover."])
put("cue_s06_c4_authors_report_frechet_inception_dis", "Metric · FID @ 256²",
    ["Frechet Inception Distance at 256", "resolution, compared against eleven", "state-of-the-art 3D-aware GAN baselines."])

# SLIDE 7 key-result
put("cue_s07_c1_headline_finding_disentanglement_doe", "Disentanglement is (nearly) free",
    ["The headline: adding full four-way", "control does not have to cost image", "quality versus entangled 3D-GANs."])
put("cue_s07_c2_stylemorph_reaches_frechet_inception", "SOTA-competitive FID",
    ["FFHQ 7.91; AFHQ Cats 4.29, Wild 3.49,", "Dogs 13.95 — all at 256 resolution."])
put("cue_s07_c3_these_numbers_sit_right_alongside", "Alongside the strongest GANs",
    ["These scores sit right beside the best", "3D-aware GANs that offer none of", "StyleMorph's editing control."])
put("cue_s07_c4_comparison_matters_most_against_dise", "vs Disentangled3D",
    ["The only other template-based method:", "StyleMorph 7.91 FFHQ vs its 28.18, and", "it also separates object from scene."])

# SLIDE 8 ablation-study
put("cue_s08_c1_ablations_all_run_under_fair", "TOCS vs NOCS (96h budget)",
    ["Swapping TOCS for plain NOCS raises FID", "8.31 → 8.90 and blurs conditioning —", "template-space coordinates matter."])
put("cue_s08_c2_removing_deformable_module_direct_oc", "Remove the deformable module",
    ["A direct occupancy network keeps FID", "similar but drastically worsens shape /", "appearance consistency scores."])
put("cue_s08_c3_switching_late_fusion_early_fusion", "Late vs early fusion",
    ["Early fusion nudges FID down slightly", "but wrecks alpha consistency 88.65 →", "85.87%, bleeding object into scene."])
put("cue_s08_c4_finally_directly_optimizing_view_con", "View-consistency trade-off",
    ["Optimizing view consistency directly", "improves it 15.84 → 8.12, but trades", "away quality, pushing FID to 12.31."])

# SLIDE 9 headline-numbers
put("cue_s09_c1_few_numbers_capture_impact_ffhq", "FFHQ FID 7.91",
    ["vs 28.18 for Disentangled3D, the only", "other template-based competitor."])
put("cue_s09_c2_animals_reaches_four_point_two", "AFHQ animals",
    ["Cats 4.29 · Wild 3.49 · Dogs 13.95", "— photorealism well beyond faces."])
put("cue_s09_c3_core_tocs_versus_nocs_ablation_shows", "TOCS → 8.31 vs NOCS 8.90",
    ["Template coordinates improve FID and", "sharpen disentanglement together."])
put("cue_s09_c4_all_learned_unstructured_2_images", "4 factors, 0 3D labels",
    ["Shape, pose, object & scene appearance", "— all learned from 2D images alone."])

# SLIDE 10 takeaway
put("cue_s10_c1_one_line_takeaway_stylemorph_deliver", "The one-line takeaway",
    ["StyleMorph delivers morphable-model", "control inside a state-of-the-art image", "generator, learned from 2D photos."])
put("cue_s10_c2_morphing_learned_canonical_template", "How it works",
    ["Morph a learned canonical template into", "a purely geometric TOCS map that gives", "StyleGAN a clean signal to condition on."])
put("cue_s10_c3_effect_builds_unsupervised_3_morphab", "The bigger picture",
    ["In effect an unsupervised 3D morphable", "model for general object categories —", "VFX control from faces to wild animals."])

# ---------- slide renderers ----------
def grid_slide(slide, kicker, title, cols=2):
    chunks = slide["chunks"]
    parts = [svg_open(), header(title, kicker)]
    gx, gy = 60, 128
    gw = (W - 2*gx - 24*(cols-1)) // cols
    n = len(chunks)
    rows = (n + cols - 1)//cols
    gh = (H - gy - 40 - 24*(rows-1)) // rows
    accents = [ACCENT, TEAL, GOLD, GREEN]
    for i, ch in enumerate(chunks):
        r, c = divmod(i, cols)
        x = gx + c*(gw+24); y = gy + r*(gh+24)
        head, body, extra = C[ch["anchor_id"]]
        inner = card(x, y, gw, gh)
        inner += accent_bar(x+18, y+22, 5, 26, accents[i % 4])
        inner += tlines(x+36, y+42, [head], size=20, color=TEXT, weight="700")
        inner += tlines(x+22, y+80, body, size=15, lh=23, color=MUTE)
        parts.append(cue_group(ch["anchor_id"], ch["cue_keywords"], inner))
    parts.append(svg_close())
    return "\n".join(parts)

def bars_overlay(x, y, w, h):
    # mini FID bar chart: lower is better
    data = [("SMorph", 7.91, GREEN), ("D3D", 28.18, RED), ("Cats", 4.29, TEAL),
            ("Wild", 3.49, TEAL), ("Dogs", 13.95, GOLD)]
    mx = 30.0
    bw = 42; gap = 20; base = y+h-34; top = y+18
    plot_h = base-top
    out = [f'<text x="{x}" y="{y+10}" font-family="{FONT}" font-size="12" fill="{MUTE}">FID @256² (lower is better)</text>']
    for i,(lab,val,col) in enumerate(data):
        bx = x + i*(bw+gap)
        bh = max(6, plot_h*val/mx)
        by = base-bh
        out.append(f'<rect x="{bx}" y="{by}" width="{bw}" height="{bh}" rx="4" fill="{col}"/>')
        out.append(f'<text x="{bx+bw/2}" y="{by-6}" font-family="{FONT}" font-size="12.5" fill="{TEXT}" font-weight="700" text-anchor="middle">{val}</text>')
        out.append(f'<text x="{bx+bw/2}" y="{base+16}" font-family="{FONT}" font-size="11.5" fill="{MUTE}" text-anchor="middle">{lab}</text>')
    return "\n".join(out)

def key_result_slide(slide):
    kicker, title = "KEY RESULT", "Disentanglement without a quality tax"
    chunks = slide["chunks"]
    parts = [svg_open(), header(title, kicker)]
    # top row: c1, c3 as cards; bottom-left c4 card; bottom-right c2 card with bar chart
    layout = {
        chunks[0]["anchor_id"]: (60, 128, 560, 250),   # c1
        chunks[2]["anchor_id"]: (644, 128, 576, 250),   # c3
        chunks[3]["anchor_id"]: (60, 402, 560, 278),    # c4
        chunks[1]["anchor_id"]: (644, 402, 576, 278),   # c2 (chart)
    }
    accents = {chunks[0]["anchor_id"]:ACCENT, chunks[2]["anchor_id"]:TEAL,
               chunks[3]["anchor_id"]:GOLD, chunks[1]["anchor_id"]:GREEN}
    for ch in chunks:
        aid = ch["anchor_id"]; x,y,w,h = layout[aid]
        head, body, extra = C[aid]
        inner = card(x,y,w,h)
        inner += accent_bar(x+18, y+22, 5, 26, accents[aid])
        inner += tlines(x+36, y+42, [head], size=20, color=TEXT, weight="700")
        inner += tlines(x+22, y+80, body, size=15, lh=23, color=MUTE)
        if aid == chunks[1]["anchor_id"]:
            inner += bars_overlay(x+26, y+150, w-52, 110)
        parts.append(cue_group(aid, ch["cue_keywords"], inner))
    parts.append(svg_close())
    return "\n".join(parts)

def headline_slide(slide):
    kicker, title = "HEADLINE NUMBERS", "The impact in four numbers"
    chunks = slide["chunks"]
    parts = [svg_open(), header(title, kicker)]
    big = {chunks[0]["anchor_id"]:("7.91","FFHQ FID",GREEN),
           chunks[1]["anchor_id"]:("4.29 / 3.49 / 13.95","AFHQ Cats / Wild / Dogs",TEAL),
           chunks[2]["anchor_id"]:("8.31","TOCS FID  (NOCS 8.90)",GOLD),
           chunks[3]["anchor_id"]:("4 / 0","factors / 3D labels",ACCENT)}
    gx, gy = 60, 128; gw=(W-2*gx-24)//2; gh=(H-gy-40-24)//2
    for i,ch in enumerate(chunks):
        aid=ch["anchor_id"]; r,c=divmod(i,2)
        x=gx+c*(gw+24); y=gy+r*(gh+24)
        num,lab,col=big[aid]; head,body,extra=C[aid]
        inner=card(x,y,gw,gh)
        inner+=accent_bar(x+18,y+22,5,26,col)
        fs = 54 if len(num)<8 else 34
        inner+=f'<text x="{x+36}" y="{y+92}" font-family="{FONT}" font-size="{fs}" fill="{col}" font-weight="800">{esc(num)}</text>'
        inner+=tlines(x+38, y+120, [lab], size=15, color=MUTE, weight="600")
        inner+=tlines(x+22, y+156, body, size=14.5, lh=22, color=MUTE)
        parts.append(cue_group(aid, ch["cue_keywords"], inner))
    parts.append(svg_close())
    return "\n".join(parts)

def title_slide(slide):
    chunks = slide["chunks"]
    parts=[svg_open()]
    parts.append(accent_bar(80, 70, 7, 128, ACCENT))
    parts.append(f'<text x="104" y="96" font-family="{FONT}" font-size="16" fill="{TEAL}" font-weight="700" letter-spacing="3">ICLR 2023 · 3D-AWARE GENERATION</text>')
    parts.append(f'<text x="104" y="150" font-family="{FONT}" font-size="52" fill="{TEXT}" font-weight="800">StyleMorph</text>')
    parts.append(f'<text x="104" y="188" font-family="{FONT}" font-size="24" fill="{MUTE}" font-weight="600">Disentangled 3D-Aware Image Synthesis</text>')
    parts.append(f'<text x="104" y="216" font-family="{FONT}" font-size="24" fill="{MUTE}" font-weight="600">with a 3D Morphable StyleGAN</text>')
    parts.append(f'<text x="104" y="252" font-family="{FONT}" font-size="15" fill="{MUTE}">Eric-Tuan Le, Edward Bartrum, Iasonas Kokkinos · UCL &amp; Alan Turing Institute</text>')
    # four concept cards
    gx, gy=80, 300; gw=(W-2*gx-24)//2; gh=180
    accents=[ACCENT,TEAL,GOLD,GREEN]
    for i,ch in enumerate(chunks):
        r,c=divmod(i,2)
        x=gx+c*(gw+24); y=gy+r*(gh+24)
        head,body,extra=C[ch["anchor_id"]]
        inner=card(x,y,gw,gh)
        inner+=accent_bar(x+18,y+22,5,24,accents[i%4])
        inner+=tlines(x+36,y+40,[head],size=18,color=TEXT,weight="700")
        inner+=tlines(x+22,y+72,body,size=14,lh=20,color=MUTE)
        parts.append(cue_group(ch["anchor_id"], ch["cue_keywords"], inner))
    parts.append(svg_close())
    return "\n".join(parts)

def takeaway_slide(slide):
    kicker,title="TAKEAWAY","Morphable control, meet photorealism"
    chunks=slide["chunks"]
    parts=[svg_open(), header(title,kicker)]
    ys=[128, 318, 508]; accents=[ACCENT,TEAL,GOLD]
    for i,ch in enumerate(chunks):
        y=ys[i]; x=60; w=W-120; h=170
        head,body,extra=C[ch["anchor_id"]]
        inner=card(x,y,w,h)
        inner+=accent_bar(x+18,y+24,5,28,accents[i])
        inner+=tlines(x+36,y+44,[head],size=21,color=TEXT,weight="700")
        inner+=tlines(x+38,y+78,body,size=16,lh=24,color=MUTE)
        parts.append(cue_group(ch["anchor_id"], ch["cue_keywords"], inner))
    parts.append(svg_close())
    return "\n".join(parts)

KICKERS = {
    "problem":"PROBLEM","motivation":"MOTIVATION","contribution":"CONTRIBUTIONS",
    "method":"METHOD","dataset-benchmark":"DATASETS & BENCHMARK",
    "ablation-study":"ABLATIONS",
}
TITLES = {
    "problem":"Control is the missing piece","motivation":"Bring 3DMM control to GANs",
    "contribution":"Three linked contributions","method":"Geometry bottleneck, then style",
    "dataset-benchmark":"Faces and animals, FID at 256²",
    "ablation-study":"What each design choice buys",
}

order = [s["id"] for s in CONTRACT["slides"]]
for i, slide in enumerate(CONTRACT["slides"]):
    sid = slide["id"]; prefix=f"{i+1:02d}"
    if sid=="title": svg=title_slide(slide)
    elif sid=="key-result": svg=key_result_slide(slide)
    elif sid=="headline-numbers": svg=headline_slide(slide)
    elif sid=="takeaway": svg=takeaway_slide(slide)
    else: svg=grid_slide(slide, KICKERS[sid], TITLES[sid], cols=2)
    fn=os.path.join(OUT, f"{prefix}_{sid}.svg")
    open(fn,"w").write(svg)
    print("wrote", fn)
print("done", len(order), "slides")
