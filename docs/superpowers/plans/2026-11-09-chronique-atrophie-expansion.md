# Chronique d'une atrophie programmée - Plan d'Expansion et de Refonte Littéraire

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Déployer une version romanesque enrichie, asymétrique et pessimiste de *Chronique d'une atrophie programmée* (~50 000 mots), éliminant les facilités biologiques, dotant l'univers d'une cohérence socio-médicale rigoureuse et intégrant l'arc tragique complet de Tristan et de l'attentat allergique.

**Architecture:** Refonte progressive des 4 actes en fichiers HTML autonomes dans `public/books/chronique-une-atrophie-programmee/`, alternant 4 chapitres-piliers massifs (3 000 - 4 500 mots), des chapitres de terrain (1 200 - 2 000 mots), des scènes d'impact et des interludes documentaires. Les métadonnées sont synchronisées dans `public/books.json`, puis compilées et validées par la suite de scripts existante.

**Tech Stack:** HTML sémantique, CSS moderne (liseuse Hylst_Reader), Python (`check_dashes.py`, scripts de vérification), Node.js (`build_jsx.js`), PowerShell (`sync-to-platform.ps1`, `verify-release.ps1`).

**Spec:** `docs/superpowers/specs/2026-11-09-chronique-atrophie-expansion-design.md`

## Global Constraints

- Respect strict de la règle zéro tiret cadratin ou demi-cadratin : `python scripts/check_dashes.py --root .` doit renvoyer 0 erreur sur tous les fichiers.
- Aucune régression sur les chemins relatifs des 48 illustrations WebP existantes (`assets/chapter-XX.webp?v=5`).
- Zéro dépendance externe, zéro CDN, respect de la CSP `'self'`.
- Préservation de la voix d'auteur (argot d'atelier, ironie mordante, descriptions organiques et viscérales).

## Review Focus

1. **Régression de dash typographique** : Toute introduction accidentelle de `—` ou `–` casse la suite de tests de release. Test : exécution immédiate de `check_dashes.py` à chaque fin de tâche.
2. **Incohérence des fers de marche** : Léonce ne doit à aucun moment courir ou sauter sans que le poids et la douleur de ses attelles de ferraille ne soient rappelés. Test : inspection de cohérence textuelle sur les verbes de motricité.
3. **Disparition de Tristan** : Tristan ne doit pas être oublié après le chapitre 40 ; son sort lors de l'attentat doit être montré explicitement. Test : présence active de Tristan dans l'Acte 4.
4. **Vérification de l'encodage UTF-8** : Aucun caractère corrompu (mojibake) lors de la génération des chapitres étendus. Test : relecture par script Python `open(..., encoding='utf-8')`.
5. **Validation Service Worker et Production** : Les modifications de chapitres doivent être intégrées dans le build et synchronisées vers Docker. Test : `verify-release.ps1` vert.

---

### Task 1 : Rédaction de la Bible du Monde et du Canon Révisé

**Files:**
- Create: `docs/superpowers/specs/bible-atrophie-canon.md`
- Test: `tests/test_canon_atrophie.py`

**Interfaces:**
- Consumes: `docs/superpowers/specs/2026-11-09-chronique-atrophie-expansion-design.md`
- Produces: Termes canoniques, chronologie (2038-2080), fiches de voix et règles anatomiques pour les tâches 2 à 5.

- [ ] **Step 1: Écrire le test automatisé vérifiant la présence des 5 concepts clés du canon**

Créer `tests/test_canon_atrophie.py` vérifiant que `bible-atrophie-canon.md` contient les termes obligatoires : `Écœurement Sémantique`, `Fers de marche`, `Tonicité Dégressive`, `Rupture d'antihistaminiques`, `Frisson Divin`.

- [ ] **Step 2: Exécuter le test pour vérifier l'échec initial**

Run: `python -m unittest tests/test_canon_atrophie.py`
Expected: FAIL (fichier absent).

- [ ] **Step 3: Rédiger la Bible dans `docs/superpowers/specs/bible-atrophie-canon.md`**

Inclure chronologie 2038-2080, glossaire du S.Y.N.D.I.C., anatomie des attelles de Léonce, profils psychologiques de Barnabé, Marthe, Tristan et Le Cliquet, carte des galeries.

- [ ] **Step 4: Exécuter le test de validation**

