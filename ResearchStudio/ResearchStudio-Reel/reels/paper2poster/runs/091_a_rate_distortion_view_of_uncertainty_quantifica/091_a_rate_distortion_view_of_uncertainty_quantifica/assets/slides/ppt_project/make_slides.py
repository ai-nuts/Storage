#!/usr/bin/env python3
"""All-native SVG deck builder for paper2video (run 091 — Distance Aware Bottleneck / DAB).

Every required narration chunk from visual_anchor_contract.json becomes its own
<g id="cue_sXX_cN_..."> card carrying a <title> of the narration keywords, so the
strict --require-pptx-anchors cue pass resolves each cue from PPTX geometry.
Zero <image> elements -> the image-size gates never fire.
"""
import json, os, html

HERE = os.path.dirname(os.path.abspath(__file__))
CONTRACT = os.path.join(HERE, "..", "..", "meta", "visual_anchor_contract.json")
OUT = os.path.join(HERE, "svg_output")
os.makedirs(OUT, exist_ok=True)

W, H = 1280, 720
# ---- palette (dark cobalt/teal) ----
BG       = "#0e131f"
BG2      = "#0b0f18"
CARD     = "#1a2536"
CARD2    = "#212f45"
STROKE   = "#2f4straight".replace("4straight", "4160")  # #2f4160
COBALT   = "#4f7cff"
TEAL     = "#33d6c6"
GREEN    = "#46d19e"
RED      = "#ff6b6b"
AMBER    = "#f4b451"
INK      = "#eaf1fb"
MUTE     = "#9db0cc"
FAINT    = "#6f819c"

SANS  = "Arial, 'Helvetica Neue', Helvetica, sans-serif"
MONO  = "'DejaVu Sans Mono', 'Courier New', monospace"

# every hex + font used, for spec_lock colors/typography drift check
COLORS = [BG, BG2, CARD, CARD2, "#2f4160", COBALT, TEAL, GREEN, RED, AMBER, INK, MUTE, FAINT, "#ffffff", "#0e131f"]

def esc(s): return html.escape(str(s), quote=True)

# ---------- primitive helpers ----------
def rect(x,y,w,h,fill,rx=14,stroke=None,sw=1,opacity=None):
    s=f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" fill="{fill}"'
    if stroke: s+=f' stroke="{stroke}" stroke-width="{sw}"'
    if opacity is not None: s+=f' opacity="{opacity}"'
    return s+'/>'

def line(x1,y1,x2,y2,stroke,sw=2,dash=None,opacity=None):
    s=f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{stroke}" stroke-width="{sw}"'
    if dash: s+=f' stroke-dasharray="{dash}"'
    if opacity is not None: s+=f' opacity="{opacity}"'
    return s+'/>'

def txt(x,y,s,size=22,fill=INK,weight="normal",anchor="start",family=SANS,ls=None,italic=False):
    a=f' text-anchor="{anchor}"' if anchor!="start" else ""
    w=f' font-weight="{weight}"' if weight!="normal" else ""
    l=f' letter-spacing="{ls}"' if ls else ""
    i=' font-style="italic"' if italic else ""
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-family="{family}" font-size="{size}"'
            f' fill="{fill}"{w}{a}{l}{i}>{esc(s)}</text>')

def circle(cx,cy,r,fill,stroke=None,sw=1,opacity=None):
    s=f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="{fill}"'
    if stroke: s+=f' stroke="{stroke}" stroke-width="{sw}"'
    if opacity is not None: s+=f' opacity="{opacity}"'
    return s+'/>'

def polyline(pts,stroke,sw=3,fill="none",dash=None):
    p=" ".join(f"{x:.1f},{y:.1f}" for x,y in pts)
    s=f'<polyline points="{p}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"'
    if dash: s+=f' stroke-dasharray="{dash}"'
    return s+'/>'

# ---------- contract ----------
C = json.load(open(CONTRACT))
KW = {}     # chunk_id -> keyword string
AID = {}    # chunk_id -> anchor_id
for s in C["slides"]:
    for c in s.get("chunks", []):
        KW[c["chunk_id"]] = " ".join(c["cue_keywords"])
        AID[c["chunk_id"]] = c["anchor_id"]

