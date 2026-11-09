# -*- coding: utf-8 -*-
import re
from pathlib import Path

out_dir = Path("public/books/approche-de-la-neurodiversite")
out_dir.mkdir(parents=True, exist_ok=True)
pages_dir = Path("D:/0CODE/0 BEST/neurodiversity-explorer-main/src/pages")
res_dir = pages_dir / "ressources"

def clean_txt(s: str) -> str:
    s = s.replace("\u2014", ", ").replace("\u2013", ", ").replace("—", ", ").replace("–", ", ")
    s = s.replace("\u00a0", " ").replace("’", "'").replace("‘", "'")
    s = re.sub(r'\s+', ' ', s).strip()
    return s

# 1. 04-la-neurodiversite-expliquee-aux-enfants.html
p_enfant = pages_dir / "NeurodiversiteEnfant.tsx"
txt_enfant = p_enfant.read_text(encoding="utf-8")
matches_enfant = re.findall(r'<p[^>]*>(.*?)</p>', txt_enfant, re.DOTALL)
paras_enfant = []
for m in matches_enfant:
    c = re.sub(r'<[^>]+>', '', m).strip()
    c = clean_txt(c)
    if len(c) > 15 and not c.startswith("Par Geoffroy"):
        paras_enfant.append(f'<p class="chapter-paragraph">{c}</p>')

ch4_html = f"""<div class="chapter-content">
  <h1 class="chapter-main-title"><strong>04. La neurodiversité expliquée aux enfants</strong></h1>
  <p class="chapter-byline">PARTIE II : L'ENFANCE, L'ÉCOLE ET LA PÉDAGOGIE DE TERRAIN · Par Geoffroy Streit (Mars 2023)</p>
  <figure class="chapter-figure">
    <img src="public/books/approche-de-la-neurodiversite/images/partie-2-couverture.webp" alt="La Main sur l'Épaule" loading="lazy" />
  </figure>
{chr(10).join(paras_enfant)}
</div>
"""
(out_dir / "04-la-neurodiversite-expliquee-aux-enfants.html").write_text(ch4_html, encoding="utf-8")
print(f"Written 04-la-neurodiversite-expliquee-aux-enfants.html ({len(paras_enfant)} paras)")

# 2. 05-enfants-en-difficulte-scolaire.html
# Text from Enfants en difficulté scolaire.doc
p_doc = Path(r"D:\0HYLST\0 HYLST ART 2024\ecrits\Réflexions\Enfants en difficulté scolaire.doc")
raw_doc = p_doc.read_bytes()
chunks_doc = re.findall(rb'(?:[\x20-\x7E\xC0-\xFF]\x00){4,}', raw_doc)
doc_str = "\n".join([c.decode("utf-16le", errors="ignore") for c in chunks_doc])
lines_doc = [clean_txt(l) for l in doc_str.splitlines() if l.strip() and not l.startswith("Normal") and not l.startswith("Police") and not l.startswith("Titre") and not l.startswith("Times") and not l.startswith("Arial") and not l.startswith("Symbol") and not l.startswith("Liberation") and not l.startswith("Microsoft") and not l.startswith("Lucida") and not l.startswith("Root") and not l.startswith("Corps") and not l.startswith("Liste") and not l.startswith("Légende") and not l.startswith("Index") and not l.startswith("Votre nom")]
# Assemble into paragraphs
paras_doc = []
curr = []
for l in lines_doc:
    if l.startswith("Enfants en difficulté scolaire"):
        continue
    if l.startswith("?") or l.startswith("-"):
        if curr:
            paras_doc.append(" ".join(curr))
            curr = []
        paras_doc.append(l)
    else:
        curr.append(l)
if curr:
    paras_doc.append(" ".join(curr))

clean_paras_doc = [f'<p class="chapter-paragraph">{p}</p>' for p in paras_doc if len(p) > 25]

ch5_html = f"""<div class="chapter-content">
  <h1 class="chapter-main-title"><strong>05. Enfants en difficulté scolaire : guide d'écoute pour parents et tuteurs</strong></h1>
  <p class="chapter-byline">PARTIE II : L'ENFANCE, L'ÉCOLE ET LA PÉDAGOGIE DE TERRAIN · Texte d'archive pédagogique (vers 2004)</p>
{chr(10).join(clean_paras_doc)}
</div>
"""
(out_dir / "05-enfants-en-difficulte-scolaire.html").write_text(ch5_html, encoding="utf-8")
print(f"Written 05-enfants-en-difficulte-scolaire.html ({len(clean_paras_doc)} paras)")

# 3. 06-pedagogie-de-terrain-le-pas-a-pas.html
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

# 4. 07-marre-d-apprendre.html
p_marre = res_dir / "MarreApprendre.tsx"
txt_marre = p_marre.read_text(encoding="utf-8")
matches_marre = re.findall(r'<p[^>]*>(.*?)</p>', txt_marre, re.DOTALL)
paras_marre = []
for m in matches_marre:
    c = re.sub(r'<[^>]+>', '', m).strip()
    c = clean_txt(c)
    if len(c) > 20 and not c.startswith("Par Geoffroy"):
        paras_marre.append(f'<p class="chapter-paragraph">{c}</p>')

ch7_html = f"""<div class="chapter-content">
  <h1 class="chapter-main-title"><strong>07. Marre d'apprendre ! Lettre ouverte aux élèves découragés</strong></h1>
  <p class="chapter-byline">PARTIE II : L'ENFANCE, L'ÉCOLE ET LA PÉDAGOGIE DE TERRAIN · Par Geoffroy Streit (2025)</p>
{chr(10).join(paras_marre)}
</div>
"""
(out_dir / "07-marre-d-apprendre.html").write_text(ch7_html, encoding="utf-8")
print(f"Written 07-marre-d-apprendre.html ({len(paras_marre)} paras)")

print("PART II FILES COMPLETE")