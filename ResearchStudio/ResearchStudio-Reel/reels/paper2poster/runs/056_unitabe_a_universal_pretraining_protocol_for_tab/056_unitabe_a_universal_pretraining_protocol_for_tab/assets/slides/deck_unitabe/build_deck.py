#!/usr/bin/env python3
"""Author the UniTabE video deck as 8 self-contained SVG slides (svg_output/)."""
import base64, os

DECK = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(DECK, "images")
OUT = os.path.join(DECK, "svg_output")
os.makedirs(OUT, exist_ok=True)

# ---- palette ----
BG="#FFFFFF"; PANEL="#F4F6F9"; PRIMARY="#16324F"; ACCENT="#1F9E8F"; ATINT="#E7F4F1"
SEC="#5FB0A6"; TEXT="#1A202C"; TEXT2="#4A5568"; TEXT3="#94A3B8"; BORDER="#E2E8F0"
BADGE="#2E9E5B"; WARN="#C0392B"; DTINT="#FBEEEC"; DBORD="#E7B6AE"; DARK="#0E2438"
ONDARK="#CBD5E1"; AMBER="#E08A1E"; BLUE="#3B7DD8"; PURPLE="#9B59B6"
SERIF='Georgia, &quot;Microsoft YaHei&quot;, serif'
SANS='Arial, &quot;Microsoft YaHei&quot;, sans-serif'
MONO='Consolas, &quot;Courier New&quot;, monospace'
FOOT="UniTabE: A Universal Pretraining Protocol for Tabular Foundation Models · Yang et al. · ICLR 2024"

def esc(s): return s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")

def T(x,y,s,size,fill,fam=SANS,weight=None,anchor=None,italic=False,ls=None,style=None):
    a=f' font-family="{fam}" font-size="{size}" fill="{fill}"'
    if weight: a+=f' font-weight="{weight}"'
    if anchor: a+=f' text-anchor="{anchor}"'
    if italic: a+=' font-style="italic"'
    if ls is not None: a+=f' letter-spacing="{ls}"'
    if style: a+=f' {style}'
    return f'<text x="{x}" y="{y}"{a}>{esc(s)}</text>'

def b64(name):
    with open(os.path.join(IMG,name),"rb") as f:
        return "data:image/png;base64,"+base64.b64encode(f.read()).decode()

def image(name,x,y,w,h,preserve="xMidYMid meet"):
    return f'<image href="{b64(name)}" x="{x}" y="{y}" width="{w}" height="{h}" preserveAspectRatio="{preserve}"/>'

def header(title,kicker):
    return (f'<g id="header">'
            f'<rect x="60" y="56" width="6" height="40" fill="{ACCENT}"/>'
            f'{T(84,88,title,34,PRIMARY,SERIF,700)}'
            f'{T(84,116,kicker,13,TEXT2,SANS,700,ls=1.5)}'
            f'</g>')

def footer(page):
    return (f'<g id="footer">'
            f'{T(60,702,FOOT,11,TEXT3)}'
            f'{T(1220,702,page,11,TEXT3,anchor="end")}'
            f'</g>')

def svg(role,body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720" width="1280" height="720" data-pptx-page-role="{role}">\n'
            f'  <g id="bg"><rect width="1280" height="720" fill="{BG}"/></g>\n'
            f'{body}\n</svg>\n')

def card(gid,desc,x,y,w,h,label,label_c,heading,lines,bar,fill=PANEL,stroke=BORDER,head_c=PRIMARY,body_c=TEXT,body_size=17,body_y0=124,gap=26,head_size=26):
    s=[f'<g id="{gid}"><desc>{esc(desc)}</desc>']
    s.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{fill}" stroke="{stroke}" stroke-width="1"/>')
    s.append(f'<rect x="{x}" y="{y}" width="6" height="{h}" rx="3" fill="{bar}"/>')
    tx=x+30
    if label: s.append(T(tx,y+40,label,13,label_c,SANS,700,ls=1.5))
    if heading: s.append(T(tx,y+82,heading,head_size,head_c,SERIF,700))
    ly=y+body_y0
    for ln in lines:
        s.append(T(tx,ly,ln,body_size,body_c)); ly+=gap
    s.append('</g>')
    return "".join(s)

