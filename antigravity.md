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
