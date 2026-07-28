#!/usr/bin/env python3
"""All-native SVG deck builder for paper2video run 002
(Transformers, parallel computation, and logarithmic depth / ICML 2024).
Reads _anchor_map.json; wraps each narration chunk in its own <g id="cue_..."> card
with a <title> holding the cue keywords, so the strict --require-pptx-anchors cue
pass resolves every anchor from PPTX geometry. All-native: zero <image>, zero gradients.
Every slide carries exactly 4 anchor groups, one per narration chunk."""
import json, os, math

HERE = os.path.dirname(os.path.abspath(__file__))
META = os.environ["VIDEO_META"]
OUT  = os.path.join(HERE, "svg_output")
os.makedirs(OUT, exist_ok=True)
AM = json.load(open(os.path.join(META, "_anchor_map.json")))

W, H = 1280, 720
BG="#0B1B2B"; PANEL="#12293D"; PANEL2="#16324A"; STROKE="#26455F"
ACCENT="#4C9BE8"; TEAL="#34D3C0"; GOLD="#F2C14E"; RED="#F2685C"; GREEN="#48C78E"; VIOLET="#B79CF0"
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

def poly(points,fill="none",stroke=None,sw=2,opacity=None,dash=None):
    st=f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    o=f' opacity="{opacity}"' if opacity is not None else ""
    d=f' stroke-dasharray="{dash}"' if dash else ""
    pts=" ".join(f"{a},{b}" for a,b in points)
    return f'<polyline points="{pts}" fill="{fill}"{st}{o}{d}/>'

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

def kpi(x,y,w,num,lbl,col,nsize=34,h=104,ff=SANS):
    return (rect(x,y,w,h,fill=PANEL2,stroke=STROKE,rx=12)+
            T(x+w/2,y+h*0.52,num,nsize,col,"800",anchor="middle",ff=ff)+
            T(x+w/2,y+h*0.80,lbl,13,SEC,"600",anchor="middle"))

def chip(x,y,w,text,col,h=34,sz=14.5):
    return (rect(x,y,w,h,fill=PANEL2,stroke=STROKE,rx=8)+
            circle(x+18,y+h/2,5,fill=col)+
            T(x+34,y+h/2+5,text,sz,TEXT,"600"))

# ---------- SLIDE 1: TITLE ----------
def s_title():
    ch=chunks("title"); b=""
    b+=T(64,72,"ICML 2024",14,ACCENT,"800",ls="3")
    b+=T(1216,72,"Columbia University  ·  Courant Institute, NYU",14,SEC,"600",anchor="end")
    b+=line(64,88,1216,88,STROKE,1)
    b+=T(64,150,"Transformers, Parallel Computation,",34,WHITE,"800")
    b+=T(64,192,"and Logarithmic Depth",34,ACCENT,"800")
    b+=rect(64,216,150,30,fill="#0F2E2B",stroke=TEAL,rx=15,sw=1.5)+T(139,236,"Parallelism",16,TEAL,"800",anchor="middle")
    b+=T(230,236,"is what makes the transformer special",15,SEC,"600")
    b+=T(64,272,"Clayton Sanford  ·  Daniel Hsu  ·  Matus Telgarsky",15,TER,"500")
    # four concept cards
    cy=300; cw=274; gap=18; cx=64
    data=[
        (ch[0],ACCENT,"The answer: parallelism","Self-attention lets every token interact at once. This paper argues that parallelism, not scale, is the transformer's defining strength."),
        (ch[1],TEAL,"Transformers = MPC","A tight, two-way correspondence between transformers and the Massively Parallel Computation model used to study distributed algorithms."),
        (ch[2],GOLD,"Log depth beats serial","A log-depth transformer solves reasoning tasks that RNNs, state-space models like Mamba, and sub-quadratic attention provably cannot do efficiently."),
        (ch[3],GREEN,"Verified empirically","On the synthetic k-hop induction heads task, trained transformers obey exactly the logarithmic depth threshold the theory predicts."),
    ]
    for i,(c,col,ti,tx) in enumerate(data):
        x=cx+i*(cw+gap)
        body=(rect(x,cy,cw,226,fill=PANEL,stroke=STROKE)+
              rect(x,cy,cw,6,fill=col,rx=6,sw=0)+
              circle(x+28,cy+48,7,fill=col)+
              T(x+46,cy+54,ti,15.5,TEXT,"800"))
        body+=para(x+22,cy+94,tx,13.5,SEC,32,22)[0]
        b+=anchor(c["aid"],c["kw"],body)
    b+=line(64,570,1216,570,STROKE,1)
    b+=T(64,606,"arXiv:2402.09268",14,ACCENT,"700")
    b+=T(320,606,"github.com/chsanford/hop-induction-heads",14,SEC,"600")
    b+=T(1216,606,"Log-depth transformers  =  constant-round parallel computation",14,TEAL,"700",anchor="end")
    return svg(b)

