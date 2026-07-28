#!/usr/bin/env python3
"""All-native SVG deck builder for paper2video run 030 (FoRDE / ICLR 2024).
Reads _anchor_map.json; wraps each narration chunk in its own <g id="cue_..."> card
with a <title> holding the cue keywords, so the strict --require-pptx-anchors cue
pass resolves every anchor from PPTX geometry."""
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

def kpi(x,y,w,num,lbl,col,nsize=34,h=104):
    return (rect(x,y,w,h,fill=PANEL2,stroke=STROKE,rx=12)+
            T(x+w/2,y+h*0.52,num,nsize,col,"800",anchor="middle")+
            T(x+w/2,y+h*0.80,lbl,13,SEC,"600",anchor="middle"))

def chip(x,y,w,text,col,h=34,sz=14.5):
    return (rect(x,y,w,h,fill=PANEL2,stroke=STROKE,rx=8)+
            circle(x+18,y+h/2,5,fill=col)+
            T(x+34,y+h/2+5,text,sz,TEXT,"600"))

# ---------- SLIDE 1: TITLE ----------
def s_title():
    ch=chunks("title"); b=""
    b+=T(64,72,"ICLR 2024",14,ACCENT,"800",ls="3")
    b+=T(1216,72,"Aalto · Helsinki · Manchester",14,SEC,"600",anchor="end")
    b+=line(64,88,1216,88,STROKE,1)
    b+=T(64,158,"Input-Gradient Space Particle Inference",40,WHITE,"800")
    b+=T(64,206,"for Neural Network Ensembles",40,ACCENT,"800")
    b+=rect(64,232,150,30,fill="#0F2E2B",stroke=TEAL,rx=15,sw=1.5)+T(139,252,"FoRDE",17,TEAL,"800",anchor="middle")
    b+=T(232,252,"First-order Repulsive Deep Ensembles",17,SEC,"600")
    b+=T(64,290,"Trung Trinh · Markus Heinonen · Luigi Acerbi · Samuel Kaski",15,TER,"500")
    # four concept cards
    cy=316; cw=274; gap=18; cx=64
    data=[
        (ch[0],ACCENT,"The method","FoRDE trains an ensemble by repelling members in the space of their input gradients."),
        (ch[1],GOLD,"Why it's new","Weight-space and function-space repulsion had failed to beat plain deep ensembles."),
        (ch[2],TEAL,"Why it works","Input gradients characterize a function up to translation, and are far smaller than weights."),
        (ch[3],GREEN,"The payoff","A markedly more robust and better-calibrated ensemble under input corruptions."),
    ]
    for i,(c,col,ti,tx) in enumerate(data):
        x=cx+i*(cw+gap)
        body=(rect(x,cy,cw,210,fill=PANEL,stroke=STROKE)+
              rect(x,cy,cw,6,fill=col,rx=6,sw=0)+
              circle(x+28,cy+46,7,fill=col)+
              T(x+46,cy+52,ti,17,TEXT,"800"))
        body+=para(x+22,cy+92,tx,14,SEC,32,23)[0]
        b+=anchor(c["aid"],c["kw"],body)
    b+=line(64,566,1216,566,STROKE,1)
    b+=T(64,602,"arXiv:2306.02775",14,ACCENT,"700")
    b+=T(280,602,"github.com/AaltoPML/FoRDE",14,SEC,"600")
    b+=T(1216,602,"Repel where it matters: input-gradient space",14,TEAL,"700",anchor="end")
    return svg(b)

