#!/usr/bin/env python3
"""All-native SVG deck builder for paper2video run 035 (PatchRot / self-supervised ViT).
Reads _anchor_map.json; wraps each narration chunk in its own <g id="cue_..."> card
with a <title> holding the cue keywords, so the strict --require-pptx-anchors cue
pass resolves every anchor from PPTX geometry. Zero <image>, zero gradients."""
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

def dtile(x,y,w,name,res,col,h=60):
    # dataset tile: name (big) with resolution beneath, both inside the box
    return (rect(x,y,w,h,fill=PANEL2,stroke=STROKE,rx=12)+
            T(x+w/2,y+34,name,19,col,"800",anchor="middle")+
            T(x+w/2,y+52,res,12,SEC,"600",anchor="middle"))

def numtile(x,y,w,h,num,lbl,col,ns=24):
    # compact numeric tile: number then label, both inside the box
    return (rect(x,y,w,h,fill=PANEL2,stroke=STROKE,rx=10)+
            T(x+w/2,y+h*0.52,num,ns,col,"800",anchor="middle")+
            T(x+w/2,y+h-9,lbl,11.5,SEC,"600",anchor="middle"))

# ---- vision-specific native glyphs ----
def orient(x,y,s,deg,col,lbl):
    # square outline with an orientation arrow on its "top" edge, rotated by deg
    cx,cy=x+s/2,y+s/2
    g=(f'<g transform="rotate({deg} {cx} {cy})">'
       + rect(x,y,s,s,fill="none",stroke=col,rx=3,sw=2)
       + f'<polygon points="{cx-6},{y+4} {cx+6},{y+4} {cx},{y-6}" fill="{col}"/>'
       + '</g>')
    return g + T(cx,y+s+16,lbl,11,SEC,"700",anchor="middle")

def patchgrid(x,y,cell,gap,col,n=3,fill=PANEL2):
    out=""
    for i in range(n):
        for j in range(n):
            out+=rect(x+j*(cell+gap), y+i*(cell+gap), cell, cell, fill=fill, stroke=col, rx=2, sw=1.4)
    return out

# ---------- SLIDE 1: TITLE ----------
def s_title():
    ch=chunks("title"); b=""
    b+=T(64,72,"NeurIPS 2022",14,ACCENT,"800",ls="3")
    b+=T(1216,72,"Arizona State University  ·  Georgia State University",14,SEC,"600",anchor="end")
    b+=line(64,88,1216,88,STROKE,1)
    b+=T(64,156,"PatchRot",44,WHITE,"800")
    b+=T(64,200,"A Self-Supervised Technique for Vision Transformers",27,ACCENT,"800")
    b+=T(64,236,"Predict the rotation of the whole image and of every patch",19,TEAL,"700")
    b+=T(64,282,"Sachin Chhabra  ·  Prabal Bijoy Dutta  ·  Hemanth Venkateswara  ·  Baoxin Li",15.5,SEC,"500")
    # decorative rotation motif upper-right
    b+=orient(1020,120,52,0,ACCENT,"0")
    b+=orient(1096,120,52,90,TEAL,"90")
    b+=orient(1020,196,52,180,GOLD,"180")
    b+=orient(1096,196,52,270,GREEN,"270")
    b+=T(1094,272,"predict the angle",11.5,TER,"700",anchor="middle")
    # four concept cards (2x2) = anchors
    cw=560; chh=118; gap=32; x0=64; x1=x0+cw+gap; cy0=316; cy1=cy0+chh+22
    data=[
        (ch[0],ACCENT,x0,cy0,"ViTs are data-hungry","Vision transformers beat ConvNets only with huge labeled datasets. PatchRot is a self-supervised fix built for transformers."),
        (ch[1],GOLD,x1,cy0,"The idea: predict rotations","Rotate the whole image or each patch by 0 / 90 / 180 / 270 degrees, then train the ViT to predict every angle."),
        (ch[2],TEAL,x0,cy1,"Two levels of rotation","The class token predicts the image rotation for global structure; new per-patch heads predict each patch's rotation for local detail."),
        (ch[3],GREEN,x1,cy1,"Beats supervised and RotNet","After pretraining, features beat training-from-scratch and RotNet on CIFAR-10, CIFAR-100, FashionMNIST and Tiny-ImageNet."),
    ]
    for c,col,x,cy,ti,tx in data:
        body=(rect(x,cy,cw,chh,fill=PANEL,stroke=STROKE)+
              rect(x,cy,6,chh,fill=col,rx=6,sw=0)+
              T(x+28,cy+36,ti,18,TEXT,"800"))
        body+=para(x+28,cy+62,tx,14,SEC,68,21)[0]
        b+=anchor(c["aid"],c["kw"],body)
    b+=line(64,616,1216,616,STROKE,1)
    b+=T(64,650,"arXiv:2210.15722",14,ACCENT,"700")
    b+=T(300,650,"A simple rotation task, crafted for the patch-token structure of ViTs.",14,SEC,"600")
    return svg(b)

