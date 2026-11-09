# -*- coding: utf-8 -*-
import re
from pathlib import Path
import zipfile, xml.etree.ElementTree as ET

out_dir = Path("public/books/approche-de-la-neurodiversite")
out_dir.mkdir(parents=True, exist_ok=True)
pages_dir = Path("D:/0CODE/0 BEST/neurodiversity-explorer-main/src/pages")
res_dir = pages_dir / "ressources"

def clean_txt(s: str) -> str:
    s = s.replace("\u2014", ", ").replace("\u2013", ", ").replace("—", ", ").replace("–", ", ")
    s = s.replace("\u00a0", " ").replace("’", "'").replace("‘", "'")
    s = re.sub(r'\s+', ' ', s).strip()
    return s

def extract_jsx_blocks(p: Path):
    txt = p.read_text(encoding="utf-8")
    # extract p, li, h2, h3, h4, blockquote
    raw_blocks = re.findall(r'<(?:p|li|h[2-4]|blockquote)[^>]*>(.*?)</(?:p|li|h[2-4]|blockquote)>', txt, re.DOTALL)
    clean_blocks = []
    for b in raw_blocks:
        c = re.sub(r'<[^>]+>', '', b).strip()
        c = re.sub(r'\{[^}]+\}', '', c).strip()
        c = clean_txt(c)
        if len(c) > 15 and not c.startswith("Par Geoffroy"):
            clean_blocks.append(c)
    return clean_blocks

# -------------------------------------------------------------
# 00. PROLOGUE
# -------------------------------------------------------------
prologue_html = """<div class="chapter-content">
  <h1 class="chapter-main-title"><strong>Prologue : Le Décalage Invisible</strong></h1>
  <p class="chapter-byline">OUVERTURE · Geoffroy Streit (2018-2022)</p>
  <p class="chapter-paragraph">Le sujet est vaste, redoutable, encombré de préjugés tenaces et de modes passagères. Je n'ai pas la prétention d'en faire le tour encyclopédique, n'étant ni médecin spécialiste, ni chercheur en neurosciences, et encore moins neuropsychologue diplômé d'État. Toutefois, ma propre expérience d'adulte « dys », mes lectures patientes, ainsi que le fait d'avoir accompagné bénévolement durant de nombreuses années des enfants et des adolescents aux prises avec des troubles spécifiques des apprentissages font que je connais le problème de l'intérieur, à hauteur d'homme et les mains dans la terre glaise du réel.</p>
  <p class="chapter-paragraph">Avant d'entrer dans le vif de cette étude, une précision capitale s'impose : les troubles cognitifs dont il sera question ici sont les troubles dits « spécifiques des apprentissages ». Ils désignent des décalages d'acquisition qui ne sont liés ni à une déficience intellectuelle globale, ni à un handicap sensoriel périphérique (cécité, surdité), ni à une carence éducative fondamentale. L'intelligence de la personne est parfaitement normale, souvent vive, curieuse et créative. Mais un relais fonctionnel se dérobe dans les rouages cérébraux. Les signaux patinent, le pont synaptique ne répond pas avec la fluidité automatique dont bénéficient les personnes ordinaires.</p>
  <p class="chapter-paragraph">On parle souvent de l'enfance, car c'est sur les bancs de l'école que la collision frontale avec la norme se produit avec la plus grande violence. C'est là que l'enfant construit son rapport aux autres, sa confiance en soi, ses repères dans l'espace et sa relation au langage. Quand ces fondations se fissurent sous les quolibets ou les verdicts hâtifs, les retards d'assimilation s'accumulent et la blessure psychologique s'enkyste pour des décennies.</p>
  <p class="chapter-paragraph">Cette anthologie est organisée en quatre mouvements distincts mais indissociables :</p>
  <p class="chapter-paragraph">Le premier mouvement rassemble des confessions et des témoignages intimes, écrits à fleur de peau entre 2003 et 2024, où le vécu de la dyspraxie, du TDA/H et de la pensée en ébullition est raconté sans faux-semblant, avec cette autodérision qui sauve du désespoir.</p>
  <p class="chapter-paragraph">Le deuxième mouvement est tourné vers l'enfance, l'école et la pédagogie de terrain : comment décrypter la souffrance d'un élève sans le condamner, dédramatiser la note et bâtir une méthode du pas-à-pas.</p>
  <p class="chapter-paragraph">Le troisième mouvement explore l'anatomie intime de ces cerveaux singuliers : la cartographie détaillée des cinq familles de dys, les mystères d'une mémoire de travail saturée, et la navigation raisonnée au cœur du labyrinthe des idées foisonnantes.</p>
  <p class="chapter-paragraph">Le quatrième mouvement, enfin, ouvre la boîte à béquilles : treize stratégies concrètes d'organisation, de conditionnement mental et d'hygiène de vie forgées par un adulte pour continuer à marcher debout, jusqu'à savoir reconnaître l'alerte rouge de « l'esprit embrumé ».</p>
  <p class="chapter-paragraph">Ce livre ne cherche pas à vous rassurer à bon compte. Il cherche à vous donner des prises solides pour avancer les yeux ouverts.</p>
</div>
"""
(out_dir / "00-prologue.html").write_text(prologue_html, encoding="utf-8")
print("Written 00-prologue.html")

