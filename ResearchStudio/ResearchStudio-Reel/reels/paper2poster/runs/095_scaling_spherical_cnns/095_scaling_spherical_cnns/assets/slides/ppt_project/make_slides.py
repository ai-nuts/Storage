#!/usr/bin/env python3
"""All-native SVG deck builder for paper2video run 095 (Scaling Spherical CNNs).
Reads _anchor_map.json; wraps each narration chunk in its own <g id="cue_..."> card
with a <title> holding the cue keywords, so the strict --require-pptx-anchors cue
pass resolves every anchor from PPTX geometry."""
import json, os, math

HERE = os.path.dirname(os.path.abspath(__file__))
META = os.environ["VIDEO_META"]
OUT  = os.path.join(HERE, "svg_output")
os.makedirs(OUT, exist_ok=True)
AM = json.load(open(os.path.join(META, "_anchor_map.json")))
QR_PAPER = os.path.join(os.environ["VIDEO_OUT"], "assets/qr/paper.png")
QR_CODE  = os.path.join(os.environ["VIDEO_OUT"], "assets/qr/code.png")

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

def image(x,y,w,h,href):
    return f'<image x="{x}" y="{y}" width="{w}" height="{h}" href="{esc(href)}" preserveAspectRatio="xMidYMid meet"/>'

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

def chip(x,y,w,text,col,h=34,size=14.5):
    return (rect(x,y,w,h,fill=PANEL2,stroke=STROKE,rx=8)+
            circle(x+18,y+h/2,5,fill=col)+
            T(x+34,y+h/2+5,text,size,TEXT,"600"))

# ---------- SLIDE 1: TITLE ----------
def s_title():
    ch=chunks("title"); b=""
    b+=T(64,72,"ICML 2023",14,ACCENT,"800",ls="3")
    b+=T(1216,72,"Google Research   ·   MIT",14,SEC,"600",anchor="end")
    b+=line(64,88,1216,88,STROKE,1)
    b+=T(64,168,"Scaling Spherical CNNs",46,WHITE,"800")
    b+=T(64,214,"Rotation-equivariant deep nets, scaled by an order of magnitude",21,ACCENT,"700")
    b+=T(64,250,"Carlos Esteves   ·   Jean-Jacques Slotine   ·   Ameesh Makadia      —   Google Research, MIT",16,SEC,"500")
    # four concept cards
    cy=292; cw=272; gap=16; cx=64
    data=[
        (ACCENT,"Signals on the sphere","Spherical CNNs generalize convnets to data on a sphere — a natural fit for molecules and weather."),
        (RED,"Stuck small","Until now: low resolutions and shallow depth. They never competed on large real problems."),
        (TEAL,"Scaled x10","Google Research and MIT scale these models by a full order of magnitude."),
        (GOLD,"New recipe, SOTA","New activations, normalization, residual blocks and TPU-tuned JAX -> SOTA on QM9, competitive weather."),
    ]
    for i,(col,ti,tx) in enumerate(data):
        x=cx+i*(cw+gap)
        body=(rect(x,cy,cw,196,fill=PANEL,stroke=STROKE)+
              rect(x,cy,cw,6,fill=col,rx=6,sw=0)+
              circle(x+26,cy+42,7,fill=col)+
              T(x+44,cy+48,ti,17,TEXT,"800"))
        pp,_=para(x+22,cy+86,tx,14,SEC,30,22)
        body+=pp
        b+=anchor(ch[i]["aid"],ch[i]["kw"],body)
    b+=line(64,548,1216,548,STROKE,1)
    b+=T(64,586,"State of the art on the QM9 molecular benchmark; the first viable spherical neural weather model.",16,TEXT,"600")
    b+=T(64,628,"arXiv:2306.05420",14,ACCENT,"700")
    b+=T(232,628,"github.com/google-research/spherical-cnn",14,SEC,"600")
    # QR utility tiles (lower-right)
    if os.path.exists(QR_PAPER):
        b+=rect(1064,566,68,84,fill=WHITE,rx=8,sw=0)+image(1072,572,52,52,QR_PAPER)+T(1098,640,"Paper",11,TER,"700",anchor="middle")
    if os.path.exists(QR_CODE):
        b+=rect(1148,566,68,84,fill=WHITE,rx=8,sw=0)+image(1156,572,52,52,QR_CODE)+T(1182,640,"Code",11,TER,"700",anchor="middle")
    return svg(b)