def write(idx,name,role,body):
    fn=os.path.join(OUT,f"{idx:02d}_{name}.svg")
    with open(fn,"w") as f: f.write(svg(role,body))
    print("wrote",fn)

# ================= SLIDE 1 : TITLE =================
def slide1():
    b=['<defs><linearGradient id="cover" x1="0" y1="0" x2="0" y2="1">'
       f'<stop offset="0%" stop-color="{PRIMARY}"/><stop offset="100%" stop-color="{DARK}"/></linearGradient></defs>']
    b=['<g id="bg2"><rect x="0" y="0" width="14" height="720" fill="'+ACCENT+'"/></g>']
    # kicker
    b.append('<g id="cover-kicker">'
             +T(80,112,"PAPER · DEEP READ",13,ACCENT,SANS,700,ls=3)
             +T(80,136,"TABULAR FOUNDATION MODELS · ICLR 2024 · arXiv:2307.09249",12,TEXT2,SANS,500,ls=1.2)
             +'</g>')
    # title
    b.append('<g id="cover-title">'
             +T(80,200,"UniTabE: A Universal Pretraining",46,PRIMARY,SERIF,700)
             +T(80,256,"Protocol for Tabular Models",46,PRIMARY,SERIF,700)
             +'</g>')
    # c1 italic subtitle
    b.append('<g id="cue_s01_c1_foundation_models_transformed_langua"><desc>foundation models transformed language and vision yet tabular data workhorse of data science left behind</desc>'
             +f'<line x1="82" y1="292" x2="182" y2="292" stroke="{PRIMARY}" stroke-width="2"/>'
             +T(80,330,"Foundation models transformed language and vision,",21,TEXT,SERIF,italic=True)
             +T(80,358,"yet tabular data, the workhorse of data science, was left behind.",21,TEXT,SERIF,italic=True)
             +'</g>')
    # c2 gap -> UniTabE + authors
    b.append('<g id="cue_s01_c2_every_table_different_schema_trained"><desc>every table different schema model trained on one rarely transfers introduces UniTabE universal pretraining protocol any table uniformly</desc>'
             +f'<rect x="80" y="384" width="740" height="92" rx="10" fill="{PANEL}" stroke="{BORDER}" stroke-width="1"/>'
             +f'<rect x="80" y="384" width="6" height="92" rx="3" fill="{ACCENT}"/>'
             +T(104,414,"THE GAP → UNITABE",13,ACCENT,SANS,700,ls=1.5)
             +T(104,442,"Every table has a different schema, so models don't transfer.",16,TEXT)
             +T(104,466,"UniTabE processes any table in one uniform way.",16,TEXT)
             +'</g>')
    # c3 how it works
    b.append('<g id="cue_s01_c3_encodes_cell_small_module_called"><desc>encodes each cell small module called TabUnit refines table Transformer adapts through text prompts</desc>'
             +f'<rect x="80" y="488" width="740" height="60" rx="10" fill="{ATINT}" stroke="{SEC}" stroke-width="1"/>'
             +T(104,514,"HOW",12,ACCENT,SANS,700,ls=1.5)
             +T(104,536,"TabUnit encodes each cell · Transformer refines the table · text prompts adapt to tasks",15,TEXT)
             +'</g>')
    # c4 headline finding
    b.append('<g id="cue_s01_c4_pretrained_thirteen_billion_kaggle_s"><desc>pretrained thirteen billion Kaggle samples beats XGBoost</desc>'
             +f'<rect x="80" y="560" width="740" height="86" rx="10" fill="#EEF6F3" stroke="{BADGE}" stroke-width="1"/>'
             +f'<rect x="80" y="560" width="6" height="86" rx="3" fill="{BADGE}"/>'
             +T(104,590,"HEADLINE FINDING",13,ACCENT,SANS,700,ls=1.5)
             +f'<text x="104" y="620" font-family="{SANS}" font-size="17" fill="{TEXT}">Pretrained on <tspan font-weight="700" fill="{BADGE}">13B Kaggle samples</tspan>, UniTabE <tspan font-weight="700" fill="{BADGE}">beats XGBoost</tspan> across benchmarks.</text>'
             +'</g>')
    # right side panel : at a glance + qr + logos
    px,pw=856,364
    b.append(f'<g id="cover-side"><rect x="{px}" y="150" width="{pw}" height="496" rx="14" fill="{PANEL}" stroke="{BORDER}" stroke-width="1"/>')
    b.append(T(px+24,184,"ARCHITECTURE AT A GLANCE",12,ACCENT,SANS,700,ls=1.2))
    # architecture teaser banner (sized so at least one visual is legible in-video)
    b.append(f'<rect x="{px+20}" y="196" width="340" height="106" rx="8" fill="{BG}" stroke="{BORDER}" stroke-width="1"/>')
    b.append(image("figure1_arch.png",px+24,200,332,97))
    b.append(T(px+24,322,"Cells → TabUnit → Transformer → shallow decoder",11,TEXT2))
    stats=[("13B","pretraining samples"),("283K","tables · 303 domains"),("0.83","avg AUC · 7 benchmarks")]
    sy=340
    for val,lab in stats:
        b.append(f'<rect x="{px+24}" y="{sy}" width="{pw-48}" height="58" rx="8" fill="{BG}" stroke="{BORDER}" stroke-width="1"/>')
        b.append(T(px+40,sy+38,val,26,PRIMARY,SERIF,700))
        b.append(T(px+150,sy+26,lab.split(" · ")[0],13,TEXT2,SANS,700))
        b.append(T(px+150,sy+44,(lab.split(" · ")[1] if " · " in lab else ""),11,TEXT3))
        sy+=66
    # qr + labels row
    b.append(image("qr_paper.png",px+24,sy+2,64,64))
    b.append(T(px+100,sy+24,"READ THE PAPER",12,PRIMARY,SANS,700,ls=1))
    b.append(T(px+100,sy+44,"arXiv:2307.09249",11,TEXT2))
    b.append(T(px+100,sy+62,"Scan to open",11,TEXT3))
    b.append('</g>')
    # institute logos below panel
    b.append('<g id="logos">'
             +image("logo_hku.png",80,660,150,29)
             +image("logo_baai.png",250,650,90,42)
             +image("logo_creatify.png",360,654,32,32)
             +T(402,676,"HKU · BAAI · Creatify AI",11,TEXT3)
             +'</g>')
    b.append(f'<g id="footer">{T(1220,702,"01",11,TEXT3,anchor="end")}</g>')
    write(1,"title","cover","".join(b))

