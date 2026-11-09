# -*- coding: utf-8 -*-
import re
from pathlib import Path

out_dir = Path("public/books/approche-de-la-neurodiversite")
out_dir.mkdir(parents=True, exist_ok=True)
res_dir = Path("D:/0CODE/0 BEST/neurodiversity-explorer-main/src/pages/ressources")

def clean_txt(s: str) -> str:
    s = s.replace("\u2014", ", ").replace("\u2013", ", ").replace("—", ", ").replace("–", ", ")
    s = s.replace("\u00a0", " ").replace("’", "'").replace("‘", "'")
    s = re.sub(r'\s+', ' ', s).strip()
    return s

# 1. intro.html
intro_html = """<div class="book-intro-generated">
  <h2>Approche de la Neurodiversité</h2>
  <p class="chapter-byline">Anthologie intégrale (2003-2025) · Vision d'un non-professionnel</p>
  <hr class="ornament">
  <p class="chapter-epigraph" style="font-style: italic; text-align: center; margin: 1.25rem 0; opacity: 0.85;">
    Ce n'est pas un manque de volonté. C'est une machinerie qui frotte à chaque seconde contre un monde qui ne pardonne pas la lenteur.
  </p>
  <h3>Le décalage invisible</h3>
  <p>Ce livre ne vient ni d'une chaire universitaire, ni d'un cabinet de neuropsychologie feutré. Il ne vous promettra aucun miracle, aucune recette magique pour transformer un handicap en « super-pouvoir », et encore moins les formules lénifiantes du développement personnel à la mode. La neurodiversité n'est pas une bénédiction romantique : au quotidien, pour celui qui la porte dans sa chair et dans son cerveau, c'est d'abord une friction permanente, une débauche d'énergie épuisante et une solitude difficile à partager.</p>
  <p>Cette anthologie réunit et consolide plus de vingt années d'expérience et d'écrits de terrain (de mars 2003 à 2025) : celle d'un adulte « dys » et TDA/H qui a dû grandir, apprendre, travailler et survivre avec des circuits cérébraux atypiques, tout en accompagnant d'autres enfants et adolescents confrontés au même mur. L'intelligence est normale, souvent vive, mais le relais se dérobe. La mémoire immédiate sature, le geste se brise, le mot exact refuse de sortir, le calcul élémentaire se brouille, et le regard des autres conclut trop vite à la paresse ou au désintérêt.</p>
  <p>L'approche défendue ici est résolument lucide, asymétrique et sans complaisance. Accepter le pessimisme du constat, ce n'est pas capituler : c'est refuser de se raconter des histoires pour bâtir de vraies béquilles d'artisan, pragmatiques et tenaces, capables de résister à la fatigue du réel.</p>
  <p><strong>16 chapitres</strong> (en quatre mouvements) · rédigé de 2003 à 2025 · compilation numérique en 2026</p>
  <p class="chapter-continuation" style="font-style: italic; text-align: center; margin-top: 1.5rem;">Hylst (Geoffroy Streit)</p>
  <p class="provenance-note">Anthologie intégrale consolidée réunissant les écrits de terrain de l'auteur (Lettre d'un dyspraxique de mars 2003, Confessions d'un chaos organisé de 2005/2024, Navigation dans le labyrinthe des idées, Marre d'apprendre !, les manuscrits d'accompagnement scolaire et la boîte aux 13 béquilles cognitives de juin 2022). Schémas vectoriels SVG et illustrations d'art éditorial créées localement sur GPU (Krea-2-Turbo).</p>
  <p class="chapter-tags" style="font-size: 0.78rem; opacity: 0.7; text-align: center; margin-top: 1.5rem;">
    #neurodiversite #troublesdys #dyspraxie #dyslexie #tdah #cognition #ecole #pedagogie #adulte #bequilles
  </p>
</div>
"""
(out_dir / "intro.html").write_text(intro_html, encoding="utf-8")
print("Written intro.html")

# 2. 00-prologue.html
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