# ---------- SLIDE 2: PROBLEM ----------
def s_problem():
    ch=chunks("problem"); b=header("Problem","Theory has not said what makes transformers special")
    # c1 left -- universality
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,152,560,196,fill=PANEL,stroke=STROKE)+
        rect(64,152,6,196,fill=GOLD,rx=6,sw=0)+
        T(92,190,"Line 1  ·  universality",16.5,GOLD,"800")+
        para(92,222,"Transformers dominate sequence modeling, yet the theory of why is unsatisfying. One line proves universality, but only for enormous models.",14.5,SEC,58,23)[0]+
        chip(92,300,504,"tells us nothing about size-efficient tasks",GOLD,32,13.5))
    # c2 right -- constant depth
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(656,152,560,196,fill=PANEL,stroke=STROKE)+
        rect(656,152,6,196,fill=RED,rx=6,sw=0)+
        T(684,190,"Line 2  ·  constant depth, growing context",16.5,RED,"800")+
        para(684,222,"A second line fixes depth and grows context length. There, many basic algorithmic tasks are simply impossible.",14.5,SEC,58,23)[0]+
        chip(684,300,504,"matching parentheses  ->  provably out of reach",RED,32,13.5))
    # c3 band -- neither isolates
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(64,364,1152,84,fill=PANEL,stroke=STROKE)+
        rect(64,364,6,84,fill=ACCENT,rx=6,sw=0)+
        T(92,398,"Neither picture isolates the distinguishing property",16,ACCENT,"800")+
        para(92,426,"Neither view pins down what actually sets transformers apart from recurrent networks or other architectures.",14.5,SEC,110,22)[0])
    # c4 band -- the question
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(64,464,1152,86,fill="#0F2E2B",stroke=TEAL,rx=14,sw=1.5)+
        rect(64,464,6,86,fill=TEAL,rx=6,sw=0)+
        T(92,498,"This paper asks",15,TEAL,"800",ls="1")+
        T(92,528,"Is there a single, clean computational property that captures the strengths AND the limits of transformers at once?",15.5,TEXT,"700"))
    return svg(b)