# ---------- SLIDE 2: PROBLEM ----------
def s_problem():
    ch=chunks("problem"); b=header("Problem","Accurate on the sphere, but far too costly")
    # left definition card (c1)
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,404,392,fill=PANEL,stroke=STROKE)+
        rect(64,158,404,6,fill=ACCENT,rx=6,sw=0)+
        T(92,206,"The domain is the sphere",19,TEXT,"800")+
        para(92,244,"Spherical CNNs swap the plane for the sphere as the domain of the signal - exactly right for molecules and the atmosphere.",15.5,SEC,40,25)[0]+
        # sphere glyph
        circle(266,410,74,fill=PANEL2,stroke=ACCENT,sw=2)+
        line(192,410,340,410,ACCENT,1,dash="4 4")+
        f'<ellipse cx="266" cy="410" rx="74" ry="26" fill="none" stroke="{ACCENT}" stroke-width="1" opacity="0.6"/>'+
        f'<ellipse cx="266" cy="410" rx="30" ry="74" fill="none" stroke="{ACCENT}" stroke-width="1" opacity="0.45"/>'+
        T(266,506,"signal lives on S^2",13,TEAL,"700",anchor="middle"))
    # right flow (c2,c3,c4)
    fx=500; fw=716
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(fx,158,fw,116,fill=PANEL,stroke=STROKE)+
        T(fx+28,196,"1  ·  The core operation is expensive",17,ACCENT,"800")+
        para(fx+28,228,"Spherical convolution is most accurate in the spectral domain - far costlier than an ordinary planar convolution.",15,SEC,72,24)[0]+
        rect(fx+28,244,fw-56,26,fill=PANEL2,stroke=STROKE,rx=6)+
        T(fx+44,262,"spectral-domain convolution  >>  planar convolution   (cost)",13.5,GOLD,"700",ff=MONO))
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(fx,286,fw,104,fill=PANEL,stroke=STROKE)+
        T(fx+28,324,"2  ·  So the models stayed small",17,GOLD,"800")+
        para(fx+28,356,"That cost confined spherical CNNs to small, low-resolution problems with modest model capacity.",15,SEC,72,24)[0])
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(fx,402,fw,148,fill="#2A1720",stroke=RED,rx=14,sw=1.5)+
        rect(fx,402,6,148,fill=RED,rx=6,sw=0)+
        T(fx+28,440,"3  ·  No large-scale spherical architecture",17,RED,"800")+
        para(fx+28,472,"There was simply no spherical network analogous to the deep planar nets - VGG-19 scale - that power modern computer vision.",15,TEXT,72,24)[0]+
        T(fx+28,534,"spherical CNNs  <<  VGG-19-scale planar CNNs",15,RED,"800",ff=MONO))
    return svg(b)

# ---------- SLIDE 3: MOTIVATION ----------
def s_motivation():
    ch=chunks("motivation"); b=header("Motivation","Spherical science problems demand scale")
    # c1 full-width headline
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,1152,88,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,88,fill=TEAL,rx=6,sw=0)+
        T(92,196,"Two motivating problems",15,TEAL,"800",ls="1.5")+
        T(92,226,"Molecular property prediction and weather forecasting are both intrinsically spherical and tied to rotations.",17,TEXT,"600"))
    # c2 molecule/earth glyph card
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,266,560,150,fill=PANEL,stroke=STROKE)+
        rect(64,266,6,150,fill=ACCENT,rx=6,sw=0)+
        T(92,304,"Rotations everywhere",17,ACCENT,"800")+
        para(92,336,"A molecule's properties don't change when you rotate it; the Earth's atmosphere is naturally a signal on a sphere.",14.5,SEC,50,23)[0]+
        # rotation glyph
        circle(150,392,8,fill=TEAL)+circle(190,376,8,fill=ACCENT)+circle(215,404,8,fill=GOLD)+
        line(150,392,190,376,STROKE,2)+line(190,376,215,404,STROKE,2)+
        T(250,398,"rotation-invariant properties",12.5,TER,"600"))
    # c3 perfect match but large
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(648,266,568,150,fill=PANEL,stroke=STROKE)+
        rect(648,266,6,150,fill=GOLD,rx=6,sw=0)+
        T(676,304,"A perfect match - at a price",17,GOLD,"800")+
        para(676,336,"Rotation-equivariant spherical CNNs should excel here. But the standard benchmarks are large and high-resolution.",14.5,SEC,52,23)[0]+
        T(676,400,"equivariance  +  scale  =  the real challenge",14,TEAL,"700",ff=MONO))
    # c4 QM9 scale stat, full width
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(64,436,1152,114,fill=PANEL,stroke=STROKE)+
        rect(64,436,6,114,fill=ACCENT,rx=6,sw=0)+
        T(92,472,"The benchmarks earlier spherical CNNs could not touch",16,TEXT,"800")+
        _statpill(92,490,"QM9","134,000 molecules",ACCENT)+
        _statpill(392,490,"18x bigger","than QM7 (7,165)",GOLD)+
        _statpill(692,490,"ERA5 weather","high-resolution grids",TEAL)+
        T(1000,516,"-> the models had to scale",14,SEC,"700"))
    return svg(b)

