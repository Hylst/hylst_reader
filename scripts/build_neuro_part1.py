# -*- coding: utf-8 -*-
from pathlib import Path

out_dir = Path("public/books/approche-de-la-neurodiversite")
out_dir.mkdir(parents=True, exist_ok=True)

# 1. intro.html
intro_content = """<div class="book-intro-generated">
  <h2>Approche de la Neurodiversité</h2>
  <p class="chapter-byline">Recueil thématique · Vision d'un non-professionnel</p>
  <hr class="ornament">
  <p class="chapter-epigraph" style="font-style: italic; text-align: center; margin: 1.25rem 0; opacity: 0.85;">
    Ce n'est pas un manque de volonté. C'est une machinerie qui frotte à chaque seconde contre un monde qui ne pardonne pas la lenteur.
  </p>
  <h3>Le décalage invisible</h3>
  <p>Ce livre ne vient ni d'une chaire universitaire, ni d'un cabinet de neuropsychologie feutré. Il ne vous promettra aucun miracle, aucune recette magique pour transformer un handicap en « super-pouvoir », et encore moins les formules lénifiantes du développement personnel à la mode. La neurodiversité n'est pas une bénédiction romantique : au quotidien, pour celui qui la porte dans sa chair et dans son cerveau, c'est d'abord une friction permanente, une débauche d'énergie épuisante et une solitude difficile à partager.</p>
  <p>Cette édition intégrale réunit et consolide vingt années d'expérience et de réflexions de terrain : celle d'un adulte « dys » qui a dû grandir, apprendre, travailler et survivre avec des circuits cérébraux atypiques, tout en accompagnant d'autres enfants et adolescents confrontés au même mur. L'intelligence est normale, souvent vive, mais le relais se dérobe. La mémoire immédiate sature, le geste se brise, le mot exact refuse de sortir, le calcul élémentaire se brouille, et le regard des autres conclut trop vite à la paresse ou au désintérêt.</p>
  <p>L'approche défendue ici est résolument lucide et sans complaisance. Accepter le pessimisme du constat, ce n'est pas capituler : c'est refuser de se raconter des histoires pour bâtir de vraies béquilles, pragmatiques et tenaces, capables de résister à la fatigue du réel.</p>
  <p><strong>13 chapitres</strong> (en trois parties) · rédigé de 2018 à 2022 · mis en ligne en 2026</p>
  <p class="chapter-continuation" style="font-style: italic; text-align: center; margin-top: 1.5rem;">Hylst (Geoffroy Streit)</p>
  <p class="provenance-note">Recueil thématique consolidé à partir des textes de réflexion de l'auteur (« Troubles dys : clarifications, réflexions et pistes de solutions pour troubles cognitifs », « Enfants en difficulté scolaire » et « Idées pour lutter contre les troubles dys et autres troubles neurocognitifs »). Schémas vectoriels SVG de l'auteur et illustrations d'art éditorial générées localement sur GPU (Krea-2-Turbo).</p>
  <p class="chapter-tags" style="font-size: 0.78rem; opacity: 0.7; text-align: center; margin-top: 1.5rem;">
    #neurodiversite #troublesdys #dyspraxie #dyslexie #tdah #cognition #ecole #pedagogie #adulte #bequilles
  </p>
</div>
"""
(out_dir / "intro.html").write_text(intro_content, encoding="utf-8")
print("Written intro.html")