# ---------- SLIDE 3: MOTIVATION ----------
def s_motivation():
    ch=chunks("motivation"); b=header("Motivation","Self-attention is fundamentally parallel")
    # c1 top band -- insight
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,152,1152,74,fill=PANEL,stroke=STROKE)+
        rect(64,152,6,74,fill=ACCENT,rx=6,sw=0)+
        T(92,186,"The authors' insight",15,ACCENT,"800",ls="1")+
        T(92,214,"Self-attention is fundamentally a parallel operation, not a serial one.",15.5,TEXT,"700"))
    # c2 left -- attention vs recurrence diagram
    body=(rect(64,244,560,196,fill=PANEL,stroke=STROKE)+
        rect(64,244,6,196,fill=TEAL,rx=6,sw=0)+
        T(92,282,"All pairs interact in one layer",16.5,TEAL,"800"))
    # attention: fully-connected token row
    ax=[130,230,330,430]; ay=318
    # draw arcs as thin lines above the row
    for i in range(4):
        for j in range(i+1,4):
            mx=(ax[i]+ax[j])/2; my=ay-18-6*(j-i)
            body+=f'<path d="M{ax[i]},{ay} Q{mx},{my} {ax[j]},{ay}" fill="none" stroke="{TEAL}" stroke-width="1.2" opacity="0.75"/>'
    for i in range(4):
        body+=circle(ax[i],ay,9,fill=PANEL2,stroke=TEAL,sw=1.6)
    body+=T(280,352,"attention  ·  parallel",13,TEAL,"700",anchor="middle")
    # recurrence: chain with arrows
    rx=[130,230,330,430]; ry=392
    for i in range(3):
        body+=line(rx[i]+9,ry,rx[i+1]-9,ry,GOLD,1.6)
        body+=f'<path d="M{rx[i+1]-9},{ry} l-6,-3 l0,6 z" fill="{GOLD}"/>'
    for i in range(4):
        body+=circle(rx[i],ry,9,fill=PANEL2,stroke=GOLD,sw=1.6)
    body+=T(280,418,"recurrence  ·  one step at a time",13,GOLD,"700",anchor="middle")
    b+=anchor(ch[1]["aid"],ch[1]["kw"],body)
    # c3 right -- MPC model
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,244,560,196,fill=PANEL,stroke=STROKE)+
        rect(656,244,6,196,fill=VIOLET,rx=6,sw=0)+
        T(684,282,"That looks like MPC",16.5,VIOLET,"800")+
        para(684,312,"Massively Parallel Computation, the theory behind MapReduce-style systems: many machines each hold a little data and exchange messages in synchronous rounds.",14,SEC,60,22)[0]+
        chip(684,398,504,"attention layer  <->  one MPC round",VIOLET,32,13.5))
    # c4 bottom band -- the bet
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(64,456,1152,94,fill="#0F2E2B",stroke=TEAL,rx=14,sw=1.5)+
        rect(64,456,6,94,fill=GREEN,rx=6,sw=0)+
        T(92,490,"The paper's bet",15,GREEN,"800",ls="1")+
        para(92,518,"Make the connection between attention layers and MPC rounds precise, and you get a single lens that explains both what transformers can do and what they cannot.",15,TEXT,116,22)[0])
    return svg(b)

# ---------- SLIDE 4: CONTRIBUTION ----------
def s_contribution():
    ch=chunks("contribution"); b=header("Contribution","A correspondence, and a task that proves it")
    # c1 top band -- two contributions / correspondence
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,152,1152,104,fill=PANEL,stroke=STROKE)+
        rect(64,152,6,104,fill=ACCENT,rx=6,sw=0)+
        T(92,184,"Contribution 1  ·  a tight two-way correspondence",16.5,ACCENT,"800")+
        rect(300,196,300,44,fill=PANEL2,stroke=STROKE,rx=8)+
        T(450,223,"R-round MPC  ->  depth R+1",14,TEAL,"800",anchor="middle",ff=MONO)+
        rect(620,196,300,44,fill=PANEL2,stroke=STROKE,rx=8)+
        T(770,223,"depth-L  ->  O(L)-round MPC",14,GOLD,"800",anchor="middle",ff=MONO)+
        T(950,214,"both directions",13.5,SEC,"700"))
    # three supporting cards
    cw=368; gap=24; x0=64; cy=272; chh=278
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(x0,cy,cw,chh,fill=PANEL,stroke=STROKE)+
        rect(x0,cy,cw,6,fill=TEAL,rx=6,sw=0)+
        T(x0+28,cy+44,"Power = MPC",17,TEAL,"800")+
        para(x0+28,cy+78,"So the algorithmic power of logarithmic-depth transformers is captured, up to constants, exactly by the MPC model.",14.5,SEC,40,23)[0]+
        chip(x0+28,cy+210,cw-56,"log-depth transformer  ==  const-round MPC",TEAL,34,12.5))
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(x0+cw+gap,cy,cw,chh,fill=PANEL,stroke=STROKE)+
        rect(x0+cw+gap,cy,cw,6,fill=GOLD,rx=6,sw=0)+
        T(x0+cw+gap+28,cy+44,"Free algorithms",17,GOLD,"800")+
        para(x0+cw+gap+28,cy+78,"The connection instantly yields log-depth transformers for classic parallel problems like graph connectivity.",14.5,SEC,40,23)[0]+
        chip(x0+cw+gap+28,cy+210,cw-56,"near-optimal under an MPC conjecture",GOLD,34,12.5))
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(x0+2*(cw+gap),cy,cw,chh,fill="#0F2E2B",stroke=GREEN,rx=14,sw=1.5)+
        rect(x0+2*(cw+gap),cy,cw,6,fill=GREEN,rx=6,sw=0)+
        T(x0+2*(cw+gap)+28,cy+44,"Contribution 2  ·  k-hop",16.5,GREEN,"800")+
        para(x0+2*(cw+gap)+28,cy+78,"A concrete synthetic task, k-hop induction heads: log-depth transformers solve it while competing architectures cannot do so efficiently.",14.5,TEXT,40,23)[0]+
        chip(x0+2*(cw+gap)+28,cy+210,cw-56,"trained models obey the threshold",GREEN,34,12.5))
    return svg(b)

