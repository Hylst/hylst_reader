# Enrichissement du Tome IV par les réflexions de jeunesse (1994-1998) : fiche de conception

Date : 8 novembre 2026  
Statut : validé par l'auteur, prêt pour le plan d'implémentation  
Portée : ajout de trois nouveaux chapitres de jeunesse en tête de *Carnets, réflexions & partages · Tome IV* dans La Bibliothèque de Hylst.

---

## 1. Intention et genèse

Dans ses archives personnelles des années 1994-1998 (contemporaines de sa formation en STL Physique de laboratoire puis de ses premières créations informatiques et rôlistes), Geoffroy Streit (Hylst) a rédigé une série de réflexions philosophiques, artistiques, sociétales et ludiques sur son site web personnel d'alors.

Ces textes constituent le socle fondateur de sa pensée non fictive :
- Sa réflexion sur l'artifice, la création libre et son coup de gueule éthique au cœur de la *demoscene* informatique des années 90 (Oric, C64, Atari ST, Amiga ; dénonciation du plagiat de code, des rips de samples et des faux graphismes scannés face au dessin manuel au pixel).
- Sa philosophie de l'« édenisme » comme partage des plaisirs, sa hiérarchie de l'effort et son besoin vital d'équilibre entre la rigueur des sciences de laboratoire (optique, électronique, informatique) et l'évasion par l'imaginaire (jeu de rôle, musique, dessin médiéval), scellée par la métaphore de la vie comme un oiseau au creux de la main.
- Ses conseils sur l'éveil sensoriel de l'enfant (le cerveau comparé à un disque dur sain à la naissance) et son plaidoyer foisonnant pour les loisirs actifs et associatifs (jeux de plateau, jeux de rôle, création) contre la passivité du « métro-boulot-dodo ».

L'objectif est d'intégrer ce corpus en tête du Tome IV (*Carnets, réflexions & partages*), qui couvrira désormais trente ans de réflexions (1994-2024) et passera de 4 à **7 textes**.

---

## 2. Décisions de découpage et de contenu

### 2.1 Les trois nouveaux chapitres (1994-1998)

1. **Chapitre 01 : *De l'art et de la demoscene informatique*** (vers 1996)
   - *Thématiques* : Définition de l'art (artifice versus Nature, gratuité matérielle, noblesse de la difficulté technique, variété des supports). La culture demoscene (création for fun, démos versus jeux interactifs). Tribune sans fard sur l'éthique des créateurs : avertissement aux programmeurs contre les routines volées, dénonciation virulente des graphismes copiés ou scannés face au travail original d'auteur, et regret du pillage de samples chez les musiciens.
2. **Chapitre 02 : *De l'édenisme et de la quête d'équilibre*** (vers 1996-1998)
   - *Thématiques* : La finalité de l'existence humaine (éprouver du plaisir et le partager). Les trois degrés de plaisirs (simples/quotidiens, besoins naturels avec désapprobation de l'orgueil/paresse/avarice, plaisirs nobles de la passion et de l'effort créateur). La valeur fondamentale de la complicité humaine. La recherche d'équilibre personnel : compenser les études scientifiques lourdes par le jeu de rôle, la musique et le dessin médiéval. Maximes de vie (Carpe Diem, ne pas remettre au lendemain, la parabole de l'oiseau au creux de la main).
3. **Chapitre 03 : *Éloge du temps libre et de l'éveil*** (vers 1998)
   - *Thématiques* : L'éveil sensoriel du jeune enfant (le cerveau comme disque dur défragmenté à la naissance, assimilation sans conflits psychologiques initiaux, rôle des parents comme guides responsables). Le panorama foisonnant et engagé des loisirs : jeux de société versus jeux de plateaux (Warhammer 40000, Space Hulk, Dune, Carcassonne, son propre jeu *Les Royaumes d'Yttria*), jeux de cartes (Magic, Vampire, Elixir), jeux de rôle, sports, pratiques artistiques, militantisme pour la richesse de vie contre la passivité télévisuelle du « métro-boulot-dodo ».

### 2.2 Re-numérotation ordonnée du Tome IV

Les 4 chapitres actuels sont décalés de 01-04 vers 04-07 :
- `04-hygiene-de-vie.html` (23 novembre 2003)
- `05-imaginez-vous.html` (19 juin 2007)
- `06-idees-cadeaux.html` (5 septembre 2008)
- `07-marre-d-apprendre.html` (vers 2024)

### 2.3 Règles de réécriture éditoriale (Charte du Tome IV)

- **Voix de l'auteur préservée** : conservation scrupuleuse de la première personne, de l'adresse directe au lecteur, des apartés, des parenthèses, des métaphores et des maximes.
- **Toilettage de forme Web 1.0** : développement des abréviations de prise de notes (`qques` → quelques, `C` → c'est, `+` → plus, `-` → moins, `svt` → souvent, `bpc` → beaucoup, `G` → j'ai), correction des coquilles de frappe et des répétitions involontaires, suppression des résidus de navigation de site personnel (`Retour home page`).
- **Typographie** : zéro tiret cadratin ou demi-cadratin. Formatage soigné en paragraphes `<p class="chapter-paragraph">` et sections `<h2>`.

---

## 3. Objectifs, non-objectifs et anti-objectifs

### Objectifs
- Offrir une lecture fluide, stimulante et vivante des premières intuitions philosophiques et éthiques de l'auteur.
- Rendre hommage à la culture demoscene des années 90 et à la passion du jeu de société/rôle avec un témoignage de première main.
- Assurer une continuité chronologique harmonieuse de 1994 à 2024 dans le volume.

### Non-objectifs
- Ne pas gommer le caractère passionné ou les partis pris tranchés de l'auteur sur les copieurs ou les paresseux.
- Ne pas chercher à actualiser les références ludiques ou informatiques (Oric, C64, Atari ST, Warhammer 40k, disques durs) : ce sont des témoins d'époque précieux.

### Anti-objectifs
- Proscrire tout ton encyclopédique neutre ou « IA ».
- Proscrire tout tiret long dans les fichiers servis.

---

## 4. Contraintes techniques

- Fichiers HTML créés dans `public/books/recueils-proses-poesies-t4-carnets-reflexions-partages/` :
  - `01-de-l-art-et-de-la-demoscene.html`
  - `02-de-l-edenisme-et-de-la-quete-d-equilibre.html`
  - `03-eloge-du-temps-libre-et-de-l-eveil.html`
- Renommage par `git mv` des 4 fichiers existants vers `04-`, `05-`, `06-`, `07-`.
- Mise à jour de `intro.html` (7 textes, période 1994-2024).
- Mise à jour de `public/books.json` avec les 7 chapitres et leurs métadonnées.
- Regénération de la fiche statique du livre (`scripts/build_book_pages.py`).
- Validation stricte : `check_dashes.py --root .`, `build_jsx.js --check`, `test-sw-policy.js`.
- Incrémentation du Service Worker (`sw.js`).
