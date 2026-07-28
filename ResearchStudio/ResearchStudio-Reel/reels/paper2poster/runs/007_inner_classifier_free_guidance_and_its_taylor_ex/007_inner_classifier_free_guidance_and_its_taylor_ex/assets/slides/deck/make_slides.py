#!/usr/bin/env python3
"""All-native SVG deck builder for paper2video run 007
(Inner Classifier-Free Guidance and Its Taylor Expansion for Diffusion Models -
ICLR 2024, Tsinghua University / USTC / Huawei).
Reads _anchor_map.json; wraps each narration chunk in its own <g id="cue_...">
card with a <title> holding the cue keywords, so the strict
--require-pptx-anchors cue pass resolves every anchor from PPTX geometry.
Zero <image>, zero gradients, ASCII mono equations only.
Theme motif: a Taylor expansion around beta = 1 - the straight tangent is
classifier-free guidance (first order), the curve's extra bend is the new
second-order inner-CFG term, gained for free from the pretrained model."""
import json, os, math

HERE = os.path.dirname(os.path.abspath(__file__))
META = os.environ["VIDEO_META"]
OUT  = os.path.join(HERE, "svg_output")
os.makedirs(OUT, exist_ok=True)
AM = json.load(open(os.path.join(META, "_anchor_map.json")))

W, H = 1280, 720
BG="#0C1024"; PANEL="#161A38"; PANEL2="#1E2450"; STROKE="#343A70"
ACCENT="#9B8CFF"; TEAL="#33D6C0"; GOLD="#F4C24C"; RED="#F2685C"; GREEN="#46C98B"
TEXT="#EAF0FB"; SEC="#A5AECF"; TER="#727BA0"; WHITE="#FFFFFF"
SANS="Arial, 'Helvetica Neue', Helvetica, sans-serif"
MONO="'DejaVu Sans Mono', Consolas, monospace"
INKG="#0E1330"  # inner glyph panel

def esc(s):
    return (str(s).replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")
            .replace('"',"&quot;"))

def T(x,y,s,size,fill=TEXT,weight="400",anchor="start",ff=SANS,ls=None,opacity=None):
    a=f' letter-spacing="{ls}"' if ls is not None else ""
    o=f' opacity="{opacity}"' if opacity is not None else ""
    return (f'<text x="{x}" y="{y}" font-family="{ff}" font-size="{size}" '
            f'fill="{fill}" font-weight="{weight}" text-anchor="{anchor}"{a}{o}>{esc(s)}</text>')

def rect(x,y,w,h,fill=PANEL,stroke=None,rx=14,sw=1.5,opacity=None):
    st=f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    o=f' opacity="{opacity}"' if opacity is not None else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}"{st}{o}/>'

def line(x1,y1,x2,y2,stroke=STROKE,sw=1.5,dash=None,cap="round"):
    d=f' stroke-dasharray="{dash}"' if dash else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{sw}" stroke-linecap="{cap}"{d}/>'

def circle(cx,cy,r,fill=ACCENT,stroke=None,sw=1.5,opacity=None):
    st=f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    o=f' opacity="{opacity}"' if opacity is not None else ""
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}"{st}{o}/>'

def poly(pts,fill="none",stroke=ACCENT,sw=2.5,dash=None):
    d=f' stroke-dasharray="{dash}"' if dash else ""
    p=" ".join(f"{x},{y}" for x,y in pts)
    return f'<polyline points="{p}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"{d}/>'

def wrap(text,maxc):
    words=text.split(); lines=[]; cur=""
    for w in words:
        if len(cur)+len(w)+1<=maxc: cur=(cur+" "+w).strip()
        else: lines.append(cur); cur=w
    if cur: lines.append(cur)
    return lines

def para(x,y,text,size,fill,maxc,lh,weight="400"):
    ls=wrap(text,maxc); out=[T(x,y+i*lh,l,size,fill,weight) for i,l in enumerate(ls)]
    return "".join(out), y+len(ls)*lh

def anchor(aid,kw,body):
    return f'<g id="{aid}"><title>{esc(" ".join(kw))}</title>{body}</g>'

def eyebrow(label):
    return (rect(64,52,5,26,fill=ACCENT,rx=2,sw=0)+
            T(82,72,label.upper(),15,SEC,"700",ls="2.5"))

def header(label,title,tsize=30):
    return eyebrow(label)+T(64,110,title,tsize,TEXT,"800")

def chunks(slide_id):
    return AM[slide_id]["chunks"]

def svg(body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
            f'width="{W}" height="{H}" font-family="{SANS}">'
            f'<rect x="0" y="0" width="{W}" height="{H}" fill="{BG}"/>'
            f'{body}</svg>')

