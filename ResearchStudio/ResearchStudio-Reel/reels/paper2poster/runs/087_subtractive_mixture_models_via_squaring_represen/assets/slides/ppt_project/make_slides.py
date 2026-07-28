#!/usr/bin/env python3
"""All-native SVG deck builder for paper2video run 087 (Subtractive Mixture Models via Squaring).

Reads the visual_anchor_contract.json and emits one <g id="cue_..."> card per contract chunk,
so the strict --require-pptx-anchors cue pass resolves 100% from PPTX geometry. No <image> boxes
anywhere -> the ppt_visuals_too_small gate never applies. Filenames are numeric-prefixed in
narration order so alphabetical sort == narration order == audio order == cue pairing.
"""
import json, math, os

HERE = os.path.dirname(os.path.abspath(__file__))
CONTRACT = os.path.join(HERE, "..", "..", "meta", "visual_anchor_contract.json")
OUT = os.path.join(HERE, "svg_output")
os.makedirs(OUT, exist_ok=True)

C = json.load(open(CONTRACT))
KW = {}   # anchor_id -> "kw kw kw"
for s in C["slides"]:
    for ch in s["chunks"]:
        KW[ch["anchor_id"]] = " ".join(ch.get("cue_keywords", []))

# ---- palette ----
BG="#0e1729"; PANEL="#16223a"; PANEL2="#1b2b47"
INK="#f1f5fb"; MUT="#9fb0c8"; FAINT="#6b7d99"
CYAN="#38bdf8"; GREEN="#34d399"; RED="#fb7185"; AMBER="#fbbf24"; VIO="#a78bfa"
BORD="#2a3c5c"
W,H=1280,720

def esc(t):
    return (t.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;"))

def txt(x,y,s,size=18,fill=INK,weight="normal",anchor="start",spacing=None,style="normal",family=None):
    a=f' text-anchor="{anchor}"' if anchor!="start" else ""
    w=f' font-weight="{weight}"' if weight!="normal" else ""
    st=f' font-style="{style}"' if style!="normal" else ""
    ls=f' letter-spacing="{spacing}"' if spacing else ""
    fam=f' font-family="{family}"' if family else ""
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}"{w}{st}{a}{ls}{fam}>{esc(s)}</text>'

def rect(x,y,w,h,fill,rx=14,stroke=None,sw=1,op=None):
    s=f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    o=f' fill-opacity="{op}"' if op is not None else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}"{o}{s}/>'

def line(x1,y1,x2,y2,stroke,sw=2,dash=None,op=None):
    d=f' stroke-dasharray="{dash}"' if dash else ""
    o=f' stroke-opacity="{op}"' if op is not None else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{sw}"{d}{o}/>'

def circle(cx,cy,r,fill,stroke=None,sw=1,op=None):
    s=f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    o=f' fill-opacity="{op}"' if op is not None else ""
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}"{o}{s}/>'

def polyline(pts,stroke,sw=2.5,fill="none",op=None):
    p=" ".join(f"{x:.1f},{y:.1f}" for x,y in pts)
    o=f' stroke-opacity="{op}"' if op is not None else ""
    return f'<polyline points="{p}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round" stroke-linecap="round"{o}/>'

def polygon(pts,fill,stroke=None,sw=1,op=None):
    p=" ".join(f"{x:.1f},{y:.1f}" for x,y in pts)
    s=f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    o=f' fill-opacity="{op}"' if op is not None else ""
    return f'<polygon points="{p}" fill="{fill}"{o}{s}/>'

def cue(aid, inner, heading=""):
    kw=KW.get(aid, aid)
    return (f'<g id="{aid}" data-cue-label="{esc(kw)}">'
            f'<title>{esc(kw)}</title><desc>{esc(heading+". "+kw if heading else kw)}</desc>'
            f'{inner}</g>')

def gauss(x,mu,sig,amp):
    return amp*math.exp(-((x-mu)**2)/(2*sig*sig))

def curve_pts(fn,x0,x1,ybase,yscale,px0,pw,n=60):
    """Map fn over [x0,x1] to screen; ybase=screen y of value 0, yscale px per unit (up = -)."""
    pts=[]
    for i in range(n+1):
        t=i/n
        xv=x0+t*(x1-x0)
        yv=fn(xv)
        pts.append((px0+t*pw, ybase - yv*yscale))
    return pts

# ---------- shared chrome ----------
def header(kicker, title, accent=CYAN):
    e=[]
    e.append(rect(60,52,6,40,accent,rx=3))
    e.append(txt(80,70,kicker.upper(),size=15,fill=accent,weight="bold",spacing="2.5"))
    e.append(txt(80,102,title,size=30,fill=INK,weight="bold",family="'Segoe UI Semibold','Segoe UI',Arial,sans-serif"))
    return "".join(e)

