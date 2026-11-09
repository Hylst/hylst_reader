# Design Document : Édition intégrale d'*Approche de la Neurodiversité* (Recueil thématique en 3 parties)

## 1. Intention et Pourquoi

*Approche de la Neurodiversité* (sous-titré *Vision d'un non-professionnel*) est l'un des ouvrages les plus personnels et singuliers de Geoffroy Streit (Hylst). Contrairement aux discours lénifiants du développement personnel qui transforment les troubles neurodéveloppementaux en « super-pouvoirs » illusoires, l'auteur y défend une approche résolument lucide, pragmatique et ancrée dans le réel : celle d'un adulte « dys » qui a dû grandir, apprendre, travailler et survivre avec une machinerie cérébrale atypique tout en accompagnant bénévolement d'autres enfants et adolescents en détresse scolaire.

La version actuellement en ligne dans la liseuse (6 chapitres, ~3 500 mots) ne constituait qu'un condensé philosophique resserré. Les archives personnelles de l'auteur recèlent trois documents fondamentaux rédigés entre 2018 et 2022 (avec des racines pédagogiques remontant à près de vingt ans) :
1. `troubles dys.odt` (~2 400 mots) : La cartographie clinique et vécue des 5 familles de troubles dys (dyslexie, dysphasie, dyspraxie, TDA/H, mémoire de travail et dyscalculie) et de l'incompréhension sociale.
2. `Enfants en difficulté scolaire.doc` (~1 400 mots) : Un guide pédagogique de terrain pour parents, professeurs particuliers et tuteurs d'enfants en souffrance scolaire.
3. `Idées pour lutter contre les troubles ‘dys’ et autres troubles neurocognitifs.pdf` (~3 330 mots, juin 2022) : La boîte à outils pragmatique de l'adulte détaillant 13 béquilles cognitives concrètes.

L'objectif de cette édition intégrale est de **consolider, enrichir et unifier ces textes en un recueil thématique majeur en trois grandes parties (11 chapitres + prologue et épilogue)**, accompagné de **schémas vectoriels SVG précis** pour les mécanismes cognitifs et d'**illustrations d'art éditorial générées localement sur GPU avec Krea-2-Turbo** pour les têtes de parties.

---

## 2. Objectifs, Non-Objectifs et Anti-Objectifs

### Objectifs
- **Recueil structuré en 3 parties (11 chapitres)** :
  - **Partie I : Anatomie des décalages (Le vécu de l'intérieur)** : 4 chapitres décrivant de manière vécue et sans jargon les 5 familles dys, la surconsommation d'énergie et l'incompréhension sociale.
  - **Partie II : L'Enfance et l'École (Guide pour parents et tuteurs)** : 3 chapitres d'accompagnement bienveillant, de diagnostic des blocages et de pédagogie du déblocage.
  - **Partie III : La Boîte à Béquilles (13 stratégies concrètes pour adultes)** : 4 chapitres de méthodes de terrain (ergonomie, délestage mental par l'écrit, gestion des pannes et de l'esprit embrumé).
  - **Épilogue** : *Vivre avec la friction*.
- **Voix authentique de l'auteur** : Préserver scrupuleusement le style de Geoffroy Streit : direct, sincère, lucide, sans prétention académique, profondément humain et bienveillant, refusant la condescendance.
- **Schémas vectoriels SVG haute précision** : Intégrer des infographies SVG claires, responsives, auto-hébergées et adaptées aux modes sombre/clair de la liseuse pour schématiser les concepts clés (boucles cognitives, segmentation des tâches, filtres attentionnels).
- **Illustrations éditoriales locales (Krea-2-Turbo)** : Générer localement sur GPU (sans API externe ni coût) des œuvres sobres et poétiques (style encre fine et lavis or/ardoise) pour les ouvertures de parties.
- **Conformité technique absolue** : Zéro tiret cadratin ou demi-cadratin (`check_dashes.py`), CSP `'self'`, précache Service Worker (`hylst-reader-v92`).

### Non-Objectifs
- Ne pas chercher à rédiger un traité médical ou psychiatrique (la valeur du texte réside dans son statut de « vision d'un non-professionnel » issu du terrain et du vécu intime).
- Ne pas prescrire de traitements médicaux ni de promesses de « guérison ».

### Anti-Objectifs
- **Zéro romantisation « super-pouvoir »** : Bannir tout discours démagogique prétendant que les troubles dys sont un don magique. C'est un handicap qui coûte de l'énergie chaque seconde.
- **Zéro jargon jargonnant** : Préférer les métaphores concrètes (l'engrenage qui coince, la mémoire qui fuit, la fatigue de l'adulte) aux néologismes médicaux prétentieux.

---

## 3. Structure détaillée du Recueil (11 Chapitres)

### Prologue
* **Le décalage invisible** : Présentation du recueil, genèse 2018-2022 (racines 2004), avertissement sur la lucidité et refus du prêt-à-penser.

### PARTIE I : ANATOMIE DES DÉCALAGES (Le vécu de l'intérieur)
* **Chapitre 1 : L'école, premier tribunal et blessure originelle**  
  Le décalage naissant hors du cocon familial. Le moment où la singularité devient une faute. L'enfant jugé paresseux ou nonchalant alors que ses circuits luttent contre la surcharge.
* **Chapitre 2 : Les cinq familles de troubles : langage, geste et calcul**  
  Description détaillée, incarnée et sans complaisance des différentes facettes :
  - Langage écrit : dyslexie et dysorthographie (la fatigue de lecture, la forme visuelle des mots qui se dérobe).
  - Langage oral : dysphasie (la parole entravée, la peur du mot qui ne sort pas).
  - Psychomoteur et espace : dyspraxie, TAC et TDC (le geste maladroit, le lacet rebelle, la feuille froissée, la géométrie impossible).
  - Activités numériques : dyscalculie (le chiffre qui se transforme, la terreur des tables et des durées).
  *Schéma SVG 1 : Cartographie interactive des 5 familles et de leurs interférences.*
* **Chapitre 3 : L'attention en miettes et la mémoire qui fuit**  
  Le TDA/H sans fard : la captation intempestive par les stimuli extérieurs, l'impulsivité relationnelle, la mémoire de travail qui sature en trois secondes, les consignes oubliées prises pour de la négligence.
* **Chapitre 4 : L'usure adulte et le malentendu permanent**  
  Démystification de la « disparition à l'âge adulte ». La persistance du coût énergétique, l'angoisse des formulaires administratifs, les entretiens d'embauche, la gestion des finances et la peur du ridicule.

### PARTIE II : L'ENFANCE ET L'ÉCOLE (Guide pour parents et tuteurs)
* **Chapitre 5 : Décrypter le malaise scolaire sans condamner**  
  La posture de l'adulte face aux mauvaises notes. Diagnostic des causes réelles : ambiance de classe agitée, humiliation par les pairs, complexes vestimentaires, fatigue accumulée. Pourquoi l'agressivité de l'enfant masque souvent un appel au secours.
* **Chapitre 6 : Dédramatiser, écouter et restaurer la confiance**  
  Sortir de la dictature du résultat immédiat. La séparation essentielle entre la valeur de l'enfant et ses notes. Écouter d'égal à égal, dédramatiser l'erreur, offrir un cadre sécurisant où l'effort est reconnu indépendamment du verdict scolaire.
* **Chapitre 7 : Pédagogie de terrain : la méthode du pas-à-pas**  
  Conseils concrets pour les cours particuliers et le travail à la maison : segmenter l'effort en petites étapes victorieuses, alterner temps calme et récréation, ancrer les notions abstraites dans des objets réels, apprendre avec humilité et patience.
  *Schéma SVG 2 : La spirale du découragement scolaire et les leviers de désamorçage.*

### PARTIE III : LA BOÎTE À BÉQUILLES (13 stratégies concrètes de terrain)
* **Chapitre 8 : L'environnement et le corps : poser les fondations**  
  - Axe 1 : L'espace de travail épuré (nuque, éclairage, posture, suppression des bruits et notifications).
  - Axe 2 : Les rituels de centrage et de respiration avant l'effort.
  - Axe 3 : L'acceptation du temps long (répéter sans honte pour apprivoiser le geste).
* **Chapitre 9 : Le délestage mental : externaliser la mémoire**  
  - Axe 4 : La segmentation des tâches en micro-étapes indolores.
  - Axe 5 : Les listes de délestage et le « pense-bête » immédiat pour vider le cerveau.
  - Axe 6 : Les rappels programmés et l'automatisation numérique au service de l'autonomie.
  - Axe 7 : Jeter sur le papier les idées parasites pour retrouver le calme.
  *Schéma SVG 3 : La boucle de délestage cognitif et d'externalisation de la mémoire.*
* **Chapitre 10 : Méthodologie intellectuelle et hygiène de vie**  
  - Axe 8 : Structurer les pensées (fiches visuelles, schémas, techniques d'ancrage).
  - Axe 9 : Vérification et relecture différée (ne jamais relire à chaud avec le cerveau fatigué).
  - Axe 10 : L'hygiène biologique : sommeil réparateur, hydratation, aération régulière.
* **Chapitre 11 : Savoir quand s'arrêter : la gestion de l'esprit embrumé**  
  - Axe 11 : Détecter le point de rupture et la saturation cognitive (« l'esprit dans le brouillard »).
  - Axe 12 : Savoir dire stop : oser demander une pause, reporter à tête reposée sans culpabiliser.
  - Axe 13 : La boussole de la bienveillance envers soi-même.

### Épilogue
* **Vivre avec la friction**  
  Le texte de clôture lucide : ni résignation ni faux espoirs. Construire des béquilles solides pour affronter la fatigue du réel et marcher debout.

---

## 4. Direction Artistique & Assets

### Schémas Vectoriels SVG (Précision & Clarté)
Trois schémas SVG interactifs et sémantiques, intégrés directement dans le flux des chapitres avec support natif des thèmes clair/sombre :
1. `neuro-schema-1-familles.svg` (Chapitre 2) : Cartographie des 5 familles de troubles, leurs zones cérébrales associées et leurs interactions quotidiennes.
2. `neuro-schema-2-pedagogie.svg` (Chapitre 7) : Boucle du découragement scolaire et leviers d'intervention bienveillante.
3. `neuro-schema-3-bequilles.svg` (Chapitre 9) : Schéma fonctionnel du délestage mental et des 13 béquilles cognitives.

### Illustrations d'en-tête (Générées localement via Krea-2-Turbo)
Quatre illustrations au format WebP optimisé (480x280 px, style art éditorial sobre à l'encre fine et lavis ardoise/or) :
1. `partie-1-couverture.webp` : *L'Archipel des Pensées* (métaphore des circuits asymétriques et des ponts suspendus).
2. `partie-2-couverture.webp` : *La Main sur l'Épaule* (silhouette bienveillante guidant un enfant vers un cahier sous une lumière douce).
3. `partie-3-couverture.webp` : *La Boîte à Outils* (engrenages de bois délicats, carnet ouvert et boussole de cuivre).
4. `epilogue-couverture.webp` : *La Silhouette et le Phare* (marcheur solitaire avançant avec assurance le long d'un sentier côtier dans la brume).

---

## 5. Spécifications Techniques

- **Chemin du livre** : `public/books/approche-de-la-neurodiversite/`
- **Fichiers** :
  - `intro.html` (carte de présentation de la liseuse)
  - `00-prologue.html` (chapitre de lecture d'ouverture)
  - `chapitre-01.html` à `chapitre-11.html`
  - `epilogue.html` (chapitre de clôture)
  - `images/` (les 4 illustrations WebP locales + les 3 schémas vectoriels SVG)
- **Catalogue (`public/books.json`)** :
  - `year`: `"2018-2022 (mis en ligne en 2026)"`
  - `writingPeriod`: `"2018-2022"`
  - `compilationYear`: 2026
  - `illustrationNote`: *"Textes de réflexion rédigés entre 2018 et 2022 (100 % de l'auteur, sans IA) · Schémas vectoriels et illustrations locales Krea 2026"*
  - Sommaire à 13 entrées (Prologue + 11 chapitres + Épilogue), garantissant une lecture linéaire complète.
- **Intégration des Schémas SVG** :
  - Intégrés sous balises sémantiques `<figure class="chapter-figure"><img src="...svg" alt="..." loading="lazy" /></figure>` avec palettes CSS adaptatives et accompagnés d'un tableau ou d'un descriptif accessible sous-jacent, conformément aux normes CSP `'self'` et à la pratique éprouvée de *Nightprowler*.
- **Démarche éditoriale** :
  - Consolidation littéraire fidèle à partir des 3 manuscrits d'archives de l'auteur (`troubles dys.odt`, `Enfants en difficulté scolaire.doc`, `Idées pour lutter contre les troubles...pdf`) : respect scrupuleux de son propos de terrain, de ses anecdotes, de sa méthode pédagogique et de ses 13 stratégies d'adulte, formulés dans son style direct, humain et lucide.
- **Service Worker** : incrémentation vers `hylst-reader-v92`.
- **Fiche statique** : regénération de `livres/approche-de-la-neurodiversite/index.html`.
- **Contrôles qualité** : `check_dashes.py` (0 tiret long), `build_jsx.js --check`, `test-sw-policy.js`.
