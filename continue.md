# Continuation : La Bibliothèque de Hylst

Point d'étape pour un agent qui reprendrait ce travail. Fichier de travail, non servi par le lecteur.

## État au 8 novembre 2026

Version **1.8.48** déployée en production le 09/11, cache Service Worker source `hylst-reader-v99`, build `e309f3d1a65c`, cache `hylst-reader-e309f3d1a65c`. 404 fichiers runtime, sitemap à 14 URL, 12 livres, 156 chapitres. Régénération intégrale des 48 illustrations de chapitres d'Atrophie avec Flux 3 Klein (`flux3-klein-sdcpp`), zéro texte (audit Tesseract 0 violation sur 48/48), cache-busting `?v=5`. `verify-release.ps1` entièrement vert. 404 fichiers runtime, sitemap à 14 URL, 12 livres, 156 chapitres. Régénération intégrale de l'Acte 2 d'Atrophie (chapitres 13 à 24) avec Flux 3 Klein rehaussé (`flux3-klein-sdcpp`), zéro texte (audit Tesseract 0 violation), cache-busting `?v=5`. `verify-release.ps1` entièrement vert. 404 fichiers runtime, sitemap à 14 URL, 12 livres, 156 chapitres. Régénération intégrale de l'Acte 1 d'Atrophie (chapitres 01 à 12) avec Flux 3 Klein rehaussé (`flux3-klein-sdcpp`), zéro texte (audit Tesseract 0 violation), cache-busting `?v=5`. `verify-release.ps1` entièrement vert. 402 fichiers runtime, sitemap à 14 URL, 12 livres, 156 chapitres. Rehaussement décor et texture 35mm Atrophie (chapitres 01 et 06) avec Flux 3 Klein (`flux3-klein-sdcpp`), zéro texte (audit Tesseract 0 violation), cache-busting `?v=5`. `verify-release.ps1` entièrement vert. 402 fichiers runtime, sitemap à 14 URL, 12 livres, 156 chapitres. Régénération haute fidélité Acte 1 Atrophie (chapitres 01 à 12) avec Flux 3 Klein (`flux3-klein-sdcpp`), zéro texte (audit Tesseract 0 violation), cache-busting `?v=4`. `verify-release.ps1` entièrement vert. 402 fichiers runtime, sitemap à 14 URL, 12 livres, 156 chapitres. Enrichissement typographique et sémantique de la Partie III de la Neurodiversité (chapitres 08, 09, 11 : titres h2/h3, listes à puces, gras et italique). `verify-release.ps1` entièrement vert. 402 fichiers runtime, sitemap à 14 URL, 12 livres, 156 chapitres. Amélioration éditoriale et typographique d'*Approche de la Neurodiversité* (chapitres 05, 10, 12, 13, 14 réparés, chapitres 04 et 07 conservés, titres h2/h3). `verify-release.ps1` entièrement vert. 277 fichiers runtime, sitemap à 13 URL, 11 livres, 94 chapitres, 105 fichiers de contenu. Précache hors ligne complet : 322 entrées, 28 illustrations de chapitre, 16 couvertures de livres à venir, 77 fontes, environ 20 Mo. `verify-release.ps1` entièrement vert.

### Fait

