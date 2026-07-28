#!/usr/bin/env python3
"""All-native SVG deck builder for paper2video run 073
(Characterizing the Optimal 0-1 Loss for Multi-class Classification with a
Test-time Attacker, NeurIPS 2023).
Reads _anchor_map.json; wraps each narration chunk in its own <g id="cue_...">
card with a <title> holding cue keywords, so --require-pptx-anchors resolves
every anchor from PPTX geometry. Zero <image>, zero gradients, ASCII mono
equations only."""
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

def poly(pts,fill="none",stroke=STROKE,sw=2.0,dash=None):
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
            T(x-12,y+h*0.72,label,14,lblcolor,"600",anchor="end")+
            T(x+bw+10,y+h*0.72,valtxt,14,color,"800"))

def kpi(x,y,num,lbl,col,w=168,h=100,nsize=30):
    return (rect(x,y,w,h,fill=PANEL2,stroke=STROKE,rx=12)+
            T(x+w/2,y+h*0.52,num,nsize,col,"800",anchor="middle")+
            T(x+w/2,y+h*0.80,lbl,12.5,SEC,"600",anchor="middle"))

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
    b+=T(64,72,"NeurIPS 2023",14,ACCENT,"800",ls="3")
    b+=T(1216,72,"Princeton  ·  Univ. of Chicago  ·  Penn State",14,SEC,"600",anchor="end")
    b+=line(64,88,1216,88,STROKE,1)
    b+=T(64,150,"Characterizing the Optimal 0-1 Loss",40,WHITE,"800")
    b+=T(64,198,"for Multi-class Classification",40,ACCENT,"800")
    b+=T(64,236,"with a Test-time Attacker",26,TEAL,"800")
    b+=T(64,276,"Dai · Ding · Bhagoji · Cullina · Zhao · Zheng · Mittal",16,SEC,"500")
    cw=560; chh=118; gap=32; x0=64; x1=x0+cw+gap; cy0=308; cy1=cy0+chh+22
    data=[
        (ch[0],ACCENT,x0,cy0,"The question","How robust can ANY classifier possibly be against an adversary that perturbs inputs at test time?"),
        (ch[1],GOLD,x1,cy0,"What they derive","Achievable information-theoretic lower bounds on the optimal 0-1 loss, for any discrete dataset."),
        (ch[2],TEAL,x0,cy1,"The tool","Build a conflict hypergraph from data + attacker, then solve a linear program for the lowest loss."),
        (ch[3],GREEN,x1,cy1,"The payoff","Efficient bounds bracket the optimum, exposing a striking gap between robust models and the limit."),
    ]
    for c,col,x,cy,ti,tx in data:
        body=(rect(x,cy,cw,chh,fill=PANEL,stroke=STROKE)+
              rect(x,cy,6,chh,fill=col,rx=6,sw=0)+
              T(x+28,cy+36,ti,18,TEXT,"800"))
        body+=para(x+28,cy+62,tx,14,SEC,68,21)[0]
        b+=anchor(c["aid"],c["kw"],body)
    b+=line(64,616,1216,616,STROKE,1)
    b+=T(64,650,"arXiv:2302.10722",14,ACCENT,"700")
    b+=T(300,650,"How far do today's robust models sit from what is even theoretically possible?",14,SEC,"600")
    return svg(b)

