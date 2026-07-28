#!/usr/bin/env python3
"""All-native SVG deck builder for paper2video run 038 (Color Equivariant Convolutional Networks).
Reads _anchor_map.json; wraps each narration chunk in its own <g id="cue_..."> card with a
<title> holding the cue keywords, so the strict --require-pptx-anchors cue pass resolves every
anchor from PPTX geometry. Zero <image>, zero gradients, ASCII mono equations only.
Theme motif: a strip of DISCRETE hue swatches = the group H_n of discrete hue rotations."""
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
# discrete hue palette used for the H_n motif (n=7 chips)
HUES=["#F2685C","#F2A24E","#F2C14E","#48C78E","#34D3C0","#4C9BE8","#9B7BE8"]

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

def bar(x,y,w,val,vmax,color,label,valtxt,lblcolor=SEC,h=26):
    bw=max(2,int(w*val/vmax))
    return (rect(x,y,w,h,fill="#0E2334",stroke=STROKE,rx=6,sw=1)+
            rect(x,y,bw,h,fill=color,rx=6,sw=0)+
            T(x-12,y+h*0.70+2,label,14,lblcolor,"600",anchor="end")+
            T(x+bw+10,y+h*0.70+2,valtxt,14,color,"800"))

def stat(x,y,w,h,num,lbl,col):
    """Robust numeric tile: number + label always inside the box for any h>=64."""
    ns=min(32,h*0.34)
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

def hueswatch(x,y,n=7,sz=26,gap=10,r=6):
    """Discrete hue chips = the group H_n of discrete hue rotations."""
    out=""
    for i in range(n):
        out+=rect(x+i*(sz+gap),y,sz,sz,fill=HUES[i%len(HUES)],rx=r,sw=0)
    return out

# ---------- SLIDE 1: TITLE ----------
def s_title():
    ch=chunks("title"); b=""
    b+=T(64,72,"NeurIPS 2023",14,ACCENT,"800",ls="3")
    b+=T(1216,72,"Computer Vision Lab  ·  Delft University of Technology",14,SEC,"600",anchor="end")
    b+=line(64,88,1216,88,STROKE,1)
    b+=T(64,152,"Color Equivariant",44,WHITE,"800")
    b+=T(64,200,"Convolutional Networks",44,ACCENT,"800")
    b+=hueswatch(690,168,7,30,12,7)
    b+=T(64,240,"Lengyel  ·  Strafforello  ·  Bruintjes  ·  Gielisse  ·  van Gemert     —   TU Delft, Computer Vision Lab",15.5,SEC,"500")
    # three concept cards in a row = anchors
    cw=373; gap=17; x0=64; cy=290; chh=250
    data=[
        (ch[0],RED,x0,"Color: a cue and a liability",
         "CNNs readily exploit color for object recognition, but it becomes a liability when test-time colors differ from those seen in training."),
        (ch[1],TEAL,x0+cw+gap,"Color Equivariant Convolutions",
         "A new building block, CEConv, that shares shape features across the color spectrum while preserving discriminative color information."),
        (ch[2],ACCENT,x0+2*(cw+gap),"Parameter sharing over hue",
         "By hard-wiring sharing over discrete hue shifts, CEConvs let ResNets generalize to rare colors and stay robust, without discarding color."),
    ]
    for c,col,x,ti,tx in data:
        body=(rect(x,cy,cw,chh,fill=PANEL,stroke=STROKE)+
              rect(x,cy,cw,6,fill=col,rx=6,sw=0)+
              hueswatch(x+26,cy+34,5,18,8,5)+
              para(x+26,cy+94,ti,18.5,TEXT,80,24,"800")[0])
        body+=para(x+26,cy+146,tx,14,SEC,42,21)[0]
        b+=anchor(c["aid"],c["kw"],body)
    b+=line(64,570,1216,570,STROKE,1)
    b+=T(64,606,"arXiv:2310.19368",14,ACCENT,"700")
    b+=T(280,606,"github.com/Attila94/CEConv",14,SEC,"600")
    b+=T(1216,606,"Share shape across colors — keep color in its own dimension.",14,SEC,"600",anchor="end")
    return svg(b)