Run: `python -m unittest tests/test_canon_atrophie.py && python scripts/check_dashes.py --root docs/superpowers/specs`
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add docs/superpowers/specs/bible-atrophie-canon.md tests/test_canon_atrophie.py
git commit -m "docs(atrophie): bible du monde et canon revise pour l'expansion du roman"
```

---

### Task 2 : Refonte et Expansion de l'Acte 1 (Chapitres 01 à 12)

**Files:**
- Modify: `public/books/chronique-une-atrophie-programmee/01-la-moquette-de-l-ame.html` à `12-la-chute-dans-le-tuyau.html`
- Create: `public/books/chronique-une-atrophie-programmee/interlude-01-registre-des-mots-interdits.html`
- Test: `tests/test_act1_expansion.py`

**Interfaces:**
- Consumes: `docs/superpowers/specs/bible-atrophie-canon.md`
- Produces: Acte 1 densifié (~12 000 mots), justification de l'Écœurement Sémantique, autopsie de l'avatar de Lyra, premier interlude documentaire.

- [ ] **Step 1: Écrire le test vérifiant la densité textuelle et l'absence de tirets cadratins de l'Acte 1**

Créer `tests/test_act1_expansion.py` vérifiant que chaque chapitre de l'Acte 1 dépasse 750 mots, que le chapitre 1 dépasse 2 500 mots, et que le glossaire d'interlude est présent.

- [ ] **Step 2: Exécuter le test pour vérifier l'échec**

Run: `python -m unittest tests/test_act1_expansion.py`
Expected: FAIL (textes actuels trop courts).

- [ ] **Step 3: Rédiger les expansions des chapitres 01 à 12 et l'interlude 01**

Intégrer les dossiers d'harmonisation réels de Léonce, la démonstration clinique de l'Écœurement Sémantique au Ch. 01, la découverte du cadavre de Lyra au Ch. 03, et la descente claustrophobique du tuyau au Ch. 12.

- [ ] **Step 4: Valider avec le test et le script de tirets**

Run: `python -m unittest tests/test_act1_expansion.py && python scripts/check_dashes.py --root public/books/chronique-une-atrophie-programmee`
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add public/books/chronique-une-atrophie-programmee/0*.html public/books/chronique-une-atrophie-programmee/1*.html tests/test_act1_expansion.py
git commit -m "feat(atrophie): expansion litteraire et approfondissement clinique Acte 1"
```

---

### Task 3 : Refonte et Expansion de l'Acte 2 (Chapitres 13 à 24)

**Files:**
- Modify: `public/books/chronique-une-atrophie-programmee/13-le-reveil-brutal.html` à `24-veillee-sous-les-tenebres.html`
- Create: `public/books/chronique-une-atrophie-programmee/interlude-02-rapport-voirie-b412.html`
- Test: `tests/test_act2_expansion.py`

**Interfaces:**
- Consumes: `docs/superpowers/specs/bible-atrophie-canon.md`
- Produces: Acte 2 densifié (~12 000 mots), forge des fers de marche par Le Cliquet, rééducation clinique réelle, set piece du Grand Réfrigérant.

- [ ] **Step 1: Écrire le test vérifiant la présence des attelles métalliques et la longueur de l'Acte 2**

Créer `tests/test_act2_expansion.py` vérifiant la mention des fers de marche au Ch. 14 et que le Ch. 14 dépasse 2 200 mots.

- [ ] **Step 2: Exécuter le test pour vérifier l'échec**

Run: `python -m unittest tests/test_act2_expansion.py`
Expected: FAIL.

- [ ] **Step 3: Rédiger les expansions des chapitres 13 à 24 et l'interlude 02**

Intégrer la fabrication des attelles de fer articulées de Léonce, la défaillance des otolithes vestibulaires au Ch. 14, la description exhaustive de la bibliothèque clandestine de Barnabé au Ch. 16, et l'épopée mécanique de la turbine de Saint-Denis (Ch. 21-23).

- [ ] **Step 4: Valider avec le test et `check_dashes.py`**

Run: `python -m unittest tests/test_act2_expansion.py && python scripts/check_dashes.py --root public/books/chronique-une-atrophie-programmee`
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add public/books/chronique-une-atrophie-programmee/1*.html public/books/chronique-une-atrophie-programmee/2*.html tests/test_act2_expansion.py
git commit -m "feat(atrophie): expansion Acte 2 avec les fers de marche et la reeducation clinique"
```

---

### Task 4 : Refonte et Expansion de l'Acte 3 (Chapitres 25 à 36)

**Files:**
- Modify: `public/books/chronique-une-atrophie-programmee/25-la-derive-des-signaux.html` à `36-le-basculement.html`
- Create: `public/books/chronique-une-atrophie-programmee/interlude-03-dossier-tristan-syndic.html`
- Test: `tests/test_act3_expansion.py`

**Interfaces:**
- Consumes: Actes 1 et 2 validés
- Produces: Acte 3 densifié (~12 000 mots), le dilemme moral de Tristan, le grand chapitre-pilier du banquet (Ch. 32), l'aveu de Léonce approfondi.

- [ ] **Step 1: Écrire le test de validation de l'Acte 3**

Créer `tests/test_act3_expansion.py` vérifiant le dossier secret de Tristan et la longueur du Ch. 32 (> 2 500 mots).

- [ ] **Step 2: Exécuter le test pour vérifier l'échec**

Run: `python -m unittest tests/test_act3_expansion.py`
Expected: FAIL.

- [ ] **Step 3: Rédiger les expansions des chapitres 25 à 36 et l'interlude 03**

Donner une consistance tragique aux confidences de Barnabé (Ch. 26), développer le grand banquet nocturne des Rétifs (Ch. 32), approfondir la confession de Léonce sur la mise à mort administrative du père de Tristan (Ch. 35) et sceller le schisme moral de Tristan (Ch. 36).

- [ ] **Step 4: Exécuter les tests de conformité**

Run: `python -m unittest tests/test_act3_expansion.py && python scripts/check_dashes.py --root public/books/chronique-une-atrophie-programmee`
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add public/books/chronique-une-atrophie-programmee/2*.html public/books/chronique-une-atrophie-programmee/3*.html tests/test_act3_expansion.py
git commit -m "feat(atrophie): expansion Acte 3, banquet des retifs et schisme de Tristan"
```