# ---------- SLIDE 2: PROBLEM ----------
def s_problem():
    ch=chunks("problem"); b=header("Problem","Robustness has no yardstick for many classes")
    # c1 left tall card: need the best-possible reference
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,404,392,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,392,fill=ACCENT,rx=6,sw=0)+
        T(92,202,"To judge robustness, you need the limit",18,TEXT,"800")+
        para(92,240,"Knowing whether a classifier is truly robust to adversarial examples requires knowing the best that is even possible.",15,SEC,42,24)[0]+
        # mini gauge glyph: model vs optimum
        rect(92,360,344,150,fill=PANEL2,stroke=STROKE,rx=10)+
        T(112,390,"where does a model sit?",13,TER,"700")+
        line(120,470,408,470,STROKE,2)+
        T(120,492,"optimum",12,GREEN,"700")+circle(126,452,7,fill=GREEN)+
        T(408,492,"trained model",12,RED,"700",anchor="end")+circle(372,432,7,fill=RED)+
        line(126,452,372,432,GOLD,2,dash="5 5")+
        T(250,428,"the gap = ?",13,GOLD,"800",anchor="middle"))
    # right: binary solved / multi-class open / no way to compute
    fx=500; fw=716
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(fx,158,fw,120,fill=PANEL,stroke=STROKE)+
        rect(fx,158,6,120,fill=GREEN,rx=6,sw=0)+
        T(fx+28,196,"Binary case: already solved",16.5,GREEN,"800")+
        para(fx+28,226,"Prior work characterized the optimal robust 0-1 loss for two classes, giving a reference point to measure progress against.",14.5,SEC,60,22)[0])
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(fx,290,fw,96,fill=PANEL,stroke=STROKE)+
        rect(fx,290,6,96,fill=GOLD,rx=6,sw=0)+
        T(fx+28,328,"Multi-class case: left open",16.5,GOLD,"800")+
        para(fx+28,356,"But real problems have many classes, and the multi-class optimum had never been characterized.",14.5,SEC,74,22)[0])
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(fx,398,fw,152,fill="#2A1720",stroke=RED,rx=14,sw=1.5)+
        rect(fx,398,6,152,fill=RED,rx=6,sw=0)+
        T(fx+28,438,"The consequence",16,RED,"800")+
        para(fx+28,468,"With no way to compute the lowest 0-1 loss achievable by any classifier against a test-time attacker, practitioners had no idea how far current defenses sit from the theoretical limit.",14.5,TEXT,74,22)[0]+
        T(fx+28,540,"multi-class optimal loss   =   unknown",15,RED,"800",ff=MONO))
    return svg(b)

# ---------- SLIDE 3: MOTIVATION ----------
def s_motivation():
    ch=chunks("motivation"); b=header("Motivation","The optimum is a diagnostic, not a curiosity")
    # c1 left: powerful diagnostic + comparison bars
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,560,392,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,392,fill=TEAL,rx=6,sw=0)+
        T(92,198,"Compare best-possible vs achieved",18,TEAL,"800")+
        para(92,230,"Measuring the best possible classifier against what state-of-the-art training reaches is a powerful diagnostic.",14.5,SEC,50,22)[0]+
        T(92,322,"0-1 loss at a fixed attack budget (schematic)",13,TER,"700")+
        bar(320,340,240,0.60,1.0,RED,"trained defense","0.60",h=30)+
        bar(320,388,240,0.02,1.0,GREEN,"optimal (best possible)","~0",h=30)+
        rect(92,442,504,90,fill=PANEL2,stroke=STROKE,rx=10)+
        T(112,472,"The gap is the story",13.5,TEAL,"800")+
        para(112,496,"How much robustness is still left on the table?",13.5,SEC,60,20)[0])
    # right: what the gap tells you / only 2 classes / higher-order interactions
    rx=648; rw=568
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(rx,158,rw,116,fill=PANEL,stroke=STROKE)+
        rect(rx,158,6,116,fill=ACCENT,rx=6,sw=0)+
        T(rx+28,196,"It localizes the bottleneck",16,ACCENT,"800")+
        para(rx+28,226,"A large gap blames your training method; a small gap blames a fundamental limit of the data and threat model.",14.5,SEC,60,22)[0])
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(rx,286,rw,108,fill=PANEL,stroke=STROKE)+
        rect(rx,286,6,108,fill=GOLD,rx=6,sw=0)+
        T(rx+28,324,"But only two classes were solved",16,GOLD,"800")+
        para(rx+28,354,"Past work delivered this diagnostic for binary classification only.",14.5,SEC,60,22)[0])
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(rx,406,rw,144,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(rx,406,6,144,fill=GOLD,rx=6,sw=0)+
        T(rx+28,444,"Many classes is not a free extension",16,GOLD,"800")+
        para(rx+28,474,"With three or more classes, examples interact in higher-order ways that binary analysis simply cannot capture.",14.5,TEXT,60,22)[0]+
        T(rx+28,536,"2 classes: pairs      3+ classes: triples, quadruples, ...",14,GOLD,"800",ff=MONO))
    return svg(b)