def cue_open(chunk_id, extra_desc=""):
    aid = AID[chunk_id]; kw = KW[chunk_id]
    d = f'<desc>{esc(extra_desc)}</desc>' if extra_desc else ""
    return f'<g id="{aid}" data-cue-label="{aid}"><title>{esc(kw)}</title>{d}'
def cue_close(): return '</g>'

# card that IS a cue anchor: rounded panel + header + body lines
def cue_card(chunk_id, x, y, w, h, header, lines, accent=COBALT, hsize=22, bsize=17,
             body_fill=MUTE, header_fill=INK, extra=""):
    out=[cue_open(chunk_id)]
    out.append(rect(x,y,w,h,CARD,rx=16,stroke="#2f4160",sw=1.2))
    out.append(rect(x,y+16,4.5,h-32,accent,rx=2.2))
    ty=y+34
    if header:
        out.append(txt(x+22,ty,header,size=hsize,fill=header_fill,weight="bold"))
        ty+=8
    ty+=22
    for ln in lines:
        out.append(txt(x+22,ty,ln,size=bsize,fill=body_fill))
        ty+=bsize+8
    if extra: out.append(extra)
    out.append(cue_close())
    return "\n".join(out)

def header_band(title, kicker):
    out=[]
    # inset accent (NOT full-bleed; starts below the 13px edge band, off L/R edges)
    out.append(rect(64,44,6,34,TEAL,rx=3))
    out.append(txt(84,58,kicker,size=15,fill=TEAL,weight="bold",ls="2.5"))
    out.append(txt(83,90,title,size=34,fill=INK,weight="bold"))
    return "\n".join(out)

def svg_wrap(body, page_role):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}"'
            f' data-pptx-page-role="{page_role}" font-family="{SANS}">\n'
            f'<rect x="0" y="0" width="{W}" height="{H}" fill="{BG}"/>\n'
            f'<rect x="0" y="0" width="{W}" height="{H}" fill="{BG}"/>\n'
            + body + "\n</svg>\n")

SLIDES=[]
def add(fn, body, role):
    SLIDES.append((fn, svg_wrap(body, role)))

# ======================================================================
# SLIDE 01 — TITLE
# ======================================================================
def s01():
    b=[]
    # left text column (kept clear of the right concept panel which starts x=720)
    b.append(rect(64,60,6,120,COBALT,rx=3))
    b.append(txt(88,96,"ICML 2024",size=17,fill=TEAL,weight="bold",ls="3"))
    b.append(txt(86,150,"A Rate-Distortion View of",size=40,fill=INK,weight="bold"))
    b.append(txt(86,198,"Uncertainty Quantification",size=40,fill=INK,weight="bold"))
    b.append(txt(88,244,"Distance Aware Bottleneck (DAB)",size=24,fill=COBALT,weight="bold"))
    b.append(txt(88,286,'Giving deep networks a sense of "knowing',size=19,fill=MUTE))
    b.append(txt(88,312,'what they don\'t know."',size=19,fill=MUTE))
    # concept anchor card (right side)
    inner=[]
    inner.append(txt(748,150,"The idea in one line",size=17,fill=TEAL,weight="bold"))
    # mini flow: data -> codebook -> distance -> uncertainty
    y=210
    def chip(x,w,t1,t2,col):
        g=[rect(x,y,w,74,CARD2,rx=12,stroke="#2f4160",sw=1)]
        g.append(txt(x+w/2,y+32,t1,size=16,fill=INK,weight="bold",anchor="middle"))
        g.append(txt(x+w/2,y+55,t2,size=13,fill=MUTE,anchor="middle"))
        return "\n".join(g)
    b_card=[rect(724,120,492,470,CARD,rx=18,stroke="#2f4160",sw=1.2)]
    b_card.append("\n".join(inner))
    b_card.append(chip(748,150,"Training data","compress",COBALT))
    b_card.append(chip(748+168,150,"Codebook","10 prototype dists",TEAL))
    b_card.append(txt(748+150+9,y+37,"→",size=26,fill=FAINT,anchor="middle"))
    y2=330
    b_card.append(rect(748,y2,468,70,CARD2,rx=12,stroke="#2f4160",sw=1))
    b_card.append(txt(770,y2+30,"distance of a new input to the codebook",size=15,fill=MUTE))
    b_card.append(txt(770,y2+54,"= principled uncertainty score",size=17,fill=INK,weight="bold"))
    b_card.append(rect(748,y2+92,468,64,"#152034",rx=12,stroke=TEAL,sw=1.2))
    b_card.append(txt(772,y2+120,"computed in a single forward pass",size=17,fill=TEAL,weight="bold"))
    b_card.append(circle(1180,y2+124,7,GREEN))
    card=cue_open("s01_c01")+"\n"+"\n".join(b_card)+"\n"+cue_close()
    b.append(card)
    b.append(txt(88,560,"Reframes uncertainty quantification as a rate–distortion problem.",size=16,fill=FAINT))
    add("01_title.svg","\n".join(b),"cover")