# ================= SLIDE 2 : PROBLEM =================
def slide2():
    b=[header("The problem: tables resist pretraining","NO FOUNDATION MODEL FOR TABULAR DATA")]
    b.append(card("cue_s02_c1_tabular_underpins_applications_like",
        "tabular data underpins applications like stock prediction real-estate forecasting credit scoring",
        60,152,570,216,"WHERE TABLES MATTER",ACCENT,"Tables run the real world",
        ["Stock prediction, real-estate","forecasting, and credit scoring all","rest on rows-and-columns data."],PRIMARY))
    b.append(card("cue_s02_c2_yet_unlike_text_images_widely",
        "yet unlike text and images tabular has no widely adopted foundation model",
        650,152,570,216,"THE MISSING PIECE",ACCENT,"No foundation model yet",
        ["Unlike text and images, tabular","data still has no widely adopted","pretrained foundation model."],ACCENT))
    b.append(card("cue_s02_c3_reason_tables_come_endless_schemas",
        "the reason tables come in endless schemas different column names data types counts model trained on one cannot be reused",
        60,392,570,216,"THE ROOT CAUSE",WARN,"Endless, mismatched schemas",
        ["Different column names, data types,","and counts mean a model trained on","one table can't be reused on another."],WARN,fill=DTINT,stroke=DBORD))
    b.append(card("cue_s02_c4_existing_methods_either_flatten_tabl",
        "existing methods either flatten tables into text losing numerical meaning or assume train and test share fixed structure both block knowledge transfer",
        650,392,570,216,"WHY WORKAROUNDS FAIL",ACCENT,"Two flawed workarounds",
        ["Flatten to text → lose numeric meaning.","Assume a fixed schema → no transfer.","Both block knowledge transfer."],BADGE))
    b.append(footer("02"))
    write(2,"problem","content","".join(b))