def stat(x,y,w,h,num,lbl,col):
    ns=min(30,h*0.34)
    return (rect(x,y,w,h,fill=PANEL2,stroke=STROKE,rx=12)+
            T(x+w/2,y+h*0.52,num,ns,col,"800",anchor="middle")+
            T(x+w/2,y+h*0.80,lbl,12.5,SEC,"600",anchor="middle"))

def chip(x,y,text,col,w=512,h=34):
    return (rect(x,y,w,h,fill=PANEL2,stroke=STROKE,rx=8)+
            circle(x+18,y+h/2,5,fill=col)+
            T(x+34,y+h/2+6,text,14.5,TEXT,"600"))

def eqbox(x,y,w,expr,size=17,h=44):
    return (rect(x,y,w,h,fill=PANEL2,stroke=STROKE,rx=8)+
            T(x+w/2,y+h/2+6,expr,size,TEXT,"800",anchor="middle",ff=MONO))

# ---- theme glyphs -------------------------------------------------------
def taylorfig(cx,cy,scale=1.0):
    """Taylor expansion of the guided score around beta = 1. The dashed straight
    tangent is classifier-free guidance (first order); the extra curvature the
    solid line adds is the new second-order inner-CFG term."""
    AW=182*scale; CH=94*scale
    ax0=cx-AW/2; ay0=cy+CH/2
    out=line(ax0,ay0,ax0+AW,ay0,STROKE,1.4)
    out+=line(ax0,ay0,ax0,ay0-CH,STROKE,1.4)
    def f(t): return 0.16+0.76*t*t
    def X(t): return ax0+t*AW
    def Y(v): return ay0-CH*v
    curve=[(X(t/24),Y(f(t/24))) for t in range(25)]
    out+=poly(curve,stroke=ACCENT,sw=2.8)
    b=0.5; fb=f(b); fp=1.52*b
    def g(t): return fb+fp*(t-b)
    out+=line(X(0.10),Y(g(0.10)),X(0.98),Y(g(0.98)),GOLD,1.8,dash="6 4")
    out+=circle(X(b),Y(fb),4.6,fill=GOLD)
    tg=0.9
    out+=line(X(tg),Y(g(tg)),X(tg),Y(f(tg)),TEAL,2.2)
    out+=T(X(tg)+7,(Y(g(tg))+Y(f(tg)))/2+4,"2nd",int(10.5*scale),TEAL,"800")
    out+=T(X(0.12),Y(g(0.12))-8,"CFG (1st order)",int(10.5*scale),GOLD,"800")
    out+=T(X(0.30),Y(f(0.9))+2,"ICFG",int(11*scale),ACCENT,"800")
    out+=T(ax0+AW,ay0+14,"beta",int(9.5*scale),TER,"700",anchor="end")
    return out

def labelbox(x,y,w,h):
    """CFG sees the condition only as an opaque label - the continuous
    structure of the condition space is thrown away."""
    out=rect(x,y,w,h,fill=INKG,stroke=STROKE,rx=8)
    cy=y+h/2
    out+=circle(x+30,cy,7,fill=TEAL)
    out+=T(x+30,cy-16,"condition c",10,TEAL,"800",anchor="middle")
    out+=line(x+44,cy,x+w*0.44,cy,SEC,2.0)
    out+=poly([(x+w*0.44-8,cy-5),(x+w*0.44,cy),(x+w*0.44-8,cy+5)],fill=SEC,stroke=SEC,sw=1)
    out+=rect(x+w*0.48,cy-18,w*0.32,36,fill=PANEL2,stroke=RED,rx=6,sw=1.4)
    out+=T(x+w*0.48+w*0.16,cy+5,"[ label ]",11,RED,"800",anchor="middle",ff=MONO)
    out+=T(x+w-12,cy+31,"structure ignored",9.5,GOLD,"700",anchor="end")
    return out

def condmanifold(x,y,w,h):
    """A text encoder maps prompts onto a continuous manifold with structure;
    inner CFG identifies that structure and moves along it (c -> m*c)."""
    out=rect(x,y,w,h,fill=INKG,stroke=STROKE,rx=8)
    ax0=x+18; ax1=x+w-16; ay=y+h/2+6
    def cv(t): return ay-(h*0.20)*math.sin(t*math.pi)
    pts=[(ax0+t/30*(ax1-ax0),cv(t/30)) for t in range(31)]
    out+=poly(pts,stroke=ACCENT,sw=2.4)
    ta=0.70; tb=0.32
    ca=(ax0+ta*(ax1-ax0),cv(ta)); cb=(ax0+tb*(ax1-ax0),cv(tb))
    out+=circle(ca[0],ca[1],5,fill=GOLD); out+=T(ca[0],ca[1]-10,"c",11,GOLD,"800",anchor="middle",ff=MONO)
    out+=circle(cb[0],cb[1],5,fill=TEAL); out+=T(cb[0],cb[1]-10,"m*c",11,TEAL,"800",anchor="middle",ff=MONO)
    out+=T(x+14,y+16,"continuous condition space",10,SEC,"700")
    out+=T(x+w-14,y+h-8,"move along structure",10,ACCENT,"800",anchor="end")
    return out