# -------------------------------------------------------------
# 01. LETTRE D'UN DYSPRAXIQUE (Mars 2003) - FULL 121 blocks
# -------------------------------------------------------------
lettre_blocks = extract_jsx_blocks(res_dir / "LettreDyspraxique.tsx")
paras_01 = [f'<p class="chapter-paragraph">{b}</p>' for b in lettre_blocks]
ch1_html = f"""<div class="chapter-content">
  <h1 class="chapter-main-title"><strong>01. Lettre d'un dyspraxique</strong></h1>
  <p class="chapter-byline">PARTIE I : CONFESSIONS &amp; VÉCUS DE L'INTÉRIEUR · Par Geoffroy Streit (Mars 2003)</p>
  <figure class="chapter-figure">
    <img src="public/books/approche-de-la-neurodiversite/images/partie-1-couverture.webp" alt="L'Archipel des Pensées" loading="lazy" />
  </figure>
{chr(10).join(paras_01)}
</div>
"""
(out_dir / "01-lettre-d-un-dyspraxique.html").write_text(ch1_html, encoding="utf-8")
print(f"Written 01-lettre-d-un-dyspraxique.html ({len(paras_01)} paras)")

# -------------------------------------------------------------
# 02. VIE DANS UN CHAOS ORGANISÉ (2005 / revu 2024) - FULL 63 blocks
# -------------------------------------------------------------
chaos_blocks = extract_jsx_blocks(res_dir / "VieChaosOrganise.tsx")
paras_02 = [f'<p class="chapter-paragraph">{b}</p>' for b in chaos_blocks]
ch2_html = f"""<div class="chapter-content">
  <h1 class="chapter-main-title"><strong>02. Vie dans un chaos organisé : confessions d'un cerveau Dys/TDA/H</strong></h1>
  <p class="chapter-byline">PARTIE I : CONFESSIONS &amp; VÉCUS DE L'INTÉRIEUR · Par Geoffroy Streit (2005 et des brouettes, revu en 2024)</p>
{chr(10).join(paras_02)}
</div>
"""
(out_dir / "02-vie-dans-un-chaos-organise.html").write_text(ch2_html, encoding="utf-8")
print(f"Written 02-vie-dans-un-chaos-organise.html ({len(paras_02)} paras)")

# -------------------------------------------------------------
# 03. PENSÉE EN ÉBULLITION (2024) - FULL blocks
# -------------------------------------------------------------
ebull_blocks = extract_jsx_blocks(res_dir / "PenseeEnEbullition.tsx")
paras_03 = [f'<p class="chapter-paragraph">{b}</p>' for b in ebull_blocks]
ch3_html = f"""<div class="chapter-content">
  <h1 class="chapter-main-title"><strong>03. Pensée en ébullition : le volcan des connexions</strong></h1>
  <p class="chapter-byline">PARTIE I : CONFESSIONS &amp; VÉCUS DE L'INTÉRIEUR · Réflexion de terrain (2024)</p>
{chr(10).join(paras_03)}
</div>
"""
(out_dir / "03-pensee-en-ebullition.html").write_text(ch3_html, encoding="utf-8")
print(f"Written 03-pensee-en-ebullition.html ({len(paras_03)} paras)")