# ======================================================================
# SLIDE 02 — PROBLEM (3 chunks)
# ======================================================================
def s02():
    b=[header_band("Confident, even when far from the data","PROBLEM")]
    y0=150; ch=430; gap=22; cw=(1152-2*gap)/3
    x=64
    b.append(cue_card("s02_c01",x,y0,cw,ch,"Know your limits",
        ["A trustworthy model","should know when it is","operating far from what","it has seen.",
         "","Reliable uncertainty is","the missing signal."],accent=TEAL,hsize=21))
    # small illustrative dot: in-dist cluster vs far point
    x+=cw+gap
    inner=[circle(x+cw/2-40,y0+320,5,COBALT) for _ in range(0)]
    b.append(cue_card("s02_c02",x,y0,cw,ch,"But deep nets don't",
        ["Deep neural networks","often make highly","confident predictions",
         "even on inputs wildly","different from their","training data.",
         "","Overconfidence = risk."],accent=RED,hsize=21))
    x+=cw+gap
    b.append(cue_card("s02_c03",x,y0,cw,ch,"GPs vs deep nets",
        ["Gaussian Processes have","a built-in sense of","distance from the","training set.",
         "","Standard deep networks","do not — efficient UQ","stays an open problem."],accent=COBALT,hsize=21))
    add("02_problem.svg","\n".join(b),"content")

# ======================================================================
# SLIDE 03 — MOTIVATION (4 chunks 2x2)
# ======================================================================
def s03():
    b=[header_band("Fast or distance-aware — why not both?","MOTIVATION")]
    y0=150; gy=[y0, y0+218]; gh=200; gap=22; cw=(1152-gap)/2; xs=[64,64+cw+gap]
    b.append(cue_card("s03_c01",xs[0],gy[0],cw,gh,"Single-pass tricks",
        ["Fast one-forward-pass methods lean on architectural",
         "tricks — e.g. spectral normalization — to stop the",
         "network's features from collapsing."],accent=COBALT,bsize=16))
    b.append(cue_card("s03_c02",xs[1],gy[0],cw,gh,"Hidden costs",
        ["Those constraints can quietly damage calibration and",
         "are awkward to bolt onto large pre-trained models."],accent=AMBER,bsize=16))
    b.append(cue_card("s03_c03",xs[0],gy[1],cw,gh,"Ensembles are pricey",
        ["Deep ensembles and Bayesian nets are naturally",
         "distance-aware — but need many forward passes,",
         "which is expensive at scale."],accent=RED,bsize=16))
    # c4 = highlighted question banner
    x=xs[1]; y=gy[1]
    inner=[rect(x,y,cw,gh,"#152239",rx=16,stroke=TEAL,sw=1.6)]
    inner.append(rect(x,y+16,4.5,gh-32,TEAL,rx=2.2))
    inner.append(txt(x+22,y+40,"The question",size=17,fill=TEAL,weight="bold"))
    inner.append(txt(x+22,y+86,"Can a single deterministic",size=20,fill=INK,weight="bold"))
    inner.append(txt(x+22,y+116,"model be distance-aware",size=20,fill=INK,weight="bold"))
    inner.append(txt(x+22,y+146,"without any of these drawbacks?",size=18,fill=MUTE))
    b.append(cue_open("s03_c04")+"\n"+"\n".join(inner)+"\n"+cue_close())
    add("03_motivation.svg","\n".join(b),"content")