# ---------- SLIDE 2: PROBLEM ----------
def s_problem():
    ch=chunks("problem"); b=header("Problem","Networks rely on color, yet colors shift")
    # c1 left tall: CNNs lean on color
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,404,392,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,392,fill=ACCENT,rx=6,sw=0)+
        T(92,202,"CNNs lean heavily on color",18,TEXT,"800")+
        para(92,240,"Convolutional networks use color as a strong cue to recognize objects, but real-world data rarely contains every color a class can take.",14.5,SEC,42,23)[0]+
        rect(92,352,344,140,fill=PANEL2,stroke=STROKE,rx=10)+
        T(112,382,"Training colors seen",13,TER,"700")+
        hueswatch(112,398,5,30,14,7)+
        T(112,470,"Test colors can be anything",13,GOLD,"700"))
    # right column, three stacked
    fx=500; fw=716
    # c2 red car -> blue car collapse
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(fx,158,fw,150,fill=PANEL,stroke=STROKE)+
        rect(fx,158,6,150,fill=RED,rx=6,sw=0)+
        T(fx+28,196,"Trained on red cars, tested on a blue one",16.5,RED,"800")+
        _car(fx+40,224,RED)+T(fx+118,300,"train",12.5,TER,"600",anchor="middle")+
        T(fx+190,268,"->",26,SEC,"800",anchor="middle")+
        _car(fx+236,224,ACCENT)+T(fx+314,300,"test",12.5,TER,"600",anchor="middle")+
        rect(fx+400,224,288,52,fill=PANEL2,stroke=STROKE,rx=10)+
        T(fx+544,248,"accuracy",12.5,SEC,"600",anchor="middle")+
        T(fx+544,270,"collapses",16,RED,"800",anchor="middle"))
    # c3 color invariance throws it away
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(fx,324,fw,104,fill=PANEL,stroke=STROKE)+
        rect(fx,324,6,104,fill=GOLD,rx=6,sw=0)+
        T(fx+28,362,"The classic remedy overshoots",16,GOLD,"800")+
        para(fx+28,392,"Color invariance sidesteps the issue by removing color entirely, throwing away a genuinely useful signal.",14.5,SEC,74,22)[0])
    # c4 the real challenge (callout)
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(fx,444,fw,106,fill="#0F2E2B",stroke=TEAL,rx=14,sw=1.5)+
        rect(fx,444,6,106,fill=TEAL,rx=6,sw=0)+
        T(fx+28,482,"The real challenge",16,TEAL,"800")+
        para(fx+28,512,"Keep color information while still generalizing across colors that were rare or absent during training.",14.5,TEXT,74,22)[0])
    return svg(b)

def _car(x,y,col):
    # tiny schematic car
    return (rect(x,y+22,148,30,fill=col,rx=8,sw=0)+
            rect(x+30,y+4,78,26,fill=col,rx=8,sw=0)+
            circle(x+34,y+54,13,fill="#0B1B2B",stroke=col,sw=3)+
            circle(x+114,y+54,13,fill="#0B1B2B",stroke=col,sw=3))