# ---------- SLIDE 2: PROBLEM ----------
def s_problem():
    ch=chunks("problem"); b=header("Problem","Vision transformers need too many labels")
    # c1 left tall card: ViTs win only with big labeled data
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,404,392,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,392,fill=ACCENT,rx=6,sw=0)+
        T(92,202,"ViTs overtook ConvNets",18,TEXT,"800")+
        para(92,240,"On many vision tasks vision transformers now lead, but only when trained on very large labeled datasets.",15,SEC,42,24)[0]+
        # data-vs-accuracy mini glyph: two bars
        T(92,352,"Accuracy vs labeled data (illustrative)",13,TER,"700")+
        bar(240,372,180,0.55,1.0,RED,"few labels","ViT low",h=26)+
        bar(240,412,180,0.95,1.0,GREEN,"many labels","ViT high",h=26)+
        rect(92,468,344,64,fill=PANEL2,stroke=STROKE,rx=10)+
        para(112,494,"The win depends on a mountain of labels.",13.5,TEAL,58,20)[0])
    # right stack
    fx=500; fw=716
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(fx,158,fw,120,fill="#2A1720",stroke=RED,rx=14,sw=1.5)+
        rect(fx,158,6,120,fill=RED,rx=6,sw=0)+
        T(fx+28,196,"With few labels, ViTs fall behind ConvNets",16,RED,"800")+
        para(fx+28,226,"They lack built-in inductive biases such as locality and translation equivariance that ConvNets get for free.",14.5,TEXT,74,22)[0])
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(fx,290,fw,96,fill=PANEL,stroke=STROKE)+
        rect(fx,290,6,96,fill=GOLD,rx=6,sw=0)+
        T(fx+28,328,"Labels at ViT scale are costly",16,GOLD,"800")+
        para(fx+28,356,"Annotating data at the scale vision transformers demand is expensive and slow.",14.5,SEC,74,22)[0])
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(fx,398,fw,152,fill=PANEL,stroke=STROKE)+
        rect(fx,398,6,152,fill=TEAL,rx=6,sw=0)+
        T(fx+28,438,"Self-supervision could help, but...",16,TEAL,"800")+
        para(fx+28,468,"SSL learns features without labels, yet popular pretext tasks were all designed for ConvNets.",14.5,SEC,74,22)[0]+
        T(fx+28,540,"They ignore the patch-token structure that makes transformers special.",14.5,TEAL,"800"))
    return svg(b)

