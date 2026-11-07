# Carnets, réflexions & partages et Sciences et technologie : plan d'implémentation

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Publier dans La Bibliothèque de Hylst le Tome IV « Carnets, réflexions & partages » et un livre « Sciences et technologie » qui reproduit l'étude technique de 2001-2002 en PDF avec une préface et quatre chapitres de synthèse de 2026.

**Architecture:** Deux nouveaux livres du catalogue `public/books.json`, servis par la liseuse React comme les sept livres existants. Chaque livre reçoit une introduction, un design propre et des chapitres HTML dans `public/books/<id>/`. Le livre scientifique ajoute quatre PDF exportés depuis les `.docx` d'origine et un bloc de téléchargement par partie. Les fiches statiques `livres/<id>/index.html` sont régénérées par le script existant.

**Tech Stack:** HTML statique, JSON, Python 3 (PIL, pypdf), PowerShell + Word COM, scripts existants `build_book_pages.py`, `build_jsx.js`, `check_dashes.py`, `sync-to-platform.ps1`.

**Spec:** `docs/superpowers/specs/2026-11-07-carnets-sciences-design.md`

## Global Constraints

- Aucun tiret cadratin ou demi-cadratin (U+2012, U+2013, U+2014, U+2015, U+FE58) dans les contenus servis. Vérification finale : `python scripts/check_dashes.py --root . --all`.
- Ne rien supprimer dans `D:\0HYLST\0 HYLST ART 2024\ecrits\textes_a_trier\`.
- Aucun CDN, aucun script inline, aucune nouvelle dépendance runtime.
- Les sources HTML de `public/books/` sont écrites à la main, jamais régénérées automatiquement.
- Les textes de réflexion sont réécrits légèrement : syntaxe, répétitions, coquilles, ponctuation, scories de blog. Images, parenthèses et jeux de mots conservés. Aucune idée ajoutée.
- L'étude technique n'est pas réécrite : seuls la préface, les résumés et les sommaires de 2026 sont nouveaux.
- Chaque chapitre du Tome IV affiche sa date d'origine et une note de source.
- Chaque partie scientifique affiche un résumé 2026, le sommaire d'origine, le lien PDF et une note de source.
- Les PDF ne sont pas précachés par le Service Worker.
- Le cache source passe de `hylst-reader-v66` à `hylst-reader-v67`.
- Le miroir de production est `D:\0CODE\AntiGravity\Cours_Memos\Docker\books_reader`. Test local via `http://127.0.0.1:8765/books_reader/`.
- Aucune synchronisation ni compilation JSX n'est lancée avant que les deux livres soient complets.

## Review Focus

- Un texte réécrit qui trahit la voix de l'auteur (vocabulaire remplacé, ironie gommée, digressions supprimées) : la réécriture doit rester une correction, pas une réécriture littéraire.
- Un sommaire d'origine inventé ou une pagination présentée comme exacte alors que l'original est ambigu : les numéros incertains doivent être signalés ou omis, jamais devinés.
- Un PDF tronqué ou sans images qui passerait la vérification de poids : contrôler le nombre de pages et rendre la première page en PNG.
- Un lien PDF relatif qui casse dans la liseuse ou dans la fiche statique : utiliser le chemin absolu `/books_reader/public/books/sciences-et-technologie-jeux-videos/pdf/...`.
- Un chapitre ajouté au catalogue mais absent du précache du Service Worker, ou l'inverse : vérifier que `sw.js` liste bien chaque nouvelle introduction et chaque nouveau chapitre.

---

## Task 1: Composants partagés et styles

**Files:**
- Modify: `css/reader.css` (ajout en fin de fichier)
- Test: `python -c "..."` de présence des classes

**Interfaces:**
- Produces: classes `.chapter-download`, `.chapter-download-link`, `.chapter-download-meta`, `.chapter-original-toc`, `.chapter-original-toc ol`, `.chapter-summary`, `.chapter-context`.

- [ ] **Step 1: Ajouter les styles**

À la fin de `css/reader.css`, ajouter :

```css
/* Bloc de téléchargement PDF (livre Sciences et technologie) */
.chapter-download {
    margin: 2.5rem auto;
    max-width: 620px;
    padding: 1.4rem 1.6rem;
    background: color-mix(in srgb, var(--book-surface) 55%, transparent);
    border: 1px solid var(--book-border);
    border-radius: 12px;
    text-align: center;
}
.chapter-download-link {
    display: inline-flex;
    align-items: center;
    gap: 0.55rem;
    padding: 0.7rem 1.4rem;
    background: var(--book-accent-dark);
    color: var(--book-bg);
    border-radius: 8px;
    font-family: var(--font-sans, sans-serif);
    font-size: 0.92rem;
    text-decoration: none;
}
.chapter-download-link:hover { opacity: 0.88; }
.chapter-download-meta {
    margin-top: 0.7rem;
    font-family: var(--font-sans, sans-serif);
    font-size: 0.75rem;
    opacity: 0.65;
}
.chapter-download-note {
    margin-top: 0.5rem;
    font-size: 0.8rem;
    opacity: 0.75;
}

/* Sommaire d'origine d'une partie */
.chapter-original-toc {
    margin: 1.5rem 0 2.5rem;
    padding: 1.2rem 1.6rem;
    border-left: 3px solid var(--book-accent);
    background: color-mix(in srgb, var(--book-surface) 45%, transparent);
}
.chapter-original-toc h3 {
    margin-top: 0;
    font-size: 1.05rem;
    letter-spacing: 0.02em;
}
.chapter-original-toc ol {
    margin: 0;
    padding-left: 1.2rem;
    font-family: var(--font-sans, sans-serif);
    font-size: 0.85rem;
    line-height: 1.7;
}
.chapter-original-toc li { margin-bottom: 0.15rem; }
.chapter-original-toc .toc-page { opacity: 0.55; }

/* Contexte et résumé de 2026 */
.chapter-context {
    text-align: center;
    font-family: var(--font-sans, sans-serif);
    font-size: 0.75rem;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: var(--book-accent-dark);
    opacity: 0.7;
    margin-bottom: 2rem;
}
.chapter-summary {
    margin-bottom: 1.4rem;
}
```