def _statpill(x,y,big,sub,col):
    return (rect(x,y,272,44,fill=PANEL2,stroke=STROKE,rx=10)+
            rect(x,y,5,44,fill=col,rx=2,sw=0)+
            T(x+20,y+21,big,15,col,"800")+T(x+20,y+38,sub,12.5,SEC,"600"))

# ---------- SLIDE 4: CONTRIBUTION ----------
def s_contribution():
    ch=chunks("contribution"); b=header("Contribution","A recipe to scale spherical CNNs 10x")
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,1152,66,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,66,fill=ACCENT,rx=6,sw=0)+
        T(92,199,"A systematic approach to scale spherical CNNs one order of magnitude larger - in three parts.",17,TEXT,"600"))
    cards=[
        (ch[1],ACCENT,"1","Fast transforms on TPUs","An efficient JAX implementation of spin-weighted spherical harmonic transforms, tuned to run fast and distributed across TPUs."),
        (ch[2],TEAL,"2","New layers and inputs","New general-purpose layers and activations for expressivity and efficiency, plus application-specific input representations for molecules and weather."),
        (ch[3],GOLD,"3","Redesign, don't just enlarge","A key finding: naive scaling - just adding depth and width - is not enough. The core components themselves had to be redesigned."),
    ]
    cw=368; gap=24; x0=64; cy=250
    for i,(c,col,num,ti,tx) in enumerate(cards):
        x=x0+i*(cw+gap)
        body=(rect(x,cy,cw,300,fill=PANEL,stroke=STROKE)+
              rect(x,cy,cw,6,fill=col,rx=6,sw=0)+
              circle(x+52,cy+66,27,fill="none",stroke=col,sw=2.5)+
              T(x+52,cy+76,num,30,col,"800",anchor="middle"))
        yy=cy+128
        for j,ln in enumerate(wrap(ti,24)):
            body+=T(x+28,yy+j*28,ln,19,TEXT,"800")
        yy+=28*len(wrap(ti,24))+10
        body+=para(x+28,yy,tx,15,SEC,40,25)[0]
        b+=anchor(c["aid"],c["kw"],body)
    return svg(b)

# ---------- SLIDE 5: METHOD ----------
def s_method():
    ch=chunks("method"); b=header("Method","New spectral-domain components")
    gx=[64,648]; gy=[158,362]; cw=568; chh=192
    # c1 spectral components
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(gx[0],gy[0],cw,chh,fill=PANEL,stroke=STROKE)+
        rect(gx[0],gy[0],6,chh,fill=ACCENT,rx=6,sw=0)+
        T(gx[0]+28,gy[0]+38,"Everything lives in spectral space",16.5,ACCENT,"800")+
        para(gx[0]+28,gy[0]+68,"Building on spin-weighted spherical CNNs, the centerpiece is a set of new components that all operate in the spectral domain.",14.5,SEC,58,22)[0]+
        chip(gx[0]+28,gy[0]+128,cw-56,"spin-weighted spherical harmonic transform",ACCENT,h=40,size=14))
    # c2 phase collapse + eqn
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(gx[1],gy[0],cw,chh,fill=PANEL,stroke=STROKE)+
        rect(gx[1],gy[0],6,chh,fill=TEAL,rx=6,sw=0)+
        T(gx[1]+28,gy[0]+38,"Phase collapse nonlinearity",16.5,TEAL,"800")+
        para(gx[1]+28,gy[0]+68,"Take the modulus to collapse phase - restoring rotation invariance while losing no information in the nonzero spins.",14.5,SEC,58,22)[0]+
        rect(gx[1]+28,gy[0]+128,cw-56,42,fill=PANEL2,stroke=STROKE,rx=8)+
        T(gx[1]+cw/2,gy[0]+155,"x0  <-  W1 x0  +  W2 |x|  +  b",17,TEXT,"800",anchor="middle",ff=MONO))
    # c3 spectral BN + pool + residual
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(gx[0],gy[1],cw,chh,fill=PANEL,stroke=STROKE)+
        rect(gx[0],gy[1],6,chh,fill=GOLD,rx=6,sw=0)+
        T(gx[0]+28,gy[1]+38,"Norm, pool and residual - all spectral",16.5,GOLD,"800")+
        chip(gx[0]+28,gy[1]+58,cw-56,"Spectral batch normalization",ACCENT,h=34)+
        chip(gx[0]+28,gy[1]+100,cw-56,"Spectral pooling",TEAL,h=34)+
        chip(gx[0]+28,gy[1]+142,cw-56,"Residual skip between Fourier coefficients",GOLD,h=34))
    # c4 DFT-as-matmul
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(gx[1],gy[1],cw,chh,fill=PANEL,stroke=STROKE)+
        rect(gx[1],gy[1],6,chh,fill=RED,rx=6,sw=0)+
        T(gx[1]+28,gy[1]+38,"DFT as dense matmul, not FFT",16.5,RED,"800")+
        para(gx[1]+28,gy[1]+68,"Compute Fourier transforms as dense matrix multiplications: on TPUs matmul is extremely fast, while memory reshuffling is the bottleneck.",14,SEC,60,22)[0]+
        rect(gx[1]+28,gy[1]+142,cw-56,38,fill=PANEL2,stroke=STROKE,rx=8)+
        T(gx[1]+cw/2,gy[1]+167,"FFT reshuffle  ->  matmul on TPU",15,TEXT,"800",anchor="middle",ff=MONO))
    return svg(b)

