# Le pantin et la poupée de cire Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Intégrer le conte inédit *Le pantin et la poupée de cire* dans *Recueils de proses et poésies fantasques · Tome II (Fantasque & merveilleux)* au chapitre 05 en diptyque avec le chapitre 04, en complétant la scène médiane à partir des notes de l'auteur et en préservant son poème de clôture.

**Architecture:** Décalage ordonné des chapitres 05 à 10 existants vers 06 à 11 dans le dossier `public/books/recueils-proses-poesies-t2-fantasque-merveilleux/`, création du nouveau fichier `05-le-pantin-et-la-poupee-de-cire.html` structuré en trois volets continus (narration originale, scène médiane en vers libres complétée, poème final de 5 strophes), mise à jour du catalogue `public/books.json` et de l'introduction `intro.html`, puis regénération de la fiche statique et validation globale.

**Tech Stack:** HTML5 sémantique, JSON (`books.json`), Python 3 (`build_book_pages.py`, `check_dashes.py`), JavaScript / Service Worker (`sw.js`, `test-sw-policy.js`).

**Spec:** `docs/superpowers/specs/2026-11-08-le-pantin-et-la-poupee-de-cire-design.md`

## Global Constraints

- Zéro tiret cadratin (`\u2014`) ou demi-cadratin (`\u2013`) dans les fichiers servis (`python scripts/check_dashes.py --root .`).
- Aucun script inline, aucun CDN au runtime (CSP `script-src 'self'`).
- Respect strict de la voix de l'auteur, du rythme ternaire, du vocabulaire d'antan et conservation mot à mot des parties rédigées par l'auteur (premier volet et poème final).
- Précache Service Worker à jour (`sw.js`) avec versionnement explicite.
- Conformité responsive 390 px sans débordement horizontal.

## Review Focus

1. **Intégrité textuelle du poème final** : les 5 strophes d'alexandrins et décasyllabes doivent être préservées mot à mot, sans altération de rime ni de ponctuation.
2. **Transition médiane naturelle** : la scène médiane doit intégrer l'ensemble des éléments des notes (pendule de minuit, boîte à musique, jeu d'ombres, danse/marelle, baiser, chaleur et larme de cire fondue) dans le même style versifié libre.
3. **Ordre et cohérence des chapitres de Tome II** : la table des matières de `books.json` et les 11 fichiers HTML doivent avoir des identifiants, titres et chemins parfaitement alignés de 01 à 11.
4. **Validité syntaxique HTML** : toutes les balises `<p>`, `<em>`, `<figure>`, `<hr>` doivent être rigoureusement équilibrées sans balise orpheline.
5. **Régénération de la fiche statique** : `livres/recueils-proses-poesies-t2-fantasque-merveilleux/index.html` doit être à jour avec les 11 chapitres listés.

---

### Task 1: Décalage ordonné des chapitres existants (05 à 10 vers 06 à 11)

**Files:**
- Modify/Rename:
  - `public/books/recueils-proses-poesies-t2-fantasque-merveilleux/10-la-taniere-du-mage.html` → `11-la-taniere-du-mage.html`
  - `public/books/recueils-proses-poesies-t2-fantasque-merveilleux/09-farouches-apparitions.html` → `10-farouches-apparitions.html`
  - `public/books/recueils-proses-poesies-t2-fantasque-merveilleux/08-metro-fantasque.html` → `09-metro-fantasque.html`
  - `public/books/recueils-proses-poesies-t2-fantasque-merveilleux/07-dangaord.html` → `08-dangaord.html`
  - `public/books/recueils-proses-poesies-t2-fantasque-merveilleux/06-intermede-feerique.html` → `07-intermede-feerique.html`
  - `public/books/recueils-proses-poesies-t2-fantasque-merveilleux/05-ondes-positives.html` → `06-ondes-positives.html`

**Interfaces:**
- Consumes: Fichiers de chapitres existants dans `public/books/recueils-proses-poesies-t2-fantasque-merveilleux/`
- Produces: Fichiers renommés laissant le slot `05-le-pantin-et-la-poupee-de-cire.html` libre pour Task 2

- [ ] **Step 1: Renommer les fichiers de 10 à 05 dans l'ordre décroissant par commande git mv**

```bash
cd "D:/Users/Geoffroy/orca/workspaces/Hylst_Reader/v1.8.24/public/books/recueils-proses-poesies-t2-fantasque-merveilleux"
git mv 10-la-taniere-du-mage.html 11-la-taniere-du-mage.html
git mv 09-farouches-apparitions.html 10-farouches-apparitions.html
git mv 08-metro-fantasque.html 09-metro-fantasque.html
git mv 07-dangaord.html 08-dangaord.html
git mv 06-intermede-feerique.html 07-intermede-feerique.html
git mv 05-ondes-positives.html 06-ondes-positives.html
```

- [ ] **Step 2: Vérifier que les 6 fichiers renommés existent et que le slot 05 est libre**

Run: `ls -1 public/books/recueils-proses-poesies-t2-fantasque-merveilleux/*.html`
Expected: Fichiers 01 à 04, puis 06 à 11 présents, aucun fichier 05.

---

### Task 2: Rédaction et création du chapitre `05-le-pantin-et-la-poupee-de-cire.html`

**Files:**
- Create: `public/books/recueils-proses-poesies-t2-fantasque-merveilleux/05-le-pantin-et-la-poupee-de-cire.html`