# ---------- SLIDE 4: CONTRIBUTION ----------
def s_contribution():
    ch=chunks("contribution"); b=header("Contribution","Three contributions")
    # c1 intro strip
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,1152,54,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,54,fill=ACCENT,rx=6,sw=0)+
        T(92,192,"The paper makes three contributions: a framework, efficient bounds, and the first multi-class empirical study of the gap.",16,TEXT,"600"))
    cards=[
        (ch[1],ACCENT,"1","Multi-class framework","Generalize the conflict-graph framework from binary to multi-class: the optimal 0-1 loss is the solution of a linear program on a conflict hypergraph."),
        (ch[2],TEAL,"2","Efficient bounds","Because the exact program can be prohibitive, develop several cheaper lower and upper bounds that bracket the range the true optimum must lie in."),
        (ch[3],GOLD,"3","First empirical study","Deliver an extensive study: the first analysis of the gap to optimal robustness for multi-class classifiers on benchmark datasets."),
    ]
    cw=368; gap=24; x0=64; cy=232; chh=318
    for i,(c,col,num,ti,tx) in enumerate(cards):
        x=x0+i*(cw+gap)
        body=(rect(x,cy,cw,chh,fill=PANEL,stroke=STROKE)+
              rect(x,cy,cw,6,fill=col,rx=6,sw=0)+
              circle(x+52,cy+68,26,fill="none",stroke=col,sw=2.5)+
              T(x+52,cy+78,num,28,col,"800",anchor="middle"))
        yy=cy+130
        for j,ln in enumerate(wrap(ti,22)):
            body+=T(x+28,yy+j*26,ln,18.5,TEXT,"800")
        yy+=26*len(wrap(ti,22))+12
        body+=para(x+28,yy,tx,14.5,SEC,40,23)[0]
        b+=anchor(c["aid"],c["kw"],body)
    b+=T(64,592,"From a binary reference point to a computable multi-class optimum, with a measured gap.",15.5,TEAL,"700")
    return svg(b)

# ---------- SLIDE 5: METHOD ----------
def s_method():
    ch=chunks("method"); b=header("Method","Conflict hypergraph -> linear program")
    # LEFT top: c1 core idea + hypergraph glyph
    lx=64; lw=568
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(lx,158,lw,196,fill=PANEL,stroke=STROKE)+
        rect(lx,158,6,196,fill=ACCENT,rx=6,sw=0)+
        T(lx+28,196,"Core idea  ·  a conflict hypergraph",16.5,ACCENT,"800")+
        para(lx+28,226,"Represent the whole classification problem as a hypergraph built from the data and the attacker's reach.",14,SEC,58,21)[0]+
        _hgraph(lx+320,262,230,78))
    # LEFT bottom: c2 vertices/hyperedges definition
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(lx,370,lw,180,fill=PANEL,stroke=STROKE)+
        rect(lx,370,6,180,fill=TEAL,rx=6,sw=0)+
        T(lx+28,408,"Vertices and hyperedges",16,TEAL,"800")+
        para(lx+28,438,"Each vertex is a data point. A set of points forms a hyperedge when they belong to different classes yet share overlapping adversarial neighborhoods, so one confusing input could be reached from any of them.",14,SEC,58,21)[0])
    # RIGHT top: c3 the LP + dual
    rxx=656; rw=560
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(rxx,158,rw,222,fill=PANEL,stroke=STROKE)+
        rect(rxx,158,6,222,fill=GOLD,rx=6,sw=0)+
        T(rxx+28,196,"Optimal loss = a linear program",16.5,GOLD,"800")+
        para(rxx+28,226,"Maximize the probability mass of correctly classified points subject to the hypergraph's incidence constraints; the dual is a fractional cover that yields the optimal attack.",14,SEC,56,21)[0]+
        eqbox(rxx+28,318,rw-56,"L* = 1 - max_q  p^T q ,  s.t.  B q <= 1",15,h=40))
    # RIGHT bottom: c4 three tractable bounds
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(rxx,396,rw,154,fill="#0F2E2B",stroke=TEAL,rx=14,sw=1.5)+
        rect(rxx,396,6,154,fill=TEAL,rx=6,sw=0)+
        T(rxx+28,430,"Exact is infeasible -> three bounds",15.5,TEAL,"800")+
        chip(rxx+28,446,"Truncate to low-degree hyperedges  ->  lower bound",ACCENT,w=rw-56,h=30)+
        chip(rxx+28,482,"Aggregate binary one-vs-one losses  ->  cheaper bound",GOLD,w=rw-56,h=30)+
        chip(rxx+28,518,"Generalized Caro-Wei  ->  matching upper bound",GREEN,w=rw-56,h=30))
    return svg(b)

