# Conception Technique — Hylst Books & Reader

Ce guide technique explique les choix d'architecture et de conception pour les développeurs souhaitant comprendre ou modifier l'application **Hylst Books & Reader**.

---

## 🏗️ 1. Architecture Globale : "Zero Build / Pure Frontend"

Contrairement à la majorité des applications React modernes qui nécessitent un processus de build complexe (`Vite`, `Webpack`, `Babel-CLI`, `Node.js`), ce projet est conçu pour être **directement lisible par un navigateur standard sans étape intermédiaire**.

### 🌟 Avantages de cette stack :
1. **Zéro configuration** : Aucun besoin d'installer de dépendances npm complexes ou de gérer des incompatibilités de versions locales.
2. **Maintenance infinie** : Les fichiers sources sont de simples fichiers statiques. Il n'y aura aucun problème d'outils de compilation obsolètes dans 5 ans.
3. **Lancement instantané** : Modifiez le code dans votre éditeur, rafraîchissez votre navigateur, le changement est immédiat !

---

## 📦 2. Chargement des Dépendances & Transpilation à la volée

Toutes les dépendances critiques sont chargées via des CDN (Content Delivery Network) hautement optimisés dans `index.html` :

```html
<!-- React & ReactDOM (Version Production de React 18) -->
<script src="https://unpkg.com/react@18/umd/react.production.min.js" crossorigin></script>
<script src="https://unpkg.com/react-dom@18/umd/react-dom.production.min.js" crossorigin></script>

<!-- Babel Standalone (Transpileur JSX à la volée dans le navigateur) -->
<script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>

<!-- idb-keyval (Gestion simplifiée d'IndexedDB pour la persistance) -->
<script src="https://cdn.jsdelivr.net/npm/idb-keyval@6/dist/umd.js"></script>
```

### 🧠 Comment le JSX est-il interprété ?
Grâce à la déclaration suivante dans `index.html` :
```html
<script type="text/babel" data-type="module" src="js/app.jsx"></script>
```
Babel Standalone intercepte le fichier `js/app.jsx` (et ses composants dépendants importés), détecte les blocs JSX, et les compile en JavaScript ES5 à la volée directement dans le navigateur du lecteur. 
De plus, `data-type="module"` indique à Babel de supporter et de transpirer les instructions `import` / `export` ES6, ce qui permet la modularisation du code.

---

## 📂 3. Modularisation React par Composants Réels

L'application est structurée de manière modulaire au sein de `js/components/`. 
Chaque fichier est un module ES6 qui exporte ses fonctions et composants :
- **`js/components/Icon.jsx`** : Fournit le set complet des icônes SVG.
- **`js/components/Ambience.jsx`** : Gère l'arrière-plan interactif et les particules.
- **`js/app.jsx`** : Sert de chef d'orchestre global, gérant la machine à états de l'application (vue active, livre en cours, progression) et la lecture audio persistante.

---

## 💾 4. Base de Données Locale IndexedDB (`db.js`)

Pour persister les données de progression sans serveur backend, nous utilisons `idb-keyval`, une abstraction ultra-légère au-dessus de l'API complexe IndexedDB du navigateur :
- **`getBooks()` / `saveBook(book)`** : Sauvegarde des livres importés au format HML, TXT, EPUB ou JSON.
- **`getProgress(bookId)` / `saveProgress(bookId, chapterIdx, ratio)`** : Sauvegarde permanente du dernier chapitre lu et du pourcentage de défilement pour un effet "continuer la lecture" transparent.
- **`getSignets(bookId)` / `saveSignet(bookId, bookmark)`** : Enregistrement de signets posés par le lecteur.

---

## 🌐 5. Cache PWA Offline complet (`sw.js`)

Le Service Worker implémente deux types de stratégies de cache distinctes :
1. **Network-First** pour les fichiers du dépôt local (HTML, CSS, images, JS locaux). Cela assure que si vous êtes connecté, vous obtenez toujours la version la plus à jour, avec une bascule immédiate sur le cache si le réseau tombe.
2. **Cache-First** pour les bibliothèques CDN et Google Fonts. Comme ces librairies externes ne changent jamais, elles sont stockées de façon permanente en cache au premier chargement, évitant ainsi des appels réseau inutiles et bloquants en mode hors-ligne.
