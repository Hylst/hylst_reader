# Fonctionnalités · La Bibliothèque de Hylst

L'application **La Bibliothèque de Hylst** propose une suite complète de fonctionnalités pour offrir une expérience de lecture immersive de premier plan.

---

## 📖 1. Le Moteur de Lecture Littéraire (ReaderView)
Conçu comme un livre physique de grande qualité, la liseuse adapte et peaufine le rendu du texte :
- **Typographies de caractère** : Utilisation conjointe de **Cormorant Garamond** (pour des titres distingués) et de **Libre Baskerville** (pour un confort de lecture optimal).
- **Thèmes graphiques immersifs** : 
  - **Mode Sépia** : Une lumière ambrée traditionnelle rappelant le papier bouffant.
  - **Mode Clair** : Lumineux et sobre, avec des contrastes équilibrés.
  - **Mode Sombre** : Un gris très doux à l'œil pour limiter la lumière bleue en pleine nuit. C'est le thème proposé par défaut au premier lancement, sans éclair clair au chargement.
- **Dropcaps automatiques** : Lettrine agrandie au premier paragraphe de chaque chapitre.
- **Mise en page théâtre** : didascalies bleues, répliques alignées à gauche et conservation des retours de ligne du manuscrit.
- **Navigation de fin de partie** : un bloc « Fin de la partie » avec la partie suivante est toujours visible sous le dernier paragraphe, même barre masquée. Une pastille `1 / 7 · Suivant` reste accessible en lecture immersive.
- **Accès direct** : `https://hylst.fr/books_reader` redirige en 301 vers `https://hylst.fr/books_reader/`, qui reste l'URL canonique.
- **L'Odyssée de l'énergie** : les 10 chapitres sont disponibles, avec relecture orthographique complète, données actualisées et mention de transparence sur l'assistance IA en dernière de couverture.
- **Recueils Wattpad** : 29 textes répartis en trois volumes, avec mise en page prose/poésie, dates de publication, lien vers la version originale et illustrations d'origine affichées en tête de chapitre et dans le sommaire. Création littéraire 100 % humaine, sans assistance d'IA.
- **Quinte ou Les Harmoniques de l'Âme** : nouvelle en sept parties, version remaniée par l'auteur, avec introduction et note de provenance.
- **Deux URL** : `/books_reader/` reste l'URL canonique, `/bibliotheque/` y redirige en 301 avec conservation de la query string.
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
  - **Fichier unique** : Sélectionnez un fichier `.EPUB`, `.TXT`, `.MD` ou `.JSON` pour l'ouvrir instantanément.
  - **Dossier HML local** : Grâce à l'API File System Access, sélectionnez un dossier complet d'ouvrage structuré pour en recréer le sommaire et le graphisme personnalisé.
  - **Assainissement** : chaque contenu importé passe par DOMPurify avant stockage et avant rendu (scripts, iframes, gestionnaires d'événements et URL `javascript:` neutralisés).

---

## 📱 5. Technologie PWA Installable
Compatible avec tous vos appareils (ordinateurs de bureau sous Windows/Mac/Linux, tablettes, smartphones Android et iOS) :
- **Service Worker intelligent** : Précache l'app shell, `public/books.json`, les 66 introductions et chapitres, les 7 couvertures actives et les 7 fiches statiques. La navigation hors ligne retombe proprement sur l'app shell ou la fiche déjà mise en cache.
- **Installation native** : S'intègre comme une application de bureau ou de téléphone grâce au fichier `manifest.json`.
