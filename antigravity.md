# La Bibliothèque de Hylst - Mémoire projet et consignes agents

## Stack réelle (04/11/2026)

- **Frontend** : HTML, CSS Vanilla, React 18.3.1 et ReactDOM 18.3.1 servis depuis `vendor/`. Les sources JSX de `js/` sont précompilées vers `js/dist/` par `scripts/build_jsx.js` avec le runtime React classique.
- **Babel** : outil de build uniquement, dans `scripts/vendor/babel.min.js`. Il n'est ni chargé par `index.html`, ni copié dans le miroir de production.
- **Hors ligne** : Service Worker maison `sw.js`, précache de l'app shell, de `public/books.json`, de 10 introductions et 82 chapitres (92 fichiers de contenu), des 10 couvertures actives et des 10 fiches statiques. Stockage local via `idb-keyval` et IndexedDB. Pas de Vite, pas de Dexie, pas de localForage.
- **Polices** : `/assets/fonts/fonts.css` sur la plateforme. **Musique** : `/hml/` en chemins relatifs.
- **Test local** : compiler, synchroniser, puis servir `D:\0CODE\AntiGravity\Cours_Memos\Docker` sur `http://127.0.0.1:8765/books_reader/`.

## Règles critiques

1. **Sources des livres** : les fichiers HTML de `public/books/l-odyss-e-de-l-ia-2-futurs-un-choix/` sont la source de vérité. Ne jamais les régénérer automatiquement. Les corrections se font manuellement, fichier par fichier.
2. **Zéro tiret long** : aucun tiret cadratin ou demi-cadratin dans les contenus servis. Contrôle obligatoire avec `python scripts/check_dashes.py --root .`.
3. **Aucun CDN au runtime** : React, JSZip, epub.js, DOMPurify et idb-keyval sont locaux. Les polices et la musique sont servies par la plateforme, en same-origin.
4. **CSP** : `script-src 'self'`. Ne jamais ajouter de script inline dans `index.html`, `droits.html` ou les fiches. Externaliser dans `js/` et déclarer le fichier dans `sw.js`.
5. **Service Worker** : ne supprimer que les caches préfixés `hylst-reader-`. Le stockage `caches` est partagé par toute l'origine `hylst.fr`.
6. **Miroir de production** : `scripts/sync-to-platform.ps1` préserve l'`index.html` de production et régénère `js/dist`. Ne jamais écraser l'index de production avec l'index source.
7. **Build JSX** : `node scripts/build_jsx.js` puis `node scripts/build_jsx.js --check`. Le sync exécute les deux et refuse une sortie périmée.
8. **301** : `/books_reader/livres/<id>` redirige vers `/books_reader/livres/<id>/` avec query conservée. Configuration dans `Cours_Memos/Docker/nginx-coolify-reference.conf`, base Coolify et conteneur `hylst-cours`.
9. **Documentation** : après chaque version, mettre à jour `CHANGELOG.md`, `todo.md`, ce fichier, et côté plateforme `changelog.md`, `securite.md`, `todo.md` et `hylst_IT_platform_content.md`.
10. **Textes de tiers (corpus Nightprowler)** : ne jamais reproduire l'Atlas de Bejofa (Letorve), le texte original des règles de combat de Mathieu Mazzoni ni l'aide à la description (Hirrinkaël). Le chapitre VI publie la version personnelle de l'auteur, inspirée de Mazzoni, pas une reproduction ; le chapitre VII suit la même règle. L'aide à la description est réécrite sous le nom de l'auteur et signalée comme provisoire par une note `chapter-source-note`. Les sources sont dans `D:\0HYLST\0 HYLST ART 2024\ecrits\`, encodage cp1252, balisage très dégradé : extraire un texte UTF-8 propre avant toute rédaction et vérifier chaque liste mot par mot, jamais depuis une sortie de console tronquée.
11. **Sitemap** : il vit uniquement dans le miroir, `D:\0CODE\AntiGravity\Cours_Memos\Docker\books_reader\sitemap.xml`. `sync-to-platform.ps1` met à jour les `lastmod` et complète automatiquement les fiches de livres déclarées dans `public/books.json` ; toute nouvelle fiche doit quand même être vérifiée après synchronisation.
12. **Illustrations de chapitre** : les images vivent dans le dossier du livre, référencées en chemin relatif, et s'affichent via `<figure class="chapter-cover">`. La génération se fait sur le GPU local avec `D:/0CODE/ClaudeCode/wainsfw/main.py` (modèle `z-image-turbo-sdcpp`, sorties WebP 1216×832), jamais via OpenRouter, dont les crédits image sont épuisés.

