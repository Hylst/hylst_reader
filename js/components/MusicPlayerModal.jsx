// js/components/MusicPlayerModal.jsx
// Dépend de : window.Icon, window.MUSIC_LIBRARY

const { useState: useStateMusicModal, useMemo: useMemoMusicModal } = React;

function MusicPlayerModal({ isOpen, onClose, currentTrack, isPlaying, isLoop, onPlayTrack, onTogglePlay, onToggleLoop }) {
    const Icon = window.Icon;
    const MUSIC_LIBRARY = window.MUSIC_LIBRARY;
    const [searchTerm, setSearchTerm] = useStateMusicModal('');

    const filteredTracks = useMemoMusicModal(() => {
        if (!searchTerm) return MUSIC_LIBRARY;
        const low = searchTerm.toLowerCase();
        return MUSIC_LIBRARY.filter(t =>
            t.title.toLowerCase().includes(low) ||
            t.genre.toLowerCase().includes(low) ||
            t.tags.some(tag => tag.toLowerCase().includes(low))
        );
    }, [searchTerm, MUSIC_LIBRARY]);

    if (!isOpen) return null;

    return (
        <div className="modal-backdrop" onClick={e => e.target === e.currentTarget && onClose()}>
            <div className="modal-content music-modal" onClick={e => e.stopPropagation()}>
                <div className="music-modal-glass-header">
                    <div className="music-modal-topbar">
                        <div className="music-modal-brand">
                            <Icon.Music />
                            <h3>Bibliothèque Musicale</h3>
                            <span className="music-track-count">{MUSIC_LIBRARY.length} titres</span>
                        </div>
                        <button className="btn btn-ghost btn-icon" onClick={onClose}><Icon.X /></button>
                    </div>

                    <div className="music-search-bar">
                        <Icon.Search />
                        <input
                            type="text"
                            placeholder="Rechercher une musique, un genre, un mood..."
                            value={searchTerm}
                            onChange={e => setSearchTerm(e.target.value)}
                        />
                        {searchTerm && (
                            <button className="clear-search-btn" onClick={() => setSearchTerm('')}><Icon.X /></button>
                        )}
                    </div>
                </div>

                <div className="music-player-layout">
                    <div className="music-list-side">
                        <div className="music-grid">
                            {filteredTracks.map(track => (
                                <div key={track.id}
                                    className={`music-item ${currentTrack?.id === track.id ? 'active' : ''}`}
                                    onClick={() => onPlayTrack(track)}>
                                    <div className="music-item-cover">
                                        <img src={track.cover} alt={track.title} loading="lazy" />
                                        {currentTrack?.id === track.id && isPlaying && (
                                            <div className="playing-overlay">
                                                <div className="wave-container">
                                                    <div className="wave-bar"></div>
                                                    <div className="wave-bar"></div>
                                                    <div className="wave-bar"></div>
                                                </div>
                                            </div>
                                        )}
                                        {currentTrack?.id === track.id && !isPlaying && (
                                            <div className="playing-overlay paused-overlay">
                                                <Icon.Pause />
                                            </div>
                                        )}
                                    </div>
                                    <div className="music-item-info">
                                        <div className="music-item-title">{track.title}</div>
                                        <div className="music-item-genre">{track.genre}</div>
                                        {track.duration && <div className="music-item-duration">{track.duration}</div>}
                                    </div>
                                </div>
                            ))}
                        </div>
                        {filteredTracks.length === 0 && (
                            <div className="music-empty">Aucun résultat pour « {searchTerm} »</div>
                        )}
                    </div>

                    {currentTrack && (
                        <div className="music-controls-side">
                            <div className="current-track-card">
                                <div className="current-track-cover-container">
                                    <img src={currentTrack.cover} alt={currentTrack.title} className="current-track-cover" />
                                    <div className="cover-overlay-controls">
                                        <button className="cover-control-btn" onClick={onTogglePlay} title={isPlaying ? 'Pause' : 'Lecture'}>
                                            {isPlaying ? <Icon.Pause /> : <Icon.Play />}
                                        </button>
                                    </div>
                                </div>
                                <div className="current-track-details">
                                    <h4>{currentTrack.title}</h4>
                                    <p className="artist">{currentTrack.artist}</p>
                                    <div className="track-meta">
                                        {currentTrack.year && <span className="meta-tag">{currentTrack.year}</span>}
                                        {currentTrack.genre && <span className="meta-tag">{currentTrack.genre}</span>}
                                        {currentTrack.bpm && <span className="meta-tag">{currentTrack.bpm} BPM</span>}
                                        {currentTrack.duration && <span className="meta-tag">⏱ {currentTrack.duration}</span>}
                                        {currentTrack.mood && <span className="meta-tag mood-tag">{currentTrack.mood}</span>}
                                    </div>
                                    {currentTrack.tags && currentTrack.tags.length > 0 && (
                                        <div className="track-tags">
                                            {currentTrack.tags.map(t => <span key={t} className="tag">#{t}</span>)}
                                        </div>
                                    )}
                                </div>
                                <div className="player-controls">
                                    <button className={`control-btn ${isLoop ? 'active' : ''}`} onClick={onToggleLoop} title={isLoop ? 'Boucle active' : 'Boucle inactive'}>
                                        {isLoop ? <Icon.Repeat /> : <Icon.RepeatOff />}
                                    </button>
                                    <button className="control-btn play-btn" onClick={onTogglePlay}>
                                        {isPlaying ? <Icon.Pause /> : <Icon.Play />}
                                    </button>
                                </div>
                            </div>
                        </div>
                    )}
                </div>
            </div>
        </div>
    );
}

window.MusicPlayerModal = MusicPlayerModal;
