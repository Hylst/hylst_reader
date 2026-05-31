import zipfile
import xml.etree.ElementTree as ET
import os
import re
import shutil

SOURCE_DIR = 'livres_pour_import/odyssee_energie'
CHAPITRES_DIR = os.path.join(SOURCE_DIR, 'chapitres')
namespaces = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}

os.makedirs(CHAPITRES_DIR, exist_ok=True)

# 1. Copier la couverture générale si elle existe
cover_src = 'public/covers/cover_odyssee_energie.webp'
cover_dst = os.path.join(SOURCE_DIR, 'cover.webp')
if os.path.exists(cover_src) and not os.path.exists(cover_dst):
    shutil.copy2(cover_src, cover_dst)
    print("SUCCESS: Couverture globale copiee vers livres_pour_import/odyssee_energie/cover.webp")

# 2. Créer le fichier config.json pour ce livre
config_path = os.path.join(SOURCE_DIR, 'config.json')
config_content = {
    "title": "L'odyssée de l'énergie",
    "author": "Hylst (Geoffroy Streit)",
    "year": 2026,
    "design": {
        "fonts": {
            "heading": "Outfit",
            "body": "Merriweather",
            "googleFonts": "family=Outfit:wght@300;400;500;600;700&family=Merriweather:ital,wght@0,300;0,400;0,700;1,300;1,400"
        },
        "colors": {
            "background": "#f3f6f7",
            "text": "#1c2833",
            "primary": "#0e6251",
            "secondary": "#d5dbdb",
            "accent": "#f39c12"
        },
        "variables": {
            "--book-bg": "#f3f6f7",
            "--book-text": "#1c2833",
            "--book-accent": "#f39c12",
            "--book-accent-dark": "#0e6251",
            "--book-surface": "#e5e8e8",
            "--book-border": "rgba(14, 98, 81, 0.15)",
            "--book-font-body": "'Merriweather', Georgia, serif",
            "--book-font-heading": "'Outfit', sans-serif",
            "--book-font-title": "'Outfit', sans-serif",
            "--book-font-size": "1.05rem",
            "--book-line-height": "1.85",
            "--book-max-width": "700px",
            "--book-dropcap-size": "4.5em"
        }
    }
}

with open(config_path, 'w', encoding='utf-8') as f:
    import json
    json.dump(config_content, f, ensure_ascii=False, indent=4)
print("SUCCESS: Fichier config.json genere pour L'Odyssee de l'Energie.")

# 3. Créer le fichier intro.html
intro_path = os.path.join(SOURCE_DIR, 'intro.html')
intro_html = """<div class="book-intro-generated">
  <h2>Dernière de couverture</h2>
  <hr class="ornament">
  <p class="dropcap">Voici un plan complet et structuré pour ce second volume. Je le conçois comme un livre complémentaire à part entière &mdash; avec sa propre identité, son propre souffle &mdash; mais conçu pour dialoguer intimement avec <em>L'Odyssée de l'IA</em>.</p>
  <p class="chapter-paragraph"><strong>La thèse centrale :</strong> L'intelligence artificielle n'est pas une entité immatérielle qui existe dans le "cloud". Elle est profondément, irréductiblement <em>physique</em>. Elle consomme de l'électricité, de l'eau, des métaux rares, des puces en silicium, des câbles en cuivre. Et la collision entre sa croissance exponentielle et les contraintes physiques de la planète est l'une des questions les plus urgentes et les moins débattues de notre époque.</p>
  <p class="chapter-paragraph"><strong>Format :</strong> Livre complémentaire &mdash; même style littéraire, même dualité dystopie/renaissance, même ancrage en 2026.<br/>
  <strong>Ton :</strong> Scientifique mais accessible, narratif, incarné dans des exemples concrets, honnête sur les incertitudes.</p>
  <p class="chapter-continuation" style="font-style: italic; text-align: center; margin-top: 1.5rem;">Quand la révolution numérique rencontre les limites physiques du monde réel. Bonne lecture.</p>
</div>
"""
with open(intro_path, 'w', encoding='utf-8') as f:
    f.write(intro_html)
print("SUCCESS: Fichier intro.html genere.")