## État actuel

- Version **1.8.50** déployée le 09/11, cache Service Worker source `hylst-reader-v99`, build `b0bcfcc94ccb`, SW `hylst-reader-b0bcfcc94ccb`. 409 fichiers runtime, 12 livres, 160 chapitres (52 pour Atrophie dont 4 interludes documentaires), 14 URL au sitemap. `verify-release.ps1` entièrement vert en production.
- **Refonte intégrale et expansion pessimiste d'*Atrophie* (édition 67 100 mots)** : volumétrie triplée (passage de 21 750 à 67 106 mots), intégration de 4 chapitres-piliers (2 500 à 3 700 mots), 4 interludes documentaires S.Y.N.D.I.C., Fers de marche articulés de Léonce (4,5 kg par jambe), Écœurement Sémantique, hécatombe civile du pollen et chute tragique de Tristan sous le Frisson Divin. Zéro tiret cadratin ou demi-cadratin.
- Version **1.8.49** déployée le 09/11, cache Service Worker source `hylst-reader-v99`, build `a4765c3db052`, SW `hylst-reader-a4765c3db052`. 405 fichiers runtime, 12 livres, 156 chapitres, 14 URL au sitemap. `verify-release.ps1` entièrement vert en production.
- **Enrichissement de Nightprowler XII (Pistes inachevées)** : schéma vectoriel triptyque `chapitre-12-schema.svg` (1200×800) et intégration de trois tables techniques d6 de jeu (complications au campement, incidents de herse, périls de Kalaar).
- Version **1.8.48** déployée le 09/11, cache Service Worker source `hylst-reader-v99`, build `e309f3d1a65c`, SW `hylst-reader-e309f3d1a65c`. 404 fichiers runtime, 12 livres, 156 chapitres, 14 URL au sitemap. `verify-release.ps1` entièrement vert en production.
- **Régénération intégrale des 48 illustrations d'Atrophie avec Flux 3 Klein** : les 48 chapitres disposent désormais d'illustrations haute fidélité avec décors détaillés et ambiance 35mm, zéro texte (audit Tesseract 0 violation sur 48/48), cache-busting forcé `?v=5`.
- Version **1.8.47** déployée le 09/11, cache Service Worker source `hylst-reader-v99`, build `302aca1140ef`, SW `hylst-reader-302aca1140ef`. 404 fichiers runtime, 12 livres, 156 chapitres, 14 URL au sitemap. `verify-release.ps1` entièrement vert en production.
- **Régénération intégrale de l'Acte 2 d'Atrophie (13 à 24) avec Flux 3 Klein rehaussé** : les 12 chapitres disposent d'illustrations calibrées avec décors complets de catacombes, bibliothèque clandestine, crypte et centrale, ambiance 35mm, zéro texte (audit Tesseract 0 violation sur 12/12) et cache-busting forcé `?v=5`.
- Version **1.8.46** déployée le 09/11, cache Service Worker source `hylst-reader-v99`, build `7202b462124c`, SW `hylst-reader-7202b462124c`. 404 fichiers runtime, 12 livres, 156 chapitres, 14 URL au sitemap. `verify-release.ps1` entièrement vert en production.
- **Régénération intégrale de l'Acte 1 d'Atrophie (01 à 12) avec Flux 3 Klein rehaussé** : les 12 chapitres disposent d'illustrations calibrées avec décors complets de meulière et béton, ambiance 35mm, zéro texte (audit Tesseract 0 violation sur 12/12) et cache-busting forcé `?v=5`.
- Version **1.8.45** déployée le 09/11, cache Service Worker source `hylst-reader-v99`, build `478f3b056a27`, SW `hylst-reader-478f3b056a27`. 402 fichiers runtime, 12 livres, 156 chapitres, 14 URL au sitemap. `verify-release.ps1` entièrement vert en production.
- **Rehaussement de décor et texture 35mm Atrophie (01 et 06)** : chapitres 01 et 06 régénérés avec `flux3-klein-sdcpp` avec prompts enrichis de décor complet (béton humide, meulière, lanterne, tuyauteries), zéro texte (audit Tesseract 0 violation), cache-busting forcé `?v=5`.
- Version **1.8.44** déployée le 09/11, cache Service Worker source `hylst-reader-v99`, build `118351d10e5a`, SW `hylst-reader-118351d10e5a`. 402 fichiers runtime, 12 livres, 156 chapitres, 14 URL au sitemap. `verify-release.ps1` entièrement vert en production.
- **Régénération haute fidélité Acte 1 Atrophie avec Flux 3 Klein** : chapitres 01 à 12 régénérés avec `flux3-klein-sdcpp` (16 steps, 800x450 WebP q85), zéro texte (audit Tesseract 0 violation sur 12/12), cache-busting forcé `?v=4`.
- Version **1.8.43** déployée le 09/11 (commit plateforme `b8ddb7e1`), cache Service Worker source `hylst-reader-v99`, build `e30b4eebec9f`, SW `hylst-reader-e30b4eebec9f`. 402 fichiers runtime, 12 livres, 156 chapitres, 14 URL au sitemap. `verify-release.ps1` entièrement vert en production.
- **Enrichissement typographique Partie III Neurodiversité (chapitres 08, 09, 11)** : structuration sémantique avec sous-titres `<h2>`/`<h3>`, listes à puces `<ul><li>`, mise en valeur en gras/italique des concepts et techniques clés.
- Version **1.8.42** déployée le 09/11 (commit plateforme `c7ffcaad`), cache Service Worker source `hylst-reader-v99`, build `fc0a8a4d8d23`, SW `hylst-reader-fc0a8a4d8d23`. 402 fichiers runtime, 12 livres, 156 chapitres, 14 URL au sitemap. `verify-release.ps1` entièrement vert en production.
- **Amélioration éditoriale et typographique d'Approche de la Neurodiversité** : purge intégrale du code React TSX au chapitre 10, recollage des coupures de phrases et suppression des métadonnées OLE Word au chapitre 05, reconstitution continue des 14 stratégies aux chapitres 12, 13 et 14, maintien des chapitres 04 et 07, structuration sémantique avec titres de section `<h2>`/`<h3>` et listes ordonnées/non-ordonnées.
- Version **1.8.41** déployée le 09/11 (commit plateforme `93f50ab5`, docs `5fcb2e18`), cache Service Worker source `hylst-reader-v97`, build `90ef30d837de`, SW `hylst-reader-90ef30d837de`. 402 fichiers runtime, 12 livres, 156 chapitres (168 fichiers de contenu), 14 URL au sitemap. `verify-release.ps1` entièrement vert en production.
- **Régénération intégrale des 48 illustrations d'Atrophie avec Qwen Image 2.1 Uncensored** :
  - 48 illustrations de chapitres générées localement sur GPU RTX 5070 avec `qwen-image-21-uc-sdcpp` via `wainsfw` (format 16:9 cinématographique 1024x576, 20 steps, CFG 2.5).
  - Cohérence stricte des personnages (Léonce, Marthe, Barnabé, Le Cliquet) et des décors (clapiers délabrés, catacombes, Tour Zéphyr, centrale).
  - Zéro mention AURA, zéro cartouche anglais sur l'ensemble des 48 images (audit Tesseract à 0 violation).
  - Cache-busting forcé `?v=3` sur les 48 chapitres HTML pour purger immédiatement tout cache navigateur client.
