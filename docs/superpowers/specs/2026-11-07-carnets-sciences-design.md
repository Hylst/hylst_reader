# Carnets, réflexions & partages et Sciences et technologie : fiche de conception

Date : 7 novembre 2026
Statut : validé par l'auteur, prêt pour le plan d'implémentation
Portée : deux ouvrages numériques de La Bibliothèque de Hylst, à partir de textes retrouvés dans les archives personnelles.

## 1. Intention

La bibliothèque contient déjà trois recueils de proses et poésies, un roman, un essai et un livre de jeu de rôle. Les archives personnelles ont livré deux ensembles qui ne trouvent pas leur place dans ces catégories :

- quatre textes de réflexion écrits entre 2003 et 2024, personnels, pratiques ou adressés à un lecteur ;
- une étude technique bibliographique de 2001-2002 sur les technologies des jeux vidéos, avec ses schémas, ses références et ses images d'époque.

L'objectif est de leur donner une place claire, sans les fondre dans les recueils de fiction et sans réécrire ce qui fait leur valeur : la voix de l'auteur pour les premiers, le document original pour la seconde.

## 2. Ce qui est décidé

- Un quatrième tome dans la série des recueils, assumé comme non fictif : **Carnets, réflexions & partages**.
- Un livre séparé, qui sert de rubrique **Sciences et technologie** : **Analyse des solutions techniques mises en œuvre dans les jeux vidéos**, avec une préface de 2026 et quatre PDF complets.
- Les textes de réflexion sont réécrits légèrement, datés en tête et accompagnés d'une note de source.
- L'étude technique n'est pas réécrite. Chaque partie reçoit un résumé de 2026, son sommaire d'origine et un PDF exporté depuis le document Word.
- Aucun fichier source n'est supprimé.
- Aucun tiret cadratin ou demi-cadratin dans les contenus servis.
- Aucune nouvelle dépendance, aucun CDN, aucun script inline.

## 3. Contraintes

- Les textes servis sont en HTML dans `public/books/<id>/`, avec une introduction `intro.html`.
- Le catalogue `public/books.json` reste la source de vérité des livres et des chapitres.
- Les fiches statiques `livres/<id>/index.html` sont générées par `scripts/build_book_pages.py`.
- Le Service Worker précache les introductions, les chapitres et les couvertures déclarées dans `books.json`. Les PDF ne sont pas précachés.
- Les polices sont locales ou servies par la plateforme. Aucune requête vers Google Fonts au runtime.
- Le PDF est produit avec Word, seul outil disponible qui conserve la mise en page et les images des `.docx`.
- Le style de l'auteur est conservé : première personne, adresse au lecteur, parenthèses, jeux de mots, digressions. La réécriture se limite à la syntaxe, aux répétitions, aux coquilles, à la ponctuation et aux scories de blog.
- Les dates d'origine sont affichées. Les ajouts de 2026 sont signalés.

## 4. Approches examinées

### 4.1 Où placer les textes de réflexion

1. **Les ajouter au Tome III.** Refusé : le Tome III est un recueil de fiction intime, les textes de réflexion en changeraient la nature et la promesse.
2. **Créer une rubrique séparée sans continuité avec les recueils.** Refusé : l'auteur a validé un quatrième tome, la continuité de série est plus lisible dans la bibliothèque.
3. **Créer le Tome IV, avec un sous-titre qui assume le carnet.** Retenu. La série garde son unité, le volume annonce clairement qu'il n'est pas un recueil de fiction.

### 4.2 Comment publier l'étude technique

1. **Convertir les 141 000 mots en HTML.** Refusé : travail disproportionné, perte des schémas et des légendes, risque de dénaturer un document académique de 2001.
2. **Publier uniquement les PDF, sans chapitre de synthèse.** Refusé : le lecteur arrive sans contexte, et la rubrique n'existe pas dans la liseuse.
3. **Format hybride : une préface, quatre chapitres de synthèse avec sommaire d'origine, et un PDF par partie.** Retenu. Le texte original reste intact, la lecture est guidée, la liseuse reste le point d'entrée.

