#requires -Version 5.1
<#
.SYNOPSIS
    Synchronise Hylst_Reader vers le miroir de production de la plateforme Hylst.

.DESCRIPTION
    Copie uniquement les fichiers runtime (css, js, public, vendor, manifest.json, sw.js)
    dans D:\0CODE\AntiGravity\Cours_Memos\Docker\books_reader.

    L'index.html de production est PRÉSERVÉ : il contient le patch plateforme
    (vendor/, /assets/fonts/fonts.css, canonical). Le script vérifie que ce patch
    est toujours présent et refuse de continuer sinon.

    Le script :
      - vérifie la source et la cible ;
      - refuse un index source ou cible qui pointerait encore vers un CDN ;
      - calcule une empreinte de build et l'injecte dans sw.js et les ?v= de l'index ;
      - met à jour la date du sitemap ;
      - vérifie les empreintes des fichiers copiés ;
      - supprime le .env local du miroir (jamais versionné, inutile au runtime) ;
      - peut committer le dossier books_reader (option -Commit) sans jamais pousser.

.PARAMETER Source
    Racine du projet source. Par défaut : le dossier parent de scripts/.

.PARAMETER Target
    Miroir de production. Par défaut : D:\0CODE\AntiGravity\Cours_Memos\Docker\books_reader

.PARAMETER Commit
    Ajoute books_reader au commit Git de la plateforme. Ne pousse jamais.

.PARAMETER Prune
    Supprime les fichiers runtime de la cible qui n'existent plus dans la source
    (uniquement css/, js/, public/, vendor/). À utiliser après avoir vérifié la liste.

.PARAMETER DryRun
    Affiche les actions sans modifier la cible.

.EXAMPLE
    powershell -ExecutionPolicy Bypass -File .\scripts\sync-to-platform.ps1

.EXAMPLE
    powershell -ExecutionPolicy Bypass -File .\scripts\sync-to-platform.ps1 -Commit
