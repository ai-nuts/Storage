#!/usr/bin/env python3
"""All-native SVG deck builder for paper2video run 097 (EP / Jacobian homeostasis).
Reads _anchor_map.json; wraps each narration chunk in its own <g id="cue_..."> card
with a <title> holding the cue keywords, so the strict --require-pptx-anchors cue
pass resolves every anchor from PPTX geometry. Zero <image>, zero gradients, ASCII
mono equations only."""
import json, os, math

HERE = os.path.dirname(os.path.abspath(__file__))
META = os.environ["VIDEO_META"]
OUT  = os.path.join(HERE, "svg_output")
os.makedirs(OUT, exist_ok=True)
AM = json.load(open(os.path.join(META, "_anchor_map.json")))

W, H = 1280, 720
BG="#0B1B2B"; PANEL="#12293D"; PANEL2="#16324A"; STROKE="#26455F"
ACCENT="#4C9BE8"; TEAL="#34D3C0"; GOLD="#F2C14E"; RED="#F2685C"; GREEN="#48C78E"
TEXT="#EAF2FB"; SEC="#9DB3C8"; TER="#6E869C"; WHITE="#FFFFFF"
SANS="Arial, 'Helvetica Neue', Helvetica, sans-serif"
MONO="'DejaVu Sans Mono', Consolas, monospace"

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

def bar(x,y,w,val,vmax,color,label,valtxt,lblcolor=SEC,h=26):
    bw=max(2,int(w*val/vmax))
    return (rect(x,y,w,h,fill="#0E2334",stroke=STROKE,rx=6,sw=1)+
            rect(x,y,bw,h,fill=color,rx=6,sw=0)+
            T(x-12,y+h*0.72,label,14,lblcolor,"600",anchor="end")+
            T(x+bw+10,y+h*0.72,valtxt,14,color,"800"))

def kpi(x,y,num,lbl,col,w=168,h=100):
    return (rect(x,y,w,h,fill=PANEL2,stroke=STROKE,rx=12)+
            T(x+w/2,y+56,num,30,col,"800",anchor="middle")+
            T(x+w/2,y+82,lbl,12.5,SEC,"600",anchor="middle"))

def chip(x,y,text,col,w=512,h=34):
    return (rect(x,y,w,h,fill=PANEL2,stroke=STROKE,rx=8)+
            circle(x+18,y+h/2,5,fill=col)+
            T(x+34,y+h/2+6,text,14.5,TEXT,"600"))

def eqbox(x,y,w,expr,size=17,h=44):
    return (rect(x,y,w,h,fill=PANEL2,stroke=STROKE,rx=8)+
            T(x+w/2,y+h/2+6,expr,size,TEXT,"800",anchor="middle",ff=MONO))

# ---------- SLIDE 1: TITLE ----------
def s_title():
    ch=chunks("title"); b=""
    b+=T(64,72,"ICLR 2024",14,ACCENT,"800",ls="3")
    b+=T(1216,72,"Friedrich Miescher Institute  ·  University of Basel",14,SEC,"600",anchor="end")
    b+=line(64,88,1216,88,STROKE,1)
    b+=T(64,158,"Improving Equilibrium Propagation",40,WHITE,"800")
    b+=T(64,206,"without Weight Symmetry",40,ACCENT,"800")
    b+=T(64,244,"through Jacobian Homeostasis",26,TEAL,"800")
    b+=T(64,284,"Axel Laborieux   ·   Friedemann Zenke      —   Friedrich Miescher Institute & University of Basel",16,SEC,"500")
    # four concept cards (2x2) = anchors
    cw=560; chh=118; gap=32; x0=64; x1=x0+cw+gap; cy0=316; cy1=cy0+chh+22
    data=[
        (ch[0],ACCENT,x0,cy0,"Equilibrium propagation (EP)","An energy-based, backprop-free way to train networks on brains or neuromorphic chips using only relaxation dynamics."),
        (ch[1],GOLD,x1,cy0,"Two classical demands","EP needs perfectly symmetric weights and an infinitesimally small nudge, both hard for real physical substrates."),
        (ch[2],TEAL,x0,cy1,"Remove both biases","Cauchy integral erases finite-nudge bias exactly; a homeostatic loss tames weight-asymmetry bias on the Jacobian."),
        (ch[3],GREEN,x1,cy1,"The payoff","For the first time, asymmetric EP trains on ImageNet 32x32, with only a small gap to the ideal symmetric case."),
    ]
    for c,col,x,cy,ti,tx in data:
        body=(rect(x,cy,cw,chh,fill=PANEL,stroke=STROKE)+
              rect(x,cy,6,chh,fill=col,rx=6,sw=0)+
              T(x+28,cy+36,ti,18,TEXT,"800"))
        body+=para(x+28,cy+62,tx,14,SEC,68,21)[0]
        b+=anchor(c["aid"],c["kw"],body)
    b+=line(64,616,1216,616,STROKE,1)
    b+=T(64,650,"arXiv:2309.02214",14,ACCENT,"700")
    b+=T(300,650,"Functional symmetry, not weight symmetry, is what EP really needs.",14,SEC,"600")
    return svg(b)