def expansionbars(x,y,w,h):
    """The guided score as a Taylor series: base + first-order CFG term + the
    new, small second-order inner-CFG term."""
    out=rect(x,y,w,h,fill=INKG,stroke=STROKE,rx=8)
    out+=T(x+16,y+24,"score ~ e0 + w*e1 + v*e2",13,TEXT,"800",ff=MONO)
    bx=x+16; bw=w-32; by=y+38
    segs=[("base",0.30,SEC),("CFG",0.44,GOLD),("ICFG",0.22,GREEN)]
    total=sum(s[1] for s in segs); cx=bx
    for lbl,frac,col in segs:
        seg=bw*frac/total
        out+=rect(cx,by,seg,26,fill=col,rx=4,sw=0,opacity=0.92)
        out+=T(cx+seg/2,by+17,lbl,11,BG,"800",anchor="middle")
        cx+=seg
    ly=y+86
    out+=circle(x+22,ly,5,fill=GOLD); out+=T(x+34,ly+4,"w e1 = first order (CFG)",10.5,SEC,"700")
    out+=circle(x+250,ly,5,fill=GREEN); out+=T(x+262,ly+4,"v e2 = new 2nd order",10.5,GREEN,"800")
    return out

def metricpair(x,y,w,h):
    """The two headline metrics: FID (image fidelity, lower better) and CLIP
    Score (prompt alignment, higher better)."""
    out=rect(x,y,w,h,fill=INKG,stroke=STROKE,rx=8)
    half=w/2
    cx1=x+half/2
    out+=T(cx1,y+26,"FID",15,ACCENT,"800",anchor="middle")
    out+=line(cx1,y+38,cx1,y+h-32,ACCENT,2.4)
    out+=poly([(cx1-6,y+h-40),(cx1,y+h-30),(cx1+6,y+h-40)],fill=ACCENT,stroke=ACCENT,sw=1)
    out+=T(cx1,y+h-13,"lower better",10,SEC,"700",anchor="middle")
    out+=line(x+half,y+14,x+half,y+h-14,STROKE,1,dash="4 4")
    cx2=x+half+half/2
    out+=T(cx2,y+26,"CLIP",15,TEAL,"800",anchor="middle")
    out+=line(cx2,y+h-32,cx2,y+38,TEAL,2.4)
    out+=poly([(cx2-6,y+46),(cx2,y+36),(cx2+6,y+46)],fill=TEAL,stroke=TEAL,sw=1)
    out+=T(cx2,y+h-13,"higher better",10,SEC,"700",anchor="middle")
    return out

def pareto(x,y,w,h):
    """FID vs CLIP trade-off: inner CFG sits up and to the left of plain CFG -
    better fidelity AND better alignment at once."""
    out=rect(x,y,w,h,fill=INKG,stroke=STROKE,rx=8)
    ax0=x+40; ax1=x+w-16; ay0=y+h-26; ay1=y+20
    out+=line(ax0,ay0,ax0,ay1,STROKE,1.2)
    out+=line(ax0,ay0,ax1,ay0,STROKE,1.2)
    out+=T(ax0-6,ay1+2,"CLIP",9.5,TER,"700",anchor="end")
    out+=T(ax1,ay0+15,"FID ->",9.5,TER,"700",anchor="end")
    def PX(fx): return ax0+fx*(ax1-ax0)
    def PY(fy): return ay0-fy*(ay0-ay1)
    cfg=(0.70,0.32); icfg=(0.30,0.78)
    out+=line(PX(cfg[0])-3,PY(cfg[1])-3,PX(icfg[0])+7,PY(icfg[1])+7,GOLD,1.6,dash="5 4")
    out+=T((PX(cfg[0])+PX(icfg[0]))/2+8,(PY(cfg[1])+PY(icfg[1]))/2-8,"better",9.5,GOLD,"800")
    out+=circle(PX(cfg[0]),PY(cfg[1]),6,fill=ACCENT)
    out+=T(PX(cfg[0])+9,PY(cfg[1])+11,"CFG",10.5,ACCENT,"800")
    out+=circle(PX(icfg[0]),PY(icfg[1]),6.5,fill=GREEN)
    out+=T(PX(icfg[0])+9,PY(icfg[1])+4,"ICFG",10.5,GREEN,"800")
    return out

