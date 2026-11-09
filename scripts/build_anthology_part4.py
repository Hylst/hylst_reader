# -*- coding: utf-8 -*-
from pathlib import Path

out_dir = Path("public/books/approche-de-la-neurodiversite")
out_dir.mkdir(parents=True, exist_ok=True)

# 1. 12-l-environnement-et-le-corps-poser-les-fondations.html
ch12_html = """<div class="chapter-content">
  <h1 class="chapter-main-title"><strong>12. L'environnement et le corps : poser les fondations</strong></h1>
  <p class="chapter-byline">PARTIE IV : LA BOÎTE À BÉQUILLES, DISCIPLINE &amp; SURVIE · 13 stratégies de terrain (Juin 2022)</p>
  <figure class="chapter-figure">
    <img src="public/books/approche-de-la-neurodiversite/images/partie-3-couverture.webp" alt="La Boîte à Outils" loading="lazy" />
  </figure>
  <p class="chapter-paragraph">Si comme moi vous devez vivre au quotidien avec des troubles dys, psychomoteurs ou plus généralement neurocognitifs, vous avez forcément cherché des moyens d'en atténuer les désagréments, d'en contourner la difficulté ou d'en amoindrir le handicap. Non ?</p>
  <p class="chapter-paragraph">Ces troubles sont hélas invisibles au premier regard. Ils sont aussi, trop souvent, mal compris lorsqu'ils se manifestent, engendrant jugements de valeur erronés et mise à l'écart. Et ils s'avèrent permanents, récurrents et circonstanciellement exacerbés par la fatigue ou l'émotion.</p>
  <p class="chapter-paragraph">Alors, quand malgré des efforts de volonté considérables les blocages persistent, il faut cesser de s'acharner contre le mur et apprendre à poser des béquilles techniques solides. La première famille de béquilles concerne l'environnement direct et la posture corporelle.</p>
  <p class="chapter-paragraph"><strong>Axe 1 : Un espace de travail strictement calibré.</strong><br>Ne travaillez jamais au milieu du désordre. Pour un cerveau dont les filtres attentionnels sont poreux, chaque objet qui traîne sur la table est une invitation au décrochage. Aménagez une pièce à l'écart, confortable juste ce qu'il faut (pas trop molle pour ne pas inciter à la somnolence, mais suffisamment ergonomique pour préserver les articulations). Veillez au maintien de la nuque, à l'inclinaison du plan de travail, à l'appui stable des avant-bras et à un éclairage franc, indirect, sans scintillement.</p>
  <p class="chapter-paragraph"><strong>Axe 2 : Élimination impitoyable des parasites sensoriels.</strong><br>Coupez systématiquement les sources de distraction : notifications de smartphones, onglets de réseaux sociaux ouverts en arrière-plan, téléviseur allumé sans son, radio qui babille. Chaque sonnerie ou vibration agit comme un coup de canif dans le fil fragile de votre concentration, et il vous faudra ensuite cinq à dix minutes pour retrouver le niveau d'immersion initial.</p>
  <p class="chapter-paragraph"><strong>Axe 3 : Le rituel d'ancrage et de respiration préalable.</strong><br>Avant d'attaquer une tâche complexe, ne vous jetez pas tête baissée sur le clavier. Asseyez-vous confortablement. Fermez les yeux pendant trente à soixante secondes. Prenez deux ou trois grandes inspirations lentes par le nez en gonflant le ventre, puis soufflez longuement par la bouche. Faites mentalement le tour de votre corps, relâchez les mâchoires et les épaules. Ce sas de décompression permet d'apaiser l'anxiété anticipatoire de l'échec.</p>
  <p class="chapter-paragraph"><strong>Axe 4 : L'acceptation du temps long et de la répétition.</strong><br>Même si certaines actions présentent pour vous une difficulté bien supérieure à la moyenne : les répéter sans honte, c'est se les réapproprier pas à pas. Si cela prend deux fois plus de temps qu'à un collègue, et bien soit ! La lenteur n'est pas un crime : c'est le rythme naturel d'une mécanique qui compense par la conscience ce que d'autres exécutent par pur automatisme réflexe.</p>
</div>
"""
(out_dir / "12-l-environnement-et-le-corps-poser-les-fondations.html").write_text(ch12_html, encoding="utf-8")
print("Written 12-l-environnement-et-le-corps-poser-les-fondations.html")