# ======================================================================
# SLIDE 04 — CONTRIBUTION (4 chunks)
# ======================================================================
def s04():
    b=[header_band("Uncertainty as compression","CONTRIBUTION")]
    y0=150; gy=[y0, y0+218]; gh=200; gap=22; cw=(1152-gap)/2; xs=[64,64+cw+gap]
    b.append(cue_card("s04_c01",xs[0],gy[0],cw,gh,"1  Rate–distortion lens",
        ["View uncertainty quantification through the lens of",
         "rate–distortion theory — a fresh, principled framing."],accent=COBALT,bsize=16))
    b.append(cue_card("s04_c02",xs[1],gy[0],cw,gh,"2  Compress → measure",
        ["Compress the entire training set into a small codebook",
         "of prototype distributions, then measure how far a new",
         "input is from that codebook."],accent=TEAL,bsize=16))
    b.append(cue_card("s04_c03",xs[0],gy[1],cw,gh,"3  The DAB model",
        ["The Distance Aware Bottleneck (DAB): one deterministic",
         "model that produces uncertainty in a single forward pass."],accent=GREEN,bsize=16))
    b.append(cue_card("s04_c04",xs[1],gy[1],cw,gh,"4  Practical toolkit",
        ["An alternating-minimization training algorithm, a",
         "meta-probabilistic distortion over distributions of",
         "embeddings, and a post-hoc variant for pre-trained nets."],accent=AMBER,bsize=16))
    add("04_contribution.svg","\n".join(b),"content")

# ======================================================================
# SLIDE 05 — METHOD (4 chunks) with a small pipeline diagram
# ======================================================================
def s05():
    b=[header_band("How DAB measures distance","METHOD")]
    # top row: c1 wide, c4 wide
    y0=150
    b.append(cue_card("s05_c01",64,y0,566,132,"Rate term, reimagined",
        ["Builds on the Information Bottleneck, but replaces its",
         "rate term with an achievable rate from rate–distortion",
         "theory with finite cardinality."],accent=COBALT,bsize=15))
    b.append(cue_card("s05_c04",650,y0,566,132,"A Gaussian-Process analogue",
        ["Closely analogous to a GP: the codebook plays the role",
         "of inducing points, and statistical distance replaces",
         "Euclidean distance."],accent=TEAL,bsize=15))
    # c2 = pipeline diagram card
    y1=300; ph=232
    inner=[rect(64,y1,566,ph,CARD,rx=16,stroke="#2f4160",sw=1.2)]
    inner.append(rect(64,y1+16,4.5,ph-32,GREEN,rx=2.2))
    inner.append(txt(86,y1+34,"Codebook of centroid distributions",size=18,fill=INK,weight="bold"))
    # nodes
    def node(cx,cy,r,lab,col,sub=None):
        g=[circle(cx,cy,r,"#152034",stroke=col,sw=2)]
        g.append(txt(cx,cy+5,lab,size=14,fill=INK,weight="bold",anchor="middle"))
        if sub: g.append(txt(cx,cy+r+18,sub,size=12,fill=MUTE,anchor="middle"))
        return "\n".join(g)
    ex=120; ey=y1+120
    inner.append(node(ex,ey,30,"x","#4f7cff","new input"))
    inner.append(txt(ex+52,ey+4,"→",size=24,fill=FAINT,anchor="middle"))
    inner.append(node(ex+104,ey,34,"enc","#33d6c6","embed dist."))
    # codebook centroids cluster
    cbx=430; cby=ey
    for i,(dx,dy) in enumerate([(-34,-30),(6,-40),(40,-14),(28,26),(-16,34),(-44,6)]):
        inner.append(circle(cbx+dx,cby+dy,9,TEAL,opacity=0.85))
    inner.append(txt(cbx+2,y1+205,"codebook (10 codes)",size=12,fill=MUTE,anchor="middle"))
    inner.append(line(ex+142,ey,cbx-52,cby,FAINT,2,dash="5 5"))
    inner.append(txt((ex+142+cbx-52)/2,ey-12,"KL distance",size=13,fill=GREEN,anchor="middle",weight="bold"))
    b.append(cue_open("s05_c02")+"\n"+"\n".join(inner)+"\n"+cue_close())
    # c3 = alternating training card
    y2=300
    b.append(cue_card("s05_c03",650,y2,566,ph,"Alternating optimization",
        ["Gradient updates of the encoder & decoder, alternating",
         "with cheap analytic updates of the soft assignments",
         "and centroids — echoing the classic",
         "Blahut–Arimoto algorithm."],accent=AMBER,bsize=16))
    add("05_method.svg","\n".join(b),"content")