# ---------- SLIDE 6: DATASET ----------
def s_dataset():
    ch=chunks("dataset-benchmark"); b=header("Dataset / Benchmark","Two very different spherical domains")
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,1152,64,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,64,fill=ACCENT,rx=6,sw=0)+
        T(92,197,"The experiments span two very different domains: small molecules and the global atmosphere.",16.5,TEXT,"600"))
    # c2 QM9 card
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,244,560,306,fill=PANEL,stroke=STROKE)+
        rect(64,244,6,306,fill=ACCENT,rx=6,sw=0)+
        T(92,286,"QM9  ·  molecular property regression",17,ACCENT,"800")+
        para(92,320,"Small organic molecules, each mapped onto the sphere for rotation-equivariant regression.",14.5,SEC,54,22)[0]+
        _kpi(92,362,"134K","molecules",ACCENT)+_kpi(272,362,"<=29","atoms each",TEAL)+_kpi(452,362,"12","regression targets",GOLD)+
        rect(92,478,504,48,fill=PANEL2,stroke=STROKE,rx=8)+
        T(112,507,"targets: energetic  ·  electronic  ·  thermodynamic properties",14,SEC,"600"))
    # c3 weather card
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,244,560,306,fill=PANEL,stroke=STROKE)+
        rect(656,244,6,306,fill=TEAL,rx=6,sw=0)+
        T(684,286,"WeatherBench / ERA5  ·  forecasting",17,TEAL,"800")+
        para(684,320,"Models train on ERA5 reanalysis data through the WeatherBench benchmark.",14.5,SEC,54,22)[0]+
        chip(684,372,504,"Geopotential Z500 and temperature T850, T2M",ACCENT,h=36,size=13.5)+
        chip(684,416,504,"3- and 5-day horizons, out to 28 days",TEAL,h=36,size=13.5)+
        chip(684,460,504,"Iterative high-resolution forecasting",GOLD,h=36,size=13.5)+
        T(684,522,"from short-range nowcasts to long-range global forecasts",13.5,TER,"600"))
    return svg(b)

def _kpi(x,y,num,lbl,col):
    return (rect(x,y,168,100,fill=PANEL2,stroke=STROKE,rx=12)+
            T(x+84,y+54,num,30,col,"800",anchor="middle")+
            T(x+84,y+82,lbl,12.5,SEC,"600",anchor="middle"))