# ================= SLIDE 3 : MOTIVATION =================
def slide3():
    b=[header("Can the pretraining recipe work for tables?","LEARN ONCE, TRANSFER TO MANY TASKS")]
    # c1 dark
    b.append('<g id="cue_s03_c1_promise_pretraining_learns_general_k"><desc>promise of pretraining model learns general knowledge once from huge unlabeled data then transfers cheaply to many tasks</desc>'
             +f'<rect x="60" y="152" width="570" height="216" rx="12" fill="{PRIMARY}"/>'
             +T(90,192,"THE PROMISE OF PRETRAINING",12,SEC,SANS,700,ls=1.5)
             +T(90,232,"Learn once, transfer widely",24,"#FFFFFF",SERIF,700)
             +T(90,274,"A model absorbs general knowledge from",16,ONDARK)
             +T(90,300,"huge unlabeled data, then transfers it",16,ONDARK)
             +T(90,326,"cheaply to many downstream tasks.",16,ONDARK)
             +'</g>')
    b.append(card("cue_s03_c2_authors_ask_whether_recipe_work",
        "the authors ask whether this recipe can work for tables",
        650,152,570,216,"THE QUESTION",ACCENT,"Does it work for tables?",
        ["The authors ask whether this same","pretrain-then-transfer recipe can","carry over to structured tables."],ACCENT,fill=ATINT,stroke=SEC))
    b.append(card("cue_s03_c3_three_ingredients_needed_way_represe",
        "three ingredients needed a way to represent any table regardless of schema training framework flexible for many objectives data source large enough to pretrain at scale",
        60,392,570,216,"THREE INGREDIENTS",ACCENT,"What it takes",
        ["1  Represent any table, any schema","2  A framework for many objectives","3  Data large enough to pretrain"],PRIMARY,body_size=16))
    b.append(card("cue_s03_c4_together_one_tabular_could_handle",
        "together one tabular model could handle classification regression missing-value imputation zero-shot prediction tables that grow new columns without redesigning per task",
        650,392,570,216,"THE PAYOFF",ACCENT,"One model, many tasks",
        ["Classification · regression · imputation","zero-shot · tables that gain columns,","all without redesigning per task."],BADGE))
    b.append(footer("03"))
    write(3,"motivation","content","".join(b))

# ================= SLIDE 4 : METHOD =================
def slide4():
    b=[header("Method: TabUnit + Transformer + prompts","FIGURE 1 · STRUCTURE-FREE, CELL-LEVEL ARCHITECTURE")]
    # figure band
    b.append('<g id="figure1">'
             +f'<rect x="60" y="150" width="1160" height="342" rx="12" fill="{PANEL}" stroke="{BORDER}" stroke-width="1"/>'
             +image("figure1_arch.png",76,158,1128,326)
             +'</g>')
    steps=[
        ("cue_s04_c1_unitabe_heart_module_called_tabunit",
         "at UniTabE heart module called TabUnit handles one cell at a time treats each cell key-value pair column name key content value",
         "1","TabUnit per cell",PRIMARY,["Each cell is a key-value pair:","column name is the key,","content is the value."]),
        ("cue_s04_c2_name_embedded_mean_pooled_data_type",
         "the name embedded and mean-pooled data-type embedding marking numerical categorical textual fused in through a gate salary column handled numbers or words",
         "2","Fuse data type",ACCENT,["Name is embedded + mean-pooled;","a data-type gate marks numeric,","categorical or textual."]),
        ("cue_s04_c3_linking_layer_injects_column_vector",
         "linking layer injects column vector into each value token attention links values to their column all cell vectors plus CLS token pass through Transformer encoder",
         "3","Link + encode",BLUE,["A linking layer ties columns to","values; all cells plus a CLS","token pass a Transformer encoder."]),
        ("cue_s04_c4_deliberately_shallow_lstm_decoder_gu",
         "deliberately shallow LSTM decoder guided by free-form prompt fill in missing value salary generates answer token by token weak decoder forces knowledge into encoder pretraining multi-cell masking contrastive learning",
         "4","Shallow decoder",BADGE,["Weak LSTM decoder + prompt","keeps knowledge in the encoder.","Pretrain: masking + contrastive."]),
    ]
    xs=[60,351,642,933]; w=278; y=506; h=158
    for (gid,desc,num,title,bar,lines),x in zip(steps,xs):
        s=[f'<g id="{gid}"><desc>{esc(desc)}</desc>']
        s.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{BG}" stroke="{BORDER}" stroke-width="1"/>')
        s.append(f'<rect x="{x}" y="{y}" width="{w}" height="6" rx="3" fill="{bar}"/>')
        s.append(f'<circle cx="{x+30}" cy="{y+38}" r="15" fill="{bar}"/>')
        s.append(T(x+30,y+43,num,16,"#FFFFFF",SANS,700,anchor="middle"))
        s.append(T(x+56,y+43,title,17,PRIMARY,SERIF,700))
        ly=y+74
        for ln in lines:
            s.append(T(x+20,ly,ln,12.5,TEXT)); ly+=22
        s.append('</g>')
        b.append("".join(s))
    b.append(footer("04"))
    write(4,"method","content","".join(b))

