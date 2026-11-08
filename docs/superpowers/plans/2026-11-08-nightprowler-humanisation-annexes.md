# Plan d'implémentation : Humanisation des scénarios et refonte des Annexes (Nightprowler)

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Enrichir le style littéraire des scénarios des Carnets de Samarande (VIII à XI) pour lui donner une voix d'auteur vivante, humaine, alambiquée et mordante, et compléter/corriger en profondeur le chapitre « XIII. Annexes » avec enveloppement des tables, lexique étendu et aides de jeu.

**Architecture:** Édition manuelle chirurgicale des fichiers HTML de chapitre dans `public/books/nightprowler-carnets-de-samarande/`. Respect strict des règles de typographie (aucun tiret long), accessibilité des tables (`.chapter-table-scroll` avec `data-cols`), validation SW et synchronisation plateforme.

**Tech Stack:** HTML5 sémantique, CSS Vanilla, JavaScript / Node.js (scripts de build et vérification), Python (check_dashes).

**Spec:** Instructions utilisateur directes : « dans les carnets de samarandes, pour ce qui est des scnéarions, rend si possible l'écriture plus humaine, avec parfois un brin de folie, quelques iréégularités, phrases alamnbiquées... complète et corrige la partie 'XIII. Annexes' ».

## Global Constraints

- Aucun tiret cadratin ou demi-cadratin dans les fichiers servis (`python scripts/check_dashes.py --root .`).
- Ne jamais régénérer automatiquement les HTML de `public/books/` : édition manuelle exclusive.
- Tous les tableaux `<table class="chapter-stats-table">` doivent être encapsulés dans `<div class="chapter-table-scroll" data-cols="N" role="region" aria-label="Tableau du chapitre" tabindex="0">`.
- Préserver tous les textes et données d'origine (1999-2011).
- Pas de CDN au runtime, CSP `script-src 'self'`.
- Synchronisation miroir via `scripts/sync-to-platform.ps1 -Prune` et vérification sur `http://127.0.0.1:8765/books_reader/`.

## Review Focus

1. Absence de tirets cadratins/demi-cadratins dans tous les fichiers touchés.
2. Équilibre parfait des balises HTML sur les chapitres modifiés.
3. Conformité de chaque conteneur de tableau avec `data-cols` égal au nombre réel de `<th>`.
4. Maintien de l'exactitude des valeurs de règles et cohérence du lore.
5. Intégrité du rendu responsive sur écran mobile de 390 px.

---

### Task 1: Compléter et corriger le chapitre « XIII. Annexes »

**Files:**
- Modify: `public/books/nightprowler-carnets-de-samarande/chapitre-13.html`

- [ ] **Step 1: Envelopper les 14 tableaux existants**
  Ajouter `<div class="chapter-table-scroll" data-cols="N" role="region" aria-label="Tableau du chapitre" tabindex="0">` autour de chaque tableau (Identité, Caractéristiques, Compétences, Fatigue/Santé, Armes, Équipement, Lexique, Chronologie).

- [ ] **Step 2: Corriger et étendre le Lexique**
  Harmoniser l'orthographe (ex: Kahlér avec accent), ajouter les termes clés introduits dans les scénarios VIII à XI (Azefhfkrijiiir, Bromi, Kharvâsh, Main de Cendre, Veilleurs, Marques, La Verte, Bief, Pierre de rosette, Quartier 30, Hautes Lices, Double 7, etc.), avec des définitions savoureuses et précises.

- [ ] **Step 3: Compléter la Chronologie et ajouter des tables d'ambiance**
  Intégrer les repères temporels des scénarios. Ajouter une table d'argot des voleurs de Samarande et une table des aléas urbains pour faire de cette annexe un véritable outil de jeu vivant.

- [ ] **Step 4: Mettre à jour la note de source et vérifier la typographie**
  Signaler les compléments dans `chapter-source-note`, éliminer tout tiret cadratin.

---

### Task 2: Humaniser et donner du relief d'auteur aux scénarios (Chapitres VIII à XI)

**Files:**
- Modify: `public/books/nightprowler-carnets-de-samarande/chapitre-8.html`
- Modify: `public/books/nightprowler-carnets-de-samarande/chapitre-9.html`
- Modify: `public/books/nightprowler-carnets-de-samarande/chapitre-10.html`
- Modify: `public/books/nightprowler-carnets-de-samarande/chapitre-11.html`

- [ ] **Step 1: Chapitre VIII (*Le squelette enfoui d'Azefhfkrijiiir*)**
  Retoucher les descriptions pour insuffler cette voix d'auteur brute, un brin hallucinée : la moiteur de la crypte, les sarcasmes des Veilleurs, l'ironie noire autour du crâne scellé, phrases plus sinueuses et organiques.

- [ ] **Step 2: Chapitre IX (*Esclavage gouri sans vergogne*)**
  Donner du corps à la détresse et à la folie du camp : le rat géant qui chuchote des absurdités venimeuses, l'odeur de la soupe aux mousses, les jurons des mineurs, les phrases alambiquées qui dépeignent la bureaucratie carcérale de la Main de Cendre.

- [ ] **Step 3: Chapitre X (*Vapeur et boulons*)**
  Renforcer le profil d'Humbert en savant toqué, maniaque, toussotant et obsédé par ses jauges ; décrire la machine avec ses gargouillements métalliques baroques ; donner à la filature de Tramiel le parfum d'une comédie sinistre dans les bas-fonds.

- [ ] **Step 4: Chapitre XI (*La reconquête du trône des Rodallois*)**
  Insuffler la grandiloquence baroque et la cruauté froide de la féodalité : les formules ampoulées des quatre lois, les remarques caustiques sur les ducs de Lujevire, la lourdeur poisseuse du démon cornu et l'absurdité du destin princier.

---

### Task 3: Envelopper les tableaux de `chapitre-12.html` (*Pistes inachevées*)

**Files:**
- Modify: `public/books/nightprowler-carnets-de-samarande/chapitre-12.html`

- [ ] **Step 1: Envelopper les 4 tableaux dans `.chapter-table-scroll`**
  Vérifier les attributs `data-cols` et la classe `.chapter-stats-table.descripteurs`.

---

### Task 4: Contrôles qualité et validation

- [ ] **Step 1: Contrôle typographique**
  Exécuter `python scripts/check_dashes.py --root .`.
- [ ] **Step 2: Contrôle JSX et Service Worker**
  Exécuter `node scripts/build_jsx.js --check` et `node scripts/test-sw-policy.js`.
- [ ] **Step 3: Contrôle HTML et SVG**
  Vérifier l'équilibrage de l'arbre DOM et les wrappers des tableaux.
- [ ] **Step 4: Rendu visuel et mobile 390 px**
  Vérifier l'affichage via Chrome headless.

---

### Task 5: Synchronisation et livraison

- [ ] **Step 1: Synchroniser vers le miroir**
  Exécuter `scripts/sync-to-platform.ps1 -Prune`.
- [ ] **Step 2: Tester sur `http://127.0.0.1:8765/books_reader/`**
- [ ] **Step 3: Mettre à jour la documentation (CHANGELOG, todo, antigravity, docs plateforme)**
- [ ] **Step 4: Commits et déploiement**