### 4.3 Comment produire les PDF

1. **LibreOffice ou pandoc.** Non disponibles sur la machine.
2. **Reconstruction HTML puis impression PDF.** Perte des images et de la pagination d'origine.
3. **Export Word COM `ExportAsFixedFormat`.** Retenu, testé sur la partie A : 21 pages, 913 Ko, images conservées.

### 4.4 Comment produire les couvertures

1. **Image générée avec le texte inclus.** Risque de texte déformé, impossible à corriger proprement.
2. **Fond généré par le modèle local, typographie composée avec PIL.** Retenu. Le fond porte l'ambiance, le texte reste net et lisible, la composition est reproductible par script.

## 5. Tome IV : Carnets, réflexions & partages

### 5.1 Identité

- Identifiant : `recueils-proses-poesies-t4-carnets-reflexions-partages`
- Titre : `Carnets, réflexions & partages`
- Sous-titre : `Recueils de proses et poésies fantasques · Tome IV`
- Auteur : `Hylst (Geoffroy Streit)`
- Année d'édition : 2026
- Badge : `Textes retrouvés`
- `authorship` : `human`
- `aiAssisted` : `false`
- Source : archives personnelles, textes de 2003 à 2024.

Le sous-titre garde le nom de la série. L'introduction explique que ce tome est le carnet, le versant non fictif de la série.

### 5.2 Design

Le tome doit ressembler à un carnet relié, pas à un recueil de fantasy.

- Polices : Cormorant Garamond pour les titres, Libre Baskerville pour le corps, comme les tomes I à III.
- Fond : papier crème chaud `#f3ecdf`.
- Texte : encre brune `#2a241d`.
- Accent : cuivre `#b4682f`.
- Accent sombre : `#7a4a2b`.
- Surface : `#e8ddc9`.
- Bordure : `rgba(122, 74, 43, 0.18)`.
- Taille de corps : `1.04rem`, interligne `1.85`, largeur `700px`.

### 5.3 Introduction

L'introduction dit :

- ce que sont ces quatre textes, retrouvés dans les archives ;
- pourquoi ils ne sont pas dans les recueils de fiction ;
- la période couverte, 2003 à 2024 ;
- le principe de réécriture légère et les dates conservées ;
- le fil qui relie les textes : se tenir debout, regarder la société, offrir, transmettre.

Elle se termine par la mention de provenance : textes de Geoffroy Streit, sans assistance d'intelligence artificielle, mise en page technique.

### 5.4 Chapitres

Ordre chronologique.

| Fichier | Titre | Date affichée | Nature |
|---|---|---|---|
| `01-hygiene-de-vie.html` | I. Hygiène de vie | 23 novembre 2003 | Texte personnel sur la fatigue et la reconstruction |
| `02-imaginez-vous.html` | II. Imaginez-vous | 19 juin 2007 | Parabole sur une entreprise en crise, transposée à la France |
| `03-idees-cadeaux.html` | III. Idées cadeaux | 5 septembre 2008 | Article pratique sur les cadeaux faits main |
| `04-marre-d-apprendre.html` | IV. Marre d'apprendre | vers 2024 | Plaidoyer pour l'apprentissage, adressé à un jeune lecteur |

Chaque chapitre contient :

- le titre ;
- une ligne de date : `Texte écrit le 23 novembre 2003`, `Texte écrit vers 2024` ;
- le corps réécrit ;
- une note de source en fin de chapitre.

### 5.5 Règles de réécriture

- Garder la première personne, l'adresse directe, les parenthèses, les questions rhétoriques et les jeux de mots.
- Corriger la syntaxe, les accords, les répétitions, la ponctuation, les majuscules décoratives.
- Retirer les émoticônes, les `lol`, les abréviations de blog (`qques`, `vmt`, `tjrs`, `g`, `bpc`), les formules de fin d'article et les appels à commenter.
- Ne pas ajouter d'idées, de citations ou d'exemples nouveaux.
- Ne pas gommer les hésitations qui font partie du ton, sauf quand elles rendent le texte incompréhensible.
- Conserver les titres de sections quand ils structurent le texte, en les passant en `<h2>`.
- Remplacer tout tiret cadratin ou demi-cadratin par une virgule, un point-virgule, deux-points ou une parenthèse.

