# La Bibliothèque de Hylst

**La Bibliothèque de Hylst** est l'écrin numérique des livres, proses, poésies et récits de **Geoffroy Streit (alias Hylst)**. C'est une application web (PWA) *Offline-First* et *Pure Frontend*, qui reste aussi une liseuse capable d'accueillir vos propres lectures.

- Nom long : **La Bibliothèque de Hylst**
- Nom court (PWA) : **Biblio Hylst**
- Signature : **Livres, proses, poésies et récits de Geoffroy Streit**
- URL : `https://hylst.fr/books_reader/` (alias `https://hylst.fr/bibliotheque/`)
- Version : **1.8.22** (voir [CHANGELOG](CHANGELOG.md))


---

## 🌟 Points Forts

- **Expérience Premium** : Design typographique soigné (*Cormorant Garamond*, *Libre Baskerville*).
- **Musique Intégrée** : Accès à plus de 280 compositions originales de Geoffroy Streit directement dans l'app, filtrables par mood/BPM.
- **Partie V Intégrée** : Intégration du chapitre final *« De Spectateur à Architecte »* de l'essai **L'Odyssée de l'IA** (version nettoyée de ses tics typographiques d'IA).
- **Nouvelle Halloween** : *« Les Ficelles du bonheur »*, pièce de théâtre en six tableaux et un épilogue, avec didascalies bleues, répliques mises en page comme au théâtre et couverture illustrée générée localement.
- **L'Odyssée de l'énergie actualisée** : les 10 chapitres sont disponibles, avec données AIE 2026, typographie sans tirets cadratins ni ornements, et mention de transparence sur l'assistance IA en dernière de couverture.
- **Trois recueils** : 36 textes réunis en *Saisons, nature & contemplations*, *Fantasque & merveilleux* et *Cœurs, chaos & quotidien*. 29 ont été publiés sur Wattpad de 2021 à 2024 ; 7 ont été retrouvés dans les archives (quatre escapades de 1995, deux poèmes de 1996 et 1999, une prose onirique de 2020), avec provenance, dates d'origine et couvertures composées à partir des illustrations de l'auteur. Textes 100 % écrits par l'auteur, sans assistance d'IA.
- **Tome IV, *Carnets, réflexions & partages*** : quatre textes non fictifs retrouvés dans les archives, datés de 2003 à 2024, avec réécriture légère, date d'origine et note de source.
- **Sciences et technologie** : étude technique bibliographique de 2001-2002 sur les solutions techniques des jeux vidéos, avec une préface de 2026, quatre parties, les sommaires d'origine et les quatre PDF d'archive.
- **Nightprowler, carnets de Samarande** : six chapitres publiés, introduction hommage, sommaire à six entrées et illustrations de chapitre dans le style de la couverture.
- **Illustrations d'origine** : chaque texte des recueils retrouve sa couverture Wattpad, affichée en tête de chapitre et en miniature dans le sommaire.
- **Quinte ou Les Harmoniques de l'Âme** : nouvelle en sept parties, version remaniée par l'auteur, avec une écriture 100 % humaine.
- **Zéro Backend** : Tout tourne dans votre navigateur. Vos données (livres, progression, signets) restent chez vous dans IndexedDB.
- **Sécurité des imports** : les EPUB, dossiers HML et JSON importés passent par DOMPurify avant stockage et avant rendu.
- **Import Flexible** : Importez vos propres textes (EPUB, TXT, MD, JSON) ou dossiers HML complets, lus confortablement dans le Reader.
- **Ambiance Visuelle** : Animations d'ambiance subtiles adaptées à chaque thème (grain de papier, ondes sépia, lueurs blanches, poussières stellaires).
- **Temps de Lecture Intelligent** : Calcul dynamique du temps restant et indicateur contextuel.
- **Interface Adaptative** : Navigation fluide avec indicateurs de progression intégrés.

---

## 🚀 Architecture & Technos

- **Framework** : React 18, JSX précompilé vers `js/dist/` par `scripts/build_jsx.js`. Babel reste un outil de build, jamais chargé par le navigateur.
- **Modularité** : Composants React isolés et autonomes au sein de `js/components/`.
- **Stockage** : `idb-keyval` (IndexedDB) pour la persistance locale totale de vos bibliothèques.
- **PWA & Offline** : Service Worker (`sw.js`) qui précache l'app shell, les 105 contenus de livres (11 introductions et 94 chapitres) et les 11 couvertures. La bibliothèque, les fiches et la lecture restent accessibles hors ligne dès la première visite terminée.
- **Design** : CSS3 Vanilla modulaire.

---

## 📚 En Savoir Plus (Documentation Technique)

Pour comprendre en profondeur le fonctionnement de l'application, consultez nos guides dédiés :
1. 📁 **[Structure du Projet](structure.md)** : Cartographie des dossiers et fichiers.
2. 🛠️ **[Fonctionnalités Détaillées](features.md)** : Descriptif des outils de la liseuse.
3. 🧠 **[Conception Technique](readme-dev.md)** : Explications sur React, la précompilation JSX, le Service Worker et IndexedDB.
4. 🚀 **[Guide de Test et Déploiement](test_build_deploy.md)** : Guide Windows local + déploiement réel dans `Cours_Memos/Docker/books_reader` (dépôt `Hylst/cours_info`, Coolify `hylst-cours`) et script `scripts/sync-to-platform.ps1`.
5. 📝 **[Journal des versions](CHANGELOG.md)** : Historique détaillé et notes de release.
6. 🤖 **[Mémoire projet et consignes agents](antigravity.md)** : Stack réelle, règles critiques et état de production.

---

## ⌨️ Raccourcis Clavier

- `Espace` / `PageDown` : Faire défiler vers le bas d'environ 80%.
- `Flèche Droite` / `Gauche` : Chapitre suivant / précédent.
- `Home` / `End` : Haut / Bas de page.
- `Esc` : Fermer les menus, modals et barres d'outils.

---

## 📜 Licence & Crédits

Créé par **Geoffroy Streit (Hylst)** - Mail : geoffroy.streit@gmail.com  
Développé par **Antigravity**.  
Tous les contenus musicaux et littéraires natifs sont la propriété exclusive de Geoffroy Streit (Hylst).
