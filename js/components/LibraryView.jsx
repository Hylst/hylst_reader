// js/components/LibraryView.jsx
// Dépend de : window.Icon, window.HylstDB

const { useState: useStateLib, useEffect: useEffectLib, useMemo: useMemoLib } = React;

const FUTURE_BOOKS = [
    { id: 'f1', title: "L'Odyssée de l'Énergie", subtitle: "Le Carburant Invisible de l'IA", genre: 'Essai SF', cover: 'covers/cover_odyssee_energie.webp' },
    { id: 'f2', title: "Les Chroniques d'Étheria", subtitle: "Roman d'Heroic Fantasy", genre: 'Fantasy', cover: 'covers/cover_etheria.webp' },
    { id: 'f3', title: 'Scénarios et campagnes pour Nightprowler', subtitle: 'JDR MédFan', genre: 'JDR', cover: 'covers/cover_nightprowler.webp' },
    { id: 'f4', title: 'Recueils de proses et poésies fantasques', subtitle: 'Littérature', genre: 'Poésie', cover: 'covers/cover_proses_poesies.webp' },
    { id: 'f5', title: 'Considérations existentielles', subtitle: 'Réflexions philosophiques', genre: 'Philosophie', cover: 'covers/cover_existentiel.webp' },
    { id: 'f6', title: "Quinte ou Les Harmoniques de l'âme", subtitle: 'Roman', genre: 'Roman', cover: 'covers/cover_quinte.webp' },
    { id: 'f7', title: "L'Autre en moi", subtitle: 'Thriller psychologique', genre: 'Thriller', cover: 'covers/cover_autre_en_moi.webp' },
    { id: 'f8', title: "L'Élu d'Astrakan", subtitle: "Livre dont vous êtes le héros · Fantasy", genre: 'LDVELH', cover: 'covers/cover_astrakan.webp' },
    { id: 'f9', title: '12 Scénarios soirées enquêtes & murder', subtitle: 'Jeu de rôle soirée', genre: 'Jeu', cover: 'covers/cover_murder.webp' },
    { id: 'f10', title: 'Approche de la Neurodiversité', subtitle: "Vision d'un non-professionnel", genre: 'Essai', cover: 'covers/cover_neuro.webp' },
    { id: 'f11', title: 'Essentiels en Mathématiques', subtitle: 'Apprentissage', genre: 'Éducation', cover: 'covers/cover_maths.webp' },
    { id: 'f12', title: 'Essentiels en Physique', subtitle: 'Apprentissage', genre: 'Éducation', cover: 'covers/cover_physique.webp' },
    { id: 'f12b', title: 'Essentiels en Optique', subtitle: 'Apprentissage', genre: 'Éducation', cover: 'covers/cover_optique.webp' },
    { id: 'f13', title: 'Essentiels en Électronique', subtitle: 'Apprentissage', genre: 'Éducation', cover: 'covers/cover_electronique.webp' },
    { id: 'f13b', title: 'Essentiels en Informatique', subtitle: 'Apprentissage', genre: 'Éducation', cover: 'covers/cover_informatique.webp' },
    { id: 'f15', title: 'Algorithm for Love', subtitle: 'Recueil de nouvelles SF', genre: 'Nouvelles', cover: 'covers/cover_algorithm_love.webp' },
    { id: 'f16', title: 'Chroniques de Godefroi', subtitle: 'Livre de règles · JDR Médiéval', genre: 'JDR', cover: 'covers/cover_godefroi.webp' },
    { id: 'f17', title: "Chroniques d'une atrophie programmée", subtitle: 'Roman de Science-Fiction', genre: 'SF', cover: 'covers/cover_atrophie.webp' },
    { id: 'f18', title: 'Nouvelles satiriques alsaciennes', subtitle: 'Humour & terroir alsacien', genre: 'Nouvelles', cover: 'covers/cover_nouvelles_alsaciennes.webp' },
    { id: 'f19', title: "Solutions d'Automatisation par IA", subtitle: 'Guide pratique entreprise', genre: 'Guide', cover: 'covers/cover_automatisation_ia.webp' },
    { id: 'f20', title: "Les Éclats du Corbeau", subtitle: "Livre dont vous êtes le héros · Mystère & Étrange", genre: 'LDVELH', cover: 'covers/cover_eclats_corbeau.webp' },
];