# ======================================================================
# SLIDE 06 — DATASET / BENCHMARK (4 chunks)
# ======================================================================
def s06():
    b=[header_band("How it is evaluated","DATASET / BENCHMARK")]
    y0=150; gy=[y0, y0+218]; gh=200; gap=22; cw=(1152-gap)/2; xs=[64,64+cw+gap]
    b.append(cue_card("s06_c01",xs[0],gy[0],cw,gh,"Several settings",
        ["Tested across several complementary settings — from",
         "small-scale OOD detection to large-scale ImageNet."],accent=COBALT,bsize=16))
    # c2 = ID/OOD map
    x=xs[1]; y=gy[0]
    inner=[rect(x,y,cw,gh,CARD,rx=16,stroke="#2f4160",sw=1.2)]
    inner.append(rect(x,y+16,4.5,gh-32,TEAL,rx=2.2))
    inner.append(txt(x+22,y+34,"CIFAR-10 benchmark",size=18,fill=INK,weight="bold"))
    def pill(px,py,t,sub,col):
        g=[rect(px,py,150,58,"#152034",rx=10,stroke=col,sw=1.4)]
        g.append(txt(px+75,py+26,t,size=16,fill=INK,weight="bold",anchor="middle"))
        g.append(txt(px+75,py+46,sub,size=12,fill=MUTE,anchor="middle"))
        return "\n".join(g)
    inner.append(pill(x+22,y+70,"CIFAR-10","in-distribution",GREEN))
    inner.append(pill(x+196,y+70,"SVHN","far OOD",COBALT))
    inner.append(pill(x+370,y+70,"CIFAR-100","near OOD (hard)",AMBER))
    inner.append(txt(x+22,y+168,"far vs. near out-of-distribution stress tests",size=14,fill=MUTE))
    b.append(cue_open("s06_c02")+"\n"+"\n".join(inner)+"\n"+cue_close())
    b.append(cue_card("s06_c03",xs[0],gy[1],cw,gh,"And at scale",
        ["Also: misclassification prediction on CIFAR-10, then",
         "scaling up to ImageNet-1K with ImageNet-O as the",
         "out-of-distribution set."],accent=GREEN,bsize=16))
    b.append(cue_card("s06_c04",xs[1],gy[1],cw,gh,"Tiny bottleneck, strong field",
        ["Just an 8-dim latent bottleneck and 10 distributional",
         "codes. Compared against deep ensembles, DDU, DUQ,",
         "DUE, SNGP, and the vanilla variational IB."],accent=COBALT,bsize=16))
    add("06_dataset-benchmark.svg","\n".join(b),"content")