# ---------- SLIDE 3: MOTIVATION ----------
def s_motivation():
    ch=chunks("motivation"); b=header("Motivation","Push rotation prediction to the patch level")
    # c1 left: ViT outputs one token per patch
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,560,392,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,392,fill=ACCENT,rx=6,sw=0)+
        T(92,198,"A ViT outputs one token per patch",18,ACCENT,"800")+
        para(92,230,"It splits an image into patches and applies self-attention, so unlike a ConvNet it produces a separate output for every patch, not just one for the whole image.",14.5,SEC,50,22)[0]+
        # patch grid glyph with tokens
        patchgrid(150,336,52,10,ACCENT,n=3)+
        T(360,362,"->",22,SEC,"800",anchor="middle")+
        rect(408,336,150,180,fill=PANEL2,stroke=STROKE,rx=10)+
        T(483,360,"per-patch",12.5,TEAL,"700",anchor="middle")+
        T(483,378,"tokens",12.5,TEAL,"700",anchor="middle")+
        "".join(circle(432+ (k%3)*36, 404+(k//3)*40, 7, fill=TEAL) for k in range(9))+
        T(92,540,"One output per patch, ready to supervise locally.",13.5,TEAL,"700"))
    # right stack
    rx=648; rw=568
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(rx,158,rw,116,fill=PANEL,stroke=STROKE)+
        rect(rx,158,6,116,fill=GOLD,rx=6,sw=0)+
        T(rx+28,196,"RotNet: rotation is a rich signal",16,GOLD,"800")+
        para(rx+28,226,"Prior work showed that simply predicting an image's rotation angle teaches a ConvNet surprisingly rich features.",14.5,SEC,60,22)[0])
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(rx,286,rw,150,fill="#0F2E2B",stroke=TEAL,rx=14,sw=1.5)+
        rect(rx,286,6,150,fill=TEAL,rx=6,sw=0)+
        T(rx+28,324,"The natural question",16,TEAL,"800")+
        para(rx+28,354,"Can we push rotation prediction down to the patch level, so the transformer learns local features per patch as well as global structure for the whole image?",14.5,TEXT,60,22)[0])
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(rx,448,rw,102,fill=PANEL,stroke=STROKE)+
        rect(rx,448,6,102,fill=GREEN,rx=6,sw=0)+
        T(rx+28,486,"A perfect fit for token models",16,GREEN,"800")+
        para(rx+28,516,"That patch-level signal is exactly what a token-based model is built to exploit.",14.5,SEC,60,22)[0])
    return svg(b)

# ---------- SLIDE 4: CONTRIBUTION ----------
def s_contribution():
    ch=chunks("contribution"); b=header("Contribution","Three contributions")
    # c1 intro strip
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,1152,54,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,54,fill=ACCENT,rx=6,sw=0)+
        T(92,191,"The paper makes three main contributions for training vision transformers without labels.",16,TEXT,"600"))
    cards=[
        (ch[1],TEAL,"1","PatchRot, built for ViTs","A self-supervised task that predicts rotation at two levels: the class token predicts the whole-image rotation for global context, and new per-patch heads predict each patch's rotation for local detail."),
        (ch[2],GOLD,"2","A buffer gap between patches","A gap inserted between patches during training so the network cannot cheat by matching continuous edges, forcing it to learn genuine content."),
        (ch[3],GREEN,"3","Extensive gains","PatchRot beats supervised-from-scratch and RotNet across multiple datasets, and its features transfer well and help in semi-supervised settings."),
    ]
    cw=368; gap=24; x0=64; cy=236; chh=314
    for i,(c,col,num,ti,tx) in enumerate(cards):
        x=x0+i*(cw+gap)
        body=(rect(x,cy,cw,chh,fill=PANEL,stroke=STROKE)+
              rect(x,cy,cw,6,fill=col,rx=6,sw=0)+
              circle(x+52,cy+68,26,fill="none",stroke=col,sw=2.5)+
              T(x+52,cy+78,num,28,col,"800",anchor="middle"))
        yy=cy+134
        for j,ln in enumerate(wrap(ti,24)):
            body+=T(x+28,yy+j*26,ln,18,TEXT,"800")
        yy+=26*len(wrap(ti,24))+12
        body+=para(x+28,yy,tx,14,SEC,40,22)[0]
        b+=anchor(c["aid"],c["kw"],body)
    b+=T(64,592,"Global and local rotation together — a self-supervised task made for transformers.",15,TEAL,"700")
    return svg(b)