# ---------- SLIDE 2: PROBLEM ----------
def s_problem():
    ch=chunks("problem"); b=header("Problem","Two strict demands EP cannot escape")
    # c1 what EP is (left tall card)
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,404,392,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,392,fill=ACCENT,rx=6,sw=0)+
        T(92,202,"What makes EP appealing",18,TEXT,"800")+
        para(92,240,"EP computes gradients using only the network's own relaxation dynamics, with no separate backward pass.",15,SEC,42,24)[0]+
        # mini free -> nudged relaxation glyph
        rect(92,346,144,120,fill=PANEL2,stroke=STROKE,rx=10)+
        T(164,332,"free phase",12,TER,"600",anchor="middle")+
        circle(128,406,9,fill=ACCENT)+circle(164,388,9,fill=ACCENT)+circle(200,414,9,fill=ACCENT)+
        line(128,406,164,388,STROKE,2)+line(164,388,200,414,STROKE,2)+
        T(252,392,"nudge",12,GOLD,"700")+line(244,404,300,404,GOLD,2,dash="4 4")+T(300,410,"->",18,GOLD,"800")+
        rect(316,346,120,120,fill=PANEL2,stroke=STROKE,rx=10)+T(376,332,"nudged",12,TER,"600",anchor="middle")+
        circle(352,406,9,fill=TEAL)+circle(388,392,9,fill=TEAL)+circle(412,414,9,fill=TEAL)+
        T(92,502,"Gradient read off from how the state moves.",13.5,TEAL,"700"))
    # right: two requirements + the tangle
    fx=500; fw=716
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(fx,158,fw,120,fill=PANEL,stroke=STROKE)+
        T(fx+28,196,"Two strict requirements",17,GOLD,"800")+
        rect(fx+28,214,320,48,fill=PANEL2,stroke=STROKE,rx=8)+circle(fx+52,238,6,fill=RED)+T(fx+70,243,"Perfectly symmetric weights",14.5,TEXT,"700")+
        rect(fx+368,214,320,48,fill=PANEL2,stroke=STROKE,rx=8)+circle(fx+392,238,6,fill=RED)+T(fx+410,243,"Infinitesimally small nudge",14.5,TEXT,"700"))
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(fx,290,fw,96,fill=PANEL,stroke=STROKE)+
        rect(fx,290,6,96,fill=GOLD,rx=6,sw=0)+
        T(fx+28,328,"Both are very hard on real hardware",16,GOLD,"800")+
        para(fx+28,356,"Physical and neuromorphic substrates cannot deliver exact weight transposes or vanishingly small teaching signals.",14.5,SEC,74,22)[0])
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(fx,398,fw,152,fill="#2A1720",stroke=RED,rx=14,sw=1.5)+
        rect(fx,398,6,152,fill=RED,rx=6,sw=0)+
        T(fx+28,438,"The open question",16,RED,"800")+
        para(fx+28,468,"Does weight asymmetry actually harm learning? It had never been pinned down, because its effect is tangled up with the error from a finite nudge.",14.5,TEXT,74,22)[0]+
        T(fx+28,540,"asymmetry bias  +  finite-nudge bias  =  ?",15,RED,"800",ff=MONO))
    return svg(b)

