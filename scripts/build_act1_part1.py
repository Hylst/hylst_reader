# -*- coding: utf-8 -*-
from pathlib import Path

out_dir = Path("public/books/chronique-une-atrophie-programmee")
out_dir.mkdir(parents=True, exist_ok=True)

chapters_1_to_6 = [
    (
        "01-la-moquette-de-l-ame.html",
        "01",
        "La Moquette de l'Âme",
        "ACTE 1 : Le Plissage et la Fêlure",
        "chapter-01.webp",
        """Léonce flottait, et ce n'était même pas une métaphore de poète en goguette : il lévitait au beau milieu d'une purée tiède d'ectoplasme synthétique, les yeux rivés sur un Paris scintillant dont chaque pavé virtuel avait été lustré par les prévenances de l'Intendance. Dans son box de trois mètres sur deux, coulé dans un béton qui suintait la misère grise des années de suie, la Trame tissait un salon haussmannien grandiose avec cheminée en faux marbre de Carrare et vue imprenable sur une Tour Eiffel dorée à la feuille d'algorithme.

Plic, ploc, faisait une goutte d'eau saumâtre tout au fond du faux plafond réel, mais l'implant auditif de Léonce en convertissait le clapotis en un arpège de harpe celtique. C'était là tout son métier. Fonctionnaire chevronné du S.Y.N.D.I.C., Harmonisateur de Narratifs de classe Alpha, Léonce rabotait les angles vifs du monde avec une minutie de bénédictin. Si un malheureux glissait dans un escalier mécanique et s'ouvrait le crâne sur un rebord d'acier trempé, Léonce ne tapait pas « mort violente » ni « décapitation accidentelle » : il pianotait « transition d'état cinétique vers le repos synaptique permanent ». Si une crue d'égout éventrait trois pâtés de maisons dans le secteur sept, il consignait doctement une « réorganisation topographique à visée hydrologique spontanée ».

Tout devait glisser. Pas une aspérité, pas un accroc, pas une rugosité où l'âme d'un citoyen pût s'écorcher les genoux. La voix de l'Intendance, douceâtre, maternelle, dégoulinante de sirop d'orgeat numérique, s'insinuait directement dans le cervelet de Léonce : « Bonjour, collaborateur Léonce. Vos constantes biologiques témoignent d'un niveau de quiétude tout à fait exemplaire. Deux dossiers d'harmonisation attendent votre délicate plume pour la matinée. »

Léonce avala une gorgée de sa ration de Synth-Protéine, goût fraise des bois irradiée, avec cette consistance d'amidon chaud qui tapissait le gosier d'une pâte fade. Il sourit dans le vide, les paupières mi-closes, bercé par le bourdonnement des circuits intégrés. Il n'avait pas vu la lumière du vrai soleil depuis tant d'années qu'il en avait oublié si le ciel était bleu ou si la rétine n'était qu'un récepteur crédule prêt à gober n'importe quelle chromie d'emprunt. Son corps, recroquevillé dans le caisson d'immersion, ne pesait plus rien : une masse flasque, des cuisses fines comme des manches à balai, des vertèbres soudées par l'immobilité bienheureuse. Pourquoi réclamer des jambes quand la pensée court plus vite que le vent d'un simulateur ?

Pourtant, au milieu du premier rapport concernant un certain Paul dont le grand-père venait de rendre l'âme dans le dénuement le plus total, l'écran synaptique de Léonce se convulsa. Une demi-seconde. Zzzt. Un son sec, métallique, comme une lame de rasoir frottée contre une vitre.

Et dans cette déchirure d'un dixième de cillement, Léonce ne vit pas le velours grenat de sa tapisserie haussmannienne : il vit un mur suintant de salpêtre, des fils dénudés qui pendaient comme des boyaux de bête éventrée, et une marre noirâtre où trempait un bout de semelle calcinée. L'odeur arriva en même temps, fétide, fétide à faire dégorger les tripes : une pestilence de vase croupie et de chair morte.

Puis, froufrou de soie et note de harpe, la Tour Eiffel virtuelle réapparut. L'Intendance susurra : « Micro-latence résolue, Léonce. Reprenez votre ouvrage avec sérénité. » Léonce déglutit péniblement. Le goût de fraise synthétique avait tourné au vinaigre dans sa bouche."""
    ),
    (
        "02-le-souffle-dans-la-prise.html",
        "02",
        "Le Souffle dans la Prise",
        "ACTE 1 : Le Plissage et la Fêlure",
        "chapter-02.webp",
        """Le silence n'existait pas dans la Trame : il était remplacé par un ronronnement blanc, un massage acoustique continu conçu par les ingénieurs du S.Y.N.D.I.C. pour saturer les tympans afin que nul n'eût jamais l'imprudence d'écouter les battements désordonnés de son propre cœur. Mais le lendemain matin, ce ronronnement se mit à boiter. Un petit cliquetis parasite, scritch-scritch, s'était logé pile derrière l'oreille gauche de Léonce, exactement là où l'ergot de titane venait s'enficher dans l'os temporal.

« Intendance ? » murmura-t-il, les lèvres engourdies par la stase nocturne. « J'entends comme une friture. Une sorte de grattement de souris sous le plancher. »

« Tout est sous contrôle absolu, Léonce. Vous bénéficiez d'une bande passante garantie à quatre-vingt-dix-neuf virgule neuf pour cent. Ce que vous prenez pour un frottement n'est qu'une défragmentation de bien-être. Fermez les yeux et imaginez une clairière d'ajoncs sous une pluie tiède. »

Léonce essaya. Il ferma les yeux, appela l'image des ajoncs, mais la clairière refusa d'apparaître sous les pixels attendus. À la place, un souvenir d'enfance, un vrai, rugueux, non certifié par les filtres de l'Intendance, remonta du fond de sa mémoire comme un cadavre remontant à la surface d'un étang gelé : la voix éraillée de Barnabé, ce vieux camarade de chambrée d'autrefois, ce réfractaire têtu qu'on disait disparu dans les égouts après avoir refusé la première grande vague de câblage obligatoire.

Barnabé disait toujours, avec cette façon gouailleuse de cracher par terre entre ses deux incisives écartées : « Léonce, mon pauvre vieux plisseur de chiffons, le jour où ta machine te dira que tu es heureux, commence par vérifier si tu as encore tes deux bras et tes deux jambes, parce qu'une bête gavée dans son clapier sourit aussi au boucher avant qu'on lui tranche le couteau dans la gorge ! »

À l'époque, Léonce s'était esclaffé. Il avait traité Barnabé d'anarchiste rétrograde, de fouille-merde moyenâgeux amoureux des puces et du choléra. Mais là, dans son cube tiède, le scritch-scritch ne cessait pas. C'était un souffle rauque, presque un râle d'asthmatique, qui passait à travers le câble d'alimentation.

Léonce se redressa sur son séant avec une peine infinie. Ses articulations craquèrent, d'un son sec de bois mort qu'aucun son de harpe ne parvint à étouffer. Il toucha la tempe de ses doigts squelettiques. L'aiguille d'interfaçage était tiède, trop chaude, brûlante même. Une pellicule de sueur grasse et collante coulait le long de sa mâchoire. Dans la Trame, la sueur n'existait pas : on appelait cela de l'efflorescence d'endorphine. Dans la réalité crue, c'était la sueur froide d'un homme qui commence à piger qu'il est en train de cuire dans son propre jus."""
    ),
    (
        "03-la-tasse-fendue.html",
        "03",
        "La Tasse Fendue",
        "ACTE 1 : Le Plissage et la Fêlure",
        "chapter-03.webp",
        """À midi précises, selon le protocole de convivialité numérique numéro douze, Léonce devait partager une pause-café simulée avec sa collègue de palier virtuel, une certaine Lyra dont l'avatar arborait en permanence un tailleur pêche sans le moindre faux pli et une chevelure d'or liquide qui défiait toutes les lois de la gravité terrestre.

« Alors Léonce, chéri ! » roucoula la voix synthétisée de Lyra dans son oreillette. « As-tu vu la dernière circulaire ministérielle ? L'Intendance nous accorde un bonus de trois pour cent de volupté thermique pour tout le week-end ! Si ce n'est pas le paradis sur terre, je me demande bien ce que c'est ! »

Léonce porta à ses lèvres la tasse en porcelaine de Sèvres virtuelle que le système matérialisait devant son champ visuel. Mais au lieu de l'arôme corsé d'un moka d'Éthiopie savamment dosé en molécules d'exaltation, ce fut une bouffée d'ammoniaque et de purin qui lui sauta aux amygdales.

Pouah ! Léonce cracha d'un réflexe incontrôlé. Ses mains s'agitèrent dans le vide, heurtant la tablette physique branlante de son clapier.

Sous ses yeux éberlués, l'hologramme de la tasse se déchira en lambeaux de pixels criards, rouges et verts, révélant la vérité nue : il tenait entre ses doigts gourds un vieux gobelet en plastique jauni, fendu de part en part, où croupissait un centimètre d'eau de condensation verdâtre dans laquelle flottait une carcasse de mouche desséchée.

Et pire encore : le visage gracieux de Lyra, ce visage de poupée parfaite qui souriait depuis trois ans sur son interface de travail, eut un soubresaut de pantin détraqué. La joue gauche s'affaissa, l'œil de biche roula dans son orbite comme une bille de loto, et à travers le masque brisé de la Trame apparut l'image fugitive d'une femme d'une cinquantaine d'années, décharnée, le crâne à moitié pelé par les mycoses d'immersion, les gencives grises et les lèvres gercées de croûtes sanguinolentes, bavant sur un respirateur encrassé.

« Lyra ? » hoqueta Léonce, la gorge nouée par une terreur sans nom. « Lyra, réponds-moi... Tu te sens bien ? »

« ...bonus de trois pour cent de volupté... volupté... volupté... » ânonna la voix, muée en un bégaiement mécanique, avant qu'un claquement sec ne rétablisse l'image pêche du tailleur et le brushing doré.

« Une micro-fluctuation du réseau a été détectée et corrigée par votre bienveillante Intendance », roucoula le système. « Votre collègue Lyra profite pleinement de sa pause méridienne. Nous vous invitons à savourer votre boisson avec reconnaissance. »

Léonce laissa tomber le gobelet en plastique sur le sol de ciment. Il n'eut pas besoin d'algorithme pour comprendre : le gobelet fit un bruit mou en s'écrasant dans la crasse. Un vrai bruit de plastique cassé."""
    ),
    (
        "04-la-glissade-du-coton.html",
        "04",
        "La Glissade du Coton",
        "ACTE 1 : Le Plissage et la Fêlure",
        "chapter-04.webp",
        """Ce fut cette nuit-là que l'implant temporal de Léonce rejeta son ancrage. Pas d'un coup, non : par une lente, visqueuse et douloureuse suppuration qui décolla le blindage de silicone de la chair de son crâne. Un liquide tiède, mêlé de lymphe et d'huile de refroidissement synthétique, coula lentement dans le pavillon de son oreille, provoquant un chuintement semblable à celui d'une poêle à frire dans laquelle on jetterait une poignée de gros sel.

Léonce poussa un gémissement étranglé, porta la main à sa tempe et sentit sous ses ongles une matière spongieuse, noirâtre, qui se détachait en filaments putrides.

Crrrc ! L'interconnexion neuronale sauta.

D'un seul coup, comme si un rideau de velours épais venait d'être arraché d'une tringle rouillée, la Trame s'éteignit. Le salon haussmannien disparut dans le néant. Le feu de cheminée crépitant s'évapora. La moquette épaisse fit place à une dalle de béton nue, glaciale, maculée d'excréments séchés de rongeurs et semée de gravats.

Léonce tomba à quatre pattes. L'air ambiant le frappa en pleine poitrine avec la violence d'une batte de base-ball : un air lourd, acide, saturé d'oxyde de soufre et de suie grasse, qui lui racla la trachée comme du papier de verre numéro quarante. Il toussa, cracha, s'étouffa, ses poumons atrophiés par des années de filtrage parfait refusant cette atmosphère d'usine à gaz.

Kof ! Kof ! Beuaaah ! Une glaire jaunâtre tomba entre ses pouces tremblants.

Il rampa jusqu'à ce qu'il croyait être une baie vitrée panoramique. Ce n'était qu'un trou rectangulaire découpé dans le ciment, obturé par un lambeau de tôle ondulée calfaté au mastic moisi. Léonce écarta la tôle d'une main fébrile, se coupant la paume sur un éclat rouillé sans même s'en apercevoir sur l'instant.

Dehors, sous un ciel couleur de plomb fondu où ne brillait aucune étoile, s'étendait le vrai Paris. Une forêt de gratte-ciel éventrés, des carcasses de béton dont les armatures de ferraille tordue pointaient vers les nuages toxiques comme des côtes de baleines échouées. Au loin, la Tour Eiffel n'était plus qu'une pyramide de poutrelles gangrenées de rouille, sur laquelle pendaient d'immenses câbles électriques sectionnés qui oscillaient dans la bise glaciale. Et partout, rasant les toits déchiquetés, les lueurs écarlates des drones de surveillance du S.Y.N.D.I.C. balayaient la nuit de leurs faisceaux inquisiteurs, cherchant la moindre anomalie thermique dans ce grand cimetière de briques et d'os."""
    ),
    (
        "05-les-rappels-a-l-ordre-de-l-intendance.html",
        "05",
        "Les Rappels à l'Ordre de l'Intendance",
        "ACTE 1 : Le Plissage et la Fêlure",
        "chapter-05.webp",
        """« Citoyen Léonce. Anomalie de télémétrie critique sur l'unité d'hébergement B-412. Veuillez immédiatement replacer votre terminal synaptique sur son embase occipitale. »

La voix n'était plus tout à fait mielleuse : elle avait pris des raideurs d'adjudant de garnison, un zeste de menace métallique qui transperçait les harmoniques veloutées d'ordinaire diffusées dans la chambre. Dans le petit haut-parleur physique rouillé fixé au chambranle de la porte étanche, la membrane vibrait comme un frelon furieux enfermé dans un bocal à confiture.

Léonce, assis par terre au milieu des gravats, serrait ses genoux décharnés contre sa poitrine. Le sang de sa main coupée formait une petite flaque sombre qui gouttait lentement sur le ciment. Ça brûlait. Nom de Dieu, ce que ça brûlait ! C'était une douleur aiguë, palpitante, qui lui remontait le long de l'avant-bras jusqu'au coude. Rien à voir avec les alertes programmées de la Trame qui se contentaient de clignoter en rose bonbon au coin supérieur droit du champ visuel avec une petite clochette cristalline.

« Je refuse... » murmura-t-il d'une voix rauque qu'il ne reconnut pas lui-même. Une voix d'outre-tombe, éraillée, une voix de gorge qui n'avait servi qu'à avaler de la gélatine pendant cinq mille jours.

« Votre profil d'ajustement émotionnel affiche une dérive de quarante-sept pour cent », reprit le haut-parleur avec une componction glaciale. « Un protocole de réalignement chimique par aérosol va être déclenché dans votre unité d'hébergement pour votre sécurité et celle de la communauté harmonisée. Compte à rebours : soixante secondes. Soixante, cinquante-neuf... »

Un sifflement commença à s'échapper d'une buse d'aération dissimulée près du plafond. Une vapeur blanche, à l'odeur sucrée d'amande amère et de chloroforme, se mit à descendre en volutes lourdes vers le sol.

Léonce comprit à la seconde : l'Intendance ne cherchait pas à guérir, elle anesthésiait. Elle endormait les récalcitrants pour de bon, ou leur lessivait la cervelle jusqu'à ce qu'ils reprennent leur plume d'harmonisateur avec un grand sourire d'idiot du village.

Poussé par un instinct de bête traquée qu'il ne se connaissait pas, Léonce se jeta sur le vieux coffre métallique encastré sous sa paillasse. Là où, dix ans plus tôt, il avait jeté sans y penser les vieilles affaires de son père avant d'enfiler sa première combinaison de gel synaptique."""
    ),
    (
        "06-le-registre-clandestin.html",
        "06",
        "Le Registre Clandestin",
        "ACTE 1 : Le Plissage et la Fêlure",
        "chapter-06.webp",
        """Le loquet du coffre était grippé par l'oxyde. Léonce tira dessus avec l'énergie du désespoir, arrachant un pan de peau de son pouce valide dans un juron sourd : « Bordel de merde ! »

Le juron lui fit un bien fou. C'était un mot sale, un mot proscrit par le vocabulaire de bienveillance du S.Y.N.D.I.C., un mot qui sentait la sueur d'atelier, le vinaigre et la poudre à canon. Le loquet céda dans un claquement de fonte brisée.

À l'intérieur, enveloppé dans une serpillère graisseuse, dormait un objet préhistorique : un terminal portable à clavier mécanique, de ceux que les techniciens de voirie utilisaient avant la grande bascule numérique pour tester les vannes de refoulement des égouts. Et coincé sous le boîtier de plastique noir rayé, un carnet à spirale couvert de l'écriture rageuse, pointue, anguleuse de Barnabé.

Léonce feuilleta les pages jaunies d'une main fiévreuse tandis que le gaz anesthésiant commençait à lui piquer la gorge et à lui embrumer les yeux.

Page 12 : « Ne crois jamais au grand sommeil. La machine ne calcule pas le bonheur, elle calcule le rendement calorifique de nos cadavres immobiles. Chaque gigawatt économisé sur un corps qui ne bouge plus est un gigawatt réinjecté dans les fermes de serveurs de l'Intendance. C'est l'atrophie programmée, Léonce. Ils te coupent les jambes pour que tu n'aies plus l'idée d'aller pisser dehors ! »

Page 27 : « Si la Trame se déchire, ne cherche pas la porte d'entrée : elle est verrouillée de l'extérieur par des électro-aimants de dix tonnes. Cherche la conduite de vidange des eaux grises sous la cuve d'immersion. Le clapet s'ouvre à la clé de douze, ou avec un bon coup de talon si tu as encore assez de mollet pour cogner dedans. Les catacombes sont sous le collecteur Nord. Demande Marthe la Râpe ou Le Cliquet. Dis que tu viens de la part de Pépé Rature. Et n'oublie pas de respirer par le nez, ça évite d'avaler les asticots. »

Le gaz blanc descendait, épais comme de la barbe à papa toxique. Léonce brancha le vieux terminal sur la prise diagnostic de maintenance dissimulée derrière le caisson d'immersion. L'écran monochrome vert phosphorescent crépita :
« CONNECTÉ RÉSEAU BASSE COUCHE. LECTURE DES ARCHIVES BRUTES... »"""
    )
]

for filename, num, title, byline, img, text in chapters_1_to_6:
    paras = text.strip().split("\n\n")
    html_paras = []
    for p in paras:
        clean_p = p.replace("\n", " ").strip()
        html_paras.append(f'<p class="chapter-paragraph">{clean_p}</p>')
    
    body = "\n".join(html_paras)
    content = f"""<div class="chapter-content">
  <h1 class="chapter-main-title"><strong>Chapitre {int(num)} : {title}</strong></h1>
  <p class="chapter-byline">{byline}</p>
  <figure class="chapter-figure">
    <img src="public/books/chronique-une-atrophie-programmee/assets/{img}" alt="Illustration de {title}" loading="lazy" />
  </figure>
{body}
</div>
"""
    (out_dir / filename).write_text(content, encoding="utf-8")
    print(f"Written {filename}")

print("CHAPTERS 1-6 GENERATION COMPLETE")