def ucurve(x,y,w,h):
    """The middle point m gives a U-shaped FID: too close and the estimate
    misses long-term change, too near 0 or 1 and the model can't score it -
    best around m = 1.1."""
    out=rect(x,y,w,h,fill=INKG,stroke=STROKE,rx=8)
    ax0=x+34; ax1=x+w-14; ay0=y+h-26; ay1=y+16
    out+=line(ax0,ay0,ax1,ay0,STROKE,1.2)
    out+=line(ax0,ay0,ax0,ay1,STROKE,1.2)
    def v(t): return min(0.92,0.20+2.5*(t-0.55)**2)
    pts=[(ax0+t/40*(ax1-ax0),ay0-v(t/40)*(ay0-ay1)) for t in range(41)]
    out+=poly(pts,stroke=ACCENT,sw=2.6)
    mx=ax0+0.55*(ax1-ax0); my=ay0-v(0.55)*(ay0-ay1)
    out+=line(mx,my,mx,ay0,GOLD,1.2,dash="4 4")
    out+=circle(mx,my,4.6,fill=GOLD)
    out+=T(mx,ay0+15,"m=1.1",9.5,GOLD,"800",anchor="middle")
    out+=T(ax0-4,ay1+4,"FID",9.5,TER,"700",anchor="end")
    out+=T(ax1,ay0+15,"middle point m",9.5,TER,"700",anchor="end")
    return out

def stepcurve(x,y,w,h):
    """FID falls fast with sampling steps and is already good at just 10 steps,
    improving only modestly out to 50."""
    out=rect(x,y,w,h,fill=INKG,stroke=STROKE,rx=8)
    ax0=x+34; ax1=x+w-14; ay0=y+h-26; ay1=y+16
    out+=line(ax0,ay0,ax1,ay0,STROKE,1.2)
    out+=line(ax0,ay0,ax0,ay1,STROKE,1.2)
    def v(t): return 0.82*math.exp(-2.4*t)+0.12
    pts=[(ax0+t/40*(ax1-ax0),ay0-v(t/40)*(ay0-ay1)) for t in range(41)]
    out+=poly(pts,stroke=TEAL,sw=2.6)
    t10=0.15; mx=ax0+t10*(ax1-ax0); my=ay0-v(t10)*(ay0-ay1)
    out+=circle(mx,my,4.6,fill=GOLD)
    out+=T(mx+7,my-6,"10 steps",9.5,GOLD,"800")
    out+=T(ax1,pts[-1][1]-6,"50",9.5,TEAL,"800",anchor="end")
    out+=T(ax0-4,ay1+4,"FID",9.5,TER,"700",anchor="end")
    out+=T(ax1,ay0+15,"sampling steps ->",9.5,TER,"700",anchor="end")
    return out

# ---------- SLIDE 1: TITLE ----------
def s_title():
    ch=chunks("title"); b=""
    b+=T(64,72,"ICLR 2024",14,ACCENT,"800",ls="2")
    b+=T(1216,72,"Diffusion Models  ·  Guidance  ·  Taylor Expansion",13.5,SEC,"600",anchor="end")
    b+=line(64,88,1216,88,STROKE,1)
    b+=T(64,150,"ICFG",44,WHITE,"800")
    b+=T(64,196,"Inner Classifier-Free Guidance and Its",23,ACCENT,"800")
    b+=T(64,224,"Taylor Expansion for Diffusion Models",23,ACCENT,"800")
    b+=taylorfig(1112,176,1.0)
    b+=T(64,258,"Shikun Sun · Longhui Wei · Zhicai Wang · Zixuan Wang · Junliang Xing · Jia Jia · Qi Tian",13,SEC,"500")
    b+=T(64,280,"Tsinghua University   ·   Univ. of Science and Technology of China   ·   Huawei",12.5,TER,"600")
    cw=276; gap=16; x0=64; cy=306; chh=224
    data=[
        (ch[0],ACCENT,x0,"CFG: the control knob",
         "Classifier-free guidance lets conditional diffusion models trade sample diversity against fidelity - the standard control every model uses."),
        (ch[1],RED,x0+cw+gap,"But it ignores structure",
         "When the condition is continuous, like a text embedding, plain CFG treats it as an opaque label and ignores that structure entirely."),
        (ch[2],TEAL,x0+2*(cw+gap),"CFG is just first order",
         "This ICLR 2024 paper from Tsinghua and Huawei recasts standard CFG as the first-order term of a broader Taylor expansion: inner CFG."),
        (ch[3],GREEN,x0+3*(cw+gap),"One extra term, no retraining",
         "Adding a second-order term, with no change to training, buys a better fidelity-diversity balance for Stable Diffusion in a few lines of code."),
    ]
    for c,col,x,ti,tx in data:
        body=(rect(x,cy,cw,chh,fill=PANEL,stroke=STROKE)+
              rect(x,cy,cw,6,fill=col,rx=6,sw=0)+
              circle(x+26,cy+42,7,fill=col))
        body+=para(x+44,cy+48,ti,17,TEXT,22,22,"800")[0]
        body+=para(x+24,cy+96,tx,13,SEC,34,19)[0]
        b+=anchor(c["aid"],c["kw"],body)
    b+=line(64,556,1216,556,STROKE,1)
    b+=T(64,592,"openreview.net/forum?id=0QAzIMq32X",14,ACCENT,"700")
    b+=T(1216,592,"One extra term. No retraining.",14,SEC,"600",anchor="end")
    return svg(b)