# ---------- SLIDE 3: MOTIVATION ----------
def s_motivation():
    ch=chunks("motivation"); b=header("Motivation","Why train on physical substrates at all")
    # c1 energy headline + comparison bars (left)
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,560,392,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,392,fill=TEAL,rx=6,sw=0)+
        T(92,198,"It comes down to energy",18,TEAL,"800")+
        para(92,230,"Brains and neuromorphic chips could train networks at a tiny fraction of digital hardware's energy cost.",14.5,SEC,50,22)[0]+
        T(92,320,"Relative training energy (illustrative)",13,TER,"700")+
        bar(300,338,280,1.00,1.00,GOLD,"Digital / backprop","high",h=30)+
        bar(300,384,280,0.06,1.00,TEAL,"Physical substrate","tiny",h=30)+
        rect(92,440,504,90,fill=PANEL2,stroke=STROKE,rx=10)+
        T(112,470,"The prize",13.5,TEAL,"800")+
        para(112,494,"A biologically plausible, low-energy route to training large networks.",13.5,SEC,60,20)[0])
    # right: backprop's demand, EP sidesteps, warning sign
    rx=648; rw=568
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(rx,158,rw,116,fill=PANEL,stroke=STROKE)+
        rect(rx,158,6,116,fill=RED,rx=6,sw=0)+
        T(rx+28,196,"Backprop is biologically implausible",16,RED,"800")+
        para(rx+28,226,"It needs a separate linear backward pass and the exact transpose of every weight matrix, neither of which substrates provide.",14.5,SEC,60,22)[0])
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(rx,286,rw,108,fill=PANEL,stroke=STROKE)+
        rect(rx,286,6,108,fill=ACCENT,rx=6,sw=0)+
        T(rx+28,324,"EP sidesteps this",16,ACCENT,"800")+
        para(rx+28,354,"But its own weight-symmetry assumption is nearly as demanding as backprop's transpose.",14.5,SEC,60,22)[0])
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(rx,406,rw,144,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(rx,406,6,144,fill=GOLD,rx=6,sw=0)+
        T(rx+28,444,"A warning sign",16,GOLD,"800")+
        para(rx+28,474,"Asymmetric EP had only ever worked on toy tasks like MNIST, and outright failed on CIFAR-10.",14.5,TEXT,60,22)[0]+
        T(rx+28,536,"MNIST  ok      ·      CIFAR-10  fails  (why?)",14.5,GOLD,"800",ff=MONO))
    return svg(b)

# ---------- SLIDE 4: CONTRIBUTION ----------
def s_contribution():
    ch=chunks("contribution"); b=header("Contribution","Four contributions")
    cards=[
        (ch[0],ACCENT,"1","Separate the two biases","Analytically isolate generalized EP's two error sources: the finite nudge, and the asymmetry of the network's Jacobian."),
        (ch[1],TEAL,"2","Holomorphic EP, asymmetric","Extend holomorphic EP to asymmetric, complex-differentiable systems, recovering the exact error without weight symmetry."),
        (ch[2],GOLD,"3","A homeostatic loss","Introduce a loss that reduces the asymmetry of the Jacobian directly, rather than forcing the weights to be symmetric."),
        (ch[3],GREEN,"4","Scale to ImageNet 32x32","Show that with this loss, EP finally scales all the way up to ImageNet at 32 by 32 resolution."),
    ]
    cw=272; gap=24; x0=64; cy=180; chh=372
    for i,(c,col,num,ti,tx) in enumerate(cards):
        x=x0+i*(cw+gap)
        body=(rect(x,cy,cw,chh,fill=PANEL,stroke=STROKE)+
              rect(x,cy,cw,6,fill=col,rx=6,sw=0)+
              circle(x+50,cy+66,26,fill="none",stroke=col,sw=2.5)+
              T(x+50,cy+76,num,28,col,"800",anchor="middle"))
        yy=cy+134
        for j,ln in enumerate(wrap(ti,17)):
            body+=T(x+24,yy+j*26,ln,17.5,TEXT,"800");
        yy+=26*len(wrap(ti,17))+10
        body+=para(x+24,yy,tx,14,SEC,30,22)[0]
        b+=anchor(c["aid"],c["kw"],body)
    b+=T(64,584,"Two biases, cleanly separated  —  then each one removed.",15.5,TEAL,"700")
    return svg(b)

