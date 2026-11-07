// js/components/AboutModal.jsx
// Dépend de : window.Icon

const { useState: useStateAbout, useRef: useRefAbout } = React;

function AboutModal({ onClose }) {
    const [activeTab, setActiveTab] = useStateAbout('about');
    const Icon = window.Icon;
    const modalRef = useRefAbout(null);

    window.useModalA11y(onClose, modalRef);

    const tabs = [
        { id: 'about', label: 'À propos', icon: <Icon.Info /> },
        { id: 'features', label: 'Fonctions', icon: <Icon.Zap /> },
        { id: 'creator', label: 'Créateur', icon: <Icon.User /> },
        { id: 'tips', label: 'Astuces', icon: <Icon.Help /> },
        { id: 'rights', label: 'Droits', icon: <Icon.Shield /> },
    ];

    return (
        <div className="modal-backdrop" onClick={e => e.target === e.currentTarget && onClose()}>
            <div className="modal-content about-modal-v2" ref={modalRef} role="dialog" aria-modal="true" aria-label="À propos de La Bibliothèque de Hylst">
                <div className="about-modal-glass-header">
                    <div className="about-modal-topbar">
                        <div className="about-header-title">
                            <div className="about-logo">H</div>
                            <div>
                                <h3>La Bibliothèque de Hylst</h3>
                                <span className="about-version">Version 1.8.21 &middot; 2026</span>
                            </div>
                        </div>
                        <button className="btn btn-ghost btn-icon" onClick={onClose} aria-label="Fermer" title="Fermer"><Icon.X /></button>
                    </div>
                </div>

                <div className="about-tabs">
                    {tabs.map(tab => (
                        <button
                            key={tab.id}
                            className={`about-tab-btn ${activeTab === tab.id ? 'active' : ''}`}
                            onClick={() => setActiveTab(tab.id)}
                        >
                            {tab.icon}
                            <span>{tab.label}</span>
                        </button>
                    ))}
                </div>

                <div className="about-scroll-content" role="region" aria-label="Contenu de la fenêtre À propos" tabIndex={0}>
                    {activeTab === 'about' && (
                        <div className="about-tab-content animate-fade-in">
                            <p className="about-hero-text">
                                <strong>La Bibliothèque de Hylst</strong> réunit les livres, proses, poésies et récits de Geoffroy Streit. Ce n'est pas un lecteur universel avant tout : c'est un havre numérique intimiste, pensé pour l'immersion littéraire, graphique et sonore, où l'on peut aussi importer ses propres lectures.
                            </p>
                            <div className="about-author-dispatch">
                                <div className="author-note-header-line">
                                    <span className="author-wax-seal-mini">GS</span>
                                    <span className="author-note-kicker">Mot de l'auteur &middot; Geoffroy Streit</span>
                                </div>
                                <p style={{ fontStyle: 'italic', marginBottom: '0.75rem', lineHeight: 1.75 }}>
                                    &laquo; De mes anciens blogs et sites web, ces tiroirs numériques encombrés qui n'ont jamais reçu d'autre visite que la mienne (et encore, les jours de courage), j'aurai de quoi remplir ce lieu : mes écrits d'hier, parfois inachevés, souvent à revoir, sagement alignés dans cette bibliothèque numérique que je m'acharne à bâtir pour les offrir, libres de consultation, à qui voudra bien s'y perdre... &raquo;
                                </p>
                                <p style={{ fontStyle: 'italic', color: 'var(--app-primary)', fontSize: '0.9rem', textAlign: 'right', margin: 0 }}>
                                    En attendant, la porte est ouverte : entrez, et pardonnez la poussière.
                                </p>
                            </div>
                            <div className="about-grid">
                                <div className="about-card">
                                    <Icon.Book />
                                    <h4>La Bibliothèque Légendaire</h4>
                                    <p>Parcourez les écrits de <strong className="highlight-text">Geoffroy Streit</strong> (alias Hylst) : romans ambitieux, nouvelles singulières, poésies mélancoliques, guides techniques et jeux de rôles... Un univers artistique protéiforme, imparfait mais résolument unique, à portée de clic.</p>
                                </div>
                                <div className="about-card">
                                    <Icon.Download />
                                    <h4>Importation Universelle</h4>
                                    <p>Propulsez vos propres récits au cœur de la liseuse ! Importez vos fichiers <code>.EPUB</code>, <code>.TXT</code>, <code>.JSON</code> ou des dossiers d'œuvres complexes. Votre collection vous suit partout, stockée en toute sécurité au sein de votre navigateur.</p>
                                </div>
                                <div className="about-card">
                                    <Icon.Shield />
                                    <h4>Souveraineté Accrue</h4>
                                    <p>Zéro pistage, zéro backend, pas de cloud imposé. Une architecture <strong>"Pure Frontend"</strong> pour préserver votre confidentialité, vous laissant seul maître de vos lectures et de vos données.</p>
                                </div>
                                <div className="about-card">
                                    <Icon.Music />
                                    <h4>Symphonies Immersives</h4>
                                    <p>Plongez dans l'expérience d'une lecture graphique accompagnée de musique ambiante grâce à une musicothèque intégrée de plus de <strong>280 titres</strong> ! La majorité de ces ambiances sonores ont été composées et co-produites (avec l'assistance minutieuse de l'IA par Hylst) pour augmenter les émotions de vos lectures.</p>
                                </div>
                                <div className="about-card">
                                    <Icon.Shield />
                                    <h4>Des améliorations prévues</h4>
                                    <p>- <strong>Personnalisation :</strong> À chaque écrit proposé, une sélection de musiques d'ambiances adéquates, mais aussi un environnement graphique spécifique.<br />- Mes écrits que j'importerai et activerai progressivement.<br />- Correction de coquilles &amp; bugs, améliorations UX/UI progressives...</p>
                                </div>
                            </div>
                        </div>
                    )}

                    {activeTab === 'features' && (
                        <div className="about-tab-content animate-fade-in">
                            <h4>Une plateforme conçue pour l'évasion</h4>
                            <div className="features-list">
                                <div className="feature-item">
                                    <div className="feature-icon"><Icon.Type /></div>
                                    <div className="feature-details">
                                        <strong>Typographie Noble &amp; Confort</strong>
                                        <p>L'interface sublime le texte en utilisant des polices à empattements organiques telles que <em>Cormorant Garamond</em> et <em>Libre Baskerville</em>, garantissant une lisibilité optimale digne des ouvrages imprimés traditionnels.</p>
                                    </div>
                                </div>
                                <div className="feature-item">
                                    <div className="feature-icon"><Icon.Moon /></div>
                                    <div className="feature-details">
                                        <strong>Thèmes Adaptatifs Magiques</strong>
                                        <p>Alternez entre les modes <strong>Sépia</strong>, <strong>Clair</strong> et <strong>Sombre</strong>. Égayez votre lecture avec des animations ambiantes (particules) subtiles. La taille des polices, l'alignement et les gouttières sont finement paramétrables.</p>
                                    </div>
                                </div>
                                <div className="feature-item">
                                    <div className="feature-icon"><Icon.Cpu /></div>
                                    <div className="feature-details">
                                        <strong>Technologie PWA "Offline First"</strong>
                                        <p>Votre bibliothèque ne craint pas les coupures réseau. En installant l'application sur votre appareil (PC, Tablette, Smartphone), le Service Worker sauvegarde vos lectures. Lisez n'importe où, même au fin fond d'une forêt sans connexion internet.</p>
                                    </div>
                                </div>
                                <div className="feature-item">
                                    <div className="feature-icon"><Icon.Music /></div>
                                    <div className="feature-details">
                                        <strong>Lecteur Audio Intégré "Gapless"</strong>
                                        <p>Un baladeur minimaliste avec contrôles avancés pour vous accompagner : lecture aléatoire, mode boucle (sur une piste ou toute la bibliothèque) et mini-player flottant persistant lors du changement de chapitre.</p>
                                    </div>
                                </div>
                                <div className="feature-item">
                                    <div className="feature-icon"><Icon.BookmarkFilled /></div>
                                    <div className="feature-details">
                                        <strong>Mémoire et Signets Intelligents</strong>
                                        <p>Ne perdez jamais le fil. L'application mémorise discrètement votre progression en temps réel pour l'autofocus, et vous permet d'épingler manuellement vos chapitres favoris via le système de <strong>Signets</strong>. La page d'accueil vous proposera instantanément de <em>Continuer la lecture</em> à partir de votre dernier signet.</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    )}

                    {activeTab === 'creator' && (
                        <div className="about-tab-content animate-fade-in">
                            <div className="creator-profile">
                                <div className="creator-header">
                                    <div className="creator-avatar-large">G</div>
                                    <div className="creator-info">
                                        <h4>Geoffroy Streit</h4>
                                        <p className="creator-titles">Écrivain · Compositeur · Développeur</p>
                                    </div>
                                </div>
                                <p className="creator-bio">
                                    Au cœur de ce projet se trouve une volonté d'offrir un cadre à la hauteur des récits.
                                    Écrivain occasionnel et créateur de musiques d'ambiances, Geoffroy Streit (Hylst) a conçu ce lecteur personnalisé pour que la musique
                                    et les mots s'entremêlent harmonieusement.
                                </p>
                                <div className="creator-links">
                                    <a href="https://hylst.fr" target="_blank" rel="noopener noreferrer" className="creator-link-btn" title="Site web Hylst">
                                        <Icon.Globe /> <span>Visiter mon site hylst.fr</span>
                                    </a>
                                    <a href="https://hylst.bandcamp.com/" target="_blank" rel="noopener noreferrer" className="creator-link-btn" title="Bandcamp">
                                        <Icon.Music /> <span>Musiques composées (sans IA) (Bandcamp)</span>
                                    </a>
                                    <a href="https://soundcloud.com/hhhylst" target="_blank" rel="noopener noreferrer" className="creator-link-btn" title="Soundcloud">
                                        <Icon.Headphones /> <span>Musiques composées (sans IA) (SoundCloud)</span>
                                    </a>
                                    <a href="https://www.wattpad.com/user/GeoffroyStreit" target="_blank" rel="noopener noreferrer" className="creator-link-btn" title="Wattpad">
                                        <Icon.Book /> <span>Anciennes proses et poésies (sans IA) (Wattpad)</span>
                                    </a>
                                    <a href="https://www.deviantart.com/hhylst" target="_blank" rel="noopener noreferrer" className="creator-link-btn" title="DeviantArt">
                                        <Icon.Image /> <span>Dessins, Pixel Art &amp; Digital Painting (sans IA) (DeviantArt)</span>
                                    </a>
                                    <a href="https://www.youtube.com/@HyLsT16" target="_blank" rel="noopener noreferrer" className="creator-link-btn" title="YouTube">
                                        <Icon.Youtube /> <span>Vidéos &amp; Clips (sans IA sauf mention) (YouTube)</span>
                                    </a>
                                    <a href="https://demozoo.org/sceners/2341/" target="_blank" rel="noopener noreferrer" className="creator-link-btn" title="Demozoo">
                                        <Icon.Cpu /> <span>Contributions Demoscene &middot; code, musique, gfx (Demozoo)</span>
                                    </a>
                                    <a href="mailto:geoffroy.streit@gmail.com" className="creator-link-btn" title="Email">
                                        <Icon.Mail /> <span>Me contacter</span>
                                    </a>
                                </div>
                            </div>
                        </div>
                    )}

                    {activeTab === 'tips' && (
                        <div className="about-tab-content animate-fade-in">
                            <div className="tips-grid">
                                <div className="tip-box">
                                    <h4><Icon.Zap /> Raccourcis Clavier</h4>
                                    <ul>
                                        <li><code>Espace</code> ou <code>Page Down</code> : Défilement fluide vers le bas d'environ 80% de la hauteur de l'écran.</li>
                                        <li><code>Flèche Droite</code> / <code>Gauche</code> : Navigation rapide entre les chapitres d'un livre.</li>
                                        <li><code>Touche Début</code> / <code>Fin</code> : Aller directement tout en haut ou tout en bas de la page.</li>
                                        <li><code>Échap</code> : Ferme les barres latérales et modales.</li>
                                        <li><code>Ctrl + F</code> : Utilisez la recherche native du navigateur.</li>
                                    </ul>
                                </div>
                                <div className="tip-box">
                                    <h4><Icon.Mouse /> Tactile, Stylus &amp; Souris</h4>
                                    <ul>
                                        <li><strong>Geste (Swipe) Latéral</strong> : Sur mobile, glissez vers la gauche ou la droite pour tourner les pages virtuelles.</li>
                                        <li><strong>Double Tap (ou Clic)</strong> n'importe où dans le texte : Fait apparaître ou disparaître toutes les barres d'interfaces (Mode Focus).</li>
                                        <li><strong>Barre de Progression Intelligente</strong> : Un clic n'importe où fait défiler le texte de manière fluide.</li>
                                    </ul>
                                </div>
                                <div className="tip-box full-width">
                                    <h4><Icon.Settings /> Secret &amp; Astuce d'importation avancée</h4>
                                    <p>Vous souhaitez intégrer un tome entier avec sa structure originale ? Vous pouvez glisser-déposer tout le dossier d'un livre (s'il suit l'architecture Hylst HTML), mais pour une expérience sur mesure : assurez-vous de concevoir <strong>un fichier <code>config.json</code> racine</strong>.</p>
                                    <p className="tip-hint">L'application se chargera alors de construire automatiquement l'interface narrative, avec les chapitres ordonnés, la couverture, l'auteur, et le résumé officiel !</p>
                                </div>
                            </div>
                        </div>
                    )}
                    {activeTab === 'rights' && (
                        <div className="about-tab-content animate-fade-in">
                            <p className="about-hero-text" style={{ textAlign: 'left', fontSize: '1rem' }}>
                                Les textes, illustrations et musiques de cette bibliothèque appartiennent à
                                <strong> Geoffroy Streit</strong> et sont protégés par le droit d'auteur.
                                La lecture, la courte citation avec mention du nom et le partage du lien sont
                                autorisés. La reproduction, la réutilisation commerciale et l'entraînement de
                                modèles d'intelligence artificielle ne le sont pas.
                            </p>
                            <div className="rights-summary-grid">
                                <div className="rights-summary-card allowed">
                                    <h4><Icon.Check /> Autorisé</h4>
                                    <ul>
                                        <li>Lire, relire, imprimer pour un usage personnel.</li>
                                        <li>Citer quelques lignes en me nommant.</li>
                                        <li>Partager le lien d'un livre ou d'un texte.</li>
                                    </ul>
                                </div>
                                <div className="rights-summary-card forbidden">
                                    <h4><Icon.X /> Interdit sans accord</h4>
                                    <ul>
                                        <li>Recopier ou republier un texte, même partiellement.</li>
                                        <li>Adapter, traduire, revendre, intégrer à une offre payante.</li>
                                        <li>Alimenter un corpus ou entraîner une IA.</li>
                                    </ul>
                                </div>
                            </div>
                            <p className="rights-note">
                                Illustrations : la plupart sont générées ou retouchées avec l'aide d'une IA,
                                sous ma direction. Les photographies et créations personnelles sont signalées.
                            </p>
                            <a className="btn btn-primary rights-page-link" href="droits.html">
                                <Icon.Shield /> Lire la page complète des droits
                            </a>
                        </div>
                    )}
                </div>

                <div className="modal-footer about-footer">
                    <p>La Bibliothèque de Hylst &middot; Livres, proses, poésies et récits de Geoffroy Streit.</p>
                    <button className="btn btn-primary" onClick={onClose}>Commencer la lecture</button>
                </div>
            </div>
        </div>
    );
}

window.AboutModal = AboutModal;