- [ ] **Step 2: Vérifier**

Run: `python -c "s=open('css/reader.css',encoding='utf-8').read(); print(all(c in s for c in ['chapter-download','chapter-original-toc','chapter-summary','chapter-context']))"`
Expected: `True`

---

## Task 2: Couvertures

**Files:**
- Create: `scripts/make_book_covers.py`
- Create: `public/covers/recueils-proses-poesies-t4-carnets-reflexions-partages.webp`
- Create: `public/covers/sciences-et-technologie-jeux-videos.webp`

**Interfaces:**
- Consumes: polices Windows `C:/Windows/Fonts/georgiab.ttf`, `georgiai.ttf`, `segoeuib.ttf`, `seguisb.ttf`.
- Produces: deux WebP 600x900, poids < 250 Ko, sans tiret cadratin.

- [ ] **Step 1: Écrire le script**

Créer `scripts/make_book_covers.py`. Le script compose les deux couvertures directement en PIL, sans image générée : fond texturé par dégradé et bruit déterministe, filets, titre, sous-titre, auteur. Aucun texte confié à un modèle d'image.

```python
# -*- coding: utf-8 -*-
"""Compose les couvertures du Tome IV et du livre Sciences et technologie."""
from pathlib import Path
import random
from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "public" / "covers"
W, H = 600, 900

def font(path, size):
    return ImageFont.truetype(path, size)

def centered(draw, y, text, fnt, fill, spacing=0):
    if spacing:
        total = sum(draw.textlength(c, font=fnt) + spacing for c in text) - spacing
        x = (W - total) / 2
        for c in text:
            draw.text((x, y), c, font=fnt, fill=fill)
            x += draw.textlength(c, font=fnt) + spacing
        return
    w = draw.textlength(text, font=fnt)
    draw.text(((W - w) / 2, y), text, font=fnt, fill=fill)

def wrap(draw, text, fnt, max_width):
    words, lines, line = text.split(), [], ""
    for word in words:
        trial = f"{line} {word}".strip()
        if draw.textlength(trial, font=fnt) <= max_width:
            line = trial
        else:
            lines.append(line)
            line = word
    if line:
        lines.append(line)
    return lines

def paper(bg, grain, seed):
    rnd = random.Random(seed)
    im = Image.new("RGB", (W, H), bg)
    px = im.load()
    for y in range(H):
        for x in range(0, W, 2):
            d = rnd.randint(-grain, grain)
            r, g, b = px[x, y]
            px[x, y] = (max(0, min(255, r + d)), max(0, min(255, g + d)), max(0, min(255, b + d)))
    return im.filter(ImageFilter.GaussianBlur(0.4))
```

Le corps du script définit deux fonctions `cover_tome4()` et `cover_sciences()` qui suivent les compositions ci-dessous, puis les enregistre en WebP qualité 88.

Composition Tome IV :
- fond papier chaud `#f3ecdf`, grain 6, vignettage brun léger ;
- cadre filet cuivre `#b4682f` à 40 px des bords, double trait ;
- en haut, en petites capitales espacées : `RECUEILS DE PROSES ET POÉSIES FANTASQUES` ;
- au centre : `TOME IV` en 34 px, puis `Carnets,` / `réflexions` / `& partages` en georgiab 84/72/64 px, couleur `#2a241d` ;
- sous le titre, filet cuivre de 120 px ;
- en bas : `Hylst` en georgiai 46 px, puis `Geoffroy Streit` en sans 22 px ;
- coins : petite fleur ou arabesque dessinée en traits, pas de texte.

Composition Sciences :
- fond papier froid `#edf1f3`, grain 4, fine grille technique bleu-gris très pâle tous les 30 px ;
- bandeau supérieur bleu `#1f4b63` de 190 px avec `SCIENCES & TECHNOLOGIE` en sans bold 30 px, blanc, espacé ;
- au centre : `Analyse des solutions` / `techniques mises en œuvre` / `dans les jeux vidéos` en georgiab 44 px, couleur `#1a2830` ;
- sous le titre, filet ambre `#b5732b` de 160 px ;
- plus bas : `Étude technique bibliographique` en sans 20 px, puis `2001-2002` en sans bold 30 px ambre ;
- en bas : `Hylst (Geoffroy Streit)` en sans 20 px, puis `Édition numérique 2026` en sans 16 px.

- [ ] **Step 2: Exécuter**

Run: `python scripts/make_book_covers.py`
Expected: deux lignes `public/covers/....webp (600, 900)`.

- [ ] **Step 3: Vérifier taille et rendu**

Run: `python -c "from PIL import Image; import os; [print(p, Image.open('public/covers/'+p).size, os.path.getsize('public/covers/'+p)) for p in ['recueils-proses-poesies-t4-carnets-reflexions-partages.webp','sciences-et-technologie-jeux-videos.webp']]"`
Expected: `(600, 900)` et poids inférieur à 250 000 octets pour chacun.

Ouvrir les deux images avec l'outil de lecture pour contrôle visuel : texte net, aucun chevauchement, titre lisible en vignette.

---

## Task 3: Tome IV, introduction

**Files:**
- Create: `public/books/recueils-proses-poesies-t4-carnets-reflexions-partages/intro.html`