# ---------- SLIDE 2: PROBLEM ----------
def s_problem():
    ch=chunks("problem"); b=header("Problem","A continuous condition, wasted")
    # c1 left tall: CFG is the control knob
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,404,392,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,392,fill=ACCENT,rx=6,sw=0)+
        T(92,202,"CFG is the control knob",17.5,TEXT,"800")+
        para(92,238,"Conditional diffusion models lean on classifier-free guidance to control how diverse and how faithful their generated samples are.",14,SEC,42,22)[0]+
        rect(92,352,344,146,fill=PANEL2,stroke=STROKE,rx=10)+
        T(112,382,"the one dial CFG gives you",12.5,TER,"700")+
        eqbox(112,398,304,"raise w:  fidelity up, diversity down",12,h=40)+
        T(112,478,"one scalar, and nothing about c",12,SEC,"600"))
    fx=500; fw=716
    # c2 CFG sees only an opaque label
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(fx,158,fw,150,fill=PANEL,stroke=STROKE)+
        rect(fx,158,6,150,fill=RED,rx=6,sw=0)+
        T(fx+28,196,"CFG sees only an opaque label",16.5,RED,"800")+
        para(fx+28,226,"Standard CFG treats the condition as an opaque label; it places no constraints at all on the condition space it steers through.",14,SEC,50,21)[0]+
        labelbox(fx+430,220,272,74))
    # c3 gold callout: the space is continuous
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(fx,324,fw,104,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(fx,324,6,104,fill=GOLD,rx=6,sw=0)+
        T(fx+28,362,"But that space is continuous",16,GOLD,"800")+
        para(fx+28,392,"A text-prompt embedding lives in a genuinely continuous space - so all of that continuity and structure simply goes to waste.",14.5,TEXT,74,22)[0])
    # c4 green callout: the question
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(fx,444,fw,106,fill="#0F2E2B",stroke=GREEN,rx=14,sw=1.5)+
        rect(fx,444,6,106,fill=GREEN,rx=6,sw=0)+
        T(fx+28,482,"The question this paper asks",16,GREEN,"800")+
        para(fx+28,512,"If the condition lives in a structured, continuous space, can we do better than plain classifier-free guidance?",14.5,SEC,74,22)[0])
    return svg(b)

# ---------- SLIDE 3: MOTIVATION ----------
def s_motivation():
    ch=chunks("motivation"); b=header("Motivation","Move along the condition space")
    # c1 left top: two ways to guide
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,560,192,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,192,fill=ACCENT,rx=6,sw=0)+
        T(92,196,"Two ways to guide a diffusion model",16,ACCENT,"800")+
        para(92,226,"There are two main routes to inject guidance: an external trained classifier, or classifier-free guidance a single model learns jointly.",14,SEC,58,21)[0]+
        chip(92,300,"external classifier   vs   classifier-free guidance",ACCENT,w=468,h=34))
    # c2 left bottom: neither knows the shape
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,366,560,184,fill=PANEL,stroke=STROKE)+
        rect(64,366,6,184,fill=TEAL,rx=6,sw=0)+
        T(92,404,"Neither knows the shape",16,TEAL,"800")+
        para(92,434,"Both routes work well in practice, but neither says anything about the shape of the condition space they are steering through.",14,SEC,58,21)[0]+
        eqbox(92,506,504,"guidance strength  !=  geometry of c",13.5))
    # c3 right top gold: a text encoder has structure
    rx=648; rw=568
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(rx,158,rw,192,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(rx,158,6,192,fill=GOLD,rx=6,sw=0)+
        T(rx+28,196,"A text encoder has real structure",16.5,GOLD,"800")+
        para(rx+28,226,"The authors' insight: a text encoder maps prompts into a continuous space with genuine structure - and if you can identify it, you can move along it.",14,TEXT,64,21)[0]+
        condmanifold(rx+28,296,rw-56,44))
    # c4 right bottom green: that opening is ICFG
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(rx,366,rw,184,fill="#0F2E2B",stroke=GREEN,rx=14,sw=1.5)+
        rect(rx,366,6,184,fill=GREEN,rx=6,sw=0)+
        T(rx+28,404,"That opening is inner CFG",16,GREEN,"800")+
        para(rx+28,434,"Following that structure from inside the condition space, rather than treating it as a flat label, is exactly what inner classifier-free guidance does.",14,TEXT,58,21)[0]+
        T(rx+28,524,"guide from within the condition space",13.5,GREEN,"800",ff=MONO))
    return svg(b)