# ---------- SLIDE 2: PROBLEM ----------
def s_problem():
    ch=chunks("problem"); b=header("Problem","Where you repel members matters")
    # c1 top full-width
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,152,1152,96,fill=PANEL,stroke=STROKE)+
        rect(64,152,6,96,fill=ACCENT,rx=6,sw=0)+
        T(92,188,"Particle-based inference makes diversity explicit",16.5,ACCENT,"800")+
        para(92,218,"Ensemble members capture different explanations of the data; a repulsion term pushes particles apart. But the space you repel in decides whether it helps.",15,SEC,96,24)[0])
    # c2 weight space (left)  c3 function space (right) -- both failure modes
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,268,560,192,fill="#2A1720",stroke=RED,rx=14,sw=1.5)+
        rect(64,268,6,192,fill=RED,rx=6,sw=0)+
        T(92,306,"Weight space  ✗",17,RED,"800")+
        T(92,336,"wasteful",14,GOLD,"700")+
        para(92,364,"Networks are heavily over-parameterized, so many different weight vectors encode the very same function. Repelling weights mostly moves redundant coordinates.",14.5,TEXT,58,23)[0])
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,268,560,192,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(656,268,6,192,fill=GOLD,rx=6,sw=0)+
        T(684,306,"Function space  ✗",17,GOLD,"800")+
        T(684,336,"intractable",14,GOLD,"700")+
        para(684,364,"Comparing whole functions is computationally hard; the shortcuts in prior work compared outputs only on training inputs and led to underfitting.",14.5,TEXT,58,23)[0])
    # c4 bottom band -- neither works
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(64,478,1152,72,fill=PANEL,stroke=STROKE)+
        rect(64,478,6,72,fill=SEC,rx=6,sw=0)+
        T(92,510,"The gap",14,TER,"800",ls="1.5")+
        T(92,536,"Neither weight-space nor function-space repulsion delivered meaningful gains over standard deep ensembles.",16,TEXT,"600"))
    return svg(b)

# ---------- SLIDE 3: MOTIVATION ----------
def s_motivation():
    ch=chunks("motivation"); b=header("Motivation","A third view: input gradients")
    # c1 top band -- the third representation
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,152,1152,120,fill=PANEL,stroke=STROKE)+
        rect(64,152,6,120,fill=TEAL,rx=6,sw=0)+
        T(92,186,"Represent a network a third way",15,TEAL,"800",ls="1")+
        para(92,214,"Beyond its weights and its function values, a model is characterized up to a translation by its first-order input gradients — the derivatives of the output with respect to the input.",15,TEXT,98,24)[0]+
        T(92,262,"grad_x f(x)   —  derivative of the output w.r.t. the input",13.5,ACCENT,"700",ff=MONO))
    # three property cards
    cw=368; gap=24; x0=64; cy=290; chh=260
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(x0,cy,cw,chh,fill=PANEL,stroke=STROKE)+
        rect(x0,cy,cw,6,fill=ACCENT,rx=6,sw=0)+
        T(x0+28,cy+42,"Property 1  ·  compact",16.5,ACCENT,"800")+
        para(x0+28,cy+72,"Input gradients are the same size as the input — far smaller than the enormous weight vector — so they are cheap to compare with a kernel.",14.5,SEC,40,23)[0]+
        # size comparison bars
        T(x0+28,cy+186,"size to compare",12.5,TER,"700")+
        rect(x0+28,cy+198,312,20,fill="#0E2334",stroke=STROKE,rx=5,sw=1)+rect(x0+28,cy+198,312,20,fill=RED,rx=5,sw=0)+T(x0+40,cy+213,"weights",12,WHITE,"800")+
        rect(x0+28,cy+226,44,20,fill=ACCENT,rx=5,sw=0)+T(x0+80,cy+241,"input gradient",12,SEC,"700"))
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(x0+cw+gap,cy,cw,chh,fill=PANEL,stroke=STROKE)+
        rect(x0+cw+gap,cy,cw,6,fill=TEAL,rx=6,sw=0)+
        T(x0+cw+gap+28,cy+42,"Property 2  ·  distinct features",16.5,TEAL,"800")+
        para(x0+cw+gap+28,cy+72,"Forcing members to have different input gradients forces them to depend on different input features of the data.",14.5,SEC,40,23)[0]+
        chip(x0+cw+gap+28,cy+168,cw-56,"Member A  →  features {edges}",ACCENT,32,13.5)+
        chip(x0+cw+gap+28,cy+208,cw-56,"Member B  →  features {texture}",TEAL,32,13.5))
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(x0+2*(cw+gap),cy,cw,chh,fill="#0F2E2B",stroke=TEAL,rx=14,sw=1.5)+
        rect(x0+2*(cw+gap),cy,cw,6,fill=GREEN,rx=6,sw=0)+
        T(x0+2*(cw+gap)+28,cy+42,"The intuition  ·  robustness",16.5,GREEN,"800")+
        para(x0+2*(cw+gap)+28,cy+72,"If members react to complementary patterns, corrupting one pattern will not fool all of them at once — the ensemble stays reliable.",14.5,TEXT,40,23)[0]+
        T(x0+2*(cw+gap)+28,cy+206,"corrupt one feature  →",13,TER,"700")+
        T(x0+2*(cw+gap)+28,cy+234,"others still classify correctly",13.5,GREEN,"800"))
    return svg(b)

