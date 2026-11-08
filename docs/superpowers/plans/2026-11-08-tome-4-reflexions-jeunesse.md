# Enrichissement du Tome IV par les réflexions de jeunesse (1994-1998) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Intégrer trois nouveaux chapitres thématiques issus des écrits de jeunesse de l'auteur (1994-1998) en tête de *Carnets, réflexions & partages · Tome IV*, portant le recueil de 4 à 7 textes et étendant sa couverture chronologique à trente ans de pensée (1994-2024).

**Architecture:** Décalage ordonné par `git mv` des 4 chapitres existants (01-04 vers 04-07), rédaction soignée des trois nouveaux chapitres HTML (`01-de-l-art-et-de-la-demoscene.html`, `02-de-l-edenisme-et-de-la-quete-d-equilibre.html`, `03-eloge-du-temps-libre-et-de-l-eveil.html`) en respectant la charte éditoriale du Tome IV, mise à jour du catalogue `public/books.json` et de l'introduction `intro.html`, puis regénération de la fiche statique et validation globale.

**Tech Stack:** HTML5 sémantique, JSON (`books.json`), Python 3 (`build_book_pages.py`, `check_dashes.py`), JavaScript / Service Worker (`sw.js`, `test-sw-policy.js`).

**Spec:** `docs/superpowers/specs/2026-11-08-tome-4-reflexions-jeunesse-design.md`

## Global Constraints

- Zéro tiret cadratin (`\u2014`) ou demi-cadratin (`\u2013`) dans les fichiers servis (`python scripts/check_dashes.py --root .`).
- Aucun script inline, aucun CDN au runtime (CSP `script-src 'self'`).
- Respect strict de la voix de l'auteur, de sa franchise, de ses maximes (« l'oiseau dans la main ») et de ses métaphores (le disque dur sain), tout en nettoyant les abréviations de prise de notes Web 1.0 (`qques`, `C`, `+`, `-`, `svt`, `G`).
- Précache Service Worker à jour (`sw.js`) avec versionnement explicite.
- Conformité responsive 390 px sans débordement horizontal.

## Review Focus

1. **Fidélité au ton et aux prises de position de l'auteur** : le coup de gueule sur la demoscene (rip de code, contrefaçon graphique scannée vs pixel art original), la théorie des plaisirs et de l'équilibre sciences/médiéval, et le plaidoyer pour les jeux de plateau doivent conserver leur énergie intacte.
2. **Ordre et cohérence des 7 chapitres du Tome IV** : la table des matières de `books.json` et les 7 fichiers HTML doivent avoir des identifiants, titres et chemins parfaitement alignés de 01 à 07.
3. **Nettoyage rigoureux des scories de navigation** : disparition totale des résidus de page web personnelle (`Retour home page`, `en construction`) au profit d'une structure fluide en sections `<h2>`.
4. **Validité syntaxique HTML** : toutes les balises `<p>`, `<h2>`, `<ul>`, `<li>` doivent être rigoureusement équilibrées sans balise orpheline.
5. **Régénération de la fiche statique** : `livres/recueils-proses-poesies-t4-carnets-reflexions-partages/index.html` doit être à jour avec les 7 chapitres listés.

---

### Task 1: Décalage ordonné des chapitres existants du Tome IV (01-04 vers 04-07)

**Files:**
- Modify/Rename:
  - `public/books/recueils-proses-poesies-t4-carnets-reflexions-partages/04-marre-d-apprendre.html` → `07-marre-d-apprendre.html`
  - `public/books/recueils-proses-poesies-t4-carnets-reflexions-partages/03-idees-cadeaux.html` → `06-idees-cadeaux.html`
  - `public/books/recueils-proses-poesies-t4-carnets-reflexions-partages/02-imaginez-vous.html` → `05-imaginez-vous.html`
  - `public/books/recueils-proses-poesies-t4-carnets-reflexions-partages/01-hygiene-de-vie.html` → `04-hygiene-de-vie.html`