# 2. 13-le-delestage-mental-externaliser-la-memoire.html
ch13_html = """<div class="chapter-content">
  <h1 class="chapter-main-title"><strong>13. Le délestage mental : externaliser la mémoire</strong></h1>
  <p class="chapter-byline">PARTIE IV : LA BOÎTE À BÉQUILLES, DISCIPLINE &amp; SURVIE · 13 stratégies de terrain (Juin 2022)</p>
  <figure class="chapter-figure">
    <img src="public/books/approche-de-la-neurodiversite/images/neuro-schema-3-bequilles.svg" alt="Architecture des 13 béquilles cognitives pour adultes neuroatypiques" loading="lazy" />
  </figure>
  <p class="chapter-paragraph">La mémoire de travail d'un profil neuroatypique est semblable à la mémoire vive d'un vieil ordinateur : si vous y laissez tourner dix programmes en même temps, le processeur surchauffe et la machine plante sur un écran bleu.</p>
  <p class="chapter-paragraph">Le secret d'une vie productive et sereine réside donc dans un principe fondamental : externaliser tout ce qui peut l'être sur des supports physiques fiables.</p>
  <p class="chapter-paragraph"><strong>Axe 5 : La segmentation en micro-étapes.</strong><br>Ne regardez jamais un projet sous la forme d'un bloc monolithique (« rédiger le rapport financier annuel » ou « réorganiser tout l'atelier »). C'est le meilleur moyen de provoquer une tétanie d'inhibition. Découpez la tâche en sous-actions minuscules, presque ridicules par leur simplicité : « ouvrir le classeur », « classer les factures de janvier », « imprimer le récapitulatif ». En validant chaque étape l'une après l'autre, vous offrez à votre cerveau des micro-doses de satisfaction qui entretiennent la motivation sans saturer l'espace de calcul.</p>
  <p class="chapter-paragraph"><strong>Axe 6 : Les listes de délestage et le pense-bête immédiat.</strong><br>Ayez toujours à portée de main un calepin de poche ou une application de notes minimaliste. Dès qu'une tâche, une commission ou une idée surgit à l'esprit, écrivez-la immédiatement ! Ne vous dites jamais : « Je m'en souviendrai tout à l'heure. » C'est faux : cinq minutes plus tard, l'information aura sombré dans les oubliettes. En la consignant sur le papier, vous libérez instantanément vos neurones du stress de la rétention.</p>
  <p class="chapter-paragraph"><strong>Axe 7 : L'automatisation numérique et les alarmes programmées.</strong><br>Faites des outils technologiques vos serviteurs les plus dociles. Programmez des rappels sonores sur votre téléphone pour les échéances critiques : prise de médicaments, départ pour un rendez-vous, arrêt d'une cuisson au four. Si un courriel ou un message vous préoccupe et risque d'empoisonner votre soirée, rédigez-le et programmez son envoi automatique pour le lendemain matin à neuf heures. Vous dormirez sur vos deux oreilles sans porter la charge du message différé.</p>
  <p class="chapter-paragraph"><strong>Axe 8 : Jeter sur papier pour assainir l'esprit.</strong><br>Lorsque des pensées récurrentes, des angoisses ou des bribes de projets tournent en boucle dans votre tête comme des chevaux de bois emballés, asseyez-vous avec une feuille vierge et écrivez tout ce qui passe, en vrac, sans souci de syntaxe ni d'orthographe. Videz la poubelle mentale. Une fois les mots matérialisés sur la feuille, le cerveau constate que la matière est sécurisée et accepte enfin de baisser la garde.</p>
</div>
"""
(out_dir / "13-le-delestage-mental-externaliser-la-memoire.html").write_text(ch13_html, encoding="utf-8")
print("Written 13-le-delestage-mental-externaliser-la-memoire.html")

