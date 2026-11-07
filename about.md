# À Propos de La Bibliothèque de Hylst

**La Bibliothèque de Hylst** réunit les livres, proses, poésies et récits de Geoffroy Streit (Hylst). Ce n'est pas d'abord un lecteur universel : c'est un sanctuaire numérique intimiste, dédié à la lecture et à l'immersion sonore.

L'application a été conçue pour offrir un cadre noble et apaisant aux œuvres de l'auteur, tout en permettant aux lecteurs d'importer leurs propres contenus dans un environnement respectueux de leur vie privée.

- Nom long : **La Bibliothèque de Hylst**
- Nom court : **Biblio Hylst**
- Signature : **Livres, proses, poésies et récits de Geoffroy Streit**
- URL : `https://hylst.fr/books_reader/`, alias `https://hylst.fr/bibliotheque/`

---

## 🌟 Expérience de lecture premium
- **Typographie Noble** : Design soigné utilisant des polices classiques (*Cormorant Garamond*, *Libre Baskerville*).
- **Thèmes Adaptatifs** : Modes Sépia, Clair et Sombre personnalisables avec des animations d'ambiance et des nuages de particules spécifiques. Le mode **Sombre** est celui proposé par défaut au premier lancement ; le choix de chacun est ensuite mémorisé et réappliqué avant le premier rendu.
- **Accompagnement Musical** : Un lecteur audio premium intégré avec accès à plus de **280 compositions originales** de Hylst (tags, moods, recherche par ambiance).
- **Ouverture et Liberté** : Importez vos propres livres (EPUB, TXT, Markdown, JSON, dossiers HML complexes) pour en profiter dans cet écrin de lecture.
- **Illustrations d'origine** : les textes publiés sur Wattpad affichent leur couverture d'origine en tête de chapitre et en miniature dans le sommaire.
- **Quinte ou Les Harmoniques de l'Âme** : nouvelle en sept parties, dans la version remaniée par l'auteur.
- **Souveraineté des Données** : Pas de cloud imposé, pas de pistage. Vos livres et votre progression restent stockés physiquement dans votre navigateur au sein d'IndexedDB.
- **Intelligence de Lecture** : Calcul dynamique du temps restant par chapitre et indicateurs de progression contextuels.

---

## 🚀 Technologie (Stack v1.8.17)
L'application utilise une stack moderne "Pure Frontend" optimisée pour la modularité et les performances :
- **React 18 & JSX précompilé** : Interface réactive découpée en composants ES6 autonomes, compilés au build vers `js/dist/`. Aucun transpileur n'est chargé par le navigateur.
- **IndexedDB (`idb-keyval`)** : Persistance robuste sans serveur pour les textes, signets et progressions de lecture.
- **Service Workers (PWA)** : Précache de l'app shell, des contenus de livres et des couvertures, puis Network-First avec repli cache. La bibliothèque et la lecture fonctionnent hors ligne.
- **Sécurité** : CSP stricte en balise meta et en en-tête Nginx, limitée à `/books_reader/`, avec `frame-ancestors 'self'`.
- **CSS3 Vanilla modulaire** : Design soigné reposant sur des variables et des tokens (grain de papier animés, z-index stables et animations fluides).

---

## 🎨 L'Auteur & Créateur
**Geoffroy Streit** (Hylst) est au cœur de ce projet. Écrivain occasionnel, dessinateur demoscene, passionné d'informatique et compositeur alsacien, il a imaginé cet outil pour offrir à ses lecteurs un cadre à la hauteur de ses récits. La musique intégrée à l'application fait partie intégrante de son univers artistique, conçue pour accompagner et décupler le rythme des émotions nées des mots.

---
*La Bibliothèque de Hylst · Livres, proses, poésies et récits de Geoffroy Streit.*