**Interfaces:**
- Consumes: Fichiers de chapitres existants dans `public/books/recueils-proses-poesies-t4-carnets-reflexions-partages/`
- Produces: Fichiers renommés laissant les slots 01, 02 et 03 libres pour Task 2

- [ ] **Step 1: Renommer les fichiers de 04 à 01 dans l'ordre décroissant par commande git mv**

```bash
cd "D:/Users/Geoffroy/orca/workspaces/Hylst_Reader/v1.8.24/public/books/recueils-proses-poesies-t4-carnets-reflexions-partages"
git mv 04-marre-d-apprendre.html 07-marre-d-apprendre.html
git mv 03-idees-cadeaux.html 06-idees-cadeaux.html
git mv 02-imaginez-vous.html 05-imaginez-vous.html
git mv 01-hygiene-de-vie.html 04-hygiene-de-vie.html
```

- [ ] **Step 2: Vérifier que les 4 fichiers renommés existent et que les slots 01, 02 et 03 sont libres**

Run: `ls -1 public/books/recueils-proses-poesies-t4-carnets-reflexions-partages/*.html`
Expected: Fichiers 04 à 07 présents, aucun fichier 01, 02 ou 03.

---

### Task 2: Rédaction et création des 3 nouveaux chapitres de jeunesse (01 à 03)

**Files:**
- Create: `public/books/recueils-proses-poesies-t4-carnets-reflexions-partages/01-de-l-art-et-de-la-demoscene.html`
- Create: `public/books/recueils-proses-poesies-t4-carnets-reflexions-partages/02-de-l-edenisme-et-de-la-quete-d-equilibre.html`
- Create: `public/books/recueils-proses-poesies-t4-carnets-reflexions-partages/03-eloge-du-temps-libre-et-de-l-eveil.html`

**Interfaces:**
- Consumes: Manuscrits de jeunesse de Geoffroy Streit (1994-1998)
- Produces: Trois nouveaux chapitres HTML balisés et prêts pour la liseuse

- [ ] **Step 1: Rédiger `01-de-l-art-et-de-la-demoscene.html`**
  - Titre : *De l'art et de la demoscene informatique*
  - Date : `Texte écrit vers 1996`
  - Sections : L'essence de l'art (artifice, inutilité matérielle, noblesse de l'effort), L'esprit de la demoscene (Oric, C64, Atari ST, Amiga, création pour le spectacle), Tribune critique sans complaisance (les programmeurs et le rip de routines, les graphistes et la dénonciation des scans/copies face au pixel art d'auteur, les musiciens et le pillage de samples). Note de source en fin de texte.

- [ ] **Step 2: Rédiger `02-de-l-edenisme-et-de-la-quete-d-equilibre.html`**
  - Titre : *De l'édenisme et de la quête d'équilibre*
  - Date : `Texte écrit vers 1996-1998`
  - Sections : L'édenisme comme finalité (éprouver le plaisir et le partager), La graduation des plaisirs (plaisirs simples, besoins naturels et mise en garde contre l'orgueil, la paresse et l'avarice, plaisirs nobles de la passion et de l'effort qui paie), Le lien à autrui et la complicité, La recherche d'équilibre personnel (sciences de laboratoire en optique, électronique et informatique compensées par l'imaginaire médiéval du jeu de rôle, du dessin et de la musique), Maximes de vie (Carpe Diem, ne pas remettre au lendemain, la parabole de l'oiseau au creux de la main). Note de source.

- [ ] **Step 3: Rédiger `03-eloge-du-temps-libre-et-de-l-eveil.html`**
  - Titre : *Éloge du temps libre et de l'éveil*
  - Date : `Texte écrit vers 1998`
  - Sections : L'éveil sensoriel du jeune enfant (les cinq sens, la métaphore du cerveau comme disque dur défragmenté à la naissance qui accumule sans conflits psychologiques initiaux, le rôle de guide des parents), Manifeste pour les loisirs actifs contre le métro-boulot-dodo (jeux de société versus jeux de plateaux avec figurines, Warhammer 40000, Space Hulk, Dune, Carcassonne, création du jeu *Les Royaumes d'Yttria*, jeux de cartes Magic et Vampire, jeux de rôle, sports et clubs associatifs). Note de source.