- Version **1.8.40** déployée le 09/11 (commit plateforme `b281b8f5`, docs `adfddecb`), cache Service Worker source `hylst-reader-v96`, build `c8c8705aa1e5`, SW `hylst-reader-c8c8705aa1e5`. 402 fichiers runtime, 12 livres, 156 chapitres (168 fichiers de contenu), 14 URL au sitemap. `verify-release.ps1` entièrement vert en production.
- **Restauration intégrale d'Approche de la Neurodiversité & Cache-busting Atrophie** :
  - Restauration intégrale sans troncature des 16 chapitres de l'anthologie (19 272 mots, extraction exhaustive de `Lettre d'un dyspraxique` 120 paras, `Chaos organisé` 62 paras, `Marre d'apprendre` 67 paras, `Labyrinthe des idées` 275 paras, `Les cinq familles` 143 paras de `troubles dys.odt`, et les 13 béquilles complètes).
  - Préservation du style asymétrique, humain et alambiqué de l'auteur.
  - Cache-busting forcé `?v=2` sur toutes les balises d'images d'Atrophie pour forcer la purge des anciens visuels avec mention AURA dans les navigateurs clients.
- Version **1.8.39** déployée le 09/11 (commit plateforme `0bda8cbb`, docs `06dbb4f9`), cache Service Worker source `hylst-reader-v95`, build `20cdd2868200`, SW `hylst-reader-20cdd2868200`. 402 fichiers runtime, 12 livres, 156 chapitres (168 fichiers de contenu), 14 URL au sitemap. `verify-release.ps1` entièrement vert en production.
- **Régénération locale sur GPU des illustrations d'Atrophie (zéro mention AURA)** :
  - 10 nouvelles illustrations d'ambiance générées avec Krea-2-Turbo (`krea-2-turbo-sdcpp`) sur GPU RTX 5070 via `wainsfw`.
  - Élimination intégrale du mot AURA et des titrages anglais sur les 48 chapitres de *Chronique d'une atrophie*. Tesseract OCR à 0 violation.