# ======================================================================
# SLIDE 07 — KEY RESULT (3 chunks) with AUROC bar chart
# ======================================================================
def s07():
    b=[header_band("Best-in-class OOD detection","KEY RESULT")]
    y0=150
    # c1 headline banner (top wide)
    x=64; y=y0; w=1152; h=76
    inner=[rect(x,y,w,h,"#152239",rx=14,stroke=TEAL,sw=1.5)]
    inner.append(rect(x,y+14,4.5,h-28,TEAL,rx=2.2))
    inner.append(txt(x+24,y+46,"DAB outperforms every baseline on both out-of-distribution tasks.",size=21,fill=INK,weight="bold"))
    b.append(cue_open("s07_c01")+"\n"+"\n".join(inner)+"\n"+cue_close())
    # c2 = AUROC chart card
    y1=y0+96; ch=344
    inner=[rect(64,y1,700,ch,CARD,rx=16,stroke="#2f4160",sw=1.2)]
    inner.append(rect(64,y1+16,4.5,ch-32,COBALT,rx=2.2))
    inner.append(txt(86,y1+38,"CIFAR-10 → OOD detection (AUROC / AUPRC)",size=17,fill=INK,weight="bold"))
    # grouped bars: two groups (vs SVHN, vs CIFAR-100), AUROC & AUPRC
    base_y=y1+280; maxh=180; scale=lambda v:(v-0.85)/(1.0-0.85)*maxh  # zoom 0.85..1.0
    groups=[("vs SVHN",[("AUROC",0.986,COBALT),("AUPRC",0.994,TEAL)]),
            ("vs CIFAR-100",[("AUROC",0.922,COBALT),("AUPRC",0.915,TEAL)])]
    gx=140
    for gname,bars in groups:
        for i,(lab,val,col) in enumerate(bars):
            bh=scale(val); bx=gx+i*84
            inner.append(rect(bx,base_y-bh,60,bh,col,rx=6))
            inner.append(txt(bx+30,base_y-bh-10,f"{val:.3f}",size=15,fill=INK,weight="bold",anchor="middle",family=MONO))
            inner.append(txt(bx+30,base_y+22,lab,size=12,fill=MUTE,anchor="middle"))
        inner.append(txt(gx+72,base_y+44,gname,size=14,fill=INK,weight="bold",anchor="middle"))
        gx+=300
    inner.append(txt(690,y1+70,"beats even a",size=13,fill=MUTE,anchor="end"))
    inner.append(txt(690,y1+90,"5-model ensemble",size=15,fill=GREEN,weight="bold",anchor="end"))
    b.append(cue_open("s07_c02")+"\n"+"\n".join(inner)+"\n"+cue_close())
    # c3 = efficiency card (params + acc)
    y2=y0+96
    inner=[rect(786,y2,430,ch,CARD,rx=16,stroke="#2f4160",sw=1.2)]
    inner.append(rect(786,y2+16,4.5,ch-32,GREEN,rx=2.2))
    inner.append(txt(808,y2+38,"...in a single forward pass",size=17,fill=INK,weight="bold"))
    # param comparison bars (horizontal)
    def hbar(py,lab,val,maxv,col,vlabel):
        bw=330*val/maxv
        g=[txt(808,py-8,lab,size=14,fill=MUTE)]
        g.append(rect(808,py,330,26,"#152034",rx=6))
        g.append(rect(808,py,bw,26,col,rx=6))
        g.append(txt(808+bw-8 if bw>120 else 808+bw+8,py+18,vlabel,size=13,fill=INK if bw>120 else MUTE,weight="bold",anchor="end" if bw>120 else "start",family=MONO))
        return "\n".join(g)
    inner.append(hbar(y2+96,"DAB (single model)",36.5,182,GREEN,"36.5M"))
    inner.append(hbar(y2+166,"Deep ensemble (×5)",182,182,RED,"182M"))
    inner.append(line(808,y2+240,1196,y2+240,"#2f4160",1))
    inner.append(txt(808,y2+272,"Accuracy held on par",size=14,fill=MUTE))
    inner.append(txt(1196,y2+272,"~96%",size=22,fill=TEAL,weight="bold",anchor="end",family=MONO))
    b.append(cue_open("s07_c03")+"\n"+"\n".join(inner)+"\n"+cue_close())
    add("07_key-result.svg","\n".join(b),"content")