**Interfaces:**
- Produces: structure `div.book-intro-generated` identique aux tomes I à III.

- [ ] **Step 1: Écrire l'introduction**

```html
<div class="book-intro-generated">
  <h2>Recueils de proses et poésies fantasques</h2>
  <p class="chapter-byline">Tome IV</p>
  <hr class="ornament">
  <h3>Carnets, réflexions &amp; partages</h3>
  <p>Ce tome est le versant non fictif de la série. Quatre textes retrouvés dans mes archives, écrits entre 2003 et 2024, où je ne raconte pas d'histoire : je parle de moi, de la société, des cadeaux qu'on fabrique et de ce qu'apprendre veut dire.</p>
  <p>Ils n'avaient pas leur place dans les trois recueils précédents, qui rassemblent des proses et des poésies. Ici, la matière est le carnet : l'aveu de fatigue, la fable politique, l'article pratique, le plaidoyer adressé à un plus jeune que soi.</p>
  <p>Je les ai relus et corrigés légèrement : orthographe, ponctuation, répétitions, abréviations de blog. Les images, les parenthèses et les jeux de mots sont restés. Chaque texte garde sa date d'origine en tête et une note de source en fin de chapitre.</p>
  <p>Le fil qui les relie tient en quelques mots : se tenir debout, regarder la société en face, offrir ce qu'on peut fabriquer, transmettre ce qu'on a compris.</p>
  <p><strong>4 textes</strong> · du 23 novembre 2003 à 2024</p>
  <p class="chapter-continuation" style="font-style: italic; text-align: center; margin-top: 1.5rem;">Textes retrouvés dans les archives de l'auteur, relus et adaptés pour cette édition numérique.<br>Hylst (Geoffroy Streit)</p>
  <p class="provenance-note">Textes écrits par Geoffroy Streit (Hylst), sans assistance d'intelligence artificielle. La réécriture légère et la mise en page ont été réalisées avec des outils techniques.</p>
</div>
```

- [ ] **Step 2: Vérifier**

Run: `python scripts/check_dashes.py --root . --all`
Expected: `[OK] Aucun tiret cadratin ou demi-cadratin`.

---

## Task 4: Tome IV, chapitre 1 « Hygiène de vie »

**Files:**
- Read: `D:\0HYLST\0 HYLST ART 2024\ecrits\textes_a_trier\03_REFLEXIONS\hygiene-de-vie.md`
- Create: `public/books/recueils-proses-poesies-t4-carnets-reflexions-partages/01-hygiene-de-vie.html`

**Interfaces:**
- Produces: structure `chapter-content`, `h1.chapter-main-title`, `p.chapter-byline`, `hr.chapter-divider`, `p.chapter-paragraph`, `p.chapter-source-note`.

- [ ] **Step 1: Relire la source en entier**

Lire les 78 lignes de `hygiene-de-vie.md`. Repérer les idées conservées : fatigue mentale, physique et morale ; tempérament d'énergie ; coups du sort ; refus de devenir larve ; besoin de sortir, marcher, respirer ; chocolat noir aux écorces d'orange ; cerveau muscle ; glucose, magnésium, phosphore ; sommeil ; eau ; respiration.

- [ ] **Step 2: Réécrire**

Réécriture moyenne à lourde, en gardant la première personne et le ton d'aveu. Retirer `lol`, `;o)`, `☺`, les abréviations (`qques`, `vmt`, `tjrs`), les émoticônes et les passages trop hachés. Garder les images et les parenthèses. Ne pas transformer le texte en article de santé : les conseils restent personnels, avec leurs hésitations.

Structure HTML :

```html
<div class="chapter-content">
  <h1 class="chapter-main-title"><strong>I. Hygiène de vie</strong></h1>
  <p class="chapter-byline">Texte écrit le 23 novembre 2003</p>
  <hr class="chapter-divider" />
  <p class="chapter-paragraph">...</p>
  <h2>...</h2>
  <p class="chapter-paragraph">...</p>
  <p class="chapter-source-note">Version originale retrouvée dans les archives de l'auteur, texte du 23 novembre 2003. Réécriture légère en 2026 : orthographe, ponctuation, répétitions et abréviations de blog. Les images et les parenthèses ont été conservées.</p>
</div>
```

- [ ] **Step 3: Vérifier les scories**

Run: `python -c "s=open('public/books/recueils-proses-poesies-t4-carnets-reflexions-partages/01-hygiene-de-vie.html',encoding='utf-8').read().lower(); print([w for w in ['lol','qques','vmt','tjrs',':o)','☺','=)'] if w in s])"`
Expected: `[]`

---

## Task 5: Tome IV, chapitre 2 « Imaginez-vous »

**Files:**
- Read: `D:\0HYLST\0 HYLST ART 2024\ecrits\textes_a_trier\03_REFLEXIONS\imaginez-vous.md`
- Create: `public/books/recueils-proses-poesies-t4-carnets-reflexions-partages/02-imaginez-vous.html`

- [ ] **Step 1: Relire la source**

Conserver : l'entreprise en difficulté, la fidélité des salariés, le poste de direction à durée limitée de cinq ans, le vote du personnel, le candidat sortant non reconduit, le parachute doré, puis la transposition à la France, les deux candidats et les trois questions finales. Corriger les accords (`auquel`, `difficiles`), les subordonnées et les `=)`.

- [ ] **Step 2: Écrire le chapitre**

Même structure que la Task 4, avec :

```html
<h1 class="chapter-main-title"><strong>II. Imaginez-vous</strong></h1>
<p class="chapter-byline">Texte écrit le 19 juin 2007</p>
```

Note de source : date du 19 juin 2007, réécriture légère, ton de fable politique conservé.