# ================= SLIDE 5 : DATASET / BENCHMARK =================
def slide5():
    b=[header("A Kaggle-scale corpus, held-out benchmarks","FIGURE 2 · DOMAIN & DATA-TYPE DISTRIBUTION")]
    # figure2 left
    b.append('<g id="figure2">'
             +f'<rect x="60" y="152" width="720" height="468" rx="12" fill="{PANEL}" stroke="{BORDER}" stroke-width="1"/>'
             +T(84,186,"DISTRIBUTION OF DOMAINS & CELL DATA TYPES",12,ACCENT,SANS,700,ls=1.2)
             +image("figure2_dist.png",76,200,688,292)
             +T(84,530,"Left: tables per domain. Right: numeric / categorical /",13,TEXT2)
             +T(84,552,"textual cell proportions across train / dev / test splits.",13,TEXT2)
             +'</g>')
    b.append(card("cue_s05_c1_pretrain_scale_team_assembled_massiv",
        "to pretrain at scale team assembled massive tabular dataset from Kaggle seven terabytes three hundred and three domains two hundred eighty-three thousand tables roughly thirteen billion examples",
        800,152,420,148,"THE CORPUS",ACCENT,"7 TB from Kaggle",
        ["303 domains · 283K tables","≈13B individual examples"],PRIMARY,body_size=15,body_y0=112,gap=22,head_size=23))
    b.append(card("cue_s05_c2_average_table_about_twenty_nine_nume",
        "on average each table about twenty-nine numerical columns eight textual ones investing finance economics among largest domains",
        800,312,420,148,"TABLE SHAPE",ACCENT,"≈29 numeric columns",
        ["Plus ~8 textual columns","Top: investing, finance, economics"],BADGE,body_size=15,body_y0=112,gap=22,head_size=23))
    b.append(card("cue_s05_c3_evaluation_they_hold_out_twelve",
        "for evaluation they hold out twelve Kaggle tasks six classification six regression never seen in pretraining plus seven widely used public benchmarks compare against established methods",
        800,472,420,148,"EVALUATION",ACCENT,"12 held-out + 7 public",
        ["6 classification + 6 regression","never seen, plus 7 public sets"],BLUE,body_size=15,body_y0=112,gap=22,head_size=23))
    b.append(footer("05"))
    write(5,"dataset_benchmark","content","".join(b))

