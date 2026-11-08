# Changelog
Toutes les modifications notables apportées au projet **La Bibliothèque de Hylst** sont documentées dans ce fichier.

## [1.8.29] - 2026-11-08

### Modifié
- **Sciences et technologie (*Analyse des solutions techniques mises en œuvre dans les jeux vidéos*)** :
  - **Correction de la date d'archive** : attribution de l'année réelle `2001-2002` dans `public/books.json` et sur la fiche statique (en remplacement de la date erronée `2026` qui laissait supposer un ouvrage contemporain).
  - **Précision de la genèse** : explicitation dans la préface et l'introduction de la filiation de l'étude, dont l'intérêt pour les capteurs, l'optique et l'instrumentation physique est né dès 1994 sur les bancs de Terminale STL (Physique de laboratoire), avant d'être nourri et formalisé en 5e année d'école d'ingénieurs (NFIO optronique, promotion 7) en 2001-2002.
  - **Titre du premier chapitre** : renommage de « Préface 2026 » en « Préface de l'auteur » pour lever tout anachronisme de présentation.
  - **Illustrations d'archives authentiques (2001-2002)** : extraction directe et conversion en WebP optimisé de 5 figures et photographies historiques majeures issues des documents Word originaux de l'auteur pour orner les en-têtes de chapitres de la liseuse :
    - *Préface de l'auteur* : figure de couverture d'origine (gant de données et capture spatiale du squelette 3D de la main).
    - *Partie A* : le Power Glove de Mattel, interface manuelle pionnière à résistances variables.
    - *Partie B* : bras maître exosquelette robotique à retour d'effort mécanique et couplage haptique.
    - *Partie C* : visiocasque stéréoscopique Virtual Research à écrans LCD miniaturisés et écouteurs binauraux.
    - *Partie D* : système de localisation spatiale à 6 degrés de liberté Polhemus 3Space UltraTrak.
  - **Clarification des documents complets** : mention explicite que la liseuse présente la mise en perspective analytique, le sommaire et les figures d'archives clés, tandis que l'étude intégrale et ses 159 planches illustrées d'époque restent téléchargeables dans les 4 fichiers PDF d'origine.
- **Service Worker** : passage à la version source `hylst-reader-v85` dans `sw.js`. Précache automatique des 5 nouvelles illustrations WebP.
- **Fiche statique** : regénération de `livres/sciences-et-technologie-jeux-videos/index.html` affichant l'année `2001-2002` et « Préface de l'auteur ».

### Vérifié
- `python scripts/check_dashes.py --root .` : 133 fichiers contrôlés, zéro tiret long.
- `node scripts/build_jsx.js --check` : 10 fichiers JSX compilés et à jour.
- `node scripts/test-sw-policy.js` : 6/6 tests de politique Service Worker validés.
- Validation DOM des 5 chapitres de *Sciences et technologie* : balises HTML équilibrées, 0 erreur.
- Rendu visuel mobile 390 px inspecté et validé via Chrome headless avec affichage net des figures d'archives.
- Synchronisation miroir (`scripts/sync-to-platform.ps1 -Prune`) : build `514f57879866`, 283 fichiers runtime vérifiés.
- Serveur local `http://127.0.0.1:8765/books_reader/` : HTTP 200 sur index, SW, fiches, chapitres et les 5 illustrations WebP.
- Production : déployée le 08/11 (commit plateforme `c80b771b`, docs `0e4445fd`), build `514f57879866`, SW `hylst-reader-514f57879866`, index `?v=514f57879866`. `verify-release.ps1` entièrement vert : build cohérent, 13 URL, 11 fiches, 301, CSP meta et Nginx, `.env` 403, sources 404. Fiche statique en `<p class="year">2001-2002</p>` et illustrations d'archives en 200 sur le domaine de production.

## [1.8.28] - 2026-11-08

### Ajouté
- **Tome II (*Fantasque & merveilleux*) — Chapitre 05 : *Le pantin et la poupée de cire*** : intégration d'un conte poétique inédit rédigé en novembre 2021 lors d'un défi littéraire (*Nouvember 2021*), retrouvé dans les archives personnelles de l'auteur. Le texte forme un diptyque narratif direct avec *Le précieux pantin de bois* (chapitre 04) dont il compose le pendant féerique et nocturne dans l'échoppe de jouets traditionnels de l'ancienne ruelle des Jouvenceaux.
  - *Premier volet* : texte manuscrit d'origine intégralement préservé (l'éveil nocturne, le pendule d'argent, la boîte d'allumettes, la haute bougie coquelicot, la traversée acrobatique de la boutique et l'arrivée devant la poupée de cire).
  - *Scène médiane complétée* : prose poétique cadencée en vers libres épousant le souffle et le rythme ternaire du manuscrit, développant les notes d'étape de l'auteur (les douze coups de minuit au pendule, le réveil d'une boîte à musique en fer blanc, le jeu d'ombres projeté sur les boiseries, la danse et la marelle enchantée, l'impétuosité d'un baiser timide et la tragédie de la chaleur qui fait naître une première larme de cire fondue).
  - *Poème final* : poème original complet de 5 strophes d'alexandrins et décasyllabes préservé mot à mot (*L'aube ouvre son regard, lisse sa chevelure... Un sanglot de cire se suspend à la lune / Une larme volée au cœur d'une poupée*).
  - Volume du conte : 1 557 mots, balisage HTML sémantique avec classes `poem-stanza`.

### Modifié
- **Tome II (*Fantasque & merveilleux*)** :
  - Décalage ordonné des chapitres 05 à 10 existants vers les positions 06 à 11 (`06-ondes-positives`, `07-intermede-feerique`, `08-dangaord`, `09-metro-fantasque`, `10-farouches-apparitions`, `11-la-taniere-du-mage`).
  - Le recueil passe de 10 à **11 textes** (de 1999 à 2026).
  - Mise à jour de `intro.html` pour présenter les 11 textes et expliciter le diptyque des pantins de l'artisan.
  - Mise à jour du catalogue `public/books.json` (11 chapitres, métadonnées, dates et chemins alignés).
  - Fiche statique `livres/recueils-proses-poesies-t2-fantasque-merveilleux/index.html` regénérée via `scripts/build_book_pages.py`.
- **Catalogue global** : La Bibliothèque de Hylst compte désormais **11 livres et 95 chapitres** (106 fichiers de contenu).
- **Service Worker** : incrémentation du cache source vers `hylst-reader-v84` dans `sw.js`.
- **Typographie et responsive** : zéro tiret cadratin ou demi-cadratin sur les 133 fichiers contrôlés (`python scripts/check_dashes.py --root .`). Rendu desktop et mobile 390 px validé sans débordement horizontal.

- **Version** : 1.8.28, build `7665440676e7`.

### Vérifié
- `python scripts/check_dashes.py --root .` : 133 fichiers contrôlés, zéro tiret long.
- `node scripts/build_jsx.js --check` : 10 fichiers JSX compilés et à jour.
- `node scripts/test-sw-policy.js` : 6/6 tests de politique Service Worker validés.
- Validation des 11 chapitres de Tome II : balises HTML équilibrées, 0 erreur DOM, métadonnées `books.json` synchronisées.
- Rendu visuel desktop (1440 px) et mobile (390 px) inspecté et validé via Chrome headless.
- Synchronisation miroir (`scripts/sync-to-platform.ps1 -Prune`) : build `7665440676e7`, 278 fichiers runtime vérifiés, 6 fichiers orphelins décalés purgés proprement du miroir.
- Serveur local `http://127.0.0.1:8765/books_reader/` : HTTP 200 sur index, SW, fiches, chapitres 01 à 11.
- Production : déployée le 08/11 (commit plateforme `7c69dc42`, docs `44ac5c69`), build `7665440676e7`, SW `hylst-reader-7665440676e7`, index `?v=7665440676e7`. `verify-release.ps1` entièrement vert : build cohérent, 13 URL, 11 fiches, 301, CSP meta et Nginx, `.env` 403, sources 404. Chapitre 05 et fiche Tome II en 200 sur le domaine de production.

## [1.8.27] - 2026-11-08

### Modifié
- **Chapitre XIII (Annexes)** : refonte complète et enrichissement de la section finale de *Nightprowler, carnets de Samarande*. Les 14 tableaux d'origine sont désormais tous enveloppés dans `.chapter-table-scroll` avec attribut `data-cols` exact. Le lexique passe de 25 à 45 entrées attestées, couvrant les entités démoniaques (Azefhfkrijiiir, Kharvâsh, rat de Bromi), les factions (Main de Cendre, Veilleurs, Marques, Ezgir, Kahlérs), les artefacts (pierre de rosette, émeraudes de focus, fer froid) et les lieux des provinces (Alliphance, Orgilaine, Lujevire, Mont-Orgueil, Hautes Lices, Quartier 30, Bief). La chronologie est étendue avec les jalons de campagne (1500, 2557, 2558, 2559). Ajout d'une table de 16 termes d'argot des coupe-bourses de Samarande et de deux tables d6 de péripéties urbaines (ambiances nocturnes et complications de coupe-gorges). Volume porté de 1 795 à 3 060 mots de texte (17 tableaux, 6 `h2`).
- **Humanisation des scénarios (Chapitres VIII à XI)** : révision stylistique vivante et organique donnant du relief d'auteur, de la verdeur, des phrases alambiquées et une pointe d'ironie mordante aux intrigues de jeu :
  - *Chapitre VIII* : détails tactiles sur la moiteur du puits, le sarcophage balancé comme une huche à pain, le cynisme bureaucratique d'Albéric et Mathilde.
  - *Chapitre IX* : accentuation de la détresse charnelle et de la folie toxique du parasite de Bromi, la fange de la rafle de la famille Migeon.
  - *Chapitre X* : portrait maniaque et tragi-comique d'Humbert Aglino renvoyé de la guilde, puanteur de suie et d'acide, horreur du broyage de vie sous le vernis du rendement alchimique.
  - *Chapitre XI* : cruauté féodale froide de Wilfried l'Impitoyable, grandiloquence juridique de l'écartèlement public, ironie mordante sur les alliances de cour.
- **Chapitre XII (Pistes inachevées)** : enveloppement systématique des 4 tableaux dans `.chapter-table-scroll` avec `data-cols="3"`.
- **Service Worker** : passage à la version source `hylst-reader-v83` (build miroir `ffbc6d92d427`).
- **Typographie et accessibilité** : zéro tiret cadratin ou demi-cadratin sur 132 fichiers source et 151 fichiers miroir. Totalité des 95 tableaux des chapitres VIII à XIII enveloppés et défilables sur écran mobile 390 px sans débordement.
- **Version** : 1.8.27, build `ffbc6d92d427`.

### Vérifié
- `python scripts/check_dashes.py --root .` : 132 fichiers contrôlés, zéro tiret long.
- `node scripts/build_jsx.js --check` : 10 fichiers JSX compilés et à jour.
- `node scripts/test-sw-policy.js` : 6/6 tests de politique du Service Worker validés.
- Validation des 6 chapitres (VIII à XIII) et des 7 SVGs : balises HTML équilibrées, 100 % des tableaux enveloppés, 0 tiret long, 0 erreur.
- Rendu visuel desktop et mobile 390 px vérifié via Chrome headless pour XIII.
- Synchronisation miroir (`scripts/sync-to-platform.ps1 -Prune`) : build `ffbc6d92d427`, 277 fichiers runtime vérifiés, zéro dossier de travail.
- Serveur local `http://127.0.0.1:8765/books_reader/` : HTTP 200 sur index, SW, fiches, chapitres 8 à 13.
- Production : déployée le 08/11 (commit plateforme `256085f7`, docs `48005aec`), build `ffbc6d92d427`, SW `hylst-reader-ffbc6d92d427`, index `?v=ffbc6d92d427`. `verify-release.ps1` entièrement vert : build cohérent, 13 URL, 11 fiches, 301, CSP meta et Nginx, `.env` 403, sources 404, aucun Babel ni JSX servi. Chapitre 13 et ses annexes complètes en 200 sur le domaine de production.

## [1.8.26] - 2026-11-08

### Modifié
- **Chapitre XI** : enrichissement majeur du scénario médiéval-fantastique sombre « La reconquête du trône des Rodallois » (1999-2004) porté de 2 762 à 9 089 mots de texte (9 302 bruts), avec 17 sections `h2`, 23 tableaux tous enveloppés dans `.chapter-table-scroll` et 2 figures. Ajout d'une fiche technique complète, de la vérité de campagne avec le démon Kharvâsh l'Équarrisseur et le contrat de fer froid, de cinq horloges de tension politique, de la géographie du royaume d'Alliphance et de ses trois provinces (12 lieux majeurs), du détail tactique de la fuite du jardin royal, des dilemmes civils de résistance sous les quatre lois, des fiches de 14 figures majeures et secondaires du royaume, d'une matrice relationnelle de 8 factions féodales, de la quête des six preuves décisives, des règles d'affrontement et de rupture du démon Kharvâsh, de l'assaut en trois temps avec tableau d'alertes de la forteresse, de 10 issues principales et 6 secondaires, d'un ensemble complet de tables d'aides de jeu d6 (rumeurs, bruits, patrouilles, reliques, Kharvâsh, dernières images), du découpage horaire de campagne et convention, et des protocoles de sécurité de table. Ajout du schéma vectoriel `chapitre-11-schema.svg` à trois panneaux (la dynastie brisée, la terreur des quatre lois, les voies du trône).
- **Service Worker** : passage à la version source `hylst-reader-v82` (build miroir `07ddbab6e488`). Le schéma vectoriel `chapitre-11-schema.svg` est automatiquement extrait du HTML et précaché pour le mode hors ligne.
- **Typographie et responsive** : zéro tiret cadratin ou demi-cadratin sur les 132 fichiers source et 151 fichiers miroir (`check_dashes.py --all`). Tous les 23 tableaux sont dotés de conteneurs défilables avec `data-cols` exact, sans débordement de page à 390 px.
- **Version** : 1.8.26, build `07ddbab6e488`.