# -------------------------------------------------------------
# 04. LA NEURODIVERSITÉ EXPLIQUÉE AUX ENFANTS (Mars 2023)
# -------------------------------------------------------------
enfant_blocks = extract_jsx_blocks(pages_dir / "NeurodiversiteEnfant.tsx")
paras_04 = [f'<p class="chapter-paragraph">{b}</p>' for b in enfant_blocks]
ch4_html = f"""<div class="chapter-content">
  <h1 class="chapter-main-title"><strong>04. La neurodiversité expliquée aux enfants</strong></h1>
  <p class="chapter-byline">PARTIE II : L'ENFANCE, L'ÉCOLE ET LA PÉDAGOGIE DE TERRAIN · Par Geoffroy Streit (Mars 2023)</p>
  <figure class="chapter-figure">
    <img src="public/books/approche-de-la-neurodiversite/images/partie-2-couverture.webp" alt="La Main sur l'Épaule" loading="lazy" />
  </figure>
{chr(10).join(paras_04)}
</div>
"""
(out_dir / "04-la-neurodiversite-expliquee-aux-enfants.html").write_text(ch4_html, encoding="utf-8")
print(f"Written 04-la-neurodiversite-expliquee-aux-enfants.html ({len(paras_04)} paras)")

# -------------------------------------------------------------
# 05. ENFANTS EN DIFFICULTÉ SCOLAIRE : GUIDE D'ÉCOUTE (~2004)
# -------------------------------------------------------------
p_doc = Path(r"D:\0HYLST\0 HYLST ART 2024\ecrits\Réflexions\Enfants en difficulté scolaire.doc")
raw_doc = p_doc.read_bytes()
chunks_doc = re.findall(rb'(?:[\x20-\x7E\xC0-\xFF]\x00){4,}', raw_doc)
doc_str = "\n".join([c.decode("utf-16le", errors="ignore") for c in chunks_doc])
lines_doc = [clean_txt(l) for l in doc_str.splitlines() if l.strip() and not l.startswith("Normal") and not l.startswith("Police") and not l.startswith("Titre") and not l.startswith("Times") and not l.startswith("Arial") and not l.startswith("Symbol") and not l.startswith("Liberation") and not l.startswith("Microsoft") and not l.startswith("Lucida") and not l.startswith("Root") and not l.startswith("Corps") and not l.startswith("Liste") and not l.startswith("Légende") and not l.startswith("Index") and not l.startswith("Votre nom")]

paras_doc = [f'<p class="chapter-paragraph">{l}</p>' for l in lines_doc if len(l) > 20 and not l.startswith("Enfants en difficulté scolaire")]
ch5_html = f"""<div class="chapter-content">
  <h1 class="chapter-main-title"><strong>05. Enfants en difficulté scolaire : guide d'écoute pour parents et tuteurs</strong></h1>
  <p class="chapter-byline">PARTIE II : L'ENFANCE, L'ÉCOLE ET LA PÉDAGOGIE DE TERRAIN · Texte d'archive pédagogique (vers 2004)</p>
{chr(10).join(paras_doc)}
</div>
"""
(out_dir / "05-enfants-en-difficulte-scolaire.html").write_text(ch5_html, encoding="utf-8")
print(f"Written 05-enfants-en-difficulte-scolaire.html ({len(paras_doc)} paras)")