# ================= SLIDE 6 : KEY RESULT =================
def slide6():
    b=[header("Key result: pretraining beats XGBoost","AVERAGE AUC OVER 7 PUBLIC TABULAR BENCHMARKS")]
    # chart card (c2)
    cx,cy,cw,ch=60,150,612,470
    s=['<g id="cue_s06_c2_seven_standard_public_benchmarks_uni"><desc>on seven standard public benchmarks UniTabE reaches average area-under-curve about zero point eight three beating Tapas FT-Transformer industry favorite XGBoost</desc>']
    s.append(f'<rect x="{cx}" y="{cy}" width="{cw}" height="{ch}" rx="12" fill="{PANEL}" stroke="{BORDER}" stroke-width="1"/>')
    s.append(T(cx+30,cy+40,"AVERAGE AUC · 7 BENCHMARKS",13,ACCENT,SANS,700,ls=1.2))
    # bars: baseline range 0.70..0.85 mapped
    base_x=cx+120; base_y=cy+400; bar_w=110; gap=60; maxh=300
    lo,hi=0.70,0.85
    bars=[("UniTabE",0.83,BADGE),("Best baseline",0.81,BLUE),("XGBoost",0.79,AMBER)]
    # axis gridlines
    for gv in [0.70,0.75,0.80,0.85]:
        gy=base_y-(gv-lo)/(hi-lo)*maxh
        s.append(f'<line x1="{base_x-20}" y1="{gy:.1f}" x2="{cx+cw-30}" y2="{gy:.1f}" stroke="{BORDER}" stroke-width="1"/>')
        s.append(T(cx+40,gy+4,f"{gv:.2f}",12,TEXT3))
    bx=base_x
    for name,val,col in bars:
        bh=(val-lo)/(hi-lo)*maxh
        s.append(f'<rect x="{bx}" y="{base_y-bh:.1f}" width="{bar_w}" height="{bh:.1f}" rx="6" fill="{col}"/>')
        s.append(T(bx+bar_w/2,base_y-bh-12,f"{val:.2f}",20,PRIMARY,SERIF,700,anchor="middle"))
        s.append(T(bx+bar_w/2,base_y+24,name,13,TEXT,SANS,700,anchor="middle"))
        bx+=bar_w+gap
    s.append(T(cx+30,cy+ch-18,"Beats Tapas, FT-Transformer and the industry-favorite XGBoost.",13,TEXT2))
    s.append('</g>')
    b.append("".join(s))
    # right column
    b.append('<g id="cue_s06_c1_experiments_show_pretraining_pays_of"><desc>the experiments show pretraining pays off</desc>'
             +f'<rect x="696" y="150" width="524" height="82" rx="12" fill="{PRIMARY}"/>'
             +T(720,186,"THE VERDICT",12,SEC,SANS,700,ls=1.5)
             +T(720,216,"Pretraining pays off.",24,"#FFFFFF",SERIF,700)
             +'</g>')
    b.append(card("cue_s06_c3_twelve_held_out_kaggle_tasks_spannin",
        "on twelve held-out Kaggle tasks spanning classification and regression UniTabE again outperforms XGBoost and a strong TransTab variant",
        696,248,524,178,"12 HELD-OUT KAGGLE TASKS",ACCENT,"Wins on unseen tasks",
        ["Across classification and regression,","UniTabE again beats XGBoost and","a strong TransTab variant."],BADGE))
    b.append(card("cue_s06_c4_also_performs_well_zero_shot_mode",
        "it also performs well in zero-shot mode making accurate predictions on some datasets with no task-specific finetuning evidence of genuine transferable reasoning about tables",
        696,442,524,178,"ZERO-SHOT",ACCENT,"Predicts with no finetuning",
        ["On some datasets it predicts","accurately with zero task-specific","finetuning, real transfer."],BLUE))
    b.append(footer("06"))
    write(6,"key_result","content","".join(b))