- [ ] **Step 4: Vérifier l'équilibre des balises HTML et l'absence de tirets longs sur les 3 fichiers**

Run: `python scripts/check_dashes.py --root .`
Expected: [OK] Aucun tiret cadratin ou demi-cadratin.

---

### Task 3: Mise à jour de `books.json` et de `intro.html` de Tome IV

**Files:**
- Modify: `public/books.json`
- Modify: `public/books/recueils-proses-poesies-t4-carnets-reflexions-partages/intro.html`

**Interfaces:**
- Consumes: Fichiers de chapitres 01 à 07
- Produces: Métadonnées de bibliothèque à jour

- [ ] **Step 1: Mettre à jour `public/books/recueils-proses-poesies-t4-carnets-reflexions-partages/intro.html`**
  - Présenter les 7 textes couvrant trente ans (1994-2024), en explicitant les racines de jeunesse (l'art et la demoscene des années 90, l'édenisme et l'équilibre sciences/médiéval, l'éloge du jeu et du temps libre) qui ouvrent le volume.

- [ ] **Step 2: Mettre à jour l'entrée de Tome IV dans `public/books.json`**
  - Déclarer les 7 chapitres ordonnés de 01 à 07 avec leurs identifiants, titres, chemins et dates d'origine.
  - Vérifier la validité JSON avec `python -m json.tool public/books.json > /dev/null`.

---

### Task 4: Regénération de la fiche statique et mise à jour du Service Worker

**Files:**
- Modify: `sw.js`
- Generate: `livres/recueils-proses-poesies-t4-carnets-reflexions-partages/index.html`

**Interfaces:**
- Consumes: `public/books.json`, `scripts/build_book_pages.py`
- Produces: Fiche statique de Tome IV à jour et cache Service Worker incrémenté

- [ ] **Step 1: Regénérer les fiches de livres statiques**

```bash
python scripts/build_book_pages.py
```
Expected: `livres/recueils-proses-poesies-t4-carnets-reflexions-partages/index.html` mis à jour avec les 7 chapitres.

- [ ] **Step 2: Incrémenter le cache Service Worker dans `sw.js`**
  - Passer `CACHE_NAME` de `'hylst-reader-v85'` à `'hylst-reader-v86'` (v1.8.30).

- [ ] **Step 3: Exécuter la suite de tests Service Worker et JSX**

```bash
node scripts/build_jsx.js --check && node scripts/test-sw-policy.js
```
Expected: [OK] 10 fichier(s) compilé(s) à jour. Tous les tests passent.

---

### Task 5: Contrôle qualité, rendu visuel desktop/mobile 390 px et validation

**Files:**
- Test: Script Python de vérification DOM, tirets longs et cohérence des 7 chapitres
- Visual: Captures Chrome headless 1440 px et 390 px sur les nouveaux chapitres
- Documentation: `CHANGELOG.md`, `todo.md`, `antigravity.md`

- [ ] **Step 1: Vérifier le DOM et la typographie sur les 7 chapitres du Tome IV**
  - Contrôle automatique HTMLParser et détection de tirets longs.

- [ ] **Step 2: Générer des aperçus Chrome headless et inspecter en mobile 390 px**
  - Vérifier la lisibilité des sections `<h2>`, la fluidité des listes de jeux et l'absence de débordement horizontal.

- [ ] **Step 3: Mettre à jour `CHANGELOG.md`, `todo.md` et `antigravity.md` pour v1.8.30**