#>
[CmdletBinding()]
param(
    [string]$Source = '',
    [string]$Target = 'D:\0CODE\AntiGravity\Cours_Memos\Docker\books_reader',
    [switch]$Commit,
    [switch]$Prune,
    [switch]$DryRun
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

function Fail([string]$Message) {
    Write-Host "[ERREUR] $Message" -ForegroundColor Red
    exit 1
}

function Info([string]$Message) {
    Write-Host "[INFO] $Message" -ForegroundColor Cyan
}

function Warn([string]$Message) {
    Write-Host "[ATTENTION] $Message" -ForegroundColor Yellow
}

function Ok([string]$Message) {
    Write-Host "[OK] $Message" -ForegroundColor Green
}

function Write-Utf8NoBom([string]$Path, [string]$Content) {
    $encoding = New-Object System.Text.UTF8Encoding($false)
    [System.IO.File]::WriteAllText($Path, $Content, $encoding)
}

function Get-RelativePath([string]$Root, [string]$FullName) {
    return $FullName.Substring($Root.Length).TrimStart('\')
}

if ([string]::IsNullOrWhiteSpace($Source)) {
    $scriptPath = $MyInvocation.MyCommand.Path
    if ([string]::IsNullOrWhiteSpace($scriptPath)) {
        Fail "Impossible de déterminer le chemin du script. Passe -Source explicitement."
    }
    $Source = Split-Path -Parent (Split-Path -Parent $scriptPath)
}

if (-not (Test-Path -LiteralPath $Source)) { Fail "Source introuvable : $Source" }
if (-not (Test-Path -LiteralPath $Target)) { Fail "Cible introuvable : $Target" }

$Source = (Resolve-Path -LiteralPath $Source).Path.TrimEnd('\')
$Target = (Resolve-Path -LiteralPath $Target).Path.TrimEnd('\')
$PlatformRoot = Split-Path -Parent $Target

$SourceIndexPath = Join-Path $Source 'index.html'
$TargetIndexPath = Join-Path $Target 'index.html'
$TargetSwPath = Join-Path $Target 'sw.js'
$TargetSitemapPath = Join-Path $Target 'sitemap.xml'

if (-not (Test-Path -LiteralPath $SourceIndexPath)) { Fail "index.html source manquant : $SourceIndexPath" }
if (-not (Test-Path -LiteralPath $TargetIndexPath)) { Fail "index.html cible manquant : $TargetIndexPath" }
if (-not (Test-Path -LiteralPath (Join-Path $Target 'vendor'))) { Fail "vendor/ cible manquant : $Target" }
if (-not (Test-Path -LiteralPath $TargetSitemapPath)) { Fail "sitemap.xml cible manquant : $TargetSitemapPath" }

Info "Source : $Source"
Info "Cible  : $Target"

# Contrôle typographique : aucun tiret cadratin ou demi-cadratin dans le contenu servi.
$dashScript = Join-Path $Source 'scripts\check_dashes.py'
if (-not (Test-Path -LiteralPath $dashScript)) {
    Fail "scripts/check_dashes.py manquant : contrôle typographique impossible."
}
& python $dashScript --root $Source
if ($LASTEXITCODE -ne 0) {
    Fail "Tirets cadratins ou demi-cadratins détectés dans la source."
}

# ---------------------------------------------------------------------------
# 1. Vérifications préalables (approche pessimiste)
# ---------------------------------------------------------------------------

$sourceIndex = Get-Content -Raw -Encoding UTF8 -LiteralPath $SourceIndexPath
$targetIndex = Get-Content -Raw -Encoding UTF8 -LiteralPath $TargetIndexPath

$cdnPattern = 'https://unpkg\.com|https://cdn\.jsdelivr\.net|https://cdnjs\.cloudflare\.com'
if ($sourceIndex -match $cdnPattern) {
    Fail "L'index source utilise encore un CDN. Aligne-le sur vendor/ avant de synchroniser."
}

$sourceMarkers = @(
    'vendor/react.production.min.js',
    'vendor/react-dom.production.min.js',
    'vendor/babel.min.js',
    'vendor/idb-keyval.js',
    'vendor/jszip.min.js',
    'vendor/epub.min.js',
    'vendor/purify.min.js',
    'js/sanitize.js'
)
foreach ($marker in $sourceMarkers) {
    if ($sourceIndex -notmatch [regex]::Escape($marker)) {
        Fail "L'index source ne référence pas $marker."
    }
}

$targetMarkers = @(
    '<base href="/books_reader/">',
    'href="/assets/fonts/fonts.css"',
    'src="vendor/react.production.min.js"',
    'src="vendor/react-dom.production.min.js"',
    'src="vendor/babel.min.js"',
    'src="vendor/idb-keyval.js"',
    'src="vendor/jszip.min.js"',
    'src="vendor/epub.min.js"',
    'src="vendor/purify.min.js"',
    'src="js/sanitize.js',
    'rel="canonical" href="https://hylst.fr/books_reader/"',
    'data-theme="dark"',
    'id="theme-color-meta"'
)
foreach ($marker in $targetMarkers) {
    if ($targetIndex -notmatch [regex]::Escape($marker)) {
        Fail "L'index de production ne contient pas le marqueur attendu : $marker. Corrige-le avant de synchroniser."
    }
}

# Vérifier que tous les scripts de l'index source sont présents dans l'index cible
$sourceScripts = [regex]::Matches($sourceIndex, 'src="([^"?]+)') | ForEach-Object { $_.Groups[1].Value } | Where-Object { $_ -like 'js/*' -or $_ -like 'vendor/*' }
foreach ($script in $sourceScripts) {
    if ($targetIndex -notmatch [regex]::Escape($script)) {
        Fail "L'index de production ne référence pas le script '$script' présent dans l'index source."
    }
}
if ($targetIndex -match $cdnPattern) {
    Fail "L'index de production contient encore une référence CDN. Corrige-le avant de synchroniser."
}
if ($targetIndex -match 'https://fonts\.googleapis\.com') {
    Fail "L'index de production charge encore Google Fonts. Il doit utiliser /assets/fonts/fonts.css."
}

if (Test-Path -LiteralPath (Join-Path $PlatformRoot '.git')) {
    $remote = & git -C $PlatformRoot remote get-url origin 2>$null
    if ($LASTEXITCODE -ne 0 -or $remote -notmatch 'Hylst/cours_info') {
        Warn "Le dépôt cible ne ressemble pas à Hylst/cours_info : $remote"
    }
} else {
    Warn "Aucun dépôt Git détecté à la racine de la plateforme : $PlatformRoot"
}

# Le .env du miroir ne doit pas rester dans un dossier servi par Nginx.
$targetEnv = Join-Path $Target '.env'
if (Test-Path -LiteralPath $targetEnv) {
    if ($DryRun) {
        Warn "DryRun : le .env du miroir serait supprimé : $targetEnv"
    } else {
        Remove-Item -LiteralPath $targetEnv -Force
        Warn "Supprimé : .env du miroir de déploiement (les clés restent dans le .env source, non versionné)."
    }
}

# ---------------------------------------------------------------------------
# 2. Calcul de l'empreinte de build
# ---------------------------------------------------------------------------

$runtimeDirs = @('css', 'js', 'public', 'vendor')
$runtimeFiles = @('manifest.json', 'sw.js')

$hashFiles = New-Object System.Collections.Generic.List[System.IO.FileInfo]
$hashFiles.Add((Get-Item -LiteralPath $SourceIndexPath))
$hashFiles.Add((Get-Item -LiteralPath (Join-Path $Source 'manifest.json')))
foreach ($dir in $runtimeDirs) {
    $srcDir = Join-Path $Source $dir
    if (-not (Test-Path -LiteralPath $srcDir)) { Fail "Dossier source manquant : $srcDir" }
    Get-ChildItem -LiteralPath $srcDir -Recurse -File -Force | ForEach-Object { $hashFiles.Add($_) }
}

$hashLines = $hashFiles |
    Sort-Object FullName |
    ForEach-Object {
        $relative = Get-RelativePath $Source $_.FullName
        $hash = (Get-FileHash -LiteralPath $_.FullName -Algorithm SHA256).Hash.ToLower()
        "$relative=$hash"
    }

$joined = $hashLines -join "`n"
$sha256 = [System.Security.Cryptography.SHA256]::Create()
$buildHash = ([BitConverter]::ToString($sha256.ComputeHash([System.Text.Encoding]::UTF8.GetBytes($joined)))).Replace('-', '').Substring(0, 12).ToLower()

Info "Empreinte de build : $buildHash"

# ---------------------------------------------------------------------------
# 3. Copie des fichiers runtime
# ---------------------------------------------------------------------------

foreach ($dir in $runtimeDirs) {
    $srcDir = Join-Path $Source $dir
    $dstDir = Join-Path $Target $dir
    if (-not (Test-Path -LiteralPath $dstDir)) {
        if (-not $DryRun) { New-Item -ItemType Directory -Path $dstDir -Force | Out-Null }
    }
    if ($DryRun) {
        Info "DryRun : copie de $dir/ vers $dstDir"
    } else {
        Get-ChildItem -LiteralPath $srcDir -Force | ForEach-Object {
            Copy-Item -LiteralPath $_.FullName -Destination $dstDir -Recurse -Force
        }
    }
}

foreach ($file in $runtimeFiles) {
    $srcFile = Join-Path $Source $file
    $dstFile = Join-Path $Target $file
    if ($DryRun) {
        Info "DryRun : copie de $file"
    } else {
        Copy-Item -LiteralPath $srcFile -Destination $dstFile -Force
    }
}

if (-not $DryRun) {
    # Nettoyage des fichiers orphelins dans public/books
    $targetBooksDir = Join-Path $Target 'public\books'
    $sourceBooksDir = Join-Path $Source 'public\books'
    if (Test-Path -LiteralPath $targetBooksDir) {
        Get-ChildItem -LiteralPath $targetBooksDir -Recurse -File | ForEach-Object {
            $rel = Get-RelativePath $targetBooksDir $_.FullName
            $srcP = Join-Path $sourceBooksDir $rel
            if (-not (Test-Path -LiteralPath $srcP)) {
                Info "Suppression de l'orphelin dans la cible : $rel"
                Remove-Item -LiteralPath $_.FullName -Force
            }
        }
    }

    & python $dashScript --root $Target
    if ($LASTEXITCODE -ne 0) {
        Fail "Tirets cadratins ou demi-cadratins détectés dans la cible."
    }
}

# ---------------------------------------------------------------------------
# 4. Cache-busting : sw.js + index.html
# ---------------------------------------------------------------------------

if (-not $DryRun) {
    $sw = Get-Content -Raw -Encoding UTF8 -LiteralPath $TargetSwPath
    if ($sw -notmatch "const CACHE_NAME = '[^']+';") {
        Fail "Impossible de trouver CACHE_NAME dans $TargetSwPath"
    }
    $sw = [regex]::Replace($sw, "const CACHE_NAME = '[^']+';", "const CACHE_NAME = 'hylst-reader-$buildHash';")
    Write-Utf8NoBom $TargetSwPath $sw

    $newIndex = [regex]::Replace($targetIndex, '(\?v=)[^"''&]+', '${1}' + $buildHash)
    Write-Utf8NoBom $TargetIndexPath $newIndex

    $today = Get-Date -Format 'yyyy-MM-dd'
    $sitemap = Get-Content -Raw -Encoding UTF8 -LiteralPath $TargetSitemapPath
    $sitemap = [regex]::Replace($sitemap, '<lastmod>[^<]+</lastmod>', "<lastmod>$today</lastmod>")
    Write-Utf8NoBom $TargetSitemapPath $sitemap
}

# ---------------------------------------------------------------------------
# 5. Vérifications post-copie
# ---------------------------------------------------------------------------

if (-not $DryRun) {
    $checked = 0
    foreach ($file in $hashFiles) {
        $relative = Get-RelativePath $Source $file.FullName
        if ($relative -eq 'index.html') { continue }

        $dstFile = Join-Path $Target $relative
        if (-not (Test-Path -LiteralPath $dstFile)) {
            Fail "Fichier manquant dans la cible : $relative"
        }

        $srcHash = (Get-FileHash -LiteralPath $file.FullName -Algorithm SHA256).Hash
        $dstHash = (Get-FileHash -LiteralPath $dstFile -Algorithm SHA256).Hash
        if ($srcHash -ne $dstHash) {
            Fail "Empreinte différente : $relative"
        }
        $checked++
    }
    Ok "$checked fichiers runtime vérifiés (hors index.html et sw.js)."

    $afterIndex = Get-Content -Raw -Encoding UTF8 -LiteralPath $TargetIndexPath
    if ($afterIndex -notmatch [regex]::Escape("?v=$buildHash")) {
        Fail "L'index de production n'a pas été cache-busté avec $buildHash."
    }
    if ($afterIndex -match $cdnPattern -or $afterIndex -match 'https://fonts\.googleapis\.com') {
        Fail "L'index de production contient encore une dépendance externe."
    }

    $afterSw = Get-Content -Raw -Encoding UTF8 -LiteralPath $TargetSwPath
    if ($afterSw -notmatch "hylst-reader-$buildHash") {
        Fail "Le cache du Service Worker n'a pas été mis à jour."
    }
    Ok "Cache Service Worker : hylst-reader-$buildHash"
    Ok "Index production : ?v=$buildHash"
}

# ---------------------------------------------------------------------------
# 6. Fichiers runtime obsolètes (option -Prune)
# ---------------------------------------------------------------------------

$sourceRelativeSet = @{}
foreach ($file in $hashFiles) {
    $sourceRelativeSet[(Get-RelativePath $Source $file.FullName)] = $true
}

$extraFiles = New-Object System.Collections.Generic.List[string]
foreach ($dir in $runtimeDirs) {
    $dstDir = Join-Path $Target $dir
    if (-not (Test-Path -LiteralPath $dstDir)) { continue }
    Get-ChildItem -LiteralPath $dstDir -Recurse -File -Force | ForEach-Object {
        $relative = Get-RelativePath $Target $_.FullName
        if (-not $sourceRelativeSet.ContainsKey($relative)) {
            $extraFiles.Add($relative)
        }
    }
}

if ($extraFiles.Count -gt 0) {
    if ($Prune) {
        foreach ($relative in $extraFiles) {
            $full = Join-Path $Target $relative
            if ($DryRun) {
                Warn "DryRun : suppression de $relative"
            } else {
                Remove-Item -LiteralPath $full -Force
                Warn "Supprimé (obsolète) : $relative"
            }
        }
    } else {
        Warn "Fichiers runtime présents dans la cible mais absents de la source :"
        $extraFiles | Sort-Object | ForEach-Object { Write-Host "  - $_" -ForegroundColor Yellow }
        Warn "Relance avec -Prune pour les supprimer, après vérification."
    }
}

# ---------------------------------------------------------------------------
# 7. Commit local optionnel (jamais de push)
# ---------------------------------------------------------------------------

if ($Commit) {
    if ($DryRun) {
        Info "DryRun : commit ignoré."
    } else {
        $status = & git -C $PlatformRoot status --short -- books_reader
        if ($LASTEXITCODE -ne 0) { Fail "git status a échoué dans $PlatformRoot" }

        if (-not $status) {
            Warn "Aucun changement dans books_reader : rien à committer."
        } else {
            Info "Changements à committer :"
            $status | ForEach-Object { Write-Host "  $_" }
            & git -C $PlatformRoot add books_reader
            if ($LASTEXITCODE -ne 0) { Fail "git add a échoué." }
            & git -C $PlatformRoot commit -m "Resync books_reader build $buildHash"
            if ($LASTEXITCODE -ne 0) { Fail "git commit a échoué." }
            Ok "Commit local créé. Aucun push effectué."
            Info "Vérifie puis pousse avec : git -C `"$PlatformRoot`" push origin main"
        }
    }
}

Ok "Synchronisation terminée. Build : $buildHash"
Info "Prochaine étape : tester https://hylst.fr/books_reader/ après le déploiement Coolify."