**Interfaces:**
- Consumes: Manuscrit de novembre 2021 de Geoffroy Streit (première partie, notes d'étape, poème final de 5 strophes)
- Produces: Nouveau chapitre HTML balisé et prêt pour la liseuse

- [ ] **Step 1: Écrire le fichier complet avec la scène médiane harmonisée en vers libres**

Composer le fichier `05-le-pantin-et-la-poupee-de-cire.html` avec :
1. En-tête : classe `chapter-content`, titre `Le pantin et la poupée de cire`, byline `Texte composé pour un défi littéraire (Nouvember 2021), complété pour cette édition`.
2. Volet 1 : Texte intégral d'origine du pantin dans l'échoppe de la ruelle des Jouvenceaux.
3. Volet 2 : Raccord poétique développé en vers libres incorporant :
   - Le pendule égrenant les douze coups de minuit.
   - La boîte à musique remontée dont le cylindre égrène un refrain nostalgique.
   - Le jeu d'ombres dansant sur les murs et le plancher de chêne, les mains de porcelaine et de chiffon doucement soutenues dans une marelle enchantée.
   - L'impétuosité du pantin qui approche la flamme de la bougie pour lui voler un baiser timide ; la chaleur traîtresse qui attendrit la cire immaculée de la joue.
   - La larme de cire fondue qui s'écoule lentement alors que la mèche vacille et que les premières pâleurs de l'aube pointent aux carreaux.
4. Volet 3 : Le poème de 5 strophes textuel (*L'aube ouvre son regard, lisse sa chevelure...*).
5. Note de source en fin de chapitre.

- [ ] **Step 2: Vérifier l'équilibre des balises HTML et l'absence de tirets longs**

Run: `python scripts/check_dashes.py --root .`
Expected: [OK] Aucun tiret cadratin ou demi-cadratin.

---

### Task 3: Mise à jour de `books.json` et de `intro.html` de Tome II

**Files:**
- Modify: `public/books.json`
- Modify: `public/books/recueils-proses-poesies-t2-fantasque-merveilleux/intro.html`

**Interfaces:**
- Consumes: Fichiers de chapitres 01 à 11
- Produces: Métadonnées de bibliothèque à jour pour l'app shell et le lecteur

- [ ] **Step 1: Mettre à jour `public/books/recueils-proses-poesies-t2-fantasque-merveilleux/intro.html`**

Remplacer la mention « Dix textes où le réel se fissure... » par « Onze textes où le réel se fissure... », mentionner le diptyque des deux pantins de l'artisan, et ajuster « 11 textes · de 1999 à 2026 ».

- [ ] **Step 2: Mettre à jour l'entrée du Tome II dans `public/books.json`**

Dans l'objet `recueils-proses-poesies-t2-fantasque-merveilleux` :
1. Mettre à jour les entrées du tableau `chapters` :
   - Conserver chapitres 01 à 04.
   - Insérer en position 5 l'objet chapitre pour `05-le-pantin-et-la-poupee-de-cire` (id, title: "Le pantin et la poupée de cire", path: "books/recueils-proses-poesies-t2-fantasque-merveilleux/05-le-pantin-et-la-poupee-de-cire.html", shortDescription).
   - Mettre à jour les ids et paths des chapitres 06 à 11 pour refléter le décalage.
2. Vérifier la validité JSON avec `python -m json.tool public/books.json > /dev/null`.

- [ ] **Step 3: Vérifier que `books.json` est valide**

Run: `python -m json.tool public/books.json > /dev/null`
Expected: Code de retour 0 sans erreur de syntaxe.

---

### Task 4: Regénération de la fiche statique et mise à jour du Service Worker

**Files:**
- Modify: `sw.js`
- Generate: `livres/recueils-proses-poesies-t2-fantasque-merveilleux/index.html`

**Interfaces:**
- Consumes: `public/books.json`, `scripts/build_book_pages.py`
- Produces: Fiche statique de Tome II à jour et cache Service Worker incrémenté

- [ ] **Step 1: Regénérer les fiches de livres statiques**

```bash
python scripts/build_book_pages.py
```
Expected: `livres/recueils-proses-poesies-t2-fantasque-merveilleux/index.html` mis à jour avec les 11 chapitres.

- [ ] **Step 2: Incrémenter le cache Service Worker dans `sw.js`**

Passer `CACHE_NAME` de `'hylst-reader-v83'` à `'hylst-reader-v84'`.

- [ ] **Step 3: Exécuter la suite de tests de politique Service Worker et JSX**

```bash
node scripts/build_jsx.js --check && node scripts/test-sw-policy.js
```
Expected: [OK] 10 fichier(s) compilé(s) à jour. Tous les tests passent.

---

### Task 5: Contrôle qualité, rendu visuel desktop/mobile 390 px et validation

**Files:**
- Test: Script Python de vérification DOM, tirets longs et cohérence des 11 chapitres
- Visual: Captures Chrome headless 1440 px et 390 px

- [ ] **Step 1: Exécuter le script de vérification DOM et typographie sur les 11 chapitres de Tome II**

Vérifier que les balises HTML sont équilibrées, 0 tiret cadratin/demi-cadratin, présence des 11 chapitres.

- [ ] **Step 2: Générer un aperçu Chrome headless et capturer en 1440 px et 390 px**

Vérifier visuellement le rendu mobile (390 px) pour s'assurer de l'absence de débordement horizontal et de la beauté typographique du conte et du poème.

- [ ] **Step 3: Mettre à jour `CHANGELOG.md`, `todo.md` et `antigravity.md`**

Inscrire l'ajout de la v1.8.28 (Tome II porté à 11 textes avec *Le pantin et la poupée de cire*).