# ---------- SLIDE 4: CONTRIBUTION ----------
def s_contribution():
    ch=chunks("contribution"); b=header("Contribution","CFG is only the first order")
    cards=[
        (ch[0],ACCENT,"Sum","CFG is just first order","Standard CFG is not the whole story - it is only the first-order term of a broader expansion the authors call inner CFG."),
        (ch[1],TEAL,"beta","A Taylor series in strength","Write the guided score as a Taylor series in the guidance strength around one: first order recovers CFG, then add a second-order term."),
        (ch[2],GREEN,"0","No retraining needed","That new second-order term is computed entirely from the existing pretrained model, so nothing has to be retrained."),
        (ch[3],GOLD,"3","Theory and algorithms","They also give a training policy, two sampling algorithms, and a convergence analysis backing the expansion."),
    ]
    cw=272; gap=24; x0=64; cy=180; chh=372
    for i,(c,col,tag,ti,tx) in enumerate(cards):
        x=x0+i*(cw+gap)
        body=(rect(x,cy,cw,chh,fill=PANEL,stroke=STROKE)+
              rect(x,cy,cw,6,fill=col,rx=6,sw=0)+
              circle(x+50,cy+66,26,fill="none",stroke=col,sw=2.5)+
              T(x+50,cy+75,tag,20,col,"800",anchor="middle",ff=MONO))
        yy=cy+134
        tlines=wrap(ti,18)
        for j,ln in enumerate(tlines):
            body+=T(x+24,yy+j*26,ln,17.5,TEXT,"800")
        yy+=26*len(tlines)+12
        body+=para(x+24,yy,tx,14,SEC,30,22)[0]
        b+=anchor(c["aid"],c["kw"],body)
    b+=T(64,586,"The same pretrained model, reinterpreted as the leading term of a principled Taylor expansion.",15.5,TEAL,"700")
    return svg(b)

# ---------- SLIDE 5: METHOD ----------
def s_method():
    ch=chunks("method"); b=header("Method","A second-order term, gained for free")
    # c1 full-width top: the guided distribution + eq + glyph
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,1152,168,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,168,fill=ACCENT,rx=6,sw=0)+
        T(92,192,"The guided distribution, raised to beta",16.5,TEXT,"800")+
        para(92,220,"Write the guided intermediate distribution as the unconditional one times the conditional-to-unconditional ratio, raised to a power beta.",13.5,SEC,64,20)[0]+
        eqbox(92,272,560,"p_b ~ p_u * (p_c / p_u)^beta,  beta = w+1",13,h=40)+
        expansionbars(676,196,540,116))
    # c2 Taylor-expand -> recover CFG
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,342,560,208,fill=PANEL,stroke=STROKE)+
        rect(64,342,6,208,fill=TEAL,rx=6,sw=0)+
        T(92,380,"Taylor-expand, recover CFG",16.5,TEAL,"800")+
        para(92,410,"Take a Taylor expansion of the score predictor in beta, evaluated at beta equals one. The first-order term is exactly classifier-free guidance.",13.5,TEXT,58,20)[0]+
        eqbox(92,508,504,"first-order term  =  CFG",13.5))
    # c3 gold: the new second-order term
    rxx=656; rw=560
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(rxx,342,rw,102,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(rxx,342,6,102,fill=GOLD,rx=6,sw=0)+
        T(rxx+28,376,"The new second-order term",16,GOLD,"800")+
        para(rxx+28,404,"Estimated with a middle point m in (0,1) - just one extra score evaluation at the scaled condition m times c.",13,TEXT,64,19)[0])
    # c4 green: a few lines on Stable Diffusion
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(rxx,460,rw,90,fill=PANEL,stroke=STROKE)+
        rect(rxx,460,6,90,fill=GREEN,rx=6,sw=0)+
        T(rxx+28,492,"A few lines on Stable Diffusion",15.5,GREEN,"800")+
        para(rxx+28,518,"Everything comes from the trained network, so second-order ICFG drops into pretrained SD, tuned by weights w and v.",12.5,SEC,74,17)[0])
    return svg(b)