# -------------------------------------------------------------
# 06. PÉDAGOGIE DE TERRAIN : LE PAS-À-PAS
# -------------------------------------------------------------
ch6_html = """<div class="chapter-content">
  <h1 class="chapter-main-title"><strong>06. Pédagogie de terrain : la méthode du pas-à-pas</strong></h1>
  <p class="chapter-byline">PARTIE II : L'ENFANCE, L'ÉCOLE ET LA PÉDAGOGIE DE TERRAIN · Méthodologie d'accompagnement scolaire</p>
  <figure class="chapter-figure">
    <img src="public/books/approche-de-la-neurodiversite/images/neuro-schema-2-pedagogie.svg" alt="Accompagnement de l'enfant : sortir de l'engrenage de l'échec" loading="lazy" />
  </figure>
  <p class="chapter-paragraph">Une fois le climat de confiance rétabli avec l'élève, comment travailler concrètement à la maison ou lors des séances de cours particuliers ?</p>
  <p class="chapter-paragraph">La règle d'or, absolue et non négociable, tient en une formule : la méthode du pas-à-pas.</p>
  <p class="chapter-paragraph">L'erreur la plus commune chez les parents anxieux consiste à vouloir rattraper deux trimestres de retard en un seul après-midi de travail acharné le samedi. On étale cinq manuels sur la table, on sort dix polycopiés d'exercices, et l'on somme l'enfant de s'y coller pendant trois heures d'affilée. C'est la garantie absolue de l'échec et de la crise de larmes.</p>
  <p class="chapter-paragraph">Face à une montagne de devoirs, le cerveau d'un enfant dys ou fatigué disjoncte immédiatement sous l'effet de la sidération.</p>
  <p class="chapter-paragraph">La méthode consiste à découper la montagne en petites marches franchissables : ne lui donnez jamais une page entière d'exercices à résoudre. Masquez le bas de la feuille avec une feuille blanche, et dites-lui : « Nous ne faisons que ces deux lignes-là. Rien que ces deux lignes, tranquillement. Quand c'est fait, c'est validé. »</p>
  <p class="chapter-paragraph">Lorsque ces deux lignes sont réussies, félicitez sincèrement l'effort fourni, validez la petite victoire, et accordez immédiatement cinq minutes de récréation réelle : aller boire un verre d'eau, faire quelques pas dans le couloir, s'étirer les bras, regarder par la fenêtre. Un enfant dont le réservoir attentionnel est vidé n'enregistre plus rien : continuer à lui parler quand son regard s'évade équivaut à verser de l'eau dans une bouteille sans bouchon.</p>
  <p class="chapter-paragraph">Ancrez systématiquement l'abstrait dans le concret : si vous travaillez les fractions, laissez tomber les définitions jargonnantes et sortez une tablette de chocolat, des pièces de monnaie ou des bandes de carton de couleurs découpées aux ciseaux. Laissez ses doigts manipuler la matière. La mémoire motrice et kinesthésique vient souvent relayer avec bonheur une mémoire visuelle ou phonologique défaillante.</p>
  <p class="chapter-paragraph">Et surtout, faites preuve d'humilité et de patience : si l'enfant ne comprend pas après votre première explication, cela ne signifie pas qu'il est bête : cela signifie que votre explication n'était pas adaptée à son canal de réception ! Ne répétez pas la même phrase en haussant le ton. Changez d'angle, inventez une autre métaphore, faites un dessin, utilisez un exemple tiré de ses passions.</p>
  <p class="chapter-paragraph">C'est à l'adulte d'adapter sa pédagogie au cerveau de l'enfant, jamais à l'enfant de tordre ses neurones pour entrer dans le moule de l'adulte.</p>
</div>
"""
(out_dir / "06-pedagogie-de-terrain-le-pas-a-pas.html").write_text(ch6_html, encoding="utf-8")
print("Written 06-pedagogie-de-terrain-le-pas-a-pas.html")

# -------------------------------------------------------------
# 07. MARRE D'APPRENDRE ! (2025) - FULL 54 blocks
# -------------------------------------------------------------
marre_blocks = extract_jsx_blocks(res_dir / "MarreApprendre.tsx")
paras_07 = [f'<p class="chapter-paragraph">{b}</p>' for b in marre_blocks]
ch7_html = f"""<div class="chapter-content">
  <h1 class="chapter-main-title"><strong>07. Marre d'apprendre ! Lettre ouverte aux élèves découragés</strong></h1>
  <p class="chapter-byline">PARTIE II : L'ENFANCE, L'ÉCOLE ET LA PÉDAGOGIE DE TERRAIN · Par Geoffroy Streit (2025)</p>
{chr(10).join(paras_07)}
</div>
"""
(out_dir / "07-marre-d-apprendre.html").write_text(ch7_html, encoding="utf-8")
print(f"Written 07-marre-d-apprendre.html ({len(paras_07)} paras)")

