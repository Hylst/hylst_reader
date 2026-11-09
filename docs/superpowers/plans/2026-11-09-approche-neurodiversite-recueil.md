# Approche de la Neurodiversité — Recueil Thématique — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Consolider et enrichir *Approche de la Neurodiversité* en un recueil thématique majeur en 3 parties (13 entrées : Prologue, 11 chapitres et Épilogue) unifiant les trois textes d'archives de l'auteur (2018-2022), avec 3 schémas vectoriels SVG interactifs et 4 illustrations locales générées par GPU (Krea-2-Turbo).

**Architecture:** Fusion éditoriale rigoureuse de `troubles dys.odt`, `Enfants en difficulté scolaire.doc`, et `Idées pour lutter contre les troubles...pdf` (2022), création de 3 infographies SVG haute précision responsives, génération locale des 4 illustrations de têtes de parties, mise à jour du catalogue `public/books.json` (sommaire à 13 entrées, période 2018-2022), Service Worker v92, fiche statique et déploiement miroir.

**Tech Stack:** HTML5 sémantique, SVG vectoriel responsive, React (liseuse Hylst_Reader), Python 3 (générateurs, PIL, PyMuPDF), Krea-2-Turbo (`wainsfw` local sdcpp sur GPU RTX 5070), Service Worker PWA Vanilla JS.

**Spec:** `docs/superpowers/specs/2026-11-09-approche-neurodiversite-recueil-design.md`

## Global Constraints

- **Zéro tiret long** : Aucun tiret cadratin (`—`, `\u2014`) ou demi-cadratin (`–`, `\u2013`) dans les fichiers HTML, JSON ou JS servis. `python scripts/check_dashes.py --root .` doit retourner 0 erreur.
- **Zéro CDN au runtime** : Aucune dépendance externe, police ou image en ligne. Tous les assets résident dans `public/`.
- **Politique Service Worker** : Précache isolé préfixé `hylst-reader-`, exclusion stricte des flux audio lourds du précache.
- **CSP stricte** : `default-src 'self'`. Aucun script inline.
- **Filiation éthique** : Métadonnées claires (`writingPeriod: "2018-2022"`, `authorship: "human"`, mention explicite des illustrations Krea et schémas SVG).

## Review Focus

1. **Fidélité au propos et à la voix d'auteur** : Aucune dérive « super-pouvoir » New Age ou condescendance médicale ; maintien du ton franc, direct, lucide et bienveillant de Geoffroy Streit.
2. **Précision des 3 schémas SVG** : Chaque schéma SVG doit être parfaitement lisible sur mobile (reflow/viewBox responsive) et en mode sombre comme en mode clair.
3. **Absence de tirets cadratins dans les 13 fichiers de chapitres** : Validation regex et `check_dashes.py` rigoureuse.
4. **Cohérence du sommaire de 13 chapitres** : Chaînage sans saut de `00-prologue.html` jusqu'à `epilogue.html` dans `public/books.json` et dans la navigation liseuse.
5. **Génération locale d'images propre** : Vérification des dimensions, poids WebP (< 500 Ko) et absence totale de texte en anglais incrusté sur les 4 illustrations Krea.

---

### Task 1: Création des 3 schémas vectoriels SVG haute précision

**Files:**
- Create: `public/books/approche-de-la-neurodiversite/images/neuro-schema-1-familles.svg`
- Create: `public/books/approche-de-la-neurodiversite/images/neuro-schema-2-pedagogie.svg`
- Create: `public/books/approche-de-la-neurodiversite/images/neuro-schema-3-bequilles.svg`
- Test: `python scripts/test_neuro_svg.py`

**Interfaces:**
- Produces: 3 fichiers SVG vectoriels sémantiques avec styles CSS adaptatifs (mode sombre/clair) décrivant les 5 familles dys, la boucle d'accompagnement scolaire, et les 13 béquilles.

- [ ] **Step 1: Écrire le test unitaire pour valider les 3 schémas SVG**

