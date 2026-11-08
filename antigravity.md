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

- Version **1.8.26** synchronisée le 08/11, cache Service Worker source `hylst-reader-v82`, build `07ddbab6e488`, SW `hylst-reader-07ddbab6e488`. 277 fichiers runtime, 11 livres, 94 chapitres, 13 URL au sitemap.
- **Chapitre XI enrichi** :
  - **Chapitre XI** (*La reconquête du trône des Rodallois*) porté à 9 089 mots de texte (17 `h2`, 23 tableaux, 2 figures, schéma vectoriel `chapitre-11-schema.svg`). Fiche technique, 5 horloges féodales, géographie d'Alliphance (12 lieux), dilemmes des quatre lois, 14 figures majeures, 8 factions et matrice relationnelle, épreuves des six preuves, règles et contre-mesures de Kharvâsh l'Équarrisseur et du contrat de fer froid, assaut du donjon et alertes, 10 issues principales et 6 secondaires, tables d'aides de jeu d6, sécurité de table.
- **Chapitres VIII, IX et X enrichis** :
  - Chapitre VIII : 7 161 mots, 11 sections, 14 tableaux, 3 figures, `chapitre-8-plan.svg` et `chapitre-8-schema.svg`.
  - Chapitre IX (*Esclavage gouri sans vergogne*) : 16 603 mots, 22 `h2`, 35 tableaux, 3 figures, plan et schéma vectoriel `chapitre-9-schema.svg`.
  - Chapitre X (*Vapeur et boulons*) : 13 885 mots, 18 `h2`, 33 tableaux, 3 figures, plan et schéma vectoriel `chapitre-10-schema.svg`.
- **Tableaux mobiles** : les 91 tableaux des chapitres VIII, IX, X et XI sont tous enveloppés dans `.chapter-table-scroll` avec `data-cols` adéquat. Aucun débordement horizontal à 390 px.
- Version **1.8.25** déployée en production (build `712e7d5f6378`, SW `hylst-reader-712e7d5f6378`).
- Catalogue à **11 livres et 94 chapitres** (105 fichiers de contenu).
- Livre ***Nightprowler, carnets de Samarande*** : chapitres VIII, IX, X et XI enrichis au standard de publication complète de campagne/convention. Prochaine étape : chapitre XII (*Pistes inachevées*).
- Miroir local synchronisé et validé sur `http://127.0.0.1:8765/books_reader/` avec build `07ddbab6e488`.

## Prochaines étapes possibles

- Enrichir le chapitre XII, *Pistes inachevées* (camp du prince démon, contrôle d'entrée, Kalaar) avec tables d'exploration, dangers, factions et schémas vectoriels.
- Enrichir le chapitre XIII, *Annexes* (lexique, chronologie, aides de jeu).
- Refactorisation CSS et allègement de `base.css`.
- Export `.json` de la bibliothèque importée.
- Preset de lecture longue avec réduction automatique des animations.
- Refactorisation CSS et allègement de `base.css`.
- Export `.json` de la bibliothèque importée.
- Preset de lecture longue avec réduction automatique des animations.
- Refactorisation CSS et allègement de `base.css`.
- Export `.json` de la bibliothèque importée.
- Preset de lecture longue avec réduction automatique des animations.