- Version **1.8.38** déployée le 09/11 (commit plateforme `50e4d3a1`, docs `7e1778b4`), cache Service Worker source `hylst-reader-v94`, build `bbbd652d6381`, SW `hylst-reader-bbbd652d6381`. 402 fichiers runtime, 12 livres, 156 chapitres (168 fichiers de contenu), 14 URL au sitemap.
- **Pied de page mobile & Transparence éthique IA** :
  - Déplacement de `<footer className="app-footer">` à l'intérieur du conteneur de défilement `<main className="library-container">`. Fini le pied de page flottant qui prenait 1/4 d'écran sur smartphone : il est désormais accessible naturellement tout en bas de page.
  - Mentions éthiques de l'assistance IA affinées :
    - *Approche de la Neurodiversité* : relecture assistée par IA pour corriger coquilles et lourdeurs d'expression d'écrits 2003-2025, illustrations d'ouverture Krea locales.
    - *Chronique d'une atrophie programmée* : écriture manuelle originelle jusqu'aux 2/3, puis assistance IA pour structuration, corrections, brainstorming, recherches et illustrations d'ambiance.
- Version **1.8.37** déployée le 09/11 (commit plateforme `6fd89cdc`, docs `691ada2e`), cache Service Worker source `hylst-reader-v93`, build `59670cfcb111`, SW `hylst-reader-59670cfcb111`. 402 fichiers runtime, 12 livres, 156 chapitres (168 fichiers de contenu), 14 URL au sitemap. `verify-release.ps1` entièrement vert en production.
- **Anthologie intégrale d'*Approche de la Neurodiversité* (16 chapitres, 2003-2025)** :
  - Intégration exhaustive des écrits de terrain de l'auteur sur 22 ans (site `hylst.fr/neurodivers/` et manuscrits d'archives).
  - 4 mouvements : I. Confessions & Vécus (Lettre d'un dyspraxique mars 2003, Chaos 2005/2024, Pensée en ébullition 2024), II. Enfance & École (Neurodiversité enfant 2023, Difficulté scolaire, Pas-à-pas avec SVG 2, Marre d'apprendre ! 2025), III. Anatomie des cerveaux (5 familles avec SVG 1, Mémoire 2024, Labyrinthe des idées 2024, Cerveau danse 2025), IV. Boîte à béquilles (13 stratégies avec SVG 3, Conditionnement, Esprit embrumé), Prologue et Épilogue.
  - Style asymétrique, humain et alambiqué d'auteur préservé.
  - 3 schémas vectoriels SVG interactifs et 4 illustrations locales GPU Krea-2-Turbo.
  - Catalogue et fiche statique à 16 entrées, période `2003-2025 (compilation 2026)`.
