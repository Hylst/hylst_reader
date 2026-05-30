// js/components/GlobalSettingsModal.jsx
import { Icon } from './Icon.jsx';
import { normalizeBackgroundAnimations } from './Ambience.jsx';

const THEME_KEYS = ['sepia', 'light', 'dark'];

export function GlobalSettingsModal({ settings, onUpdateSettings, onClose }) {
    return (
        <div className="modal-backdrop" onClick={e => e.target === e.currentTarget && onClose()}>
            <div className="modal-content settings-modal">
                <div className="modal-header">
                    <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                        <Icon.Settings />
                        <h3>Paramètres</h3>
                    </div>
                    <button className="btn btn-ghost btn-icon" onClick={onClose}><Icon.X /></button>
                </div>
                <div className="settings-body">
                    <div className="setting-group">
                        <label>Thème</label>
                        <div className="setting-options">
                            {THEME_KEYS.map(t => (
                                <button key={t} className={`btn${settings.theme === t ? ' btn-primary' : ''}`}
                                    onClick={() => onUpdateSettings({ ...settings, theme: t })}>
                                    {t === 'sepia' ? <Icon.Book /> : t === 'light' ? <Icon.Sun /> : <Icon.Moon />}
                                    {t === 'sepia' ? 'Sépia' : t === 'light' ? 'Clair' : 'Sombre'}
                                </button>
                            ))}
                        </div>
                    </div>
                    <div className="setting-group">
                        <label>Animations de fond par thème</label>
                        <div className="theme-animation-grid">
                            {THEME_KEYS.map(t => {
                                const label = t === 'sepia' ? 'Sépia' : t === 'light' ? 'Clair' : 'Sombre';
                                const active = !!normalizeBackgroundAnimations(settings.backgroundAnimations)[t];
                                return (
                                    <div className="theme-animation-item" key={`global-anim-${t}`}>
                                        <span className="theme-animation-label">{label}</span>
                                        <button
                                            className={`btn${active ? ' btn-primary' : ''}`}
                                            onClick={() => onUpdateSettings({
                                                ...settings,
                                                backgroundAnimations: {
                                                    ...normalizeBackgroundAnimations(settings.backgroundAnimations),
                                                    [t]: !active
                                                }
                                            })}
                                        >
                                            {active ? 'Animé' : 'Statique'}
                                        </button>
                                    </div>
                                );
                            })}
                        </div>
                    </div>
                    <div className="setting-group">
                        <label>Taille du texte</label>
                        <div className="setting-options">
                            <button className="btn" onClick={() => onUpdateSettings({ ...settings, fontScale: Math.max(0.7, settings.fontScale - 0.1) })}>A−</button>
                            <span style={{ minWidth: '3rem', textAlign: 'center' }}>{Math.round(settings.fontScale * 100)}%</span>
                            <button className="btn" onClick={() => onUpdateSettings({ ...settings, fontScale: Math.min(1.7, settings.fontScale + 0.1) })}>A+</button>
                        </div>
                    </div>
                    <div className="setting-group">
                        <label>Largeur du texte</label>
                        <div className="setting-options">
                            {['small', 'medium', 'large'].map(w => (
                                <button key={w} className={`btn${settings.contentWidth === w ? ' btn-primary' : ''}`}
                                    onClick={() => onUpdateSettings({ ...settings, contentWidth: w })}>
                                    {w === 'small' ? 'Étroit' : w === 'medium' ? 'Moyen' : 'Large'}
                                </button>
                            ))}
                        </div>
                    </div>
                    <div className="setting-group">
                        <label>Alignement</label>
                        <div className="setting-options">
                            {['left', 'justify'].map(a => (
                                <button key={a} className={`btn${settings.alignment === a ? ' btn-primary' : ''}`}
                                    onClick={() => onUpdateSettings({ ...settings, alignment: a })}>
                                    {a === 'left' ? '⬅ Gauche' : '⬛ Justifié'}
                                </button>
                            ))}
                        </div>
                    </div>
                    <div className="setting-group">
                        <label>Mode Concentration</label>
                        <div className="setting-options">
                            <button className={`btn${settings.focusMode ? ' btn-primary' : ''}`}
                                onClick={() => onUpdateSettings({ ...settings, focusMode: !settings.focusMode })}>
                                <Icon.Eye /> {settings.focusMode ? 'Actif' : 'Inactif'}
                            </button>
                        </div>
                    </div>
                    <div className="setting-group">
                        <label>Indicateurs</label>
                        <div className="setting-options">
                            <button className={`btn${settings.showReadingTime ? ' btn-primary' : ''}`}
                                onClick={() => onUpdateSettings({ ...settings, showReadingTime: !settings.showReadingTime })}>
                                Temps
                            </button>
                            <button className={`btn${settings.showProgressPercent ? ' btn-primary' : ''}`}
                                onClick={() => onUpdateSettings({ ...settings, showProgressPercent: !settings.showProgressPercent })}>
                                % Slider
                            </button>
                        </div>
                    </div>
                    <div className="setting-group">
                        <label>Affichage</label>
                        <div className="setting-options">
                            <button className="btn" onClick={() => {
                                const el = document.documentElement;
                                if (!document.fullscreenElement) {
                                    el.requestFullscreen?.();
                                } else {
                                    document.exitFullscreen?.();
                                }
                            }}>Plein écran</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}