def footer(n):
    e=[]
    e.append(line(60,690,1220,690,BORD,1,op=0.7))
    e.append(txt(60,708,"Subtractive Mixture Models via Squaring",size=12,fill=FAINT))
    e.append(txt(1220,708,f"{n:02d} / 10",size=12,fill=FAINT,anchor="end"))
    return "".join(e)

def frame(body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">'
            f'<rect width="{W}" height="{H}" fill="{BG}"/>'
            f'<rect x="0" y="0" width="{W}" height="4" fill="{CYAN}" opacity="0.0"/>'
            f'{body}</svg>')

def card_shell(x,y,w,h,accent=None):
    e=rect(x,y,w,h,PANEL,rx=16,stroke=BORD,sw=1.2)
    if accent:
        e+=rect(x,y,5,h,accent,rx=2.5)
    return e

def wrap_lines(lines,x,y0,step=25,size=18,fill=MUT):
    return "".join(txt(x,y0+i*step,ln,size=size,fill=fill) for i,ln in enumerate(lines))

def grid_card(aid,x,y,w,h,accent,heading,lines,badge=None,extra=""):
    inner=card_shell(x,y,w,h,accent)
    hx=x+28
    if badge:
        inner+=circle(x+40,y+42,17,accent,op=0.16)
        inner+=txt(x+40,y+48,badge,size=18,fill=accent,weight="bold",anchor="middle")
        hx=x+70
    inner+=txt(hx,y+48,heading,size=20,fill=INK,weight="bold")
    inner+=wrap_lines(lines,x+28,y+82,step=25,size=17.5,fill=MUT)
    inner+=extra
    return cue(aid,inner,heading)

# ================= SLIDE 01 : TITLE =================
def slide01():
    e=[BG]
    body=[]
    # top-left accent + venue
    body.append(rect(60,60,6,120,CYAN,rx=3))
    body.append(txt(84,86,"ICLR 2024",size=15,fill=CYAN,weight="bold",spacing="3"))
    body.append(txt(84,132,"Subtractive Mixture Models",size=44,fill=INK,weight="bold",family="'Segoe UI Semibold','Segoe UI',Arial,sans-serif"))
    body.append(txt(84,178,"via Squaring: Representation & Learning",size=30,fill=CYAN,weight="bold"))
    body.append(txt(84,210,"Loconte, Sladek, Mengel, Trapp, Solin, Gillis, Vergari",size=16,fill=MUT))
    body.append(txt(84,232,"Univ. of Edinburgh · Aalto · CNRS-CRIL · Univ. de Mons",size=14,fill=FAINT))

    # hero panels (c1 additive / c2 subtractive)
    hy=258; hh=224
    # left additive
    x=60; w=566
    inner=card_shell(x,hy,w,hh,GREEN)
    inner+=txt(x+28,hy+40,"Additive mixture",size=20,fill=INK,weight="bold")
    inner+=txt(x+28,hy+64,"blend simple parts by adding",size=15,fill=MUT)
    # bumpy green curve (all-positive sum of gaussians)
    ax0=x+40; aw=w-80; ybase=hy+188; ys=95
    fn=lambda t: gauss(t,0.22,0.09,0.55)+gauss(t,0.5,0.10,0.7)+gauss(t,0.78,0.08,0.5)
    inner+=line(ax0,ybase,ax0+aw,ybase,BORD,1.5)
    pts=curve_pts(fn,0,1,ybase,ys,ax0,aw)
    fill_pts=[(ax0,ybase)]+pts+[(ax0+aw,ybase)]
    inner+=polygon(fill_pts,GREEN,op=0.16)
    inner+=polyline(pts,GREEN,2.6)
    inner+=txt(x+28,hy+hh-16,"Σ wᵢ cᵢ(x),  wᵢ ≥ 0",size=15,fill=GREEN,family="Consolas,'Courier New',monospace")
    body.append(cue("cue_s01_c1_mixture_models_usually_blend_simple",inner,"Additive mixture blends by adding"))
    # right subtractive
    x=654
    inner=card_shell(x,hy,w,hh,RED)
    inner+=txt(x+28,hy+40,"Subtractive mixture",size=20,fill=INK,weight="bold")
    inner+=txt(x+28,hy+64,"cancel mass to carve a hole",size=15,fill=MUT)
    ax0=x+40; ybase=hy+188; ys=110
    fn2=lambda t: max(0.0, gauss(t,0.5,0.26,0.95)-gauss(t,0.5,0.085,0.85))
    inner+=line(ax0,ybase,ax0+aw,ybase,BORD,1.5)
    pts=curve_pts(fn2,0,1,ybase,ys,ax0,aw)
    fill_pts=[(ax0,ybase)]+pts+[(ax0+aw,ybase)]
    inner+=polygon(fill_pts,RED,op=0.16)
    inner+=polyline(pts,RED,2.6)
    # a downward arrow marking the hole
    hx=ax0+aw*0.5
    inner+=line(hx,hy+92,hx,ybase-6,AMBER,1.6,dash="4 4")
    inner+=txt(hx,hy+86,"hole",size=13,fill=AMBER,anchor="middle")
    inner+=txt(x+28,hy+hh-16,"allow  wᵢ < 0  →  fewer components",size=15,fill=RED,family="Consolas,'Courier New',monospace")
    body.append(cue("cue_s01_c2_but_what_mixture_could_also",inner,"What if a mixture could subtract mass"))

    # bottom chips (c3 / c4)
    cy=502; ch=150
    x=60; w=566
    inner=card_shell(x,cy,w,ch,CYAN)
    inner+=txt(x+28,cy+42,"The idea",size=18,fill=CYAN,weight="bold")
    inner+=wrap_lines(["Learn deep subtractive mixtures by","squaring a signed tensorized","probabilistic circuit."],x+28,cy+74,step=24,size=17.5,fill=MUT)
    body.append(cue("cue_s01_c3_published_iclr_2024_shows_how",inner,"Published ICLR 2024 learn deep subtractive by squaring"))
    x=654
    inner=card_shell(x,cy,w,ch,VIO)
    inner+=txt(x+28,cy+42,"Why it matters",size=18,fill=VIO,weight="bold")
    inner+=wrap_lines(["Squaring keeps a valid density with","negative parameters — and is provably,","exponentially more compact."],x+28,cy+74,step=24,size=17.5,fill=MUT)
    body.append(cue("cue_s01_c4_squaring_keeps_valid_distribution_wh",inner,"Squaring keeps valid distribution negative parameters authors prove"))

    body.append(footer(1))
    return frame("".join(body))