# ---------- SLIDE 5: METHOD ----------
def s_method():
    ch=chunks("method"); b=header("Method","A single attention layer routes one MPC round")
    gx=[64,648]; gy=[152,362]; cw=568; chh=198
    # c1 routing gadget + diagram
    body=(rect(gx[0],gy[0],cw,chh,fill=PANEL,stroke=STROKE)+
        rect(gx[0],gy[0],6,chh,fill=ACCENT,rx=6,sw=0)+
        T(gx[0]+28,gy[0]+38,"The routing gadget",16.5,ACCENT,"800")+
        para(gx[0]+28,gy[0]+66,"In MPC each round ends with machines sending addressed messages. One self-attention layer performs exactly this routing.",14,SEC,60,21)[0])
    # small routing diagram: 3 senders -> 3 receivers
    sxs=[gx[0]+70,gx[0]+70,gx[0]+70]; rxs=[gx[0]+300,gx[0]+300,gx[0]+300]
    ys=[gy[0]+128,gy[0]+152,gy[0]+176]
    routes=[(0,1),(1,2),(2,0)]
    for a,r in routes:
        body+=line(gx[0]+82,ys[a],gx[0]+288,ys[r],TEAL,1.4)
    for i in range(3):
        body+=circle(gx[0]+76,ys[i],7,fill=PANEL2,stroke=ACCENT,sw=1.5)
        body+=circle(gx[0]+294,ys[i],7,fill=PANEL2,stroke=TEAL,sw=1.5)
    body+=T(gx[0]+76,gy[0]+196,"machines",11.5,SEC,"600",anchor="middle")
    body+=T(gx[0]+294,gy[0]+196,"routed msgs",11.5,SEC,"600",anchor="middle")
    body+=T(gx[0]+420,ys[1]+4,"= 1 attention layer",13,ACCENT,"800",anchor="middle")
    b+=anchor(ch[0]["aid"],ch[0]["kw"],body)
    # c2 Lemma 3.2
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(gx[1],gy[0],cw,chh,fill=PANEL,stroke=STROKE)+
        rect(gx[1],gy[0],6,chh,fill=GOLD,rx=6,sw=0)+
        T(gx[1]+28,gy[0]+38,"Lemma 3.2  ·  keep it tall and skinny",16.5,GOLD,"800")+
        para(gx[1]+28,gy[0]+66,"Encode each message redundantly with multiple hashing, and move it with sparse propagation.",14,SEC,60,21)[0]+
        chip(gx[1]+28,gy[0]+114,cw-56,"multiple hashing  +  sparse propagation",GOLD,32,13)+
        chip(gx[1]+28,gy[0]+154,cw-56,"tall-skinny Q/K/V  ->  small embedding dim",TEAL,32,13))
    # c3 stack -> depth, and reverse
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(gx[0],gy[1],cw,chh,fill=PANEL,stroke=STROKE)+
        rect(gx[0],gy[1],6,chh,fill=TEAL,rx=6,sw=0)+
        T(gx[0]+28,gy[1]+38,"Stack the layers",16.5,TEAL,"800")+
        rect(gx[0]+28,gy[1]+58,cw-56,46,fill=PANEL2,stroke=STROKE,rx=8)+
        T(gx[0]+cw/2,gy[1]+86,"R communication rounds  ->  depth R + 1",14.5,TEXT,"800",anchor="middle",ff=MONO)+
        para(gx[0]+28,gy[1]+126,"The reverse direction packs a whole transformer layer into one MPC round, so transformers are no stronger than the model.",13.5,SEC,62,21)[0])
    # c4 k-hop construction
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(gx[1],gy[1],cw,chh,fill="#0F2E2B",stroke=GREEN,rx=14,sw=1.5)+
        rect(gx[1],gy[1],6,chh,fill=GREEN,rx=6,sw=0)+
        T(gx[1]+28,gy[1]+38,"The k-hop construction",16.5,GREEN,"800")+
        para(gx[1]+28,gy[1]+66,"A tailored, causally-masked construction of constant width, with depth exactly:",14,SEC,60,21)[0]+
        rect(gx[1]+28,gy[1]+108,cw-56,58,fill=PANEL2,stroke=GREEN,rx=10,sw=1.5)+
        T(gx[1]+cw/2,gy[1]+144,"L  =  floor( log2 k )  +  2",20,GREEN,"800",anchor="middle",ff=MONO))
    return svg(b)