- Version **1.8.36** déployée le 09/11 (commit plateforme `30c72d7b`, docs `d3c9ff9c`), cache Service Worker source `hylst-reader-v92`, build `b4a05e753aea`, SW `hylst-reader-b4a05e753aea`. 399 fichiers runtime, 12 livres, 153 chapitres (165 fichiers de contenu), 14 URL au sitemap. `verify-release.ps1` entièrement vert en production.
- **Édition intégrale d'*Approche de la Neurodiversité* (Recueil thématique en 3 parties, 13 chapitres)** :
  - Consolidation des 3 textes d'archives (2018-2022) : Partie I (Anatomie des décalages, 5 familles dys d'après `troubles dys.odt`), Partie II (L'Enfance et l'École, guide d'accompagnement d'après `Enfants en difficulté scolaire.doc`), Partie III (La Boîte à Béquilles, 13 stratégies concrètes de l'adulte d'après `Idées pour lutter...pdf`).
  - 3 schémas vectoriels SVG interactifs créés : `neuro-schema-1-familles.svg`, `neuro-schema-2-pedagogie.svg`, `neuro-schema-3-bequilles.svg`.
  - 4 illustrations d'art éditorial générées localement sur GPU RTX 5070 (Krea-2-Turbo) : `partie-1-couverture.webp`, `partie-2-couverture.webp`, `partie-3-couverture.webp`, `epilogue-couverture.webp`.
  - Sommaire étendu à 13 entrées avec Prologue et Épilogue pour une navigation linéaire complète. Fiche statique regénérée.
- Version **1.8.35** déployée le 09/11 (commit plateforme `ac6cabe3`, docs `1c7b8b45`), cache Service Worker source `hylst-reader-v91`, build `f45d0fcef3ea`, SW `hylst-reader-f45d0fcef3ea`. 385 fichiers runtime, 12 livres, 146 chapitres (158 fichiers de contenu), 14 URL au sitemap. `verify-release.ps1` entièrement vert en production.
- **Cadrage des vignettes et élimination d'AURA** :
  - `.chapter-figure` calibré sous `css/reader.css` (`max-width: 480px; max-height: 280px; object-fit: cover`) évitant le débordement plein écran sur la lecture.
  - Élimination des bandeaux anglais et des mentions « AURA » sur les 48 illustrations de chapitres.
  - Rectification de la datation d'*Approche de la Neurodiversité* : rédaction de **2018 à 2022** (mise en ligne en 2026).
- Version **1.8.34** déployée le 09/11 (commit plateforme `0d7b368b`, docs `ff0ac19d`), cache Service Worker source `hylst-reader-v90`, build `31530bf4ee27`, SW `hylst-reader-31530bf4ee27`. 385 fichiers runtime, 12 livres, 146 chapitres (158 fichiers de contenu), 14 URL au sitemap. `verify-release.ps1` entièrement vert en production.
- **Publication du 12ᵉ livre : *Chronique d'une atrophie programmée*** :
  - Roman complet en 48 chapitres et 4 actes (20 105 mots).
  - Éradication des clichés d'IA (AURA, Léo, Silas, Anya, Glitch, Marcus le clone) au profit de Léonce l'Ajusteur / Plisseur de mots, Barnabé Pépé Rature, Marthe la Râpe, Le Cliquet, Tristan et l'Intendance du S.Y.N.D.I.C.
  - Style asymétrique, débridé et satirique d'auteur (onomatopées, folie humaine, viscéralité de la chair).
  - Twist satirique du « Frisson Divin » (dopamine + histamine) scrupuleusement conservé.
  - 48 illustrations WebP locales auditées et intégrées.
  - Retrait de `f17` des livres futurs, 12 fiches statiques générées.
- Version **1.8.33** déployée le 08/11 (commit plateforme `a8ad11a5`, docs `fd1da5b4`), cache Service Worker source `hylst-reader-v89`, build `da7807980fa5`, SW `hylst-reader-da7807980fa5`. 286 fichiers runtime, 11 livres, 98 chapitres (109 fichiers de contenu), 13 URL au sitemap. `verify-release.ps1` entièrement vert en production.
- **Ajustements tomes de poésie** :
  - Terme « club d'écrivains » remplacé par « club / groupe d'écriture » (amateurs non professionnels pour le plaisir et le challenge créatif).
  - Datation du Tome III (*Cœurs, chaos & quotidien*) étendue à `1995-2024` (textes initiés dès 1995 comme pour le Tome I).
  - Vérification des textes d'archives : confirmation que *Effet papillon* (Tome III-01), *Ariane* (Tome III-02) et *Le rêve d'un gaijin profane* (Tome II-01) sont déjà en ligne.