# 3. 14-conditionnement-hygiene-de-vie-et-esprit-embrume.html
ch14_html = """<div class="chapter-content">
  <h1 class="chapter-main-title"><strong>14. Conditionnement, hygiène de vie et gestion de l'esprit embrumé</strong></h1>
  <p class="chapter-byline">PARTIE IV : LA BOÎTE À BÉQUILLES, DISCIPLINE &amp; SURVIE · 13 stratégies de terrain (Juin 2022)</p>
  <p class="chapter-paragraph">Puisque les circuits séquentiels et verbaux de l'hémisphère gauche peinent souvent à traiter l'information abstraite brute, il faut systématiquement solliciter les circuits spatiaux, visuels et associatifs.</p>
  <p class="chapter-paragraph"><strong>Axe 9 : Structurer les pensées de manière graphique.</strong><br>Vous n'arrivez pas à appréhender une notion complexe ou à construire un raisonnement à plusieurs variables ? Dessinez-le ! Utilisez des cartes heuristiques (mind maps), des arborescences, des organigrammes fléchés, des fiches récapitulatives avec surligneurs de couleurs contrastées. Transformez les paragraphes indigestes en tableaux synthétiques à colonnes. Le cerveau dys, souvent très à l'aise avec la pensée globale et panoramique, saisit en un coup d'œil sur un schéma ce qu'il mettrait quarante minutes à décrypter dans un texte linéaire.</p>
  <p class="chapter-paragraph"><strong>Axe 10 : La règle impérative de la relecture différée.</strong><br>Ne relisez jamais un travail important (lettre de motivation, contrat de bail, courriel sensible, bilan comptable) immédiatement après l'avoir rédigé ! Vos yeux sont fatigués, votre cerveau est encore saturé par l'intention du texte et il lira ce qu'il croit avoir écrit plutôt que ce qui est réellement couché sur la page. Fermez le document, allez faire un tour ou passez une bonne nuit de sommeil. Le lendemain matin, l'esprit reposé et le recul rétabli, les coquilles, les contresens et les oublis vous sauteront aux yeux avec une évidence lumineuse.</p>
  <p class="chapter-paragraph"><strong>Axe 11 : Le carburant biologique du système nerveux.</strong><br>Le cerveau d'un profil neuroatypique consomme jusqu'à deux fois plus de glucose et d'oxygène qu'un cerveau ordinaire pour accomplir une tâche similaire, en raison de la mobilisation constante de circuits compensatoires non automatisés. Vous ne pouvez pas exiger d'une telle mécanique qu'elle fonctionne avec un réservoir vide.</p>
  <p class="chapter-paragraph">Cela impose une hygiène biologique stricte :<br>Un sommeil inviolable : la nuit n'est pas une variable d'ajustement pour travailler plus tard. C'est pendant le sommeil profond que le cerveau nettoie ses toxines métaboliques et consolide les apprentissages de la journée.<br>Une hydratation continue : buvez de l'eau fraîche régulièrement tout au long de la journée ; la déshydratation la plus minime se traduit immédiatement par une baisse de vigilance et des maux de tête diffus.<br>Une aération fréquente : ouvrez grand la fenêtre toutes les deux heures pour renouveler l'air de la pièce et chasser le dioxyde de carbone accumulé.</p>
  <p class="chapter-paragraph"><strong>Axe 12 : Détecter l'alerte de l'esprit embrumé.</strong><br>Il arrive des heures où, malgré toute votre bonne volonté, la machinerie cérébrale se grippe complètement. Vous lisez la même phrase six fois de suite sans en comprendre le premier mot ; vous êtes incapable d'additionner sept et cinq sans recompter sur vos doigts ; votre vision se trouble légèrement, vos tempes s'alourdissent et une sensation d'hébétude cotonneuse envahit votre esprit.<br>C'est l'alerte rouge : le point de saturation cognitive absolue. Insister dans cet état est pire qu'inutile : c'est destructeur.</p>
  <p class="chapter-paragraph"><strong>Axe 13 : Savoir dire stop et pratiquer la bienveillance envers soi.</strong><br>Quand le brouillard tombe sur vos neurones, appliquez le protocole d'arrêt d'urgence : sauvegardez votre travail en cours sur deux supports fiables, posez les crayons, fermez l'écran. Si vous êtes au milieu d'une réunion professionnelle ou d'une discussion familiale tendue, n'ayez pas honte de poser vos limites avec calme et dignité : « Je commence à saturer, mon esprit est fatigué. Je préfère faire une pause de quinze minutes / reprendre ce point demain à tête reposée pour ne pas dire de bêtise. »</p>
  <p class="chapter-paragraph">Et par-dessus tout : cultivez la bienveillance envers vos propres limites. Vous aurez encore des oublis, des maladresses motrices, des jours sans énergie et des moments d'inattention déroutants. C'est ainsi : cette architecture est la vôtre. Le courage ne consiste pas à prétendre qu'on ne trébuche jamais : il consiste à se fabriquer de bonnes béquilles pour continuer à marcher droit, d'un pas sûr et sans courber l'échine.</p>
</div>
"""
(out_dir / "14-conditionnement-hygiene-de-vie-et-esprit-embrume.html").write_text(ch14_html, encoding="utf-8")
print("Written 14-conditionnement-hygiene-de-vie-et-esprit-embrume.html")