# ---------- SLIDE 4: CONTRIBUTION ----------
def s_contribution():
    ch=chunks("contribution"); b=header("Contribution","Three contributions")
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,152,1152,64,fill=PANEL,stroke=STROKE)+
        rect(64,152,6,64,fill=ACCENT,rx=6,sw=0)+
        T(92,192,"A new repulsion space, a practical kernel, and a data-driven way to set its lengthscales.",17,TEXT,"600"))
    cards=[
        (ch[1],ACCENT,"1","Repel input gradients","A method that adds a repulsion term defined on input gradients rather than on weights or function outputs."),
        (ch[2],TEAL,"2","A practical, linear kernel","Compares the normalized true-label input gradients across training data, keeping computation linear in the number of samples."),
        (ch[3],GOLD,"3","PCA lengthscales","Chooses the kernel lengthscales from the principal components of the data, emphasizing high-variance features for corruption robustness."),
    ]
    cw=368; gap=24; x0=64; cy=240; chh=320
    for c,col,num,ti,tx in cards:
        i=cards.index(c) if False else None
    for idx,(c,col,num,ti,tx) in enumerate(cards):
        x=x0+idx*(cw+gap)
        body=(rect(x,cy,cw,chh,fill=PANEL,stroke=STROKE)+
              rect(x,cy,cw,6,fill=col,rx=6,sw=0)+
              circle(x+52,cy+70,27,fill="none",stroke=col,sw=2.5)+
              T(x+52,cy+80,num,30,col,"800",anchor="middle"))
        yy=cy+140
        for j,ln in enumerate(wrap(ti,24)):
            body+=T(x+28,yy+j*28,ln,19,TEXT,"800")
        yy+=28*len(wrap(ti,24))+10
        body+=para(x+28,yy,tx,14.5,SEC,40,24)[0]
        b+=anchor(c["aid"],c["kw"],body)
    return svg(b)