# ---------- SLIDE 7: KEY RESULT ----------
def s_result():
    ch=chunks("key-result"); b=header("Key Result","State of the art on molecules and weather")
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,150,1152,50,fill=PANEL,stroke=STROKE)+
        rect(64,150,6,50,fill=GREEN,rx=6,sw=0)+
        T(92,182,"The scaled spherical CNN is strong on both fronts - molecular regression and weather forecasting.",16.5,TEXT,"700"))
    # c2 QM9 card
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,214,560,336,fill=PANEL,stroke=STROKE)+
        rect(64,214,6,336,fill=ACCENT,rx=6,sw=0)+
        T(92,250,"QM9  ·  molecular regression",16.5,ACCENT,"800")+
        para(92,282,"Reaches state of the art, beating the previously dominant graph neural nets and transformers.",14,SEC,56,21)[0]+
        _kpi(92,326,"8 / 12","targets, Split 1",GREEN)+_kpi(272,326,"9 / 12","targets, Split 2",GREEN)+
        T(534,354,"SOTA",24,GREEN,"800",anchor="middle")+T(534,378,"vs GNNs &",12.5,SEC,"600",anchor="middle")+T(534,396,"transformers",12.5,SEC,"600",anchor="middle")+
        T(92,464,"State-of-the-art targets (higher is better)",13.5,SEC,"700")+
        bar(240,480,300,9,12,GREEN,"Split 2","9 / 12",h=22)+
        bar(240,512,300,8,12,ACCENT,"Split 1","8 / 12",h=22))
    # c3 weather card
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,214,560,336,fill=PANEL,stroke=STROKE)+
        rect(656,214,6,336,fill=TEAL,rx=6,sw=0)+
        T(684,250,"WeatherBench  ·  forecasting",16.5,TEAL,"800")+
        para(684,282,"Beats the WeatherBench baseline on every metric in the simpler two-predictor setting.",14,SEC,56,21)[0]+
        chip(684,330,504,"Outperforms baseline on ALL 2-predictor metrics",GREEN,h=40,size=14)+
        chip(684,382,504,"Beats simulation-pretrained models on temperature",ACCENT,h=40,size=14)+
        rect(684,442,504,50,fill="#0F2E2B",stroke=TEAL,rx=10,sw=1.5)+
        T(700,472,"First viable spherical neural weather model",15,TEAL,"800")+
        T(684,524,"even rivaling models trained on large simulated datasets",13.5,TER,"600"))
    # c4 headline strip
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(64,564,1152,116,fill="#0F2E2B",stroke=TEAL,rx=14,sw=1.5)+
        rect(64,564,6,116,fill=TEAL,rx=6,sw=0)+
        T(92,600,"A first for the field",16,TEAL,"800")+
        para(92,632,"This is the first demonstration that spherical CNNs are viable neural weather models - a domain long dominated by other architectures.",15,TEXT,116,24)[0])
    return svg(b)

# ---------- SLIDE 8: ABLATION ----------
def s_ablation():
    ch=chunks("ablation-study"); b=header("Ablation Study","Each redesigned component earns its place")
    # c1 setup note (top full width)
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,1152,58,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,58,fill=ACCENT,rx=6,sw=0)+
        T(92,193,"A careful ablation isolates the effect of each change on a QM9 model - error and speed together.",16.5,TEXT,"600"))
    # c2 waterfall chart (left)
    cx=64; cw=680
    body=(rect(cx,238,cw,312,fill=PANEL,stroke=STROKE)+
          rect(cx,238,6,312,fill=TEAL,rx=6,sw=0)+
          T(cx+28,276,"Cumulative RMSE reduction (from the JAX baseline)",16,TEXT,"800"))
    steps=[("JAX baseline",0.0,SEC),("+ Phase collapse",8.0,ACCENT),
           ("+ Spectral batch-norm",9.4,TEAL),("+ Efficient residual",11.8,GOLD)]
    bx=cx+220; bw=420; y0=316; rowh=52; vmax=13.0
    for i,(lbl,val,col) in enumerate(steps):
        yy=y0+i*rowh
        w=max(3,int(bw*val/vmax))
        body+=T(cx+40,yy+22,lbl,14,TEXT,"700")
        body+=rect(bx,yy+4,bw,30,fill="#0E2334",stroke=STROKE,rx=6,sw=1)
        body+=rect(bx,yy+4,w,30,fill=col,rx=6,sw=0)
        body+=T(bx+w+12,yy+25,("baseline" if val==0 else f"-{val:.1f}%"),14,col,"800")
    body+=T(cx+40,y0+4*rowh+22,"all while improving training speed",13.5,GREEN,"700")
    b+=anchor(ch[0 if False else 1]["aid"],ch[1]["kw"],body)
    # c3 comparison / enthalpy (right)
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(764,238,452,312,fill=PANEL,stroke=STROKE)+
        rect(764,238,6,312,fill=GOLD,rx=6,sw=0)+
        T(792,276,"Beats prior alternatives",16,GOLD,"800")+
        para(792,308,"A separate comparison confirms each new piece beats earlier work.",14,SEC,44,22)[0]+
        chip(792,352,396,"Phase collapse  >  prior nonlinearity",ACCENT,h=34,size=13.5)+
        chip(792,392,396,"Spectral pooling  >  prior pooling",TEAL,h=34,size=13.5)+
        chip(792,432,396,"Spherical molecule rep  >  prior input",GREEN,h=34,size=13.5)+
        rect(792,480,396,50,fill=PANEL2,stroke=GOLD,rx=10,sw=1.5)+
        T(812,504,"QM9 enthalpy MAE",13.5,SEC,"600")+T(1168,504,"15.25 meV",18,GOLD,"800",anchor="end")+
        T(812,522,"driven down together by the new components",12,TER,"600"))
    return svg(b)