# ================= SLIDE 02 : PROBLEM =================
def slide02():
    b=[header("Problem","Additive mixtures are wasteful on holey densities",RED)]
    # c1
    def hole_target(x,y,w,h):
        ax0=x+30; aw=w-60; ybase=y+h-42; ys=88
        fn=lambda t: max(0.0, gauss(t,0.5,0.30,0.95)-gauss(t,0.5,0.09,0.9))
        s=line(ax0,ybase,ax0+aw,ybase,BORD,1.4)
        pts=curve_pts(fn,0,1,ybase,ys,ax0,aw)
        s+=polygon([(ax0,ybase)]+pts+[(ax0+aw,ybase)],RED,op=0.15)
        s+=polyline(pts,RED,2.4)
        s+=txt(x+30,y+h-14,"target density has a gap",size=13,fill=FAINT)
        return s
    b.append(grid_card("cue_s02_c1_traditional_mixture_models_build_com",60,170,566,248,CYAN,
        "Convex, additive blend",
        ["Classical mixtures build complex","densities by adding simple","components — a convex combination.","Simple, but often wildly inefficient."]))
    b.append(grid_card("cue_s02_c2_target_distribution_gaps_holes_its",654,170,566,248,RED,
        "Holes cost many components",
        ["To carve a gap, an additive mixture","must stack up many bumps around it."],
        extra=hole_target(654,300,566,116)))
    b.append(grid_card("cue_s02_c3_natural_fix_let_some_components",60,438,566,248,GREEN,
        "The natural fix: subtract",
        ["Let some components subtract","probability mass instead of only","adding it — cancel where the","density should be low."]))
    def dip(x,y,w,h):
        ax0=x+30; aw=w-60; ybase=y+56; ys=44
        fn=lambda t: gauss(t,0.35,0.12,0.7)-gauss(t,0.7,0.12,1.05)
        s=line(ax0,ybase,ax0+aw,ybase,BORD,1.4,dash="5 4")
        s+=txt(ax0+aw+2,ybase+4,"0",size=12,fill=FAINT)
        pts=curve_pts(fn,0,1,ybase,ys,ax0,aw)
        s+=polyline(pts,AMBER,2.4)
        return s
    b.append(grid_card("cue_s02_c4_catch_once_you_allow_subtraction",654,438,566,248,AMBER,
        "The catch",
        ["Subtraction can push the function","below zero — no longer a valid","distribution — and learning it","becomes genuinely hard."],
        extra=dip(654,560,566,120)))
    return frame("".join(b))