- Version **1.8.32** déployée le 08/11 (commit plateforme `2f2d3269`, docs `7184e940`), cache Service Worker source `hylst-reader-v88`, build `b6d90941bf41`, SW `hylst-reader-b6d90941bf41`. 286 fichiers runtime, 11 livres, 98 chapitres (109 fichiers de contenu), 13 URL au sitemap. `verify-release.ps1` entièrement vert en production.
- **Genèse et provenance des 3 tomes de poésie** :
  - Explicitation de la chaîne de création : rédigés sur le blog Joueb (*Pour la parole et pour le plaisir* sous la plume Hylst), revus en 1999-2000 pour le 2e site web personnel, prolongés en 2021 dans les *Fantasques du Bocal*, accompagnés d'affiches/couvertures originales en 2024, compilés en recueils en 2026.
  - Mises à jour des introductions de Tomes I, II, III et des mentions `illustrationNote`. Fiches statiques regénérées.
- Version **1.8.31** déployée le 08/11 (commit plateforme `4acec827`, docs `8da8b6e3`), cache Service Worker source `hylst-reader-v87`, build `a268efd0d8b6`, SW `hylst-reader-a268efd0d8b6`. 286 fichiers runtime, 11 livres, 98 chapitres (109 fichiers de contenu), 13 URL au sitemap. `verify-release.ps1` entièrement vert en production.
- **Transparence des dates et mentions IA** :
  - Dissociation des périodes de rédaction réelle (100 % de l'auteur) et de l'année de compilation numérique 2026 : *Nightprowler* (1999-2011), *Carnets* (1994-2024), *Sciences* (2001-2002), *Saisons* (1999-2024), *Fantasque* (1999-2026), *Cœurs* (2021-2024).
  - Ligne dédiée `.illustration-note` ajoutée sur les fiches statiques et dans l'app, précisant le remplacement des illustrations par des générations IA locales en 2026 pour Nightprowler, et la présence des figures authentiques pour Sciences.
- Version **1.8.30** déployée le 08/11 (commit plateforme `687c843d`, docs `328e9bfa`), cache Service Worker source `hylst-reader-v86`, build `1939c2d25914`, SW `hylst-reader-1939c2d25914`. 286 fichiers runtime, 11 livres, 98 chapitres (109 fichiers de contenu), 13 URL au sitemap. `verify-release.ps1` entièrement vert en production.
- **Tome IV (*Carnets, réflexions & partages*) — Réflexions de jeunesse (1994-1998)** :
  - Intégration en tête de volume de 3 chapitres fondateurs : *I. De l'art et de la demoscene informatique* (vers 1996), *II. De l'édenisme et de la quête d'équilibre* (vers 1996-1998), *III. Éloge du temps libre et de l'éveil* (vers 1998).
  - Décalage des chapitres existants de 01-04 vers 04-07 (7 textes au total, période 1994-2024). Fiche statique regénérée.
- Version **1.8.29** déployée le 08/11 (commit plateforme `c80b771b`, docs `0e4445fd`), cache Service Worker source `hylst-reader-v85`, build `514f57879866`, SW `hylst-reader-514f57879866`. 283 fichiers runtime, 11 livres, 95 chapitres (106 fichiers de contenu), 13 URL au sitemap. `verify-release.ps1` entièrement vert en production.
- **Sciences et technologie (*Analyse des solutions techniques mises en œuvre dans les jeux vidéos*)** :
  - Date d'archive corrigée à `2001-2002` dans `public/books.json` et sur la fiche statique (au lieu de 2026 erroné).
  - Genèse explicitée : intérêt pour les capteurs et l'optique né dès 1994 en Terminale STL (Physique de laboratoire), formalisé en 5e année d'ingénieur NFIO optronique en 2001-2002.
  - Renommage de « Préface 2026 » en « Préface de l'auteur ».
  - Intégration de 5 illustrations d'archives authentiques de 2001 extraites des fichiers Word originaux (Power Glove, CyberGlove, visiocasque VR, traqueur Polhemus 3Space).
- Version **1.8.28** déployée le 08/11 (commit plateforme `7c69dc42`, docs `44ac5c69`), cache Service Worker source `hylst-reader-v84`, build `7665440676e7`, SW `hylst-reader-7665440676e7`. 278 fichiers runtime, 11 livres, 95 chapitres (106 fichiers de contenu), 13 URL au sitemap. `verify-release.ps1` entièrement vert en production.
- **Tome II (*Fantasque & merveilleux*) — Chapitre 05 (*Le pantin et la poupée de cire*)** :
  - Conte poétique inédit écrit en novembre 2021 lors du défi *Nouvember 2021*, formant diptyque avec le chapitre 04 (*Le précieux pantin de bois*).
  - Premier volet original scrupuleusement conservé mot à mot.
  - Scène médiane complétée en vers libres d'après les notes préparatoires de l'auteur (minuit au pendule d'argent, boîte à musique en fer blanc, danse et marelle sur le parquet, impétuosité d'un baiser timide, chaleur de la bougie et larme de cire fondue).
  - Poème final de 5 strophes textuellement préservé.
  - Chapitres 05 à 10 décalés vers 06 à 11. Recueil porté de 10 à 11 textes. Fiche statique regénérée.
- Version **1.8.27** déployée le 08/11 (commit plateforme `256085f7`, docs `48005aec`), cache Service Worker source `hylst-reader-v83`, build `ffbc6d92d427`, SW `hylst-reader-ffbc6d92d427`. 277 fichiers runtime, 11 livres, 94 chapitres, 13 URL au sitemap. `verify-release.ps1` entièrement vert en production.
- **Chapitre XIII (Annexes) refondu et complété** :
  - 3 060 mots de texte, 6 `h2`, 10 `h3`, 17 tableaux tous enveloppés dans `.chapter-table-scroll`.
  - Feuille de personnage normalisée et accessible.
  - Lexique étendu à 45 entrées attestées couvrant la totalité des scénarios et provinces (Azefhfkrijiiir, Bromi, Kharvâsh, Main de Cendre, Veilleurs, Marques, La Verte, Bief, Pierre de rosette, Quartier 30, Hautes Lices, Double 7, etc.).
  - Chronologie des campagnes (1500, 2258, 2300, 2310, 2476, 2557, 2558, 2559).
  - Recueil de 16 termes d'argot des coupe-bourses de Samarande et deux tables d6 de péripéties urbaines.
- **Humanisation stylistique des scénarios VIII, IX, X et XI** :
  - Écriture plus organique, vivante, avec verve d'auteur, phrases alambiquées, pointes d'ironie mordante et descriptions viscérales.
- **Chapitre XII (Pistes inachevées)** : 4 tableaux enveloppés dans `.chapter-table-scroll` avec `data-cols="3"`.
- **Tableaux mobiles** : l'intégralité des 95 tableaux des chapitres VIII à XIII sont désormais tous enveloppés dans `.chapter-table-scroll` avec `data-cols` exact. Zéro débordement horizontal à 390 px.
- Version **1.8.26** déployée en production (build `07ddbab6e488`, SW `hylst-reader-07ddbab6e488`).
- Catalogue à **11 livres et 94 chapitres** (105 fichiers de contenu).
- Livre ***Nightprowler, carnets de Samarande*** : entièrement achevé, enrichi, humanisé et doté d'annexes exhaustives. Prochaine étape : enrichissement du chapitre XII (*Pistes inachevées*).
- Miroir local synchronisé et validé sur `http://127.0.0.1:8765/books_reader/` avec build `ffbc6d92d427`.

## Prochaines étapes possibles

- Enrichir le chapitre XII, *Pistes inachevées* (camp du prince démon, contrôle d'entrée, Kalaar) avec tables d'exploration, dangers, factions et schémas vectoriels.
- Refactorisation CSS et allègement de `base.css`.
- Export `.json` de la bibliothèque importée.
- Preset de lecture longue avec réduction automatique des animations.
- Refactorisation CSS et allègement de `base.css`.
- Export `.json` de la bibliothèque importée.
- Preset de lecture longue avec réduction automatique des animations.
- Refactorisation CSS et allègement de `base.css`.
- Export `.json` de la bibliothèque importée.
- Preset de lecture longue avec réduction automatique des animations.
- Refactorisation CSS et allègement de `base.css`.
- Export `.json` de la bibliothèque importée.
- Preset de lecture longue avec réduction automatique des animations.