---

### Task 5 : Refonte et Expansion de l'Acte 4 (Chapitres 37 à 48)

**Files:**
- Modify: `public/books/chronique-une-atrophie-programmee/37-au-fond-du-gouffre.html` à `48-la-fin-et-les-retifs.html`
- Create: `public/books/chronique-une-atrophie-programmee/interlude-04-liturgie-du-frisson.html`
- Test: `tests/test_act4_expansion.py`

**Interfaces:**
- Consumes: Actes 1 à 3 validés
- Produces: Acte 4 densifié (~14 000 mots), hécatombe civile montrée, Tristan piégé par le Frisson Divin, veillée funèbre de Barnabé sur scène.

- [ ] **Step 1: Écrire le test vérifiant la présence de Tristan dans le Frisson et la veillée de Barnabé**

Créer `tests/test_act4_expansion.py` vérifiant que Tristan est mentionné aux Ch. 46-47 et que les derniers chapitres rendent compte des victimes réelles du pollen.

- [ ] **Step 2: Exécuter le test pour vérifier l'échec**

Run: `python -m unittest tests/test_act4_expansion.py`
Expected: FAIL.

- [ ] **Step 3: Rédiger les expansions des chapitres 37 à 48 et l'interlude 04**

Mettre en scène l'assaut de la Tour Zéphyr (Ch. 41-44), l'effet dévastateur du pollen sur les dormeurs (asphyxies, panique, Ch. 45-46), la liturgie perverse du Frisson Divin avec la chute tragique de Tristan (Ch. 47), et la mort poignante de Barnabé au milieu de ses graines (Ch. 48).

- [ ] **Step 4: Exécuter les tests et `check_dashes.py`**

Run: `python -m unittest tests/test_act4_expansion.py && python scripts/check_dashes.py --root public/books/chronique-une-atrophie-programmee`
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add public/books/chronique-une-atrophie-programmee/3*.html public/books/chronique-une-atrophie-programmee/4*.html tests/test_act4_expansion.py
git commit -m "feat(atrophie): expansion Acte 4, chute de Tristan et liturgie du Frisson Divin"
```

---

### Task 6 : Intégration Catalogue, Synchronisation Plateforme et Tests de Release

**Files:**
- Modify: `public/books.json`
- Modify: `sw.js`
- Test: `scripts/verify-release.ps1`

**Interfaces:**
- Consumes: L'ensemble des 48 chapitres et interludes finalisés
- Produces: Déploiement en miroir de production Docker et validation release 100 % verte.

- [ ] **Step 1: Mettre à jour `public/books.json` et générer les fiches statiques**

Mettre à jour les métadonnées (nombre de mots, résumé de l'édition augmentée), puis exécuter `python scripts/build_book_pages.py`.

- [ ] **Step 2: Vérifier la compilation JSX**

Run: `node scripts/build_jsx.js --check`
Expected: [OK] 10 fichier(s) compilé(s) à jour.

- [ ] **Step 3: Vérifier l'absence totale de tirets cadratins**

Run: `python scripts/check_dashes.py --root .`
Expected: [OK] Aucun tiret cadratin ou demi-cadratin.

- [ ] **Step 4: Synchroniser vers le miroir Docker**

Run: `powershell -NoProfile -ExecutionPolicy Bypass -File scripts/sync-to-platform.ps1`
Expected: [OK] Synchronisation réussie sans régression.

- [ ] **Step 5: Valider la release complète en production locale**

Run: `powershell -NoProfile -ExecutionPolicy Bypass -File scripts/verify-release.ps1`
Expected: 100 % vert.

- [ ] **Step 6: Mettre à jour les documentations et commiter**

Mettre à jour `CHANGELOG.md`, `todo.md`, `antigravity.md` et pousser sur les dépôts source et plateforme.

```bash
git add -A
git commit -m "release: deploiement integral de Chronique d'une atrophie programmee etendue (~50k mots)"
```