# ---------- SLIDE 6: DATASET ----------
def s_dataset():
    ch=chunks("dataset-benchmark"); b=header("Dataset / Benchmark","The k-hop induction heads task")
    # c1 top band -- standard induction heads
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,152,1152,96,fill=PANEL,stroke=STROKE)+
        rect(64,152,6,96,fill=ACCENT,rx=6,sw=0)+
        T(92,186,"Start from standard induction heads",16,ACCENT,"800")+
        para(92,214,"Complete a bigram: predict the token that followed the last occurrence of the current token.",14.5,SEC,72,22)[0]+
        # mini sequence
        T(700,196,"... a  b ...  c  d ...  a  ->  ?",15,TEXT,"800",ff=MONO)+
        T(700,224,"last 'a' was followed by 'b'  ->  predict b",13,TEAL,"700",ff=MONO))
    # c2 left -- k-hop chaining
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,264,560,150,fill=PANEL,stroke=STROKE)+
        rect(64,264,6,150,fill=GOLD,rx=6,sw=0)+
        T(92,300,"k-hop chains the lookup",16.5,GOLD,"800")+
        para(92,330,"Use one completion to decide which bigram to complete next, k times over.",14.5,SEC,58,22)[0]+
        chip(92,372,504,"hop_k  =  find, then find again, k times",GOLD,32,13.5))
    # c3 right -- stress test / parallel folding
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,264,560,150,fill=PANEL,stroke=STROKE)+
        rect(656,264,6,150,fill=TEAL,rx=6,sw=0)+
        T(684,300,"Why it is a stress test",16.5,TEAL,"800")+
        para(684,330,"It looks like it needs k sequential steps, yet a parallel architecture can fold it into logarithmically many.",14.5,SEC,58,22)[0]+
        chip(684,372,504,"k serial steps  ->  log k parallel depth",TEAL,32,13.5))
    # c4 bottom band -- config
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(64,430,1152,120,fill="#0F2E2B",stroke=GREEN,rx=14,sw=1.5)+
        rect(64,430,6,120,fill=GREEN,rx=6,sw=0)+
        T(92,464,"Training / evaluation setup",16,GREEN,"800")+
        kpi(92,478,262,"N = 100","sequence length",ACCENT,30,60)+
        kpi(366,478,262,"|Sigma| = 4","symbol alphabet",TEAL,30,60)+
        kpi(640,478,262,"k = 0 .. 16","hop counts swept",GOLD,30,60)+
        kpi(914,478,262,"multi-task","one model, random k",GREEN,26,60))
    return svg(b)