# ================= SLIDE 03 : MOTIVATION =================
def slide03():
    b=[header("Motivation","Subtraction pays off — but non-negativity is the obstacle",VIO)]
    b.append(grid_card("cue_s03_c1_why_revisit_now_because_subtraction",60,170,566,248,GREEN,
        "Subtraction pays off",
        ["A mixture that can cancel mass","captures complex shapes with","far fewer components than a","purely additive one."]))
    b.append(grid_card("cue_s03_c2_problem_guaranteeing_result_stays_no",654,170,566,248,RED,
        "The obstacle",
        ["The hard part is guaranteeing the","resulting function stays","non-negative everywhere — a valid","probability density."]))
    b.append(grid_card("cue_s03_c3_energy_based_models_enforce_non_nega",60,438,566,248,AMBER,
        "Energy-based detour",
        ["Energy-based models enforce","non-negativity by exponentiation —","but then lose the ability to","normalize the model tractably."]))
    # c4: three community chips
    x=654;y=438;w=566;h=248
    inner=card_shell(x,y,w,h,CYAN)
    inner+=txt(x+28,y+44,"Reinvented in many fields",size=20,fill=INK,weight="bold")
    inner+=wrap_lines(["Several communities each rediscovered","a squaring trick — with no shared,","tractable framework tying them together."],x+28,y+78,step=24,size=17,fill=MUT)
    chips=[("Signal processing",GREEN),("Kernel methods",CYAN),("Quantum / Born",VIO)]
    cyc=y+164
    for i,(nm,cl) in enumerate(chips):
        cx=x+28+i*178
        inner+=rect(cx,cyc,166,52,PANEL2,rx=10,stroke=cl,sw=1.3)
        inner+=circle(cx+22,cyc+26,7,cl)
        inner+=txt(cx+38,cyc+31,nm,size=13.5,fill=INK,weight="bold")
    b.append(cue("cue_s03_c4_meanwhile_several_separate_communiti",inner,"Meanwhile several separate communities rediscovered squaring"))
    return frame("".join(b))

# ================= SLIDE 04 : CONTRIBUTION =================
def slide04():
    b=[header("Contribution","Four contributions",CYAN)]
    data=[
        ("cue_s04_c1_work_makes_four_contributions_first","1",CYAN,"General framework",
            ["Represent subtractive mixtures by","squaring, in the language of","tensorized probabilistic circuits","(NPC²s)."]),
        ("cue_s04_c2_second_shows_these_squared_non_monot","2",VIO,"A unifying view",
            ["Squared non-monotonic circuits","generalize √-of-density models,","PSD kernel models, and quantum","Born machines."]),
        ("cue_s04_c3_third_proves_exponential_lower_bound","3",AMBER,"Exponential separation",
            ["A function a single squared circuit","encodes compactly needs","exponentially more units in any","monotonic circuit."]),
        ("cue_s04_c4_fourth_backs_experiments_real_world","4",GREEN,"Broad empirical evidence",
            ["Validated on continuous, discrete,","UCI multivariate data, and","language-model distillation."]),
    ]
    pos=[(60,170),(654,170),(60,438),(654,438)]
    for (aid,badge,cl,head,lines),(x,y) in zip(data,pos):
        b.append(grid_card(aid,x,y,566,248,cl,head,lines,badge=badge))
    return frame("".join(b))

# ================= SLIDE 05 : METHOD =================
def slide05():
    b=[header("Method","Square a signed mixture — then go deep, layer by layer",GREEN)]
    mono="Consolas,'Courier New',monospace"
    # c1
    x,y=60,170
    inner=card_shell(x,y,566,248,GREEN)
    inner+=txt(x+28,y+44,"Square a signed mixture",size=20,fill=INK,weight="bold")
    inner+=wrap_lines(["Unconstrained real weights let","components be negative; squaring","forces the output non-negative for","any weights."],x+28,y+78,step=23,size=16.5,fill=MUT)
    inner+=rect(x+28,y+186,510,44,PANEL2,rx=10,stroke=BORD,sw=1)
    inner+=txt(x+44,y+214,"c²(x) = (Σ wᵢ cᵢ(x))²  ≥ 0 ,  wᵢ ∈ ℝ",size=17,fill=GREEN,family=mono)
    b.append(cue("cue_s05_c1_core_idea_take_mixture_unconstrained",inner,"Core idea take mixture unconstrained real weights negative"))
    # c2
    x,y=654,170
    inner=card_shell(x,y,566,248,CYAN)
    inner+=txt(x+28,y+44,"Expand the square",size=20,fill=INK,weight="bold")
    inner+=wrap_lines(["A K-component mixture becomes a","sum over all pairs — a product of","experts whose normalizer Z has a","closed form for many families."],x+28,y+78,step=23,size=16.5,fill=MUT)
    inner+=rect(x+28,y+186,510,44,PANEL2,rx=10,stroke=BORD,sw=1)
    inner+=txt(x+44,y+214,"Σᵢ Σⱼ wᵢ wⱼ cᵢ(x) cⱼ(x)  /  Z",size=17,fill=CYAN,family=mono)
    b.append(cue("cue_s05_c2_expanding_square_turns_k_component_m",inner,"Expanding square turns k-component mixture sum over all pairs"))
    # c3 : go deep - layer chain
    x,y=60,438
    inner=card_shell(x,y,566,248,VIO)
    inner+=txt(x+28,y+44,"Go deep: square each layer",size=20,fill=INK,weight="bold")
    inner+=wrap_lines(["Recursively square a tensorized,","structured-decomposable circuit","layer by layer."],x+28,y+78,step=23,size=16.5,fill=MUT)
    lx=x+34; ly=y+184
    labels=["input","⊗ prod","Σ sum","( · )²"]
    cols=[CYAN,GREEN,AMBER,VIO]
    for i,(lb,cl) in enumerate(zip(labels,cols)):
        bx=lx+i*128
        inner+=rect(bx,ly,104,44,PANEL2,rx=9,stroke=cl,sw=1.4)
        inner+=txt(bx+52,ly+28,lb,size=14,fill=cl,anchor="middle",weight="bold")
        if i<3:
            inner+=line(bx+104,ly+22,bx+128,ly+22,FAINT,2)
            inner+=polygon([(bx+128,ly+22),(bx+121,ly+18),(bx+121,ly+26)],FAINT)
    b.append(cue("cue_s05_c3_deep_authors_square_tensorized_struc",inner,"Deep authors square tensorized structured-decomposable circuit layer"))
    # c4
    x,y=654,438
    inner=card_shell(x,y,566,248,AMBER)
    inner+=txt(x+28,y+44,"Still tractable",size=20,fill=INK,weight="bold")
    inner+=wrap_lines(["Each squared layer holds a quadratic","number of units but still outputs a","vector — so the model trains with","gradient descent, computing Z once","per batch."],x+28,y+78,step=23,size=16.5,fill=MUT)
    inner+=txt(x+28,y+222,"K units  →  O(K²) units , vector output",size=14.5,fill=AMBER,family=mono)
    b.append(cue("cue_s05_c4_squared_layer_holds_quadratic_number",inner,"Squared layer holds quadratic number units still outputs vector"))
    return frame("".join(b))

