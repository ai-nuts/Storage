#!/usr/bin/env python3
"""Native SVG deck for AVFS paper2video (run063). 10 slides, 1920x1080.
Each cue_* anchor from the visual anchor contract is attached to a distinct
visible group so the post-hoc cue matcher can bind narration chunks to geometry.
"""
import base64, os, textwrap

HERE = os.path.dirname(os.path.abspath(__file__))
BUNDLE = "/datadisk/project/ResearchStudio/benchmarks/paper2poster/runs/063_a_view_from_somewhere_human_centric_face_represe/063_a_view_from_somewhere_human_centric_face_represe"
FIG = os.path.join(BUNDLE, "assets/figures")
LOGO = os.path.join(BUNDLE, "assets/logos")
QR = os.path.join(BUNDLE, "assets/qr")
OUT = os.path.join(HERE, "svg_final")
os.makedirs(OUT, exist_ok=True)

W, H = 1920, 1080

# ---- palette ----
BG = "#FBFCFE"
INK = "#15202E"
MUTED = "#5A6B82"
LINE = "#E1E8F1"
CARDBG = "#F4F7FB"
WHITE = "#FFFFFF"
PRIMARY = "#4338CA"      # indigo
PRIMARY_SOFT = "#ECEDFB"
TEAL = "#0E8F86"
TEAL_SOFT = "#E1F3F0"
ROSE = "#CF2E56"
ROSE_SOFT = "#FBE7ED"
AMBER = "#B8730F"
AMBER_SOFT = "#FBF0DE"
GOLD = "#B7791F"

FS = "'DejaVu Sans','Helvetica Neue',Arial,sans-serif"
FM = "'DejaVu Sans Mono','Courier New',monospace"

CHARW = 0.535  # avg char width factor for DejaVu Sans


def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def b64(path):
    with open(path, "rb") as f:
        return "data:image/png;base64," + base64.b64encode(f.read()).decode()


def T(x, y, s, size=32, color=INK, weight="normal", anchor="start", font=FS, ls="0"):
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-family="{font}" font-size="{size}" '
            f'fill="{color}" font-weight="{weight}" text-anchor="{anchor}" '
            f'letter-spacing="{ls}">{esc(s)}</text>')


def wrap(s, size, maxw):
    maxc = max(6, int(maxw / (size * CHARW)))
    return textwrap.wrap(s, maxc)


def para(x, y, s, size=28, color=MUTED, maxw=600, lh=1.42, weight="normal", font=FS):
    out = []
    ln = 0
    for line in wrap(s, size, maxw):
        out.append(T(x, y + ln * size * lh, line, size, color, weight, font=font))
        ln += 1
    return "\n".join(out), y + ln * size * lh


def rrect(x, y, w, h, fill, stroke="none", sw=0, rx=18, extra=""):
    st = f' stroke="{stroke}" stroke-width="{sw}"' if stroke != "none" else ""
    return f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" fill="{fill}"{st}{extra}/>'


def anchor_open(aid):
    return f'<g id="{aid}" data-cue-label="{aid}"><title>{aid}</title><desc>{aid}</desc>'


def slide_open(bg=BG):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
            f'viewBox="0 0 {W} {H}"><rect width="{W}" height="{H}" fill="{bg}"/>')


def header(kicker, title, accent=PRIMARY, subtitle=None):
    s = []
    s.append(rrect(110, 84, 54, 8, accent, rx=4))
    s.append(T(180, 100, kicker.upper(), 26, accent, "bold", ls="3"))
    s.append(T(110, 176, title, 62, INK, "bold"))
    y = 176
    if subtitle:
        s.append(T(110, 220, subtitle, 30, MUTED))
        y = 220
    s.append(f'<line x1="110" y1="{y+34}" x2="1810" y2="{y+34}" stroke="{LINE}" stroke-width="2"/>')
    return "\n".join(s), y + 34


def footer(n, label="A View From Somewhere — Human-Centric Face Representations (ICLR 2023)"):
    s = []
    s.append(f'<line x1="110" y1="1012" x2="1810" y2="1012" stroke="{LINE}" stroke-width="1.5"/>')
    s.append(T(110, 1050, label, 22, MUTED))
    s.append(T(1810, 1050, f"{n:02d} / 10", 22, MUTED, anchor="end", font=FM))
    return "\n".join(s)