- [ ] **Step 3: Vérifier**

Run: `python -c "s=open('public/books/recueils-proses-poesies-t4-carnets-reflexions-partages/02-imaginez-vous.html',encoding='utf-8').read(); print('19 juin 2007' in s, 'chapter-source-note' in s)"`
Expected: `True True`

---

## Task 6: Tome IV, chapitre 3 « Idées cadeaux »

**Files:**
- Read: `D:\0HYLST\0 HYLST ART 2024\ecrits\textes_a_trier\03_REFLEXIONS\idees-cadeaux.md`
- Create: `public/books/recueils-proses-poesies-t4-carnets-reflexions-partages/03-idees-cadeaux.html`

- [ ] **Step 1: Relire la source**

Conserver le catalogue : dessin, peinture, photographie, écriture, musique, pâte à sel, papier mâché, papier vieilli, parfum, bougies, cadres, couture, cuisine. Conserver les recettes et les proportions. Conserver le jeu de mots sur Louis et l'ouïe. Retirer la formule de contact finale et les `\!`.

- [ ] **Step 2: Écrire le chapitre**

Même structure, avec :

```html
<h1 class="chapter-main-title"><strong>III. Idées cadeaux</strong></h1>
<p class="chapter-byline">Texte écrit le 5 septembre 2008</p>
```

Les listes peuvent utiliser `<ul>` et `<li>` dans `.chapter-content`, ou des `p.chapter-paragraph` précédés d'un tiret simple. Ne pas utiliser de tiret cadratin.

- [ ] **Step 3: Vérifier**

Run: `python -c "s=open('public/books/recueils-proses-poesies-t4-carnets-reflexions-partages/03-idees-cadeaux.html',encoding='utf-8').read(); print('5 septembre 2008' in s, 'pâte à sel' in s, 'Louis' in s)"`
Expected: `True True True`

---

## Task 7: Tome IV, chapitre 4 « Marre d'apprendre »

**Files:**
- Read: `D:\0HYLST\0 HYLST ART 2024\ecrits\textes_a_trier\03_REFLEXIONS\marre-d-apprendre.md`
- Create: `public/books/recueils-proses-poesies-t4-carnets-reflexions-partages/04-marre-d-apprendre.html`

- [ ] **Step 1: Relire la source**

Conserver la structure en quatre parties, l'adresse au jeune lecteur, les lunettes magiques, l'escalier de la connaissance, le `tilt`, le super-cerveau, les exemples (Google, IA, cabane, fusée, jeu vidéo). Retirer les majuscules décoratives, les `\!`, les puces Markdown et les effets de mise en forme. Garder le ton direct.

- [ ] **Step 2: Écrire le chapitre**

Même structure, avec :

```html
<h1 class="chapter-main-title"><strong>IV. Marre d'apprendre</strong></h1>
<p class="chapter-byline">Texte écrit vers 2024</p>
```

Note de source : préciser que la date exacte n'a pas été retrouvée.

- [ ] **Step 3: Vérifier**

Run: `python -c "s=open('public/books/recueils-proses-poesies-t4-carnets-reflexions-partages/04-marre-d-apprendre.html',encoding='utf-8').read(); print('vers 2024' in s, s.count('<h2') >= 3)"`
Expected: `True True`

---

## Task 8: Catalogue et précache du Tome IV

**Files:**
- Modify: `public/books.json`
- Modify: `sw.js`
- Create: `livres/recueils-proses-poesies-t4-carnets-reflexions-partages/index.html` (généré)

**Interfaces:**
- Consumes: les cinq fichiers de la Task 3 à la Task 7.
- Produces: entrée de catalogue `recueils-proses-poesies-t4-carnets-reflexions-partages`, précache v67.

- [ ] **Step 1: Ajouter l'entrée dans `public/books.json`**

Après l'entrée du Tome III, ajouter un objet avec :

```json
{
  "id": "recueils-proses-poesies-t4-carnets-reflexions-partages",
  "title": "Carnets, réflexions & partages",
  "subtitle": "Recueils de proses et poésies fantasques · Tome IV",
  "author": "Hylst (Geoffroy Streit)",
  "year": 2026,
  "authorship": "human",
  "aiAssisted": false,
  "badge": "Textes retrouvés",
  "coverPath": "covers/recueils-proses-poesies-t4-carnets-reflexions-partages.webp",
  "introPath": "books/recueils-proses-poesies-t4-carnets-reflexions-partages/intro.html",
  "source": {
    "platform": "Archives personnelles",
    "importedAt": "2026-11-07"
  },
  "design": {
    "fonts": {
      "heading": "Cormorant Garamond",
      "body": "Libre Baskerville",
      "googleFonts": "family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,600&family=Libre+Baskerville:ital,wght@0,400;0,700;1,400"
    },
    "colors": {
      "background": "#f3ecdf",
      "text": "#2a241d",
      "primary": "#7a4a2b",
      "secondary": "#e8ddc9",
      "accent": "#b4682f"
    },
    "variables": {
      "--book-bg": "#f3ecdf",
      "--book-text": "#2a241d",
      "--book-accent": "#b4682f",
      "--book-accent-dark": "#7a4a2b",
      "--book-surface": "#e8ddc9",
      "--book-border": "rgba(122, 74, 43, 0.18)",
      "--book-font-body": "'Libre Baskerville', Georgia, serif",
      "--book-font-heading": "'Cormorant Garamond', Georgia, serif",
      "--book-font-title": "'Cormorant Garamond', Georgia, serif",
      "--book-font-size": "1.04rem",
      "--book-line-height": "1.85",
      "--book-max-width": "700px",
      "--book-dropcap-size": "4.5em"
    }
  },
  "chapters": [
    { "id": "01-hygiene-de-vie.html", "title": "I. Hygiène de vie", "path": "books/recueils-proses-poesies-t4-carnets-reflexions-partages/01-hygiene-de-vie.html", "available": true, "originalDate": "2003-11-23" },
    { "id": "02-imaginez-vous.html", "title": "II. Imaginez-vous", "path": "books/recueils-proses-poesies-t4-carnets-reflexions-partages/02-imaginez-vous.html", "available": true, "originalDate": "2007-06-19" },
    { "id": "03-idees-cadeaux.html", "title": "III. Idées cadeaux", "path": "books/recueils-proses-poesies-t4-carnets-reflexions-partages/03-idees-cadeaux.html", "available": true, "originalDate": "2008-09-05" },
    { "id": "04-marre-d-apprendre.html", "title": "IV. Marre d'apprendre", "path": "books/recueils-proses-poesies-t4-carnets-reflexions-partages/04-marre-d-apprendre.html", "available": true, "originalDate": "2024" }
  ]
}
```

