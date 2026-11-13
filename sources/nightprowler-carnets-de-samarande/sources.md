# Sources : Nightprowler, carnets de Samarande

Document de travail, exclu du miroir public. Il trace ce que l'édition 2026 doit à ses sources et ce qu'elle ajoute.

## 1. Source principale

| Champ | Valeur |
|---|---|
| Fichier | `Aides de jeu.htm` |
| Emplacement | `D:\0HYLST\0 HYLST ART 2024\ecrits\Jeu de rôle\Aides de jeu.htm` |
| Taille | 55 048 octets |
| Encodage | ISO-8859-1 / cp1252 |
| Sauvegarde | 2011-03-31 |
| URL d'origine | `http://hylst.voila.net/hnpaj.htm` |
| Texte extrait | 42 356 caractères |

La page contient :

- des questions-réponses de la mailing list Nightprowler sur l'expérience par niveaux, le réalisme, les scénarios, le vol et la lassitude du jeu ;
- des remarques sur la monnaie et les boutiques : pièces de bronze, échelonnement des prix, boulanger réveillé à minuit ;
- un personnage type, Albert Degreffion, avec ses caractéristiques et ses compétences ;
- l'atlas de Bejofa de Letorve : 38 quartiers, 5 sections, deux enceintes, 10 portes, le quartier franc 36, les juridictions prévôtales, le relief et les portes nommées ;
- des liens vers trois pages séparées : `fichpers.htm` (feuille de personnage), `combat.htm` (règles de combat de Mathieu Mazzoni) et `aidcreapersos.htm` (description de personnage de Hirrinkaël).

## 2. Pages liées

| Page | Auteur | Usage dans les carnets | Présence locale |
|---|---|---|---|
| `fichpers.htm` | Auteur de la page | Feuille de personnage simplifiée, citée dans les annexes | Absente du dossier local |
| `combat.htm` | Mathieu Mazzoni | Système de combat repris au chapitre VI | Absente du dossier local |
| `aidcreapersos.htm` | Hirrinkaël | Source probable du chapitre V, non vérifiée mot pour mot | Absente du dossier local |

## 3. Correspondances avec les carnets

| Chapitre | Nature de la reprise | Preuve |
|---|---|---|
| II. L'esprit du jeu | Réponses de la mailing list sur l'expérience et le réalisme | Citation explicite : « Ces réponses sont restées dans les archives de la page Aides de jeu, et j'en reprends ici l'essentiel, remis en ordre. » Blocs identiques de 29, 24, 22 et 18 mots. |
| III. Vies et prix | Pièces de bronze, échelonnement des prix, boulanger à minuit | Blocs identiques de 18 et 14 mots, dont « on voit mal un boulanger être réveillé pour une miche de pain de seigle à minuit ». |
| VII. Figures et prétirés | Albert Degreffion et son bloc de caractéristiques | Blocs identiques de 27, 25 et 18 mots. Le nom complet et les valeurs sont recopiés. |
| XIII. Annexes | Bandeaux Noirs, Bejofa, Sahar, chronologie 2300 et 2476 | Source déclarée en fin de chapitre : « Annexes composées en 2026 à partir de la feuille de personnage fichpers.htm, des aides de jeu hnpaj.htm, du chapitre I et des scénarios VIII à XII. » |
| VI. Le combat | Système de Mathieu Mazzoni | La page donne le lien vers `combat.htm`, mais le texte de combat n'est pas dans la page. |
| V. Décrire un personnage | Liste de descripteurs physiques | Source probable : `aidcreapersos.htm`, liée par la page. Non vérifiable localement. |

## 4. Ce qui n'est pas reproduit

- L'atlas de Bejofa de Letorve n'est pas recopié. Il est résumé dans le glossaire et la chronologie.
- Les questions-réponses de forum sur les scénarios, le vol et la lassitude ne sont pas reprises telles quelles.
- La feuille de personnage, le combat et la description de personnage restent des pages liées, pas des chapitres des carnets.
- Les images, tableaux et plans de l'atlas ne sont pas repris.

## 5. Écarts constatés

### 5.1. « Cité franche »

Le glossaire dit : « Ancienne rive insoumise de Samarande devenue cité franche en 2476, ceinte de deux murailles et de dix portes. » Source déclarée : « Aides de jeu et chapitre X ».

Or :

- la page ne contient pas l'expression « cité franche » ;
- elle dit que Bejofa est devenue « une Cité à part entière » et que son « apparition » remonte à 2476 ;
- le chapitre X n'emploie pas non plus l'expression.

La mention est donc un ajout de l'édition 2026, pas une citation de la page ni du chapitre X.

### 5.2. L'échelle de Bejofa

Le chapitre X dit : « Bejofa est le quartier pauvre de l'autre côté du bief. »

L'atlas décrit Bejofa comme une ville entière, divisée en 5 sections, avec des quartiers riches (sections I et II) et des quartiers pauvres (sections IV et V). Le scénario se déroule au quartier 30, que l'atlas classe dans la section IV : « Ses quartiers sont tous pauvres, exceptés les quartiers 28 et 29 qui sont misérables, et le quartier 25 qui est rural. »

Le décor du scénario est donc juste. La phrase généralise à tort un quartier à toute la ville.

### 5.3. La date de 2476

La chronologie dit : « 2476 : Bejofa obtient le statut de cité franche autonome ; construction de l'enceinte du Gouverneur. » Source déclarée : « Charte historique attestée dans les carnets. »

Or :

- l'atlas dit que l'enceinte du Gouverneur est la plus ancienne, qu'elle date de la même époque que l'enceinte du Prince à Samarande, et que seul son nom a changé en 2476 ;
- aucun autre chapitre ne mentionne 2476 : la date n'apparaît que dans le glossaire et la chronologie du chapitre XIII.

La source déclarée ne peut donc pas être vérifiée dans les carnets publiés. La date vient de la page, pas d'une charte interne.

## 6. Méthode

- Extraction du texte de `Aides de jeu.htm` en cp1252, puis normalisation des espaces.
- Extraction des treize chapitres des carnets.
- Normalisation des deux corpus (minuscules, accents retirés, ponctuation remplacée) pour comparer les mots.
- Recherche de blocs identiques avec `difflib.SequenceMatcher`, seuil de 8 mots.
- Vérification des termes et des dates par recherche contextuelle.

Analyse du 2026-11-13.