def card(x, y, w, h, aid=None, fill=WHITE, stroke=LINE, sw=2, rx=18, accent=None):
    """Open a card group (optionally anchored). Returns (open_str, close_str)."""
    o = []
    if aid:
        o.append(anchor_open(aid))
    o.append(rrect(x, y, w, h, fill, stroke, sw, rx))
    if accent:
        o.append(rrect(x, y, 8, h, accent, rx=4))
    c = "</g>" if aid else ""
    return "\n".join(o), c


def chip(x, y, txt, fill, fg, size=24, padx=18, h=44):
    w = len(txt) * size * CHARW + padx * 2
    s = rrect(x, y, w, h, fill, rx=h/2) + T(x + padx, y + h/2 + size*0.35, txt, size, fg, "bold")
    return s, w


def write(name, body):
    svg = slide_open() + "\n" + body + "\n</svg>"
    with open(os.path.join(OUT, name), "w") as f:
        f.write(svg)
    print("wrote", name)


# =================================================================== SLIDE 1
def s1_title():
    s = [slide_open()]
    s.pop()  # write() adds slide_open; build body only
    b = []
    # left accent band
    b.append(rrect(0, 0, 26, H, PRIMARY, rx=0))
    # venue + anchor c1 (title block)
    o, c = card(110, 150, 1180, 300, aid="cue_s01_c1_view_somewhere_published_iclr_2023",
                fill=WHITE, stroke=LINE, sw=0, rx=24)
    b.append(o)
    b.append(rrect(110, 150, 1180, 300, WHITE, LINE, 0, 24))
    b.append(T(150, 235, "ICLR 2023", 28, PRIMARY, "bold", ls="2"))
    b.append(T(150, 330, "A View From Somewhere", 74, INK, "bold"))
    b.append(T(150, 405, "Human-Centric Face Representations", 44, MUTED, "bold"))
    b.append(c)
    # authors / institutes
    b.append(T(150, 500, "Jerone T. A. Andrews    ·    Przemyslaw Joniak    ·    Alice Xiang", 28, INK))
    b.append(T(150, 540, "Sony AI    ·    University of Tokyo", 26, MUTED))
    # anchor c2 card
    o, c = card(110, 600, 860, 150, aid="cue_s01_c2_instead_relying_problematic_demograp",
                fill=PRIMARY_SOFT, stroke="none", sw=0, rx=20, accent=PRIMARY)
    b.append(o)
    b.append(T(150, 660, "No demographic labels", 30, PRIMARY, "bold"))
    txt, _ = para(150, 700, "Learn from 600K+ human judgments of face similarity, aligned with perception.", 26, INK, maxw=790)
    b.append(txt)
    b.append(c)
    # anchor c3 card
    o, c = card(110, 780, 860, 150, aid="cue_s01_c3_result_face_representation_interpret",
                fill=TEAL_SOFT, stroke="none", sw=0, rx=20, accent=TEAL)
    b.append(o)
    b.append(T(150, 840, "A continuous, interpretable space", 30, TEAL, "bold"))
    txt, _ = para(150, 880, "Avoids invasive categories; captures the continuous nature of human diversity.", 26, INK, maxw=790)
    b.append(txt)
    b.append(c)
    # right column: QR + logo cluster
    rx0 = 1360
    b.append(rrect(rx0, 150, 450, 780, WHITE, LINE, 2, 24))
    b.append(T(rx0 + 225, 208, "Scan for more", 24, MUTED, "bold", anchor="middle"))
    cx = rx0 + 225
    # Paper QR — large (square frame clears the min-visual gate on its own)
    pp = os.path.join(QR, "paper.png")
    if os.path.exists(pp):
        b.append(rrect(cx - 148, 236, 296, 296, CARDBG, LINE, 2, 16))
        b.append(f'<image x="{cx-132}" y="252" width="264" height="264" href="{b64(pp)}" preserveAspectRatio="xMidYMid meet"/>')
        b.append(T(cx, 566, "Paper  ·  arXiv:2303.17176", 24, INK, "bold", anchor="middle"))
    # Code QR — smaller companion
    cp = os.path.join(QR, "code.png")
    if os.path.exists(cp):
        b.append(rrect(cx - 90, 600, 180, 180, CARDBG, LINE, 2, 14))
        b.append(f'<image x="{cx-72}" y="618" width="144" height="144" href="{b64(cp)}" preserveAspectRatio="xMidYMid meet"/>')
        b.append(T(cx, 802, "Code  ·  github.com/SonyAI", 22, MUTED, anchor="middle"))
    # institute logos row (decorative)
    try:
        b.append(f'<image x="{rx0+40}" y="840" width="180" height="66" href="{b64(os.path.join(LOGO,"sony-company.png"))}" preserveAspectRatio="xMidYMid meet"/>')
        b.append(f'<image x="{rx0+240}" y="840" width="180" height="66" href="{b64(os.path.join(LOGO,"university-of-tokyo.png"))}" preserveAspectRatio="xMidYMid meet"/>')
    except Exception:
        pass
    b.append(footer(1))
    write("01_title.svg", "\n".join(b))