Créer `scripts/test_neuro_svg.py` :
```python
from pathlib import Path
import xml.etree.ElementTree as ET

def test_neuro_svgs():
    img_dir = Path("public/books/approche-de-la-neurodiversite/images")
    assert img_dir.exists(), "Le dossier images n'existe pas"
    for name in ["neuro-schema-1-familles.svg", "neuro-schema-2-pedagogie.svg", "neuro-schema-3-bequilles.svg"]:
        p = img_dir / name
        assert p.exists(), f"Fichier manquant: {p}"
        tree = ET.parse(p)
        root = tree.getroot()
        assert "viewBox" in root.attrib, f"Pas de viewBox dans {name}"
        assert len(root.findall(".//{http://www.w3.org/2000/svg}text")) > 5, f"Texte insuffisant dans {name}"
    print("ALL 3 NEURO SVG SCHEMAS OK")

if __name__ == "__main__":
    test_neuro_svgs()
```

- [ ] **Step 2: Vérifier que le test échoue avant création**

Run: `python scripts/test_neuro_svg.py`
Expected: FAIL avec "Le dossier images n'existe pas" ou "Fichier manquant"

- [ ] **Step 3: Créer les 3 schémas SVG avec design sobre et adaptatif**

Concevoir et générer les trois schémas :
1. `neuro-schema-1-familles.svg` : Les 5 familles (Langage écrit, Langage oral, Psychomoteur/Espace, Attention/Exécution, Mémoire, Calcul) avec zones cérébrales et impacts quotidiens.
2. `neuro-schema-2-pedagogie.svg` : Le cercle vicieux de l'échec scolaire vs la boucle vertueuse de l'écoute, dédramatisation, pas-à-pas et confiance.
3. `neuro-schema-3-bequilles.svg` : Les 13 béquilles cognitives réparties en 4 piliers (Corps & Espace, Délestage mental, Hygiène de vie, Gestion de l'esprit embrumé).

- [ ] **Step 4: Valider le test des schémas SVG**

Run: `python scripts/test_neuro_svg.py`
Expected: `ALL 3 NEURO SVG SCHEMAS OK`

- [ ] **Step 5: Commit**

```bash
git add public/books/approche-de-la-neurodiversite/images/ scripts/test_neuro_svg.py
git commit -m "feat(neuro): creation des 3 schemas vectoriels SVG haute precision"
```

---

### Task 2: Génération locale des 4 illustrations d'art éditorial (Krea-2-Turbo)

**Files:**
- Create: `public/books/approche-de-la-neurodiversite/images/partie-1-couverture.webp`
- Create: `public/books/approche-de-la-neurodiversite/images/partie-2-couverture.webp`
- Create: `public/books/approche-de-la-neurodiversite/images/partie-3-couverture.webp`
- Create: `public/books/approche-de-la-neurodiversite/images/epilogue-couverture.webp`
- Test: `python scripts/test_neuro_art.py`

**Interfaces:**
- Consumes: Moteur local `wainsfw` (`krea-2-turbo-sdcpp` sur GPU RTX 5070)
- Produces: 4 illustrations WebP (480x280 px, format vignette, art éditorial encre et or, zéro texte).

- [ ] **Step 1: Écrire le test pour valider les 4 illustrations**

Créer `scripts/test_neuro_art.py` :
```python
from pathlib import Path
from PIL import Image

def test_neuro_art():
    img_dir = Path("public/books/approche-de-la-neurodiversite/images")
    for name in ["partie-1-couverture.webp", "partie-2-couverture.webp", "partie-3-couverture.webp", "epilogue-couverture.webp"]:
        p = img_dir / name
        assert p.exists(), f"Image manquante: {p}"
        im = Image.open(p)
        assert im.format == "WEBP", f"Format non webp: {im.format}"
        assert p.stat().st_size > 5000 and p.stat().st_size < 500000, "Taille anormale"
    print("ALL 4 NEURO ART ASSETS OK")

if __name__ == "__main__":
    test_neuro_art()
```

- [ ] **Step 2: Vérifier que le test échoue avant génération**

Run: `python scripts/test_neuro_art.py`
Expected: FAIL avec "Image manquante"

- [ ] **Step 3: Générer les 4 illustrations avec Krea-2-Turbo et les optimiser**

Exécuter un script Python pilotant `D:/0CODE/ClaudeCode/wainsfw/main.py` avec le modèle `krea-2-turbo-sdcpp` (ou repli Z-Image Turbo local si serveur sdcpp occupé) :
- Partie 1 : *L'Archipel des Pensées* (îles cérébrales, ponts de corde, encre fine et lavis ardoise/or).
- Partie 2 : *La Main sur l'Épaule* (silhouette bienveillante guidant un enfant vers un cahier ouvert).
- Partie 3 : *La Boîte à Outils* (engrenages de bois délicats, boussole et carnet de notes).
- Épilogue : *La Silhouette et le Phare* (marcheur solitaire avançant sur un sentier dans la brume).
Recadrer et redimensionner en WebP 480x280 px sans aucun texte.

- [ ] **Step 4: Valider le test d'art**

Run: `python scripts/test_neuro_art.py`
Expected: `ALL 4 NEURO ART ASSETS OK`

- [ ] **Step 5: Commit**

```bash
git add public/books/approche-de-la-neurodiversite/images/ scripts/test_neuro_art.py
git commit -m "feat(neuro): generation locale des 4 illustrations Krea-2-Turbo"
```

---

### Task 3: Rédaction de la Partie I (Prologue + Chapitres 1 à 4 — Anatomie des décalages)

**Files:**
- Create: `public/books/approche-de-la-neurodiversite/00-prologue.html`
- Create/Modify: `public/books/approche-de-la-neurodiversite/chapitre-01.html` à `chapitre-04.html`
- Modify: `public/books/approche-de-la-neurodiversite/intro.html`
- Test: `python scripts/check_dashes.py --root public/books/approche-de-la-neurodiversite`

**Interfaces:**
- Consumes: `troubles dys.odt` et le texte existant des chapitres 1 à 4.
- Produces: 5 fichiers HTML complets avec le schéma SVG 1 et l'illustration Partie 1.

- [ ] **Step 1: Rédiger `00-prologue.html` et mettre à jour `intro.html`**

- `intro.html` : présentation du recueil en 3 parties, genèse 2018-2022, note éthique d'auteur.
- `00-prologue.html` : Le décalage invisible, genèse de la démarche, le refus de la démagogie des « super-pouvoirs ».

- [ ] **Step 2: Rédiger Chapitres 1 et 2 (L'école et les 5 familles dys)**

- Chapitre 1 : *L'école, premier tribunal et blessure originelle* (illustration `partie-1-couverture.webp`).
- Chapitre 2 : *Les cinq familles de troubles : langage, geste et calcul* (intégration du `neuro-schema-1-familles.svg` avec tableau accessible de synthèse).

- [ ] **Step 3: Rédiger Chapitres 3 et 4 (Attention, mémoire et usure adulte)**

- Chapitre 3 : *L'attention en miettes et la mémoire qui fuit* (TDA/H, mémoire immédiate saturée, malentendus).
- Chapitre 4 : *L'usure adulte et le malentendu permanent* (le coût énergétique persistant, la peur de l'incompétence, la solitude).

- [ ] **Step 4: Contrôler l'absence de tirets cadratins**

Run: `python scripts/check_dashes.py --root public/books/approche-de-la-neurodiversite`
Expected: `[OK] Aucun tiret cadratin ou demi-cadratin`

- [ ] **Step 5: Commit**

```bash
git add public/books/approche-de-la-neurodiversite/
git commit -m "feat(neuro): redaction Partie I (Prologue et chapitres 1 a 4) avec schema 1"
```

---

### Task 4: Rédaction de la Partie II (Chapitres 5 à 7 — L'Enfance et l'École)

**Files:**
- Create: `public/books/approche-de-la-neurodiversite/chapitre-05.html` à `chapitre-07.html`
- Test: `python scripts/check_dashes.py --root public/books/approche-de-la-neurodiversite`

**Interfaces:**
- Consumes: `Enfants en difficulté scolaire.doc`.
- Produces: 3 fichiers HTML complets avec le schéma SVG 2 et l'illustration Partie 2.

- [ ] **Step 1: Rédiger Chapitre 5 : *Décrypter le malaise scolaire sans condamner***

Illustration `partie-2-couverture.webp`. Diagnostic des vraies causes : ambiance de classe, humiliations ordinaires, fatigue, complexes, agressivité comme masque de la détresse.

- [ ] **Step 2: Rédiger Chapitre 6 : *Dédramatiser, écouter et restaurer la confiance***

La posture d'adulte : sortir de la tyrannie de la note, écoute d'égal à égal, réhabiliter la valeur personnelle de l'enfant.

- [ ] **Step 3: Rédiger Chapitre 7 : *Pédagogie de terrain : la méthode du pas-à-pas***

Intégration du schéma SVG 2 (`neuro-schema-2-pedagogie.svg`) avec descriptif. La segmentation des efforts, petites victoires, récréations indispensables, ancrage dans le concret.

- [ ] **Step 4: Contrôler l'absence de tirets cadratins**

Run: `python scripts/check_dashes.py --root public/books/approche-de-la-neurodiversite`
Expected: `[OK] Aucun tiret cadratin ou demi-cadratin`

- [ ] **Step 5: Commit**

```bash
git add public/books/approche-de-la-neurodiversite/
git commit -m "feat(neuro): redaction Partie II (chapitres 5 a 7) avec schema 2"
```

---

### Task 5: Rédaction de la Partie III et Épilogue (Chapitres 8 à 11 + Épilogue — La Boîte à Béquilles)

**Files:**
- Create: `public/books/approche-de-la-neurodiversite/chapitre-08.html` à `chapitre-11.html`
- Create: `public/books/approche-de-la-neurodiversite/epilogue.html`
- Test: `python scripts/check_dashes.py --root public/books/approche-de-la-neurodiversite`

**Interfaces:**
- Consumes: `Idées pour lutter contre les troubles ‘dys’...pdf` (2022) et l'épilogue existant.
- Produces: 5 fichiers HTML complets avec le schéma SVG 3 et les illustrations Partie 3 et Épilogue.

- [ ] **Step 1: Rédiger Chapitre 8 : *L'environnement et le corps : poser les fondations***

Illustration `partie-3-couverture.webp`. Axes 1 à 3 : ergonomie du bureau, rituels de centrage/respiration, acceptation du temps long.

- [ ] **Step 2: Rédiger Chapitre 9 : *Le délestage mental : externaliser la mémoire***

Intégration du schéma SVG 3 (`neuro-schema-3-bequilles.svg`). Axes 4 à 7 : segmentation en micro-étapes, listes de délestage, rappels programmés et décharge sur papier.

- [ ] **Step 3: Rédiger Chapitres 10 et 11 (Méthodologie et gestion de l'esprit embrumé)**

- Chapitre 10 : Axes 8 à 10 : structuration visuelle, relecture différée, sommeil et hygiène biologique.
- Chapitre 11 : Axes 11 à 13 : détecter le point de rupture (« l'esprit dans le brouillard »), oser dire stop, bienveillance envers soi.

- [ ] **Step 4: Rédiger `epilogue.html` : *Vivre avec la friction***

Illustration `epilogue-couverture.webp`. Le texte de conclusion lucide, sans résignation : construire des béquilles tenaces et marcher debout.

- [ ] **Step 5: Contrôler l'absence de tirets cadratins**

Run: `python scripts/check_dashes.py --root public/books/approche-de-la-neurodiversite`
Expected: `[OK] Aucun tiret cadratin ou demi-cadratin sur l'ensemble des 14 fichiers HTML`

- [ ] **Step 6: Commit**

```bash
git add public/books/approche-de-la-neurodiversite/
git commit -m "feat(neuro): redaction Partie III (chapitres 8 a 11) et epilogue avec schema 3"
```

---

### Task 6: Intégration catalogue, régénération des 12 fiches statiques et UI

**Files:**
- Modify: `public/books.json`
- Modify: `scripts/build_book_pages.py`
- Test: `python scripts/build_book_pages.py && node scripts/build_jsx.js --check`

**Interfaces:**
- Consumes: Les 13 fichiers de chapitres créés dans `public/books/approche-de-la-neurodiversite/`.
- Produces: Sommaire à 13 entrées dans `public/books.json`, fiche statique `livres/approche-de-la-neurodiversite/index.html`.

- [ ] **Step 1: Mettre à jour l'entrée du livre dans `public/books.json`**

- Mettre à jour `chapters` avec les 13 entrées : `00-prologue.html`, `chapitre-01.html` à `chapitre-11.html`, et `epilogue.html` avec leurs titres exacts.
- Valider le JSON : `python -m json.tool public/books.json > /dev/null`.

- [ ] **Step 2: Régénérer la fiche statique indexable**

Run: `python scripts/build_book_pages.py`
Expected: `12 fiches generees.`

- [ ] **Step 3: Valider le JSX et le contrôle des tirets**

Run: `node scripts/build_jsx.js --check && python scripts/check_dashes.py --root .`
Expected: `[OK] 10 fichier(s) compilé(s) à jour` et `[OK] Aucun tiret cadratin ou demi-cadratin`

- [ ] **Step 4: Commit**

```bash
git add public/books.json livres/approche-de-la-neurodiversite/index.html
git commit -m "feat(neuro): mise a jour catalogue 13 chapitres et fiche statique"
```

---

### Task 7: Mise à jour Service Worker (v92) et validation locale

**Files:**
- Modify: `sw.js`
- Test: `node scripts/test-sw-policy.js`

**Interfaces:**
- Consumes: Tous les fichiers de `public/books/approche-de-la-neurodiversite/` (HTML, SVG, WebP).
- Produces: Cache `hylst-reader-v92` incluant tous les nouveaux contenus.

- [ ] **Step 1: Incrémenter le cache dans `sw.js`**

Passer `CACHE_NAME` à `hylst-reader-v92`.

- [ ] **Step 2: Exécuter les tests de politique Service Worker**

Run: `node scripts/test-sw-policy.js`
Expected: `Tous les tests de politique du Service Worker passent.`

- [ ] **Step 3: Commit**

```bash
git add sw.js
git commit -m "feat(sw): version hylst-reader-v92 pour le recueil Neurodiversite"
```

---

### Task 8: Documentation, synchronisation miroir et déploiement production (v1.8.36)

**Files:**
- Modify: `CHANGELOG.md`
- Modify: `todo.md`
- Modify: `antigravity.md`
- Modify: Dépôt plateforme `D:/0CODE/AntiGravity/Cours_Memos/Docker`
- Test: `powershell -ExecutionPolicy Bypass -File scripts/verify-release.ps1`

- [ ] **Step 1: Mettre à jour `CHANGELOG.md`, `todo.md` et `antigravity.md`**

Consigner la version 1.8.36 : Édition intégrale d'*Approche de la Neurodiversité* en recueil thématique de 3 parties (13 chapitres, 3 schémas SVG, 4 illustrations Krea locales).

- [ ] **Step 2: Commiter et pousser dans le dépôt source**

```bash
git add CHANGELOG.md todo.md antigravity.md
git commit -m "docs: release notes v1.8.36 pour l'edition integrale Neurodiversite"
git push origin Hylst/v1.8.24
```

- [ ] **Step 3: Synchroniser vers le miroir de plateforme**

Run: `powershell -ExecutionPolicy Bypass -File scripts/sync-to-platform.ps1 -Prune`
Expected: Build généré, 0 tiret long, synchronisation réussie.

- [ ] **Step 4: Mettre à jour les documentations de la plateforme Docker**

Mettre à jour `changelog.md`, `todo.md`, `securite.md` et `hylst_IT_platform_content.md`.

- [ ] **Step 5: Commiter et pousser sur `cours_info` `main`**

```bash
cd "D:/0CODE/AntiGravity/Cours_Memos/Docker"
git add books_reader
git commit -m "Books Reader 1.8.36 : edition integrale Approche de la Neurodiversite (13 chapitres, 3 SVG, 4 WebP)"
git add changelog.md todo.md securite.md hylst_IT_platform_content.md
git commit -m "docs : Books Reader 1.8.36 synchronise"
git push origin main
```

- [ ] **Step 6: Vérifier le déploiement en production**

Attendre le déploiement Coolify et exécuter :
Run: `powershell -ExecutionPolicy Bypass -File scripts/verify-release.ps1`
Expected: 100 % vert avec HTTP 200 sur `https://hylst.fr/books_reader/livres/approche-de-la-neurodiversite/`.