- [ ] **Step 2: Passer le cache en v67**

Dans `sw.js`, remplacer `const CACHE_NAME = 'hylst-reader-v66';` par `const CACHE_NAME = 'hylst-reader-v67';`. Vérifier que `precacheBooks` lit `books.json` et précache automatiquement les nouveaux chapitres. Si la liste est statique, ajouter les cinq chemins.

- [ ] **Step 3: Valider le JSON et générer la fiche**

Run: `python -c "import json; d=json.load(open('public/books.json',encoding='utf-8')); print(len(d), [b['id'] for b in d][-2:])"`
Expected: `9` puis les deux nouveaux identifiants (le second après la Task 14).

Run: `python scripts/build_book_pages.py`
Expected: génération des fiches, dont `livres/recueils-proses-poesies-t4-carnets-reflexions-partages/index.html`.

---

## Task 9: Export des quatre PDF

**Files:**
- Create: `scripts/export_etjv_pdfs.ps1`
- Create: `public/books/sciences-et-technologie-jeux-videos/pdf/partie-a-introduction-histoire-interfaces-manuelles.pdf`
- Create: `public/books/sciences-et-technologie-jeux-videos/pdf/partie-b-interfaces-sensori-motrices.pdf`
- Create: `public/books/sciences-et-technologie-jeux-videos/pdf/partie-c-interfaces-de-visualisation.pdf`
- Create: `public/books/sciences-et-technologie-jeux-videos/pdf/partie-d-capteurs-autres-systemes.pdf`
- Create: `public/books/sciences-et-technologie-jeux-videos/pdf/manifest.json`

**Interfaces:**
- Consumes: `D:\0HYLST\0 HYLST ART 2024\ecrits\textes_a_trier\04_ARCHIVES_TECHNIQUES\sources-word\etjv-{a,b,c,d}.docx`.
- Produces: quatre PDF et un manifeste avec `pages`, `bytes`, `sha256`.

- [ ] **Step 1: Écrire le script PowerShell**

Le script ouvre Word en mode invisible, pour chaque document : `Documents.Open`, lit `ComputeStatistics(2)` (pages), `ExportAsFixedFormat($dest, 17)`, ferme sans sauvegarder, puis écrit `manifest.json` en UTF-8. Il échoue si un PDF fait moins de 100 Ko ou zéro page. Il libère Word dans un `finally`.

- [ ] **Step 2: Exécuter**

Run: `powershell -ExecutionPolicy Bypass -File scripts/export_etjv_pdfs.ps1`
Expected: quatre lignes `OK <fichier> <pages> pages <octets> octets`, puis `manifest.json`.

- [ ] **Step 3: Contrôler les PDF**

Run: `python -c "import json; m=json.load(open('public/books/sciences-et-technologie-jeux-videos/pdf/manifest.json',encoding='utf-8')); [print(x['file'], x['pages'], x['bytes']) for x in m]"`
Expected: quatre entrées, pages > 0, bytes > 100000.

Run: `python -c "import fitz; d=fitz.open('public/books/sciences-et-technologie-jeux-videos/pdf/partie-a-introduction-histoire-interfaces-manuelles.pdf'); p=d[0]; pix=p.get_pixmap(dpi=80); pix.save('C:/Users/Geoffroy/AppData/Local/Temp/opencode/etjv-a-p1.png'); print(d.page_count)"`
Expected: nombre de pages cohérent avec le manifeste ; ouvrir le PNG pour vérifier que la première page est lisible.

---

## Task 10: Livre Sciences, introduction

**Files:**
- Create: `public/books/sciences-et-technologie-jeux-videos/intro.html`

- [ ] **Step 1: Écrire l'introduction**

```html
<div class="book-intro-generated">
  <h2>Sciences et technologie</h2>
  <p class="chapter-byline">Étude technique bibliographique · 2001-2002</p>
  <hr class="ornament">
  <h3>Analyse des solutions techniques mises en œuvre dans les jeux vidéos</h3>
  <p>Cette étude a été écrite en 2001 et 2002, dans le cadre de la cinquième année NFIO, promotion 7. Elle cherchait à comprendre comment un jeu vidéo fonctionne, du clavier au visiocasque, en passant par les capteurs, les afficheurs et les techniques de numérisation.</p>
  <p>Elle est publiée ici telle qu'elle a été rédigée, avec ses schémas, ses références et ses images d'époque. Une préface de 2026 dit ce qu'elle a bien vu, ce qu'elle ne pouvait pas voir et comment la lire. Quatre parties reprennent ensuite l'étude, chacune avec un résumé, son sommaire d'origine et le PDF complet.</p>
  <p>Ce n'est pas un état de l'art de 2026. C'est une archive : un travail d'étudiant, daté, documenté, parfois naïf, souvent juste sur l'essentiel.</p>
  <p><strong>5 chapitres</strong> · préface 2026 et étude de 2001-2002</p>
  <p class="chapter-continuation" style="font-style: italic; text-align: center; margin-top: 1.5rem;">Étude originale conservée en PDF, préface et synthèses écrites pour cette édition numérique.<br>Hylst (Geoffroy Streit)</p>
  <p class="provenance-note">Étude et préface écrites par Geoffroy Streit (Hylst), sans assistance d'intelligence artificielle. L'export PDF et la mise en page ont été réalisés avec des outils techniques.</p>
</div>
```