# ---------- SLIDE 3: MOTIVATION ----------
def s_motivation():
    ch=chunks("motivation"); b=header("Motivation","Color is a natural axis for equivariance")
    # c1 left: geometric equivariance worked
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,560,200,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,200,fill=ACCENT,rx=6,sw=0)+
        T(92,196,"Equivariance paid off for geometry",17,ACCENT,"800")+
        para(92,226,"Group equivariant convolutions share parameters across rotations and flips, dramatically improving data efficiency for geometric transformations.",14.5,SEC,58,22)[0]+
        _rotarrows(150,300,ACCENT)+_rotarrows(280,300,ACCENT)+_rotarrows(410,300,ACCENT)+
        T(510,314,"rotations, flips",13,TER,"600",anchor="middle"))
    # c2 left bottom: photometric left aside
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,374,560,176,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(64,374,6,176,fill=GOLD,rx=6,sw=0)+
        T(92,412,"Photometric changes were left aside",16,GOLD,"800")+
        para(92,442,"Hue shifts and other photometric transformations had gone largely unexplored, even as geometry got all the attention.",14.5,SEC,58,22)[0]+
        hueswatch(92,494,7,26,10,6))
    # c3 right top: color-selective neurons
    rx=648; rw=568
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(rx,158,rw,200,fill=PANEL,stroke=STROKE)+
        rect(rx,158,6,200,fill=TEAL,rx=6,sw=0)+
        T(rx+28,196,"Early CNN layers are color-selective",16.5,TEAL,"800")+
        para(rx+28,226,"Studies of trained CNNs show that early layers learn strongly color-selective neurons.",14.5,SEC,58,22)[0]+
        # mini neurons tinted by hue
        circle(rx+70,318,15,fill=HUES[0])+circle(rx+140,318,15,fill=HUES[2])+
        circle(rx+210,318,15,fill=HUES[3])+circle(rx+280,318,15,fill=HUES[5])+
        T(rx+360,324,"color-tuned filters",13,TER,"600"))
    # c4 right bottom: treat hue like a rotation (callout)
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(rx,374,rw,176,fill="#0F2E2B",stroke=TEAL,rx=14,sw=1.5)+
        rect(rx,374,6,176,fill=TEAL,rx=6,sw=0)+
        T(rx+28,412,"Treat a hue shift like a rotation",16,TEAL,"800")+
        para(rx+28,442,"Make hue a symmetry the network respects by design, rather than something it must relearn from data.",14.5,TEXT,58,22)[0]+
        T(rx+28,528,"rotation  ~=  hue shift",15,TEAL,"800",ff=MONO))
    return svg(b)

def _rotarrows(cx,cy,col):
    # small circular rotation glyph
    return (circle(cx,cy,20,fill="none",stroke=col,sw=2.5)+
            f'<path d="M {cx+18} {cy-6} L {cx+18} {cy-16} L {cx+8} {cy-16}" fill="none" stroke="{col}" stroke-width="2.5" stroke-linecap="round"/>')

# ---------- SLIDE 4: CONTRIBUTION ----------
def s_contribution():
    ch=chunks("contribution"); b=header("Contribution","One block, four properties")
    cards=[
        (ch[0],ACCENT,"1","Color Equivariant Convolution","A new layer that hard-wires parameter sharing over discrete hue shifts."),
        (ch[1],TEAL,"2","Shape shared, color kept","Shares shape across the color spectrum while keeping color in a dedicated group dimension of the feature map."),
        (ch[2],GOLD,"3","Drops into ResNet","Formulated in the language of symmetry groups, it slots into standard networks with no architectural surgery."),
        (ch[3],GREEN,"4","Validated toy and real","Controlled toy experiments and realistic benchmarks show better robustness, hand in hand with color augmentation."),
    ]
    cw=272; gap=24; x0=64; cy=180; chh=372
    for i,(c,col,num,ti,tx) in enumerate(cards):
        x=x0+i*(cw+gap)
        body=(rect(x,cy,cw,chh,fill=PANEL,stroke=STROKE)+
              rect(x,cy,cw,6,fill=col,rx=6,sw=0)+
              circle(x+50,cy+66,26,fill="none",stroke=col,sw=2.5)+
              T(x+50,cy+76,num,28,col,"800",anchor="middle"))
        yy=cy+134
        tlines=wrap(ti,17)
        for j,ln in enumerate(tlines):
            body+=T(x+24,yy+j*26,ln,17.5,TEXT,"800")
        yy+=26*len(tlines)+12
        body+=para(x+24,yy,tx,14,SEC,30,22)[0]
        b+=anchor(c["aid"],c["kw"],body)
    b+=T(64,586,"Exploit color and be robust to color — with one drop-in building block.",15.5,TEAL,"700")
    return svg(b)