# ---------- SLIDE 7: KEY RESULT ----------
def s_result():
    ch=chunks("key-result"); b=header("Key Result","Each layer doubles the reachable hop count")
    # c1 left top -- theory: necessary & sufficient
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,152,560,138,fill=PANEL,stroke=STROKE)+
        rect(64,152,6,138,fill=TEAL,rx=6,sw=0)+
        T(92,188,"Theory  ·  log depth is necessary",16,TEAL,"800")+
        para(92,218,"Logarithmic depth is not just sufficient but necessary: any transformer solving k-hop needs depth on the order of log k.",14.5,SEC,58,22)[0]+
        chip(92,256,504,"depth  =  Theta( log k )",TEAL,28,13.5))
    # c2 left mid -- experiment setup
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,304,560,120,fill=PANEL,stroke=STROKE)+
        rect(64,304,6,120,fill=ACCENT,rx=6,sw=0)+
        T(92,340,"Experiment  ·  train depths 2 - 6",16,ACCENT,"800")+
        para(92,370,"Train transformers of depths two through six and measure token-wise error as k grows. The picture is remarkably clean.",14.5,SEC,58,22)[0])
    # c4 left bottom -- threshold + interpretable
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(64,438,560,112,fill="#0F2E2B",stroke=GREEN,rx=14,sw=1.5)+
        rect(64,438,6,112,fill=GREEN,rx=6,sw=0)+
        T(92,472,"Threshold matches to the layer",15.5,GREEN,"800")+
        T(92,502,"empirical boundary  =  floor(log2 k) + 2",14.5,GREEN,"800",ff=MONO)+
        T(92,530,"learned attention patterns mirror the hand-designed proof",13.5,SEC,"700"))
    # c3 right -- the doubling chart
    body=(rect(656,152,560,398,fill=PANEL,stroke=STROKE)+
        rect(656,152,6,398,fill=GOLD,rx=6,sw=0)+
        T(684,188,"+1 layer  ~  2x the largest learnable k",15.5,GOLD,"800"))
    body+=_double_chart(700,212,486,300)
    b+=anchor(ch[2]["aid"],ch[2]["kw"],body)
    return svg(b)

def _double_chart(x,y,w,h):
    out=rect(x,y,w,h,fill="#0E2334",stroke=STROKE,rx=10)
    ox=x+52; oy=y+h-40; pw=w-84; ph=h-70
    out+=line(ox,y+14,ox,oy,STROKE,1.5)
    out+=line(ox,oy,ox+pw,oy,STROKE,1.5)
    depths=[2,3,4,5,6]; kmax=[1,2,4,8,16]; cols=[TER,SEC,ACCENT,TEAL,GREEN]
    vmax=16.0
    n=len(depths); slot=pw/n; bw=slot*0.52
    for yv in [0,4,8,12,16]:
        yy=oy-ph*(yv/vmax)
        out+=line(ox,yy,ox+pw,yy,STROKE,1,dash="2 5")
        out+=T(ox-10,yy+4,str(yv),11,TER,"600",anchor="end")
    for i,(d,km,c) in enumerate(zip(depths,kmax,cols)):
        cx=ox+slot*i+slot/2
        bh=ph*(km/vmax)
        out+=rect(cx-bw/2,oy-bh,bw,bh,fill=c,rx=5,sw=0)
        out+=T(cx,oy-bh-8,f"k<={km}",13,c,"800",anchor="middle")
        out+=T(cx,oy+18,f"L={d}",12.5,SEC,"700",anchor="middle")
    out+=T(x+w/2,y+h-6,"transformer depth L   ->   largest solvable k = 2^(L-2)",11.5,SEC,"700",anchor="middle")
    # doubling arrows annotation
    out+=T(ox+pw-6,y+30,"each step doubles",11.5,GOLD,"800",anchor="end")
    return out