# ---------- SLIDE 5: METHOD ----------
def s_method():
    ch=chunks("method"); b=header("Method","Rotate, predict at two levels, then fine-tune")
    lx=64; lw=568
    # c1: rotate step
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(lx,158,lw,200,fill=PANEL,stroke=STROKE)+
        rect(lx,158,6,200,fill=ACCENT,rx=6,sw=0)+
        T(lx+28,196,"Step 1  ·  rotate",16.5,ACCENT,"800")+
        para(lx+28,226,"Take an input image and either rotate the whole image, or rotate each patch independently, by a random multiple of ninety degrees.",14,SEC,58,21)[0]+
        orient(lx+40,300,40,0,ACCENT,"0")+orient(lx+150,300,40,90,TEAL,"90")+
        orient(lx+260,300,40,180,GOLD,"180")+orient(lx+370,300,40,270,GREEN,"270")+
        T(lx+470,326,"4-way",14,SEC,"800",anchor="middle")+
        T(lx+470,344,"label",14,SEC,"800",anchor="middle"))
    # c2: class token -> image rotation
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(lx,374,lw,176,fill="#0F2E2B",stroke=TEAL,rx=14,sw=1.5)+
        rect(lx,374,6,176,fill=TEAL,rx=6,sw=0)+
        T(lx+28,412,"Step 2  ·  class token -> image rotation",15.5,TEAL,"800")+
        para(lx+28,442,"The ViT predicts these angles as a simple four-way classification. The class token, which normally predicts the object class, is repurposed to predict the whole-image rotation for global structure.",14,SEC,58,21)[0])
    rxx=656; rw=560
    # c3: patch heads -> patch rotation + buffer gap
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(rxx,158,rw,200,fill=PANEL,stroke=STROKE)+
        rect(rxx,158,6,200,fill=GOLD,rx=6,sw=0)+
        T(rxx+28,196,"Step 3  ·  patch heads + buffer gap",15.5,GOLD,"800")+
        para(rxx+28,226,"New MLP heads on each patch token predict that patch's rotation for local detail. Patches are cropped from a larger grid so a buffer gap sits between them, and edge continuity can't leak the answer.",14,SEC,56,21)[0]+
        patchgrid(rxx+390,300,30,10,GOLD,n=3)+
        T(rxx+435,300-6,"gap",11,TER,"700",anchor="middle"))
    # c4: reduced -> full resolution
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(rxx,374,rw,176,fill=PANEL,stroke=STROKE)+
        rect(rxx,374,6,176,fill=GREEN,rx=6,sw=0)+
        T(rxx+28,412,"Step 4  ·  reduced -> full resolution",15.5,GREEN,"800")+
        para(rxx+28,442,"Pretrain at reduced resolution; then remove the extra patch heads and fine-tune at full resolution on the real task, with positional embeddings interpolated to the larger patch count.",14,SEC,56,21)[0])
    return svg(b)

# ---------- SLIDE 6: DATASET ----------
def s_dataset():
    ch=chunks("dataset-benchmark"); b=header("Dataset / Benchmark","Four datasets, transfer and semi-supervised")
    # c1 four datasets strip
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,1152,120,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,120,fill=ACCENT,rx=6,sw=0)+
        T(92,194,"Four standard image-classification datasets",17,ACCENT,"800")+
        dtile(92,206,256,"CIFAR-10","32 x 32",ACCENT)+
        dtile(368,206,256,"CIFAR-100","32 x 32",ACCENT)+
        dtile(644,206,256,"FashionMNIST","32 x 32",ACCENT)+
        dtile(920,206,280,"Tiny-ImageNet","64 x 64",GOLD))
    # c2 backbone
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,296,560,120,fill=PANEL,stroke=STROKE)+
        rect(64,296,6,120,fill=TEAL,rx=6,sw=0)+
        T(92,334,"Backbone and extra probes",16,TEAL,"800")+
        para(92,364,"A compact ViT with six encoder blocks. SVHN and MNIST also probe rotation-invariant objects like digits.",14.5,SEC,58,22)[0])
    # c3 patch sizes
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,296,560,120,fill=PANEL,stroke=STROKE)+
        rect(656,296,6,120,fill=GOLD,rx=6,sw=0)+
        T(684,334,"Patch sizes and buffer gap",16,GOLD,"800")+
        para(684,364,"Patch size 4 pixels for the small datasets, 8 for Tiny-ImageNet, with a buffer gap set to a quarter of the patch size.",14.5,SEC,58,22)[0])
    # c4 transfer + semi-supervised
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(64,434,1152,116,fill="#0F2E2B",stroke=GREEN,rx=14,sw=1.5)+
        rect(64,434,6,116,fill=GREEN,rx=6,sw=0)+
        T(92,472,"Beyond plain classification",16.5,GREEN,"800")+
        para(92,502,"Transfer learning between CIFAR-10 and CIFAR-100, plus a semi-supervised setting on CIFAR-10 with only a handful of labels, from 250 up to 10,000.",14.5,TEXT,110,23)[0])
    return svg(b)