function AnimatedAppTitle({ className = "", style = {} }) {
    const text = "Hylst Books & Reader";
    return (
        <span className={`app-title animated-title ${className}`.trim()} style={style} aria-label={text} title={text}>
            {text.split('').map((char, index) => (
                <span
                    key={index}
                    className="wave-char"
                    style={{ '--char-index': index }}
                    aria-hidden="true"
                >
                    {char}
                </span>
            ))}
        </span>
    );
}

function FutureBookCard({ book, delay = 0 }) {
    const Icon = window.Icon;
    return (
        <div className="book-card future-card" style={{ animationDelay: `${delay}ms` }} title="Bientot disponible" role="img">
            <div className="book-cover-container">
                {book.cover
                    ? <img src={`public/${book.cover}`} alt={book.title} loading="lazy" className="book-cover" />
                    : <div className="future-cover-placeholder"><Icon.Lock /><span>{book.genre}</span></div>
                }
                <div className="future-badge">Bientot</div>
            </div>
            <div className="book-info">
                <div className="book-title">{book.title}</div>
                <div className="book-author">{book.subtitle}</div>
                <div className="book-genre-tag">{book.genre}</div>
            </div>
        </div>
    );
}

function BookCard({ book, onClick, delay = 0 }) {
    const Icon = window.Icon;
    const { getProgress } = window.HylstDB;
    const [coverUrl, setCoverUrl] = useStateLib(null);
    const [progress, setProgress] = useStateLib(null);

    useEffectLib(() => {
        if (book.coverBlob) {
            const url = URL.createObjectURL(book.coverBlob);
            setCoverUrl(url);
            return () => URL.revokeObjectURL(url);
        } else if (book.coverPath) {
            setCoverUrl(`public/${book.coverPath}?t=${Date.now()}`);
        }
    }, [book.coverBlob, book.coverPath]);

    useEffectLib(() => {
        getProgress(book.id).then(p => { if (p) setProgress(p.scrollRatio || 0); });
    }, [book.id]);

    return (
        <div className="book-card" style={{ animationDelay: `${delay}ms` }} onClick={onClick} role="button" tabIndex={0}
            onKeyDown={e => e.key === 'Enter' && onClick()}>
            <div className="book-cover-container">
                {coverUrl
                    ? <img src={coverUrl} alt={book.title} loading="lazy" className="book-cover" />
                    : <span style={{ opacity: 0.4, fontSize: '0.8rem' }}>Pas de couverture</span>
                }
            </div>
            <div className="book-info">
                <div className="book-title">{book.title}</div>
                <div className="book-author">{book.author}</div>
            </div>
            {progress !== null && progress > 0 && (
                <div className="book-progress-bar" title={`${Math.round(progress * 100)}% lu`}>
                    <div className="book-progress-fill" style={{ width: `${progress * 100}%` }} />
                </div>
            )}
        </div>
    );
}