# ---------- SLIDE 5: METHOD ----------
def s_method():
    ch=chunks("method"); b=header("Method","Wasserstein descent, input-gradient kernel")
    gx=[64,648]; gy=[152,362]; cw=568; chh=198
    # c1 WGD particles
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(gx[0],gy[0],cw,chh,fill=PANEL,stroke=STROKE)+
        rect(gx[0],gy[0],6,chh,fill=ACCENT,rx=6,sw=0)+
        T(gx[0]+28,gy[0]+38,"Wasserstein gradient descent",17,ACCENT,"800")+
        para(gx[0]+28,gy[0]+68,"Each network in the ensemble is a particle. Its update combines two forces at every step.",14.5,SEC,58,22)[0]+
        chip(gx[0]+28,gy[0]+112,cw-56,"Driving force  →  toward the Bayesian posterior",ACCENT,34,13.5)+
        chip(gx[0]+28,gy[0]+154,cw-56,"Repulsion force  →  pushes particles apart",TEAL,34,13.5))
    # c2 update equation
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(gx[1],gy[0],cw,chh,fill=PANEL,stroke=STROKE)+
        rect(gx[1],gy[0],6,chh,fill=TEAL,rx=6,sw=0)+
        T(gx[1]+28,gy[0]+38,"The particle update",17,TEAL,"800")+
        para(gx[1]+28,gy[0]+68,"Driving term climbs the log-posterior; the kernel-weighted repulsion term spreads members out.",14.5,SEC,58,22)[0]+
        rect(gx[1]+28,gy[0]+118,cw-56,58,fill=PANEL2,stroke=STROKE,rx=8)+
        T(gx[1]+cw/2,gy[0]+142,"theta+ = theta + eta ( grad log pi(theta)",15,TEXT,"800",anchor="middle",ff=MONO)+
        T(gx[1]+cw/2,gy[0]+164,"          −  sum grad k / sum k )",15,TEXT,"800",anchor="middle",ff=MONO))
    # c3 the kernel
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(gx[0],gy[1],cw,chh,fill=PANEL,stroke=STROKE)+
        rect(gx[0],gy[1],6,chh,fill=GOLD,rx=6,sw=0)+
        T(gx[0]+28,gy[1]+38,"The kernel  ·  the crucial choice",16.5,GOLD,"800")+
        para(gx[0]+28,gy[1]+68,"Compare the true-label input gradients, normalized to the unit sphere, with an RBF kernel. Directions matter because magnitudes shrink as training converges.",14,SEC,60,21)[0]+
        rect(gx[0]+28,gy[1]+148,cw-56,38,fill=PANEL2,stroke=STROKE,rx=8)+
        T(gx[0]+cw/2,gy[1]+172,"s = grad_x f(x)_y / || grad_x f(x)_y ||",15,TEXT,"800",anchor="middle",ff=MONO))
    # c4 PCA lengthscales
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(gx[1],gy[1],cw,chh,fill=PANEL,stroke=STROKE)+
        rect(gx[1],gy[1],6,chh,fill=RED,rx=6,sw=0)+
        T(gx[1]+28,gy[1]+38,"PCA lengthscales",16.5,RED,"800")+
        para(gx[1]+28,gy[1]+68,"Kernel lengthscales are set from the principal components of the data, so repulsion is strongest along the most informative input directions.",14,SEC,60,21)[0]+
        # mini pca arrows
        line(gx[1]+40,gy[1]+176,gx[1]+150,gy[1]+150,ACCENT,3)+T(gx[1]+156,gy[1]+150,"PC1 (high variance)",12.5,ACCENT,"700")+
        line(gx[1]+40,gy[1]+176,gx[1]+92,gy[1]+156,TEAL,2.5)+T(gx[1]+156,gy[1]+176,"PC2 (lower variance)",12.5,TEAL,"700"))
    return svg(b)

# ---------- SLIDE 6: DATASET ----------
def s_dataset():
    ch=chunks("dataset-benchmark"); b=header("Dataset / Benchmark","From toy tasks to corrupted images")
    # c1 top band -- toy tasks
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,152,1152,86,fill=PANEL,stroke=STROKE)+
        rect(64,152,6,86,fill=TEAL,rx=6,sw=0)+
        T(92,186,"Illustrative toy tasks",15,TEAL,"800",ls="1")+
        para(92,214,"1D regression and 2D classification show directly how input-gradient repulsion raises predictive uncertainty away from the training data.",15,TEXT,96,24)[0])
    # c2 main datasets (left)  c3 corrupted (right)
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,258,560,180,fill=PANEL,stroke=STROKE)+
        rect(64,258,6,180,fill=ACCENT,rx=6,sw=0)+
        T(92,296,"Main image classification",16.5,ACCENT,"800")+
        chip(92,314,504,"CIFAR-10  ·  CIFAR-100  ·  TinyImageNet",ACCENT,32,13.5)+
        chip(92,354,246,"ResNet / PreActResNet",TEAL,32,13)+
        chip(350,354,246,"ensemble of 10 members",GOLD,32,13)+
        T(92,424,"Ten particles, standard vision backbones.",13.5,SEC,"600"))
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,258,560,180,fill=PANEL,stroke=STROKE)+
        rect(656,258,6,180,fill=GOLD,rx=6,sw=0)+
        T(684,296,"Corruption robustness",16.5,GOLD,"800")+
        para(684,326,"CIFAR-10-C, CIFAR-100-C and TinyImageNet-C apply a demanding grid of image corruptions.",14,SEC,60,21)[0]+
        _corrgrid(684,376)+
        T(940,392,"19 types",15,GOLD,"800")+T(940,414,"× 5 severity levels",13,SEC,"700"))
    # c4 metrics bottom band
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(64,458,1152,92,fill=PANEL,stroke=STROKE)+
        rect(64,458,6,92,fill=GREEN,rx=6,sw=0)+
        T(92,492,"Metrics  ·  clean and averaged over all corruptions",16,GREEN,"800")+
        chip(92,506,340,"Accuracy",GREEN,32,13.5)+
        chip(444,506,340,"Negative log-likelihood",ACCENT,32,13.5)+
        chip(796,506,340,"Expected calibration error",GOLD,32,13.5))
    return svg(b)