# ======================================================================
# SLIDE 08 — ABLATION STUDY (3 chunks)
# ======================================================================
def s08():
    b=[header_band("Predicting its own mistakes","ABLATION STUDY")]
    y0=150
    # c1 = headline number card (left narrow)
    inner=[rect(64,y0,300,344,CARD,rx=16,stroke="#2f4160",sw=1.2)]
    inner.append(rect(64,y0+16,4.5,344-32,COBALT,rx=2.2))
    inner.append(txt(86,y0+40,"CIFAR-10 misclassification",size=15,fill=INK,weight="bold"))
    inner.append(txt(86,y0+66,"calibration AUROC",size=14,fill=MUTE))
    inner.append(txt(214,y0+180,"0.930",size=64,fill=TEAL,weight="bold",anchor="middle",family=MONO))
    inner.append(txt(214,y0+224,"DAB",size=18,fill=INK,weight="bold",anchor="middle"))
    inner.append(txt(214,y0+284,"near the deep-ensemble",size=13,fill=MUTE,anchor="middle"))
    inner.append(txt(214,y0+306,"ceiling of 0.951",size=13,fill=MUTE,anchor="middle"))
    b.append(cue_open("s08_c01")+"\n"+"\n".join(inner)+"\n"+cue_close())
    # c2 = calibration AUROC bar chart (single-pass methods)
    x=386; w=470; ch=344
    inner=[rect(x,y0,w,ch,CARD,rx=16,stroke="#2f4160",sw=1.2)]
    inner.append(rect(x,y0+16,4.5,ch-32,GREEN,rx=2.2))
    inner.append(txt(x+22,y0+38,"Calibration AUROC vs. single-pass methods",size=16,fill=INK,weight="bold"))
    rows=[("Ensemble ×5",0.951,RED),("DAB",0.930,TEAL),("SNGP",0.897,COBALT),
          ("DUQ",0.889,COBALT),("DUE",0.856,COBALT),("DDU",0.632,FAINT)]
    ry=y0+70; rh=40
    for lab,val,col in rows:
        bw=(val-0.55)/(0.97-0.55)*300
        inner.append(txt(x+22,ry+22,lab,size=14,fill=INK if lab=="DAB" else MUTE,weight="bold" if lab=="DAB" else "normal"))
        inner.append(rect(x+140,ry+4,300,22,"#152034",rx=5))
        inner.append(rect(x+140,ry+4,bw,22,col,rx=5))
        inner.append(txt(x+140+bw+8,ry+21,f"{val:.3f}",size=13,fill=INK,weight="bold",family=MONO))
        ry+=rh
    b.append(cue_open("s08_c02")+"\n"+"\n".join(inner)+"\n"+cue_close())
    # c3 = codebook visualization card
    x=878; w=338
    inner=[rect(x,y0,w,ch,CARD,rx=16,stroke="#2f4160",sw=1.2)]
    inner.append(rect(x,y0+16,4.5,ch-32,AMBER,rx=2.2))
    inner.append(txt(x+22,y0+38,"Learned codebook",size=16,fill=INK,weight="bold"))
    # centroids with attracted points of one class each
    cols=[COBALT,TEAL,GREEN,AMBER,RED,"#b98bff"]
    centers=[(x+90,y0+120),(x+230,y0+110),(x+150,y0+200),(x+260,y0+210),(x+95,y0+270),(x+235,y0+285)]
    import math
    for i,(cx,cy) in enumerate(centers):
        col=cols[i%len(cols)]
        for k in range(6):
            ang=k*1.047+i; rr=14+ (k%3)*7
            inner.append(circle(cx+rr*math.cos(ang),cy+rr*math.sin(ang),3.4,col,opacity=0.8))
        inner.append(circle(cx,cy,6,"#0e131f",stroke=col,sw=2.4))
    inner.append(txt(x+22,y0+318,"10 centroids attract one class each",size=12.5,fill=MUTE))
    b.append(cue_open("s08_c03")+"\n"+"\n".join(inner)+"\n"+cue_close())
    add("08_ablation-study.svg","\n".join(b),"content")