# ---------- SLIDE 5: METHOD ----------
def s_method():
    ch=chunks("method"); b=header("Method","Erase one bias exactly, shrink the other")
    # LEFT: finite-nudge bias -> Cauchy integral (c1 + c2)
    lx=64; lw=568
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(lx,158,lw,200,fill=PANEL,stroke=STROKE)+
        rect(lx,158,6,200,fill=ACCENT,rx=6,sw=0)+
        T(lx+28,196,"Bias 1  ·  finite nudge",16.5,ACCENT,"800")+
        para(lx+28,226,"Drive the network with an oscillating teaching signal and use a Cauchy integral to recover the exact error vector, for any nudge size and even an asymmetric Jacobian.",14,SEC,58,21)[0]+
        eqbox(lx+28,314,lw-56,"du*/db = (1/2 pi i) oint u*_b / b^2 db",15))
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(lx,374,lw,176,fill="#0F2E2B",stroke=TEAL,rx=14,sw=1.5)+
        rect(lx,374,6,176,fill=TEAL,rx=6,sw=0)+
        T(lx+28,412,"Estimate it continuously",16,TEAL,"800")+
        para(lx+28,442,"The integral can be estimated over many oscillation cycles, removing the need for separate free and nudged phases.",14,SEC,58,21)[0]+
        eqbox(lx+28,502,lw-56,"= (1/T|b|) integral_0^T u*_b(t) e^(-2 pi i t/T) dt",13.5))
    # RIGHT: Jacobian asymmetry -> homeostatic loss (c3 + c4)
    rxx=656; rw=560
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(rxx,158,rw,200,fill=PANEL,stroke=STROKE)+
        rect(rxx,158,6,200,fill=GOLD,rx=6,sw=0)+
        T(rxx+28,196,"Bias 2  ·  Jacobian asymmetry",16.5,GOLD,"800")+
        para(rxx+28,226,"This bias grows with the skew-symmetric part A of the Jacobian. A homeostatic loss penalizes exactly that part, estimated with the Hutchinson trace trick.",14,SEC,56,21)[0]+
        eqbox(rxx+28,314,rw-56,"L_homeo = E[ ||J e||^2 - e^T J^2 e ]",15))
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(rxx,374,rw,176,fill=PANEL,stroke=STROKE)+
        rect(rxx,374,6,176,fill=GREEN,rx=6,sw=0)+
        T(rxx+28,412,"Key insight  ·  functional symmetry",16,GREEN,"800")+
        para(rxx+28,442,"The loss improves functional symmetry of the Jacobian without ever forcing the weights themselves to be symmetric.",14,SEC,56,21)[0]+
        eqbox(rxx+28,502,rw-56,"d_b u* = delta - 2 S^-1 A delta + o(.)",14))
    return svg(b)