# ---------- SLIDE 7: KEY RESULT ----------
def s_result():
    ch=chunks("key-result"); b=header("Key Result","PatchRot beats supervised and RotNet everywhere")
    # c1 headline strip
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,150,1152,50,fill=PANEL,stroke=STROKE)+
        rect(64,150,6,50,fill=GREEN,rx=6,sw=0)+
        T(92,182,"On every dataset tested, PatchRot pretraining tops both supervised-from-scratch and the RotNet baseline.",16.5,TEXT,"700"))
    # c2 CIFAR-10 bars (left)
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,214,560,190,fill=PANEL,stroke=STROKE)+
        rect(64,214,6,190,fill=TEAL,rx=6,sw=0)+
        T(92,250,"CIFAR-10 top-1  ·  higher is better",16,TEAL,"800")+
        bar(300,278,250,83.9,100,RED,"Supervised","83.9%",h=30)+
        bar(300,326,250,92.6,100,GREEN,"PatchRot","92.6%",h=30)+
        rect(92,364,504,28,fill="#0F2E2B",stroke=TEAL,rx=8,sw=1.5)+
        T(112,384,"+8.7 points over training from scratch",14,TEAL,"800"))
    # c3 CIFAR-100 + FashionMNIST (right)
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,214,560,190,fill=PANEL,stroke=STROKE)+
        rect(656,214,6,190,fill=GOLD,rx=6,sw=0)+
        T(684,250,"CIFAR-100 & FashionMNIST top-1",16,GOLD,"800")+
        bar(892,278,250,50.2,100,RED,"C100 Supervised","50.2%",h=26)+
        bar(892,320,250,70.6,100,GREEN,"C100 PatchRot","70.6%",h=26)+
        bar(892,362,250,94.1,100,ACCENT,"FMNIST PatchRot","94.1%",h=26))
    # c4 linear probing / single block
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(64,418,1152,190,fill=PANEL,stroke=STROKE)+
        rect(64,418,6,190,fill=ACCENT,rx=6,sw=0)+
        T(92,456,"Even a frozen network learns useful features",16.5,ACCENT,"800")+
        para(92,488,"With linear probing the whole network is frozen and only the final layer is trained, yet accuracy gets close to full supervised performance.",14.5,SEC,86,22)[0]+
        chip(92,540,"Fine-tuning just a single encoder block already beats training from scratch",ACCENT,w=1080,h=40))
    b+=T(64,648,"Strong features whether you fine-tune everything, one block, or nothing at all.",14,SEC,"600")
    return svg(b)

# ---------- SLIDE 8: ABLATION ----------
def s_ablation():
    ch=chunks("ablation-study"); b=header("Ablation Study","Every component earns its place")
    # c1 setup + patch-only
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,560,150,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,150,fill=ACCENT,rx=6,sw=0)+
        T(92,196,"CIFAR-10: drop one piece at a time",16,ACCENT,"800")+
        para(92,226,"Training on patch rotations alone, without whole-image rotation, drops accuracy to 91.8% because the model loses global context.",14.5,SEC,54,22)[0])
    # c2 bars comparing variants
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,324,560,226,fill=PANEL,stroke=STROKE)+
        rect(64,324,6,226,fill=TEAL,rx=6,sw=0)+
        T(92,360,"CIFAR-10 top-1  ·  variants vs full",14.5,TEXT,"800")+
        bar(330,388,180,91.0,93,GOLD,"Image only (RotNet)","91.0%",h=28)+
        bar(330,432,180,91.8,93,ACCENT,"Patch only","91.8%",h=28)+
        bar(330,476,180,92.6,93,GREEN,"Full PatchRot","92.6%",h=28)+
        rect(92,510,504,28,fill="#0F2E2B",stroke=TEAL,rx=8,sw=1.5)+
        T(112,530,"Global + local rotation beats either alone",14,TEAL,"800"))
    # c3 other ablations (right top)
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,158,560,244,fill=PANEL,stroke=STROKE)+
        rect(656,158,6,244,fill=GOLD,rx=6,sw=0)+
        T(684,196,"Other design choices that matter",16,GOLD,"800")+
        chip(684,222,"Rotate image + patches together (one pass) -> hurts",RED,w=504,h=44)+
        chip(684,278,"Train at original instead of reduced resolution -> hurts",RED,w=504,h=44)+
        chip(684,334,"Reuse existing head instead of dedicated patch heads -> hurts",RED,w=504,h=44))
    # c4 conclusion (right bottom)
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(656,418,560,132,fill="#0F2E2B",stroke=GREEN,rx=14,sw=1.5)+
        rect(656,418,6,132,fill=GREEN,rx=6,sw=0)+
        T(684,456,"All variants land below the full method",16.5,GREEN,"800")+
        para(684,488,"Each falls under the full 92.6%, showing every design decision contributes.",14.5,TEXT,56,22)[0])
    return svg(b)