# ---------- SLIDE 9: HEADLINE NUMBERS ----------
def s_headline():
    ch=chunks("headline-numbers"); b=header("Headline Numbers","The impact in four numbers")
    cw=560; ch_h=176; gx=[64,656]; gy=[168,360]
    tiles=[
        (ch[0],ACCENT,"10x","order of magnitude","Scaled up in both operations and feature resolution versus prior spherical CNNs."),
        (ch[1],GREEN,"8/12 · 9/12","QM9 state-of-the-art targets","SOTA on 8 of 12 targets in Split 1 and 9 of 12 in Split 2."),
        (ch[2],TEAL,"3x -> 100x","faster","About 3x faster than the original in JAX; up to 100x on 32 TPUs, distributed."),
        (ch[3],GOLD,"-8.0%","QM9 error","The phase collapse nonlinearity alone reduces QM9 error by eight percent."),
    ]
    for i,(c,col,num,lbl,tx) in enumerate(tiles):
        x=gx[i%2]; y=gy[i//2]
        body=(rect(x,y,cw,ch_h,fill=PANEL,stroke=STROKE)+
              rect(x,y,6,ch_h,fill=col,rx=6,sw=0)+
              T(x+30,y+78,num,44,col,"800")+
              T(x+30,y+112,lbl,17,TEXT,"800"))
        body+=para(x+30,y+142,tx,14.5,SEC,64,22)[0]
        b+=anchor(c["aid"],c["kw"],body)
    return svg(b)

# ---------- SLIDE 10: TAKEAWAY ----------
def s_takeaway():
    ch=chunks("takeaway"); b=header("Takeaway","Not limited - just poorly scaled")
    cards=[
        (ch[0],ACCENT,"Never fundamentally limited","Spherical CNNs were not held back by any inherent ceiling - they were simply poorly scaled."),
        (ch[1],TEAL,"Redesign plus hardware-tuning","Redesigning the nonlinearity, normalization and residual block, plus an implementation tuned to modern accelerators, lets them finally scale - state of the art on molecular property prediction and genuinely competitive as neural weather models."),
        (ch[2],GREEN,"An open platform","The authors release their JAX implementation as a platform for further research on spherical data."),
    ]
    y=168
    for c,col,ti,tx in cards:
        lines=wrap(tx,92)
        hh=64+len(lines)*24
        body=(rect(64,y,1152,hh,fill=PANEL,stroke=STROKE)+
              rect(64,y,6,hh,fill=col,rx=6,sw=0)+
              circle(112,y+hh/2,10,fill=col)+
              T(150,y+40,ti,19,TEXT,"800"))
        body+=para(150,y+70,tx,15.5,SEC,92,24)[0]
        b+=anchor(c["aid"],c["kw"],body)
        y+=hh+18
    b+=line(64,y+6,1216,y+6,STROKE,1)
    b+=T(64,y+40,"Scaling Spherical CNNs",16,TEXT,"700")
    b+=T(64,y+66,"ICML 2023  ·  arXiv:2306.05420  ·  github.com/google-research/spherical-cnn",13.5,SEC,"600")
    return svg(b)

SLIDES=[("01_title",s_title),("02_problem",s_problem),("03_motivation",s_motivation),
        ("04_contribution",s_contribution),("05_method",s_method),("06_dataset",s_dataset),
        ("07_key_result",s_result),("08_ablation",s_ablation),("09_headline_numbers",s_headline),
        ("10_takeaway",s_takeaway)]

for name,fn in SLIDES:
    open(os.path.join(OUT,name+".svg"),"w").write(fn())
    print("wrote",name)
print("DONE",len(SLIDES))