def parse_docx(docx_path):
    with zipfile.ZipFile(docx_path) as docx:
        tree = ET.parse(docx.open('word/document.xml'))
        root = tree.getroot()
        
        paragraphs = []
        for p in root.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p'):
            p_text_parts = []
            for r in p.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}r'):
                rPr = r.find('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}rPr', namespaces)
                is_bold = False
                is_italic = False
                if rPr is not None:
                    if rPr.find('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}b', namespaces) is not None:
                        is_bold = True
                    if rPr.find('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}i', namespaces) is not None:
                        is_italic = True
                
                run_text = []
                for t in r.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t'):
                    if t.text:
                        run_text.append(t.text)
                
                text = "".join(run_text)
                if text:
                    if is_bold:
                        text = f"<strong>{text}</strong>"
                    if is_italic:
                        text = f"<em>{text}</em>"
                    p_text_parts.append(text)
            
            paragraph_text = "".join(p_text_parts).strip()
            if paragraph_text:
                paragraphs.append(paragraph_text)
        return paragraphs

# Convertir les 8 chapitres
for ch_idx in range(1, 9):
    docx_filename = f"odyssee_energie_ch{ch_idx}.docx"
    docx_path = os.path.join(SOURCE_DIR, docx_filename)
    
    if not os.path.exists(docx_path):
        print(f"WARNING: Chapitre {ch_idx} non trouve : {docx_path}")
        continue
        
    print(f"INFO: Analyse de {docx_filename}...")
    paras = parse_docx(docx_path)
    
    html_parts = []
    
    # Extraire Quote, Title, Subtitle
    if ch_idx == 1:
        # Chapitre 1 a des métadonnées de couverture supplémentaires aux indices 0 à 5
        quote = paras[8].strip('"').strip('«').strip('»').strip()
        title = paras[6] # "Préambule"
        subtitle = paras[7] # "Une requête et ses conséquences invisibles"
        content_paras = paras[9:]
    else:
        # Chapitres 2 à 8
        title = paras[0] # "Chapitre X"
        subtitle = paras[1] + " — " + paras[2] # "Titre — Sous-titre"
        quote = paras[3].strip('"').strip('«').strip('»').strip()
        content_paras = paras[4:]
        
    # Ajouter la ligne d'accroche centré en italique avec guillemets français
    html_parts.append(f'<p class="chapter-paragraph" style="text-align: center; font-style: italic; font-size: 1.15rem; margin-bottom: 1.5rem;">« {quote} »</p>')
    # Ajouter l'image d'illustration
    html_parts.append(f'<figure class="chapter-cover"><img src="chapitre-{ch_idx}-cover.webp" alt="Chapitre {ch_idx} : couverture" /></figure>')
    # Titres du chapitre
    html_parts.append(f'<h1 class="chapter-main-title">{title}</h1>')
    html_parts.append(f'<h2 class="chapter-subtitle">{subtitle}</h2>')
    
    first_paragraph_done = False
    
    for para in content_paras:
        # Remplacer les tirets cadratins doubles et simples par des tirets d'incise propres
        para = para.replace(' — ', ' &mdash; ').replace(' - ', ' &mdash; ')
        
        # Détecter les sous-sections comme "1.1 — ..." ou "1.1 - ..."
        sub_match = re.match(r'^(<strong>)?(\d+\.\d+)\s+&mdash;\s+(.+)(</strong>)?$', para)
        if not sub_match:
            sub_match = re.match(r'^(<strong>)?(\d+\.\d+)\s*:\s*(.+)(</strong>)?$', para)
        if not sub_match:
            sub_match = re.match(r'^(<strong>)?(\d+\.\d+)\s+(.+)(</strong>)?$', para)
            
        if sub_match:
            num = sub_match.group(2)
            sect_title = re.sub(r'</?(strong|em)>', '', sub_match.group(3))
            html_parts.append(f'<h3 class="subsection-heading"><span class="subsection-number">{num}</span> {sect_title}</h3>')
            continue
            
        # Détecter d'autres en-têtes de section comme "Sources :" ou "Encadré :"
        if re.match(r'^(<strong>)?(Sources|Encadré|Note de l\'Auteur|Annexe)\s*:(</strong>)?', para, re.IGNORECASE):
            html_parts.append(f'<h3 class="labeled-section">{para.rstrip(":")}<span class="section-colon">:</span></h3>')
            continue
            
        # Paragraphes normaux / Lettrine
        css_class = 'chapter-paragraph'
        if not first_paragraph_done and len(para) > 60 and not para.startswith('<strong>'):
            css_class = 'dropcap'
            first_paragraph_done = True
            
        html_parts.append(f'<p class="{css_class}">{para}</p>')
        
    # Écrire le fichier de sortie HTML dans le dossier chapitres/
    output_filename = f"chapitre-{ch_idx}.html"
    output_path = os.path.join(CHAPITRES_DIR, output_filename)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(html_parts))
        
    print(f"SUCCESS: Chapitre {ch_idx} genere dans {output_path}")

print("\nSUCCESS: TOUS LES CHAPITRES DE L'ODYSSÉE DE L'ÉNERGIE ONT ÉTÉ CONVERTIS !")