def _corrgrid(x,y):
    out=""
    cols=["#2E6F63","#3E8F7E","#C99B3B","#B85B50","#3A6EA5"]
    for r in range(5):
        for c in range(5):
            col=cols[c] if r<=c else PANEL2
            out+=rect(x+c*20,y+r*16,16,12,fill=col,rx=2,sw=0)
    return out

# ---------- SLIDE 7: KEY RESULT ----------
def s_result():
    ch=chunks("key-result"); b=header("Key Result","Best under corruption, on every metric")
    # c1 top band
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,152,1152,58,fill=PANEL,stroke=STROKE)+
        rect(64,152,6,58,fill=GREEN,rx=6,sw=0)+
        T(92,188,"FoRDE-PCA is the strongest method on every corrupted-image metric, while staying competitive on clean data.",16.5,TEXT,"700"))
    # c2 accuracy-gain card (left)
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,230,560,320,fill=PANEL,stroke=STROKE)+
        rect(64,230,6,320,fill=ACCENT,rx=6,sw=0)+
        T(92,268,"Accuracy gain over the 2nd-best method",16.5,ACCENT,"800")+
        kpi(92,286,246,"+2.4%","CIFAR-10-C",GREEN,36,108)+
        kpi(350,286,246,"+1.3%","CIFAR-100-C",GREEN,36,108)+
        T(92,432,"Under input corruptions (higher is better)",13.5,SEC,"700")+
        bar(300,448,260,2.4,2.8,GREEN,"CIFAR-10-C","+2.4",h=22)+
        bar(300,480,260,1.3,2.8,TEAL,"CIFAR-100-C","+1.3",h=22)+
        T(92,528,"Competitive on clean images; clearly ahead once corruptions hit.",13,SEC,"600"))
    # c3 toy uncertainty card (right)
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,230,560,320,fill=PANEL,stroke=STROKE)+
        rect(656,230,6,320,fill=TEAL,rx=6,sw=0)+
        T(684,268,"Toy tasks  ·  more uncertainty away from data",15.5,TEAL,"800")+
        _uncertainty(684,300)+
        para(684,506,"In 1D and 2D, FoRDE raises uncertainty off the data more than deep ensembles — direct evidence of greater functional diversity.",13.5,SEC,74,20)[0])
    return svg(b)

def _uncertainty(x,y):
    # a band widening away from the data, with a scatter of training points in the middle
    out=rect(x,y,504,150,fill="#0E2334",stroke=STROKE,rx=10)
    cx0=x+40; cx1=x+464; base=y+96; import math
    top=[]; bot=[]
    for i in range(0,101,4):
        px=cx0+(cx1-cx0)*i/100.0
        d=abs(i-50)/50.0
        band=8+46*d*d
        top.append((px,base-band)); bot.append((px,base+band))
    pts=" ".join(f"{a},{bb}" for a,bb in top)+" "+" ".join(f"{a},{bb}" for a,bb in reversed(bot))
    out+=f'<polygon points="{pts}" fill="{TEAL}" opacity="0.18"/>'
    out+=f'<polyline points="{" ".join(f"{a},{bb}" for a,bb in top)}" fill="none" stroke="{TEAL}" stroke-width="2"/>'
    out+=f'<polyline points="{" ".join(f"{a},{bb}" for a,bb in bot)}" fill="none" stroke="{TEAL}" stroke-width="2"/>'
    out+=line(cx0,base,cx1,base,STROKE,1.5,dash="4 4")
    mid=(cx0+cx1)/2
    for k in range(-3,4):
        out+=circle(mid+k*20,base+4,3,fill=ACCENT)
    out+=T(x+width_mid(cx0,cx1),y+140,"training data",12,SEC,"700",anchor="middle")
    out+=T(cx0-2,y+18,"high uncertainty",11.5,TEAL,"700")
    out+=T(cx1+2,y+18,"high uncertainty",11.5,TEAL,"700",anchor="end")
    return out