# 4. 15-epilogue-vivre-avec-la-friction.html
ch15_html = """<div class="chapter-content">
  <h1 class="chapter-main-title"><strong>15. Épilogue : Vivre avec la friction</strong></h1>
  <p class="chapter-byline">CLÔTURE · Geoffroy Streit (2022)</p>
  <figure class="chapter-figure">
    <img src="public/books/approche-de-la-neurodiversite/images/epilogue-couverture.webp" alt="La Silhouette et le Phare" loading="lazy" />
  </figure>
  <p class="chapter-paragraph">Au terme de cette traversée de plus de vingt années d'expérience et d'écrits, le tableau que nous avons dressé peut sembler rude et sans fard.</p>
  <p class="chapter-paragraph">Il l'est délibérément, parce que le maquillage optimiste du développement personnel ne console personne dans la solitude d'une copie raturée ou d'une relance administrative angoissante. Dire la vérité des troubles dys et du TDA/H, nommer l'épuisement, la honte accumulée et la friction quotidienne, c'est le seul moyen d'arracher ces réalités à l'opprobre du jugement moral.</p>
  <p class="chapter-paragraph">Non, la neurodiversité n'est pas un conte de fées. Elle n'est pas un cadeau du ciel déguisé en énigme, et ceux qui prétendent le contraire n'ont sans doute jamais passé une nuit entière à pleurer sur un formulaire d'embauche ou à se faire insulter au fond d'une cour d'école.</p>
  <p class="chapter-paragraph">Mais refuser l'illusion ne signifie aucunement céder au désespoir.</p>
  <p class="chapter-paragraph">Ceux qui grandissent et vivent avec ces machineries atypiques développent souvent, par la force des choses, des qualités de résilience, une empathie profonde pour les fragilités d'autrui et une inventivité remarquable pour contourner les obstacles là où d'autres se contentent d'emprunter des boulevards balisés.</p>
  <p class="chapter-paragraph">Ils apprennent la patience, l'humilité du recommencement et la valeur inestimable des solidarités discrètes.</p>
  <p class="chapter-paragraph">Accepter son fonctionnement, ce n'est pas hisser le drapeau blanc de la défaite : c'est troquer l'armure trop lourde de la normalité feinte contre un trousseau de clés d'artisan bien ajustées. C'est apprendre à aménager son atelier, à respecter ses rythmes biologiques, à s'entourer de regards qui ne jugent pas, et à savourer chaque victoire avec la fierté légitime de celui qui a dû tout conquérir de haute lutte.</p>
  <p class="chapter-paragraph">La friction ne disparaîtra jamais complètement. Mais lorsqu'on cesse de se battre contre sa propre nature pour bâtir des passerelles d'intelligence et de fraternité, on découvre qu'il est possible de traverser l'existence les yeux grands ouverts, le cœur solide, et la tête haute.</p>
</div>
"""
(out_dir / "15-epilogue-vivre-avec-la-friction.html").write_text(ch15_html, encoding="utf-8")
print("Written 15-epilogue-vivre-avec-la-friction.html")

# 5. Clean up old temporary files chapitre-01.html to chapitre-11.html and epilogue.html
old_files = [f"chapitre-{i:02d}.html" for i in range(1, 12)] + ["epilogue.html"]
for of in old_files:
    p = out_dir / of
    if p.exists():
        p.unlink()
        print(f"Removed old {of}")

print("PART IV FILES COMPLETE AND OLD FILES CLEANED")