# ---------- SLIDE 6: DATASET ----------
def s_dataset():
    ch=chunks("dataset-benchmark"); b=header("Dataset / Benchmark","MS-COCO, measured by FID and CLIP")
    # c1 full-width top: text-to-image on MS-COCO
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,1152,150,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,150,fill=ACCENT,rx=6,sw=0)+
        T(92,194,"Text-to-image on MS-COCO",16,TEXT,"800")+
        para(92,224,"The main evaluation is text-to-image generation on the MS-COCO validation set, the standard prompt-to-image benchmark.",14,SEC,58,21)[0]+
        para(92,290,"pretrained Stable Diffusion, no fine-tuning of the base model",12.5,TER,64,18)[0]+
        metricpair(852,176,340,112))
    # c2 the two metrics
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,324,560,226,fill=PANEL,stroke=STROKE)+
        rect(64,324,6,226,fill=TEAL,rx=6,sw=0)+
        T(92,362,"Two metrics tell the story",16,TEAL,"800")+
        para(92,390,"FID measures image fidelity, where lower is better; CLIP Score measures how well the image matches the prompt, where higher is better.",13.5,SEC,58,20)[0]+
        stat(92,466,254,66,"FID","fidelity  (lower better)",ACCENT)+
        stat(362,466,254,66,"CLIP","alignment  (higher better)",TEAL))
    # c3 three settings
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,324,560,226,fill=PANEL,stroke=STROKE)+
        rect(656,324,6,226,fill=RED,rx=6,sw=0)+
        T(684,362,"Three experimental settings",15.5,RED,"800")+
        para(684,390,"Beyond MS-COCO, the authors add a class-conditional study and a few-shot fine-tuning study.",13.5,SEC,58,20)[0]+
        chip(684,432,"Stable Diffusion   ·   text-to-image on MS-COCO",ACCENT,w=504,h=32)+
        chip(684,470,"U-ViT   ·   class-conditional generation",TEAL,w=504,h=32)+
        chip(684,508,"Stable Diffusion 1.5   ·   few-shot fine-tuning",GOLD,w=504,h=32))
    return svg(b)

# ---------- SLIDE 7: KEY RESULT ----------
def s_result():
    ch=chunks("key-result"); b=header("Key Result","Better FID and CLIP at once")
    # c1 headline strip + pareto
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,1152,150,fill="#0F2E2B",stroke=GREEN,rx=14,sw=1.5)+
        rect(64,158,6,150,fill=GREEN,rx=6,sw=0)+
        T(92,196,"The second-order term genuinely helps",16.5,GREEN,"800")+
        rect(92,214,540,80,fill=PANEL2,stroke=STROKE,rx=12)+
        para(112,244,"On the fidelity-alignment plane, inner CFG sits up and to the left of plain CFG - it improves both metrics together.",13,SEC,60,20)[0]+
        pareto(656,214,560,80))
    # c2 ICFG numbers
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,324,368,224,fill=PANEL,stroke=STROKE)+
        rect(64,324,6,224,fill=TEAL,rx=6,sw=0)+
        T(92,360,"ICFG  @  w=2, v=1/4",16,TEAL,"800")+
        para(92,388,"On MS-COCO, second-order inner CFG reaches:",13.5,SEC,42,20)[0]+
        stat(92,430,150,102,"15.28","FID",TEAL)+
        stat(254,430,150,102,"26.11","CLIP",TEAL))
    # c3 vs CFG
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(456,324,368,224,fill=PANEL,stroke=STROKE)+
        rect(456,324,6,224,fill=ACCENT,rx=6,sw=0)+
        T(484,360,"vs CFG, same setting",16,ACCENT,"800")+
        para(484,388,"Plain CFG is worse on both - ICFG wins fidelity and alignment:",13.5,SEC,44,20)[0]+
        stat(484,430,150,102,"15.42","FID  (CFG)",ACCENT)+
        stat(646,430,150,102,"25.80","CLIP  (CFG)",ACCENT))
    # c4 gold: better geometry
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(848,324,368,224,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(848,324,6,224,fill=GOLD,rx=6,sw=0)+
        T(876,360,"A more favorable geometry",15.5,GOLD,"800")+
        para(876,390,"The sweet spot is w = 2, v = 1/4. The full condition space trades off the two metrics more favorably than plain CFG can.",13.5,TEXT,42,20)[0]+
        chip(876,502,"no change to training",GOLD,w=316,h=32))
    return svg(b)

# ---------- SLIDE 8: ABLATION ----------
def s_ablation():
    ch=chunks("ablation-study"); b=header("Ablation Study","Choosing m and the step budget")
    # c1 full-width intro strip
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,1152,104,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,104,fill=GREEN,rx=6,sw=0)+
        T(92,194,"Two ablations pin down the design",16,GREEN,"800")+
        para(92,224,"Two studies fix the key knobs of second-order inner CFG: the middle point m used to estimate the term, and the number of sampling steps.",14,SEC,120,21)[0])
    # c2 left: middle point m -> U-shape
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,286,560,264,fill=PANEL,stroke=STROKE)+
        rect(64,286,6,264,fill=ACCENT,rx=6,sw=0)+
        T(92,324,"Middle point m: a U-shaped FID",16,ACCENT,"800")+
        para(92,352,"If the two points are too close, the estimate can't capture long-term change; drift too near 0 or 1 and the model struggles to score them. Best around m = 1.1.",13.5,SEC,40,20)[0]+
        ucurve(332,432,268,100))
    # c3 right: sampling steps
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,286,560,264,fill=PANEL,stroke=STROKE)+
        rect(656,286,6,264,fill=TEAL,rx=6,sw=0)+
        T(684,324,"Sampling steps: good even at 10",16,TEAL,"800")+
        para(684,352,"Varying the number of sampling steps shows the method already produces well-matched images at just ten steps, improving only modestly out to fifty.",13.5,SEC,40,20)[0]+
        stepcurve(924,432,268,100))
    return svg(b)