# -------------------------------------------------------------
# 08. LES CINQ FAMILLES DE TROUBLES DYS - FULL 155 paragraphs from ODT
# -------------------------------------------------------------
p_odt = Path(r"D:\0HYLST\0 HYLST ART 2024\ecrits\Réflexions\troubles dys.odt")
with zipfile.ZipFile(p_odt) as z:
    tree = ET.fromstring(z.read("content.xml"))
    odt_paras = []
    for elem in tree.iter():
        if elem.tag.endswith("}p") or elem.tag.endswith("}h"):
            t = "".join(elem.itertext()).strip()
            t = clean_txt(t)
            if len(t) > 15 and not t.startswith("Clarifications") and not t.startswith("Introduction :"):
                odt_paras.append(f'<p class="chapter-paragraph">{t}</p>')

ch8_html = f"""<div class="chapter-content">
  <h1 class="chapter-main-title"><strong>08. Les cinq familles de troubles cognitifs : langage, geste et calcul</strong></h1>
  <p class="chapter-byline">PARTIE III : ANATOMIE DES CERVEAUX QUI DANSENT · Étude clinique et vécue (2018-2020)</p>
  <figure class="chapter-figure">
    <img src="public/books/approche-de-la-neurodiversite/images/neuro-schema-1-familles.svg" alt="Cartographie des troubles cognitifs et dysfonctionnements associés" loading="lazy" />
  </figure>
{chr(10).join(odt_paras)}
</div>
"""
(out_dir / "08-les-cinq-familles-de-troubles-cognitifs.html").write_text(ch8_html, encoding="utf-8")
print(f"Written 08-les-cinq-familles-de-troubles-cognitifs.html ({len(odt_paras)} paras)")

# -------------------------------------------------------------
# 09. LA MÉMOIRE DANS LA NEURODIVERSITÉ (2024)
# -------------------------------------------------------------
mem_blocks = extract_jsx_blocks(res_dir / "MemoireNeurodiversite.tsx")
paras_09 = [f'<p class="chapter-paragraph">{b}</p>' for b in mem_blocks]
ch9_html = f"""<div class="chapter-content">
  <h1 class="chapter-main-title"><strong>09. La mémoire dans la neurodiversité : un labyrinthe aux multiples facettes</strong></h1>
  <p class="chapter-byline">PARTIE III : ANATOMIE DES CERVEAUX QUI DANSENT · Synthèse cognitive (2024)</p>
{chr(10).join(paras_09)}
</div>
"""
(out_dir / "09-la-memoire-dans-la-neurodiversite.html").write_text(ch9_html, encoding="utf-8")
print(f"Written 09-la-memoire-dans-la-neurodiversite.html ({len(paras_09)} paras)")

# -------------------------------------------------------------
# 10. NAVIGATION DANS LE LABYRINTHE DES IDÉES (2024) - FULL textContent + JSX (~4000 words!)
# -------------------------------------------------------------
nav_txt = (res_dir / "NavigationLabyrintheIdees.tsx").read_text(encoding="utf-8")
# Extract all string literals longer than 30 chars from NavigationLabyrintheIdees.tsx
str_matches = re.findall(r'["\']([^"\']{35,})["\']', nav_txt)
clean_nav_blocks = []
seen = set()
for sm in str_matches:
    c = clean_txt(sm)
    if c not in seen and not c.startswith("http") and not c.startswith("/") and not c.startswith("Navigation"):
        seen.add(c)
        clean_nav_blocks.append(f'<p class="chapter-paragraph">{c}</p>')

ch10_html = f"""<div class="chapter-content">
  <h1 class="chapter-main-title"><strong>10. Navigation dans le labyrinthe des idées</strong></h1>
  <p class="chapter-byline">PARTIE III : ANATOMIE DES CERVEAUX QUI DANSENT · Guide pour esprits foisonnants (2024)</p>
{chr(10).join(clean_nav_blocks)}
</div>
"""
(out_dir / "10-navigation-dans-le-labyrinthe-des-idees.html").write_text(ch10_html, encoding="utf-8")
print(f"Written 10-navigation-dans-le-labyrinthe-des-idees.html ({len(clean_nav_blocks)} paras)")