# ================= SLIDE 7 : ABLATION =================
def slide7():
    b=[header("Ablation: every component earns its place","LINKING LAYER, FUSE GATE, OBJECTIVES, DECODER DEPTH")]
    # c1 top-left with big numbers
    s=['<g id="cue_s07_c1_ablations_confirm_part_earns_its"><desc>ablations confirm each part earns its place removing the linking layer which ties names to values causes the largest drop from AUC zero point eight three down to zero point seven five</desc>']
    s.append(f'<rect x="60" y="152" width="570" height="216" rx="12" fill="{DTINT}" stroke="{DBORD}" stroke-width="1"/>')
    s.append(f'<rect x="60" y="152" width="6" height="216" rx="3" fill="{WARN}"/>')
    s.append(T(90,192,"BIGGEST DROP · LINKING LAYER",13,WARN,SANS,700,ls=1.5))
    s.append(T(90,236,"Removing column–value links",23,PRIMARY,SERIF,700))
    s.append(T(96,306,"0.83",40,BADGE,SERIF,700))
    s.append(T(214,300,"→",30,TEXT3))
    s.append(T(250,306,"0.75",40,WARN,SERIF,700))
    s.append(T(96,344,"average AUC falls when the linking layer is ablated",15,TEXT))
    s.append('</g>')
    b.append("".join(s))
    b.append(card("cue_s07_c2_removing_fuse_layer_injects_data_typ",
        "removing the fuse layer that injects data-type information also hurts and removing both is worse",
        650,152,570,216,"FUSE GATE",ACCENT,"Data-type fusion matters",
        ["Dropping the fuse layer that injects","data-type information also hurts,","and removing both is worse still."],ACCENT))
    b.append(card("cue_s07_c3_dropping_either_pretraining_objectiv",
        "dropping either pretraining objective multi-cell masking or contrastive learning reduces performance too",
        60,392,570,216,"PRETRAINING OBJECTIVES",ACCENT,"Two signals, complementary",
        ["Dropping either objective, multi-cell","masking or contrastive learning,","reduces performance too."],BADGE))
    b.append(card("cue_s07_c4_notably_one_layer_decoder_beats_thre",
        "notably a one-layer decoder beats three or six layer ones supporting the choice to keep the decoder shallow",
        650,392,570,216,"DECODER DEPTH",ACCENT,"Shallow decoder wins",
        ["A 1-layer decoder beats 3- and","6-layer ones, confirming the choice","to keep knowledge in the encoder."],BLUE))
    b.append(footer("07"))
    write(7,"ablation_study","content","".join(b))

# ================= SLIDE 8 : TAKEAWAY =================
def slide8():
    b=[header("Takeaway: a foundation model for tables","RESPECT STRUCTURE, PRETRAIN AT SCALE, TRANSFER")]
    # c1 hero dark band
    b.append('<g id="cue_s08_c1_pretraining_paradigm_reshaped_langua"><desc>the pretraining paradigm that reshaped language and vision can extend to structured tabular data</desc>'
             +f'<rect x="60" y="152" width="1160" height="150" rx="14" fill="{PRIMARY}"/>'
             +f'<rect x="60" y="152" width="6" height="150" rx="3" fill="{ACCENT}"/>'
             +T(96,196,"THE BIG PICTURE",12,SEC,SANS,700,ls=2)
             +T(96,242,"The pretraining paradigm that reshaped language and",26,"#FFFFFF",SERIF,700)
             +T(96,278,"vision can extend to structured tabular data.",26,"#FFFFFF",SERIF,700)
             +'</g>')
    b.append(card("cue_s08_c2_key_respect_table_structure_rather",
        "the key is to respect table structure rather than flatten it into text represent each cell by its column name value and data type refine with a Transformer adapt through free-form prompts",
        60,324,570,296,"THE PRINCIPLE",ACCENT,"Respect the structure",
        ["Don't flatten tables into text.","Represent each cell by its","column name, value, and data type,","refine with a Transformer, and","adapt through free-form prompts."],PRIMARY))
    b.append(card("cue_s08_c3_pretrained_billions_unitabe_becomes",
        "pretrained on billions UniTabE becomes a general tabular model that transfers across tasks beats the XGBoost baseline and handles missing values and tables that gain columns",
        650,324,570,296,"THE OUTCOME",ACCENT,"A general tabular model",
        ["Pretrained on billions of examples,","UniTabE transfers across tasks,","beats the long-standing XGBoost","baseline, and gracefully handles","missing values and new columns."],BADGE))
    b.append(footer("08"))
    write(8,"takeaway","content","".join(b))

for fn in [slide1,slide2,slide3,slide4,slide5,slide6,slide7,slide8]:
    fn()
print("DONE")