def _hgraph(x,y,w,h):
    # small conflict-hypergraph glyph: 3 colored vertices enclosed by a hyperedge blob
    v=[(x+40,y+18,ACCENT),(x+150,y+10,GOLD),(x+110,y+66,GREEN)]
    body=rect(x-14,y-12,w,h+20,fill="#0E2334",stroke=STROKE,rx=10)
    # hyperedge enclosure
    body+=(f'<path d="M {x+18},{y+22} C {x-6},{y-8} {x+90},{y-24} {x+160},{y-6} '
           f'C {x+200},{y+20} {x+170},{y+80} {x+120},{y+82} '
           f'C {x+60},{y+92} {x+2},{y+58} {x+18},{y+22} Z" fill="{RED}" opacity="0.14" '
           f'stroke="{RED}" stroke-width="1.5" stroke-dasharray="4 4"/>')
    for vx,vy,c in v:
        body+=circle(vx,vy,9,fill=c)
    body+=T(x+w-24,y+h-2,"hyperedge = conflict",11,RED,"700",anchor="end")
    return body

# ---------- SLIDE 6: DATASET ----------
def s_dataset():
    ch=chunks("dataset-benchmark"); b=header("Dataset / Benchmark","MNIST and CIFAR-10 under an L2 attacker")
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,1152,58,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,58,fill=ACCENT,rx=6,sw=0)+
        T(92,193,"Two standard vision benchmarks, MNIST and CIFAR-10, evaluated across a sweep of L2 perturbation budgets.",16,TEXT,"600"))
    # c2 3-class setup (left)
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,240,560,150,fill=PANEL,stroke=STROKE)+
        rect(64,240,6,150,fill=TEAL,rx=6,sw=0)+
        T(92,282,"3-class studies  ·  1000 samples / class",17,TEAL,"800")+
        para(92,316,"A tractable multi-class setting for the exact hypergraph.",14.5,SEC,58,22)[0]+
        chip(92,350,"MNIST 1 / 4 / 7      CIFAR-10 plane / bird / ship",TEAL,w=468,h=30))
    # c3 full 10-class (right)
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,240,560,150,fill=PANEL,stroke=STROKE)+
        rect(656,240,6,150,fill=GOLD,rx=6,sw=0)+
        T(684,282,"Full 10-class problem",17,GOLD,"800")+
        para(684,316,"Efficient bounds are also computed on the complete training sets.",14.5,SEC,58,22)[0]+
        chip(684,350,"MNIST 10-class   ·   CIFAR-10 10-class  (full data)",GOLD,w=468,h=30))
    # c4 reference defenses
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(64,410,1152,140,fill="#2A1720",stroke=RED,rx=14,sw=1.5)+
        rect(64,410,6,140,fill=RED,rx=6,sw=0)+
        T(92,448,"Reference defenses  ·  TRADES adversarial training",17,RED,"800")+
        para(92,480,"A small convolutional network for MNIST and a wide residual network for CIFAR-10, both evaluated with the strong APGD attack from AutoAttack.",14.5,TEXT,110,23)[0])
    return svg(b)