# ---------- SLIDE 8: ABLATION ----------
def s_ablation():
    ch=chunks("ablation-study"); b=header("Ablation Study","It is really about depth, not size")
    # c1 top band
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,152,1152,58,fill=PANEL,stroke=STROKE)+
        rect(64,152,6,58,fill=ACCENT,rx=6,sw=0)+
        T(92,188,"The depth sweep (L = 2..6) is the main ablation: it cleanly traces out the logarithmic threshold.",16,TEXT,"600"))
    # c2 left -- widen models
    body=(rect(64,230,560,164,fill=PANEL,stroke=STROKE)+
        rect(64,230,6,164,fill=GOLD,rx=6,sw=0)+
        T(92,268,"Widen the model  ·  boundary barely moves",16,GOLD,"800"))
    body+=chip(92,288,504,"m=128, H=4   ->   m=256, H=8",GOLD,34,14)
    body+=para(92,352,"The depth-versus-k boundary hardly shifts: the dependence is about depth, not sheer size.",13.5,SEC,66,20)[0]
    b+=anchor(ch[1]["aid"],ch[1]["kw"],body)
    # c3 right -- finite sample
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,230,560,164,fill=PANEL,stroke=STROKE)+
        rect(656,230,6,164,fill=TEAL,rx=6,sw=0)+
        T(684,268,"Finite-sample regime",16,TEAL,"800")+
        para(684,300,"Where overfitting is a risk, deeper models generalize better, hinting at an inductive bias suited to compositional tasks.",14.5,SEC,58,22)[0]+
        chip(684,356,504,"deeper  ->  better generalization",TEAL,30,13.5))
    # c4 bottom band -- interpretability
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(64,414,1152,136,fill="#0F2E2B",stroke=GREEN,rx=14,sw=1.5)+
        rect(64,414,6,136,fill=GREEN,rx=6,sw=0)+
        T(92,448,"Crack open the trained network",16,GREEN,"800")+
        para(92,478,"The attention matrices line up with the intermediate pointer computations from the proof: the learned solution mechanistically resembles the theoretical construction.",14.5,TEXT,104,23)[0]+
        chip(92,520,1096,"learned attention heads  ==  the find^j pointers used in the proof",GREEN,24,13.5))
    return svg(b)

# ---------- SLIDE 9: HEADLINE NUMBERS ----------
def s_headline():
    ch=chunks("headline-numbers"); b=header("Headline Numbers","Logarithmic, where the alternatives are linear")
    # c1 top band -- depth formula + doubling
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,152,1152,74,fill=PANEL,stroke=STROKE)+
        rect(64,152,6,74,fill=ACCENT,rx=6,sw=0)+
        T(92,182,"Depth to solve k-hop, in proof and in trained networks",15.5,ACCENT,"800")+
        chip(92,192,470,"L  =  floor(log2 k) + 2",TEAL,30,13.5)+
        chip(576,192,470,"+1 layer  ~  2x k    (6 layers -> k <= 16)",GOLD,30,13.5))
    # two KPI cards -- simulation constants
    cw=560; x0=64; cy=246; chh=132
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(x0,cy,cw,chh,fill=PANEL,stroke=STROKE)+
        rect(x0,cy,cw,6,fill=TEAL,rx=6,sw=0)+
        T(x0+28,cy+40,"Simulation constants are clean",16,TEAL,"800")+
        rect(x0+28,cy+58,cw-56,54,fill=PANEL2,stroke=STROKE,rx=8)+
        T(x0+cw/2,cy+82,"R-round MPC  ->  depth R + 1",14,TEXT,"800",anchor="middle",ff=MONO)+
        T(x0+cw/2,cy+102,"depth-L transformer  ->  O(L)-round MPC",14,SEC,"800",anchor="middle",ff=MONO))
    # c3 right -- competitor bars
    body=(rect(x0+cw+24,cy,cw,chh,fill=PANEL,stroke=STROKE)+
        rect(x0+cw+24,cy,cw,6,fill=RED,rx=6,sw=0)+
        T(x0+cw+24+28,cy+40,"Competitors need depth L >= k",16,RED,"800")+
        chip(x0+cw+24+28,cy+58,cw-56,"multi-layer RNN / Mamba   (Cor. 5.2)",RED,24,13)+
        chip(x0+cw+24+28,cy+90,cw-56,"sub-quadratic attention / Performer   (Cor. 5.3)",GOLD,24,13))
    b+=anchor(ch[2]["aid"],ch[2]["kw"],body)
    # c4 bottom band -- log vs linear chart
    body=(rect(64,398,1152,152,fill="#0F2E2B",stroke=TEAL,rx=14,sw=1.5)+
        rect(64,398,6,152,fill=TEAL,rx=6,sw=0)+
        T(92,430,"Where the transformer is logarithmic in k, the alternatives are linear",15.5,TEXT,"800"))
    body+=_logvslin_chart(700,414,486,124)
    b+=anchor(ch[3]["aid"],ch[3]["kw"],body)
    return svg(b)