- **Hors ligne complet (1.8.23, déployée)** : le Service Worker extrait les `<img>` des introductions et chapitres, précache les 28 illustrations et plans SVG, les 16 couvertures des livres à venir et les 77 fontes de la plateforme. Testé en profil Chromium vierge sur la production : bibliothèque, droits, 7 fiches avec et sans slash, liseuse des 7 livres, chapitre 1 et suivant, plans SVG, 0 image cassée, 0 réponse en erreur, 0 violation CSP.
- **Nightprowler 1.8.10** : introduction réécrite dans un ton d'hommage, six chapitres (I à VI), six illustrations de chapitre, sommaire à six entrées sur la page du livre, fiche statique et image Open Graph.
- **Nightprowler, chapitre VII (1.8.13, déployée)** : six fiches normalisées, Albert Degreffion et les cinq prétirés de la convention de 2011, avec portraits et conseils de jeu réécrits, valeurs d'origine et illustration de chapitre. Le sommaire de la fiche passe à sept entrées.
- **Nightprowler, chapitre VIII (1.8.14, déployée)** : le scénario du squelette enfoui, écrit vers 1999, restructuré en six actes, complété par la table des objets maudits, le marché des Veilleurs, la rencontre finale et ses trois issues, et une section « Mener la table ». Illustration de chapitre. Le sommaire de la fiche passe à huit entrées.
- **Nightprowler, chapitre IX (1.8.15, déployée)** : l'esclavage gouri, écrit en 1999-2000 et retapé en 2001, restructuré en cinq actes, avec le plan du camp redessiné en SVG (zones A à O), les six issues en tableau, les avertissements de contenu et une section « Mener la table ». Illustration de chapitre. Le sommaire de la fiche passe à neuf entrées.
- **Nightprowler, chapitre X (1.8.16, déployée)** : Vapeur et boulons, écrit pour la convention des Alchimistes de 2011, restructuré en cinq actes, avec le plan du moulin en SVG, la machine et la pierre de rosette décrites, le sort de Tramiel tranché et les issues en tableau. Illustration de chapitre. Le sommaire de la fiche passe à dix entrées.
- **Nightprowler, chapitre XI (1.8.17, déployée)** : La reconquête du trône des Rodallois, écrit en 1999 pour un autre jeu et clairement séparé de Nightprowler, restructuré en cinq actes, avec les quatre lois et les figures en tableaux, la vérité du pacte, les alliances, les preuves, les issues et une section « Mener la table ». Illustration de chapitre. Le sommaire de la fiche passe à onze entrées.
- **Nightprowler, chapitre XII (1.8.18, déployée)** : Pistes inachevées, trois titres de 1999 jamais développés (le camp barbare du prince démon, le contrôle d'entrée à choix, les aventures à Kalaar), proposés en 2026 sous forme de trois pages de jeu avec variantes et tables. Illustration de chapitre. Le sommaire de la fiche passe à douze entrées.
- **Nightprowler, chapitre XIII (1.8.19, déployée)** : Annexes, feuille de personnage vierge complète normalisée en tableaux HTML d'après `fichpers.htm`, lexique alphabétique de 23 termes attestés dans les textes et scénarios, chronologie documentée (avant 59, 2258, vers 2300, vers 2310, 2476, 2559) et inventaire des silences des sources. Illustration de chapitre. Le livre *Nightprowler, carnets de Samarande* est complet avec ses 13 chapitres et son sommaire à treize entrées.
- **Tome IV, *Carnets, réflexions & partages*** : quatre textes retrouvés, datés et légèrement réécrits. *Hygiène de vie* (23 novembre 2003), *Imaginez-vous* (19 juin 2007), *Idées cadeaux* (5 septembre 2008), *Marre d'apprendre* (vers 2024). Chaque chapitre porte sa date et une note de source.
- **Livre *Sciences et technologie*** : préface 2026, quatre parties avec résumé, sommaire d'origine et PDF. Les quatre PDF sont exportés depuis les `.docx` d'origine (A 21 pages, B 17, C 40, D 36), avec images et mise en page conservées. Manifeste `pdf/manifest.json`.
- **Catalogue** : 10 livres, 88 chapitres, 10 fiches statiques. Deux couvertures composées (600x900). Styles de téléchargement, sommaire et résumé ajoutés à `css/reader.css` et `css/book-page.css`.
- **Inédits littéraires (1.8.12, déployée)** : quatre escapades de 1995 (B2, C, D, E) insérées après « Escapade boisée » dans le Tome I, *Un brin d'écrit* (1996) en clôture du Tome I, *Farouches apparitions* (1999) et *La tanière du mage* (2020) dans le Tome II. Réécriture légère, dates d'origine et notes de source. La partie B, « À la campagne », reste au Tome III. Les couvertures des deux tomes annoncent « SEIZE TEXTES · 1995-2024 » et « DIX TEXTES · 1999-2024 », images Open Graph comprises.
- **Vérifications** : `check_dashes.py` sur 124 fichiers, `books.json` valide (10 livres, 88 chapitres), JSX compilé et à jour, 10 fiches générées, 268 fichiers runtime dans le miroir, 12 URL dans le sitemap, chapitre XIII et son illustration en 200 dans le miroir local. La production 1.8.19 est vérifiée avec son chapitre XIII et son illustration en 200.
- **Sources** : le dossier `D:\0HYLST\0 HYLST ART 2024\ecrits\textes_a_trier\` est rangé en quatre dossiers et inventorié dans `00_INVENTAIRE.md`. Rien n'a été supprimé.

### À faire, dans l'ordre

1. **Documents plateforme** : après chaque déploiement, vérifier que `changelog.md`, `securite.md`, `todo.md` et `hylst_IT_platform_content.md` n'ont pas été écrasés par l'agent de déploiement.
2. **Textes littéraires restants du corpus** : explorer et intégrer les inédits isolés des archives (`effet papillon.txt`, `Ariane.txt` / `.pdf`, `japonisant .odt` « Le rêve d'un gaijin profane »).

### Repères techniques

- Liens PDF : chemin absolu `/books_reader/public/books/sciences-et-technologie-jeux-videos/pdf/...`, identique dans la liseuse et dans la fiche statique.
- Les PDF ne sont pas précachés par le Service Worker ; seuls l'introduction, les chapitres, les couvertures et les fiches le sont.
- `public/books.json` est la source du catalogue et du précache. Toute nouvelle entrée doit être suivie de `python scripts/build_book_pages.py`, d'un bump de `CACHE_NAME` et d'une synchronisation.
- `css/book-page.css` est réécrit par `scripts/build_book_pages.py` : toute modification de style passe par la constante `STYLE` du script, pas seulement par le fichier CSS.
- Les scripts d'export Word COM utilisent `[System.IO.Path]::Combine`, jamais `Join-Path`, et un processus Word par partie.

## Dossier Nightprowler (archive de travail)

## 0. Deux chemins à ne pas confondre

- Racine du depot du lecteur : `D:\0CODE\AntiGravity\Hylst_Reader` (c'est la que vivent `public/`, `js/`, `css/`, `scripts/`).
- Archive des sources : `D:\0HYLST\0 HYLST ART 2024\ecrits\` (miroir du site de 2004, encodage cp1252).

Les commandes `git`, `python scripts/check_dashes.py` et `node scripts/build_jsx.js` se lancent depuis la racine du depot, pas depuis l'archive.

## 1. Ce que le livre doit etre

- Une entree unique dans `public/books.json`, identifiant `nightprowler-carnets-de-samarande`.
- Auteur : Geoffroy Streit. Corpus : ses ecrits Nightprowler, 1999 a 2011.
- Principe editorial fixe par l'auteur : ne reprendre que ce qui est de lui, corriger et completer, reecrire en son nom ce qui est trouve, en attendant qu'il retrouve ses propres versions plus evoluees. Les pages concernees portent une note disant qu'elles sont provisoires.
- Dossier cible : `public/books/nightprowler-carnets-de-samarande/`, chapitres HTML plats (`chapitre-N.html`), car la liseuse n'a pas de table des matieres imbriquee.

## 2. Corpus source mesure

Toutes les tailles et tous les comptes de mots ci-dessous ont ete mesures sur les fichiers, pas estimes. Les `.htm` sont en cp1252 et leur balisage est tres degrade (attributs `font size="2..."`, mots colles) : la reecriture manuelle est obligatoire.

| Fichier | Octets | Mots de texte | Date | Role |
|---|---|---|---|---|
| `hnp.htm` | 10 392 | 1 312 | 1999 | Presentation du monde de Samarande. Chapitre I. |
| `hnpaj.htm` | 61 050 | 6 964 | 2000 | FAQ de la mailing list, economie, Albert Degreffion. Chapitres II, III, VII. Contient aussi l'Atlas de Bejofa (exclu). |
| `hnpab.htm` | 6 542 | 646 | avant 2000 | Aide a l'ecriture de scenario. Chapitre IV. |
| `hnpsc.htm` | 16 184 | 1 904 | avant 2000 | Scenario du squelette enfoui. Chapitre VIII. |
| `aidcreapersos.htm` | 7 654 | 550 | non datee | Aide a la description des personnages, 15 registres. Chapitre V. |
| `combat.htm` | 23 722 | 2 748 | non datee | Ma version des regles de combat, inspiree de Mazzoni. Chapitre VI. |
| `fichpers.htm` | 6 784 | 447 | non datee | Deux fiches de personnages types. Chapitre VII. |
| `introsc.htm` | 2 644 | 240 | 1999 | Introduction du scenario Rodallois, autre jeu. Chapitre XI. |
| `scenar.htm` | 5 914 | 701 | 1999 | Scenario Rodallois, autre jeu. Chapitre XI. |
| `scenareg.rtf` | 314 665 | 3 044 utiles | 2001-07-02 | Scenario de l'esclavage gouri, version longue. Chapitre IX. |
| `scenaraf.rtf` | absent du dossier | 1 565 utiles | 2001-07-02 | Version courte, archive seulement, remplacee par `scenareg.rtf`. |
| `.docx` 2011 | 6 pages | 2 792 | 2011-04-22 | Scenario Vapeur et boulons. Chapitre X, base de travail `.md` dans `textes_a_trier`. |

## 3. Dates retenues, confirmees par l'auteur

- `hnp.htm` : 1999.
- `hnpaj.htm` : 2000.
- `hnpab.htm` et `hnpsc.htm` : un peu avant 2000, donc vers 1999.
- Esclavage gouri : redige en 1999-2000, retape en juillet 2001.
- Vapeur et boulons : avril 2011, quinzieme convention des Alchimistes.
- Rodallois : 1999, autre jeu, chapitre separe.

## 4. Plan de livraison, 13 chapitres

Partie I, le jeu (1999-2000)
1. Le monde de Samarande (`hnp.htm`), reecriture complete.
2. L'esprit du jeu, entretien de mailing list (`hnpaj.htm`), questions restituees et reponses en regard.
3. Vies et prix, economie et echoppes (`hnpaj.htm`), en tableaux.

Partie II, aides de jeu
4. Batir un scenario (`hnpab.htm`), liste tronquee a completer.
5. Decrire un personnage (`aidcreapersos.htm`), fait, voir section 8.
6. Le combat (`combat.htm`), reecrit et reorganise, version provisoire.
7. Figures et preretires : Albert Degreffion et les cinq personnages de 2011, en tableaux normalises. Version de l'auteur, inspiree de sources tierces, jamais une reproduction.

Partie III, scenarios
8. Le squelette enfoui d'Azefhfkrijiiir (`hnpsc.htm`), rencontre finale a ecrire.
9. Esclavage gouri sans vergogne (`scenareg.rtf`), restructure en actes, plan du camp redessine, zones A a O, six issues.
10. Vapeur et boulons (2011), plan du moulin absent, machine a decrire, artefact a expliquer, sort de Tramiel a trancher.
11. La reconquete du trone des Rodallois (`scenar.htm` et `introsc.htm`), autre jeu, chapitre clairement separe.
12. Pistes inachevees : camp barbare du prince demon, controle d'entree, Kalaar.

Annexes
13. Feuille de personnage vierge, lexique, chronologie 2258, 2300, 2476, 2559.

## 5. Textes tiers : aucun reproduit

- Atlas de Bejofa (Letorve) : exclu, aucun chapitre. Bejofa n'apparait que par les lieux traverses par les scenarios propres de l'auteur, quartier 30, ruelle des fripes, marche Fresnel, auberge du Soleil de Farande.
- Aide a la description (Hirrinkaël) : listes reprises, texte reecrit sous le nom de l'auteur, note de provisoire dans le chapitre.
- Regles de combat : la version publiee au chapitre VI est celle de l'auteur, inspiree de Mazzoni, pas une reproduction de son texte. Meme regle pour le chapitre VII : texte de l'auteur, inspiration tierce, pas de reproduction.
- Images du scenario 2011 : liens greluche.info et flickr, inutilisables, CSP `img-src 'self'` et droits non clairs. Plans a produire en SVG local ou WebP.

## 6. Regles projet a ne pas casser

- Ne jamais regenerer automatiquement les HTML de `public/books/` : correction manuelle.
- Zero tiret cadratin ou demi-cadratin, y compris dans les fichiers de travail. Controle : `python scripts/check_dashes.py --root .` Attention, ce script ne scanne pas les `.md` : les verifier a la main.
- Aucun CDN, aucune police distante, aucun script inline (CSP `script-src 'self'`). Tout script va dans `js/` et doit etre declare dans le precache de `sw.js`.
- Le Service Worker ne supprime que les caches prefixes `hylst-reader-`. Bump de `CACHE_NAME` a chaque version.
- `node scripts/build_jsx.js` puis `--check` si du JSX bouge.
- Synchronisation par `scripts/sync-to-platform.ps1`, qui preserve l'`index.html` de production et exclut les sources `.jsx` et Babel.
- Miroir de production : `D:\0CODE\AntiGravity\Cours_Memos\Docker\books_reader`, teste via `http://127.0.0.1:8765/books_reader/` et non depuis la racine source.
- Apres chaque version : `CHANGELOG.md`, `todo.md`, `antigravity.md`, puis `changelog.md`, `securite.md`, `todo.md` et `hylst_IT_platform_content.md` cote plateforme.

## 7. Integration technique (faite le 06/11/2026, a reprendre a chaque chapitre publie)

- Entree dans `public/books.json` : `id`, `title`, `subtitle`, `author`, `year` (2026 pour l'edition numerique, dates reelles dans l'intro), `design` avec fontes, couleurs et variables, `coverPath`, `introPath`, `chapters[]` avec `id`, `title`, `path`, `available`, puis `badge`, `authorship: "human"`, `aiAssisted: false`, `tags`.
- Modele complet a copier : entree `l-odyss-e-de-l-nergie` dans `public/books.json`.
- Couverture deja presente : `public/covers/cover_nightprowler.webp`.
- Retirer la vignette d'attente correspondante dans `js/components/LibraryView.jsx` (constante `FUTURE_BOOKS`, entree `f3`), sinon doublon.
- Les images de chapitre sont prefixees automatiquement par `transformChapterHTML` dans `js/components/ReaderView.jsx` : poser les fichiers dans le dossier du livre et referencer un chemin relatif.
- Bump de `CACHE_NAME` dans `sw.js`, puis verification dans le miroir.

Etat : l'entree est en place avec les chapitres I a VI, six illustrations de chapitre dans le style de la couverture, un sommaire a six entrees sur la page du livre, une introduction reecrite dans un ton d'hommage avec le lien Grog et les romans de Pierre Pevel, la fiche `livres/nightprowler-carnets-de-samarande/index.html` est generee, l'image Open Graph est produite, la vignette `f3` est retiree de `LibraryView.jsx`, le cache est en `hylst-reader-v66` en source et le miroir local est en build `c66ade22a32c` avec 222 fichiers runtime. La production est en 1.8.10, build `c66ade22a32c`, deployee le 06/11 avec les chapitres I a VI et l'introduction hommage. A refaire a chaque nouveau chapitre : ajout dans `chapters[]`, bump du cache, regeneration de la fiche par `python scripts/build_book_pages.py`.

- Le sitemap n'est pas dans le depot source : il vit dans le miroir `books_reader/sitemap.xml`. `sync-to-platform.ps1` met a jour les `lastmod` et complete automatiquement les fiches declarees dans `public/books.json` ; verifier quand meme le nombre d'URL apres chaque synchronisation.

Polices : seules `Outfit` et `Merriweather` existent dans `public/fonts`. Toute autre famille demanderait un telechargement par `scripts/fetch_book_fonts.py`, donc une nouvelle dependance locale : a eviter.

## 8. Etat reel au moment de cette note

Fait au 06/11/2026 :

- `intro.html` : presentation de l'edition, principe editorial, dates, hommage au jeu, lien vers la fiche du Grog, presentation du jeu (1995, Siroz ; 2006, 2d Sans Faces), quatre romans de Pierre Pevel parus en 1998 sous le pseudonyme de Pierre Jacq (*Premiers Sangs*, *La Voie du sang*, *Le Prix du sang*, *In memoriam*, cycle *Chroniques des sept cites*) et supplement *Memoires de Sang*. Mention des vingt-cinq ans, du style repris, du sommaire et des illustrations IA generees localement.
- `chapitre-1.html`, le monde de Samarande, d'apres `hnp.htm` (1999) : paragraphes restaures, orthographe corrigee, contenu inchange, tournures d'epoque gardees. Section « Ce que cette presentation ne dit pas » ajoutee en 2026 et signalee dans la note de source.
- `chapitre-2.html`, l'esprit du jeu, d'apres les cinq reponses de la mailing list dans `hnpaj.htm` (2000). Les questions des correspondants sont resumees, pas reproduites. Dernier paragraphe de 2026, signale dans la note.
- `chapitre-3.html`, vies et prix, d'apres les remarques economiques et l'inventaire d'echoppes de `hnpaj.htm` (2000), range en tableau par besoin. Tous les noms d'echoppes sont verifies contre la source : les variantes corrigees sont magazin vers magasin, chiromancin vers chiromancien, espio!ns vers espions, poissonier vers poissonnier, sculteurs vers sculpteurs, orticulteur vers horticulteur.
- `chapitre-4.html`, batir un scenario, d'apres `hnpab.htm` (vers 1999) : les quatre elements (lieu, moment, personnages, intrigue), les six autres cites, puis les mobiles en tableau. Le fichier d'origine s'arrete en pleine idee : les deux derniers paragraphes sont ajoutes et signales dans la note de source, ainsi que la section « Un exemple » ajoutee en 2026.
- `chapitre-5.html`, decrire un personnage, d'apres les 15 registres de `aidcreapersos.htm` : nez, regard, bouche et dentition, cheveux, peau, pilosite faciale, visage, corpulence, demarche, voix, accent, special, rire, idiosyncrasie, attitude. Listes fideles au fichier, decoupage et commentaires nouveaux, section « Trois traits, pas plus » ajoutee en 2026, note de provenance en fin de chapitre.
- `chapitre-6.html`, le combat, d'apres `combat.htm` : deux moteurs separes, l'action par action (degainer, rangs, attaques enchainees, defenses, contre-attaque, deux armes, penetration de garde, resistance des armes, attaques speciales) et l'echange en une phase de cinq secondes (initiative, taille des armes, Force, postures, resolution, blessures, armes de jet, volonte). Les incoherences du fichier d'origine sont listees en fin de chapitre, pas comblees. Note de provenance : texte de l'auteur, inspire de Mathieu Mazzoni, version provisoire.
- Illustrations : `chapitre-1-cover.webp` a `chapitre-6-cover.webp`, generees sur le GPU local (`D:/0CODE/ClaudeCode/wainsfw/main.py`, modele `z-image-turbo-sdcpp`, 1216x832, 114 a 197 Ko), dans le style de la couverture. Chaque chapitre I a VI ouvre sur son image.
- Integration : entree `nightprowler-carnets-de-samarande` dans `public/books.json` (8 livres au catalogue), badge En chantier, design Outfit et Merriweather, fiche statique generee, image Open Graph produite, sommaire a six entrees dans `BookHomeView` avec ouverture directe du chapitre choisi, `f3` retiree de `FUTURE_BOOKS`, cache `hylst-reader-v65`, sitemap du miroir complete a 10 URL avec la fiche Nightprowler et completion automatique dans `sync-to-platform.ps1`, 222 fichiers runtime dans le miroir en build `ca5f4163630e`, `CHANGELOG.md`, `todo.md` et `antigravity.md` a jour. Ajout CSS : `.chapter-stats-table.descripteurs td:first-child` aligne les etiquettes a gauche, `.book-home-toc` pour le sommaire.

Fait : verification hors ligne complete dans un profil Chromium vierge. Les 1.8.9 a 1.8.23 sont deployees (build `0b632e9d5101`, commit plateforme `f4da5092`). Les documents plateforme de la 1.8.18 sont ecrits et pousses (commit `6fcef7be`), a reverifier apres chaque redeploiement (l'agent plateforme peut les ecraser).
La suite a proposer : verification offline approfondie de Nightprowler dans un profil Chromium vierge ; rediger un message pour l'agent deployment / suivi des apps sur la plateforme Hylst IT (dossier Docker / container Nginx Statique pour VPS).

Point de methode : le corps d'un chapitre ne s'ouvre dans la liseuse que par un clic, aucun parametre d'URL ne cible un chapitre. Le rendu se controle donc sur une page d'apercu jetable qui charge `css/reader.css` et `css/book-fonts.css`, ou par capture d'ecran Chrome headless. Les extractions de travail vont dans `.extract/`, supprime apres usage.

## 9. Erratum utile

Une premiere version du chapitre V a ete ecrite avec des listes de descripteurs largement inventees (mots absents du fichier source, comme « pingouin », « psychanalytique », « chaldron », « guenon », « manucure », « phalange ») et quelques phrases incoherentes. Elle a ete integralement remplacee. Lecon a garder : sur ces sources cp1252 tres degradees, extraire le texte net dans un fichier intermediaire et verifier chaque liste mot par mot contre ce fichier avant de rediger.

## 10. Pieges connus

- Le dossier `ecrits\Jeu de rôle\` ne contient qu'une copie partielle. Les versions completes sont a la racine de `ecrits\`.
- Les `.htm` du miroir portent tous une date de modification de 2004 : inutilisable pour dater les textes. Se fier aux indications de l'auteur et aux metadonnees des RTF et DOCX.
- Le `.md` de `textes_a_trier` n'est pas un document a publier tel quel : c'est le DOCX de 2011 converti, avec cinq corrections (appesantir, lingots, sortiront, Maitresse, Environnement) et deux images en base64 inutilisables.
- Incoherences a trancher dans le corpus : Gromy ou Bromi, S'rhik ou S'rhie, K'ret ou K'rëtrr, Krieu'kr, Cassar ou Khaler, Umelorien ou Melorien, Strolicke.
- Orthographe a normaliser : ligonts vers lingots, apesantir vers appesantir, sortirons vers sortiront.
- `hnpaj.htm` contient 6 964 mots dont environ 4 500 pour la FAQ, 700 pour l'economie, 450 pour Albert Degreffion et le reste pour l'Atlas de Bejofa, exclu.
- Les tableaux du lecteur : `.chapter-stats-table` est stylee pour deux ou trois colonnes, `.chapter-table` est utilisee ailleurs avec des styles inline. Les deux fonctionnent.

## 11. Reprise

1. Lire cette note, puis extraire le texte net de la source du chapitre a traiter dans un fichier intermediaire UTF-8 hors du depot.
2. Verifier les listes et les faits contre ce fichier avant de rediger.
3. Ecrire le chapitre, sans tiret cadratin, avec la note de provenance si le texte vient d'un tiers.
4. Passer `python scripts/check_dashes.py --root .` apres chaque chapitre.
5. A la fin seulement, integrer `books.json`, l'intro et les annexes, puis bump du cache, sync et documents de suivi.

En cas de doute sur une decision editoriale, la consigne de l'auteur prime : ne reprendre que ce qui est de lui, reecrire en son nom, et signaler clairement ce qui est provisoire.