# 2. Chapters of Part I
part1_chapters = [
    (
        "00-prologue.html",
        "00",
        "Prologue : Le Décalage Invisible",
        "OUVERTURE",
        "",
        """Le sujet est vaste, redoutable, encombré de préjugés tenaces et de modes passagères. Je n'ai pas la prétention d'en faire le tour encyclopédique, n'étant ni médecin spécialiste, ni chercheur en neurosciences, et encore moins neuropsychologue diplômé d'État. Toutefois, ma propre expérience d'adulte « dys », mes lectures patientes, ainsi que le fait d'avoir accompagné bénévolement durant de nombreuses années des enfants et des adolescents aux prises avec des troubles spécifiques des apprentissages font que je connais le problème de l'intérieur, à hauteur d'homme et les mains dans la terre glaise du réel.

Avant d'entrer dans le vif de cette étude, une précision capitale s'impose : les troubles cognitifs dont il sera question ici sont les troubles dits « spécifiques des apprentissages ». Ils désignent des décalages d'acquisition qui ne sont liés ni à une déficience intellectuelle globale, ni à un handicap sensoriel périphérique (cécité, surdité), ni à une carence éducative fondamentale. L'intelligence de la personne est parfaitement normale, souvent vive, curieuse et créative. Mais un relais fonctionnel se dérobe dans les rouages cérébraux. Les signaux patinent, le pont synaptique ne répond pas avec la fluidité automatique dont bénéficient les personnes ordinaires.

On parle souvent de l'enfance, car c'est sur les bancs de l'école que la collision frontale avec la norme se produit avec la plus grande violence. C'est là que l'enfant construit son rapport aux autres, sa confiance en soi, ses repères dans l'espace et sa relation au langage. Quand ces fondations se fissurent sous les quolibets ou les verdicts hâtifs, les retards d'assimilation s'accumulent et la blessure psychologique s'enkyste pour des décennies.

Ce recueil est conçu comme un triptyque complet :
La première partie dissèque la machinerie intime des différentes familles de troubles dys et explore sans faux-fuyant le coût énergétique invisible qu'elles imposent chaque jour.
La deuxième partie est un guide d'accompagnement de terrain pour les parents, tuteurs et enseignants confrontés à la détresse scolaire d'un enfant : comment désamorcer l'angoisse, restaurer le dialogue et reconstruire l'envie d'apprendre par le pas-à-pas.
La troisième partie propose un arsenal pragmatique de treize béquilles concrètes pour l'adulte, afin d'organiser son espace, délester sa mémoire de travail et savoir dire stop lorsque survient le redoutable « esprit embrumé ».

Ce livre ne cherche pas à vous rassurer à bon compte. Il cherche à vous donner des prises solides pour avancer les yeux ouverts."""
    ),
    (
        "chapitre-01.html",
        "01",
        "I. L'école, premier tribunal et blessure originelle",
        "PARTIE I : ANATOMIE DES DÉCALAGES",
        "public/books/approche-de-la-neurodiversite/images/partie-1-couverture.webp",
        """L'école est le premier tribunal. C'est là que le décalage cesse d'être une simple singularité domestique, tolérée ou contournée par la tendresse familiale, pour devenir une infraction aux normes du groupe.

Tant que l'enfant évolue dans son cercle proche, ses maladresses peuvent passer pour de la fantaisie, ses silences pour de la timidité, ses lenteurs pour de la rêverie poétique. Mais dès l'entrée en cours préparatoire, l'institution déploie ses grilles d'évaluation uniformes : il faut tenir son crayon entre trois doigts avec une pression calibrée, reconnaître des graphèmes arbitraires en une fraction de seconde, rester assis six heures sur une chaise de bois sans gigoter, et restituer des consignes doubles ou triples sans jamais perdre le fil.

Pour l'enfant porteur d'un trouble dys ou d'un déficit d'attention, cette entrée en matière ressemble à une traversée en haute mer sur un radeau de fortune. Les autres avancent avec une aisance insolente : ils automatisent le geste de la boucle, retiennent l'ordre des lettres sans y penser, répètent les tables de mémoire comme une comptine. Pour lui, chaque geste exige une délibération consciente, un surcroît d'énergie épuisant.

Et le drame commence lorsque l'adulte, parent ou enseignant désemparé, pose sur cette détresse l'étiquette la plus dévastatrice qui soit : celle de la paresse.

« Il pourrait s'il voulait. » « Il ne fait aucun effort. » « Il a la tête dans les nuages. » Ces petites phrases assassines, répétées dix fois par jour au bas d'une dictée rougeoyante ou d'un problème de calcul inachevé, finissent par convaincre l'enfant de sa propre indignité. Il ne comprend pas pourquoi sa volonté, pourtant tendue à bloc jusqu'à en avoir mal au crâne et la nausée au ventre, ne produit que des résultats médiocres.

Alors, pour survivre au sentiment d'injustice, deux chemins destructeurs s'ouvrent à lui : le retrait dépressif (se faire oublier au fond de la classe, regarder par la fenêtre, s'éteindre doucement pour ne plus offrir de prise aux moqueries) ou la rébellion provocatrice (faire le pitre, casser le matériel, jouer les fortes têtes pour masquer sa terreur sous un masque de défi insolent).

Cette blessure originelle ne se referme jamais tout à fait. Elle s'incruste dans les profondeurs de l'estime de soi, prête à resurgir des décennies plus tard au détour d'un formulaire administratif à remplir ou d'une remarque anodine d'un supérieur hiérarchique."""
    ),
    (
        "chapitre-02.html",
        "02",
        "II. Les cinq familles de troubles : langage, geste et calcul",
        "PARTIE I : ANATOMIE DES DÉCALAGES",
        "public/books/approche-de-la-neurodiversite/images/neuro-schema-1-familles.svg",
        """Les manuels médicaux aiment classer les pathologies dans des tiroirs étanches. Dans la réalité vécue, ces troubles se croisent, s'entrelacent et se renforcent mutuellement dans une mosaïque complexe. On peut néanmoins dégager cinq grandes familles de perturbations, chacune attaquant un relais spécifique de l'apprentissage.

La première famille concerne le langage écrit : la dyslexie et la dysorthographie. Contrairement aux idées reçues, la dyslexie n'est pas une défaillance de la vue : c'est un dysfonctionnement du traitement phonologique et visio-spatial des symboles écrits. L'enfant peine à associer le son (phonème) à sa graphie (graphème). La forme visuelle des mots refuse de s'imprimer dans sa mémoire à long terme : il peut lire dix fois le mot « maison » sur la même page, et à la onzième ligne, son cerveau hésitera encore comme devant un hiéroglyphe inconnu. L'écriture qui en découle est lente, laborieuse, lardée de fautes phonétiques et d'inversions, transformant la moindre rédaction en calvaire musculaire et cognitif.

La deuxième famille touche le langage oral : la dysphasie. Moins fréquente mais encore plus isolante, elle altère l'organisation de la parole et parfois la compréhension des énoncés verbaux. L'enfant cherche ses mots, construit des phrases tronquées, bute sur la syntaxe, peine à décoder les intonations ou les doubles sens. La communication courante devient une épreuve de traduction permanente, engendrant des quiproquos douloureux avec les camarades et les adultes qui prennent sa réserve pour un manque d'intelligence.

La troisième famille est celle du geste et de l'espace : la dyspraxie motrice et visio-spatiale, souvent regroupée sous le terme de trouble du développement de la coordination (TDC). C'est l'impossibilité d'automatiser les séquences de gestes du quotidien. S'habiller, lacer ses chaussures, boutonner sa chemise, manier des ciseaux, tracer un cercle au compas ou utiliser une règle graduée : ce qui relève du réflexe naturel pour les autres exige pour le dyspraxique une concentration millimétrée de chaque seconde. La dysgraphie qui en découle rend l'écriture manuelle presque illisible et génère des crampes violentes dans l'avant-bras dès la troisième ligne de cahier.

La quatrième famille est celle des activités numériques : la dyscalculie. Souvent méconnue ou confondue avec un simple « manque de bosse des maths », elle perturbe la représentation mentale des grandeurs, l'ordre de grandeur des nombres et la logique des opérations. Le chiffre 38 se métamorphose en 83 lors de la copie ; les tables de multiplication refusent de s'ancrer durablement dans les neurones ; la lecture de l'heure sur un cadran à aiguilles reste un mystère déroutant, et le rendu de monnaie lors des courses devient une source d'angoisse quotidienne.

Enfin, la cinquième famille, transversale à toutes les autres, regroupe les déficits attentionnels et les pannes de mémoire de travail, que nous allons explorer en détail dans le chapitre suivant."""
    ),
    (
        "chapitre-03.html",
        "03",
        "III. L'attention en miettes et la mémoire qui fuit",
        "PARTIE I : ANATOMIE DES DÉCALAGES",
        "",
        """Si la parole entravée et le geste maladroit constituent la carcasse visible du handicap, l'usure la plus sourde et la plus destructrice se joue dans les coulisses de l'attention et de la mémoire de travail.

Chez une personne au fonctionnement ordinaire, le cerveau dispose d'un filtre sélectif redoutablement efficace : le thalamus et le cortex préfrontal travaillent de concert pour reléguer au second plan les bruits de circulation dans la rue, le bourdonnement du néon au plafond, le froissement de papier du voisin de table ou la démangeaison fugitive au coude. Seule l'information pertinente (la voix du professeur, la ligne du texte, le calcul en cours) accède au foyer de la conscience claire.

Chez la personne atteinte de troubles de l'attention (avec ou sans hyperactivité motrice), ce filtre ressemble à une passoire aux mailles déchirées.

Chaque stimulus de l'environnement immédiat arrive avec la même intensité, la même urgence, le même volume sonore. Une mouche qui tape contre la vitre, une porte qui grince dans le couloir, une craie qui crisse sur le tableau noir : l'esprit est violemment arraché à son objet d'étude toutes les quarante secondes. Il ne s'agit nullement d'un caprice ou d'une mauvaise éducation : c'est une défaillance neurologique de l'inhibition des distracteurs.

À cette perméabilité épuisante s'ajoute l'étroitesse dramatique de la mémoire de travail. La mémoire de travail est la table d'opération du cerveau, la zone tampon où l'on maintient actives les données le temps d'accomplir une opération mentale. Chez une personne moyenne, cette table peut accueillir environ sept éléments distincts. Chez un profil dys ou TDA, la table est minuscule et encombrée : elle ne peut retenir que deux ou trois informations à la fois avant de saturer complètement.

Donnez à un enfant dyspraxique la consigne suivante : « Ouvre ton livre de géographie à la page quarante-deux, prends ton crayon rouge dans ta trousse et souligne le titre du document trois en double trait. »

Pour son cerveau, c'est une surcharge cognitive foudroyante. Il ouvre son cartable, cherche son livre, et le temps de trouver la page quarante-deux, la couleur du crayon et la nature du document ont déjà disparu de sa mémoire immédiate comme de l'eau tiède jetée sur une plaque de zinc brûlante. Il lève les yeux, perdu, et le professeur s'agace : « Tu ne m'écoutes jamais ! »

L'adulte porte en lui ces mêmes failles : oubli des rendez-vous malgré un agenda rempli, perte chronique des clés de maison ou des lunettes, difficulté à suivre une conversation soutenue dans un restaurant bruyant, fatigue écrasante au bout d'une heure de réunion en visioconférence. Ce n'est pas de la négligence : c'est un moteur qui tourne constamment en surrégime pour maintenir à flot une mémoire qui fuit."""
    ),
    (
        "chapitre-04.html",
        "04",
        "IV. L'usure adulte et le malentendu permanent",
        "PARTIE I : ANATOMIE DES DÉCALAGES",
        "",
        """Il existe une croyance naïve, confortée par un demi-siècle de discours pédiatriques rassurants, selon laquelle les troubles dys finiraient par s'évaporer au sortir de l'adolescence, dissous par la grâce de la majorité civile ou l'obtention d'un diplôme d'apprentissage.

C'est une fable commode. On ne guérit pas d'une architecture cérébrale atypique. On apprend seulement à faire semblant avec plus ou moins de brio.

À l'âge adulte, la sanction ne prend plus la forme d'un zéro pointé à l'encre rouge sur une copie de français : elle prend celle, bien plus sournoise, d'une lettre de licenciement pour faute d'inattention, d'un refus d'embauche après un test psychotechnique chronométré, d'une relance d'huissier pour une facture égarée au fond d'un tiroir, ou d'un conflit conjugal né d'un oubli répété pris pour un manque d'amour.

L'adulte dys évolue dans un monde conçu par et pour des profils neurotypiques, où la rapidité d'exécution, la polyvalence multitâche et l'aptitude à manipuler des abstractions administratives constituent le mètre étalon de la valeur sociale.

Remplir une déclaration d'impôts en ligne, vérifier un bail de location, calculer une mensualité de crédit avec taux variable, s'orienter dans un parking souterrain à trois niveaux ou rédiger un rapport professionnel sans laisser échapper de coquille grossière : chacune de ces tâches ordinaires représente pour lui une montagne rocheuse à escalader à mains nues.

Pour masquer ces défaillances et éviter le jugement méprisant de ses pairs, l'adulte déploie des trésors d'énergie dans des stratégies de compensation épuisantes. Il compense sa lenteur en travaillant le soir et le week-end ; il compense ses trous de mémoire en se créant des rituels maniaques d'organisation ; il s'interdit les promotions qui l'exposeraient à des réunions trop verbales ou à des synthèses écrites publiques.

Cette vigilance de chaque seconde porte un nom en psychologie cognitive : le coût du masquage.

Au fil des années, ce masquage permanent use l'organisme jusqu'à la corde. Il conduit à des états de burn-out atypiques, incompris du corps médical qui y voit une banale dépression réactionnelle, alors qu'il s'agit du simple épuisement mécanique d'une machine dont les bielles ont tourné trente ans sans une goutte d'huile de tolérance sociale."""
    )
]

for filename, num, title, byline, img, text in part1_chapters:
    paras = text.strip().split("\n\n")
    html_paras = []
    for p in paras:
        clean_p = p.replace("\n", " ").strip()
        html_paras.append(f'<p class="chapter-paragraph">{clean_p}</p>')
    
    body = "\n".join(html_paras)
    img_html = ""
    if img:
        img_html = f"""  <figure class="chapter-figure">
    <img src="{img}" alt="Illustration de {title}" loading="lazy" />
  </figure>\n"""
    
    content = f"""<div class="chapter-content">
  <h1 class="chapter-main-title"><strong>{title}</strong></h1>
  <p class="chapter-byline">{byline}</p>
{img_html}{body}
</div>
"""
    (out_dir / filename).write_text(content, encoding="utf-8")
    print(f"Written {filename}")

print("PART I GENERATION COMPLETE")