# ---------- SLIDE 7: KEY RESULT ----------
def s_result():
    ch=chunks("key-result"); b=header("Key Result","A large, previously unquantified gap")
    # c1 headline strip
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,150,1152,50,fill=PANEL,stroke=STROKE)+
        rect(64,150,6,50,fill=RED,rx=6,sw=0)+
        T(92,182,"Adversarially trained classifiers land far from the optimum, and the gap is much wider than in the binary case.",16.5,TEXT,"700"))
    # c2 3-class CIFAR-10 bars (left)
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,214,560,264,fill=PANEL,stroke=STROKE)+
        rect(64,214,6,264,fill=TEAL,rx=6,sw=0)+
        T(92,250,"3-class CIFAR-10 0-1 loss  ·  lower is better",15.5,TEAL,"800")+
        bar(300,282,250,0.60,1.0,RED,"TRADES training","0.60",h=32)+
        bar(300,336,250,0.01,1.0,GREEN,"optimal achievable","~0",h=32)+
        rect(92,392,504,70,fill="#2A1720",stroke=RED,rx=10,sw=1.5)+
        T(112,420,"At this budget the optimum is essentially zero,",14,TEXT,"700")+
        T(112,442,"yet TRADES cannot beat 0.60 loss.",14,RED,"800"))
    # c3 10-class sandwich (right)
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,214,560,264,fill=PANEL,stroke=STROKE)+
        rect(656,214,6,264,fill=GOLD,rx=6,sw=0)+
        T(684,250,"10-class  ·  bounds sandwich the optimum",15.5,GOLD,"800")+
        _sandwich(700,272,500,150)+
        T(684,452,"Lower and upper bounds nearly coincide, so the gap is not an artifact of loose bounds.",13.5,SEC,"600"))
    # c4 takeaway strip
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(64,492,1152,116,fill=PANEL,stroke=STROKE)+
        rect(64,492,6,116,fill=ACCENT,rx=6,sw=0)+
        T(92,526,"Robust training struggles more as classes grow",16,ACCENT,"800")+
        para(92,556,"The gap widens with the number of classes: what looks tolerable in the binary case becomes a large shortfall once several classes interact.",14.5,SEC,90,22)[0])
    b+=T(64,648,"The bottleneck is the training method, not a fundamental limit of the data.",14,SEC,"600")
    return svg(b)

def _sandwich(x,y,w,h):
    # optimal band bracketed tightly by lower/upper bounds, rising with budget
    box=rect(x,y,w,h,fill="#0E2334",stroke=STROKE,rx=8)
    def curve(off,amp):
        pts=[]
        for i in range(0,w-40+1,10):
            t=i/(w-40); v=off+amp*(t**1.4)
            pts.append((x+30+i, y+h-18-int(v*(h-40))))
        return pts
    lo=curve(0.05,0.62); up=curve(0.10,0.66)
    # shaded band between
    band=("<path d=\"M "+" L ".join(f"{px},{py}" for px,py in lo)+
          " L "+" L ".join(f"{px},{py}" for px,py in reversed(up))+
          f" Z\" fill=\"{GOLD}\" opacity=\"0.16\"/>")
    body=(box+band+poly(lo,stroke=GREEN,sw=2.5)+poly(up,stroke=GOLD,sw=2.5)+
          T(x+w-10,y+22,"upper bound",11,GOLD,"700",anchor="end")+
          T(x+w-10,y+h-24,"lower bound",11,GREEN,"700",anchor="end")+
          T(x+34,y+h-4,"attack budget ->",11,TER,"600"))
    return body