def width_mid(a,b): return (a+b)/2

# ---------- SLIDE 8: ABLATION ----------
def s_ablation():
    ch=chunks("ablation-study"); b=header("Ablation Study","Lengthscales trade clean vs. robust")
    # c1 top band setup
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,152,1152,58,fill=PANEL,stroke=STROKE)+
        rect(64,152,6,58,fill=ACCENT,rx=6,sw=0)+
        T(92,188,"The kernel lengthscales govern how repulsion is distributed across input dimensions — the key design knob.",16,TEXT,"600"))
    # c2 PCA (left), c3 identity/tuned (mid) -- two comparison cards on top row
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,230,368,150,fill="#0F2E2B",stroke=TEAL,rx=14,sw=1.5)+
        rect(64,230,6,150,fill=TEAL,rx=6,sw=0)+
        T(92,268,"FoRDE-PCA",16.5,TEAL,"800")+
        T(92,296,"best robustness",14,GREEN,"700")+
        para(92,324,"Emphasizes high-variance features, giving the strongest corruption robustness.",13.5,SEC,42,20)[0])
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(456,230,760,150,fill=PANEL,stroke=STROKE)+
        rect(456,230,6,150,fill=GOLD,rx=6,sw=0)+
        T(484,268,"FoRDE-Identity  &  FoRDE-Tuned",16.5,GOLD,"800")+
        para(484,298,"Identity lengthscales give the best clean accuracy on CIFAR-100 and best likelihood on CIFAR-10, but sacrifice some robustness.",14,SEC,88,22)[0]+
        T(484,362,"Tuning between the two extremes → best of both worlds in most cases.",14,GREEN,"800"))
    # c4 ensemble-size bar chart bottom band
    body=(rect(64,398,1152,152,fill=PANEL,stroke=STROKE)+
          rect(64,398,6,152,fill=ACCENT,rx=6,sw=0)+
          T(92,432,"Diversity is efficient  ·  corruption robustness vs. ensemble size",16,TEXT,"800"))
    body+=bar(360,452,760,10,30,TEAL,"FoRDE (10 members)","10 members  →  matches",h=26)
    body+=bar(360,492,760,30,30,SEC,"Deep Ensemble (30)","30 members",h=26)
    body+=T(92,536,"A 10-member FoRDE matches or exceeds the corruption robustness of a 30-member deep ensemble.",13.5,GREEN,"800")
    b+=anchor(ch[3]["aid"],ch[3]["kw"],body)
    return svg(b)