# =================================================================== SLIDE 2
def s2_problem():
    b = []
    h, y0 = header("Problem", "Categorical labels are the wrong tool", ROSE)
    b.append(h)
    cards = [
        ("cue_s02_c1_evaluating_diversity_face_datasets_a", "Diversity = demographic labels",
         "Dataset diversity is almost always measured with categorical labels: race, gender, or age."),
        ("cue_s02_c2_but_these_labels_frequently_unavaila", "Unreliable & restricted",
         "Labels are often unavailable, legally restricted to collect, and biased when inferred by annotators."),
        ("cue_s02_c3_worse_categorical_labels_flatten_con", "They flatten appearance",
         "Skin tone becomes only light or dark, yet two faces with the same label can look very different."),
        ("cue_s02_c4_rigid_taxonomies_also_erase_multi_et", "Rigid taxonomies cause harm",
         "They erase multi-ethnic people, shift meaning across cultures, and harm those who are mislabeled."),
    ]
    cw, ch = 828, 320
    gx, gy = 110, 300
    gap = 44
    for i, (aid, title, body) in enumerate(cards):
        cx = gx + (i % 2) * (cw + gap)
        cy = gy + (i // 2) * (ch + gap)
        o, c = card(cx, cy, cw, ch, aid=aid, fill=WHITE, stroke=LINE, sw=2, accent=ROSE)
        b.append(o)
        b.append(T(cx + 44, cy + 74, f"0{i+1}", 30, ROSE, "bold", font=FM))
        b.append(T(cx + 110, cy + 74, title, 34, INK, "bold"))
        txt, _ = para(cx + 44, cy + 140, body, 28, MUTED, maxw=cw - 90, lh=1.45)
        b.append(txt)
        b.append(c)
    b.append(footer(2))
    write("02_problem.svg", "\n".join(b))


# =================================================================== SLIDE 3
def s3_motivation():
    b = []
    h, y0 = header("Motivation", "Similarity is continuous, and personal", PRIMARY)
    b.append(h)
    cards = [
        ("cue_s03_c1_authors_argue_face_similarity_fundam", "Continuous & personal",
         "Face similarity is fundamentally continuous and depends on who is doing the judging.", TEAL, TEAL_SOFT),
        ("cue_s03_c2_could_learn_representation_directly", "Align with perception",
         "Learn a representation aligned with human perception to skip semantic labels while still measuring diversity.", PRIMARY, PRIMARY_SOFT),
        ("cue_s03_c3_existing_psychological_embedding_met", "Prior embeddings fail",
         "They either cannot embed new faces beyond the training set, or pool every judgment and lose annotator differences.", ROSE, ROSE_SOFT),
    ]
    cw = 540
    gx, gy, gap = 110, 320, 40
    ch = 560
    for i, (aid, title, body, ac, soft) in enumerate(cards):
        cx = gx + i * (cw + gap)
        o, c = card(cx, gy, cw, ch, aid=aid, fill=WHITE, stroke=LINE, sw=2, rx=22)
        b.append(o)
        b.append(rrect(cx + 22, gy, cw - 44, 12, ac, rx=6))
        b.append(rrect(cx + 44, gy + 54, 70, 70, soft, rx=16))
        b.append(T(cx + 79, gy + 100, str(i+1), 40, ac, "bold", anchor="middle"))
        b.append(T(cx + 44, gy + 190, title, 32, INK, "bold"))
        txt, _ = para(cx + 44, gy + 250, body, 28, MUTED, maxw=cw - 88, lh=1.5)
        b.append(txt)
        b.append(c)
    b.append(footer(3))
    write("03_motivation.svg", "\n".join(b))


# =================================================================== SLIDE 4
def s4_contribution():
    b = []
    h, y0 = header("Contribution", "A View From Somewhere (AVFS)", PRIMARY)
    b.append(h)
    # big brand card
    o, c = card(110, 300, 520, 630, aid="cue_s04_c1_their_answer_view_somewhere_avfs",
                fill=PRIMARY, stroke="none", sw=0, rx=24)
    b.append(o)
    b.append(T(370, 470, "AVFS", 130, WHITE, "bold", anchor="middle", ls="4"))
    b.append(T(370, 540, "A View From Somewhere", 30, "#C9CCF6", "bold", anchor="middle"))
    txt, _ = para(160, 640, "A conditional framework that learns face representations directly from human similarity judgments.", 30, "#E7E8FB", maxw=420, lh=1.5)
    b.append(txt)
    b.append(c)
    # right two stacked cards
    o, c = card(674, 300, 1136, 300, aid="cue_s04_c2_they_collect_dataset_six_hundred",
                fill=WHITE, stroke=LINE, sw=2, accent=TEAL)
    b.append(o)
    b.append(T(720, 375, "A new judgment dataset", 34, INK, "bold"))
    # three inline stats
    stats = [("638K", 52, "triplet judgments"), ("~5K", 52, "faces"), ("+ identity", 40, "annotator id & demographics")]
    for i, (v, vs, l) in enumerate(stats):
        sx = 720 + i * 360
        b.append(T(sx, 470, v, vs, TEAL, "bold", font=FM))
        tt, _ = para(sx, 510, l, 24, MUTED, maxw=340, lh=1.3)
        b.append(tt)
    b.append(c)
    o, c = card(674, 630, 1136, 300, aid="cue_s04_c3_top_they_build_conditional_learning",
                fill=WHITE, stroke=LINE, sw=2, accent=PRIMARY)
    b.append(o)
    b.append(T(720, 705, "A conditional learning framework", 34, INK, "bold"))
    tt, _ = para(720, 765, "Produces a continuous, low-dimensional, human-interpretable embedding space, plus per-annotator masks showing how different people weigh different visual dimensions.", 28, MUTED, maxw=1050, lh=1.5)
    b.append(tt)
    b.append(c)
    b.append(footer(4))
    write("04_contribution.svg", "\n".join(b))


# =================================================================== SLIDE 5
def s5_method():
    b = []
    h, y0 = header("Method", "Conditional odd-one-out embedding", PRIMARY)
    b.append(h)
    # pipeline: 4 modules left->right
    mods = [
        ("cue_s05_c1_core_conditional_convolutional_netwo", "ResNet-18 encoder",
         ["Face -> 128-d embedding", "Triplet odd-one-out:", "pick the least-similar face"], TEAL, TEAL_SOFT),
        ("cue_s05_c2_annotator_assigned_learnable_gating", "Annotator gating mask",
         ["Learnable mask m per", "annotator: m = sigmoid(w)", "scales each dimension"], PRIMARY, PRIMARY_SOFT),
        ("cue_s05_c3_similarity_between_two_faces_dot", "Masked similarity",
         ["s = < ReLU(e_a)*m ,", "      ReLU(e_b)*m >", "-> odd-one-out prob"], AMBER, AMBER_SOFT),
        ("cue_s05_c4_sparsity_non_negativity_penalty_keep", "Sparse & non-negative",
         ["Sparsity + non-negativity", "penalty on dimensions", "~22 active dims remain"], ROSE, ROSE_SOFT),
    ]
    cw = 400
    gx, gy, gap = 110, 330, 33
    ch = 470
    for i, (aid, title, lines, ac, soft) in enumerate(mods):
        cx = gx + i * (cw + gap)
        o, c = card(cx, gy, cw, ch, aid=aid, fill=WHITE, stroke=LINE, sw=2, rx=20)
        b.append(o)
        b.append(rrect(cx + 40, gy + 44, 64, 64, soft, rx=14))
        b.append(T(cx + 72, gy + 88, str(i+1), 36, ac, "bold", anchor="middle", font=FM))
        b.append(T(cx + 40, gy + 165, title, 29, INK, "bold"))
        yy = gy + 222
        for ln in lines:
            fnt = FM if ("(" in ln or "<" in ln or "->" in ln or "=" in ln or "*" in ln) else FS
            b.append(T(cx + 40, yy, ln, 21, MUTED, font=fnt))
            yy += 42
        b.append(c)
        # arrow between
        if i < 3:
            ax = cx + cw + 4
            b.append(T(ax + 12, gy + ch/2 + 12, "->", 40, MUTED, "bold", anchor="middle", font=FM))
    # bottom note
    b.append(T(110, 900, "Trained end-to-end on 638K odd-one-out judgments; masks are the only per-annotator parameters.", 26, MUTED))
    b.append(footer(5))
    write("05_method.svg", "\n".join(b))


# =================================================================== SLIDE 6
def s6_dataset():
    b = []
    h, y0 = header("Dataset / Benchmark", "638K judgments, annotator-aware", TEAL)
    b.append(h)
    o, c = card(110, 300, 828, 300, aid="cue_s06_c1_avfs_dataset_comprises_six_hundred",
                fill=WHITE, stroke=LINE, sw=2, accent=TEAL)
    b.append(o)
    b.append(T(154, 372, "Dataset composition", 32, INK, "bold"))
    b.append(T(154, 470, "638,000", 62, TEAL, "bold", font=FM))
    b.append(T(154, 512, "triplet judgments", 26, MUTED))
    b.append(T(560, 470, "4,921", 62, PRIMARY, "bold", font=FM))
    b.append(T(560, 512, "near-frontal faces", 26, MUTED))
    b.append(c)
    o, c = card(110, 630, 828, 300, aid="cue_s06_c2_every_single_judgment_carries_annota",
                fill=PRIMARY_SOFT, stroke="none", sw=0, accent=PRIMARY)
    b.append(o)
    b.append(T(154, 702, "Every judgment is labeled by who made it", 32, INK, "bold"))
    tt, _ = para(154, 762, "Each triplet records the annotator's identifier and self-identified demographic attributes, enabling per-annotator conditioning.", 28, INK, maxw=740, lh=1.5)
    b.append(tt)
    b.append(c)
    # right: evaluation card
    o, c = card(978, 300, 832, 630, aid="cue_s06_c3_authors_evaluate_held_out_judgments",
                fill=WHITE, stroke=LINE, sw=2, accent=AMBER)
    b.append(o)
    b.append(T(1022, 372, "Three evaluations", 32, INK, "bold"))
    rows = [
        ("Same stimuli", "held-out judgments over the same 4,921 faces"),
        ("Novel stimuli", "80,000 judgments over entirely new faces"),
        ("Semantic baselines", "attribute recognizers trained on CelebA + FairFace"),
    ]
    yy = 460
    for t, d in rows:
        b.append(rrect(1022, yy - 34, 14, 14, AMBER, rx=3))
        b.append(T(1056, yy, t, 30, INK, "bold"))
        tt, ny = para(1056, yy + 42, d, 26, MUTED, maxw=700, lh=1.4)
        b.append(tt)
        yy = ny + 60
    b.append(c)
    b.append(footer(6))
    write("06_dataset_benchmark.svg", "\n".join(b))


# =================================================================== SLIDE 7
def s7_key_result():
    b = []
    h, y0 = header("Key Result", "Beats semantic-label baselines", TEAL)
    b.append(h)
    # anchor c1: results figures panel
    o, c = card(110, 300, 1130, 630, aid="cue_s07_c1_across_both_same_stimuli_novel_stimu",
                fill=WHITE, stroke=LINE, sw=2, accent=TEAL)
    b.append(o)
    b.append(T(154, 366, "Predicting human similarity judgments", 32, INK, "bold"))
    b.append(T(154, 410, "Accuracy and Spearman's r vs. baselines trained on semantic labels", 24, MUTED))
    b.append(T(154, 470, "Same stimuli (Fig. 1)", 26, TEAL, "bold"))
    b.append(f'<image x="154" y="486" width="1040" height="200" href="{b64(os.path.join(FIG,"figure1.png"))}" preserveAspectRatio="xMidYMid meet"/>')
    b.append(T(154, 730, "Novel stimuli (Fig. 3)", 26, PRIMARY, "bold"))
    b.append(f'<image x="154" y="746" width="1040" height="160" href="{b64(os.path.join(FIG,"figure3.png"))}" preserveAspectRatio="xMidYMid meet"/>')
    b.append(c)
    # anchor c2: takeaway card
    o, c = card(1280, 300, 530, 630, aid="cue_s07_c2_importantly_annotator_specific_masks",
                fill=TEAL_SOFT, stroke="none", sw=0, accent=TEAL)
    b.append(o)
    b.append(T(1320, 372, "Masks generalize", 34, INK, "bold"))
    tt, ny = para(1320, 440, "Annotator-specific masks transfer even to triplets of entirely novel faces.", 28, INK, maxw=450, lh=1.5)
    b.append(tt)
    b.append(rrect(1320, ny + 30, 450, 2, TEAL))
    tt, _ = para(1320, ny + 90, "The embedding is far more aligned with the human mental representation of faces than spaces from categorical labels.", 27, MUTED, maxw=450, lh=1.5)
    b.append(tt)
    b.append(c)
    b.append(footer(7))
    write("07_key_result.svg", "\n".join(b))


# =================================================================== SLIDE 8
def s8_ablation():
    b = []
    h, y0 = header("Ablation Study", "Annotators are not interchangeable", ROSE)
    b.append(h)
    o, c = card(110, 300, 560, 630, aid="cue_s08_c1_test_whether_annotators_really_matte",
                fill=WHITE, stroke=LINE, sw=2, accent=PRIMARY)
    b.append(o)
    b.append(T(154, 372, "Shuffle test", 34, INK, "bold"))
    tt, _ = para(154, 440, "Randomly re-assign which annotator mask attaches to each of the 80K judgments, and recompute accuracy 100 times.", 28, MUTED, maxw=480, lh=1.5)
    b.append(tt)
    b.append(rrect(154, 640, 460, 210, PRIMARY_SOFT, rx=16))
    b.append(T(384, 720, "80,000", 56, PRIMARY, "bold", anchor="middle", font=FM))
    b.append(T(384, 770, "judgments  ·  x100 shuffles", 26, MUTED, anchor="middle"))
    b.append(c)
    # big drop stat
    o, c = card(710, 300, 560, 630, aid="cue_s08_c2_accuracy_drops_about_sixty_two_perce",
                fill=ROSE_SOFT, stroke="none", sw=0, accent=ROSE)
    b.append(o)
    b.append(T(990, 380, "Accuracy collapses", 32, INK, "bold", anchor="middle"))
    b.append(T(990, 520, "62%", 96, INK, "bold", anchor="middle", font=FM))
    b.append(T(990, 560, "true annotators", 26, MUTED, anchor="middle"))
    b.append(T(990, 600, "v", 40, ROSE, "bold", anchor="middle"))
    b.append(T(990, 720, "53%", 96, ROSE, "bold", anchor="middle", font=FM))
    b.append(T(990, 760, "shuffled annotators", 26, MUTED, anchor="middle"))
    b.append(c)
    # dim elimination
    o, c = card(1310, 300, 500, 630, aid="cue_s08_c3_dimension_elimination_analysis_furth",
                fill=WHITE, stroke=LINE, sw=2, accent=AMBER)
    b.append(o)
    b.append(T(1354, 372, "How many dimensions?", 32, INK, "bold"))
    b.append(T(1354, 490, "6-13", 74, AMBER, "bold", font=FM))
    tt, _ = para(1354, 540, "dimensions recover most predictive accuracy", 26, MUTED, maxw=420, lh=1.4)
    b.append(tt)
    b.append(T(1354, 700, "15-22", 74, PRIMARY, "bold", font=FM))
    tt, _ = para(1354, 750, "dimensions explain the full similarity structure", 26, MUTED, maxw=420, lh=1.4)
    b.append(tt)
    b.append(T(1354, 880, "Similarity is context-dependent.", 24, INK, "bold"))
    b.append(c)
    b.append(footer(8))
    write("08_ablation_study.svg", "\n".join(b))


# =================================================================== SLIDE 9
def s9_headline():
    b = []
    # header anchor c1
    o, c = card(110, 84, 1700, 150, aid="cue_s09_c1_headline_numbers_tell_whole_story",
                fill="none", stroke="none", sw=0, rx=0)
    b.append(o)
    b.append(rrect(110, 90, 54, 8, GOLD, rx=4))
    b.append(T(180, 106, "HEADLINE NUMBERS", 26, GOLD, "bold", ls="3"))
    b.append(T(110, 182, "The whole story in four numbers", 62, INK, "bold"))
    b.append(f'<line x1="110" y1="216" x2="1810" y2="216" stroke="{LINE}" stroke-width="2"/>')
    b.append(c)
    tiles = [
        ("cue_s09_c2_six_hundred_thirty_eight_thousand_hu", "638K", "human judgments", "over 4,921 distinct faces", PRIMARY, PRIMARY_SOFT),
        ("cue_s09_c3_twenty_two_interpretable_embedding_d", "22", "interpretable dimensions", "retained at ~62% val. accuracy", TEAL, TEAL_SOFT),
        ("cue_s09_c4_when_annotator_identities_scrambled", "61.7 -> 52.8", "% accuracy", "when annotators are scrambled", ROSE, ROSE_SOFT),
    ]
    cw = 540
    gx, gy, gap = 110, 300, 40
    ch = 560
    for i, (aid, big, lab, sub, ac, soft) in enumerate(tiles):
        cx = gx + i * (cw + gap)
        o, c = card(cx, gy, cw, ch, aid=aid, fill=soft, stroke="none", sw=0, rx=24)
        b.append(o)
        b.append(rrect(cx + 24, gy, cw - 48, 12, ac, rx=6))
        fs_big = 150 if i < 2 else 84
        b.append(T(cx + cw/2, gy + 300, big, fs_big, ac, "bold", anchor="middle", font=FM))
        b.append(T(cx + cw/2, gy + 400, lab, 36, INK, "bold", anchor="middle"))
        b.append(T(cx + cw/2, gy + 460, sub, 27, MUTED, anchor="middle"))
        b.append(c)
    b.append(T(110, 990, "All achieved without ever training on a single semantic label.", 30, INK, "bold"))
    b.append(footer(9))
    write("09_headline_numbers.svg", "\n".join(b))


# =================================================================== SLIDE 10
def s10_takeaway():
    b = []
    h, y0 = header("Takeaway", "Perception over taxonomy", PRIMARY)
    b.append(h)
    o, c = card(110, 300, 1130, 630, aid="cue_s10_c1_key_takeaway_learning_face_represent",
                fill=WHITE, stroke=LINE, sw=2, accent=PRIMARY)
    b.append(o)
    b.append(T(154, 384, "Learn from judgments, not labels", 40, INK, "bold"))
    tt, ny = para(154, 460, "Learning face representations from human similarity judgments, rather than demographic labels, yields a continuous, interpretable, perception-aligned embedding space.", 32, MUTED, maxw=1040, lh=1.55)
    b.append(tt)
    chips = ["Continuous", "Interpretable", "Perception-aligned", "Label-free diversity"]
    xx = 154
    for ch_txt in chips:
        cs, cwid = chip(xx, ny + 40, ch_txt, PRIMARY_SOFT, PRIMARY)
        b.append(cs)
        xx += cwid + 20
    b.append(c)
    o, c = card(1280, 300, 530, 630, aid="cue_s10_c2_because_framework_only_requires_keep",
                fill=TEAL_SOFT, stroke="none", sw=0, accent=TEAL)
    b.append(o)
    b.append(T(1320, 384, "Beyond faces", 36, INK, "bold"))
    tt, _ = para(1320, 450, "The framework only needs to track which annotator made which judgment, so the same conditional approach extends to almost any task built on human decisions.", 29, MUTED, maxw=450, lh=1.55)
    b.append(tt)
    # resource references (text-only; keeps this a purely textual slide)
    b.append(rrect(1320, 770, 450, 140, WHITE, LINE, 2, 16))
    b.append(T(1344, 818, "Paper  ·  arXiv:2303.17176", 25, INK, "bold"))
    b.append(T(1344, 862, "Code  ·  github.com/SonyAI/", 22, MUTED))
    b.append(T(1344, 892, "a_view_from_somewhere", 22, MUTED))
    b.append(c)
    b.append(footer(10))
    write("10_takeaway.svg", "\n".join(b))


if __name__ == "__main__":
    s1_title(); s2_problem(); s3_motivation(); s4_contribution(); s5_method()
    s6_dataset(); s7_key_result(); s8_ablation(); s9_headline(); s10_takeaway()
    print("done ->", OUT)