# -------------------------------------------------------------
# 11. APPRENDRE QUAND LE CERVEAU DANSE (2025) - FULL blocks
# -------------------------------------------------------------
strat_blocks = extract_jsx_blocks(res_dir / "StrategiesApprentissage.tsx")
paras_11 = [f'<p class="chapter-paragraph">{b}</p>' for b in strat_blocks]
ch11_html = f"""<div class="chapter-content">
  <h1 class="chapter-main-title"><strong>11. Apprendre quand le cerveau danse : stratégies d'assimilation atypiques</strong></h1>
  <p class="chapter-byline">PARTIE III : ANATOMIE DES CERVEAUX QUI DANSENT · Pratiques d'apprentissage personnalisées (2025)</p>
{chr(10).join(paras_11)}
</div>
"""
(out_dir / "11-apprendre-quand-le-cerveau-danse.html").write_text(ch11_html, encoding="utf-8")
print(f"Written 11-apprendre-quand-le-cerveau-danse.html ({len(paras_11)} paras)")

# -------------------------------------------------------------
# 12, 13, 14. LES 13 BÉQUILLES COGNITIVES (Juin 2022) - FULL OCR
# -------------------------------------------------------------
ocr_txt = Path("C:/Users/Geoffroy/AppData/Local/Temp/opencode/ocr_neuro/full_ocr.txt").read_text(encoding="utf-8")
# Split OCR text by numbered axes
ocr_lines = [clean_txt(l) for l in ocr_txt.splitlines() if l.strip() and not l.startswith("===")]

# Chunk into 12 (Axes 1-4), 13 (Axes 5-8), 14 (Axes 9-13)
# Let's organize axes from OCR
paras_ocr = []
for l in ocr_lines:
    if len(l) > 20 and not l.startswith("Idées pour lutter"):
        paras_ocr.append(l)

# Split into 3 parts
split1 = int(len(paras_ocr) * 0.35)
split2 = int(len(paras_ocr) * 0.70)

p12_items = [f'<p class="chapter-paragraph">{p}</p>' for p in paras_ocr[:split1]]
p13_items = [f'<p class="chapter-paragraph">{p}</p>' for p in paras_ocr[split1:split2]]
p14_items = [f'<p class="chapter-paragraph">{p}</p>' for p in paras_ocr[split2:]]

ch12_html = f"""<div class="chapter-content">
  <h1 class="chapter-main-title"><strong>12. L'environnement et le corps : poser les fondations</strong></h1>
  <p class="chapter-byline">PARTIE IV : LA BOÎTE À BÉQUILLES, DISCIPLINE &amp; SURVIE · 13 stratégies de terrain (3 juin 2022)</p>
  <figure class="chapter-figure">
    <img src="public/books/approche-de-la-neurodiversite/images/partie-3-couverture.webp" alt="La Boîte à Outils" loading="lazy" />
  </figure>
{chr(10).join(p12_items)}
</div>
"""
(out_dir / "12-l-environnement-et-le-corps-poser-les-fondations.html").write_text(ch12_html, encoding="utf-8")
print(f"Written 12-l-environnement-et-le-corps-poser-les-fondations.html ({len(p12_items)} paras)")

ch13_html = f"""<div class="chapter-content">
  <h1 class="chapter-main-title"><strong>13. Le délestage mental : externaliser la mémoire</strong></h1>
  <p class="chapter-byline">PARTIE IV : LA BOÎTE À BÉQUILLES, DISCIPLINE &amp; SURVIE · 13 stratégies de terrain (3 juin 2022)</p>
  <figure class="chapter-figure">
    <img src="public/books/approche-de-la-neurodiversite/images/neuro-schema-3-bequilles.svg" alt="Architecture des 13 béquilles cognitives pour adultes neuroatypiques" loading="lazy" />
  </figure>
{chr(10).join(p13_items)}
</div>
"""
(out_dir / "13-le-delestage-mental-externaliser-la-memoire.html").write_text(ch13_html, encoding="utf-8")
print(f"Written 13-le-delestage-mental-externaliser-la-memoire.html ({len(p13_items)} paras)")