# ---------- SLIDE 9: HEADLINE NUMBERS ----------
def s_headline():
    ch=chunks("headline-numbers"); b=header("Headline Numbers","The results in one place")
    # c1 CIFAR-10 big lift
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,168,1152,146,fill=PANEL,stroke=STROKE)+
        rect(64,168,6,146,fill=GREEN,rx=6,sw=0)+
        T(92,206,"CIFAR-10  ·  +8.7 points over supervised",16.5,GREEN,"800")+
        kpi(92,224,"83.9%","Supervised",RED,w=210,h=76)+
        T(322,270,"->",30,SEC,"800",anchor="middle")+
        kpi(352,224,"92.6%","PatchRot",GREEN,w=210,h=76)+
        kpi(600,224,"+8.7 pts","top-1 gain",TEAL,w=230,h=76)+
        rect(852,224,364,76,fill=PANEL2,stroke=STROKE,rx=12)+
        para(872,252,"A large lift from self-supervised rotation pretraining.",14,SEC,40,20)[0])
    # c2 CIFAR-100
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,330,560,220,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(64,330,6,220,fill=GOLD,rx=6,sw=0)+
        T(92,368,"CIFAR-100  ·  over +20 points",16.5,GOLD,"800")+
        kpi(92,388,"50.2%","Supervised top-1",RED,w=250,h=104)+
        kpi(370,388,"70.6%","PatchRot top-1",GOLD,w=250,h=104)+
        T(92,532,"And 90.2% top-5 accuracy on CIFAR-100.",14,SEC,"600"))
    # c3 FashionMNIST + Tiny-ImageNet + semi-supervised
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,330,560,104,fill=PANEL,stroke=STROKE)+
        rect(656,330,6,104,fill=ACCENT,rx=6,sw=0)+
        T(684,366,"FashionMNIST & Tiny-ImageNet",15.5,ACCENT,"800")+
        numtile(684,378,252,50,"94.1%","FashionMNIST top-1",ACCENT,ns=24)+
        numtile(962,378,254,50,"73.4%","Tiny-ImageNet top-5",ACCENT,ns=24))
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(656,446,560,104,fill="#0F2E2B",stroke=GREEN,rx=14,sw=1.5)+
        rect(656,446,6,104,fill=GREEN,rx=6,sw=0)+
        T(684,482,"Semi-supervised CIFAR-10  ·  4k labels",15.5,GREEN,"800")+
        numtile(684,494,252,48,"~54%","Supervised",RED,ns=22)+
        numtile(962,494,254,48,"81%","PatchRot",GREEN,ns=22))
    return svg(b)

# ---------- SLIDE 10: TAKEAWAY ----------
def s_takeaway():
    ch=chunks("takeaway"); b=header("Takeaway","A simple rotation task, made for ViTs")
    cards=[
        (ch[0],ACCENT,"A very simple idea","Predicting the rotation of both the whole image and each individual patch turns out to be a self-supervised task perfectly suited to vision transformers."),
        (ch[1],TEAL,"Global and local, no labels","The class token learns global structure and the patch heads learn local detail, so PatchRot builds rich features without any labels and reliably beats supervised-from-scratch and RotNet across four datasets, in transfer, and when labels are scarce."),
        (ch[2],GREEN,"A practical recipe","It is a lightweight, practical recipe for pretraining vision transformers on limited data."),
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
    b+=T(64,632,"PatchRot: A Self-Supervised Technique for Training Vision Transformers",15.5,TEXT,"700")
    b+=T(64,660,"NeurIPS 2022  ·  Chhabra, Dutta, Venkateswara, Li  ·  arXiv:2210.15722  ·  github.com/s-chh/PatchRot",13.5,SEC,"600")
    return svg(b)

SLIDES=[("01_title",s_title),("02_problem",s_problem),("03_motivation",s_motivation),
        ("04_contribution",s_contribution),("05_method",s_method),("06_dataset",s_dataset),
        ("07_key_result",s_result),("08_ablation",s_ablation),("09_headline",s_headline),
        ("10_takeaway",s_takeaway)]

for name,fn in SLIDES:
    open(os.path.join(OUT,name+".svg"),"w").write(fn())
    print("wrote",name)
print("DONE",len(SLIDES))