function LibraryView({ books, onImport, onImportDirectory, onOpenBook, settings, onUpdateSettings, lastSession, onResume, onShowAbout, onShowMusic, onShowSettings, currentTrack, isPlaying, isLoop, onTogglePlay, onToggleLoop, onStop }) {
    const Icon = window.Icon;
    const hylstBooks = books.filter(b => !b.isImported);
    const userBooks = books.filter(b => b.isImported);

    return (
        <div style={{ display: 'flex', flexDirection: 'column', height: '100%', minHeight: 0 }} className="view-enter">
            <header className="app-header">
                <AnimatedAppTitle />
                <div className="header-actions">
                    <button className="btn btn-ghost btn-icon" title="À propos" onClick={onShowAbout}>
                        <Icon.Info />
                    </button>
                    <button className="btn btn-ghost btn-icon" title="Paramètres" onClick={onShowSettings}>
                        <Icon.Settings />
                    </button>
                    <button className="btn btn-ghost btn-icon btn-theme-toggle" title="Changer le thème"
                        onClick={() => {
                            const themes = ['sepia', 'light', 'dark'];
                            const next = themes[(themes.indexOf(settings.theme) + 1) % themes.length];
                            onUpdateSettings({ ...settings, theme: next });
                        }}
                    >
                        {settings.theme === 'dark' ? <Icon.Sun /> : settings.theme === 'light' ? <Icon.Moon /> : <Icon.Book />}
                    </button>
                    {currentTrack && (
                        <div className="music-mini-bar" title={currentTrack.title}>
                            <button className="mini-open" onClick={onShowMusic} title="Ouvrir la bibliothèque musicale" type="button">
                                <img src={currentTrack.cover} alt="" className="mini-cover" />
                                <span className="mini-title">{currentTrack.title}</span>
                            </button>
                            <button className="btn btn-ghost btn-icon mini-ctrl" onClick={onTogglePlay} title={isPlaying ? 'Pause' : 'Lecture'}>
                                {isPlaying ? <Icon.Pause /> : <Icon.Play />}
                            </button>
                            <button className={`btn btn-ghost btn-icon mini-ctrl${isLoop ? ' active-loop' : ''}`} onClick={onToggleLoop} title={isLoop ? 'Boucle : active' : 'Boucle : inactive'}>
                                {isLoop ? <Icon.Repeat /> : <Icon.RepeatOff />}
                            </button>
                            <button className="btn btn-ghost btn-icon mini-ctrl" onClick={onStop} title="Arrêter">
                                <Icon.Square />
                            </button>
                            <div className="mini-preview" aria-hidden="true">
                                <div className="mini-preview-cover">
                                    <img src={currentTrack.cover} alt="" />
                                </div>
                                <div className="mini-preview-info">
                                    <div className="mini-preview-title">{currentTrack.title}</div>
                                    <div className="mini-preview-artist">{currentTrack.artist}</div>
                                    <div className="mini-preview-meta">
                                        {currentTrack.year && <span>{currentTrack.year}</span>}
                                        {currentTrack.genre && <span>{currentTrack.genre}</span>}
                                        {currentTrack.bpm && <span>{currentTrack.bpm} BPM</span>}
                                        {currentTrack.duration && <span>{currentTrack.duration}</span>}
                                        {currentTrack.mood && <span>{currentTrack.mood}</span>}
                                    </div>
                                </div>
                            </div>
                        </div>
                    )}
                    <button className={`btn btn-ghost btn-icon${currentTrack ? ' music-active' : ''}`} title="Bibliothèque musicale" onClick={onShowMusic}>
                        <Icon.Music />
                    </button>
                    <button className="btn btn-primary" style={{ gap: '0.4rem', paddingLeft: '0.75rem', paddingRight: '0.9rem', fontSize: '0.82rem' }} onClick={onImport} title="Importer un fichier (TXT, JSON, MD)">
                        <Icon.Plus /> <span className="btn-new-label">Nouveau</span>
                    </button>
                </div>
            </header>
            <main className="library-container">
                {lastSession && (
                    <div className="resume-banner">
                        <div className="resume-banner-icon">
                            <Icon.Book />
                        </div>
                        <div className="resume-banner-content">
                            <span className="resume-banner-label">Continuer la lecture</span>
                            <strong className="resume-banner-title">{lastSession.bookTitle}</strong>
                            <span className="resume-banner-meta">Chapitre {lastSession.chapterIndex + 1}</span>
                        </div>
                        <button className="resume-btn" onClick={() => onResume(lastSession)}>
                            Reprendre <Icon.ArrowRight />
                        </button>
                    </div>
                )}

                <div className="library-section-label">Bibliothèque de Hylst</div>
                <p className="library-section-desc">
                    Oeuvres intégrées &mdash; romans, nouvelles, essais, JDR et poésie de Geoffroy Streit (alias Hylst).
                </p>
                {hylstBooks.length === 0 ? (
                    <div className="empty-state" style={{ padding: '2rem' }}>
                        <p>Aucun livre intégré trouvé.</p>
                    </div>
                ) : (
                    <div className="library-grid">
                        {hylstBooks.map((book, i) => (
                            <BookCard key={book.id} book={book} onClick={() => onOpenBook(book.id)} delay={i * 60} />
                        ))}
                    </div>
                )}

                <div className="library-section-label future-label">
                    À venir &mdash; Contenus en préparation <span className="wip-badge">En cours</span>
                </div>
                <div className="future-intro">
                    <div className="future-block">
                        <p>De mes anciens blogs et sites webs, des tiroirs numériques encombrés qui n'ont reçu d'autres visites que les miennes, j'aurai matière à réunir bon nombre de mes écrits passés en ce lieu, parfois inachevés ou à revoir, rangés dans cette bibliothèque numérique que je travaille à concevoir pour y présenter, ouverts à la consultation libre, mes anciennes nouvelles, récits d'aventures HF et SF, livres dont vous êtes le héros, scénarios et campagnes de jeux de rôles, histoires fantasques, réflexions existentielles, recueils de proses et poésies, analyses pseudo-scientifiques ou plus sérieuses, recherche de sens et vérité, guides pédagogiques, frustrastions &amp; passions, divagations &amp; claivoyances, ... issus des méandres de mon cerveau bancal et de mes idées vagabondes au fil des années.</p>
                    </div>
                    <div className="future-block">
                        <p>Avec le recul &amp; l'expérience, j'aimerais reprendre bon nombre d'entre eux pour les améliorer, corriger ou compléter avant de les partager, mais en aurais-je la motivation continue ? En prendrai-je le temps ? Ne finirais-je pas encore une fois par les laisser choir au fond de mes disques dans l'obscurité, si imparfaits soient-ils ?</p>
                    </div>
                </div>
                <div className="library-grid">
                    {FUTURE_BOOKS.map((fb, i) => (
                        <FutureBookCard key={fb.id} book={fb} delay={i * 40} />
                    ))}
                </div>

                <div className="library-section-label user-library-label">
                    Vos autres lectures
                    <div style={{ display: 'flex', gap: '0.5rem', marginLeft: 'auto' }}>
                        <button className="btn" style={{ fontSize: '0.75rem', padding: '0.25rem 0.6rem' }} onClick={onImport} title="Importer .txt, .md ou .json">
                            <Icon.Plus /> Fichier
                        </button>
                        <button className="btn" style={{ fontSize: '0.75rem', padding: '0.25rem 0.6rem' }} onClick={onImportDirectory} title="Importer un dossier HML complet">
                            <Icon.Upload /> Dossier HML
                        </button>
                    </div>
                </div>
                <p className="library-section-desc">
                    Contenus que vous avez importés &mdash; stockés localement sur votre appareil.
                </p>
                {userBooks.length === 0 ? (
                    <div className="import-zone-container" style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1rem' }}>
                        <div className="import-zone" onClick={onImport}>
                            <Icon.Plus />
                            <p style={{ marginTop: '0.75rem', fontWeight: 500 }}>Importer un fichier</p>
                            <p style={{ fontSize: '0.8rem', marginTop: '0.5rem', opacity: 0.7 }}>JSON, TXT ou Markdown</p>
                        </div>
                        <div className="import-zone" onClick={onImportDirectory}>
                            <Icon.Upload />
                            <p style={{ marginTop: '0.75rem', fontWeight: 500 }}>Importer un dossier</p>
                            <p style={{ fontSize: '0.8rem', marginTop: '0.5rem', opacity: 0.7 }}>Format HML (dossier complet)</p>
                        </div>
                    </div>
                ) : (
                    <div className="library-grid">
                        {userBooks.map((book, i) => (
                            <BookCard key={book.id} book={book} onClick={() => onOpenBook(book.id)} delay={i * 60} />
                        ))}
                    </div>
                )}

            </main>
            <footer className="app-footer">
                <div className="footer-content">
                    <div className="footer-brand">
                        <span className="app-title" style={{ fontSize: '1.1rem' }}>Hylst Books &amp; Reader</span>
                        <span className="footer-wip">En cours de développement</span>
                    </div>
                    <div className="footer-creator">
                        Créé par <strong>Geoffroy Streit</strong> alias <em>Hylst</em>
                        &nbsp;&middot;&nbsp; Artiste &eacute;clectique, développeur bancal, &eacute;crivain &agrave; ses heures
                        &nbsp;&middot;&nbsp;
                        <a href="mailto:geoffroy.streit@gmail.com" className="footer-mail">
                            <Icon.Mail /> geoffroy.streit@gmail.com
                        </a>
                    </div>
                </div>
            </footer>
        </div>
    );
}

window.AnimatedAppTitle = AnimatedAppTitle;
window.LibraryView = LibraryView;