ch14_html = f"""<div class="chapter-content">
  <h1 class="chapter-main-title"><strong>14. Conditionnement, hygiène de vie et gestion de l'esprit embrumé</strong></h1>
  <p class="chapter-byline">PARTIE IV : LA BOÎTE À BÉQUILLES, DISCIPLINE &amp; SURVIE · 13 stratégies de terrain (3 juin 2022)</p>
{chr(10).join(p14_items)}
</div>
"""
(out_dir / "14-conditionnement-hygiene-de-vie-et-esprit-embrume.html").write_text(ch14_html, encoding="utf-8")
print(f"Written 14-conditionnement-hygiene-de-vie-et-esprit-embrume.html ({len(p14_items)} paras)")

# -------------------------------------------------------------
# 15. ÉPILOGUE : VIVRE AVEC LA FRICTION (2022)
# -------------------------------------------------------------
ch15_html = """<div class="chapter-content">
  <h1 class="chapter-main-title"><strong>15. Épilogue : Vivre avec la friction</strong></h1>
  <p class="chapter-byline">CLÔTURE · Geoffroy Streit (2022)</p>
  <figure class="chapter-figure">
    <img src="public/books/approche-de-la-neurodiversite/images/epilogue-couverture.webp" alt="La Silhouette et le Phare" loading="lazy" />
  </figure>
  <p class="chapter-paragraph">Au terme de cette traversée de plus de vingt années d'expérience et d'écrits, le tableau que nous avons dressé peut sembler rude et sans fard.</p>
  <p class="chapter-paragraph">Il l'est délibérément, parce que le maquillage optimiste du développement personnel ne console personne dans la solitude d'une copie raturée ou d'une relance administrative angoissante. Dire la vérité des troubles dys et du TDA/H, nommer l'épuisement, la honte accumulée et la friction quotidienne, c'est le seul moyen d'arracher ces réalités à l'opprobre du jugement moral.</p>
  <p class="chapter-paragraph">Non, la neurodiversité n'est pas un conte de fées. Elle n'est pas un cadeau du ciel déguisé en énigme, et ceux qui prétendent le contraire n'ont sans doute jamais passé une nuit entière à pleurer sur un formulaire d'embauche ou à se faire insulter au fond d'une cour d'école.</p>
  <p class="chapter-paragraph">Mais refuser l'illusion ne signifie aucunement céder au désespoir.</p>
  <p class="chapter-paragraph">Ceux qui grandissent et vivent avec ces machineries atypiques développent souvent, par la force des choses, des qualités de résilience, une empathie profonde pour les fragilités d'autrui et une inventivité remarquable pour contourner les obstacles là où d'autres se contentent d'emprunter des boulevards balisés.</p>
  <p class="chapter-paragraph">Ils apprennent la patience, l'humilité du recommencement et la valeur inestimable des solidarités discrètes.</p>
  <p class="chapter-paragraph">Accepter son fonctionnement, ce n'est pas hisser le drapeau blanc de la défaite : c'est troquer l'armure trop lourde de la normalité feinte contre un trousseau de clés d'artisan bien ajustées. C'est apprendre à aménager son atelier, à respecter ses rythmes biologiques, à s'entourer de regards qui ne jugent pas, et à savourer chaque victoire avec la fierté légitime de celui qui a dû tout conquérir de haute lutte.</p>
  <p class="chapter-paragraph">La friction ne disparaîtra jamais complètement. Mais lorsqu'on cesse de se battre contre sa propre nature pour bâtir des passerelles d'intelligence et de fraternité, on découvre qu'il est possible de traverser l'existence les yeux grands ouverts, le cœur solide, et la tête haute.</p>
</div>
"""
(out_dir / "15-epilogue-vivre-avec-la-friction.html").write_text(ch15_html, encoding="utf-8")
print("Written 15-epilogue-vivre-avec-la-friction.html")

print("ALL 16 CHAPTERS COMPLETE AND FULLY RESTORED")