# ---------- SLIDE 6: DATASET ----------
def s_dataset():
    ch=chunks("dataset-benchmark"); b=header("Dataset / Benchmark","Four datasets of rising difficulty")
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,1152,58,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,58,fill=ACCENT,rx=6,sw=0)+
        T(92,193,"Experiments span four datasets of increasing difficulty, from bias-isolation MLPs up to large-scale image classification.",16,TEXT,"600"))
    # c2 fashion mnist (bias isolation)
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,240,560,150,fill=PANEL,stroke=STROKE)+
        rect(64,240,6,150,fill=ACCENT,rx=6,sw=0)+
        T(92,282,"Fashion MNIST  ·  small MLPs",19,ACCENT,"800")+
        para(92,316,"Small multilayer networks used to cleanly isolate and measure each source of bias.",14.5,SEC,58,22)[0]+
        chip(92,350,"Purpose: separate finite-nudge vs asymmetry bias",ACCENT,w=468,h=30))
    # c3 recurrent conv arch (CIFAR/ImageNet)
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,240,560,150,fill=PANEL,stroke=STROKE)+
        rect(656,240,6,150,fill=TEAL,rx=6,sw=0)+
        T(684,282,"Recurrent conv net  ·  asymmetric feedback",17,TEAL,"800")+
        para(684,316,"Genuinely asymmetric feedback weights, trained on progressively harder image sets.",14.5,SEC,58,22)[0]+
        chip(684,350,"CIFAR-10   ·   CIFAR-100   ·   ImageNet 32x32",TEAL,w=468,h=30))
    # c4 predictive coding appendix
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(64,410,1152,140,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(64,410,6,140,fill=GOLD,rx=6,sw=0)+
        T(92,448,"Beyond reciprocal networks (Appendix)",17,GOLD,"800")+
        para(92,480,"The same homeostatic loss also helps predictive coding networks, which have no reciprocal connections at all, confirming it targets functional symmetry rather than tied weights.",14.5,TEXT,110,23)[0])
    return svg(b)

# ---------- SLIDE 7: KEY RESULT ----------
def s_result():
    ch=chunks("key-result"); b=header("Key Result","The homeostatic loss unlocks scale")
    # c1 headline strip
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,150,1152,50,fill=PANEL,stroke=STROKE)+
        rect(64,150,6,50,fill=GREEN,rx=6,sw=0)+
        T(92,182,"On CIFAR-10, asymmetric EP without the homeostatic loss reaches only 60.4% accuracy.",16.5,TEXT,"700"))
    # c2 CIFAR-10 bars (left)
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,214,560,264,fill=PANEL,stroke=STROKE)+
        rect(64,214,6,264,fill=TEAL,rx=6,sw=0)+
        T(92,250,"CIFAR-10 accuracy  ·  higher is better",16,TEAL,"800")+
        bar(300,278,250,60.4,90,RED,"EP, no homeo","60.4%",h=30)+
        bar(300,326,250,84.3,90,GREEN,"EP + homeo","84.3%",h=30)+
        bar(300,374,250,88.6,90,ACCENT,"Symmetric","88.6%",h=30)+
        rect(92,418,504,44,fill="#0F2E2B",stroke=TEAL,rx=10,sw=1.5)+
        T(112,446,"+23.9 points  ·  only a 4.3-point gap to symmetric",15,TEAL,"800"))
    # c3 ImageNet first-of-its-kind (right)
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,214,560,264,fill=PANEL,stroke=STROKE)+
        rect(656,214,6,264,fill=GOLD,rx=6,sw=0)+
        T(684,250,"ImageNet 32x32  ·  first EP result ever",16,GOLD,"800")+
        kpi(684,272,"31.4%","Top-1 accuracy",GOLD,w=250,h=104)+
        kpi(962,272,"55.2%","Top-5 accuracy",GOLD,w=250,h=104)+
        rect(684,394,528,68,fill=PANEL2,stroke=STROKE,rx=10)+
        para(704,422,"The first time this family of methods trains at all at ImageNet scale.",13.5,SEC,64,20)[0])
    # c4 alignment trend strip
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(64,492,1152,116,fill=PANEL,stroke=STROKE)+
        rect(64,492,6,116,fill=ACCENT,rx=6,sw=0)+
        T(92,526,"Throughout training",16,ACCENT,"800")+
        _trend(560,506,360,88)+
        para(92,556,"The homeostatic loss steadily raises the Jacobian's symmetry and tightens the alignment between EP's error signals and true backprop.",14.5,SEC,58,22)[0])
    b+=T(64,648,"Approximate weight symmetry is enough — functional symmetry does the work.",14,SEC,"600")
    return svg(b)