# ---------- SLIDE 5: METHOD ----------
def s_method():
    ch=chunks("method"); b=header("Method","Hue shift as a rotation, shared by design")
    lx=64; lw=568
    # c1 hue shift = rotation about gray diagonal, group H_n
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(lx,158,lw,200,fill=PANEL,stroke=STROKE)+
        rect(lx,158,6,200,fill=ACCENT,rx=6,sw=0)+
        T(lx+28,196,"Hue shift = rotation about gray axis",16.5,ACCENT,"800")+
        para(lx+28,226,"In RGB space a hue shift is a rotation around the black-to-white diagonal. This is the group H-n of n discrete rotations about that axis.",14,SEC,52,21)[0]+
        eqbox(lx+28,314,lw-56,"H_n = { n rotations about [1,1,1] in RGB }",14))
    # c2 CEConv correlates hue-rotated filters (key eq)
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(lx,374,lw,176,fill="#0F2E2B",stroke=TEAL,rx=14,sw=1.5)+
        rect(lx,374,6,176,fill=TEAL,rx=6,sw=0)+
        T(lx+28,412,"Correlate hue-rotated filter copies",16,TEAL,"800")+
        para(lx+28,442,"Each filter is applied in every hue rotation, adding a group dimension k that indexes the hue rotation in the feature map.",14,SEC,58,21)[0]+
        eqbox(lx+28,502,lw-56,"[f * psi](x,k) = sum f_c(y) H_n(k) psi_c(y-x)",13.5))
    rxx=656; rw=560
    # c3 hidden layers: cyclic permutation
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(rxx,158,rw,200,fill=PANEL,stroke=STROKE)+
        rect(rxx,158,6,200,fill=GOLD,rx=6,sw=0)+
        T(rxx+28,196,"Hidden layers: cyclic permutation",16.5,GOLD,"800")+
        para(rxx+28,226,"Filters are cyclically permuted across the color dimension, so equivariance is preserved layer after layer throughout the network.",14,SEC,56,21)[0]+
        _cycperm(rxx+28,300,rw-56))
    # c4 filter decomposition + hybrids
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(rxx,374,rw,176,fill=PANEL,stroke=STROKE)+
        rect(rxx,374,6,176,fill=GREEN,rx=6,sw=0)+
        T(rxx+28,412,"Keep the cost in check",16,GREEN,"800")+
        para(rxx+28,442,"The extra dimension multiplies feature maps, so filters split into spatial and pointwise parts; hybrids use color equivariance only in early stages.",14,SEC,58,21)[0]+
        eqbox(rxx+28,502,rw-56,"MACs +|H_n|/k^2 + |H_n|   (small overhead)",13.5))
    return svg(b)

def _cycperm(x,y,w):
    # three hue chips with cyclic arrows
    out=""
    n=4; sz=30; gap=(w-8-n*sz)/(n-1)
    for i in range(n):
        cx=x+i*(sz+gap)
        out+=rect(cx,y,sz,sz,fill=HUES[i*2%len(HUES)],rx=6,sw=0)
        if i<n-1:
            mx=cx+sz+gap/2
            out+=T(mx,y+sz*0.72,"->",16,SEC,"800",anchor="middle")
    out+=T(x,y+sz+26,"color dimension k  ·  cyclic shift preserves equivariance",12.5,TER,"600")
    return out