# ---------- SLIDE 8: ABLATION ----------
def s_ablation():
    ch=chunks("ablation-study"); b=header("Ablation Study","Do higher-order hyperedges matter?")
    # c1 setup (left top)
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,560,112,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,112,fill=ACCENT,rx=6,sw=0)+
        T(92,196,"The question",16.5,ACCENT,"800")+
        para(92,226,"How much do the higher-order hyperedges, the triples and quadruples, actually change the computed bound?",14.5,SEC,54,22)[0])
    # c2 edge-only vs +deg3/4 bars (left bottom)
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,286,560,264,fill=PANEL,stroke=STROKE)+
        rect(64,286,6,264,fill=TEAL,rx=6,sw=0)+
        T(92,322,"Lower bound at small budget  ·  nearly identical",14.5,TEXT,"800")+
        bar(300,350,230,0.482,0.6,ACCENT,"edges only","0.482",h=30)+
        bar(300,398,230,0.483,0.6,TEAL,"+ degree 3","0.483",h=30)+
        bar(300,446,230,0.483,0.6,GREEN,"+ degree 4","0.483",h=30)+
        rect(92,494,504,44,fill="#0F2E2B",stroke=TEAL,rx=10,sw=1.5)+
        T(112,522,"Adding millions of hyperedges moves the bound by ~0",14,TEAL,"800"))
    # c3 scale of higher-order structures (right top)
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,158,560,180,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(656,158,6,180,fill=GOLD,rx=6,sw=0)+
        T(684,196,"CIFAR-10 at budget 3  ·  sheer count",16.5,GOLD,"800")+
        kpi(684,220,"~3M","degree-3 hyperedges",GOLD,w=250,h=96,nsize=32)+
        kpi(962,220,"~10M","degree-4 hyperedges",GOLD,w=250,h=96,nsize=32)+
        T(684,332,"...yet they leave the bound unchanged.",13.5,SEC,"600"))
    # c4 practical verdict (right bottom)
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(656,354,560,196,fill=PANEL,stroke=STROKE)+
        rect(656,354,6,196,fill=GREEN,rx=6,sw=0)+
        T(684,392,"Practical verdict",16.5,GREEN,"800")+
        para(684,424,"Edge-only bounds are both cheap and accurate in the practical low-budget regime.",14.5,SEC,56,22)[0]+
        chip(684,474,"Aggregated binary bound: fastest, but much looser",GOLD,w=504,h=30)+
        chip(684,510,"Scaling up model architecture: only minor gains",ACCENT,w=504,h=30))
    return svg(b)