# ================= SLIDE 06 : DATASET / BENCHMARK =================
def slide06():
    b=[header("Dataset / Benchmark","Three regimes, strong baselines",CYAN)]
    # c1
    b.append(grid_card("cue_s06_c1_experiments_cover_three_regimes",60,170,566,248,CYAN,
        "Three evaluation regimes",
        ["Synthetic 2D densities, real UCI","multivariate data, and","language-model distillation — from","the visible to the high-dimensional."]))
    # c2 : 2D rings mini
    x,y=654,170
    inner=card_shell(x,y,566,248,VIO)
    inner+=txt(x+28,y+44,"① 2D synthetic densities",size=20,fill=INK,weight="bold")
    inner+=wrap_lines(["Continuous & discrete — rings and","other holey shapes you can see."],x+28,y+78,step=23,size=16.5,fill=MUT)
    cy0=y+180
    for i,cx in enumerate([x+120,x+300,x+480]):
        inner+=circle(cx,cy0,42,VIO,op=0.13,stroke=VIO,sw=1.4)
        inner+=circle(cx,cy0,20,PANEL,stroke=VIO,sw=1.2)
    inner+=txt(x+300,y+240,"ring densities (holes)",size=13,fill=FAINT,anchor="middle")
    b.append(cue("cue_s06_c2_first_two_dimensional_synthetic_dens",inner,"First two-dimensional synthetic densities continuous discrete rings"))
    # c3 : UCI datasets chips
    x,y=60,438
    inner=card_shell(x,y,566,248,GREEN)
    inner+=txt(x+28,y+44,"② Five UCI datasets",size=20,fill=INK,weight="bold")
    names=["Power","Gas","Hepmass","MiniBooNE","BSDS300"]
    for i,nm in enumerate(names):
        r=i//3; c=i%3
        cx=x+28+c*176; cy=y+80+r*66
        inner+=rect(cx,cy,164,52,PANEL2,rx=10,stroke=BORD,sw=1)
        inner+=txt(cx+82,cy+31,nm,size=15,fill=INK,anchor="middle",weight="bold")
    b.append(cue("cue_s06_c3_second_five_standard_uci_datasets",inner,"Second five standard UCI datasets Power Gas Hepmass MiniBooNE"))
    # c4 : baselines + gpt2
    x,y=654,438
    inner=card_shell(x,y,566,248,AMBER)
    inner+=txt(x+28,y+44,"③ GPT2 distillation + baselines",size=20,fill=INK,weight="bold")
    inner+=wrap_lines(["Approximate sentences sampled from","GPT2. Baselines:"],x+28,y+78,step=23,size=16.5,fill=MUT)
    bl=["Gaussian","RealNVP","MADE","MAF","NSF","Monotonic PC","TTDE"]
    xx=x+28; yy=y+134
    for nm in bl:
        wd=12+len(nm)*8.3
        if xx+wd> x+540: xx=x+28; yy+=42
        inner+=rect(xx,yy,wd,32,PANEL2,rx=8,stroke=BORD,sw=1)
        inner+=txt(xx+wd/2,yy+21,nm,size=13,fill=MUT,anchor="middle")
        xx+=wd+10
    b.append(cue("cue_s06_c4_baselines_span_full_covariance_gauss",inner,"Baselines span full-covariance Gaussians flows monotonic circuits TTDE"))
    return frame("".join(b))