# ---------- SLIDE 6: DATASET ----------
def s_dataset():
    ch=chunks("dataset-benchmark"); b=header("Dataset / Benchmark","Two scales, one robustness protocol")
    # c1 headline strip
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,1152,58,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,58,fill=ACCENT,rx=6,sw=0)+
        T(92,193,"The evaluation spans two scales: controlled synthetic toys and eight realistic image benchmarks.",16,TEXT,"600"))
    # c2 ColorMNIST toys
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,240,560,168,fill=PANEL,stroke=STROKE)+
        rect(64,240,6,168,fill=TEAL,rx=6,sw=0)+
        T(92,280,"Synthetic ColorMNIST",18,TEAL,"800")+
        para(92,312,"Two variants isolate the phenomenon under controlled color statistics.",14.5,SEC,58,21)[0]+
        chip(92,346,"Long-tailed  ·  30 classes, strong imbalance",TEAL,w=468,h=28)+
        chip(92,378,"Biased  ·  10 classes, tunable hue spread",GOLD,w=468,h=28))
    # c3 eight benchmarks
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,240,560,168,fill=PANEL,stroke=STROKE)+
        rect(656,240,6,168,fill=ACCENT,rx=6,sw=0)+
        T(684,280,"Eight natural-image benchmarks",17,ACCENT,"800")+
        para(684,312,"Realistic classification, ResNet-18 / ResNet-44 on a single A40 GPU.",14.5,SEC,60,21)[0]+
        chip(684,346,"CIFAR-10/100  ·  STL-10  ·  Flowers-102  ·  Pet",ACCENT,w=504,h=28)+
        chip(684,378,"Caltech-101  ·  Stanford Cars  ·  ImageNet",ACCENT,w=504,h=28))
    # c4 robustness protocol (callout)
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(64,428,1152,122,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(64,428,6,122,fill=GOLD,rx=6,sw=0)+
        T(92,466,"Robustness protocol: sweep the hue",17,GOLD,"800")+
        para(92,496,"Every test image is re-rendered under a gradual hue shift from -180 to +180 degrees, and accuracy is averaged across the full sweep.",14.5,TEXT,86,22)[0]+
        hueswatch(830,470,7,26,10,6))
    return svg(b)

# ---------- SLIDE 7: KEY RESULT ----------
def s_result():
    ch=chunks("key-result"); b=header("Key Result","Robust to hue shifts, free on clean data")
    # c1 headline strip
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,150,1152,50,fill=PANEL,stroke=STROKE)+
        rect(64,150,6,50,fill=GREEN,rx=6,sw=0)+
        T(92,182,"On original, unshifted test sets, color-equivariant ResNets match vanilla ResNets — no clean-accuracy cost.",16,TEXT,"700"))
    # c2 Flowers-102 bars (left)
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,214,560,264,fill=PANEL,stroke=STROKE)+
        rect(64,214,6,264,fill=TEAL,rx=6,sw=0)+
        T(92,250,"Flowers-102  ·  avg over hue shifts",16,TEAL,"800")+
        bar(300,286,250,13.41,40,RED,"vanilla ResNet","13.4%",h=32)+
        bar(300,340,250,33.33,40,GREEN,"CEConv","33.3%",h=32)+
        rect(92,398,504,60,fill="#0F2E2B",stroke=TEAL,rx=10,sw=1.5)+
        T(112,424,"Nearly 2.5x higher when the test hue shifts",14.5,TEAL,"800")+
        T(112,446,"...while clean accuracy stays on par",13,SEC,"600"))
    # c3 CIFAR-100 & Cars (right)
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,214,560,264,fill=PANEL,stroke=STROKE)+
        rect(656,214,6,264,fill=GOLD,rx=6,sw=0)+
        T(684,250,"Same story on harder sets",16,GOLD,"800")+
        bar(892,286,250,47.01,80,RED,"CIFAR-100 base","47.0%",h=28)+
        bar(892,330,250,62.11,80,GREEN,"CIFAR-100 CE","62.1%",h=28)+
        bar(892,382,250,55.59,80,RED,"Cars base","55.6%",h=28)+
        bar(892,426,250,68.17,80,ACCENT,"Cars CE","68.2%",h=28))
    # c4 long-tailed bottom strip
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(64,492,1152,116,fill=PANEL,stroke=STROKE)+
        rect(64,492,6,116,fill=ACCENT,rx=6,sw=0)+
        T(92,526,"Controlled long-tailed ColorMNIST",16,ACCENT,"800")+
        stat(900,506,150,88,"91.4%","CE network",GREEN)+
        stat(1058,506,150,88,"71.6%","vanilla CNN",RED)+
        para(92,556,"The equivariant network reaches 91% versus 72%, with the biggest gains exactly on the rare classes that shape sharing is meant to help.",14.5,SEC,54,22)[0])
    b+=T(64,648,"Biggest improvements land on the rare, underrepresented colors.",14,SEC,"600")
    return svg(b)