### Vérifié
- `python scripts/check_dashes.py --root .` : 132 fichiers contrôlés, zéro tiret long.
- `node scripts/build_jsx.js --check` : 10 fichiers JSX compilés et à jour.
- `node scripts/test-sw-policy.js` : 6/6 tests de politique du Service Worker validés.
- Balises HTML équilibrées, 23 tableaux enveloppés avec `data-cols` exact, XML valide sur `chapitre-11-schema.svg` (17 393 octets).
- Rendu visuel desktop et mobile 390 px vérifié via Chrome headless (captures sans débordement, images et schémas vectoriels chargés, typographie saine).
- Synchronisation miroir (`scripts/sync-to-platform.ps1 -Prune`) : build `07ddbab6e488`, 277 fichiers runtime vérifiés, zéro dossier de travail.
- Serveur local `http://127.0.0.1:8765/books_reader/` : HTTP 200 sur index, SW, fiches, chapitre 11 et schéma SVG.
- Production : déployée le 08/11 (commit plateforme `734046f2`, docs `d45979b7`), build `07ddbab6e488`, SW `hylst-reader-07ddbab6e488`, index `?v=07ddbab6e488`. `verify-release.ps1` entièrement vert : build cohérent, 13 URL, 11 fiches, 301, CSP meta et Nginx, `.env` 403, sources 404, aucun Babel ni JSX servi. Chapitre 11 et son schéma SVG en 200 sur le domaine de production.

## [1.8.25] - 2026-11-08

### Modifié
- **Chapitre IX** : enrichissement majeur du scénario « Esclavage gouri sans vergogne » (1999-2001) porté de 3 791 à 16 603 mots de texte (16 871 bruts), avec 22 sections `h2`, 35 tableaux tous enveloppés dans `.chapter-table-scroll` et 3 figures. Ajout d'une fiche technique complète, de la vérité de campagne avec cinq horloges modulaires, du quartier des Hautes Lices (12 lieux), de l'acte I en trois scènes et options, des PNJ et des factions du camp, des dangers environnementaux, de la table des cinq émeraudes de focus divin, des trois phases du combat contre Bromi et son rat-démon, du détail des six routes d'évasion, des étapes du temple d'Azefhfkrijiiir et des aides de jeu en tables d6. Ajout du schéma vectoriel `chapitre-9-schema.svg` à trois panneaux (la chaîne, la machine économique, les six routes). Réconciliation géographique : temple situé à 1-2 km du camp dans les collines, population des Marques clarifiée (hors du contingent des 95 esclaves du camp).
- **Chapitre X** : enrichissement majeur du scénario « Vapeur et boulons » (convention des Alchimistes 2011) porté de 3 099 à 13 885 mots de texte (14 129 bruts), avec 18 sections `h2`, 33 tableaux tous enveloppés dans `.chapter-table-scroll` et 3 figures. Ajout de la fiche technique, de la vérité de campagne avec cinq horloges (machine 6, guilde 4, Kahlérs 4, Tramiel 6, ville 4), de Samarande et Bejofa (12 lieux de jeu), de la filature de l'acte III en six moments et complications, de la description pièce par pièce du moulin d'Humbert (zones A à I) avec rondes et sept voies d'approche, de la machine alchimique avec ses jauges (pression, température, réserve de vie, débit, bruit), ses dangers et ses modes d'arrêt, des quinze PNJ du moulin et de leurs profils, des huit factions et de leurs neuf relations croisées, de l'acte V en trois temps, du sort de Tramiel en quatre temps avec six routes de sauvetage, des règles et modes de destruction de la pierre de rosette, de dix issues principales et six issues secondaires, d'un tableau d'aides de jeu d6 (rumeurs, bruits, complications, objets, secrets, Nazir, visions, dernière image), du découpage horaire en quatre heures et des consignes de sécurité de table. Ajout du schéma vectoriel `chapitre-10-schema.svg` à trois panneaux (la chaîne de l'or, la machine, les dix issues).
- **Service Worker** : passage à la version source `hylst-reader-v81` (build miroir `712e7d5f6378`). Les deux nouveaux schémas vectoriels `chapitre-9-schema.svg` et `chapitre-10-schema.svg` sont automatiquement extraits des HTML de chapitre et précachés hors ligne.
- **Typographie et responsive** : zéro tiret cadratin ou demi-cadratin dans les sources et le miroir (`check_dashes.py --root .`). Tous les tableaux (35 dans IX, 33 dans X) sont dotés de la classe `.chapter-stats-table.descripteurs` sous conteneur `.chapter-table-scroll` avec attribut `data-cols` exact, garantissant une consultation mobile sans débordement de page à 390 px.
- **Version** : 1.8.25, build `712e7d5f6378`.

### Vérifié
- `python scripts/check_dashes.py --root .` : 132 fichiers contrôlés, zéro tiret long.
- `node scripts/build_jsx.js --check` : 10 fichiers JSX compilés et à jour.
- `node scripts/test-sw-policy.js` : 6/6 tests de politique du Service Worker passés avec succès.
- Validations HTML/XML : balises équilibrées sur IX et X, 68 tableaux enveloppés avec `data-cols` exact, XML valide sur `chapitre-9-schema.svg` (14 512 octets) et `chapitre-10-schema.svg` (17 615 octets).
- Rendu visuel desktop et mobile 390 px vérifié via Chrome headless (captures sans débordement, images et schémas vectoriels chargés, typographie saine).
- Synchronisation miroir (`scripts/sync-to-platform.ps1 -Prune`) : build `712e7d5f6378`, 276 fichiers runtime vérifiés, zéro dossier de travail.
- Serveur local `http://127.0.0.1:8765/books_reader/` : HTTP 200 sur index, SW, fiches, chapitres 9 et 10, plans et schémas SVG.
- Production : déployée le 08/11 (commit plateforme `f1bdfc1c`, docs `c11f3c62`), build `712e7d5f6378`, SW `hylst-reader-712e7d5f6378`, index `?v=712e7d5f6378`. `verify-release.ps1` entièrement vert : build cohérent, 13 URL, 11 fiches, 301, CSP meta et Nginx, `.env` 403, sources 404, aucun Babel ni JSX servi. Chapitres 9, 10 et leurs schémas SVG en 200 sur le domaine de production.

## [1.8.24] - 2026-11-08

### Modifié
- **Service Worker** : séparation du précache versionné et d'un cache d'exécution plafonné à 200 entrées. L'installation échoue désormais si l'app shell ou le cœur des livres est incomplet. Les téléchargements de précache font deux tentatives, les réponses autres que `200 basic` sont refusées, et les requêtes audio, vidéo et `Range` ne sont plus interceptées ni stockées. La navigation n'est jamais mise en cache et l'activation ne supprime que les caches `hylst-reader-`.
- **Stockage persistant** : `navigator.storage.persist()` est demandé après l'enregistrement du Service Worker, sans bloquer le démarrage.
- **Chapitre VIII** : enrichissement du scénario du squelette enfoui d'Azefhfkrijiiir de 3 188 à 7 161 mots de texte, avec 11 sections, 14 tableaux, 3 figures, une fiche technique, une clé des salles, les règles de possession, la table des rêves, les Veilleurs, les issues secondaires et les marques. Deux SVG ajoutés : une coupe de la salle basse et un schéma du verrou, de la possession et des issues.
- **Cohérence du chapitre VIII** : pierre gravée à 1 m, plafond à 1,10 m, drain des rêves réservé aux personnages non possédés, coût de volonté renvoyé à la table de possession, Vieille Orme témoin d'un rituel, P'tit Fer porteur de remplacement, résultats du d6 alignés sur leurs descriptions.
- **Tableaux mobiles** : les tableaux de chapitre sont enveloppés dans un conteneur défilable, avec une largeur minimale adaptée au nombre de colonnes. La page ne déborde plus à 390 px et les tableaux à quatre colonnes restent lisibles par défilement horizontal.
- **Polices** : suppression des cinq doublons Outfit de `public/fonts/` et de leurs cinq blocs `@font-face`. Merriweather reste auto-hébergée pour le thème sépia. `scripts/fetch_book_fonts.py` ne régénère plus que Merriweather.
- **Couvertures** : huit couvertures lourdes de *L'Odyssée de l'énergie* recompressées en WebP 1024×1024, qualité 82. Poids total ramené de 8 728 652 à 1 808 256 octets, soit 79,3 pour cent de moins, avec un PSNR de 37,39 à 38,45 dB.
- **Catalogue** : retrait de la carte obsolète de *Quinte* dans les livres à venir, déjà publiée.
- **Version** : 1.8.24, cache source `hylst-reader-v80`.

### Vérifié
- `python scripts/check_dashes.py --root .` : 132 fichiers, zéro tiret cadratin ou demi-cadratin.
- `node scripts/build_jsx.js` et `--check` : 10 fichiers compilés et à jour.
- `node scripts/test-sw-policy.js` : 6 tests de politique du Service Worker, tous verts.
- `python scripts/check_future_covers.py --root .` : 16 couvertures à venir cohérentes.
- Chapitre VIII : 7 161 mots, 11 `h2`, 14 tableaux, 3 figures, HTML équilibré, deux SVG valides, zéro tiret long.
- Lecteur desktop : titre correct, 11 sections, 14 tableaux, 3 figures, images chargées, aucun débordement horizontal, aucune erreur CSP ou console. Cache `hylst-reader-6c0293e00a62` avec 324 entrées, chapitre et deux SVG précachés, rechargement et ouverture hors ligne réussis.
- Lecteur mobile 390 px : page sans débordement, tableaux à deux colonnes lisibles, tableaux à trois et quatre colonnes défilables dans leur conteneur, ouverture hors ligne réussie.
- Synchronisation : build `6c0293e00a62`, 274 fichiers runtime, 11 fiches, fontes Outfit obsolètes élaguées, contrôles de tirets et de CSP verts sur le miroir.
- Production : déployée le 08/11 (commit plateforme `2838cd6e`), build `6c0293e00a62`, SW `hylst-reader-6c0293e00a62`, index `?v=6c0293e00a62`. `verify-release.ps1` entièrement vert : build cohérent, 13 URL, 11 fiches, 301, CSP meta et Nginx, `.env` 403, sources 404, aucun Babel ni JSX servi.

## [1.8.23] - 2026-11-08
### Modifié
- **Précache hors ligne complet** : le Service Worker lit les introductions et les chapitres déjà précachés, extrait leurs `<img>` et précache les 28 illustrations et plans SVG. Il ajoute aussi les 16 couvertures des livres à venir affichées dans la bibliothèque et les 77 fontes de la plateforme lues depuis `/assets/fonts/fonts.css`.
- **Cache** : `hylst-reader-v79`, build `0b632e9d5101`, 322 entrées, environ 20 Mo. Les PDF de *Sciences et technologie* restent hors précache.
- Version 1.8.23.

### Vérifié
- `node scripts/build_jsx.js --check` : 10 fichiers à jour. `python scripts/check_dashes.py --root .` : 132 fichiers, zéro tiret cadratin ou demi-cadratin.
- Synchronisation : build `0b632e9d5101`, 277 fichiers runtime, 11 fiches, sitemap à 13 URL.
- Profil Chromium vierge sur le miroir : 322 entrées en cache, 28 illustrations de chapitre, 29 couvertures de recueils, 16 couvertures à venir, 77 fontes et `fonts.css` présentes.
- Hors ligne : bibliothèque, `droits.html`, 7 fiches avec et sans slash, liseuse des 7 livres testés au chapitre 1, puis chapitre suivant pour Nightprowler, Sciences et technologie et le Tome I. Les illustrations de Nightprowler (1216 px), les plans SVG (1200 px) et les illustrations des recueils (512 px) s'affichent.
- 0 réponse en erreur, 0 requête échouée, 0 erreur console, 0 requête externe.
- Production déployée le 08/11 (commit plateforme `f4da5092`, conteneur `zg4880k00soco08c4wkg48ks-20261108T112915`) : build `0b632e9d5101`, SW `hylst-reader-0b632e9d5101`, index `?v=0b632e9d5101`, version 1.8.23. `verify-release.ps1` entièrement vert.
- Profil Chromium vierge sur la production : 322 entrées, 28 illustrations, 16 couvertures à venir, 77 fontes, 0 image cassée, 7 fiches avec et sans slash, 7 livres dans la liseuse, illustrations et plans SVG affichés, 0 réponse en erreur, 0 requête échouée, 0 erreur console, 0 violation CSP.

## [1.8.22] - 2026-11-07