# ================= SLIDE 07 : KEY RESULT =================
def slide07():
    b=[header("Key Result","Same size, higher likelihood — negatives carve the holes",GREEN)]
    # three columns
    x0,x1,x2=60,453,846; w=373; y=170; h=500
    # c1 : scatter above diagonal
    inner=card_shell(x0,y,w,h,GREEN)
    inner+=txt(x0+24,y+42,"NPC² beats MPC",size=19,fill=INK,weight="bold")
    inner+=txt(x0+24,y+66,"at parity of model size",size=14,fill=MUT)
    px,py,pw,ph=x0+52,y+96,280,300
    inner+=rect(px,py,pw,ph,PANEL2,rx=10,stroke=BORD,sw=1)
    inner+=line(px,py+ph,px+pw,py,FAINT,1.6,dash="5 4")
    inner+=txt(px+pw-6,py+ph-8,"MPC LL",size=11,fill=FAINT,anchor="end")
    inner+=txt(px+8,py+16,"NPC² LL",size=11,fill=FAINT)
    dots=[(0.30,0.55),(0.42,0.70),(0.55,0.78),(0.66,0.86),(0.50,0.64),(0.74,0.90),(0.38,0.60)]
    for dx,dy in dots:
        inner+=circle(px+dx*pw, py+ph-dy*ph, 6, GREEN, op=0.9)
    inner+=txt(x0+24,y+h-24,"points above diagonal → NPC² wins",size=12.5,fill=GREEN)
    b.append(cue("cue_s07_c1_headline_finding_consistent_same_siz",inner,"Headline finding consistent same size squared circuits reach higher"))
    # c2 : rings MPC vs NPC2
    inner=card_shell(x1,y,w,h,VIO)
    inner+=txt(x1+24,y+42,"2D rings",size=19,fill=INK,weight="bold")
    inner+=txt(x1+24,y+66,"negatives carve the hole",size=14,fill=MUT)
    cxm=x1+w/2
    # MPC : blob, no hole
    inner+=txt(cxm,y+108,"MPC²  (no negatives)",size=13,fill=MUT,anchor="middle")
    inner+=circle(cxm,y+180,54,RED,op=0.18,stroke=RED,sw=1.4)
    inner+=circle(cxm,y+180,26,RED,op=0.14)
    inner+=txt(cxm,y+250,"hole filled in",size=12,fill=RED,anchor="middle")
    # NPC2 : clean annulus
    inner+=txt(cxm,y+300,"NPC²  (negatives)",size=13,fill=MUT,anchor="middle")
    inner+=circle(cxm,y+372,54,GREEN,op=0.20,stroke=GREEN,sw=1.6)
    inner+=circle(cxm,y+372,26,PANEL,stroke=GREEN,sw=1.4)
    inner+=txt(cxm,y+h-24,"clean ring: hole carved",size=12.5,fill=GREEN,anchor="middle")
    b.append(cue("cue_s07_c2_two_dimensional_ring_distributions_p",inner,"Two-dimensional ring distributions plain squaring helps negative parameters"))
    # c3 : gpt2 line chart toward -52
    inner=card_shell(x2,y,w,h,CYAN)
    inner+=txt(x2+24,y+42,"GPT2 distillation",size=19,fill=INK,weight="bold")
    inner+=txt(x2+24,y+66,"scaling toward GPT2's LL",size=14,fill=MUT)
    px,py,pw,ph=x2+52,y+100,286,290
    inner+=rect(px,py,pw,ph,PANEL2,rx=10,stroke=BORD,sw=1)
    # target line -52 near top
    ty=py+40
    inner+=line(px,ty,px+pw,ty,AMBER,1.6,dash="6 4")
    inner+=txt(px+pw-6,ty-6,"GPT2 ≈ −52",size=12,fill=AMBER,anchor="end")
    # NPC2 rising
    npc=[(px+10,py+ph-30),(px+80,py+ph-90),(px+160,py+ph-150),(px+230,py+ph-190),(px+pw-8,ty+14)]
    inner+=polyline(npc,GREEN,3)
    inner+=circle(npc[-1][0],npc[-1][1],5,GREEN)
    inner+=txt(px+18,py+ph-40,"NPC²",size=13,fill=GREEN,weight="bold")
    # MPC plateau
    mpc=[(px+10,py+ph-24),(px+90,py+ph-60),(px+180,py+ph-78),(px+260,py+ph-84),(px+pw-8,py+ph-86)]
    inner+=polyline(mpc,RED,2.6)
    inner+=txt(px+pw-12,py+ph-96,"MPC",size=13,fill=RED,anchor="end",weight="bold")
    inner+=txt(px+8,py+ph+22,"larger K  →",size=12,fill=FAINT)
    b.append(cue("cue_s07_c3_gpt2_distillation_task_squared_circu",inner,"GPT2 distillation task squared circuits scale better closer GPT2"))
    return frame("".join(b))