# ---------- SLIDE 8: ABLATION ----------
def s_ablation():
    ch=chunks("ablation-study"); b=header("Ablation Study","What makes it work")
    # c1 more rotations -> more robust (left top)
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,560,180,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,180,fill=ACCENT,rx=6,sw=0)+
        T(92,196,"More hue rotations -> more robust",16.5,ACCENT,"800")+
        para(92,226,"Increasing the number of discrete rotations raises test-time robustness, with a slight capacity cost as channels shrink to keep parameters fixed.",14.5,SEC,56,22)[0]+
        _uptrend(360,286,236,40)+T(92,312,"robustness ->",13,TER,"600"))
    # c2 coset pooling = invariance (left bottom)
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,354,560,196,fill="#0F2E2B",stroke=GREEN,rx=14,sw=1.5)+
        rect(64,354,6,196,fill=GREEN,rx=6,sw=0)+
        T(92,392,"Coset pooling drives invariance",16.5,GREEN,"800")+
        para(92,424,"Group coset pooling is the mechanism that yields hue invariance. Remove it, and the network behaves like a regular one.",14.5,TEXT,56,22)[0]+
        T(92,510,"no coset pool  =  ordinary CNN",14.5,GREEN,"800",ff=MONO))
    # c3 complements augmentation (right top)
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,158,560,180,fill=PANEL,stroke=STROKE)+
        rect(656,158,6,180,fill=GOLD,rx=6,sw=0)+
        T(684,196,"Complements color-jitter",16.5,GOLD,"800")+
        para(684,226,"Equivariance and color-jitter augmentation are complementary: an equivariant network needs a lower intensity of augmentation to reach the same robustness.",14.5,SEC,56,22)[0])
    # c4 color-selectivity explains when (right bottom)
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(656,354,560,196,fill=PANEL,stroke=STROKE)+
        rect(656,354,6,196,fill=TEAL,rx=6,sw=0)+
        T(684,392,"Color-selectivity predicts benefit",16.5,TEAL,"800")+
        para(684,424,"Datasets with more color-selective neurons benefit from equivariance up to later stages.",14.5,SEC,56,22)[0]+
        chip(684,494,"Flowers-102 color selectivity = 0.70  ->  big gains",TEAL,w=504,h=34))
    return svg(b)

def _uptrend(x,y,w,h):
    pts=[]
    for i in range(0,w+1,10):
        t=i/w; v=0.10+0.82*(1-math.exp(-2.6*t))
        pts.append((x+i,y+h-6-int(v*(h-12))))
    return (rect(x,y,w,h,fill="#0E2334",stroke=STROKE,rx=8)+
            poly(pts,stroke=ACCENT,sw=2.5)+
            T(x+w-8,y+h-6,"n rotations ->",10.5,TER,"600",anchor="end"))