# ---------- SLIDE 9: HEADLINE NUMBERS ----------
def s_headline():
    ch=chunks("headline-numbers"); b=header("Headline Numbers","The result in one place")
    # c1 full-width strip: best balance
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,166,1152,132,fill="#0F2E2B",stroke=GREEN,rx=14,sw=1.5)+
        rect(64,166,6,132,fill=GREEN,rx=6,sw=0)+
        T(92,202,"Best fidelity-alignment balance on MS-COCO",16.5,GREEN,"800")+
        stat(92,220,300,66,"15.28 / 26.11","FID / CLIP  (ICFG)",GREEN)+
        rect(410,220,806,66,fill=PANEL2,stroke=STROKE,rx=12)+
        para(430,248,"Second-order inner CFG beats plain classifier-free guidance on both metrics at once, w = 2 and v = 1/4.",13.5,SEC,96,20)[0])
    # c2 middle-point sweep
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,314,560,150,fill=PANEL,stroke=STROKE)+
        rect(64,314,6,150,fill=ACCENT,rx=6,sw=0)+
        T(92,352,"Middle-point sweep",16.5,ACCENT,"800")+
        stat(92,368,236,80,"15.42","best FID",ACCENT)+
        stat(346,368,236,80,"m = 1.1","optimal middle point",TEAL)+
        T(112,458,"U-shaped FID over the estimator midpoint",12,SEC,"600"))
    # c3 U-ViT architecture
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,314,560,150,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(656,314,6,150,fill=GOLD,rx=6,sw=0)+
        T(684,352,"U-ViT architecture",16,GOLD,"800")+
        stat(684,368,236,80,"low steps","FID cut substantially",GOLD)+
        stat(938,368,236,80,"high steps","edges out CFG",TEAL)+
        T(704,458,"class-conditional generation on U-ViT",12,SEC,"600"))
    # c4 full-width bottom strip: cost
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(64,480,1152,70,fill=PANEL,stroke=STROKE)+
        rect(64,480,6,70,fill=GREEN,rx=6,sw=0)+
        T(92,510,"And it costs almost nothing",15.5,GREEN,"800")+
        T(92,534,"a few lines of code  ·  one extra score evaluation  ·  no change to training",13.5,SEC,"600")+
        eqbox(864,492,352,"beta = w + 1",14,h=46))
    return svg(b)

# ---------- SLIDE 10: TAKEAWAY ----------
def s_takeaway():
    ch=chunks("takeaway"); b=header("Takeaway","The first slice of a bigger picture")
    cards=[
        (ch[0],ACCENT,"The idea in one line","Guidance has more structure than a single scalar knob suggests - and that structure is usable."),
        (ch[1],TEAL,"CFG is only first order","Classifier-free guidance is just the first-order slice of a much richer Taylor picture of the guided score."),
        (ch[2],GREEN,"One extra term, for free","Add a single second-order term to the expansion in guidance strength and you buy a better fidelity-diversity trade-off."),
        (ch[3],GOLD,"Exploit the condition space","No retraining - just a scaled condition and a few lines of code - pointing toward the continuous structure plain CFG throws away."),
    ]
    cw=560; gap=32; x0=64; cy=176; chh=180
    pos=[(x0,cy),(x0+cw+gap,cy),(x0,cy+chh+18),(x0+cw+gap,cy+chh+18)]
    for (c,col,ti,tx),(x,y) in zip(cards,pos):
        body=(rect(x,y,cw,chh,fill=PANEL,stroke=STROKE)+
              rect(x,y,6,chh,fill=col,rx=6,sw=0)+
              circle(x+34,y+40,10,fill=col))
        for j,ln in enumerate(wrap(ti,40)):
            body+=T(x+58,y+34+j*24,ln,17,TEXT,"800")
        body+=para(x+28,y+94,tx,14,SEC,62,21)[0]
        b+=anchor(c["aid"],c["kw"],body)
    b+=line(64,584,1216,584,STROKE,1)
    b+=taylorfig(150,632,0.44)
    b+=T(1216,632,"ICFG  ·  Inner Classifier-Free Guidance & its Taylor Expansion  ·  ICLR 2024",14,SEC,"600",anchor="end")
    return svg(b)

SLIDES=[("01_title",s_title),("02_problem",s_problem),("03_motivation",s_motivation),
        ("04_contribution",s_contribution),("05_method",s_method),("06_dataset",s_dataset),
        ("07_key_result",s_result),("08_ablation",s_ablation),("09_headline",s_headline),
        ("10_takeaway",s_takeaway)]

for name,fn in SLIDES:
    open(os.path.join(OUT,name+".svg"),"w").write(fn())
    print("wrote",name)
print("DONE",len(SLIDES))