- [ ] **Step 2: Vérifier**

Run: `python scripts/check_dashes.py --root . --all`
Expected: `[OK]`.

---

## Task 11: Livre Sciences, préface 2026

**Files:**
- Create: `public/books/sciences-et-technologie-jeux-videos/00-preface.html`

- [ ] **Step 1: Écrire la préface**

Structure : titre, ligne de contexte, corps en sections `<h2>`, note de source. Contenu imposé par la spec, section 6.5 :

- le cadre (NFIO promotion 7, 5e année, 2001-2002) et la commande ;
- la méthode (documentation constructeurs, presse spécialisée, fiches techniques, aucune mesure en laboratoire) ;
- ce que l'étude a bien vu (l'interface comme cœur du jeu, l'immersion, la latence, la résolution, le champ de vision, le coût, l'encombrement, la calibration) ;
- ce qu'elle ne pouvait pas voir (smartphone comme manette, suivi inside-out, centrales MEMS, vision par ordinateur, sans-fil, LCD puis OLED, disparition du CRT et du plasma, GPU, distribution en ligne, IA générative) ;
- ce qui reste utile (grille d'analyse, distinction interfaces sensorielles et sensori-motrices, attention au corps et à la calibration) ;
- le statut du document et la restauration numérique.

Longueur cible : 900 à 1300 mots. Ton : lucide, sans auto-complaisance, sans prétendre que l'étude avait tout prévu.

Note de source :

```html
<p class="chapter-source-note">Préface écrite en novembre 2026 pour cette édition numérique. L'étude reproduite reste celle de 2001-2002, sans mise à jour technique.</p>
```

- [ ] **Step 2: Vérifier**

Run: `python -c "import re; s=open('public/books/sciences-et-technologie-jeux-videos/00-preface.html',encoding='utf-8').read(); print(len(re.sub('<[^>]+>',' ',s).split()), 'OLED' in s, 'calibration' in s)"`
Expected: environ 900 à 1300 mots, `True True`.

---

## Task 12: Livre Sciences, quatre parties

**Files:**
- Create: `public/books/sciences-et-technologie-jeux-videos/01-partie-a.html`
- Create: `public/books/sciences-et-technologie-jeux-videos/02-partie-b.html`
- Create: `public/books/sciences-et-technologie-jeux-videos/03-partie-c.html`
- Create: `public/books/sciences-et-technologie-jeux-videos/04-partie-d.html`

**Interfaces:**
- Consumes: le sommaire d'origine reconstitué ci-dessous, le manifeste PDF de la Task 9.
- Produces: quatre chapitres avec résumé, sommaire, téléchargement et note de source.

- [ ] **Step 1: Construire les sommaires d'origine**

Partie A (A, B, C) :
- A. Introduction, page 4
- B. Le cours de la technologie dans l'histoire des jeux vidéos, page 5
- B.2 Le marché des jeux vidéos : une valeur devenue sûre, page 6
- B.3 La continuité de l'évolution des technologies, page 9
- B.4 La réalité virtuelle, page 10
- B.5 La réalisation de jeux vidéos, page 15
- C. Interfaces manuelles motrices, page 15
- C.1 Clavier, page 16
- C.2 Écran tactile, crayon et pistolet optique, page 16
- C.3 Joystick, game pad, joypad, volant et pédaliers, page 17
- C.4 Souris 2D/3D et trackball avec ou sans fil, page 18

Partie B (D) :
- D. Interfaces sensori-motrices, page 22
- D.1 Gant de données et exosquelettes partiels, page 22
- D.2 Combinaisons de données, exosquelette et motion capture, page 29
- D.3 Manette, souris et trackball avec retour de force et retour tactile, page 34
- D.4 Interfaces physiologiques, page 35
- D.5 Autres interfaces sensori-motrices spécifiques, page 36

Partie C (E) :
- E. Interfaces de visualisation, page 37
- E.1 Techniques de visualisation, page 37
- E.1.1 Généralités, page 37
- E.1.2 La vision en relief, page 37
- E.1.3 Les techniques de visualisation et création de supports vidéos pour la vision en relief, page 38
- E.2 Technologies d'afficheurs, page 40
- E.2.1 CRT : afficheurs à tube cathodique, page 40
- E.2.2 LCD : afficheurs à cristaux liquides, page 44
- E.2.3 PDP : afficheur à plasma, page 57
- E.2.4 PALC : écrans plasmatron, page 59
- E.2.5 Les vidéoprojecteurs, page 59
- E.2.6 Autres technologies, page 62
- E.3 Systèmes de visualisation, page 63
- E.3.1 Écran monoscopique, page 63
- E.3.2 Écran d'ordinateur stéréoscopique, page 63
- E.3.2.1 Les écrans auto-stéréoscopiques, page 64
- E.3.2.2 Visiocasques, page 65
- E.3.2.3 Les écrans stéréoscopiques combinés à des vidéolunettes, page 67
- E.3.3 Fenêtres et bureau immersifs, visio-salles et visio-cubes, page 69
- E.3.4 Affichage rétinien, page 73

Partie D (F à J) :
- F. Capteurs de localisation, page 74
- F.1 Principes de positionnement, page 75
- F.2 Capteurs de position et d'orientation, page 75
- F.3 Capteurs de position relative ou de mouvement, page 76
- F.4 Capteurs de position absolue, page 77
- F.5 Capteurs d'orientation, page 79
- F.6 Autres capteurs, page 80
- G. Autres systèmes, page 81
- G.1 Scanners, page 81
- G.2 Appareils photo et caméras numériques, page 83
- H. Conclusion, page 103
- I. Glossaire, page 105
- J. Bibliographie, page 106

Marquer d'un `title="Pagination incertaine dans l'original"` les entrées dont le numéro est ambigu (F.2 à F.6, G.2) et ne pas inventer de sous-section absente du document.

- [ ] **Step 2: Écrire les quatre chapitres**

Structure commune :

```html
<div class="chapter-content">
  <h1 class="chapter-main-title"><strong>Partie A. Introduction, histoire et interfaces manuelles</strong></h1>
  <p class="chapter-context">Étude technique bibliographique · 2001-2002</p>
  <div class="chapter-summary">
    <p class="chapter-paragraph">...</p>
  </div>
  <div class="chapter-original-toc">
    <h3>Sommaire d'origine</h3>
    <ol>
      <li>A. Introduction <span class="toc-page">p. 4</span></li>
      ...
    </ol>
  </div>
  <div class="chapter-download">
    <a class="chapter-download-link" href="/books_reader/public/books/sciences-et-technologie-jeux-videos/pdf/partie-a-introduction-histoire-interfaces-manuelles.pdf" download>Télécharger la partie A en PDF</a>
    <p class="chapter-download-meta">21 pages · 913 Ko · mise en page d'origine</p>
    <p class="chapter-download-note">Le PDF reproduit le document Word de 2001-2002, images et schémas compris.</p>
  </div>
  <p class="chapter-source-note">Texte original de 2001-2002, non réécrit. Le résumé et le sommaire de cette page ont été écrits en 2026. Le PDF reproduit la mise en page du document Word d'origine.</p>
</div>
```

Les métadonnées de téléchargement (pages, poids) doivent reprendre le manifeste réel de la Task 9, pas les valeurs d'exemple.

Résumés : 250 à 450 mots par partie, en 2 ou 3 paragraphes. Chaque résumé dit ce que la partie couvre, ce qu'elle apporte encore et ce qui a vieilli. Aucun ajout technique non présent dans l'étude.

- [ ] **Step 3: Vérifier**

Run: `python -c "import glob,re; [print(p, 'chapter-download' in open(p,encoding='utf-8').read(), 'chapter-original-toc' in open(p,encoding='utf-8').read()) for p in sorted(glob.glob('public/books/sciences-et-technologie-jeux-videos/0[1-4]-partie-*.html'))]"`
Expected: quatre lignes, `True True`.

---

## Task 13: Catalogue, précache et fiche du livre Sciences

**Files:**
- Modify: `public/books.json`
- Modify: `sw.js` si la liste de précache est statique
- Create: `livres/sciences-et-technologie-jeux-videos/index.html` (généré)

- [ ] **Step 1: Ajouter l'entrée**

Même forme que la Task 8, avec :

```json
{
  "id": "sciences-et-technologie-jeux-videos",
  "title": "Sciences et technologie",
  "subtitle": "Analyse des solutions techniques mises en œuvre dans les jeux vidéos · Étude 2001-2002",
  "author": "Hylst (Geoffroy Streit)",
  "year": 2026,
  "authorship": "human",
  "aiAssisted": false,
  "badge": "Archives",
  "coverPath": "covers/sciences-et-technologie-jeux-videos.webp",
  "introPath": "books/sciences-et-technologie-jeux-videos/intro.html",
  "design": {
    "fonts": {
      "heading": "Outfit",
      "body": "Merriweather",
      "googleFonts": ""
    },
    "colors": {
      "background": "#edf1f3",
      "text": "#1a2830",
      "primary": "#1f4b63",
      "secondary": "#dfe8ec",
      "accent": "#b5732b"
    },
    "variables": {
      "--book-bg": "#edf1f3",
      "--book-text": "#1a2830",
      "--book-accent": "#b5732b",
      "--book-accent-dark": "#1f4b63",
      "--book-surface": "#dfe8ec",
      "--book-border": "rgba(31, 75, 99, 0.18)",
      "--book-font-body": "'Merriweather', Georgia, serif",
      "--book-font-heading": "'Outfit', system-ui, sans-serif",
      "--book-font-title": "'Outfit', system-ui, sans-serif",
      "--book-font-size": "1.02rem",
      "--book-line-height": "1.8",
      "--book-max-width": "720px",
      "--book-dropcap-size": "4.2em"
    }
  },
  "chapters": [
    { "id": "00-preface.html", "title": "Préface 2026", "path": "books/sciences-et-technologie-jeux-videos/00-preface.html", "available": true },
    { "id": "01-partie-a.html", "title": "Partie A. Introduction, histoire et interfaces manuelles", "path": "books/sciences-et-technologie-jeux-videos/01-partie-a.html", "available": true },
    { "id": "02-partie-b.html", "title": "Partie B. Interfaces sensori-motrices", "path": "books/sciences-et-technologie-jeux-videos/02-partie-b.html", "available": true },
    { "id": "03-partie-c.html", "title": "Partie C. Interfaces de visualisation", "path": "books/sciences-et-technologie-jeux-videos/03-partie-c.html", "available": true },
    { "id": "04-partie-d.html", "title": "Partie D. Capteurs, autres systèmes et conclusion", "path": "books/sciences-et-technologie-jeux-videos/04-partie-d.html", "available": true }
  ]
}
```

- [ ] **Step 2: Générer la fiche et vérifier**

Run: `python scripts/build_book_pages.py`
Expected: deux nouvelles fiches.

Run: `python -c "import json; d=json.load(open('public/books.json',encoding='utf-8')); print(len(d)); print([b['id'] for b in d])"`
Expected: `9` et les deux nouveaux identifiants en fin de liste.

---

## Task 14: Vérifications locales et rendu

**Files:**
- Test: commandes de contrôle, aucun fichier nouveau sauf les sorties temporaires.

- [ ] **Step 1: Contrôles statiques**

Run: `python scripts/check_dashes.py --root . --all`
Expected: `[OK] Aucun tiret cadratin ou demi-cadratin`.

Run: `node scripts/build_jsx.js`
Expected: compilation sans erreur.

Run: `node scripts/build_jsx.js --check`
Expected: sortie à jour, code 0.

Run: `python -c "import json; json.load(open('public/books.json',encoding='utf-8')); print('ok')"`
Expected: `ok`.

- [ ] **Step 2: Vérifier le précache**

Run: `python -c "s=open('sw.js',encoding='utf-8').read(); import json; d=json.load(open('public/books.json',encoding='utf-8')); ids=[b['id'] for b in d if b['id'].startswith(('recueils-proses-poesies-t4','sciences-et'))]; print(ids); print(all(('books/'+i.split('/')[-1]) in s or i in s for i in ids))"`
Expected: les deux identifiants et `True` si la liste est statique. Si `precacheBooks` lit le catalogue dynamiquement, vérifier à la place que `v67` est présent.

- [ ] **Step 3: Synchroniser**

Run: `powershell -ExecutionPolicy Bypass -File scripts/sync-to-platform.ps1`
Expected: synchronisation terminée, aucune erreur, sitemap à 12 URL.

- [ ] **Step 4: Servir le miroir et contrôler**

Démarrer le serveur local sur `D:\0CODE\AntiGravity\Cours_Memos\Docker` (port 8765) s'il ne tourne pas. Vérifier :

- `http://127.0.0.1:8765/books_reader/` charge la bibliothèque avec neuf livres ;
- les deux nouvelles pages livre s'ouvrent, les sommaires sont complets ;
- les chapitres s'affichent, les dates et notes de source sont visibles ;
- les quatre liens PDF répondent en 200 et téléchargent un fichier non vide ;
- les deux couvertures s'affichent.

- [ ] **Step 5: Vérifier les PDF dans le navigateur**

Ouvrir chaque PDF via l'URL locale, vérifier la première page et une page contenant une image. Noter le nombre de pages affiché et le comparer au manifeste.

---

## Task 15: Documentation et état de reprise

**Files:**
- Modify: `CHANGELOG.md`
- Modify: `todo.md`
- Modify: `antigravity.md`
- Modify: `continue.md`

- [ ] **Step 1: CHANGELOG**

Ajouter une section `## [1.8.11] - 2026-11-07` avec : Tome IV (quatre textes, dates, réécriture légère, notes de source), livre Sciences (préface 2026, quatre parties, quatre PDF, sommaire d'origine), deux couvertures, cache v67, dix fiches statiques.

- [ ] **Step 2: todo.md**

Déplacer les éléments terminés dans « Terminé (Récemment) », garder en tête la mise à jour des intitulés des tomes I à III et le lot des Escapades.

- [ ] **Step 3: antigravity.md**

Mettre à jour le nombre de livres (9), de chapitres, de fiches statiques et la version du cache (v67). Ajouter une note sur la rubrique Sciences et technologie et sur le format hybride HTML + PDF.

- [ ] **Step 4: continue.md**

Réécrire l'état de reprise : ce qui est fait, ce qui reste (Escapades B2 à E, deux poèmes, `Wizard's lair`, déploiement Nightprowler 1.8.10, vérification de production).

- [ ] **Step 5: Contrôle final**

Run: `python scripts/check_dashes.py --root . --all`
Expected: `[OK]`.

Run: `git status --short`
Expected: uniquement les fichiers attendus, aucun fichier source supprimé.

---

## Task 16: Déploiement et vérification de production

**Files:** aucun fichier source.

- [ ] **Step 1: Déployer**

Suivre la procédure Coolify du projet pour le service `books_reader`, en publiant le miroir synchronisé.

- [ ] **Step 2: Vérifier Nightprowler 1.8.10 et la nouvelle version**

Run: `bash verifier-prod.sh --full books_reader` (depuis le dossier de la plateforme).
Expected: toutes les vérifications passent, version et build attendus, pages et PDF accessibles.

- [ ] **Step 3: Consigner**

Noter dans `continue.md` et `CHANGELOG.md` la date de déploiement, la version et le build de production.

---

## Self-review

- Couverture de la spec : sections 5.1 à 5.6 couvertes par les Tasks 3 à 8 ; sections 6.1 à 6.7 par les Tasks 9 à 13 ; design et couvertures par les Tasks 1 et 2 ; vérifications par les Tasks 14 et 15 ; déploiement par la Task 16.
- Aucune étape ne laisse de choix structurel ouvert : chemins, identifiants, classes et valeurs sont fixés.
- Les noms de classes sont cohérents entre le CSS (Task 1), les chapitres (Tasks 4 à 7 et 12) et les vérifications.
- Les cinq risques du Review Focus ont chacun un contrôle : scories (Tasks 4 à 7), pagination incertaine (Task 12), PDF (Tasks 9 et 14), liens absolus (Task 12), précache (Task 14).