# ---------- SLIDE 9: HEADLINE NUMBERS ----------
def s_headline():
    ch=chunks("headline-numbers"); b=header("Headline Numbers","The impact in one place")
    # c1 Flowers-102 nearly triples (big strip)
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,168,1152,150,fill=PANEL,stroke=STROKE)+
        rect(64,168,6,150,fill=GREEN,rx=6,sw=0)+
        T(92,206,"Flowers-102 under hue shifts  ·  accuracy nearly triples",16.5,GREEN,"800")+
        stat(92,226,220,80,"13.4%","vanilla ResNet",RED)+
        T(330,278,"->",30,SEC,"800",anchor="middle")+
        stat(360,226,220,80,"33.3%","CEConv",GREEN)+
        stat(612,226,230,80,"~2.5x","robustness gain",TEAL)+
        rect(864,226,352,80,fill=PANEL2,stroke=STROKE,rx=12)+
        para(884,256,"A large jump on hue-shifted tests, with clean accuracy unchanged.",13.5,SEC,44,20)[0])
    # c2 long-tailed (left)
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,334,560,174,fill="#0F2E2B",stroke=GREEN,rx=14,sw=1.5)+
        rect(64,334,6,174,fill=GREEN,rx=6,sw=0)+
        T(92,372,"Long-tailed color experiment",16.5,GREEN,"800")+
        stat(92,392,220,84,"91.4%","CE network",GREEN)+
        stat(360,392,220,84,"71.6%","vanilla CNN",RED)+
        T(92,498,"Almost +20 points over the baseline.",13.5,SEC,"600"))
    # c3 CIFAR-100 / Cars (right)
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,334,560,174,fill=PANEL,stroke=STROKE)+
        rect(656,334,6,174,fill=ACCENT,rx=6,sw=0)+
        T(684,372,"Hue-shifted gains on harder sets",16.5,ACCENT,"800")+
        stat(684,392,250,84,"+15.1","CIFAR-100 pts",ACCENT)+
        stat(962,392,250,84,"+12.6","Stanford Cars pts",TEAL)+
        T(684,498,"Consistent lifts on realistic benchmarks.",13.5,SEC,"600"))
    # c4 modest overhead (bottom strip)
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(64,524,1152,72,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(64,524,6,72,fill=GOLD,rx=6,sw=0)+
        T(92,554,"Modest compute overhead",15.5,GOLD,"800")+
        T(92,578,"Filter decomposition keeps the increase small.",13.5,SEC,"600")+
        eqbox(720,536,472,"MACs +|H_n|/k^2 + |H_n|   ·   params +|H_n|/k^2 + 1",13,h=48))
    return svg(b)

# ---------- SLIDE 10: TAKEAWAY ----------
def s_takeaway():
    ch=chunks("takeaway"); b=header("Takeaway","Give color the equivariance it deserves")
    cards=[
        (ch[0],ACCENT,"Color deserves equivariance too","Hue shifts deserve the same equivariance treatment that rotations and translations have long enjoyed."),
        (ch[1],TEAL,"Do both, not either","Instead of choosing between exploiting color and being robust to color change, CEConvs share shape across the spectrum while keeping color in its own dimension."),
        (ch[2],GREEN,"Practical and plug-in","The block drops into standard architectures, plays well with augmentation, and delivers its largest gains precisely where color matters most."),
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
    b+=hueswatch(64,614,7,22,10,5)
    b+=T(1216,632,"Color Equivariant Convolutional Networks  ·  NeurIPS 2023  ·  arXiv:2310.19368",14,SEC,"600",anchor="end")
    return svg(b)

SLIDES=[("01_title",s_title),("02_problem",s_problem),("03_motivation",s_motivation),
        ("04_contribution",s_contribution),("05_method",s_method),("06_dataset",s_dataset),
        ("07_key_result",s_result),("08_ablation",s_ablation),("09_headline",s_headline),
        ("10_takeaway",s_takeaway)]

for name,fn in SLIDES:
    open(os.path.join(OUT,name+".svg"),"w").write(fn())
    print("wrote",name)
print("DONE",len(SLIDES))
