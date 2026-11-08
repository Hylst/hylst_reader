# Chronique d'une Atrophie Programmée — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Réécrire, unifier et intégrer le roman de science-fiction dystopique *Chronique d'une Atrophie Programmée* (48 chapitres en 4 actes) comme 12ᵉ livre dans La Bibliothèque de Hylst, en restaurant la voix d'auteur brute et excentrique de Geoffroy Streit et en éliminant les stéréotypes d'IA.

**Architecture:** Fusion de l'Acte 1 (archive locale 2026) et des Actes 2 à 4 (manuscrit 2022), application d'un nouveau schéma onomastique (Léonce, Marthe, Barnabé, Le Cliquet, Tristan, L'Intendance), rédaction de 48 chapitres HTML aux normes Hylst_Reader avec 48 illustrations WebP locales optimisées, fiche statique, intégration dans `public/books.json`, mise à jour du Service Worker et validation stricte (zéro tiret long, CSP, offline).

**Tech Stack:** HTML5 sémantique, React (liseuse Hylst_Reader), Python 3 (générateurs statiques et linter de tirets), Node.js (compilateur JSX Babel et tests de politique Service Worker), Service Worker PWA Vanilla JS.

**Spec:** `docs/superpowers/specs/2026-11-08-chronique-atrophie-design.md`

## Global Constraints

- **Zéro tiret long** : Aucun tiret cadratin (`—`, `\u2014`) ou demi-cadratin (`–`, `\u2013`) dans les fichiers HTML, JSON ou JS servis. `python scripts/check_dashes.py --root .` doit retourner 0 erreur.
- **Zéro CDN au runtime** : Aucune dépendance externe, police ou image en ligne. Tous les assets résident dans `public/`.
- **Politique Service Worker** : Précache isolé préfixé `hylst-reader-`, exclusion stricte des fichiers audio lourds du précache.
- **CSP stricte** : `default-src 'self'`. Aucun script inline.
- **Filiation éthique** : Métadonnées claires (`writingPeriod: "2022-2026"`, `authorship: "human"`, mention explicite des illustrations de l'archive).

## Review Focus

1. **Intégrité du dénouement tragique (Chapitres 47-48)** : Le twist du « Frisson Divin » (dopamine + histamine) doit être scrupuleusement conservé pour préserver l'ironie satirique de l'auteur.
2. **Absence de personnages exclus dans les illustrations** : Aucune image de chapitre ne doit montrer le clone Marcus ou la commandante Elara.
3. **Absence de tirets cadratins dans les 48 chapitres rédigés** : La ponctuation expressive (points de suspension, parenthèses, deux-points, virgules) doit se conformer à l'interdiction stricte des tirets cadratins.
4. **Cohérence du sommaire et de la pagination** : Les 48 chapitres doivent être correctement chaînés avec titres, identifiants et navigation précédent/suivant.
5. **Retrait propre de `f17` des livres futurs** : L'identifiant `f17` doit disparaître de `LibraryView.jsx` pour éviter les doublons avec le livre désormais actif.

---

### Task 1: Extraction et audit visuel des 48 illustrations WebP

**Files:**
- Create: `public/books/chronique-une-atrophie-programmee/assets/`
- Test: `python scripts/test_assets_atrophie.py`

**Interfaces:**
- Consumes: `D:/Downloads/0manus/Chronique-Atrophie-Programmee-Hors-Ligne.zip`
- Produces: 48 fichiers WebP dans `public/books/chronique-une-atrophie-programmee/assets/chapter-01.webp` ... `chapter-48.webp`.

- [ ] **Step 1: Écrire le script de test pour valider la présence et la taille des 48 images**

Créer `scripts/test_assets_atrophie.py` :
```python
from pathlib import Path

def test_chapter_assets():
    assets_dir = Path("public/books/chronique-une-atrophie-programmee/assets")
    assert assets_dir.exists(), "Le dossier d'assets n'existe pas"
    for i in range(1, 49):
        img = assets_dir / f"chapter-{i:02d}.webp"
        assert img.exists(), f"Image manquante: {img}"
        size = img.stat().st_size
        assert size > 5000 and size < 600000, f"Image {img} de taille anormale: {size}"
    print("ALL 48 CHAPTER ASSETS OK")

if __name__ == "__main__":
    test_chapter_assets()
```

- [ ] **Step 2: Vérifier que le test échoue avant extraction**

Run: `python scripts/test_assets_atrophie.py`
Expected: FAIL avec "Le dossier d'assets n'existe pas"

- [ ] **Step 3: Extraire et auditer les 48 illustrations adaptées depuis le zip**

Écrire et exécuter un script d'extraction qui extrait les images WebP de `D:/Downloads/0manus/Chronique-Atrophie-Programmee-Hors-Ligne.zip`, remplace les éventuels portraits des personnages rejetés (Marcus, Elara) par des illustrations de scènes urbaines/tunnels du même zip, et les place dans `public/books/chronique-une-atrophie-programmee/assets/chapter-01.webp` à `chapter-48.webp`.

- [ ] **Step 4: Valider le test d'assets**

Run: `python scripts/test_assets_atrophie.py`
Expected: `ALL 48 CHAPTER ASSETS OK`

- [ ] **Step 5: Commit**

```bash
git add public/books/chronique-une-atrophie-programmee/assets/ scripts/test_assets_atrophie.py
git commit -m "feat(atrophie): extraction et audit des 48 illustrations WebP"
```

---

### Task 2: Rédaction de l'Acte 1 (Chapitres 1 à 12 — Le Plissage et la Fêlure)

**Files:**
- Create: `public/books/chronique-une-atrophie-programmee/01-la-moquette-de-l-ame.html` à `12-la-chute-dans-le-tuyau.html`
- Create: `public/books/chronique-une-atrophie-programmee/intro.html`
- Test: `python scripts/check_dashes.py --root public/books/chronique-une-atrophie-programmee`

**Interfaces:**
- Consumes: Chapitres 1 à 12 de `Chronique-Atrophie-Programmee-Hors-Ligne.zip`
- Produces: 12 fichiers HTML conformes avec nouveaux noms (Léonce l'Ajusteur, L'Intendance / S.Y.N.D.I.C., la Trame, Barnabé Pépé Rature, Marthe la Râpe aperçue) et style asymétrique d'auteur.

- [ ] **Step 1: Écrire l'introduction du livre (`intro.html`)**

Créer `public/books/chronique-une-atrophie-programmee/intro.html` avec présentation du roman, date d'écriture `2022-2026 (compilation 2026)`, note de transparence d'auteur et filiation éthique (100 % écrit par l'auteur, illustrations tirées de l'archive).

- [ ] **Step 2: Rédiger et adapter les chapitres 1 à 6 en HTML**

Convertir et réécrire les chapitres 1 à 6 en injectant :
- Léonce, Harmonisateur de Narratifs, surnommé « Le Plisseur ».
- L'Intendance bureaucratique et mielleuse sous le S.Y.N.D.I.C.
- Onomatopées et phrases alambiquées.
- Structure HTML de liseuse avec `<h1 class="chapter-main-title">`, `<p class="chapter-byline">`, illustration `<figure class="chapter-figure"><img src="public/books/chronique-une-atrophie-programmee/assets/chapter-XX.webp" ...></figure>`, et paragraphes `<p class="chapter-paragraph">`.

- [ ] **Step 3: Rédiger et adapter les chapitres 7 à 12 en HTML**

Convertir et réécrire les chapitres 7 à 12 (la découverte du manifeste, la disparition des collègues, le vertige devant la Tour Eiffel rouillée, la rupture d'implant et la chute physique dans le tuyau de purge).

- [ ] **Step 4: Contrôler l'absence de tirets cadratins**

Run: `python scripts/check_dashes.py --root public/books/chronique-une-atrophie-programmee`
Expected: `[OK] Aucun tiret cadratin ou demi-cadratin dans 13 fichier(s) contrôlé(s)`

- [ ] **Step 5: Commit**

```bash
git add public/books/chronique-une-atrophie-programmee/
git commit -m "feat(atrophie): redaction Acte 1 (chapitres 1 a 12) et intro"
```

---

### Task 3: Rédaction de l'Acte 2 (Chapitres 13 à 24 — La Chair et les Décombres)

**Files:**
- Create: `public/books/chronique-une-atrophie-programmee/13-le-reveil-brutal.html` à `24-veillee-sous-les-tenebres.html`
- Test: `python scripts/check_dashes.py --root public/books/chronique-une-atrophie-programmee`

**Interfaces:**
- Consumes: Chapitres 13 à 24 de `D:/Downloads/Chronique d’une Atrophie Programmée .md`
- Produces: 12 fichiers HTML de l'Acte 2 avec Léonce, Marthe « La Râpe », Barnabé « Pépé Rature », Le Cliquet.

- [ ] **Step 1: Rédiger et adapter les chapitres 13 à 18 en HTML**

Adapter les chapitres du manuscrit 2022 :
- 13 : Le Réveil Brutal (la planche de bois, le gruau amer, Barnabé au regard d'acier).
- 14 : La Douleur est une Information (Marthe « La Râpe » et l'apprentissage de la marche sur graviers).
- 15 : Le Premier Rhume (la morve salvatrice, la fièvre comme preuve d'immunité).
- 16 : Les Fantômes du Papier (la bibliothèque souterraine de Barnabé).
- 17 : La Mémoire de la Terre (l'argile et les vers de terre).
- 18 : La Boîte de Svalbard (les semences protégées).
Insuffler des tournures d'auteur, ruptures, sonorités et folie humaine.

- [ ] **Step 2: Rédiger et adapter les chapitres 19 à 24 en HTML**

Adapter les chapitres :
- 19 : Hors du Terrier (sortie avec les masques).
- 20 : Les Cicatrices du Monde (l'ancienne exploitation minière).
- 21 : La Marche vers le Grand Réfrigérant.
- 22 : Le Tombeau des Géants.
- 23 : Le Chant des Rouages (Le Cliquet ranime la mécanique).
- 24 : Veillée sous les Ténèbres.

- [ ] **Step 3: Contrôler l'absence de tirets cadratins**

Run: `python scripts/check_dashes.py --root public/books/chronique-une-atrophie-programmee`
Expected: `[OK] Aucun tiret cadratin ou demi-cadratin dans 25 fichier(s) contrôlé(s)`

- [ ] **Step 4: Commit**

```bash
git add public/books/chronique-une-atrophie-programmee/
git commit -m "feat(atrophie): redaction Acte 2 (chapitres 13 a 24)"
```

---

### Task 4: Rédaction de l'Acte 3 (Chapitres 25 à 36 — L'Ombre et le Doute)

**Files:**
- Create: `public/books/chronique-une-atrophie-programmee/25-la-derive-des-signaux.html` à `36-le-basculement.html`
- Test: `python scripts/check_dashes.py --root public/books/chronique-une-atrophie-programmee`

**Interfaces:**
- Consumes: Chapitres 25 à 36 de `D:/Downloads/Chronique d’une Atrophie Programmée .md`
- Produces: 12 fichiers HTML de l'Acte 3.

- [ ] **Step 1: Rédiger et adapter les chapitres 25 à 30 en HTML**

Adapter les chapitres :
- 25 : La Dérive des Signaux.
- 26 : Les Confidences de Barnabé.
- 27 : Le Plan de l'Anesthésie Générale.
- 28 : L'Alerte au Secteur Cinq.
- 29 : La Blessure Ouverte.
- 30 : L'Étau Mécanique.

- [ ] **Step 2: Rédiger et adapter les chapitres 31 à 36 en HTML**

Adapter les chapitres :
- 31 : La Panne Frigorigène.
- 32 : Les Paroles de Fer (Marthe inflexible).
- 33 : Silence dans le Câble.
- 34 : La Découverte de la Faille (les conduits de la Tour Zéphyr).
- 35 : L'Aveu de Léonce (culpabilité de l'Harmonisateur).
- 36 : Le Basculement.

- [ ] **Step 3: Contrôler l'absence de tirets cadratins**

Run: `python scripts/check_dashes.py --root public/books/chronique-une-atrophie-programmee`
Expected: `[OK] Aucun tiret cadratin ou demi-cadratin dans 37 fichier(s) contrôlé(s)`

- [ ] **Step 4: Commit**

```bash
git add public/books/chronique-une-atrophie-programmee/
git commit -m "feat(atrophie): redaction Acte 3 (chapitres 25 a 36)"
```

---

### Task 5: Rédaction de l'Acte 4 (Chapitres 37 à 48 — L'Hérésie du Pollen et le Frisson Divin)

**Files:**
- Create: `public/books/chronique-une-atrophie-programmee/37-au-fond-du-gouffre.html` à `48-la-fin-et-les-retifs.html`
- Test: `python scripts/check_dashes.py --root public/books/chronique-une-atrophie-programmee`

**Interfaces:**
- Consumes: Chapitres 37 à 48 de `D:/Downloads/Chronique d’une Atrophie Programmée .md`
- Produces: 12 fichiers HTML de l'Acte 4 avec le twist satirique du « Frisson Divin ».

- [ ] **Step 1: Rédiger et adapter les chapitres 37 à 42 en HTML**

Adapter :
- 37 : Au Fond du Gouffre.
- 38 : L'Idée Scandaleuse (le pollen et le réflexe d'éternuement).
- 39 : La Serre Hydroponique de Guerre.
- 40 : Le Schisme de Tristan (l'idéaliste qui refuse la souffrance infligée).
- 41 : La Logique du Scalpel.
- 42 : L'Infiltration des Conduits.

- [ ] **Step 2: Rédiger et adapter les chapitres 43 à 48 en HTML**

Adapter :
- 43 : La Moisson Jaune.
- 44 : L'Ascension vers la Tour Zéphyr.
- 45 : L'Injection dans la turbine centrale.
- 46 : Les Premiers Éternuements (la panique des bronches dans tout Paris).
- 47 : Le Coup de Maître de l'Intendance (l'assimilation diabolique : dopamine + histamine = Le Frisson Divin).
- 48 : La Fin et les Rétifs (les Rétifs lucides face à la ville en extase morbide).

- [ ] **Step 3: Contrôler l'absence de tirets cadratins**

Run: `python scripts/check_dashes.py --root public/books/chronique-une-atrophie-programmee`
Expected: `[OK] Aucun tiret cadratin ou demi-cadratin dans 49 fichier(s) contrôlé(s)`

- [ ] **Step 4: Commit**

```bash
git add public/books/chronique-une-atrophie-programmee/
git commit -m "feat(atrophie): redaction Acte 4 (chapitres 37 a 48) et denouement Frisson Divin"
```

---

### Task 6: Intégration catalogue, générateur de fiches et mise à jour UI

**Files:**
- Modify: `public/books.json`
- Modify: `js/components/LibraryView.jsx`
- Modify: `scripts/build_book_pages.py`
- Test: `node scripts/build_jsx.js --check && python scripts/build_book_pages.py`

**Interfaces:**
- Consumes: Les 48 chapitres et `intro.html` créés dans les tâches précédentes.
- Produces: 12ᵉ livre dans `public/books.json`, fiche statique `livres/chronique-une-atrophie-programmee/index.html`, retrait de `f17` dans `LibraryView.jsx`.

- [ ] **Step 1: Ajouter le livre dans `public/books.json`**

Ajouter l'entrée complète pour `chronique-une-atrophie-programmee` avec :
- `title: "Chronique d'une atrophie programmée"`
- `subtitle: "Roman d'anticipation et d'hérésie biologique"`
- `author: "Hylst (Geoffroy Streit)"`
- `year: "2022-2026 (compilation 2026)"`
- `writingPeriod: "2022-2026"`
- `compilationYear: 2026`
- `authorship: "human"`
- `illustrationNote: "Roman rédigé entre 2022 et 2026 (100 % de l'auteur, sans IA) · Illustrations d'ambiance et de décors de l'archive 2026 · Compilation 2026"`
- `chapters`: liste ordonnée des 48 chapitres avec titre, fichier et nombre de mots.

- [ ] **Step 2: Mettre à jour `LibraryView.jsx` pour retirer `f17` de `FUTURE_BOOKS`**

Supprimer l'entrée `id: 'f17'` de la constante `FUTURE_BOOKS` dans `js/components/LibraryView.jsx`, puis recompiler le JSX :
Run: `node scripts/build_jsx.js`
Expected: `[OK] 10 fichier(s) JSX compilé(s) vers js/dist`

- [ ] **Step 3: Mettre à jour `scripts/build_book_pages.py` et générer les 12 fiches**

Vérifier la génération de `livres/chronique-une-atrophie-programmee/index.html` :
Run: `python scripts/build_book_pages.py`
Expected: `12 fiches generees.`

- [ ] **Step 4: Valider la conformité JSX et tirets**

Run: `node scripts/build_jsx.js --check && python scripts/check_dashes.py --root .`
Expected: `[OK] 10 fichier(s) compilé(s) à jour` et `[OK] Aucun tiret cadratin ou demi-cadratin`

- [ ] **Step 5: Commit**

```bash
git add public/books.json js/components/LibraryView.jsx js/dist/ scripts/build_book_pages.py livres/
git commit -m "feat(atrophie): integration catalogue, 12 fiches statiques et retrait de f17"
```

---

### Task 7: Mise à jour du Service Worker et validation locale

**Files:**
- Modify: `sw.js`
- Test: `node scripts/test-sw-policy.js`

**Interfaces:**
- Consumes: Nouveaux fichiers de chapitres et assets dans `public/books/chronique-une-atrophie-programmee/`.
- Produces: Cache `hylst-reader-v90` déclarant l'ensemble des 48 chapitres et images.

- [ ] **Step 1: Incrémenter et enrichir `sw.js`**

Passer le cache à `hylst-reader-v90` et s'assurer que les routes et assets du nouveau livre sont bien inclus dans le précache statique.

- [ ] **Step 2: Exécuter les tests de politique du Service Worker**

Run: `node scripts/test-sw-policy.js`
Expected: `Tous les tests de politique du Service Worker passent.`

- [ ] **Step 3: Contrôle global qualité local**

Run: `python scripts/check_dashes.py --root . && node scripts/build_jsx.js --check && python -m json.tool public/books.json > /dev/null`
Expected: Toutes les commandes réussissent avec code 0.

- [ ] **Step 4: Commit**

```bash
git add sw.js
git commit -m "feat(sw): version hylst-reader-v90 pour Chronique d'une atrophie programmée"
```

---

### Task 8: Documentation, synchronisation miroir et déploiement production (v1.8.34)

**Files:**
- Modify: `CHANGELOG.md`
- Modify: `todo.md`
- Modify: `antigravity.md`
- Modify: Dépôt plateforme `D:/0CODE/AntiGravity/Cours_Memos/Docker` (`changelog.md`, `todo.md`, `securite.md`, `hylst_IT_platform_content.md`, `books_reader/`)
- Test: `powershell -ExecutionPolicy Bypass -File scripts/verify-release.ps1`

- [ ] **Step 1: Mettre à jour `CHANGELOG.md`, `todo.md` et `antigravity.md` dans la source**

Consigner la version 1.8.34 : entrée du 12ᵉ livre *Chronique d'une atrophie programmée* (48 chapitres, réécriture humaine débridée, élimination des tropes IA, cache `hylst-reader-v90`).

- [ ] **Step 2: Commiter et pousser dans le dépôt source**

```bash
git add CHANGELOG.md todo.md antigravity.md
git commit -m "docs: release notes v1.8.34 pour Chronique d'une atrophie programmée"
git push origin Hylst/v1.8.24
```

- [ ] **Step 3: Synchroniser vers le miroir de plateforme**

Run: `powershell -ExecutionPolicy Bypass -File scripts/sync-to-platform.ps1 -Prune`
Expected: Build généré, 0 tiret long, synchronisation réussie.

- [ ] **Step 4: Mettre à jour les documentations de la plateforme Docker**

Mettre à jour `changelog.md`, `todo.md`, `securite.md` et `hylst_IT_platform_content.md` dans `D:/0CODE/AntiGravity/Cours_Memos/Docker/`.

- [ ] **Step 5: Commiter et pousser sur `cours_info` `main`**

```bash
cd "D:/0CODE/AntiGravity/Cours_Memos/Docker"
git add books_reader
git commit -m "Books Reader 1.8.34 : 12e livre Chronique d'une atrophie programmée (48 chapitres)"
git add changelog.md todo.md securite.md hylst_IT_platform_content.md
git commit -m "docs : Books Reader 1.8.34 synchronise"
git push origin main
```

- [ ] **Step 6: Vérifier le déploiement en production**

Attendre le déploiement Coolify et exécuter :
Run: `powershell -ExecutionPolicy Bypass -File scripts/verify-release.ps1`
Expected: 100 % vert avec HTTP 200 sur `https://hylst.fr/books_reader/livres/chronique-une-atrophie-programmee/`.