# ================= SLIDE 08 : ABLATION =================
def slide08():
    b=[header("Ablation Study","Isolating what actually helps",VIO)]
    b.append(grid_card("cue_s08_c1_confirm_gains_come_subtraction_not",60,170,566,248,CYAN,
        "Subtraction vs squaring alone",
        ["Compare against squared monotonic","circuits (MPC²): they square but keep","all parameters non-negative — so","only subtraction is removed."]))
    # c2 : bars MPC2 vs NPC2
    x,y=654,170
    inner=card_shell(x,y,566,248,GREEN)
    inner+=txt(x+28,y+44,"Negatives do the real work",size=20,fill=INK,weight="bold")
    inner+=txt(x+28,y+72,"NPC² still wins over MPC²",size=15,fill=MUT)
    bx=x+70; by=y+210; bw=90
    inner+=line(bx-16,by,x+520,by,BORD,1.4)
    inner+=rect(bx,by-70,bw,70,RED,rx=6,op=0.85)
    inner+=txt(bx+bw/2,by-78,"MPC²",size=13,fill=RED,anchor="middle")
    inner+=txt(bx+bw/2,by+20,"squaring only",size=12,fill=FAINT,anchor="middle")
    inner+=rect(bx+230,by-118,bw,118,GREEN,rx=6,op=0.9)
    inner+=txt(bx+230+bw/2,by-126,"NPC²",size=13,fill=GREEN,anchor="middle")
    inner+=txt(bx+230+bw/2,by+20,"+ negatives",size=12,fill=FAINT,anchor="middle")
    inner+=txt(x+520,by-118,"higher LL",size=12,fill=GREEN,anchor="end")
    b.append(cue("cue_s08_c2_squared_non_monotonic_circuits_still",inner,"Squared non-monotonic circuits still win negative parameters real work"))
    b.append(grid_card("cue_s08_c3_two_other_patterns_emerge_binary_tre",60,438,566,248,AMBER,
        "Structure & input layers",
        ["Binary-tree region graphs generally","beat linear-tree ones; splines help","most on continuous data, embeddings","on discrete data."]))
    b.append(grid_card("cue_s08_c4_some_discrete_image_mass_tasks_advan",654,438,566,248,RED,
        "Where the gap narrows",
        ["On some discrete image-mass tasks,","where inputs are already expressive,","the advantage of subtraction","narrows."]))
    return frame("".join(b))

# ================= SLIDE 09 : HEADLINE NUMBERS =================
def slide09():
    b=[header("Headline Numbers","The compactness gap, in numbers",AMBER)]
    # c1 : a few numbers (framing KPI)
    x,y=60,170
    inner=card_shell(x,y,566,248,CYAN)
    inner+=txt(x+28,y+46,"A few numbers make the point",size=20,fill=INK,weight="bold")
    inner+=wrap_lines(["Two levers of the result: a combinatorial","blow-up in expressiveness at fixed","parameter cost, and best-in-class","test likelihoods among tractable models."],x+28,y+84,step=25,size=16.5,fill=MUT)
    b.append(cue("cue_s09_c1_few_numbers_make_point",inner,"A few numbers make the point"))
    # c2 : K^2/2 KPI
    x,y=654,170
    inner=card_shell(x,y,566,248,VIO)
    inner+=txt(x+28,y+46,"Compactness from squaring",size=20,fill=INK,weight="bold")
    inner+=txt(x+28,y+120,"K",size=54,fill=INK,weight="bold")
    inner+=txt(x+92,y+120,"components  →",size=20,fill=MUT)
    inner+=txt(x+300,y+120,"~ K²⁄2",size=48,fill=VIO,weight="bold",family="Consolas,'Courier New',monospace")
    inner+=wrap_lines(["pairwise components reusing the same K","parameters — an exponential gap over","monotonic circuits."],x+28,y+160,step=24,size=16,fill=MUT)
    b.append(cue("cue_s09_c2_squaring_mixture_components_encodes",inner,"Squaring mixture components encodes K squared pairwise same parameters"))
    # c3 : UCI number tiles
    x,y=60,438
    inner=card_shell(x,y,566,248,GREEN)
    inner+=txt(x+28,y+44,"Best test log-likelihood (tractable)",size=19,fill=INK,weight="bold")
    tiles=[("Power","0.62"),("Gas","10.98"),("Hepmass","−20.41"),("MiniBooNE","−26.68")]
    for i,(nm,val) in enumerate(tiles):
        c=i%4
        cx=x+28+c*132; cy=y+78
        inner+=rect(cx,cy,120,120,PANEL2,rx=12,stroke=BORD,sw=1)
        inner+=txt(cx+60,cy+30,nm,size=13,fill=MUT,anchor="middle")
        inner+=txt(cx+60,cy+78,val,size=24,fill=GREEN,anchor="middle",weight="bold")
    inner+=txt(x+28,y+228,"NPC² — best among tractable models on several UCI sets",size=13,fill=FAINT)
    b.append(cue("cue_s09_c3_empirically_squared_non_monotonic_ci",inner,"Empirically squared non-monotonic circuits best test log-likelihoods UCI"))
    # c4 : gpt2 approach -52 sparkline
    x,y=654,438
    inner=card_shell(x,y,566,248,AMBER)
    inner+=txt(x+28,y+44,"On GPT2-sampled data",size=20,fill=INK,weight="bold")
    inner+=wrap_lines(["NPC² climbs toward GPT2's own","likelihood while monotonic PCs plateau."],x+28,y+78,step=24,size=16.5,fill=MUT)
    px,py,pw,ph=x+34,y+140,504,80
    ty=py+10
    inner+=line(px,ty,px+pw,ty,AMBER,1.5,dash="6 4")
    inner+=txt(px+pw,ty-6,"GPT2 ≈ −52",size=12,fill=AMBER,anchor="end")
    inner+=polyline([(px,py+ph),(px+120,py+ph-30),(px+250,py+ph-56),(px+380,py+ph-70),(px+pw,ty+8)],GREEN,3)
    inner+=polyline([(px,py+ph-4),(px+140,py+ph-28),(px+300,py+ph-36),(px+pw,py+ph-38)],RED,2.4)
    inner+=txt(px+8,py+ph-46,"NPC²",size=12,fill=GREEN,weight="bold")
    inner+=txt(px+pw,py+ph-30,"MPC",size=12,fill=RED,anchor="end",weight="bold")
    b.append(cue("cue_s09_c4_language_they_climb_toward_gpt2",inner,"Language they climb toward GPT2 likelihood monotonic plateau"))
    return frame("".join(b))

