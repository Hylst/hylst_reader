# -*- coding: utf-8 -*-
from pathlib import Path

img_dir = Path("public/books/approche-de-la-neurodiversite/images")
img_dir.mkdir(parents=True, exist_ok=True)

# SVG 1: Cartographie des 5 familles dys
svg1 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 620" width="100%" height="auto" role="img" aria-label="Cartographie des troubles cognitifs et de leurs interferences">
  <defs>
    <style>
      .bg { fill: #f8fafc; }
      .card { fill: #ffffff; stroke: #cbd5e1; stroke-width: 1.5; rx: 10px; }
      .card-accent { fill: #eff6ff; stroke: #3b82f6; stroke-width: 2; rx: 10px; }
      .card-warn { fill: #fff7ed; stroke: #f97316; stroke-width: 1.5; rx: 10px; }
      .title { font-family: system-ui, -apple-system, sans-serif; font-size: 18px; font-weight: 700; fill: #0f172a; }
      .subtitle { font-family: system-ui, -apple-system, sans-serif; font-size: 13px; font-weight: 600; fill: #334155; }
      .txt { font-family: system-ui, -apple-system, sans-serif; font-size: 12px; fill: #475569; }
      .txt-bold { font-family: system-ui, -apple-system, sans-serif; font-size: 12px; font-weight: 600; fill: #1e293b; }
      .tag { font-family: system-ui, -apple-system, sans-serif; font-size: 11px; font-weight: 700; fill: #1d4ed8; letter-spacing: 0.5px; }
      .tag-warn { font-family: system-ui, -apple-system, sans-serif; font-size: 11px; font-weight: 700; fill: #c2410c; }
      .arrow { stroke: #94a3b8; stroke-width: 2; stroke-dasharray: 4 4; fill: none; marker-end: url(#arrowhead); }
      @media (prefers-color-scheme: dark) {
        .bg { fill: #0f172a; }
        .card { fill: #1e293b; stroke: #334155; }
        .card-accent { fill: #172554; stroke: #60a5fa; }
        .card-warn { fill: #431407; stroke: #fb923c; }
        .title { fill: #f8fafc; }
        .subtitle { fill: #e2e8f0; }
        .txt { fill: #94a3b8; }
        .txt-bold { fill: #cbd5e1; }
        .tag { fill: #93c5fd; }
        .tag-warn { fill: #fdba74; }
        .arrow { stroke: #64748b; }
      }
    </style>
    <marker id="arrowhead" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
      <polygon points="0 0, 8 3, 0 6" fill="#94a3b8" />
    </marker>
  </defs>

  <rect width="100%" height="100%" class="bg" rx="14" />

  <!-- En-tete -->
  <text x="480" y="38" text-anchor="middle" class="title">Cartographie des Troubles Cognitifs et de leurs Répercussions</text>
  <text x="480" y="60" text-anchor="middle" class="txt">Architecture des cinq familles dys : un relais défaillant dans une intelligence normale</text>

  <!-- Bloc 1 : Langage ecrit -->
  <g transform="translate(40, 90)">
    <rect width="260" height="150" class="card" />
    <text x="16" y="28" class="tag">01. LANGAGE ÉCRIT</text>
    <text x="16" y="50" class="subtitle">Dyslexie &amp; Dysorthographie</text>
    <text x="16" y="74" class="txt">• Lecture hachée, déchiffrage lent</text>
    <text x="16" y="94" class="txt">• Forme visuelle des mots fuyante</text>
    <text x="16" y="114" class="txt">• Fatigue oculaire et cérébrale précoce</text>
    <text x="16" y="134" class="txt-bold">Impact : scolarité littéraire ralentie</text>
  </g>

  <!-- Bloc 2 : Langage oral -->
  <g transform="translate(350, 90)">
    <rect width="260" height="150" class="card" />
    <text x="16" y="28" class="tag">02. LANGAGE ORAL</text>
    <text x="16" y="50" class="subtitle">Dysphasie de développement</text>
    <text x="16" y="74" class="txt">• Prononciation et débit heurtés</text>
    <text x="16" y="94" class="txt">• Recherche laborieuse du mot exact</text>
    <text x="16" y="114" class="txt">• Décodage subtil des intonations lent</text>
    <text x="16" y="134" class="txt-bold">Impact : communication sociale entravée</text>
  </g>

  <!-- Bloc 3 : Psychomoteur & Espace -->
  <g transform="translate(660, 90)">
    <rect width="260" height="150" class="card" />
    <text x="16" y="28" class="tag">03. GESTE &amp; ESPACE</text>
    <text x="16" y="50" class="subtitle">Dyspraxie, TAC &amp; Dysgraphie</text>
    <text x="16" y="74" class="txt">• Écriture manuelle douloureuse</text>
    <text x="16" y="94" class="txt">• Maladresse gestuelle au quotidien</text>
    <text x="16" y="114" class="txt">• Repérage spatial et géométrie fuyants</text>
    <text x="16" y="134" class="txt-bold">Impact : perte d'autonomie pratique</text>
  </g>

  <!-- Bloc 4 : Attention & Execution -->
  <g transform="translate(180, 275)">
    <rect width="275" height="150" class="card" />
    <text x="16" y="28" class="tag">04. ATTENTION &amp; FOCUS</text>
    <text x="16" y="50" class="subtitle">TDA/H &amp; Fonctions Exécutives</text>
    <text x="16" y="74" class="txt">• Filtre attentionnel perméable</text>
    <text x="16" y="94" class="txt">• Captation impromptue par les stimuli</text>
    <text x="16" y="114" class="txt">• Difficulté à initier et maintenir la tâche</text>
    <text x="16" y="134" class="txt-bold">Impact : dispersion et épuisement mental</text>
  </g>

  <!-- Bloc 5 : Memoire & Calcul -->
  <g transform="translate(505, 275)">
    <rect width="275" height="150" class="card" />
    <text x="16" y="28" class="tag">05. MÉMOIRE &amp; CALCUL</text>
    <text x="16" y="50" class="subtitle">Mémoire de travail &amp; Dyscalculie</text>
    <text x="16" y="74" class="txt">• Saturation immédiate des consignes</text>
    <text x="16" y="94" class="txt">• Tables, conversions et durées floues</text>
    <text x="16" y="114" class="txt">• Décalage entre logique et manipulation</text>
    <text x="16" y="134" class="txt-bold">Impact : gestion du temps et des comptes</text>
  </g>

  <!-- Nœud central transversal : Le Foyer Commun -->
  <g transform="translate(140, 460)">
    <rect width="680" height="125" class="card-warn" />
    <text x="340" y="30" text-anchor="middle" class="tag-warn">LE SOCLE COMMUN DU VÉCU DYS</text>
    <text x="340" y="54" text-anchor="middle" class="subtitle">Surcharge Cognitive · Usure Invisible · Jugement Social Biaisé</text>
    <text x="340" y="80" text-anchor="middle" class="txt">Le décalage ne relève ni d'une mauvaise volonté, ni d'un déficit d'intelligence :</text>
    <text x="340" y="102" text-anchor="middle" class="txt-bold">Il exige un surcoût d'énergie permanent pour compenser chaque seconde ce que d'autres automatisent.</text>
  </g>

  <!-- Lignes d'influence -->
  <path d="M 170 240 L 300 460" class="arrow" />
  <path d="M 480 240 L 480 460" class="arrow" />
  <path d="M 790 240 L 660 460" class="arrow" />
</svg>
"""

# SVG 2: Accompagnement scolaire et demarche pedagogique
svg2 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 560" width="100%" height="auto" role="img" aria-label="Dynamique de l'accompagnement scolaire pour enfants en difficulte">
  <defs>
    <style>
      .bg { fill: #f8fafc; }
      .card-err { fill: #fef2f2; stroke: #ef4444; stroke-width: 1.5; rx: 10px; }
      .card-ok { fill: #f0fdf4; stroke: #22c55e; stroke-width: 1.5; rx: 10px; }
      .card-pivot { fill: #eff6ff; stroke: #3b82f6; stroke-width: 2; rx: 10px; }
      .title { font-family: system-ui, -apple-system, sans-serif; font-size: 18px; font-weight: 700; fill: #0f172a; }
      .subtitle { font-family: system-ui, -apple-system, sans-serif; font-size: 13px; font-weight: 600; fill: #334155; }
      .txt { font-family: system-ui, -apple-system, sans-serif; font-size: 12px; fill: #475569; }
      .txt-bold { font-family: system-ui, -apple-system, sans-serif; font-size: 12px; font-weight: 600; fill: #1e293b; }
      .tag-err { font-family: system-ui, -apple-system, sans-serif; font-size: 11px; font-weight: 700; fill: #b91c1c; }
      .tag-ok { font-family: system-ui, -apple-system, sans-serif; font-size: 11px; font-weight: 700; fill: #15803d; }
      .tag-pivot { font-family: system-ui, -apple-system, sans-serif; font-size: 11px; font-weight: 700; fill: #1d4ed8; }
      .arr-err { stroke: #ef4444; stroke-width: 2; fill: none; marker-end: url(#arr-err); }
      .arr-ok { stroke: #22c55e; stroke-width: 2; fill: none; marker-end: url(#arr-ok); }
      @media (prefers-color-scheme: dark) {
        .bg { fill: #0f172a; }
        .card-err { fill: #450a0a; stroke: #f87171; }
        .card-ok { fill: #052e16; stroke: #4ade80; }
        .card-pivot { fill: #172554; stroke: #60a5fa; }
        .title { fill: #f8fafc; }
        .subtitle { fill: #e2e8f0; }
        .txt { fill: #94a3b8; }
        .txt-bold { fill: #cbd5e1; }
        .tag-err { fill: #fca5a5; }
        .tag-ok { fill: #86efac; }
        .tag-pivot { fill: #93c5fd; }
      }
    </style>
    <marker id="arr-err" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
      <polygon points="0 0, 8 3, 0 6" fill="#ef4444" />
    </marker>
    <marker id="arr-ok" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
      <polygon points="0 0, 8 3, 0 6" fill="#22c55e" />
    </marker>
  </defs>

  <rect width="100%" height="100%" class="bg" rx="14" />

  <text x="480" y="38" text-anchor="middle" class="title">Accompagnement de l'Enfant : Sortir de l'Engrenage de l'Échec</text>
  <text x="480" y="60" text-anchor="middle" class="txt">La rupture de la spirale punitive au profit d'une remédiation pragmatique</text>

  <!-- Colonne Gauche : La Spirale de l'Echec -->
  <g transform="translate(50, 90)">
    <text x="180" y="24" text-anchor="middle" class="tag-err">L'ENGRENAGE DE LA BLESSURE</text>
    
    <g transform="translate(0, 40)">
      <rect width="360" height="70" class="card-err" />
      <text x="16" y="26" class="subtitle">1. Blocage d'apprentissage initial</text>
      <text x="16" y="48" class="txt">Mécanisme dys ignoré ou pris pour de la distraction.</text>
    </g>

    <g transform="translate(0, 130)">
      <rect width="360" height="70" class="card-err" />
      <text x="16" y="26" class="subtitle">2. Sanction scolaire &amp; Mauvaise note</text>
      <text x="16" y="48" class="txt">Le résultat chiffré condamne l'effort invisible fourni.</text>
    </g>

    <g transform="translate(0, 220)">
      <rect width="360" height="70" class="card-err" />
      <text x="16" y="26" class="subtitle">3. Jugement social &amp; Incompréhension</text>
      <text x="16" y="48" class="txt">« Il ne fait aucun effort », « Il est dans la lune ».</text>
    </g>

    <g transform="translate(0, 310)">
      <rect width="360" height="70" class="card-err" />
      <text x="16" y="26" class="subtitle">4. Agressivité ou Retrait dépressif</text>
      <text x="16" y="48" class="txt">L'enfant capitule pour se protéger du mépris.</text>
    </g>

    <path d="M 180 110 L 180 130" class="arr-err" />
    <path d="M 180 200 L 180 220" class="arr-err" />
    <path d="M 180 290 L 180 310" class="arr-err" />
  </g>

  <!-- Colonne Droite : La Remédiation Bienveillante -->
  <g transform="translate(550, 90)">
    <text x="180" y="24" text-anchor="middle" class="tag-ok">LE LEVIER PÉDAGOGIQUE DU TERRAIN</text>

    <g transform="translate(0, 40)">
      <rect width="360" height="70" class="card-ok" />
      <text x="16" y="26" class="subtitle">1. Écoute sans jugement &amp; Diagnostic</text>
      <text x="16" y="48" class="txt">Identifier la source : ambiance de classe, fatigue, dys.</text>
    </g>

    <g transform="translate(0, 130)">
      <rect width="360" height="70" class="card-ok" />
      <text x="16" y="26" class="subtitle">2. Dédramatisation de la note</text>
      <text x="16" y="48" class="txt">Séparer la valeur de l'enfant de son carnet de notes.</text>
    </g>

    <g transform="translate(0, 220)">
      <rect width="360" height="70" class="card-ok" />
      <text x="16" y="26" class="subtitle">3. Méthode du pas-à-pas &amp; Concret</text>
      <text x="16" y="48" class="txt">Micro-objectifs, pauses récréatives, supports visuels.</text>
    </g>

    <g transform="translate(0, 310)">
      <rect width="360" height="70" class="card-ok" />
      <text x="16" y="26" class="subtitle">4. Victoires minuscules &amp; Confiance</text>
      <text x="16" y="48" class="txt">L'enfant retrouve le plaisir d'oser apprendre.</text>
    </g>

    <path d="M 180 110 L 180 130" class="arr-ok" />
    <path d="M 180 200 L 180 220" class="arr-ok" />
    <path d="M 180 290 L 180 310" class="arr-ok" />
  </g>

  <!-- Pont central de bascule -->
  <g transform="translate(425, 230)">
    <rect width="110" height="70" class="card-pivot" />
    <text x="55" y="28" text-anchor="middle" class="tag-pivot">POSTURE</text>
    <text x="55" y="48" text-anchor="middle" class="txt-bold">Tuteur d'égal</text>
    <text x="55" y="62" text-anchor="middle" class="txt-bold">à égal</text>
  </g>
  <path d="M 410 265 L 425 265" class="arr-err" />
  <path d="M 535 265 L 550 265" class="arr-ok" />

  <!-- Conclusion basse -->
  <g transform="translate(100, 490)">
    <rect width="760" height="50" class="bg" stroke="#cbd5e1" stroke-width="1" rx="8" />
    <text x="380" y="30" text-anchor="middle" class="txt-bold">« On n'apprend rien sous la menace. On apprend quand on a le droit d'échouer sans être diminué. »</text>
  </g>
</svg>
"""

# SVG 3: La Boite a Bequilles (13 strategies de terrain)
svg3 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 620" width="100%" height="auto" role="img" aria-label="Architecture des 13 bequilles cognitives pour adultes neuroatypiques">
  <defs>
    <style>
      .bg { fill: #f8fafc; }
      .col-box { fill: #ffffff; stroke: #cbd5e1; stroke-width: 1.5; rx: 12px; }
      .col-header { fill: #f1f5f9; rx: 8px; }
      .title { font-family: system-ui, -apple-system, sans-serif; font-size: 18px; font-weight: 700; fill: #0f172a; }
      .header-txt { font-family: system-ui, -apple-system, sans-serif; font-size: 13px; font-weight: 700; fill: #1e293b; letter-spacing: 0.5px; }
      .item-title { font-family: system-ui, -apple-system, sans-serif; font-size: 12px; font-weight: 700; fill: #0369a1; }
      .item-desc { font-family: system-ui, -apple-system, sans-serif; font-size: 11px; fill: #475569; }
      .banner { fill: #eff6ff; stroke: #bfdbfe; stroke-width: 1.5; rx: 10px; }
      .banner-txt { font-family: system-ui, -apple-system, sans-serif; font-size: 13px; font-weight: 600; fill: #1e40af; }
      @media (prefers-color-scheme: dark) {
        .bg { fill: #0f172a; }
        .col-box { fill: #1e293b; stroke: #334155; }
        .col-header { fill: #0f172a; }
        .title { fill: #f8fafc; }
        .header-txt { fill: #f1f5f9; }
        .item-title { fill: #38bdf8; }
        .item-desc { fill: #94a3b8; }
        .banner { fill: #1e293b; stroke: #3b82f6; }
        .banner-txt { fill: #93c5fd; }
      }
    </style>
  </defs>

  <rect width="100%" height="100%" class="bg" rx="14" />

  <text x="480" y="38" text-anchor="middle" class="title">La Boîte à Béquilles : 13 Stratégies Cognitives de Terrain</text>
  <text x="480" y="60" text-anchor="middle" class="item-desc" font-size="13px">L'arsenal pragmatique de l'adulte pour contourner la friction sans s'épuiser</text>

  <!-- Pilier 1 : Corps & Espace -->
  <g transform="translate(30, 85)">
    <rect width="210" height="420" class="col-box" />
    <rect x="8" y="8" width="194" height="36" class="col-header" />
    <text x="105" y="31" text-anchor="middle" class="header-txt">1. CORPS &amp; ESPACE</text>

    <g transform="translate(14, 60)">
      <text x="0" y="14" class="item-title">1. Poste épuré</text>
      <text x="0" y="30" class="item-desc">Plan de travail dégagé.</text>
      <text x="0" y="44" class="item-desc">Nuque et mains calées.</text>
    </g>

    <g transform="translate(14, 130)">
      <text x="0" y="14" class="item-title">2. Zéro parasite</text>
      <text x="0" y="30" class="item-desc">Couper notifications,</text>
      <text x="0" y="44" class="item-desc">bruits de fond et écrans.</text>
    </g>

    <g transform="translate(14, 200)">
      <text x="0" y="14" class="item-title">3. Rituel d'ancrage</text>
      <text x="0" y="30" class="item-desc">Respirer, s'installer,</text>
      <text x="0" y="44" class="item-desc">trouver le calme intérieur.</text>
    </g>

    <g transform="translate(14, 270)">
      <text x="0" y="14" class="item-title">4. Temps long</text>
      <text x="0" y="30" class="item-desc">Répéter le geste sans honte.</text>
      <text x="0" y="44" class="item-desc">Apprivoiser la lenteur.</text>
    </g>
  </g>

  <!-- Pilier 2 : Délestage Mental -->
  <g transform="translate(260, 85)">
    <rect width="210" height="420" class="col-box" />
    <rect x="8" y="8" width="194" height="36" class="col-header" />
    <text x="105" y="31" text-anchor="middle" class="header-txt">2. DÉLESTAGE</text>

    <g transform="translate(14, 60)">
      <text x="0" y="14" class="item-title">5. Micro-étapes</text>
      <text x="0" y="30" class="item-desc">Segmenter l'effort pour</text>
      <text x="0" y="44" class="item-desc">éviter le mur mental.</text>
    </g>

    <g transform="translate(14, 130)">
      <text x="0" y="14" class="item-title">6. Listes immédiates</text>
      <text x="0" y="30" class="item-desc">Pense-bêtes prioritaires.</text>
      <text x="0" y="44" class="item-desc">Vider la mémoire vive.</text>
    </g>

    <g transform="translate(14, 200)">
      <text x="0" y="14" class="item-title">7. Automates &amp; Alarmes</text>
      <text x="0" y="30" class="item-desc">Programmer les rappels</text>
      <text x="0" y="44" class="item-desc">pour ne plus s'angoisser.</text>
    </g>

    <g transform="translate(14, 270)">
      <text x="0" y="14" class="item-title">8. Jeter sur papier</text>
      <text x="0" y="30" class="item-desc">Évacuer les pensées</text>
      <text x="0" y="44" class="item-desc">parasites avant de créer.</text>
    </g>
  </g>

  <!-- Pilier 3 : Méthode & Biologie -->
  <g transform="translate(490, 85)">
    <rect width="210" height="420" class="col-box" />
    <rect x="8" y="8" width="194" height="36" class="col-header" />
    <text x="105" y="31" text-anchor="middle" class="header-txt">3. STRUCTURE</text>

    <g transform="translate(14, 60)">
      <text x="0" y="14" class="item-title">9. Schémas visuels</text>
      <text x="0" y="30" class="item-desc">Traduire l'abstrait en</text>
      <text x="0" y="44" class="item-desc">arborescences et couleurs.</text>
    </g>

    <g transform="translate(14, 130)">
      <text x="0" y="14" class="item-title">10. Relecture différée</text>
      <text x="0" y="30" class="item-desc">Ne jamais relire à chaud</text>
      <text x="0" y="44" class="item-desc">avec les yeux fatigués.</text>
    </g>

    <g transform="translate(14, 200)">
      <text x="0" y="14" class="item-title">11. Carburant physique</text>
      <text x="0" y="30" class="item-desc">Sommeil inviolable,</text>
      <text x="0" y="44" class="item-desc">eau fraîche et aération.</text>
    </g>
  </g>

  <!-- Pilier 4 : Esprit Embrumé -->
  <g transform="translate(720, 85)">
    <rect width="210" height="420" class="col-box" />
    <rect x="8" y="8" width="194" height="36" class="col-header" />
    <text x="105" y="31" text-anchor="middle" class="header-txt">4. RUPTURE</text>

    <g transform="translate(14, 60)">
      <text x="0" y="14" class="item-title">12. Alerte « Brouillard »</text>
      <text x="0" y="30" class="item-desc">Sentir quand le cerveau</text>
      <text x="0" y="44" class="item-desc">refuse d'additionner.</text>
    </g>

    <g transform="translate(14, 150)">
      <text x="0" y="14" class="item-title">13. Savoir dire Stop</text>
      <text x="0" y="30" class="item-desc">Couper net, reporter sans</text>
      <text x="0" y="44" class="item-desc">culpabiliser. Sauvegarder.</text>
    </g>

    <g transform="translate(14, 240)">
      <text x="0" y="14" class="item-title">Bienveillance</text>
      <text x="0" y="30" class="item-desc">Pardonner l'oubli.</text>
      <text x="0" y="44" class="item-desc">Respecter ses limites.</text>
    </g>
  </g>

  <!-- Bandeau synthese inferieur -->
  <g transform="translate(30, 530)">
    <rect width="900" height="60" class="banner" />
    <text x="450" y="35" text-anchor="middle" class="banner-txt">« La béquille n'est pas un aveu de faiblesse : c'est l'intelligence de celui qui veut continuer à marcher. »</text>
  </g>
</svg>
"""

(img_dir / "neuro-schema-1-familles.svg").write_text(svg1, encoding="utf-8")
print("Written neuro-schema-1-familles.svg")

(img_dir / "neuro-schema-2-pedagogie.svg").write_text(svg2, encoding="utf-8")
print("Written neuro-schema-2-pedagogie.svg")

(img_dir / "neuro-schema-3-bequilles.svg").write_text(svg3, encoding="utf-8")
print("Written neuro-schema-3-bequilles.svg")

print("TASK 1 SVG GENERATION COMPLETE")