def _logvslin_chart(x,y,w,h):
    out=""
    ox=x+30; oy=y+h-22; pw=w-60; ph=h-40
    out+=line(ox,y+6,ox,oy,STROKE,1.4)
    out+=line(ox,oy,ox+pw,oy,STROKE,1.4)
    def px(k): return ox+pw*(k/16.0)
    def py(d): return oy-ph*(d/16.0)
    lin=[(px(k),py(k)) for k in range(1,17)]
    log=[(px(k),py(max(1,math.log2(k)+2 if k>=1 else 1))) for k in range(1,17)]
    out+=poly(lin,stroke=RED,sw=2.6)
    out+=poly(log,stroke=TEAL,sw=2.6)
    out+=T(px(16),py(16)+2,"RNN / Mamba / Performer  ~ k",11,RED,"800",anchor="end")
    out+=T(px(16),py(6)+2,"transformer  ~ log k",11,TEAL,"800",anchor="end")
    out+=T(x+w/2,y+h-2,"hop count k",10.5,SEC,"700",anchor="middle")
    out+=T(ox-6,y+12,"depth",10.5,SEC,"700",anchor="end")
    return out

# ---------- SLIDE 10: TAKEAWAY ----------
def s_takeaway():
    ch=chunks("takeaway"); b=header("Takeaway","Transformers are, in a precise sense, parallel computers")
    # c1 hero band
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,150,1152,72,fill="#0F2E2B",stroke=TEAL,rx=14,sw=1.5)+
        rect(64,150,6,72,fill=TEAL,rx=6,sw=0)+
        T(92,182,"The one thing to remember",15,TEAL,"800",ls="1")+
        T(92,210,"A transformer is, in a precise sense, a parallel computer.",17,TEXT,"800"))
    cards=[
        (ch[1],ACCENT,"Log-depth = constant-round MPC","This paper pins the intuition down: logarithmic-depth transformers are equivalent to constant-round Massively Parallel Computation."),
        (ch[2],GOLD,"A sharp, predicted separation","On k-hop, transformers succeed with depth logarithmic in k, while RNNs, state-space models like Mamba, and efficient attention all need depth linear in k."),
        (ch[3],GREEN,"Verified to the layer","Trained transformers obey the predicted threshold to the layer. The real edge is not scale, it is the ability to do many things at once."),
    ]
    y=238
    for c,col,ti,tx in cards:
        body=(rect(64,y,1152,100,fill=PANEL,stroke=STROKE)+
              rect(64,y,6,100,fill=col,rx=6,sw=0)+
              circle(112,y+50,10,fill=col)+
              T(150,y+42,ti,18,TEXT,"800"))
        body+=para(150,y+72,tx,14.5,SEC,104,22)[0]
        b+=anchor(c["aid"],c["kw"],body)
        y+=112
    b+=line(64,588,1216,588,STROKE,1)
    b+=T(64,620,"Transformers, Parallel Computation, and Logarithmic Depth",15.5,TEXT,"700")
    b+=T(64,646,"ICML 2024  ·  arXiv:2402.09268  ·  Columbia University  ·  Courant Institute, NYU",13,SEC,"600")
    return svg(b)

SLIDES=[("01_title",s_title),("02_problem",s_problem),("03_motivation",s_motivation),
        ("04_contribution",s_contribution),("05_method",s_method),("06_dataset",s_dataset),
        ("07_key_result",s_result),("08_ablation",s_ablation),("09_headline_numbers",s_headline),
        ("10_takeaway",s_takeaway)]

for name,fn in SLIDES:
    open(os.path.join(OUT,name+".svg"),"w").write(fn())
    print("wrote",name)
print("DONE",len(SLIDES))