# 3. 01-lettre-d-un-dyspraxique.html
# Extract text from LettreDyspraxique.tsx
p_lettre = res_dir / "LettreDyspraxique.tsx"
txt_lettre = p_lettre.read_text(encoding="utf-8")
matches_lettre = re.findall(r'<p[^>]*>(.*?)</p>', txt_lettre, re.DOTALL)
paras_lettre = []
for m in matches_lettre:
    c = re.sub(r'<[^>]+>', '', m).strip()
    c = clean_txt(c)
    if len(c) > 20 and not c.startswith("Par Geoffroy"):
        paras_lettre.append(f'<p class="chapter-paragraph">{c}</p>')

lettre_html = f"""<div class="chapter-content">
  <h1 class="chapter-main-title"><strong>01. Lettre d'un dyspraxique</strong></h1>
  <p class="chapter-byline">PARTIE I : CONFESSIONS &amp; VÉCUS DE L'INTÉRIEUR · Par Geoffroy Streit (Mars 2003)</p>
  <figure class="chapter-figure">
    <img src="public/books/approche-de-la-neurodiversite/images/partie-1-couverture.webp" alt="L'Archipel des Pensées" loading="lazy" />
  </figure>
  <p class="chapter-paragraph"><strong>Chers compagnons de maladresse,</strong></p>
{chr(10).join(paras_lettre)}
</div>
"""
(out_dir / "01-lettre-d-un-dyspraxique.html").write_text(lettre_html, encoding="utf-8")
print(f"Written 01-lettre-d-un-dyspraxique.html ({len(paras_lettre)} paras)")

# 4. 02-vie-dans-un-chaos-organise.html
p_chaos = res_dir / "VieChaosOrganise.tsx"
txt_chaos = p_chaos.read_text(encoding="utf-8")
matches_chaos = re.findall(r'<p[^>]*>(.*?)</p>', txt_chaos, re.DOTALL)
paras_chaos = []
for m in matches_chaos:
    c = re.sub(r'<[^>]+>', '', m).strip()
    c = clean_txt(c)
    if len(c) > 20 and not c.startswith("Par Geoffroy") and not c.startswith("Confessions"):
        paras_chaos.append(f'<p class="chapter-paragraph">{c}</p>')

chaos_html = f"""<div class="chapter-content">
  <h1 class="chapter-main-title"><strong>02. Vie dans un chaos organisé : confessions d'un cerveau Dys/TDA/H</strong></h1>
  <p class="chapter-byline">PARTIE I : CONFESSIONS &amp; VÉCUS DE L'INTÉRIEUR · Par Geoffroy Streit (2005 et des brouettes, revu en 2024)</p>
  <p class="chapter-paragraph"><strong>Chers amis aux cerveaux câblés différemment,</strong></p>
{chr(10).join(paras_chaos)}
</div>
"""
(out_dir / "02-vie-dans-un-chaos-organise.html").write_text(chaos_html, encoding="utf-8")
print(f"Written 02-vie-dans-un-chaos-organise.html ({len(paras_chaos)} paras)")

# 5. 03-pensee-en-ebullition.html
p_ebull = res_dir / "PenseeEnEbullition.tsx"
txt_ebull = p_ebull.read_text(encoding="utf-8")
matches_ebull = re.findall(r'<p[^>]*>(.*?)</p>', txt_ebull, re.DOTALL)
paras_ebull = []
for m in matches_ebull:
    c = re.sub(r'<[^>]+>', '', m).strip()
    c = clean_txt(c)
    if len(c) > 20:
        paras_ebull.append(f'<p class="chapter-paragraph">{c}</p>')

ebull_html = f"""<div class="chapter-content">
  <h1 class="chapter-main-title"><strong>03. Pensée en ébullition : le volcan des connexions</strong></h1>
  <p class="chapter-byline">PARTIE I : CONFESSIONS &amp; VÉCUS DE L'INTÉRIEUR · Réflexion de terrain (2024)</p>
{chr(10).join(paras_ebull)}
</div>
"""
(out_dir / "03-pensee-en-ebullition.html").write_text(ebull_html, encoding="utf-8")
print(f"Written 03-pensee-en-ebullition.html ({len(paras_ebull)} paras)")

print("TASK 1 FILES COMPLETE")