### Ajouté
- **Nouveau livre au catalogue : *Approche de la Neurodiversité*** (sous-titre *Vision d'un non-professionnel*) :
  - Publication complète de l'essai élaboré à partir des textes de réflexion et de terrain de l'auteur (`Idées pour lutter contre les troubles ‘dys’ et autres troubles neurocognitifs`, `Clarifications, réflexions et pistes de solutions pour troubles cognitifs`, `Enfants en difficulté scolaire`).
  - Choix d'une ligne éditoriale résolument réaliste et pessimiste, rejetant les clichés lénifiants du développement personnel et de la neurodiversité idéalisée : constat brut du handicap invisible, coût énergétique démesuré de la compensation permanente, blessure scolaire précoce, incompréhension sociale et professionnelle, mémoire de travail qui sature, dérives attentionnelles et stratégies pragmatiques de survie (segmentation chirurgicale, modélisation visuelle, béquille informatique, gestion stricte de la fatigue).
  - Ouvrage structuré en une introduction et six chapitres :
    - *Introduction : Le décalage invisible*
    - *I. L'ornière scolaire et la blessure originelle*
    - *II. La mécanique grippée : langage, geste et espace*
    - *III. L'attention en miettes et la mémoire qui fuit*
    - *IV. L'usure adulte et le malentendu permanent*
    - *V. Béquilles cognitives et stratégies de survie*
    - *VI. Épilogue : Vivre avec la friction*
  - Couverture dédiée `covers/cover_neuro.webp` (512×768), fiche statique `/livres/approche-de-la-neurodiversite/` générée avec données structurées Schema.org, et retrait de la vignette d'attente `f10` dans `LibraryView.jsx`.

### Modifié
- **Catalogue** : passage à **11 livres et 94 chapitres** (105 contenus de lecture avec les onze introductions) dans `public/books.json`.
- **Sitemap** : passage de 12 à **13 URL** dans le miroir de production avec l'indexation de la nouvelle fiche.
- **Version** : 1.8.22, cache source `hylst-reader-v78`, modale À propos et en-tête du Service Worker à jour.

### Vérifié
- `python scripts/check_dashes.py --root .` : 132 fichiers contrôlés, zéro tiret cadratin ou demi-cadratin.
- `public/books.json` valide : 11 livres, 94 chapitres.
- `node scripts/build_jsx.js` et `--check` : 10 fichiers compilés et à jour.
- `python scripts/build_book_pages.py` : 11 fiches générées.
- **Synchronisation du miroir** : build `04d19b84bf10`, cache `hylst-reader-04d19b84bf10`, 277 fichiers runtime vérifiés, sitemap à 13 URL, 26 placeholders `?v=04d19b84bf10`.
- Tests HTTP locaux : accueil, fiche Neurodiversité, chapitres 1 à 6, couverture et `books.json` en 200.

## [1.8.21] - 2026-11-07

### Modifié
- **Quinte ou Les Harmoniques de l'Âme** :
  - Restauration de la phrase d'amorce du manuscrit d'origine (`quinte.rtf`) en ouverture du chapitre 4 : *« Quinte sentit, un jour, un appel provenant des profondeurs de son propre être. Une dissonance étrange, une perturbation subtile dans les ondes stationnaires qui l'entouraient. »*
  - Harmonisation des titres des parties 4 à 7, désormais titrées dans le respect absolu du vocabulaire physique et musical de l'auteur : *IV. La Faille Spectrale*, *V. L'Épreuve du Gouffre Sonore*, *VI. L'Expansion et les Ondes Cosmiques*, *VII. La Grande Réaccordance*.
  - Retrait du badge « En chantier » dans `public/books.json` : le livre est complet et stabilisé au catalogue.
- **Version** : 1.8.21, cache source `hylst-reader-v77`, modale À propos et en-tête du Service Worker à jour.

### Vérifié
- `python scripts/check_dashes.py --root .` : 124 fichiers contrôlés, zéro tiret cadratin ou demi-cadratin.
- `public/books.json` valide : 10 livres, 88 chapitres, Quinte achevée sans badge.
- `node scripts/build_jsx.js` et `--check` : 10 fichiers compilés et à jour.
- `python scripts/build_book_pages.py` : 10 fiches générées, sommaire de Quinte complet à sept entrées.
- **Synchronisation du miroir** : build `5350a1f1c551`, cache `hylst-reader-5350a1f1c551`, 268 fichiers runtime vérifiés, sitemap à 12 URL, 26 placeholders `?v=5350a1f1c551`.
- Tests HTTP locaux : accueil, fiche Quinte, chapitres 1 à 7 et `books.json` en 200.

## [1.8.20] - 2026-11-07

### Modifié
- **Catalogue & statut** : retrait du badge « En chantier » pour le livre *Nightprowler, carnets de Samarande* dans `public/books.json`. Les treize chapitres et les annexes étant tous publiés, relus et vérifiés en production, l'ouvrage rejoint le statut des livres achevés au catalogue.
- **Version** : 1.8.20, cache source `hylst-reader-v76`, modale À propos et en-tête du Service Worker à jour.
- **Suivi projet** : mise à jour complète de `todo.md` (consolidation des versions 1.8.12 à 1.8.19 et réalignement des chantiers futurs).

### Vérifié
- `python scripts/check_dashes.py --root .` : 124 fichiers contrôlés, zéro tiret cadratin ou demi-cadratin.
- `public/books.json` valide : 10 livres, 88 chapitres, badge de Nightprowler retiré.
- `node scripts/build_jsx.js` et `--check` : 10 fichiers compilés et à jour.
- `python scripts/build_book_pages.py` : 10 fiches générées.
- **Synchronisation du miroir** : build `e1fa1775688a`, cache `hylst-reader-e1fa1775688a`, 268 fichiers runtime vérifiés, sitemap à 12 URL, 26 placeholders `?v=e1fa1775688a`.
- Tests HTTP locaux : accueil, fiche Nightprowler, chapitre XIII, illustration et `books.json` en 200.

## [1.8.19] - 2026-11-07

### Ajouté
- **Nightprowler, chapitre XIII. Annexes** : les annexes de référence pour clore le livre *Nightprowler, carnets de Samarande*. Elles réunissent trois outils indispensables à la table :
  - Une feuille de personnage vierge complète, normalisée en tableaux HTML (`.chapter-stats-table`) à partir du fichier d'origine `fichpers.htm` : identité, 11 caractéristiques, compétences réparties en cinq registres (voleur, relations humaines, prouesses physiques, combat, recherches et développement) avec caractéristiques associées, cases Expert et Privilégiée, et modificateurs de blessure F/S. Pistes de fatigue et de santé, temps et scores d'action, armes, équipement et histoire.
  - Un lexique alphabétique de 23 termes attestés dans les textes et scénarios (Arlam, Bailli, Bejofa, Cassar, Cité franche, Couronne, Culte de la Pensée, Ezgir, Féli, Gouri, Guilde, Héloderme, Kalaar, Khaler, Milicien, Monts Ocres, Préfet, Prévôt, Prince, Sahar, Samarande, Sept cités, Soloman, Umélorien).
  - Une chronologie des repères historiques documentés : avant 59 (origine de Bejofa), 2258 (insurrection de Bejofa), vers 2300 (Grande enceinte), vers 2310 (chute de Kalaar), 2476 (Bejofa devient cité), 2559 (présent de la campagne de 2011).
  - Une section « Ce que ces annexes ne disent pas » précisant les limites des sources. Aucun texte de tiers n'est reproduit.
- **Illustration du chapitre XIII** : `chapitre-13-cover.webp` (1216x832), une table de travail d'archiviste à la lueur de deux chandelles, avec feuille de personnage quadrillée, lexique relié de cuir, rouleau de chronologie, plume et encrier, générée sur le GPU local avec `z-image-turbo-sdcpp`.

### Modifié
- **Catalogue** : `public/books.json` passe de 87 à 88 chapitres ; *Nightprowler, carnets de Samarande* est complet avec 13 chapitres publiés.
- **Fiche statique** : la page de Nightprowler liste le sommaire complet à treize entrées.
- **Version** : 1.8.19, cache source `hylst-reader-v75`, modale À propos et en-tête du Service Worker à jour.
- **Compteurs** : 98 fichiers de contenu (10 introductions et 88 chapitres) dans README, readme-dev, features, structure et antigravity.

### Vérifié
- `python scripts/check_dashes.py --root .` : 124 fichiers contrôlés, zéro tiret cadratin ou demi-cadratin.
- `public/books.json` valide : 10 livres, 88 chapitres.
- `node scripts/build_jsx.js` et `--check` : 10 fichiers compilés et à jour.
- `python scripts/build_book_pages.py` : 10 fiches générées, sommaire de Nightprowler à treize entrées.
- **Synchronisation du miroir** : build `18c6aef2b4f1`, cache `hylst-reader-18c6aef2b4f1`, 268 fichiers runtime vérifiés, sitemap à 12 URL, 26 placeholders `?v=18c6aef2b4f1`.
- Tests HTTP locaux : accueil, fiche Nightprowler, chapitre XIII, illustration et `books.json` en 200 ; catalogue à 10 livres et 88 chapitres.

## [1.8.18] - 2026-11-07

### Ajouté
- **Nightprowler, chapitre XII. Pistes inachevées** : trois titres retrouvés au bas de la page « Mes scénarios », rédigée en 1999, et jamais développés : le camp barbare du prince démon Azefhfkrijiiir, le contrôle d'entrée à choix et les aventures à Kalaar. Ce chapitre ne restitue aucun texte ancien : il propose ce que l'auteur ferait aujourd'hui de ces trois idées, avec le recul et les événements des chapitres VIII à XI. Chaque piste est développée en une page de jeu, avec ses variantes et ses tables.
- **Illustration du chapitre XII** : `chapitre-12-cover.webp` (1216x832), une carte ancienne sur une table de bois avec les trois chemins, le camp barbare, la porte gardée et la cité souterraine, générée sur le GPU local avec `z-image-turbo-sdcpp`.

### Modifié
- **Catalogue** : `public/books.json` passe de 86 à 87 chapitres ; Nightprowler passe de 11 à 12 chapitres.
- **Fiche statique** : la page de Nightprowler liste le chapitre XII et son sommaire à douze entrées.
- **Version** : 1.8.18, cache source `hylst-reader-v74`, modale À propos et en-tête du Service Worker à jour.
- **Compteurs** : 97 fichiers de contenu (10 introductions et 87 chapitres) dans README, readme-dev, features, structure et antigravity.

### Vérifié
- `python scripts/check_dashes.py --root .` : 123 fichiers contrôlés, zéro tiret cadratin ou demi-cadratin.
- `public/books.json` valide : 10 livres, 87 chapitres.
- `node scripts/build_jsx.js` et `--check` : 10 fichiers compilés et à jour.
- `python scripts/build_book_pages.py` : 10 fiches générées, sommaire de Nightprowler à douze entrées.
- **Synchronisation du miroir** : build `b4601b6d69b4`, cache `hylst-reader-b4601b6d69b4`, 266 fichiers runtime vérifiés, sitemap à 12 URL, 26 placeholders `?v=b4601b6d69b4`.
- Tests HTTP locaux : accueil, fiche Nightprowler, chapitre XII, illustration et `books.json` en 200 ; catalogue à 10 livres et 87 chapitres.

## [1.8.17] - 2026-11-07

### Ajouté
- **Nightprowler, chapitre XI. La reconquête du trône des Rodallois** : un scénario écrit en 1999 pour un autre jeu que Nightprowler, conservé sous les titres « La reconquête du trône des Rodallois des terres d'Alliphance » et « Introduction à l'aventure », dernière copie datée du 1er mars 2004. Le chapitre est volontairement séparé des carnets de Samarande et le dit dès sa première ligne. La présente version réorganise les deux fichiers en cinq actes, réunit les quatre lois et les figures en tableaux, ajoute la vérité du pacte, les alliances, les preuves et les issues, ainsi que la section « Mener la table ». Les noms, les lois, le discours et le bracelet viennent des fichiers d'origine. Aucun texte de tiers n'est reproduit.
- **Illustration du chapitre XI** : `chapitre-11-cover.webp` (1216x832), un jeune prince caché dans le jardin royal à l'aube, son bracelet gravé au poignet, le château en flammes et un démon cornu dans le lointain, générée sur le GPU local avec `z-image-turbo-sdcpp`.

### Modifié
- **Catalogue** : `public/books.json` passe de 85 à 86 chapitres ; Nightprowler passe de 10 à 11 chapitres.
- **Fiche statique** : la page de Nightprowler liste le chapitre XI et son sommaire à onze entrées.
- **Version** : 1.8.17, cache source `hylst-reader-v73`, modale À propos et en-tête du Service Worker à jour.
- **Compteurs** : 96 fichiers de contenu (10 introductions et 86 chapitres) dans README, readme-dev, features, structure et antigravity.

### Vérifié
- `python scripts/check_dashes.py --root .` : 122 fichiers contrôlés, zéro tiret cadratin ou demi-cadratin.
- `public/books.json` valide : 10 livres, 86 chapitres.
- `node scripts/build_jsx.js` et `--check` : 10 fichiers compilés et à jour.
- `python scripts/build_book_pages.py` : 10 fiches générées, sommaire de Nightprowler à onze entrées.
- **Synchronisation du miroir** : build `f5edc2c6c480`, cache `hylst-reader-f5edc2c6c480`, 264 fichiers runtime vérifiés, sitemap à 12 URL, 26 placeholders `?v=f5edc2c6c480`.
- Tests HTTP locaux : accueil, fiche Nightprowler, chapitre XI, illustration et `books.json` en 200 ; catalogue à 10 livres et 86 chapitres.

## [1.8.16] - 2026-11-07

### Ajouté
- **Nightprowler, chapitre X. Vapeur et boulons** : le scénario écrit pour la quinzième convention des Alchimistes, en 2011, sur le thème « vapeur et boulons », pour les cinq prétirés du chapitre VII et une soirée de convention. Le fichier d'origine pose les bases et laisse le meneur finir le travail : le plan du moulin manque, la machine n'est décrite qu'en creux, l'artefact n'a pas de nom et le sort de Tramiel hésite entre deux lignes. La présente version le restructure en cinq actes, de la remise en liberté de K'rëtrr à la nuit du moulin, dessine le plan, décrit la machine et la pierre de rosette, tranche le sort de Tramiel et réunit les issues en tableau. Les valeurs des personnages viennent du fichier d'origine. Aucun texte de tiers n'est reproduit.
- **Plan du moulin** : `chapitre-10-plan.svg`, coupe sur trois niveaux avec la roue et le bief, l'entrepôt, la cuisine et la chambre de Jiniane, l'atelier et la machine, la réserve de vie, la chambre de Tramiel sous les toits, l'escalier piégé et le chien de garde.
- **Illustration du chapitre X** : `chapitre-10-cover.webp` (1216x832), l'atelier d'alchimie dans un moulin, la machine de cuivre et son cristal rose, l'alchimiste, le charbon et l'or, générée sur le GPU local avec `z-image-turbo-sdcpp`.

### Modifié
- **Catalogue** : `public/books.json` passe de 84 à 85 chapitres ; Nightprowler passe de 9 à 10 chapitres.
- **Fiche statique** : la page de Nightprowler liste le chapitre X et son sommaire à dix entrées.
- **Version** : 1.8.16, cache source `hylst-reader-v72`, modale À propos et en-tête du Service Worker à jour.
- **Compteurs** : 95 fichiers de contenu (10 introductions et 85 chapitres) dans README, readme-dev, features, structure et antigravity.

### Vérifié
- `python scripts/check_dashes.py --root .` : 121 fichiers contrôlés, zéro tiret cadratin ou demi-cadratin.
- `public/books.json` valide : 10 livres, 85 chapitres.
- `node scripts/build_jsx.js` et `--check` : 10 fichiers compilés et à jour.
- `python scripts/build_book_pages.py` : 10 fiches générées, sommaire de Nightprowler à dix entrées.
- **Synchronisation du miroir** : build `4c356874972d`, cache `hylst-reader-4c356874972d`, 262 fichiers runtime vérifiés, sitemap à 12 URL, 26 placeholders `?v=4c356874972d`.
- Tests HTTP locaux : accueil, fiche Nightprowler, chapitre X, illustration, plan et `books.json` en 200 ; catalogue à 10 livres et 85 chapitres.

## [1.8.15] - 2026-11-07

### Ajouté
- **Nightprowler, chapitre IX. Esclavage gouri sans vergogne** : le plus long scénario du recueil, écrit en 1999 ou 2000 et retapé le 2 juillet 2001. Le fichier d'origine est un document de travail avec abréviations et fautes de frappe, dont le plan du camp, décrit par les lettres A à O, n'a pas survécu. La présente version le restructure en cinq actes, de la rafle dans la galerie à l'évasion, redessine le plan, réunit les six issues en tableau et ajoute une section « Mener la table » avec les avertissements de contenu. Les valeurs de Bromi, du rat et des émeraudes viennent du fichier d'origine. Aucun texte de tiers n'est reproduit.
- **Plan du camp** : `chapitre-9-plan.svg`, plan schématique dessiné pour cette édition, avec les zones A à O, la voie principale, la salle secrète K, l'escalier vers le temple et les deux issues de surface.
- **Illustration du chapitre IX** : `chapitre-9-cover.webp` (1216x832), un camp de travail souterrain peuplé de gouris rats enchaînés, avec rails, chariots et un contremaître géant, générée sur le GPU local avec `z-image-turbo-sdcpp`.

### Modifié
- **Catalogue** : `public/books.json` passe de 83 à 84 chapitres ; Nightprowler passe de 8 à 9 chapitres.
- **Fiche statique** : la page de Nightprowler liste le chapitre IX et son sommaire à neuf entrées.
- **Version** : 1.8.15, cache source `hylst-reader-v71`, modale À propos et en-tête du Service Worker à jour.
- **Compteurs** : 94 fichiers de contenu (10 introductions et 84 chapitres) dans README, readme-dev, features, structure et antigravity.

### Vérifié
- `python scripts/check_dashes.py --root .` : 120 fichiers contrôlés, zéro tiret cadratin ou demi-cadratin.
- `public/books.json` valide : 10 livres, 84 chapitres.
- `node scripts/build_jsx.js` et `--check` : 10 fichiers compilés et à jour.
- `python scripts/build_book_pages.py` : 10 fiches générées, sommaire de Nightprowler à neuf entrées.
- **Synchronisation du miroir** : build `52a864e91652`, cache `hylst-reader-52a864e91652`, 259 fichiers runtime vérifiés, sitemap à 12 URL, 26 placeholders `?v=52a864e91652`.
- Tests HTTP locaux : accueil, fiche Nightprowler, chapitre IX, illustration, plan et `books.json` en 200 ; catalogue à 10 livres et 84 chapitres.

## [1.8.14] - 2026-11-07

### Ajouté
- **Nightprowler, chapitre VIII. Le squelette enfoui d'Azefhfkrijiiir** : le premier scénario complet du recueil, écrit vers 1999 pour une équipe de gouris et retrouvé sous la forme d'un synopsis d'un seul bloc, sans actes ni dialogue, qui s'arrête au milieu d'une phrase sur « Ils feront ». La présente version le découpe en six actes, de la légende des cinq parties du squelette à la rencontre finale dans la salle basse. Sont ajoutés pour cette édition : la table des objets maudits, l'identité et le marché des Veilleurs, la rencontre finale et ses trois issues, ainsi que la section « Mener la table ». Les valeurs de possession, la difficulté 8 et le décompte des caractéristiques viennent du fichier d'origine. Aucun texte de tiers n'est reproduit.
- **Illustration du chapitre VIII** : `chapitre-8-cover.webp` (1216x832), un crâne cornu traversé d'un kriss dans un sarcophage de granit ouvert, entouré de squelettes difformes à la lueur des torches, générée sur le GPU local avec `z-image-turbo-sdcpp`, dans le style de la couverture.

### Modifié
- **Catalogue** : `public/books.json` passe de 82 à 83 chapitres ; Nightprowler passe de 7 à 8 chapitres.
- **Fiche statique** : la page de Nightprowler liste le chapitre VIII et son sommaire à huit entrées.
- **Version** : 1.8.14, cache source `hylst-reader-v70`, modale À propos et en-tête du Service Worker à jour.
- **Compteurs** : 93 fichiers de contenu (10 introductions et 83 chapitres) dans README, readme-dev, features, structure et antigravity.

### Vérifié
- `python scripts/check_dashes.py --root .` : 119 fichiers contrôlés, zéro tiret cadratin ou demi-cadratin.
- `public/books.json` valide : 10 livres, 83 chapitres.
- `node scripts/build_jsx.js` et `--check` : 10 fichiers compilés et à jour.
- `python scripts/build_book_pages.py` : 10 fiches générées, sommaire de Nightprowler à huit entrées.
- **Synchronisation du miroir** : build `28566d89e3fc`, cache `hylst-reader-28566d89e3fc`, 256 fichiers runtime vérifiés, sitemap à 12 URL, 26 placeholders `?v=28566d89e3fc`.
- Tests HTTP locaux : accueil, fiche Nightprowler, chapitre VIII, illustration et `books.json` en 200 ; catalogue à 10 livres et 83 chapitres.

## [1.8.13] - 2026-11-07

### Ajouté
- **Nightprowler, chapitre VII. Figures et prétirés** : six fiches normalisées pour la table. Albert Degreffion, dit Sir Albert de Greffion nième du nom et le Noble Dé Chu, agitateur umélorien de 33 ans, puis les cinq prétirés du scénario de la quinzième convention des Alchimistes de 2011 : K'rëtrr le cambrioleur gouri rat, S'rhie la monte-en-l'air gerboise, Elyr Djedorath le contrebandier khaler, Hironne Diêtre l'espionne umélorienne et Krieu'kr le détrousseur sang-mêlé. Noms, valeurs, races, âges et équipements repris des feuilles d'origine ; portraits, commentaires et conseils de jeu réécrits pour cette édition. Aucune fiche tierce n'est reproduite.
- **Illustration du chapitre VII** : `chapitre-7-cover.webp` (1216x832), six figures réunies autour d'une table à la lanterne, générée sur le GPU local avec `z-image-turbo-sdcpp`, dans le style de la couverture.

### Modifié
- **Catalogue** : `public/books.json` passe de 81 à 82 chapitres ; Nightprowler passe de 6 à 7 chapitres.
- **Fiche statique** : la page de Nightprowler liste le chapitre VII et son sommaire à sept entrées.
- **Version** : 1.8.13, cache source `hylst-reader-v69`, modale À propos et en-tête du Service Worker à jour.
- **Compteurs** : 92 fichiers de contenu (10 introductions et 82 chapitres) dans README, readme-dev, features, structure et antigravity.

### Vérifié
- `python scripts/check_dashes.py --root .` : 118 fichiers contrôlés, zéro tiret cadratin ou demi-cadratin.
- `public/books.json` valide : 10 livres, 82 chapitres.
- `node scripts/build_jsx.js` et `--check` : 10 fichiers compilés et à jour.
- `python scripts/build_book_pages.py` : 10 fiches générées, sommaire de Nightprowler à sept entrées.
- **Synchronisation du miroir** : build `d94013061769`, cache `hylst-reader-d94013061769`, 254 fichiers runtime vérifiés, sitemap à 12 URL, 26 placeholders `?v=d94013061769`.
- Tests HTTP locaux : accueil, fiche Nightprowler, chapitre VII, illustration et `books.json` en 200 ; catalogue à 10 livres et 82 chapitres.

## [1.8.12] - 2026-11-07

### Ajouté
- **Quatre escapades retrouvées (1995)** dans le Tome I, à la suite d'« Escapade boisée » : *À travers toundra et plateaux* (partie B2), *Au gré de la montagne et des précipices* (partie C, 12 mars 1995), *Caverne et tunnels* (partie D, 12 mai 1995) et *La plage* (partie E, 12 juin 1995). Réécriture légère limitée à l'orthographe, la ponctuation, les répétitions et les formules de fin de billet ; images, parenthèses et jeux de mots conservés. La partie B, « À la campagne », reste au Tome III.
- **Un brin d'écrit (12 juin 1996)** dans le Tome I : premier poème du fichier retrouvé, présenté en strophes, avec sa date d'origine et une note de source.
- **Farouches apparitions (12 juin 1999)** dans le Tome II : second poème du même fichier, avec sa note d'origine sur les mots égarés.
- **La tanière du mage (fin 2020)** dans le Tome II : prose onirique écrite pour accompagner une peinture numérique, débarrassée des vœux de fin d'année et des clins d'œil personnels.

### Modifié
- **Catalogue** : `public/books.json` passe de 74 à 81 chapitres. Le Tome I passe de 11 à 16 textes, le Tome II de 8 à 10. Les deux introductions annoncent les nouveaux textes et les dates d'origine.
- **Fiches statiques** : les pages des Tomes I et II listent les nouveaux chapitres et les compteurs à jour.
- **Couvertures** : les couvertures des Tomes I et II sont recomposées par `scripts/update_recueils_covers.py` et annoncent « SEIZE TEXTES · 1995-2024 » et « DIX TEXTES · 1999-2024 » ; les images Open Graph suivent.
- **Version** : 1.8.12, cache source `hylst-reader-v68`, mention de version de la modale À propos.
- **Compteurs** : 91 fichiers de contenu (10 introductions et 81 chapitres) dans README, readme-dev, features, structure et antigravity.

### Vérifié
- `python scripts/check_dashes.py --root . --all` : 173 fichiers contrôlés, zéro tiret cadratin ou demi-cadratin.
- `public/books.json` valide : 10 livres, 81 chapitres.
- `node scripts/build_jsx.js` et `--check` : 10 fichiers compilés et à jour.
- `python scripts/build_book_pages.py` : 10 fiches générées, sommaires des Tomes I et II à 16 et 10 entrées.
- **Synchronisation du miroir** : build `54add590c04d`, cache `hylst-reader-54add590c04d`, 252 fichiers runtime vérifiés, sitemap à 12 URL, 26 placeholders `?v=54add590c04d`.
- **Déploiement du 07/11** : commit plateforme `49d2f2a2`, production en 1.8.12. `verify-release.ps1` entièrement vert (12 URL, 10 fiches, 301, CSP meta et Nginx, `.env` 403, sources 404) ; `books.json` sert 10 livres et 81 chapitres ; les sept nouveaux chapitres et les deux couvertures répondent en 200.

## [1.8.11] - 2026-11-07
### Ajouté
- **Tome IV, *Carnets, réflexions & partages*** : quatrième tome de la série *Recueils de proses et poésies fantasques*, consacré aux textes non fictifs retrouvés dans les archives. Quatre chapitres chronologiques : *Hygiène de vie* (23 novembre 2003), *Imaginez-vous* (19 juin 2007), *Idées cadeaux* (5 septembre 2008) et *Marre d'apprendre* (vers 2024). Réécriture légère limitée à l'orthographe, à la ponctuation, aux répétitions et aux abréviations de blog ; images, parenthèses et jeux de mots conservés. Chaque chapitre affiche sa date d'origine et une note de source.
- **Livre *Sciences et technologie*** : édition numérique de l'étude technique bibliographique *Analyse des solutions techniques mises en œuvre dans les jeux vidéos*, écrite en 2001-2002 en cinquième année NFIO, promotion 7. Une préface de 2026 (1 209 mots), puis quatre parties avec résumé 2026, sommaire d'origine et PDF complet téléchargeable. Format hybride : synthèses HTML dans la liseuse, texte et mise en page d'origine dans les PDF.
- **Quatre PDF d'archive** : partie A (21 pages, 934 518 octets), partie B (17 pages, 499 891 octets), partie C (40 pages, 1 370 408 octets), partie D (36 pages, 935 573 octets), exportés depuis les `.docx` d'origine avec Word COM, images et schémas compris. Manifeste `pdf/manifest.json` avec pages, poids et empreintes SHA-256.
- **Deux couvertures composées** : `recueils-proses-poesies-t4-carnets-reflexions-partages.webp` (600x900, 66 558 octets) et `sciences-et-technologie-jeux-videos.webp` (600x900, 36 118 octets). Fonds générés sur le GPU local, typographie composée avec PIL, sources conservées dans `scripts/assets/covers/`.
- **Scripts** : `scripts/make_book_covers.py` pour les couvertures, `scripts/export_etjv_pdfs.ps1` pour l'export Word COM par processus séparé.

### Modifié
- **Catalogue** : `public/books.json` passe de 8 à 10 livres, avec les entrées `recueils-proses-poesies-t4-carnets-reflexions-partages` (4 chapitres) et `sciences-et-technologie-jeux-videos` (5 chapitres), soit 74 chapitres déclarés.
- **Fiches statiques** : 10 fiches générées par `scripts/build_book_pages.py`, dont les deux nouvelles. Les styles du bloc de téléchargement sont désormais intégrés au script de génération, qui réécrit `css/book-page.css`.
- **Styles de la liseuse** : ajout des blocs de téléchargement PDF, sommaire d'origine, résumé de 2026, contexte de partie et listes dans `css/reader.css`.
- **Service Worker** : cache source passé de `hylst-reader-v66` à `hylst-reader-v67`. Les PDF ne sont pas précachés.
- **Index et métadonnées** : l'accueil annonce « Dix livres », son JSON-LD liste 10 entrées `Book` et la liste `<noscript>` 10 liens, Nightprowler, le Tome IV et *Sciences et technologie* compris. Les compteurs des documents (README, readme-dev, features, structure, about) et les placeholders `?v=` passent à 1.8.11.
- **Sitemap du miroir** : 12 URL, avec les fiches du Tome IV et du livre *Sciences et technologie*.

### Vérifié
- `python scripts/check_dashes.py --root . --all` : 166 fichiers contrôlés, zéro tiret cadratin ou demi-cadratin.
- `public/books.json` valide : 10 livres, 74 chapitres.
- `node scripts/build_jsx.js` : 10 fichiers JSX compilés ; `--check` à jour.
- `python scripts/build_book_pages.py` : 10 fiches générées.
- Synchronisation du miroir : build `82df59e049b6`, cache `hylst-reader-82df59e049b6`, 245 fichiers runtime vérifiés, sitemap à 12 URL, 26 placeholders `?v=` et JSON-LD à 10 entrées `Book`.
- Contrôle local sur `http://127.0.0.1:8765/books_reader/` : page d'accueil, deux fiches, cinq chapitres du Tome IV, six fichiers du livre Sciences, quatre PDF et les deux couvertures répondent en 200. Les PDF téléchargés ont exactement les poids du manifeste.
- Contrôle visuel Chrome headless des deux fiches et de la page livre *Sciences et technologie* : couvertures, sommaire, bloc PDF et citation conformes.
- Déploiement du 07/11 : build `82df59e049b6`, cache `hylst-reader-82df59e049b6`, index `?v=82df59e049b6`, commits plateforme `30e645a4` puis `31aead70` (correctif d'index). `verify-release.ps1` entièrement vert : 12 URL, 10 fiches, 301, CSP meta et Nginx, `.env` 403, sources 404. Les deux fiches, les neuf chapitres et leurs introductions, les quatre PDF, le manifeste et les deux couvertures répondent en 200 ; `books.json` sert 10 livres et 74 chapitres ; JSON-LD valide à 10 entrées `Book`.

### Limites
- Les paginations incertaines des sommaires d'origine (parties C et D) sont signalées dans les pages, jamais corrigées d'office.
- Les fichiers `.docx` et les textes sources restent dans `D:\0HYLST\0 HYLST ART 2024\ecrits\textes_a_trier\` ; rien n'a été supprimé.

## [1.8.10] - 2026-11-06
### Modifié
- **Introduction de *Nightprowler, carnets de Samarande*** : texte complété et réécrit dans un ton d'hommage. Retour sur les années de meneur de jeu et de conteur, sur les règles maison et les scénarios écrits pour ce monde ; lien vers la fiche du [Guide du Rôliste Galactique](https://www.legrog.org/jeux/nightprowler) ; présentation du jeu (publié en 1995 par Siroz, réédité en 2006 par 2d Sans Faces) ; recommandation des quatre romans de Pierre Pevel parus en 1998 sous le pseudonyme de Pierre Jacq, *Premiers Sangs*, *La Voie du sang*, *Le Prix du sang* et *In memoriam*, cycle *Chroniques des sept cités*, avec le supplément *Mémoires de Sang* pour les trois premiers tomes.
- **Mention de la nouvelle édition** : plus de vingt-cinq ans après les premières parties, style littéraire repris, chapitres et notes de marge complétés, sommaire ajouté, illustrations générées par IA sur le GPU local dans le style de la couverture. Le texte précise que les textes sont de l'auteur, que les images sont des interprétations et que l'édition n'est pas officielle.
- Version 1.8.10, cache Service Worker source `hylst-reader-v66`.

### Vérifié
- `python scripts/check_dashes.py --root . --all` : 149 fichiers contrôlés, zéro tiret cadratin ou demi-cadratin.
- `python scripts/build_book_pages.py` : 8 fiches générées, la fiche Nightprowler contient le nouveau texte, le lien vers le Grog et la mention de Pierre Pevel.
- Synchronisation du miroir : build `c66ade22a32c`, cache `hylst-reader-c66ade22a32c`, 222 fichiers runtime vérifiés, sitemap à 10 URL.
- Contrôle visuel de la page livre : le nouveau texte s'affiche dans la colonne d'introduction, sous le sommaire à six entrées.

### Limites
- Version **1.8.10** déployée le 06/11, build `c66ade22a32c`, cache `hylst-reader-c66ade22a32c`. Le miroir local 1.8.11, build `1e368c766584`, attend son déploiement Coolify.

## [1.8.9] - 2026-11-06
### Ajouté
- **Nightprowler, chapitre VI. Le combat** : version personnelle de l'auteur pour sa table, inspirée du système proposé par Mathieu Mazzoni, organisée en deux moteurs. Le premier règle l'action par action (dégainer, rangs d'action, attaques enchaînées, parade, esquive, contre-attaque, deux armes, pénétration de garde, résistance des armes, attaques en force, assommer, feinte, prise de risque). Le second traite une phase de cinq secondes en un seul jet (initiative, taille des armes, Force dans les dégâts, postures, résolution de l'échange, blessures, armes de jet, volonté facultative). Les incohérences du fichier d'origine sont signalées en fin de chapitre plutôt que comblées, et la note de provenance dit clairement que le texte est celui de l'auteur, inspiré de Mazzoni.
- **Six illustrations de chapitre** : `chapitre-1-cover.webp` à `chapitre-6-cover.webp`, peintes dans le style de la couverture (ville teintée de vert-de-gris, lanternes ambrées, nuit pluvieuse). Générées sur le GPU local avec `z-image-turbo-sdcpp`, format WebP 1216×832, 114 à 197 Ko chacune. Chaque chapitre I à VI ouvre désormais sur son image, avec un texte alternatif descriptif.
- **Sommaire sur la page du livre** : `BookHomeView` affiche la liste des chapitres sous le bouton de lecture, avec un bouton par chapitre. `startReading(index)` enregistre la progression sur le chapitre choisi avant d'ouvrir la liseuse, au lieu de forcer le premier chapitre.
- **Enrichissements des premiers chapitres** : notes de marge ajoutées en 2026 et signalées dans les notes de source. Chapitre I, section « Ce que cette présentation ne dit pas » sur la ville jouée par quartiers. Chapitre II, note sur le réalisme comme refus des raccourcis. Chapitre IV, section « Un exemple, pour ne pas en rester au principe » avec un scénario complet en un paragraphe. Chapitre V, section « Trois traits, pas plus » avec un exemple de personnage construit à la table.
- **Tableaux de descripteurs** : la première colonne est alignée à gauche pour éviter la justification des étiquettes courtes (`chapitre-stats-table.descripteurs td:first-child`).

### Modifié
- **Catalogue** : `public/books.json` déclare le chapitre VI disponible, soit 6 chapitres pour *Nightprowler, carnets de Samarande*.
- **Fiche statique** : `livres/nightprowler-carnets-de-samarande/index.html` régénérée par `scripts/build_book_pages.py`, sommaire à 6 entrées.
- **Sitemap du miroir** : la fiche `livres/nightprowler-carnets-de-samarande/` est ajoutée à `sitemap.xml`, qui passe de 9 à 10 URL, `lastmod` au 06/11. La production 1.8.8 n'en comptait que 9 : la fiche du nouveau livre manquait. `sync-to-platform.ps1` complète désormais automatiquement le sitemap avec toutes les fiches déclarées dans `public/books.json`, pour que l'oubli ne se reproduise pas.
- Version 1.8.9, cache Service Worker source `hylst-reader-v65`.

### Vérifié
- `public/books.json` valide : 8 livres, 6 chapitres Nightprowler déclarés disponibles.
- `python scripts/build_book_pages.py` : 8 fiches générées, la fiche Nightprowler affiche « VI. Le combat ».
- `python scripts/check_dashes.py --root . --all` : 149 fichiers contrôlés, zéro tiret cadratin ou demi-cadratin.
- Contrôle visuel Chrome headless du chapitre VI sur page d'aperçu chargeant `css/reader.css` et `css/book-fonts.css` : titres, tableaux à deux et trois colonnes, étiquettes non justifiées et note de source conformes.
- Contrôle visuel Chrome headless de la page livre : sommaire à six entrées sous le bouton de lecture. Contrôle du chapitre I sur page d'aperçu : illustration affichée dans la colonne de lecture, ratio 3:2 conservé.
- Huit URL locales en 200 sur `http://127.0.0.1:8765/books_reader/` : `public/books.json`, `chapitre-6.html`, la fiche statique, `css/reader.css`, `css/components.css`, `sw.js` et les illustrations des chapitres I et VI.
- Synchronisation du miroir : build `ca5f4163630e`, cache `hylst-reader-ca5f4163630e`, 222 fichiers runtime vérifiés, 115 fichiers contrôlés sans tiret dans le miroir.
- Sitemap local : 10 URL, `lastmod` 06/11, l'URL `livres/nightprowler-carnets-de-samarande/` est présente ; le script de synchronisation la réajoute automatiquement si elle manque.

### Limites
- Production en **1.8.8**, build `d7cc2afa380f`, cache `hylst-reader-d7cc2afa380f`, déployée le 06/11 : fiche statique Nightprowler et image Open Graph en 200, sitemap à 9 URL car la fiche Nightprowler manquait, 86 fichiers contrôlés sans tiret. Le miroir local 1.8.9, build `ca5f4163630e`, est synchronisé, avec la fiche ajoutée au sitemap (10 URL), et attend son déploiement Coolify.
- Coverage hors ligne Nightprowler dans un profil Chromium vierge non refaite pour cette version.
- Rendu du corps de chapitre dans la liseuse non automatisé : l'ouverture passe par un clic, aucun paramètre d'URL ne cible un chapitre.

## [1.8.8] - 2026-11-06
### Ajouté
- **Livre *Nightprowler, carnets de Samarande*** : nouvelle entrée `nightprowler-carnets-de-samarande` dans `public/books.json`, avec introduction et cinq chapitres publiés (I. Le monde de Samarande, II. L'esprit du jeu, III. Vies et prix, IV. Bâtir un scénario, V. Décrire un personnage), badge « En chantier », `authorship: human`, `aiAssisted: false`. Design en polices locales Outfit et Merriweather, aucune requête externe. Fiche statique générée par `scripts/build_book_pages.py`, image Open Graph produite.
- **Variante de tableau `.chapter-stats-table.descripteurs`** dans `css/reader.css` : la colonne de descripteurs ne reprend pas le gras ni la couleur d'accent prévus pour les valeurs numériques.

### Modifié
- **Vignette d'attente retirée** : `f3` « Scénarios et campagnes pour Nightprowler » quitte `FUTURE_BOOKS` dans `js/components/LibraryView.jsx`, le livre étant désormais intégré.
- **Rédaction du corpus Nightprowler** : présentation de 1999 (`hnp.htm`), réponses de la mailing list de 2000 (`hnpaj.htm`) aide à la description (`aidcreapersos.htm`) et inventaire d'échoppes (`hnpaj.htm`) remis en paragraphes et en tableaux, corrigées et complétées. Les listes du chapitre V sont reconstruites sur les 15 registres réellement présents dans la source, après retrait d'une première version dont les descripteurs étaient en partie inventés. L'Atlas de Bejofa (Letorve) et l'aide à la description de Hirrinkaël ne sont pas reproduits. Les règles de combat publiées au chapitre VI sont la version personnelle de l'auteur, inspirée de celle de Mathieu Mazzoni, et non une reproduction.
- Version 1.8.8, cache Service Worker source `hylst-reader-v64`.

### Vérifié
- `public/books.json` valide et chargé : 8 livres, chapitres I à V déclarés disponibles.
- `node scripts/build_jsx.js` puis `--check` : 10 fichiers compilés, sortie à jour.
- `python scripts/check_dashes.py --root .` : 93 fichiers contrôlés, zéro tiret cadratin ou demi-cadratin.
- Neuf URL locales en 200 sur le serveur de test : `books.json`, couverture, introduction, trois chapitres, fiche statique, `book-fonts.css` et `sw.js`.
- Chrome headless : la carte du livre apparaît dans la bibliothèque intégrée, la vignette « Bientôt » de Nightprowler a disparu, la page livre affiche titre, couverture, introduction et bouton « Commencer la lecture », la fiche statique affiche le titre du chapitre I et le lien `?book=nightprowler-carnets-de-samarande`.
- Contrôle visuel du chapitre V sur page d'aperçu chargeant `css/reader.css` et `css/book-fonts.css` : tableaux à deux colonnes lisibles, listes non mises en gras, titres et notes de source conformes.

### Limites
- Rendu du corps de chapitre dans la liseuse non automatisé : l'ouverture d'un chapitre passe par un clic, aucun paramètre d'URL ne cible un chapitre.
- Contrôles hors ligne, production, sitemap et Lighthouse non refaits pour cette version intermédiaire.

## [1.8.7] - 2026-11-04
### Modifié
- **CSS inline externalisés** : les styles de `droits.html` passent dans `css/droits.css`, ceux des 7 fiches statiques dans `css/book-page.css`, généré par `scripts/build_book_pages.py`. La CSP meta passe de `style-src 'self' 'unsafe-inline'` à `style-src 'self'; style-src-attr 'unsafe-inline'`, ce qui retire l'autorisation globale des blocs `<style>` tout en conservant les attributs `style` de React.
- **Hors ligne sans slash** : quand la navigation vers `/livres/<id>` échoue hors ligne, le Service Worker tente la fiche précachée `/livres/<id>/` avant de retomber sur l'app shell. Le 301 Nginx reste actif en ligne.
- **AGENTS.md** : consignes courtes pour les agents, avec renvoi vers `antigravity.md` pour la mémoire complète.
- **Script de régression** : `scripts/verify-release.ps1` contrôle `js/dist`, la règle zéro tiret, puis en production le build, le Service Worker, les 9 URL du sitemap, le 301 des 7 fiches, la CSP et les fichiers sensibles. Mode `-SkipProd` pour les contrôles locaux.
- **Précache** : `css/book-page.css` et `css/droits.css` entrent dans l'app shell hors ligne.
- Version 1.8.7, cache Service Worker source `hylst-reader-v61`.

### Vérifié
- Build local `354686eb6d46` : 107 fichiers contrôlés, zéro tiret cadratin ou demi-cadratin, 207 fichiers runtime vérifiés.
- CSP stricte en local : zéro violation, 86 attributs `style` React fonctionnels, `droits.css` et `book-page.css` servis en 200, rendu des pages statiques et de la page de droits intact.
- Hors ligne en profil vierge : `/livres/quinte-ou-les-harmoniques-de-l-ame` sans slash et avec slash affichent la même fiche, avec 139 entrées en cache après navigation.
- Production vérifiée sur le build `354686eb6d46` et le SW `hylst-reader-354686eb6d46` : 9/9 URL du sitemap en 200, 301 des 7 fiches avec query conservée, `droits.css` et `book-page.css` en 200, CSP stricte sur l'index, les droits et les 7 fiches.
- axe sans violation sur 9 états en production : bibliothèque sombre, sépia et clair, fiche livre, liseuse, paramètres, musique, fiche statique et page de droits.
- Hors ligne en profil vierge sur la production : `/livres/quinte-ou-les-harmoniques-de-l-ame` sans slash affiche la fiche statique, 139 entrées en cache après navigation.
- `scripts/verify-release.ps1` : tous les contrôles passent, y compris build, sitemap, 301, CSP meta, en-tête CSP Books Reader, absence d'en-tête global, `.env` 403 et Babel/JSX en 404.
- Lighthouse production mobile : performance 91, accessibilité 100, bonnes pratiques 100, SEO 100, LCP 3,3 s, CLS 0, TBT 10 ms.
- Lighthouse production desktop : performance 97, accessibilité 100, bonnes pratiques 100, SEO 100, LCP 1,3 s, CLS 0,008, TBT 0 ms.
- En-tête CSP Nginx actif depuis le 04/11 : configuration `28f5c867ffdb657d541daf8b0997a133`, base64 Coolify `375eebfe92a2b0bf80f37641a8f407d6`, sauvegarde `/root/hylst-nginx-backup-20261104-booksreader-csp/`. L'en-tête est limité à `/books_reader/`, absent sur la racine et CogniAI, et les CSP propres de UX-UI et Data Science Explorer restent inchangées. Persistance confirmée après deux redéploiements, conteneur final `zg4880k00soco08c4wkg48ks-20261104T154607`.

## [1.8.6] - 2026-11-04
### Modifié
- **JSX précompilé, Babel retiré du runtime** : `scripts/build_jsx.js` compile les 10 fichiers JSX vers `js/dist/*.js` avec le runtime React classique. Chaque sortie est encapsulée dans une IIFE pour préserver l'isolation des portées. Babel est déplacé dans `scripts/vendor/babel.min.js`, reste un outil de build et n'est plus copié dans le miroir. `sync-to-platform.ps1` régénère la sortie et refuse un `--check` désynchronisé.
- **Premier chargement nettement allégé** : 1,64 à 2,09 Mo et 49 à 57 requêtes selon les polices effectivement chargées, contre 4 435 554 octets et 56 requêtes en 1.8.5. Les 2 345 370 octets de Babel (53 % du chargement précédent) disparaissent du réseau. LCP local mesuré entre 472 et 892 ms selon les runs, contre 1 468 ms.
- **Précache hors ligne complet** : le Service Worker précache l'app shell, `public/books.json`, les 66 introductions et chapitres, les 7 couvertures actives et les 7 fiches statiques, soit 122 entrées. Une navigation sans correspondance retombe sur l'app shell précaché. Les caches voisins de l'origine `hylst.fr` restent préservés.
- **CSP en balise meta** : politique `default-src 'self'`, `script-src 'self'`, `object-src 'none'`, `base-uri 'self'`, images et médias limités au même domaine, aux données et aux blobs. Les scripts de thème et d'enregistrement du Service Worker sont externalisés dans `js/theme-boot.js` et `js/sw-register.js`. Les styles inline restent autorisés pour les pages statiques et les attributs React.
- **Polices et musique locales** : l'index source utilise `/assets/fonts/fonts.css` comme la production, et les 282 pistes de `js/music_data.js` pointent vers `/hml/` au lieu de l'URL absolue. Aucune requête externe au premier chargement.
- **Retour de citation annoncé** : la confirmation « Citation copiée dans le presse-papiers » est exposée dans une région `role="status" aria-live="polite"`, avec la classe `.sr-only`.
- **Redirection 301 active** : le bloc Nginx `/books_reader/livres/<id>` vers `/books_reader/livres/<id>/` est ajouté à `nginx-coolify-reference.conf`, appliqué dans la base Coolify et dans le conteneur, puis testé en production le 04/11 avec conservation de la query.
- Version 1.8.6, cache Service Worker source `hylst-reader-v60`.

### Vérifié
- Build local final `f24c89706fb0` : 105 fichiers contrôlés, zéro tiret cadratin ou demi-cadratin, 205 fichiers runtime vérifiés, aucun dossier de travail dans le miroir.
- axe sans violation sur la bibliothèque (sombre, sépia, clair), la fiche livre, la liseuse, les paramètres, la modale À propos et la bibliothèque musicale. Zéro violation CSP et zéro erreur console sur tous les états testés.
- Hors ligne en profil vierge : bibliothèque, fiche livre, lecture de la préface, fiche statique de *Quinte* et changement de chapitre fonctionnent sans réseau. Cache final : 122 entrées, 66 contenus, 7 couvertures, 7 fiches.
- Imports TXT, JSON et EPUB testés après CSP : aucun blocage, aucun message d'erreur.
- Musique : lecture d'une piste depuis `/hml/`, bouton Pause actif, zéro violation CSP.
- Thème : bascule sombre, sépia et clair, mémorisation après rechargement, couleur d'interface mise à jour.
- Manifeste et icônes : 5 icônes PNG en 200, manifeste en 200. `.env`, `sources/`, `livres_pour_import/` et `scripts/` restent inaccessibles.
- Aucune requête externe, aucune requête échouée et aucune réponse HTTP en erreur au premier chargement.
- Production `https://hylst.fr/books_reader/` vérifiée après déploiement : build `f24c89706fb0` et SW `hylst-reader-f24c89706fb0` actifs, 9/9 URL du sitemap en 200, 7/7 fiches avec CSP et icônes, Babel et les sources `.jsx` en 404.
- Production, premier chargement propre : 1 330 388 octets transférés, 57 requêtes, 0 requête externe, 0 requête échouée, 0 erreur console, 0 violation CSP.
- Production, axe sans violation sur 9 états : bibliothèque sombre, sépia et clair, fiche livre, liseuse, paramètres, musique, fiche statique et page de droits.
- Production, citation annoncée en `aria-live`, sommaire au clavier avec changement de chapitre et retour du focus, thèmes mémorisés.
- Production, hors ligne en profil vierge : cache `hylst-reader-f24c89706fb0`, bibliothèque, fiche *Les Ficelles du bonheur* et fiche statique de *Quinte* accessibles sans réseau.
- Le 301 des fiches sans slash est actif : les 7 URL `/books_reader/livres/<id>` répondent 301 vers leur version avec slash, query conservée, et les versions avec slash restent en 200. Les autres applications de la plateforme restent en 200.


### Ajouté
- **Section « Citer ce livre »** sur les sept fiches statiques (`livres/<id>/`) : modèle de référence avec auteur, titre, année et URL, rappel de la courte citation avec mention, et lien vers la page de droits. Les fiches ne reproduisent jamais le texte intégral.
- **Section « Vos données »** sur `droits.html` : absence de cookie de mesure d'audience et de traceur publicitaire, stockage local des préférences et des livres importés, nature des journaux serveur, lien vers les mentions légales.
- **Icônes PWA en PNG** : `icon-32.png`, `icon-192.png`, `icon-512.png`, `icon-512-maskable.png` et `apple-touch-icon.png` (180 px), générées par `scripts/generate_pwa_icons.py`. Le manifeste déclare la variante `maskable` et l'index référence le favicon 32 px ainsi que l'icône iOS.

### Corrigé
- **Isolation des caches du Service Worker** : l'activation ne supprime plus que les caches préfixés `hylst-reader-`. Le stockage `caches` étant partagé par toute l'origine `hylst.fr`, les caches des autres applications (`accessibilite-*`, `ux-ui-*`, etc.) sont désormais préservés.
- **Accessibilité de la liseuse** : landmark `main`, bouton de fermeture du sommaire nommé, bouton de lecture de la barre musicale nommé. Le sommaire est utilisable au clavier (Entrée et Espace), avec `aria-expanded`, `aria-controls`, `aria-current`, déplacement du focus à l'ouverture et retour au bouton déclencheur à la fermeture. Les paramètres de lecture deviennent une vraie modale (`role="dialog"`, `aria-modal`, piège de focus, Échap, restauration du focus).
- **Accessibilité de la bibliothèque** : cartes importées activables au clavier (Entrée et Espace), zones d'import converties en boutons, cartes « À venir » sans `role="img"` abusif, suppression du bouton de zoom imbriqué dans les cartes (le zoom reste disponible sur la fiche du livre), couverture de fiche activable avec Entrée et Espace.
- **Accessibilité de la musique** : liste annoncée comme région, morceaux activables au clavier, bouton lecture nommé, pochettes décoratives sans texte alternatif redondant.
- **Contrastes** : couleur texte secondaire `--app-muted` assombrie à `#6f6862`, qui atteint le ratio 4,5:1 sur les fonds sépia et clair. Les trois thèmes passent axe sans violation.
- **Hiérarchie des titres de la modale À propos** : les sous-titres `h5` deviennent des `h4`, conformément à l'ordre des titres.
- **`droits.html`** : contenu principal dans un landmark `main`, retour à la bibliothèque dans un `nav` nommé.
- **Icônes des fiches statiques** : chaque fiche déclare le favicon PNG 32 px et l'icône iOS en chemins absolus. Chrome ne demande plus `/favicon.ico` à la racine du domaine, qui renvoyait 404.
- Version 1.8.5, cache Service Worker source `hylst-reader-v59`.

### Vérifié
- Build miroir `87ac090303b6` : 103 fichiers contrôlés, zéro tiret cadratin ou demi-cadratin.
- axe sans violation sur la bibliothèque (sombre, sépia, clair), la modale À propos (5 onglets), les paramètres globaux, la fiche livre, la liseuse (3 thèmes), la fin de chapitre, la visionneuse, la musique (sombre et sépia), la bibliothèque avec livre importé, `droits.html` et les fiches statiques.
- Clavier : cartes importées, morceaux de musique, sommaire, paramètres, Échap et restauration du focus, couverture de fiche.
- Manifeste : icônes PNG servies en 200, aucune erreur d'installabilité hors navigation privée.
- Caches : ancien cache `hylst-reader-*` supprimé, cache voisin non préfixé conservé.
- 7/7 fiches statiques affichent la section de citation et déclarent leurs icônes.
- Production `https://hylst.fr/books_reader/` vérifiée le 04/11 : build `87ac090303b6` et SW `hylst-reader-87ac090303b6` actifs, 7 fiches et 9/9 URL du sitemap en 200, icônes 200, citation et canonical présents, axe sans violation sur 11 états, sommaire au clavier avec changement de chapitre et retour du focus, paramètres par Échap, cache voisin préservé, 0 requête externe, 0 erreur console, 0 requête échouée, fumée 10 pages / 129 assets / 0 anomalie, `.env` 403, `sources/` et `livres_pour_import/` 404.

## [1.8.4] - 2026-11-04
### Ajouté
- **Sept fiches statiques indexables** (`livres/<id>/`) : titre, sous-titre, auteur, année, couverture, présentation issue de l'introduction, sommaire des chapitres, lien vers la liseuse, JSON-LD `Book` avec `hasPart` et `BreadcrumbList`, Open Graph et Twitter Card avec une image JPEG propre à chaque livre.
- **Citation copiable** sur chaque fiche de livre dans la liseuse : auteur, titre, année et URL de la fiche statique, avec retour visuel « Citation copiée » et repli `execCommand` si l'API Clipboard est indisponible.
- **Navigation navigateur** : ouverture d'un livre avec `history.pushState`, retour et avance gérés par `popstate`, bouton retour de la fiche qui revient à la bibliothèque sans quitter le site.
- **Accessibilité des modales** : fermeture par Échap, piège de focus, attributs `role="dialog"` et `aria-modal="true"`, restauration du focus sur l'élément déclencheur (À propos, Paramètres, Bibliothèque musicale).
- **Polices auto-hébergées** : Outfit et Merriweather dans `public/fonts/`, déclarations dans `css/book-fonts.css`. L'injection de Google Fonts au passage en thème sépia est supprimée, y compris pour les livres qui utilisaient Merriweather.
- **Manifeste PWA** : `id`, `start_url` et `scope` alignés sur `./`, soit la racine `/books_reader/`.
- **Sitemap** : les sept livres pointent vers leurs fiches statiques.

### Corrigé
- **Fiches statiques sans slash final** : les liens internes sont désormais absolus (`/books_reader/...`) et fonctionnent avec ou sans slash, au lieu de pointer vers la racine du domaine.
- **Livres importés** : plus de mention de droits ni de bouton de citation attribués à Geoffroy Streit ; le titre du livre reste affiché dans l'onglet, le canonical reste la bibliothèque et l'URL ne change pas.
- **Dimensions des couvertures** : les fiches statiques déclarent la largeur et la hauteur réelles de chaque image.
- **Empreinte de build** : `sw.js` entre dans le calcul de l'empreinte. Une modification du Service Worker renouvelle donc le cache, même sans autre changement.
- **Mention 1.8.3 du cache source** : corrigée, le cache source était resté `hylst-reader-v56`.
- Version 1.8.4, cache Service Worker source `hylst-reader-v58`.

## [1.8.3] - 2026-11-04
### Ajouté
- **Page « Droits d'auteur & intelligence artificielle »** (`droits.html`) : propriété intellectuelle, usages autorisés (lecture, courte citation avec mention, partage du lien), usages interdits, réserve de fouille de textes et de données (TDM), signalement des usages non autorisés, statut des illustrations générées ou assistées par IA.
- **Onglet « Droits »** dans la modale À propos, avec résumé autorisé/interdit et lien vers la page complète.
- **Mention de paternité en pied de page** : `© 2026 Geoffroy Streit · Tous droits réservés` et lien « Droits & IA ».
- **Métadonnées de paternité et de réservation** : `copyright`, `rights`, `tdm-reservation`, `tdm-policy`, `rel="license"`, `robots` enrichi de `noai` et `noimageai`.
- **Référencement** : canonical, Open Graph complet (image absolue 1200×630, dimensions, texte alternatif), Twitter Card `summary_large_image`, données structurées JSON-LD (`WebSite`, `Person`, `CollectionPage`, sept `Book`), repli `<noscript>` listant les œuvres, titre `<h1>` et sections `<h2>`, titre d'onglet contextualisé par livre.
- **Image sociale 1200×630** composée par `scripts/make_social_share.py` (fond sombre, titre, quatre couvertures en éventail).

### Corrigé
- **Bibliothèque musicale** : la grille réservait en permanence une colonne de 340 px pour le lecteur, même sans piste sélectionnée, ce qui laissait un grand vide à droite en plein écran. La colonne n'est plus réservée que lorsqu'une piste est active (`.music-player-layout.without-player`).
- **Manifeste PWA** : `background_color` et `theme_color` passés au sombre (`#0f0e0c`) pour éviter un écran de démarrage blanc.
- **Fuite de contenus de travail** : `sources/`, `livres_pour_import/`, les scripts de génération et la documentation de développement ne sont plus servis depuis le miroir de production. Le script de synchronisation les supprime et refuse de continuer s'ils réapparaissent.
- Version 1.8.3, cache Service Worker source inchangé `hylst-reader-v56` (le miroir de production utilise l'empreinte de build).

## [1.8.2] - 2026-11-04
### Modifié
- **Mode sombre par défaut** : la bibliothèque s'ouvre désormais en thème *Sombre*. Le thème est appliqué sur `<html>` (`data-theme="dark"`) et par un script d'amorçage en tête de document, avant le premier rendu, pour supprimer tout éclair sépia au chargement.
- **Choix mémorisé respecté** : un thème enregistré (Sépia, Clair ou Sombre) est réappliqué avant peinture ; seuls les visiteurs sans préférence voient le mode sombre.
- **Couleur de la barre navigateur** : `theme-color` suit le thème actif (`#0f0e0c` en sombre, `#faf4e8` en sépia, `#fafaf8` en clair), y compris lors d'un changement de thème en cours de session.
- **Cohérence des replis** : les thèmes invalides retombent sur le mode sombre (`DEFAULT_SETTINGS.theme`) au lieu de Sépia.
- Version 1.8.2, cache Service Worker source `hylst-reader-v56`.

## [1.8.1] - 2026-11-04
### Ajouté
- **Direction A « Cabinet de curiosités »** : ambiance visuelle atelier d'écriture et reliure, tranches de livres avec ombre de reliure, badges cachet de cire rouge (« Nouveau ») et ambre technique (« En chantier »), cartes À venir style dossier d'atelier avec trombone décoratif, étiquettes de catalogue en laiton.
- **Carnet de bord de l'auteur** : intégration du texte lyrique avec autodérision en tête de section « À venir », et citation dans la modale À propos.
- **Visionneuse plein écran (`ImageLightbox.jsx`)** : agrandissement au clic de toutes les couvertures de la bibliothèque, fiches de livre, illustrations d'articles et miniatures du sommaire, avec gestion accessible (piège de focus, touche Échap en phase de capture).
- **Couvertures d'histoires en 512×800** : récupération des 29 couvertures Wattpad d'origine en haute résolution WebP (2,5 Mo pour l'ensemble).
- **Grille élargie** : taille des cartes portée à `minmax(260px, 1fr)`, colonne de couverture de fiche livre élargie et illustrations de chapitres portées à 360 px.
- **Quinte ou Les Harmoniques de l'Âme** : titre officiel avec accent circonflexe sur Âme, badge *En chantier*, chronologie 2021-2024, épigraphe avec graphie stylisée, tags techniques, suppression du paragraphe dupliqué en tête de partie 4 et enrichissement acoustique/modal.
- **Scanner typographique (`scripts/check_dashes.py`)** : outil de contrôle et garde-fou intégré dans `scripts/sync-to-platform.ps1` interdisant tout tiret cadratin ou demi-cadratin dans les contenus servis et les interfaces.

### Corrigé
- **Règle zéro tiret étendue à toute la bibliothèque** : suppression des 21 tirets cadratins/demi-cadratins résiduels dans les chapitres 1, 3, 4 et 5 de *L'Odyssée de l'IA*, correction du texte alternatif de couverture dans `BookHomeView.jsx`.
- **Archivage des versions complète et imprimable** de *L'Odyssée de l'IA* dans `sources/odyssee_ia/` pour garantir que 100 % des contenus servis sont contrôlés et à jour.
- Version 1.8.1, cache Service Worker source `hylst-reader-v55`.

## [1.8.0] - 2026-11-04
### Ajouté
- **Nouveau nom** : l'application devient **La Bibliothèque de Hylst**, avec le nom court PWA **Biblio Hylst** et la signature « Livres, proses, poésies et récits de Geoffroy Streit ». Le titre, le header, le footer, la modale À propos, le manifeste, les icônes PWA, les métadonnées sociales et la documentation sont alignés.
- **Alias `/bibliotheque/`** : la nouvelle URL courte redirige en 301 vers `/books_reader/`, query string conservée. L'URL existante reste canonique pour ne casser ni les favoris, ni le référencement.
- **Quinte ou Les Harmoniques de l'Âme** : nouvelle en sept parties dans sa version remaniée par l'auteur, avec introduction, provenance et métadonnées `authorship: human`, `aiAssisted: false`.
- **Illustrations des 29 textes** : récupération des couvertures Wattpad d'origine, affichées en tête de chapitre et en miniature dans le sommaire.
- **Badge Nouveau** sur *L'Odyssée de l'énergie* et sur *Quinte*.

### Corrigé
- **Voile sur le header et la bibliothèque** : l'ambiance visuelle passait au-dessus du contenu et délavait le titre, les libellés de section et le haut des cartes, surtout en thème clair. Elle est désormais peinte derrière le contenu, avec un voile clair atténué et un header plus opaque.
- **Tirets cadratins de l'interface** remplacés par des points médians dans les libellés de la bibliothèque et de la modale À propos.
- Version 1.8.0, cache Service Worker source `hylst-reader-v54`.

## [1.7.1] - 2026-11-03
### Corrigé
- **Tirets cadratins et demi-cadratins supprimés** dans les 29 textes importés, y compris les dialogues et la ligne « à suivre ». Ils sont remplacés par des traits d'union, sans toucher aux mots.
- **Intégrité des textes restaurée** : les deux lignes de titre qui avaient été retirées (`Instants d'Automne`, `Elle ne lui répond...`) sont de nouveau présentes, sous forme d'épigraphe. Le contrôle mot à mot donne désormais 0 écart avec les versions Wattpad.
- **Mention de provenance corrigée** : les textes sont intégralement écrits par Geoffroy Streit (Hylst), sans assistance d'intelligence artificielle. Seule la conversion technique et la mise en page ont été outillées.
- **Métadonnées explicites** : `authorship: human` et `aiAssisted: false` pour les trois recueils et pour *Les Ficelles du bonheur*.
- Version 1.7.1, cache Service Worker source `hylst-reader-v53`.

## [1.7.0] - 2026-11-03
### Ajouté
- **Trois recueils Wattpad** : 29 textes publiés entre mars 2021 et février 2024, réunis en trois volumes :
  - *Saisons, nature & contemplations* (11 textes) ;
  - *Fantasque & merveilleux* (8 textes) ;
  - *Cœurs, chaos & quotidien* (10 textes).
- **Provenance conservée** : chaque chapitre indique sa date de publication et renvoie à sa version originale sur Wattpad. Le dossier `sources/wattpad/manifest.json` conserve les identifiants, dates et URL des 29 histoires.
- **Couvertures composées** à partir des illustrations Wattpad de l'auteur, avec une identité graphique propre à chaque tome.
- **Mise en page poésie** : strophes compactes, alignées à gauche et non justifiées, avec conservation des retours de ligne.
- **Note de source** discrète en fin de chaque texte.

### Modifié
- Retrait de la carte « Recueils de proses et poésies fantasques » de la section « À venir », désormais remplacée par les trois volumes intégrés.
- Version 1.7.0, cache Service Worker source `hylst-reader-v52`.

### Vérifié
- 6 livres actifs, 19 cartes « À venir », 0 doublon.
- 11/11, 8/8 et 10/10 chapitres parcourus, `FIN DU LIVRE` sur chaque tome, 0 erreur console.

## [1.6.3] - 2026-11-03
### Corrigé
- **Sommaire de *L'Odyssée de l'IA*** : `Preface` → `Préface`, aligné sur le titre réel du chapitre (`Préface de l'Auteur`).
- Version 1.6.3, cache Service Worker source `hylst-reader-v51`.

## [1.6.2] - 2026-11-03
### Corrigé
- **Carte fantôme dans « À venir »** : *L'Odyssée de l'énergie* n'apparaît plus une seconde fois dans les contenus en préparation. L'entrée codée en dur a été retirée de `LibraryView.jsx`.
- **Garde-fou anti-doublon** : une œuvre déjà intégrée ne peut plus réapparaître dans « À venir », même si son titre est saisi avec une casse, des accents ou des apostrophes différents.
- **Coquilles visibles de la bibliothèque** : `Bientot` → `Bientôt`, `Oeuvres` → `Œuvres`, `frustrastions` → `frustrations`, `claivoyances` → `clairvoyances`.
- Version 1.6.2, cache Service Worker source `hylst-reader-v50`.

## [1.6.1] - 2026-11-03
### Corrigé
- Coquilles résiduelles dans *L'Odyssée de l'énergie* : `Meta n't pas` → `Meta n'a pas`, `une installateur` → `un installateur`, `devenu son uniforme` → `devenue son uniforme`, `peu de perte mécanique` → `peu de pertes mécaniques`, `modeler la production` → `modéliser la production`, `demande correlated` → `demande corrélée`, `satellites atteint` → `satellites atteints`.
- Ligatures typographiques : `main-d'oeuvre` → `main-d'œuvre`, `coeur` → `cœur`, `noeuds` → `nœuds`, `container maritime` → `conteneur maritime`.
- Version 1.6.1, cache Service Worker source `hylst-reader-v49`.

## [1.6.0] - 2026-11-03
### Ajouté
- **Les 10 chapitres de *L'Odyssée de l'énergie* sont disponibles** : préambule, introduction, chapitres 1 à 8. La navigation de fin de partie et la pastille `n / 10` fonctionnent sur l'ensemble du livre.
- **Relecture orthographique et grammaticale complète** : accents rétablis, coquilles et accords corrigés, tirets cadratins et demi-cadratins supprimés, ornements `✦` retirés.

### Modifié
- **Données actualisées** : AIE 485 TWh en 2025 et environ 950 TWh en 2030, Irlande 22 % de son électricité en 2024, parc nucléaire français 57 réacteurs et 63 GW pour un âge moyen d'environ 39 ans, CATL environ 39 %, 39 réacteurs chinois en construction, coûts du solaire en baisse d'environ 90 % depuis 2010.
- **Titres de chapitres** : les entrées du sommaire reprennent les titres réels (`I. La faim électrique`, `II. L'inflation des besoins`, etc.).
- **Mention de transparence IA** : encart discret en bas de la dernière de couverture.
- Version 1.6.0, cache Service Worker source `hylst-reader-v48`.

### Corrigé
- Accents manquants dans les chapitres 5 à 8, notamment les passés composés, les prépositions `à` et les adjectifs.
- Coquilles et accords signalés par la relecture : `publie` → `publiées`, `considerabel` → `considérable`, `neglege` → `négligé`, `environmentales` → `environnementales`, `dedicees` → `dédiées`, `incrementales` → `incrémentales`, `confinée` → `confinées`, entre autres.

## [1.5.0] - 2026-11-03
### Ajouté
- **Accès sans slash final** : `https://hylst.fr/books_reader` fonctionne désormais comme `https://hylst.fr/books_reader/`, grâce à une base d'URL explicite dans l'index de production. Le redirect 301 canonique reste recommandé côté Nginx.
- **Transparence IA** : *L'Odyssée de l'énergie* affiche en bas de sa dernière de couverture une mention discrète précisant l'usage d'outils d'intelligence artificielle comme assistants de recherche, de documentation, de vérification des sources, de brainstorming et de rédaction.

### Modifié
- **L'Odyssée de l'énergie** : actualisation des données structurantes (AIE avril 2026 : 485 TWh en 2025, ~950 TWh en 2030 ; Irlande 22 % de son électricité en 2024 ; parc nucléaire français 57 réacteurs / 63 GW, âge moyen ~39 ans ; CATL ~39 % ; 39 réacteurs chinois en construction).
- **Typographie** : suppression de tous les tirets cadratins et demi-cadratins ainsi que des ornements `✦` dans les textes de *L'Odyssée de l'énergie*.
- **Chapitres** : titres et tableaux corrigés (cohérence 57 réacteurs / 63 GW, 39 ans), note de méthode datée au 3 novembre 2026.
- Version 1.5.0, cache Service Worker source `hylst-reader-v47`.

### Corrigé
- `.../books_reader` sans slash ne chargeait plus l'application (CSS et vendor résolus à la racine).

## [1.4.0] - 2026-11-03
### Ajouté
- **Navigation de fin de partie** : un bloc « Fin de la partie » avec le titre de la partie suivante est désormais intégré au flux de lecture, sous le dernier paragraphe. Il est visible même quand la barre d'outils est masquée.
- **Pastille de secours** : en lecture immersive ou plein écran, quand les commandes sont masquées, une pastille discrète `1 / 7 · Suivant` reste visible en bas de l'écran. Elle permet d'afficher les commandes ou de passer directement à la partie suivante.
- **Fin du livre** : dernier chapitre avec bloc « Fin du livre » et retour à la fiche.

### Modifié
- Intro des *Ficelles du bonheur* : byline `2025/26`, mention « Texte intégral ».
- Version 1.4.0, cache Service Worker source `hylst-reader-v46`.

## [1.3.1] - 2026-11-03
### Modifié
- **Corrections de coquilles** dans *Les Ficelles du bonheur*, sélectionnées par l'auteur : « une promesse en quelques années » → « une promesse quelques années », « Imaginez-vous », « pêle-mêle », « dit-on », « nous regarde, Auguste », guillemets fermants, « N'est-ce pas », « ainsi, ne pense-t-elle pas », « compte-t-elle. », « un peu... », « jusqu'au menton, lui faisant », « depuis cette année-là qu'on », « toujours fait... », « aux lèvres », « Je le sais, Odette. », « un hoquet », « moult postillons », « le carton », « suit du regard », « j'ai l'impression que », « touchant chez eux. »
- **Couverture illustrée** : génération locale avec Qwen-Image-2.1 (`qwen-image-21-uc-sdcpp`), format 5:6, sans texte. Elle remplace la couverture typographique de secours pour ce livre.
- L'intro précise désormais « Texte intégral, avec corrections de coquilles. »
- Version 1.3.1, cache Service Worker source `hylst-reader-v45`.
- Note : en production, `scripts/sync-to-platform.ps1` remplace ce nom par l'empreinte de build (`hylst-reader-d9e7b736999a` pour ce build).

## [1.3.0] - 2026-11-03
### Ajouté
- **Les Ficelles du bonheur** : nouvelle pièce de théâtre pour Halloween (29 octobre 2025), intégrée en 7 chapitres (six tableaux et un épilogue). Le texte est conforme au manuscrit DOCX, sans correction ni réécriture.
- **Didascalies bleues** : les passages en bleu du Word sont conservés et stylés via `.scene-description` / `.scene-description-inline`, avec une couleur adaptée aux thèmes Sépia, Clair et Sombre.
- **Mise en page théâtre** : les répliques sont alignées à gauche (`.chapter-paragraph.dialogue`), les didascalies ont un filet bleu discret.
- **Lien direct** : `?book=les-ficelles-du-bonheur` ouvre directement la fiche du livre.
- **Couverture typographique de secours** pour les livres sans image, avec badge `Nouveau`.
- CSS : styles de didascalies, répliques et ligne de crédit (`chapter-byline`).

### Modifié
- `public/books.json` : trois livres intégrés (IA, Énergie, Ficelles du bonheur).
- `LibraryView` et `BookHomeView` : fallback de couverture et badge.
- Version 1.3.0, cache Service Worker `hylst-reader-v44`.

## [1.2.1] - 2026-11-02
### Sécurité
- **Dépendances auto-hébergées** : React 18.3.1, ReactDOM 18.3.1, Babel 8.0.9, idb-keyval 6.3.0, epub.js 0.3.93, JSZip 3.10.2 et DOMPurify 3.4.17 dans `vendor/`. Plus aucun CDN JavaScript au runtime.
- **Assainissement des imports** : DOMPurify filtre les EPUB, dossiers HML et JSON importés (scripts, iframes, gestionnaires d'événements, URL `javascript:`). Les textes TXT/MD sont échappés avant conversion HTML.
- **Défense en profondeur** : `BookHomeView` et `ReaderView` re-filtrent les livres importés déjà présents dans IndexedDB.
- **Liens externes** : `rel="noopener noreferrer"` sur les liens `target="_blank"` du modal À propos.
- **CVE** : vérification OSV du 2026-11-02, aucune vulnérabilité connue pour les versions retenues. JSZip passe de 3.10.1 à 3.10.2.

### Ajouté
- `js/sanitize.js` : helper `HylstSanitize` (`sanitizeHtml`, `sanitizeBook`, `escapeHtml`).
- `vendor/LICENSES.md` : versions, licences et empreintes SHA-256 des dépendances.
- `scripts/sync-to-platform.ps1` : synchronisation sûre vers `Cours_Memos/Docker/books_reader`, cache-busting par empreinte de build, vérifications, suppression du `.env` du miroir, commit local optionnel sans push.

### Corrigé
- `gen_music_data.py` produit désormais `const MUSIC_LIBRARY` + `window.MUSIC_LIBRARY` (au lieu d'un `export` incompatible avec le chargement par balise `<script>`).
- Piste **Dreamlike Embrace** : référence corrigée en `dreamlike_embrace.mp3/.webp` (l'ancien nom `dreamlike_embracemp3` n'existait pas dans `/hml/`).
- **Signets** : `removeSignet` filtre désormais sur `chapterIdx` au lieu d'un `id` inexistant, ce qui supprimait tous les signets du livre.
- Cache Service Worker bumpé : `hylst-reader-v43` en source, empreinte de build en production.

## [1.2.0] - 2026-05-30
### Ajouté
- **Chapitre 5 Intégré** : Intégration officielle du chapitre 5 *« De Spectateur à Architecte »* de l'essai **L'Odyssée de l'IA** (`chapitre-5.html` dans `public/books` et dans `livres_pour_import`).
- **Nettoyage Littéraire** : Réécriture complète des tirets cadratins et retrait des ornements `✦` qui font trop « généré par IA » pour un rendu plus naturel et fluide.
- **Remplacement de « Dualis-IA »** par la dénomination officielle de l'essai : *« L'odyssée de l'IA : 2 futurs, un choix »* (ou tournures de phrases adaptées comme « ce projet », « ce livre »).
- **Couverture Chapitre 5** : Génération de l'illustration manquante `chapitre-5-cover.webp` en WebP dans un style artistique premium sépia/or homogène avec les 4 précédents chapitres.
- **Documentation Technique Complète** : Création de `structure.md` (arborescence), `features.md` (fonctions), `readme-dev.md` (architecture) et `test_build_deploy.md` (guide pas-à-pas pour Windows local et déploiement VPS Hostinger + Coolify + Nginx statique dans `/books_reader/`).

### Modifié
- **Modularisation React Majeure** : Division du fichier unique massif `js/app.jsx` (2000 lignes) en composants ES6 réutilisables chargés par Babel en ligne dans `js/components/` (`Icon.jsx`, `Ambience.jsx`, `AboutModal.jsx`, `GlobalSettingsModal.jsx`, `MusicPlayerModal.jsx`, `LibraryView.jsx`, `BookHomeView.jsx`, `ReaderView.jsx`). `js/app.jsx` est allégé et plus lisible (ramené à 380 lignes).
- **Service Worker Offline** : Optimisation du fichier `sw.js` (Cache v1.2.0) pour mettre en cache les requêtes de CDN externes (`unpkg.com`, `cdn.jsdelivr.net`, etc.) avec une stratégie Cache-First, rendant l'application 100% autonome et résiliente hors-ligne.
- **README.md & about.md** : Actualisation des descriptifs du projet et de la stack.

## [1.1.12] - 2026-03-03
### Corrigé
- **Animations d'ambiance** : Correction définitive de la visibilité des effets en forçant la transparence des conteneurs de texte et en boostant l'opacité et le contraste des calques d'animation. Le z-index a été réorganisé pour garantir que l'ambiance soit toujours visible sous le texte.
- **Temps de lecture** : Déplacé à l'intérieur de la barre de navigation inférieure (au centre, à gauche du compteur de chapitre) pour éviter tout chevauchement avec les boutons de saut de page.
- **Nettoyage UI** : Suppression de l'ancien indicateur flottant et des badges redondants en haut de page.

## [1.1.11] - 2026-03-03
### Corrigé
- **Animations d'ambiance** : Correction du problème de z-index qui rendait les animations invisibles. Elles sont maintenant visibles dans tous les modes (Sépia, Clair, Sombre).
- **Temps de lecture** : Déplacement de l'indicateur en bas à droite de l'écran (visible uniquement au clic/touch) pour plus de discrétion et d'utilité.

### Ajouté
- **Indicateurs paramétrables** : Nouveaux réglages pour activer/désactiver l'affichage du temps restant et du pourcentage de progression dans le slider.
- **Slider pourcentage** : Affichage dynamique du pourcentage de lecture au niveau du curseur de défilement.

## [1.1.10] - 2026-03-03
### Corrigé
- **Lecture (layout)** : Correction du rendu du mode lecture perturbé par la couche d’ambiance (empilement/z-index stabilisé, affichage de contenu restauré).
- **Mode Sombre** : Effet allégé pour éviter le voile trop dense et améliorer le confort visuel.
- **Mode Clair** : Effet rendu visible avec halos très subtils et particules discrètes.

### Modifié
- **Mode Sépia** : Remplacement des bandes trop marquées par des nappes lumineuses douces et lentes, mieux intégrées au style littéraire.
- **Animations ambiantes** : Particules moins nombreuses, plus lentes, plus légères GPU/CPU, dérive réduite pour un mouvement plus naturel.
- **Transitions d’ambiance** : Opacités et amplitudes ajustées pour des animations progressives, qualitatives et non intrusives.

### À faire
- Ajouter un réglage utilisateur “Intensité ambiance” global (faible/moyen/élevé).
- Ajouter un preset “Lecture longue” qui réduit automatiquement l’animation.

## [1.1.9] - 2026-03-03
### Ajouté
- **Animations par thème** : Nouveau réglage dans les modals de paramètres pour activer/désactiver indépendamment les animations de fond en Sépia, Clair et Sombre.
- **Ambiance différenciée** : Trois identités visuelles distinctes selon le thème (onde chaleureuse en Sépia, halo clair en mode Clair, aura + scintillement en mode Sombre).

### Modifié
- **Bloc Continuer/Reprendre** : Refonte complète du composant avec hiérarchie typographique, meilleure lisibilité du titre, troncature élégante et CTA premium.
- **Paramètres UI** : Boutons de thème harmonisés avec icônes du design system (sans emoji), cohérence renforcée avec les tokens existants.
- **Ambiance en lecture** : Les animations de fond sont désormais visibles dans ReaderView et non uniquement dans les écrans bibliothèque/modals.

### Corrigé
- **Visibilité Sépia** : Intensité et contraste ajustés pour rendre l’ambiance perceptible sans nuire au confort de lecture.
- **Persistance settings** : Normalisation des préférences d’animation par thème dans les settings sauvegardés.
- **Cache** : Bump cache-busting vers `v1.1.9` et Service Worker `hylst-reader-v9` pour forcer la prise en compte des nouveaux styles.

### À faire
- Ajuster un slider de densité des effets pour un contrôle fin de l’intensité visuelle.
- Ajouter un preset “Mode minimal” (animations ultra-subtiles) pour les longues sessions de lecture.

## [1.1.0] - 2026-03-03
### Ajouté
- **Bibliothèque Musicale** : Accès direct aux compositions de Geoffroy Streit.
- **Lecteur Audio** : Contrôles avancés (Play/Pause, Loop, Mini-bar header, animations de vagues).
- **Menu Settings** : Personnalisation de l'expérience de lecture (taille police, thèmes, alignement).
- **Import Header** : Bouton d'accès rapide à l'importation de dossiers HML.

### Modifié
- **UI Redesign** : Passage à une largeur de modal de 1100px pour la musique.
- **Organisation** : Séparation claire entre la "Bibliothèque Hylst" et "Vos autres lectures".
- **Documentation** : Mise à jour complète de `README.md`, `resume.md` et `about.md`.

### Corrigé
- Bug de disparition du bouton Settings.
- Problème de filtrage des livres importés (`isImported` property).

## [1.1.1] - 2026-03-03
### Modifié
- **Cartes livres** : Grille élargie pour éviter les cards trop étroites.
- **Modals** : Refonte des styles pour restaurer hiérarchie et lisibilité.
- **Bibliothèque musicale** : Harmonisation des classes CSS avec le rendu réel.

### Corrigé
- Scroll vertical restauré dans la bibliothèque.
- Dégradations visuelles sur About, Settings et Music.
- Bouton pause parasite retiré de la bibliothèque musicale.

### À faire
- Vérifier le responsive sur vieux mobiles après ce correctif.

## [1.1.2] - 2026-03-03
### Modifié
- **Cards livres** : Hauteurs normalisées via conteneur couverture.
- **Layout** : Chaîne de hauteur corrigée pour le scroll bibliothèque.

### Corrigé
- Erreur `idb` non défini lors du chargement.
- État audio stabilisé si un flux distant échoue.

## [1.1.3] - 2026-03-03
### Modifié
- **Cards bibliothèque** : Hauteur réduite et densité visuelle ajustée.
- **Section À venir** : Texte enrichi en deux paragraphes.
- **Mini player** : Ouverture par clic sur la miniature/titre + aperçu au survol.

### Corrigé
- Indicateur loop rendu visuel et durable via alternance d’icônes.

## [1.1.8] - 2026-03-03
### Ajouté
- **Ambiance Visuelle** : Effet de grain de papier animé et poussière flottante discrète dans les modes Sépia et Sombre pour une immersion renforcée.
- **Mode Immersion** : Bouton plein écran dans le lecteur pour masquer l'interface du navigateur.
- **Temps de lecture dynamique** : Affichage du temps restant estimé pour finir le chapitre, mis à jour en temps réel selon votre progression.

### Modifié
- **About Modal** : Refonte complète du design. Le modal est plus large (1100px), mieux structuré et responsive. Correction des problèmes de troncature de texte.
- **Icônes** : Ajout des icônes Maximize/Minimize pour le mode plein écran.

## [1.1.7] - 2026-03-03
### Corrigé
- **Crash AboutModal** : Correction de l'erreur React #130 causée par l'utilisation d'icônes non définies. Ajout de 10 nouvelles icônes au set global.

### Modifié
- **Documentation** : Mise à jour de `about.md` et `README.md` avec les nouvelles fonctionnalités.
- **Git** : Nettoyage du fichier `.gitignore` pour une meilleure gestion du repo.

### Suggestions & À venir (Backlog)
- **Import/Export** : Permettre l'exportation d'un livre (config + chapitres) au format ZIP pour partage.
- **Lecture** : Indicateur de temps de lecture restant pour le chapitre en cours.
- **Ambiance** : Ajout d'animations de fond discrètes (particules, dégradés animés) liées au thème.

## [1.1.6] - 2026-03-03
### Ajouté
- **Raccourcis Clavier** : Support complet pour la navigation (Espace pour scroller, Flèches pour changer de chapitre, Home/End pour sauter en haut/bas).
- **Redesign Modal About** : Nouvelle interface en onglets (À propos, Fonctions, Créateur, Astuces) avec un design plus moderne, interactif et informatif.

### Modifié
- **Recherche** : Suppression de la fonction de recherche intégrée au profit de la recherche native du navigateur (`Ctrl + F`), plus performante et universelle.
- **UI** : Amélioration de la fluidité des animations et des transitions de vue.

## [1.1.5] - 2026-03-03
### Modifié
- **Navigation** : Barre de navigation de chapitre (Précédent/Suivant) désormais fixe en bas de page, fusionnée avec les boutons de saut (Haut/Bas) pour une meilleure accessibilité.
- **Recherche** : Cliquer sur un résultat de recherche dans le chapitre en cours fait défiler la page jusqu'à l'occurrence avec un effet de surbrillance temporaire.

### Corrigé
- **Images chapitres** : Correction des liens brisés vers les couvertures de chapitres (réécriture dynamique des chemins relatifs).

## [1.1.4] - 2026-03-03
### Modifié
- **Settings** : Mise en page recentrée et cartes de réglages stylisées.
- **À venir** : Paragraphes enrichis en blocs avec effets et gradients.
- **Book Home** : Mise en page lisible et scrollable.
- **Typographie** : Normalisation des titres et paragraphes du lecteur.

### Corrigé
- **Lecteur** : Réactivation du scroll et des contrôles au tap.
- **Dropcap** : La capitale initiale n’agrandit plus tout le paragraphe.

## [1.0.0] - 2026-02
- Version initiale : Liseuse PWA, support HML, stockage IndexedDB, Mode Lecteur premium.