# ================= SLIDE 10 : TAKEAWAY =================
def slide10():
    b=[BG]
    body=[]
    body.append(rect(60,52,6,40,GREEN,rx=3))
    body.append(txt(80,70,"TAKEAWAY",size=15,fill=GREEN,weight="bold",spacing="2.5"))
    body.append(txt(80,102,"Squaring makes subtraction a first-class tool",size=30,fill=INK,weight="bold",family="'Segoe UI Semibold','Segoe UI',Arial,sans-serif"))
    # c1 kicker chip
    inner=rect(60,150,566,60,PANEL,rx=14,stroke=GREEN,sw=1.3)
    inner+=circle(96,180,10,GREEN,op=0.9)
    inner+=txt(120,187,"The takeaway is simple",size=19,fill=INK,weight="bold")
    body.append(cue("cue_s10_c1_takeaway_simple",inner,"The takeaway is simple"))
    # c2 main statement (wide)
    x,y=60,238;w=1160;h=180
    inner=card_shell(x,y,w,h,CYAN)
    inner+=txt(x+34,y+52,"Valid, tractable, exponentially compact",size=24,fill=CYAN,weight="bold")
    inner+=wrap_lines(["Squaring turns subtractive mixtures into valid, tractable probabilistic models that need","exponentially fewer components than additive mixtures to reach the same expressiveness."],x+34,y+96,step=32,size=19,fill=INK)
    body.append(cue("cue_s10_c2_squaring_turns_subtractive_mixtures",inner,"Squaring turns subtractive mixtures valid tractable exponentially fewer"))
    # c3 unify (wide)
    x,y=60,440;w=1160;h=176
    inner=card_shell(x,y,w,h,VIO)
    inner+=txt(x+34,y+50,"One framework, many models",size=22,fill=VIO,weight="bold")
    inner+=txt(x+34,y+86,"Unifies √-of-density models · PSD kernel models · quantum Born machines",size=18,fill=MUT)
    for i,(nm,cl) in enumerate([("√-of-density",GREEN),("PSD kernels",CYAN),("Born machines",AMBER)]):
        cx=x+34+i*300; cy=y+110
        inner+=rect(cx,cy,268,44,PANEL2,rx=10,stroke=cl,sw=1.3)
        inner+=circle(cx+24,cy+22,7,cl)
        inner+=txt(cx+42,cy+28,nm,size=15,fill=INK,weight="bold")
    body.append(cue("cue_s10_c3_along_way_one_framework_unifies",inner,"Along way one framework unifies square-root density PSD Born"))
    body.append(footer(10))
    return frame("".join(body))

SLIDES=[("01_title",slide01),("02_problem",slide02),("03_motivation",slide03),
        ("04_contribution",slide04),("05_method",slide05),("06_dataset_benchmark",slide06),
        ("07_key_result",slide07),("08_ablation",slide08),("09_headline_numbers",slide09),
        ("10_takeaway",slide10)]

for name,fn in SLIDES:
    svg=fn()
    with open(os.path.join(OUT,name+".svg"),"w") as f:
        f.write(svg)
    print("wrote",name, len(svg),"bytes")
print("DONE")