def _trend(x,y,w,h):
    # two rising curves: symmetry + alignment
    def curve(col,amp,off):
        pts=[]
        for i in range(0,w+1,12):
            t=i/w
            v=off+amp*(1-math.exp(-3*t))
            pts.append((x+i, y+h-int(v*h)))
        return f'<polyline points="{" ".join(f"{px},{py}" for px,py in pts)}" fill="none" stroke="{col}" stroke-width="2.5"/>'
    box=rect(x,y,w,h,fill="#0E2334",stroke=STROKE,rx=8)
    return (box+curve(TEAL,0.62,0.14)+curve(ACCENT,0.5,0.28)+
            T(x+w-8,y+18,"Jacobian symmetry",11.5,TEAL,"700",anchor="end")+
            T(x+w-8,y+34,"error alignment",11.5,ACCENT,"700",anchor="end")+
            T(x+10,y+h-6,"training ->",11,TER,"600"))

# ---------- SLIDE 8: ABLATION ----------
def s_ablation():
    ch=chunks("ablation-study"); b=header("Ablation Study","Each bias, measured on its own")
    # c1 setup (left top)
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,560,110,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,110,fill=ACCENT,rx=6,sw=0)+
        T(92,196,"Isolating finite-nudge bias",16.5,ACCENT,"800")+
        para(92,226,"On Fashion MNIST with a large nudge, classic one-sided EP falls apart while the Cauchy estimate holds.",14.5,SEC,54,22)[0])
    # c2 error bars (left bottom): 38.4 vs 14.3 vs 14.7
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,284,560,266,fill=PANEL,stroke=STROKE)+
        rect(64,284,6,266,fill=TEAL,rx=6,sw=0)+
        T(92,320,"Fashion MNIST error at large nudge |b|=0.5  ·  lower is better",14.5,TEXT,"800")+
        bar(330,346,200,38.4,40,RED,"one-sided EP","38.4%",h=30)+
        bar(330,394,200,14.3,40,TEAL,"Cauchy, N=6","14.3%",h=30)+
        bar(330,442,200,14.7,40,ACCENT,"true derivative","14.7%",h=30)+
        rect(92,490,504,44,fill="#0F2E2B",stroke=TEAL,rx=10,sw=1.5)+
        T(112,518,"N=6 estimate matches the true derivative: nudge bias removed",14,TEAL,"800"))
    # c3 residual nudge bias (right top)
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,158,560,180,fill=PANEL,stroke=STROKE)+
        rect(656,158,6,180,fill=GOLD,rx=6,sw=0)+
        T(684,196,"Quantifying the residual",16.5,GOLD,"800")+
        para(684,226,"Dropping from the exact derivative to a coarse two-point (N=2) estimate costs about 3 points on CIFAR-10.",14.5,SEC,56,22)[0]+
        rect(684,290,504,34,fill=PANEL2,stroke=STROKE,rx=8)+
        T(936,312,"N=2  vs  exact   =   about -3 pts (CIFAR-10)",14.5,GOLD,"800",anchor="middle",ff=MONO))
    # c4 functional not weight symmetry (right bottom)
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(656,354,560,196,fill="#0F2E2B",stroke=GREEN,rx=14,sw=1.5)+
        rect(656,354,6,196,fill=GREEN,rx=6,sw=0)+
        T(684,392,"Functional, not weight, symmetry",16.5,GREEN,"800")+
        para(684,424,"An architecture whose output feeds straight back to the first layer, with no reciprocal connections, benefits just as much.",14.5,TEXT,56,22)[0]+
        chip(684,494,"Confirms the loss targets functional symmetry",GREEN,w=504,h=34))
    return svg(b)

