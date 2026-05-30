# Fonctionnalités — Hylst Books & Reader

L'application **Hylst Books & Reader** propose une suite complète de fonctionnalités pour offrir une expérience de lecture immersive de premier plan.

---

## 📖 1. Le Moteur de Lecture Littéraire (ReaderView)
Conçu comme un livre physique de grande qualité, la liseuse adapte et peaufine le rendu du texte :
- **Typographies de caractère** : Utilisation conjointe de **Cormorant Garamond** (pour des titres distingués) et de **Libre Baskerville** (pour un confort de lecture optimal).
- **Thèmes graphiques immersifs** : 
  - **Mode Sépia** : Une lumière ambrée traditionnelle rappelant le papier bouffant.
  - **Mode Clair** : Lumineux et sobre, avec des contrastes équilibrés.
  - **Mode Sombre** : Un gris très doux à l'œil pour limiter la lumière bleue en pleine nuit.
- **Dropcaps automatiques** : Lettrine agrandie au premier paragraphe de chaque chapitre.
- **Réglages du texte** : Choix de la largeur de colonne (Étroit, Moyen, Large), alignement (Gauche ou Justifié), et taille du texte (de 70% à 170% de la taille de base).
- **Mode Focus Absolu** : Un double-clic ou double-tap masque instantanément toutes les interfaces pour ne laisser que le texte pur et l'ambiance.

---

## 🎵 2. La Musicothèque Immersive Intégrée
Conçue par Geoffroy Streit, la bibliothèque sonore contient plus de **280 titres** :
- **Atmosphères dédiées** : Chaque morceau est étiqueté par genre, BPM, année et mood (Mélancolique, Spatial, Épique...).
- **Lecteur Audio Premium** : Un mini-player flottant persiste tout au long de la lecture et permet de mettre en pause, de passer au titre suivant, ou d'activer le mode boucle.
- **Recherche par Tag** : Une barre de recherche filtre instantanément la tracklist selon vos envies de lecture.

---

## 🌀 3. Les Effets d'Ambiance Animés (Ambience)
Pour donner vie à l'écran, un calque dynamique se superpose subtilement sous le texte :
- **Grain de papier tactile** : Effet de grain imprimé s'agitant doucement en arrière-plan.
- **Poussières flottantes** : Des particules s'élèvent et oscillent lentement sur l'écran (ondes lumineuses en sépia, lueurs claires en blanc, scintillements stellaires en mode sombre).
- **Intensité débrayable** : Possibilité de passer en mode statique (sans animation) individuellement par thème selon les envies.

---

## ⚡ 4. Souveraineté & Importation Universelle (Offline First)
L'application fonctionne à 100% sans serveur de base de données en s'appuyant sur les capacités de votre navigateur :
- **IndexedDB (`idb-keyval`)** : Stocke physiquement vos livres importés et garde en mémoire votre progression de lecture exacte et vos signets.
- **Importation multiple** :
  - **Fichier unique** : Glissez-déposez un fichier `.EPUB`, `.TXT`, `.MD` ou `.JSON` pour l'ouvrir instantanément.
  - **Dossier HML local** : Grâce à l'API File System Access, glissez un dossier complet d'ouvrage structuré pour en recréer le sommaire et le graphisme personnalisé.

---

## 📱 5. Technologie PWA Installable
Compatible avec tous vos appareils (ordinateurs de bureau sous Windows/Mac/Linux, tablettes, smartphones Android et iOS) :
- **Service Worker intelligent** : Met en cache non seulement les styles et scripts locaux, mais également les dépendances CDN externes (React, Babel, idb-keyval), rendant l'application parfaitement autonome hors-ligne après le premier chargement.
- **Installation native** : S'intègre comme une application de bureau ou de téléphone grâce au fichier `manifest.json`.