Décisions par texte :

- **Hygiène de vie** : réécriture moyenne à lourde. Le texte est un brouillon assumé, avec des digressions et des abréviations. On garde l'aveu de fatigue, l'image du corps qui pèse, le chocolat noir aux écorces d'orange, l'idée du cerveau muscle, les conseils sur la respiration, le glucose, le magnésium et le phosphore. On retire les tics de blog et les passages trop hachés, sans transformer le texte en article de santé.
- **Imaginez-vous** : réécriture moyenne. On garde les deux candidats, le bilan, les trois questions finales, et la transposition à la France. On corrige les accords, les subordonnées et les `=)`. On garde le ton de fable politique.
- **Idées cadeaux** : réécriture légère. On garde le catalogue d'idées, les recettes (pâte à sel, papier mâché, papier vieilli, parfum), le jeu de mots sur Louis et l'ouïe, et l'adresse au lecteur. On retire la formule de contact finale.
- **Marre d'apprendre** : réécriture légère. On garde la structure en quatre parties, l'adresse au jeune lecteur, l'image des lunettes magiques, l'escalier de la connaissance, le `tilt`, le super-cerveau. On retire les majuscules décoratives et les effets de mise en forme. On garde les exemples (Google, IA, cabane, fusée, jeu vidéo).

### 5.6 Notes de source

Modèle pour les chapitres :

> Version originale retrouvée dans les archives de l'auteur, texte du 23 novembre 2003. Réécriture légère en 2026 : orthographe, ponctuation, répétitions et scories de blog. Les images, les parenthèses et les jeux de mots ont été conservés.

Pour `Marre d'apprendre`, préciser que la date exacte n'a pas été retrouvée et que le texte est daté vers 2024.

## 6. Sciences et technologie

### 6.1 Identité

- Identifiant : `sciences-et-technologie-jeux-videos`
- Titre : `Sciences et technologie`
- Sous-titre : `Analyse des solutions techniques mises en œuvre dans les jeux vidéos · Étude 2001-2002`
- Auteur : `Hylst (Geoffroy Streit)`
- Année d'édition : 2026
- Badge : `Archives`
- `authorship` : `human`
- `aiAssisted` : `false`
- Mention : étude technique bibliographique, NFIO promotion 7, 5e année, 2001-2002.

Le titre court sert de rubrique. Le sous-titre porte le titre complet de l'étude et sa date.

### 6.2 Design

Le livre doit évoquer un dossier technique, pas un recueil littéraire.

- Polices : Outfit pour les titres, Merriweather pour le corps, toutes deux déjà auto-hébergées.
- Fond : papier froid `#edf1f3`.
- Texte : encre bleu-noir `#1a2830`.
- Accent : ambre technique `#b5732b`.
- Accent sombre : `#1f4b63`.
- Surface : `#dfe8ec`.
- Bordure : `rgba(31, 75, 99, 0.18)`.
- Taille de corps : `1.02rem`, interligne `1.8`, largeur `720px`.

L'ambre sert aux liens, aux filets et aux téléchargements. Le bleu sert aux titres et aux blocs de sommaire.

### 6.3 Introduction

L'introduction dit :

- ce qu'est cette étude, quand et pourquoi elle a été écrite ;
- ce qu'elle couvre : histoire, interfaces, afficheurs, capteurs, numérisation ;
- comment elle est publiée : préface, quatre parties, PDF d'origine ;
- ce que le lecteur ne doit pas y chercher : une mise à jour technique de 2026 ;
- la mention de provenance et l'absence d'assistance IA.

Elle liste les quatre parties avec leur lien PDF, en chemin absolu `/books_reader/public/books/sciences-et-technologie-jeux-videos/pdf/...`, pour fonctionner aussi bien dans la liseuse que sur la fiche statique.

### 6.4 Chapitres