# ---------- SLIDE 9: HEADLINE NUMBERS ----------
def s_headline():
    ch=chunks("headline-numbers"); b=header("Headline Numbers","The results in one place")
    # c1 CIFAR-10 big lift
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,168,1152,146,fill=PANEL,stroke=STROKE)+
        rect(64,168,6,146,fill=GREEN,rx=6,sw=0)+
        T(92,206,"CIFAR-10  ·  the homeostatic loss earns its keep",16.5,GREEN,"800")+
        kpi(92,224,"60.4%","EP, no homeo",RED,w=210,h=76)+
        T(322,270,"->",30,SEC,"800",anchor="middle")+
        kpi(352,224,"84.3%","EP + homeo",GREEN,w=210,h=76)+
        kpi(600,224,"4.3 pts","gap to symmetric",TEAL,w=230,h=76)+
        rect(852,224,364,76,fill=PANEL2,stroke=STROKE,rx=12)+
        para(872,252,"A 23.9-point jump from only approximate weight symmetry.",14,SEC,40,20)[0])
    # c2 ImageNet
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,330,560,220,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(64,330,6,220,fill=GOLD,rx=6,sw=0)+
        T(92,368,"ImageNet 32x32  ·  first of its kind",16.5,GOLD,"800")+
        kpi(92,388,"31.4%","Top-1",GOLD,w=250,h=104)+
        kpi(370,388,"55.2%","Top-5",GOLD,w=250,h=104)+
        T(92,532,"The first equilibrium-propagation result at this scale.",14,SEC,"600"))
    # c3 Fashion MNIST nudge
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,330,560,220,fill=PANEL,stroke=STROKE)+
        rect(656,330,6,220,fill=TEAL,rx=6,sw=0)+
        T(684,368,"Fashion MNIST  ·  large nudge |b|=0.5",16.5,TEAL,"800")+
        kpi(684,388,"38.4%","classic EP error",RED,w=250,h=104)+
        T(946,442,"->",30,SEC,"800",anchor="middle")+
        kpi(966,388,"14.3%","exact estimate",TEAL,w=250,h=104)+
        T(684,532,"The Cauchy estimate cuts error by more than half.",14,SEC,"600"))
    return svg(b)

# ---------- SLIDE 10: TAKEAWAY ----------
def s_takeaway():
    ch=chunks("takeaway"); b=header("Takeaway","EP does not need symmetric weights")
    cards=[
        (ch[0],ACCENT,"Drop the hard assumption","Equilibrium propagation does not actually need perfectly symmetric weights to learn well."),
        (ch[1],TEAL,"Two fixes, one payoff","A Cauchy integral removes finite-nudge bias exactly; a homeostatic loss encourages functional Jacobian symmetry, so asymmetric nets scale to ImageNet-level tasks."),
        (ch[2],GREEN,"A biologically plausible path","Functional symmetry is weaker and more achievable than weight symmetry, hinting brains might rely on similar homeostatic mechanisms."),
    ]
    y=176
    for c,col,ti,tx in cards:
        body=(rect(64,y,1152,116,fill=PANEL,stroke=STROKE)+
              rect(64,y,6,116,fill=col,rx=6,sw=0)+
              circle(112,y+58,10,fill=col)+
              T(150,y+46,ti,19,TEXT,"800"))
        body+=para(150,y+78,tx,15.5,SEC,88,24)[0]
        b+=anchor(c["aid"],c["kw"],body)
        y+=132
    b+=line(64,596,1216,596,STROKE,1)
    b+=T(64,632,"Improving Equilibrium Propagation without Weight Symmetry through Jacobian Homeostasis",15.5,TEXT,"700")
    b+=T(64,660,"ICLR 2024  ·  Laborieux & Zenke  ·  arXiv:2309.02214",13.5,SEC,"600")
    return svg(b)

SLIDES=[("01_title",s_title),("02_problem",s_problem),("03_motivation",s_motivation),
        ("04_contribution",s_contribution),("05_method",s_method),("06_dataset",s_dataset),
        ("07_key_result",s_result),("08_ablation",s_ablation),("09_headline",s_headline),
        ("10_takeaway",s_takeaway)]

for name,fn in SLIDES:
    open(os.path.join(OUT,name+".svg"),"w").write(fn())
    print("wrote",name)
print("DONE",len(SLIDES))
