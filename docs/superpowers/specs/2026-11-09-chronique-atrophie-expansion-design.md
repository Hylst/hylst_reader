# Design Spec : Expansion et Refonte Pessimiste de *Chronique d'une atrophie programmée*

## 1. Intention et Justification

*Chronique d'une atrophie programmée* est une dystopie d'anticipation et d'hérésie biologique écrite par Geoffroy Streit (Hylst). Dans sa version initiale (48 micro-chapitres de ~450 mots, ~21 750 mots au total), le texte fonctionne comme un synopsis romancé d'une remarquable puissance thématique (le pollen d'ambroisie contre la Trame, le coup de maître du Frisson Divin au chapitre 47). 

Néanmoins, l'audit critique pessimiste a révélé cinq vulnérabilités majeures :
1. **La physiologie magique** : Une rééducation motrice en quinze jours après dix ans de stase liquide est médicalement impossible.
2. **Le paradoxe bureaucratique** : L'absence de justification à l'emploi d'humains pour euphémiser la mort à l'ère de l'intelligence artificielle.
3. **Le coût civil invisible de l'attentat** : L'injection de quarante livres de pollen hautement allergisant dans soixante mille organismes décharnés et confinés sans aucun filtre ne peut pas produire qu'un simple réveil festif : elle provoque une hécatombe par œdème de Quincke et asphyxie aiguë.
4. **L'abandon de Tristan** : La voix éthique du récit quitte la scène au chapitre 40 sans résolution ni contrepoint.
5. **L'uniformité du rythme** : La cadence mécanique de ~450 mots par chapitre empêche l'installation des silences, de l'ennui claustrophobique et des set pieces d'envergure.

Cette refonte vise à porter l'ouvrage à une dimension romanesque adulte, viscérale et tragique (~45 000 à 60 000 mots), en brisant l'isométrie des chapitres et en assumant l'ambiguïté morale de chaque camp.

---

## 2. Principes Fondateurs du Canon Révisé

### A. Physiologie : Les Fers de Marche et la Dégradation Réelle
- Léonce bénéficiait dans son clapier du protocole de *Tonicité Dégressive* : des impulsions galvaniques involontaires toutes les six heures prévenaient la nécrose gangréneuse. Ses muscles ne sont pas absents, mais atrocement fibrosés, rétractés et privés de proprioception.
- Le talon d'Achille est raccourci (équinisme spastique). Pour lui permettre de se mouvoir dans les catacombes, Le Cliquet lui forge des **attelles articulées en fer blanc et cuir de rebut** (« les fers de marche »), fixées aux tibias par des colliers boulonnés.
- Chaque déplacement de Léonce s'accompagne d'un cliquetis métallique lourd, de broiements articulaires et d'une instabilité vestibulaire constante (vertiges, nausées).

### B. Le S.Y.N.D.I.C. et l'Écœurement Sémantique
- Le S.Y.N.D.I.C. (*Système National de Distribution et d'Interfaçage Confortable*) a tenté, lors des réformes de 2058, d'automatiser à 100 % la rédaction des euphémismes mortuaires.
- *L'Écœurement Sémantique* : le système limbique des dormeurs en stase détecte l'absence d'affect biologique dans la syntaxe synthétique, déclenchant des crises convulsives fatales (rejets vagaux en série).
- Pour être digestible par le subconscient des branchés, le mensonge d'État doit être rédigé par un être humain qui ressent **de la honte et de la culpabilité**. La signature neurale de cette mauvaise conscience organique agit comme l'adjuvant nécessaire au sommeil des foules. Léonce est payé pour sa honte.

### C. La Logistique du Frisson Divin : La Rupture d'Antihistaminiques
- L'Intendance ne recourt pas au Frisson Divin par pure perversité théâtrale : les usines de pharmacochimie lourde sont inondées depuis vingt ans. Les stocks de corticoïdes et d'antihistaminiques sont épuisés.
- Face à un taux de déconnexion d'urgence de 68 %, la seule ressource neurochimique disponible à débit illimité est la pompe à dopamine des noyaux accumbens. L'algorithme dérive l'arc réflexe du prurit et de la douleur vers les récepteurs du plaisir absolu.

### D. Le Destin Tragique de Tristan
- Tristan ne disparaît plus. Refusant le massacre au pollen, il remonte seul vers les clapiers de Belleville pour déclencher manuellement les clapets de secours et sauver son amie d'enfance ou des vieillards.
- Arrivé en surface sans masque, il est pris dans le vortex d'ambroisie. Face à l'asphyxie et à la mort imminente, il est brisé par son propre instinct de survie et s'enfiche lui-même un terminal mural dans l'oreille.
- Léonce le découvre dans la ronde des danseurs extatiques, le visage scarifié, riant et saignant sous le Frisson Divin.

---

## 3. Architecture des Niveaux de Longueur

Pour enrayer l'effet métronome, les chapitres adoptent désormais quatre gabarits distincts :
1. **Chapitres-Piliers (3 000 à 4 500 mots)** : Les quatre charnières émotionnelles et immersives (Chapitre 1, Chapitre 14, Chapitre 32, Chapitres 46-47 combinés).
2. **Chapitres de Tension et de Terrain (1 200 à 2 000 mots)** : L'exploration des galeries, l'entraînement, les dilemmes et les pannes mécaniques.
3. **Scènes d'Impact (600 à 1 000 mots)** : Coupures nettes, sabotages, alarmes, fuites dans le noir.
4. **Interludes documentaires (400 à 800 mots)** : Archives d'État, tables d'équivalences, rapports de voirie, dossiers de police synaptique.

---

## 4. Contraintes Techniques Plateforme
- Respect absolu de `python scripts/check_dashes.py --root .` (zéro tiret cadratin ou demi-cadratin dans les fichiers servis).
- Zéro dépendance externe ou CDN au runtime.
- Précache Service Worker à jour (`sw.js`).
- Validation par `powershell -ExecutionPolicy Bypass -File scripts/verify-release.ps1`.
