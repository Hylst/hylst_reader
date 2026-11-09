# Anthologie Approche de la Neurodiversité (2003-2025) — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Réaliser l'anthologie intégrale d'*Approche de la Neurodiversité* en 16 chapitres et 4 grands mouvements thématiques couvrant 22 ans d'écrits (2003-2025), préservant la voix humaine, irrégulière et alambiquée de l'auteur, avec 3 schémas vectoriels SVG et 4 illustrations locales d'art éditorial Krea-2-Turbo.

**Architecture:** Extraction et intégration des sources textuelles du site `https://hylst.fr/neurodivers/` (`Lettre d'un dyspraxique`, `Chaos organisé`, `Labyrinthe des idées`, `Pensée en ébullition`, `Mémoire`, `Marre d'apprendre`) croisées avec les 3 manuscrits d'archives (`troubles dys.odt`, `Enfants en difficulté scolaire.doc`, `Idées pour lutter...pdf`), 3 schémas SVG interactifs, 4 visuels Krea WebP, catalogue `public/books.json` à 16 chapitres, SW v93 et déploiement production.

**Tech Stack:** HTML5 sémantique, SVG vectoriel responsive, React (liseuse Hylst_Reader), Python 3, Krea-2-Turbo (`wainsfw`), Service Worker PWA.

**Spec:** `docs/superpowers/specs/2026-11-09-approche-neurodiversite-recueil-design.md`

## Global Constraints

- **Zéro tiret long** : Aucun tiret cadratin (`—`, `\u2014`) ou demi-cadratin (`–`, `\u2013`). `python scripts/check_dashes.py --root .` doit retourner 0 erreur.
- **Zéro CDN au runtime** : Aucune dépendance externe, police ou image en ligne. Tous les assets résident dans `public/`.
- **Politique Service Worker** : Précache isolé préfixé `hylst-reader-`, exclusion des flux audio du précache.
- **CSP stricte** : `default-src 'self'`.
- **Filiation éthique** : Métadonnées claires (`writingPeriod: "2003-2025"`, `authorship: "human"`, note sur schémas SVG et visuels Krea).

## Review Focus

1. **Authenticité des textes historiques** : Chaque texte conserve son byline de date réelle (Mars 2003, 2005/2024, 2018-2022, Mars 2023, 2025).
2. **Asymétrie et liberté des longueurs** : Pas d'uniformisation artificielle des chapitres ; respect du rythme propre à chaque écrit.
3. **Absence de tirets cadratins** : Contrôle systématique sur les 16 fichiers HTML de chapitres.
4. **Cohérence du sommaire de 16 chapitres** : Chaînage strict dans `books.json` et dans la liseuse.
5. **Intégrité des 3 schémas vectoriels SVG** : Parfaite intégration responsive dans les chapitres 06, 08 et 13.

---

### Task 1: Rédaction Partie I (Prologue + Chapitres 01 à 03 — Confessions & Vécus de l'intérieur)

**Files:**
- Modify: `public/books/approche-de-la-neurodiversite/intro.html`
- Create: `public/books/approche-de-la-neurodiversite/00-prologue.html`
- Create: `public/books/approche-de-la-neurodiversite/01-lettre-d-un-dyspraxique.html`
- Create: `public/books/approche-de-la-neurodiversite/02-vie-dans-un-chaos-organise.html`
- Create: `public/books/approche-de-la-neurodiversite/03-pensee-en-ebullition.html`
- Test: `python scripts/check_dashes.py --root public/books/approche-de-la-neurodiversite`

**Interfaces:**
- Consumes: `LettreDyspraxique.tsx`, `VieChaosOrganise.tsx`, `PenseeEnEbullition.tsx`
- Produces: 5 fichiers HTML complets avec bylines d'époque et illustration `partie-1-couverture.webp`.

- [ ] **Step 1: Rédiger `intro.html` et `00-prologue.html`**
- [ ] **Step 2: Rédiger `01-lettre-d-un-dyspraxique.html` (Mars 2003)**
- [ ] **Step 3: Rédiger `02-vie-dans-un-chaos-organise.html` (2005/2024)**
- [ ] **Step 4: Rédiger `03-pensee-en-ebullition.html` (2024)**
- [ ] **Step 5: Contrôler l'absence de tirets cadratins**
- [ ] **Step 6: Commit**

---

### Task 2: Rédaction Partie II (Chapitres 04 à 07 — L'Enfance, l'École et la Pédagogie de terrain)

**Files:**
- Create: `public/books/approche-de-la-neurodiversite/04-la-neurodiversite-expliquee-aux-enfants.html`
- Create: `public/books/approche-de-la-neurodiversite/05-enfants-en-difficulte-scolaire.html`
- Create: `public/books/approche-de-la-neurodiversite/06-pedagogie-de-terrain-le-pas-a-pas.html`
- Create: `public/books/approche-de-la-neurodiversite/07-marre-d-apprendre.html`
- Test: `python scripts/check_dashes.py --root public/books/approche-de-la-neurodiversite`

**Interfaces:**
- Consumes: `NeurodiversiteEnfant.tsx`, `Enfants en difficulté scolaire.doc`, `MarreApprendre.tsx`, schéma SVG 2
- Produces: 4 fichiers HTML complets avec illustration `partie-2-couverture.webp`.

- [ ] **Step 1: Rédiger `04-la-neurodiversite-expliquee-aux-enfants.html` (Mars 2023)**
- [ ] **Step 2: Rédiger `05-enfants-en-difficulte-scolaire.html` (vers 2004)**
- [ ] **Step 3: Rédiger `06-pedagogie-de-terrain-le-pas-a-pas.html` avec schéma SVG 2**
- [ ] **Step 4: Rédiger `07-marre-d-apprendre.html` (2025)**
- [ ] **Step 5: Contrôler l'absence de tirets cadratins**
- [ ] **Step 6: Commit**