# ======================================================================
# SLIDE 09 — HEADLINE NUMBERS (2 chunks)
# ======================================================================
def s09():
    b=[header_band("The numbers at a glance","HEADLINE NUMBERS")]
    y0=150; ch=430; gap=24; cw=(1152-gap)/2; xs=[64,64+cw+gap]
    def kpi(px,py,val,lab,col):
        g=[txt(px,py,val,size=40,fill=col,weight="bold",family=MONO)]
        g.append(txt(px,py+26,lab,size=13.5,fill=MUTE))
        return "\n".join(g)
    # c1 CIFAR-10
    x=xs[0]; inner=[rect(x,y0,cw,ch,CARD,rx=18,stroke="#2f4160",sw=1.2)]
    inner.append(rect(x,y0+16,4.5,ch-32,COBALT,rx=2.2))
    inner.append(txt(x+26,y0+44,"CIFAR-10 (small scale)",size=19,fill=INK,weight="bold"))
    inner.append(kpi(x+26,y0+130,"0.986","OOD AUROC vs SVHN  (best in class)",COBALT))
    inner.append(kpi(x+26,y0+230,"0.922","OOD AUROC vs CIFAR-100  (hard, near)",TEAL))
    inner.append(kpi(x+26,y0+330,"0.930","misclassification calibration AUROC",GREEN))
    b.append(cue_open("s09_c01")+"\n"+"\n".join(inner)+"\n"+cue_close())
    # c2 ImageNet
    x=xs[1]; inner=[rect(x,y0,cw,ch,CARD,rx=18,stroke="#2f4160",sw=1.2)]
    inner.append(rect(x,y0+16,4.5,ch-32,TEAL,rx=2.2))
    inner.append(txt(x+26,y0+44,"ImageNet scale (fine-tuned ResNet-50)",size=19,fill=INK,weight="bold"))
    def vs(px,py,t,a,bv,note):
        g=[txt(px,py,t,size=14,fill=MUTE)]
        g.append(txt(px,py+40,a,size=34,fill=INK,weight="bold",family=MONO))
        g.append(txt(px+150,py+40,"vs "+bv,size=22,fill=FAINT,family=MONO))
        g.append(txt(px+300,py+40,note,size=14,fill=GREEN,weight="bold"))
        return "\n".join(g)
    inner.append(vs(x+26,y0+96,"Misclassification (DAB vs 5-model ensemble)","0.868","0.861","beats ensemble"))
    inner.append(vs(x+26,y0+196,"OOD vs ImageNet-O","0.743","0.642","+0.101 AUROC"))
    inner.append(line(x+26,y0+310,x+cw-26,y0+310,"#2f4160",1))
    inner.append(txt(x+26,y0+346,"Trainable params",size=14,fill=MUTE))
    inner.append(txt(x+26,y0+384,"~36M",size=30,fill=GREEN,weight="bold",family=MONO))
    inner.append(txt(x+160,y0+384,"vs ~118M",size=24,fill=FAINT,family=MONO))
    b.append(cue_open("s09_c02")+"\n"+"\n".join(inner)+"\n"+cue_close())
    add("09_headline-numbers.svg","\n".join(b),"content")

# ======================================================================
# SLIDE 10 — TAKEAWAY (2 chunks)
# ======================================================================
def s10():
    b=[header_band("A unified, distance-aware view","TAKEAWAY")]
    y0=150; ch=300; gap=24; cw=(1152-gap)/2; xs=[64,64+cw+gap]
    b.append(cue_card("s10_c01",xs[0],y0,cw,ch,"Compression buys distance",
        ["Recast uncertainty as compressing training data into",
         "a learned codebook, and a single deterministic network",
         "gains a genuine sense of distance from what it has seen —",
         "matching or beating expensive ensembles at a fraction",
         "of the cost."],accent=COBALT,bsize=17))
    b.append(cue_card("s10_c02",xs[1],y0,cw,ch,"Statistical, not geometric",
        ["Because distance is statistical rather than geometric,",
         "DAB gives a unified, Gaussian-Process-like view of",
         "uncertainty — for both classification and regression —",
         "and can even be attached after the fact to large",
         "pre-trained models."],accent=TEAL,bsize=17))
    # closing strip (non-anchor, ends on a plain element to avoid spillage)
    y=y0+ch+30
    b.append(rect(64,y,1152,70,"#152239",rx=14,stroke="#2f4160",sw=1))
    b.append(txt(90,y+44,"Distance Aware Bottleneck — principled uncertainty in one forward pass.",size=19,fill=INK,weight="bold"))
    b.append(circle(1176,y+35,8,TEAL))
    add("10_takeaway.svg","\n".join(b),"content")

for f in (s01,s02,s03,s04,s05,s06,s07,s08,s09,s10): f()

for fn, svg in SLIDES:
    with open(os.path.join(OUT, fn), "w") as fh:
        fh.write(svg)
print("wrote", len(SLIDES), "slides to", OUT)
for fn,_ in SLIDES: print("  ", fn)