# ---------- SLIDE 9: HEADLINE NUMBERS ----------
def s_headline():
    ch=chunks("headline-numbers"); b=header("Headline Numbers","The gap, made concrete")
    # c1 3-class CIFAR-10 plateau (full width)
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,162,1152,120,fill=PANEL,stroke=STROKE)+
        rect(64,162,6,120,fill=RED,rx=6,sw=0)+
        T(92,198,"3-class CIFAR-10  ·  adversarial training plateaus",16.5,RED,"800")+
        kpi(92,214,"0.60","TRADES 0-1 loss",RED,w=220,h=54,nsize=26)+
        T(330,254,"vs",22,SEC,"800",anchor="middle")+
        kpi(360,214,"~0","optimal loss",GREEN,w=220,h=54,nsize=26)+
        rect(600,214,616,54,fill=PANEL2,stroke=STROKE,rx=12)+
        T(624,247,"Adv. training cannot beat 0.60 where the optimum is essentially zero.",14,SEC,"600"))
    # c2 MNIST certified (left)
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,298,560,138,fill=PANEL,stroke=STROKE)+
        rect(64,298,6,138,fill=ACCENT,rx=6,sw=0)+
        T(92,334,"Best certified MNIST model  ·  optimal LB = 0",15.5,ACCENT,"800")+
        kpi(92,352,"0.27","loss @ budget 1.52",ACCENT,w=250,h=72,nsize=28)+
        kpi(360,352,"0.44","loss @ budget 2.0",ACCENT,w=250,h=72,nsize=28))
    # c3 CIFAR-10 certified (right)
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,298,560,138,fill=PANEL,stroke=STROKE)+
        rect(656,298,6,138,fill=TEAL,rx=6,sw=0)+
        T(684,334,"Best certified CIFAR-10 model  ·  optimal LB = 0",15.5,TEAL,"800")+
        kpi(684,352,"0.60","loss @ budget 1.0",TEAL,w=250,h=72,nsize=28)+
        kpi(952,352,"0.80","loss @ budget 2.0",TEAL,w=250,h=72,nsize=28))
    # c4 structural (full width)
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(64,452,1152,120,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(64,452,6,120,fill=GOLD,rx=6,sw=0)+
        T(92,488,"Structural surprise  ·  CIFAR-10 at budget 3",16.5,GOLD,"800")+
        kpi(92,504,"~3M","degree-3 edges",GOLD,w=230,h=56,nsize=26)+
        kpi(340,504,"~10M","degree-4 edges",GOLD,w=230,h=56,nsize=26)+
        rect(590,504,626,56,fill=PANEL2,stroke=STROKE,rx=12)+
        T(614,538,"Millions of higher-degree hyperedges leave the bound completely unchanged.",13.5,SEC,"600"))
    b+=T(64,602,"Certified-robustness numbers from the paper; optimal lower bound is zero in every row above.",13,TER,"600")
    return svg(b)

# ---------- SLIDE 10: TAKEAWAY ----------
def s_takeaway():
    ch=chunks("takeaway"); b=header("Takeaway","A measurable gap, and a tool to close it")
    cards=[
        (ch[0],RED,"The gap is large and now measurable","Multi-class robust classification has a large, now-quantifiable gap between what current defenses achieve and what is theoretically possible, far worse than in the binary case."),
        (ch[1],TEAL,"A computable optimum with cheap bounds","The conflict-hypergraph framework computes the optimal 0-1 loss as a linear program, and edge-only truncated bounds pin that optimum down tightly in the practical low-budget regime."),
        (ch[2],GREEN,"A fast diagnostic for future defenses","This gives practitioners a fast tool to see how much robustness is still on the table, pointing research toward closing the gap rather than endlessly iterating attacks and defenses."),
    ]
    y=176
    for c,col,ti,tx in cards:
        body=(rect(64,y,1152,116,fill=PANEL,stroke=STROKE)+
              rect(64,y,6,116,fill=col,rx=6,sw=0)+
              circle(112,y+58,10,fill=col)+
              T(150,y+46,ti,19,TEXT,"800"))
        body+=para(150,y+78,tx,15.5,SEC,92,24)[0]
        b+=anchor(c["aid"],c["kw"],body)
        y+=132
    b+=line(64,596,1216,596,STROKE,1)
    b+=T(64,632,"Characterizing the Optimal 0-1 Loss for Multi-class Classification with a Test-time Attacker",15.5,TEXT,"700")
    b+=T(64,660,"NeurIPS 2023  ·  Dai et al.  ·  arXiv:2302.10722  ·  github.com/inspire-group/multiclass_robust_lb",13.5,SEC,"600")
    return svg(b)

SLIDES=[("01_title",s_title),("02_problem",s_problem),("03_motivation",s_motivation),
        ("04_contribution",s_contribution),("05_method",s_method),("06_dataset",s_dataset),
        ("07_key_result",s_result),("08_ablation",s_ablation),("09_headline",s_headline),
        ("10_takeaway",s_takeaway)]

for name,fn in SLIDES:
    open(os.path.join(OUT,name+".svg"),"w").write(fn())
    print("wrote",name)
print("DONE",len(SLIDES))