---

### Task 3: Rédaction Partie III (Chapitres 08 à 11 — Anatomie des Cerveaux qui dansent)

**Files:**
- Create: `public/books/approche-de-la-neurodiversite/08-les-cinq-familles-de-troubles-cognitifs.html`
- Create: `public/books/approche-de-la-neurodiversite/09-la-memoire-dans-la-neurodiversite.html`
- Create: `public/books/approche-de-la-neurodiversite/10-navigation-dans-le-labyrinthe-des-idees.html`
- Create: `public/books/approche-de-la-neurodiversite/11-apprendre-quand-le-cerveau-danse.html`
- Test: `python scripts/check_dashes.py --root public/books/approche-de-la-neurodiversite`

**Interfaces:**
- Consumes: `troubles dys.odt`, `MemoireNeurodiversite.tsx`, `NavigationLabyrintheIdees.tsx`, `StrategiesApprentissage.tsx`, schéma SVG 1
- Produces: 4 fichiers HTML complets avec schéma SVG 1.

- [ ] **Step 1: Rédiger `08-les-cinq-familles-de-troubles-cognitifs.html` avec schéma SVG 1**
- [ ] **Step 2: Rédiger `09-la-memoire-dans-la-neurodiversite.html` (2024)**
- [ ] **Step 3: Rédiger `10-navigation-dans-le-labyrinthe-des-idees.html` (2024)**
- [ ] **Step 4: Rédiger `11-apprendre-quand-le-cerveau-danse.html` (2025)**
- [ ] **Step 5: Contrôler l'absence de tirets cadratins**
- [ ] **Step 6: Commit**

---

### Task 4: Rédaction Partie IV et Épilogue (Chapitres 12 à 15 — La Boîte à Béquilles & Survie)

**Files:**
- Create: `public/books/approche-de-la-neurodiversite/12-l-environnement-et-le-corps-poser-les-fondations.html`
- Create: `public/books/approche-de-la-neurodiversite/13-le-delestage-mental-externaliser-la-memoire.html`
- Create: `public/books/approche-de-la-neurodiversite/14-conditionnement-hygiene-de-vie-et-esprit-embrume.html`
- Create: `public/books/approche-de-la-neurodiversite/15-epilogue-vivre-avec-la-friction.html`
- Test: `python scripts/check_dashes.py --root public/books/approche-de-la-neurodiversite`

**Interfaces:**
- Consumes: `Idées pour lutter...pdf` (juin 2022), schéma SVG 3, illustrations Partie 3 et Épilogue
- Produces: 4 fichiers HTML complets avec schéma SVG 3.

- [ ] **Step 1: Rédiger `12-l-environnement-et-le-corps-poser-les-fondations.html` (Juin 2022)**
- [ ] **Step 2: Rédiger `13-le-delestage-mental-externaliser-la-memoire.html` avec schéma SVG 3**
- [ ] **Step 3: Rédiger `14-conditionnement-hygiene-de-vie-et-esprit-embrume.html` (Juin 2022)**
- [ ] **Step 4: Rédiger `15-epilogue-vivre-avec-la-friction.html`**
- [ ] **Step 5: Nettoyer tout ancien fichier orphelin (`chapitre-*.html`)**
- [ ] **Step 6: Contrôler l'absence de tirets cadratins sur les 16 fichiers HTML**
- [ ] **Step 7: Commit**

---

### Task 5: Intégration catalogue (books.json) à 16 entrées et fiche statique

**Files:**
- Modify: `public/books.json`
- Modify: `livres/approche-de-la-neurodiversite/index.html`
- Test: `python scripts/build_book_pages.py && python -m json.tool public/books.json > /dev/null`

**Interfaces:**
- Consumes: Les 16 fichiers de chapitres
- Produces: Sommaire à 16 entrées, période `2003-2025 (compilation 2026)`, fiche statique régénérée.

- [ ] **Step 1: Mettre à jour `public/books.json` avec les 16 entrées**
- [ ] **Step 2: Régénérer la fiche statique (`build_book_pages.py`)**
- [ ] **Step 3: Vérifier l'intégrité du JSX et des tirets**
- [ ] **Step 4: Commit**

---

### Task 6: Mise à jour Service Worker (v93) et validation locale

**Files:**
- Modify: `sw.js`
- Test: `node scripts/test-sw-policy.js`

- [ ] **Step 1: Passer `sw.js` à `hylst-reader-v93`**
- [ ] **Step 2: Exécuter les tests SW policy**
- [ ] **Step 3: Contrôle global qualité local**
- [ ] **Step 4: Commit**

---

### Task 7: Documentation, synchronisation miroir et déploiement production (v1.8.37)

**Files:**
- Modify: `CHANGELOG.md`
- Modify: `todo.md`
- Modify: `antigravity.md`
- Modify: Dépôt plateforme `D:/0CODE/AntiGravity/Cours_Memos/Docker`
- Test: `powershell -ExecutionPolicy Bypass -File scripts/verify-release.ps1`

- [ ] **Step 1: Mettre à jour `CHANGELOG.md`, `todo.md` et `antigravity.md`**
- [ ] **Step 2: Commiter et pousser dans le dépôt source**
- [ ] **Step 3: Synchroniser vers le miroir plateforme (`sync-to-platform.ps1 -Prune`)**
- [ ] **Step 4: Mettre à jour les documentations Docker**
- [ ] **Step 5: Commiter et pousser sur `cours_info` `main`**
- [ ] **Step 6: Vérifier le déploiement en production (`verify-release.ps1`)**