# ---------- SLIDE 9: HEADLINE NUMBERS ----------
def s_headline():
    ch=chunks("headline-numbers"); b=header("Headline Numbers","The impact in four numbers")
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,152,1152,58,fill=PANEL,stroke=STROKE)+
        rect(64,152,6,58,fill=ACCENT,rx=6,sw=0)+
        T(92,188,"A few numbers capture what repelling input gradients buys you.",16.5,TEXT,"700"))
    # three big KPI cards
    cw=368; gap=24; x0=64; cy=236; chh=200
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(x0,cy,cw,chh,fill=PANEL,stroke=STROKE)+
        rect(x0,cy,cw,6,fill=GREEN,rx=6,sw=0)+
        T(x0+cw/2,cy+96,"+2.4% / +1.3%",34,GREEN,"800",anchor="middle")+
        T(x0+cw/2,cy+130,"accuracy on CIFAR-10-C / -100-C",13.5,SEC,"600",anchor="middle")+
        T(x0+cw/2,cy+158,"over the next-best method",13,TER,"600",anchor="middle"))
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(x0+cw+gap,cy,cw,chh,fill=PANEL,stroke=STROKE)+
        rect(x0+cw+gap,cy,cw,6,fill=TEAL,rx=6,sw=0)+
        T(x0+cw+gap+cw/2,cy+96,"10  ≈  30",38,TEAL,"800",anchor="middle")+
        T(x0+cw+gap+cw/2,cy+130,"members match a deep ensemble",13.5,SEC,"600",anchor="middle")+
        T(x0+cw+gap+cw/2,cy+158,"3× fewer models, same robustness",13,TER,"600",anchor="middle"))
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(x0+2*(cw+gap),cy,cw,chh,fill=PANEL,stroke=STROKE)+
        rect(x0+2*(cw+gap),cy,cw,6,fill=GOLD,rx=6,sw=0)+
        T(x0+2*(cw+gap)+cw/2,cy+96,"19 × 5",38,GOLD,"800",anchor="middle")+
        T(x0+2*(cw+gap)+cw/2,cy+130,"corruption types × severity levels",13.5,SEC,"600",anchor="middle")+
        T(x0+2*(cw+gap)+cw/2,cy+158,"a demanding robustness grid",13,TER,"600",anchor="middle"))
    b+=rect(64,464,1152,86,fill=PANEL2,stroke=STROKE,rx=12)
    b+=T(92,500,"Ensemble size 10  ·  ResNet18 backbone  ·  input-gradient kernel with linear cost in the number of training samples",14.5,SEC,"600")
    b+=T(92,530,"Gains hold across CIFAR-10-C, CIFAR-100-C and TinyImageNet-C.",14.5,TEAL,"700")
    return svg(b)

# ---------- SLIDE 10: TAKEAWAY ----------
def s_takeaway():
    ch=chunks("takeaway"); b=header("Takeaway","The space of diversity is the lever")
    cards=[
        (ch[0],ACCENT,"Where, not just how much","The space in which you enforce ensemble diversity matters as much as the amount of repulsion you apply."),
        (ch[1],TEAL,"Input gradients are the sweet spot","Repelling in this compact space makes members genuinely different functions — without the waste of weights or the intractability of functions."),
        (ch[2],GREEN,"Data-driven and robust","With PCA lengthscales from principal component analysis, the ensembles are more robust and better calibrated under real-world input corruptions."),
    ]
    y=168
    for c,col,ti,tx in cards:
        body=(rect(64,y,1152,118,fill=PANEL,stroke=STROKE)+
              rect(64,y,6,118,fill=col,rx=6,sw=0)+
              circle(112,y+59,10,fill=col)+
              T(150,y+48,ti,19,TEXT,"800"))
        body+=para(150,y+80,tx,15.5,SEC,92,24)[0]
        b+=anchor(c["aid"],c["kw"],body)
        y+=136
    b+=line(64,596,1216,596,STROKE,1)
    b+=T(64,632,"FoRDE  ·  Input-gradient space particle inference for neural network ensembles",16,TEXT,"700")
    b+=T(64,660,"ICLR 2024  ·  arXiv:2306.02775  ·  github.com/AaltoPML/FoRDE",13.5,SEC,"600")
    return svg(b)

SLIDES=[("01_title",s_title),("02_problem",s_problem),("03_motivation",s_motivation),
        ("04_contribution",s_contribution),("05_method",s_method),("06_dataset",s_dataset),
        ("07_key_result",s_result),("08_ablation",s_ablation),("09_headline_numbers",s_headline),
        ("10_takeaway",s_takeaway)]

for name,fn in SLIDES:
    open(os.path.join(OUT,name+".svg"),"w").write(fn())
    print("wrote",name)
print("DONE",len(SLIDES))