| Fichier | Titre | Contenu |
|---|---|---|
| `00-preface.html` | Préface 2026 | Contexte, ce que l'étude cherchait, ce qu'elle a raté, ce qu'elle annonçait déjà, mode de lecture |
| `01-partie-a.html` | Partie A. Introduction, histoire et interfaces manuelles | Parties A, B et C de l'étude |
| `02-partie-b.html` | Partie B. Interfaces sensori-motrices | Partie D |
| `03-partie-c.html` | Partie C. Interfaces de visualisation | Partie E |
| `04-partie-d.html` | Partie D. Capteurs, autres systèmes et conclusion | Parties F à J |

Chaque partie contient :

- le titre ;
- une ligne de contexte : `Étude technique bibliographique · 2001-2002` ;
- un résumé de 2026 en plusieurs paragraphes ;
- le sommaire d'origine, avec les numéros de page quand ils sont connus ;
- un bloc de téléchargement du PDF, avec le nombre de pages et le poids ;
- une note de source.

Le bloc de téléchargement utilise une classe dédiée `chapter-download`, ajoutée à `css/reader.css`. Le lien porte l'attribut `download`.

### 6.5 Préface 2026

La préface est un texte de 2026, signé, qui raconte :

- le cadre : NFIO promotion 7, 5e année, année 2001-2002 ;
- la commande : une étude technique bibliographique, avec un ancrage optronique ;
- la méthode : lectures de constructeurs, presse spécialisée, fiches techniques, pas de mesures en laboratoire ;
- ce que l'étude a bien vu : l'interface comme cœur du jeu, l'immersion, la latence, la résolution, le champ de vision, le coût, l'encombrement, la calibration ;
- ce qu'elle ne pouvait pas voir : le smartphone comme manette universelle, le suivi à l'intérieur vers l'extérieur, les centrales inertielles MEMS, la vision par ordinateur, le sans-fil, la domination du LCD puis de l'OLED, la disparition du CRT et du plasma, le GPU, la distribution en ligne, l'IA générative ;
- ce qui reste utile : la grille d'analyse, la distinction entre interfaces sensorielles et sensori-motrices, l'attention au corps et à la calibration ;
- le statut du document : travail d'étudiant, daté, non mis à jour, à lire comme une archive ;
- la restauration numérique : export PDF depuis Word, mise en page et images conservées.

La préface ne prétend pas que l'étude avait tout prévu. Elle dit aussi ce qu'elle a manqué.

### 6.6 PDF

Les quatre PDF sont exportés depuis les quatre `.docx` de `04_ARCHIVES_TECHNIQUES/sources-word/` avec Word COM, en mode écran, avec les images d'origine.

| PDF | Source | Contenu |
|---|---|---|
| `partie-a-introduction-histoire-interfaces-manuelles.pdf` | `etjv-a.docx` | A, B, C |
| `partie-b-interfaces-sensori-motrices.pdf` | `etjv-b.docx` | D |
| `partie-c-interfaces-de-visualisation.pdf` | `etjv-c.docx` | E |
| `partie-d-capteurs-autres-systemes.pdf` | `etjv-d.docx` | F à J |

Le script `scripts/export_etjv_pdfs.ps1` ouvre chaque document, lit le nombre de pages, exporte le PDF et écrit un manifeste JSON. Les PDF sont stockés dans `public/books/sciences-et-technologie-jeux-videos/pdf/`.

Critères : quatre fichiers présents, pages supérieures à zéro, poids supérieur à 100 Ko, première page lisible, images conservées. Si un PDF dépasse 20 Mo, le signaler et vérifier le rendu avant de l'accepter.

### 6.7 Notes de source

Modèle pour les parties :

> Texte original de 2001-2002, non réécrit. Le résumé et le sommaire de cette page ont été écrits en 2026. Le PDF reproduit la mise en page du document Word d'origine.

Pour la préface :

> Préface écrite en novembre 2026 pour cette édition numérique. L'étude reproduite reste celle de 2001-2002.

## 7. Fichiers créés ou modifiés

Créés :

