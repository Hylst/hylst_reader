#requires -Version 5.1
<#
.SYNOPSIS
    Exporte les quatre parties de l'etude technique 2001-2002 en PDF.

.DESCRIPTION
    Chaque partie est exportee dans un processus Word separe : c'est la seule
    facon fiable observee sur cette machine, ou une boucle COM sur une meme
    instance Word peut se bloquer apres le premier export.

    Le script parent appelle quatre fois ce meme fichier avec -Part A|B|C|D,
    puis rassemble les metadonnees dans manifest.json.

    Source : D:\0HYLST\0 HYLST ART 2024\ecrits\textes_a_trier\04_ARCHIVES_TECHNIQUES\sources-word
    Sortie : public\books\sciences-et-technologie-jeux-videos\pdf
#>
param(
    [string]$SourceDir = "D:\0HYLST\0 HYLST ART 2024\ecrits\textes_a_trier\04_ARCHIVES_TECHNIQUES\sources-word",
    [string]$OutDir = "",
    [ValidateSet("A", "B", "C", "D")]
    [string]$Part = ""
)

$ErrorActionPreference = "Stop"

$root = Split-Path -Parent $PSScriptRoot
if ([string]::IsNullOrWhiteSpace($OutDir)) {
    $OutDir = [System.IO.Path]::Combine($root, "public\books\sciences-et-technologie-jeux-videos\pdf")
}

$documents = @{
    A = @{ Part = "A"; Source = "etjv-a.docx"; File = "partie-a-introduction-histoire-interfaces-manuelles.pdf" }
    B = @{ Part = "B"; Source = "etjv-b.docx"; File = "partie-b-interfaces-sensori-motrices.pdf" }
    C = @{ Part = "C"; Source = "etjv-c.docx"; File = "partie-c-interfaces-de-visualisation.pdf" }
    D = @{ Part = "D"; Source = "etjv-d.docx"; File = "partie-d-capteurs-autres-systemes.pdf" }
}

if (-not (Test-Path -LiteralPath $OutDir)) {
    New-Item -ItemType Directory -Path $OutDir -Force | Out-Null
}

function Export-One([string]$Key) {
    $item = $documents[$Key]
    $src = [System.IO.Path]::Combine($SourceDir, $item.Source)
    $dest = [System.IO.Path]::Combine($OutDir, $item.File)

    if (-not (Test-Path -LiteralPath $src)) {
        throw "Document source introuvable : $src"
    }
    if (Test-Path -LiteralPath $dest) {
        Remove-Item -LiteralPath $dest -Force
    }

    $word = $null
    try {
        $word = New-Object -ComObject Word.Application
        $word.Visible = $false
        $word.DisplayAlerts = 0
        $word.AutomationSecurity = 3

        $doc = $word.Documents.Open($src, $false, $true)
        try {
            $pages = [int]$doc.ComputeStatistics(2)
            $doc.ExportAsFixedFormat($dest, 17)
        }
        finally {
            $doc.Close($false)
        }
    }
    finally {
        if ($null -ne $word) {
            $word.Quit()
            [System.Runtime.InteropServices.Marshal]::ReleaseComObject($word) | Out-Null
            $word = $null
        }
        [GC]::Collect()
        [GC]::WaitForPendingFinalizers()
    }

    if (-not (Test-Path -LiteralPath $dest)) {
        throw "Export PDF absent : $dest"
    }
    $bytes = (Get-Item -LiteralPath $dest).Length
    if ($pages -le 0) {
        throw "Nombre de pages invalide pour $($item.Source) : $pages"
    }
    if ($bytes -lt 100000) {
        throw "PDF trop leger pour $($item.Source) : $bytes octets"
    }

    $result = [ordered]@{
        part = $item.Part
        file = $item.File
        source = $item.Source
        pages = $pages
        bytes = $bytes
        sha256 = (Get-FileHash -LiteralPath $dest -Algorithm SHA256).Hash.ToLowerInvariant()
    }
    $result | ConvertTo-Json -Depth 4 | Set-Content -LiteralPath ([System.IO.Path]::Combine($OutDir, "part-$Key.json")) -Encoding UTF8
    Write-Host ("OK {0} {1} pages {2} octets" -f $item.File, $pages, $bytes)
}

if (-not [string]::IsNullOrWhiteSpace($Part)) {
    Export-One $Part
    exit 0
}

foreach ($key in @("A", "B", "C", "D")) {
    & powershell.exe -NoProfile -ExecutionPolicy Bypass -File $PSCommandPath -Part $key -SourceDir $SourceDir -OutDir $OutDir
    if ($LASTEXITCODE -ne 0) {
        throw "Echec de l'export de la partie $key (code $LASTEXITCODE)."
    }
}

$manifest = @()
foreach ($key in @("A", "B", "C", "D")) {
    $partPath = [System.IO.Path]::Combine($OutDir, "part-$key.json")
    $manifest += Get-Content -LiteralPath $partPath -Raw | ConvertFrom-Json
    Remove-Item -LiteralPath $partPath -Force
}

$manifestPath = [System.IO.Path]::Combine($OutDir, "manifest.json")
$manifest | ConvertTo-Json -Depth 4 | Set-Content -LiteralPath $manifestPath -Encoding UTF8
Write-Host "Manifeste : $manifestPath"
