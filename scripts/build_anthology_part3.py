# -*- coding: utf-8 -*-
import re
from pathlib import Path
import zipfile, xml.etree.ElementTree as ET

out_dir = Path("public/books/approche-de-la-neurodiversite")
out_dir.mkdir(parents=True, exist_ok=True)
res_dir = Path("D:/0CODE/0 BEST/neurodiversity-explorer-main/src/pages/ressources")

def clean_txt(s: str) -> str:
    s = s.replace("\u2014", ", ").replace("\u2013", ", ").replace("—", ", ").replace("–", ", ")
    s = s.replace("\u00a0", " ").replace("’", "'").replace("‘", "'")
    s = re.sub(r'\s+', ' ', s).strip()
    return s

# 1. 08-les-cinq-familles-de-troubles-cognitifs.html
# Text from troubles dys.odt
p_odt = Path(r"D:\0HYLST\0 HYLST ART 2024\ecrits\Réflexions\troubles dys.odt")
with zipfile.ZipFile(p_odt) as z:
    tree = ET.fromstring(z.read("content.xml"))
    raw_odt = "".join(tree.itertext())

clean_odt = clean_txt(raw_odt)
# Split sections
sections_odt = re.split(r'(?=\b(?:1\.2\.\d|1\.\d|ORIGINE|QUI|CLASSIFICATION|QUAND|CONSÉQUENCES|1\.2\.1\.1|1\.2\.1\.2|1\.2\.2|1\.2\.3|1\.2\.4|1\.2\.5)\b)', clean_odt)
paras_odt = [f'<p class="chapter-paragraph">{s.strip()}</p>' for s in sections_odt if len(s.strip()) > 35]

ch8_html = f"""<div class="chapter-content">
  <h1 class="chapter-main-title"><strong>08. Les cinq familles de troubles cognitifs : langage, geste et calcul</strong></h1>
  <p class="chapter-byline">PARTIE III : ANATOMIE DES CERVEAUX QUI DANSENT · Étude clinique et vécue (2018-2020)</p>
  <figure class="chapter-figure">
    <img src="public/books/approche-de-la-neurodiversite/images/neuro-schema-1-familles.svg" alt="Cartographie des troubles cognitifs et dysfonctionnements associés" loading="lazy" />
  </figure>
{chr(10).join(paras_odt[:25])}
</div>
"""
(out_dir / "08-les-cinq-familles-de-troubles-cognitifs.html").write_text(ch8_html, encoding="utf-8")
print(f"Written 08-les-cinq-familles-de-troubles-cognitifs.html ({len(paras_odt[:25])} paras)")

# 2. 09-la-memoire-dans-la-neurodiversite.html
p_mem = res_dir / "MemoireNeurodiversite.tsx"
txt_mem = p_mem.read_text(encoding="utf-8")
matches_mem = re.findall(r'<(?:p|li)[^>]*>(.*?)</(?:p|li)>', txt_mem, re.DOTALL)
paras_mem = []
for m in matches_mem:
    c = re.sub(r'<[^>]+>', '', m).strip()
    c = clean_txt(c)
    if len(c) > 25:
        paras_mem.append(f'<p class="chapter-paragraph">{c}</p>')

ch9_html = f"""<div class="chapter-content">
  <h1 class="chapter-main-title"><strong>09. La mémoire dans la neurodiversité : un labyrinthe aux multiples facettes</strong></h1>
  <p class="chapter-byline">PARTIE III : ANATOMIE DES CERVEAUX QUI DANSENT · Synthèse cognitive (2024)</p>
{chr(10).join(paras_mem)}
</div>
"""
(out_dir / "09-la-memoire-dans-la-neurodiversite.html").write_text(ch9_html, encoding="utf-8")
print(f"Written 09-la-memoire-dans-la-neurodiversite.html ({len(paras_mem)} paras)")

# 3. 10-navigation-dans-le-labyrinthe-des-idees.html
p_nav = res_dir / "NavigationLabyrintheIdees.tsx"
txt_nav = p_nav.read_text(encoding="utf-8")
matches_nav = re.findall(r'<(?:p|li)[^>]*>(.*?)</(?:p|li)>', txt_nav, re.DOTALL)
paras_nav = []
for m in matches_nav:
    c = re.sub(r'<[^>]+>', '', m).strip()
    c = re.sub(r'\{[^}]+\}', '', c).strip()
    c = clean_txt(c)
    if len(c) > 25:
        paras_nav.append(f'<p class="chapter-paragraph">{c}</p>')

ch10_html = f"""<div class="chapter-content">
  <h1 class="chapter-main-title"><strong>10. Navigation dans le labyrinthe des idées</strong></h1>
  <p class="chapter-byline">PARTIE III : ANATOMIE DES CERVEAUX QUI DANSENT · Guide pour esprits foisonnants (2024)</p>
{chr(10).join(paras_nav)}
</div>
"""
(out_dir / "10-navigation-dans-le-labyrinthe-des-idees.html").write_text(ch10_html, encoding="utf-8")
print(f"Written 10-navigation-dans-le-labyrinthe-des-idees.html ({len(paras_nav)} paras)")

# 4. 11-apprendre-quand-le-cerveau-danse.html
p_strat = res_dir / "StrategiesApprentissage.tsx"
txt_strat = p_strat.read_text(encoding="utf-8")
matches_strat = re.findall(r'<(?:p|li)[^>]*>(.*?)</(?:p|li)>', txt_strat, re.DOTALL)
paras_strat = []
for m in matches_strat:
    c = re.sub(r'<[^>]+>', '', m).strip()
    c = clean_txt(c)
    if len(c) > 25:
        paras_strat.append(f'<p class="chapter-paragraph">{c}</p>')

ch11_html = f"""<div class="chapter-content">
  <h1 class="chapter-main-title"><strong>11. Apprendre quand le cerveau danse : stratégies d'assimilation atypiques</strong></h1>
  <p class="chapter-byline">PARTIE III : ANATOMIE DES CERVEAUX QUI DANSENT · Pratiques d'apprentissage personnalisées (2025)</p>
{chr(10).join(paras_strat)}
</div>
"""
(out_dir / "11-apprendre-quand-le-cerveau-danse.html").write_text(ch11_html, encoding="utf-8")
print(f"Written 11-apprendre-quand-le-cerveau-danse.html ({len(paras_strat)} paras)")

print("PART III FILES COMPLETE")