- `public/books/recueils-proses-poesies-t4-carnets-reflexions-partages/intro.html`
- `public/books/recueils-proses-poesies-t4-carnets-reflexions-partages/01-hygiene-de-vie.html`
- `public/books/recueils-proses-poesies-t4-carnets-reflexions-partages/02-imaginez-vous.html`
- `public/books/recueils-proses-poesies-t4-carnets-reflexions-partages/03-idees-cadeaux.html`
- `public/books/recueils-proses-poesies-t4-carnets-reflexions-partages/04-marre-d-apprendre.html`
- `public/books/sciences-et-technologie-jeux-videos/intro.html`
- `public/books/sciences-et-technologie-jeux-videos/00-preface.html`
- `public/books/sciences-et-technologie-jeux-videos/01-partie-a.html`
- `public/books/sciences-et-technologie-jeux-videos/02-partie-b.html`
- `public/books/sciences-et-technologie-jeux-videos/03-partie-c.html`
- `public/books/sciences-et-technologie-jeux-videos/04-partie-d.html`
- `public/books/sciences-et-technologie-jeux-videos/pdf/*.pdf`
- `public/covers/recueils-proses-poesies-t4-carnets-reflexions-partages.webp`
- `public/covers/sciences-et-technologie-jeux-videos.webp`
- `scripts/export_etjv_pdfs.ps1`
- `scripts/make_book_covers.py`

Modifiés :

- `public/books.json` : deux entrées, neuf chapitres.
- `css/reader.css` : styles `chapter-download` et `chapter-original-toc`.
- `sw.js` : cache `hylst-reader-v67`.
- `CHANGELOG.md`, `todo.md`, `antigravity.md`, `continue.md`.

Générés :

- `livres/recueils-proses-poesies-t4-carnets-reflexions-partages/index.html`
- `livres/sciences-et-technologie-jeux-videos/index.html`
- `public/covers/og/*.jpg` par `build_book_pages.py`.
- `css/book-page.css` par `build_book_pages.py`.

## 8. Vérifications

- `python scripts/check_dashes.py --root .` : zéro tiret cadratin ou demi-cadratin.
- `python -c "import json; json.load(open('public/books.json', encoding='utf-8'))"` : catalogue valide.
- `python scripts/build_book_pages.py` : dix fiches générées, dont les deux nouvelles.
- `node scripts/build_jsx.js` puis `node scripts/build_jsx.js --check` : sortie à jour.
- Les quatre PDF existent, pages et poids cohérents, première page rendue en PNG pour contrôle visuel.
- Les chapitres contiennent la date d'origine et la note de source.
- Les chapitres du Tome IV ne contiennent plus `lol`, `:o)`, `☺`, `qques`, `vmt`, `tjrs`, `g bcp`.
- Les liens PDF répondent en 200 sur `http://127.0.0.1:8765/books_reader/public/books/sciences-et-technologie-jeux-videos/pdf/...`.
- Les deux couvertures sont en WebP 600x900, poids inférieur à 250 Ko, texte lisible.
- La page livre et la fiche statique affichent les nouveaux sommaire.
- `powershell -ExecutionPolicy Bypass -File scripts/sync-to-platform.ps1` : miroir synchronisé, sitemap complet.

## 9. Hors périmètre

- Les Escapades B2 à E, les deux poèmes et `Wizard's lair` : lot suivant.
- La mise à jour des intitulés et des dates des tomes I à III pour intégrer les textes de 1995 à 2008 : à faire quand les Escapades seront publiées.
- La réécriture ou la mise à jour technique de l'étude de 2001-2002.
- Une table des matières imbriquée dans la liseuse.
- Le déploiement Coolify et la vérification de production, qui restent des étapes séparées.

## 10. Ce qui reste au builder

- Rédiger les quatre textes du Tome IV dans le ton de l'auteur, en suivant les décisions ci-dessus.
- Rédiger l'introduction, la préface 2026 et les quatre résumés de parties.
- Reconstituer les sommaires d'origine à partir du document Word, sans inventer de section.
- Composer les deux couvertures et vérifier la lisibilité du texte.
- Exporter les PDF et contrôler leur rendu.
- Mettre à jour le catalogue, le Service Worker et la documentation.
