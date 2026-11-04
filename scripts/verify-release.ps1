#requires -Version 5.1
<#
.SYNOPSIS
    Vérifie une release de La Bibliothèque de Hylst avant et après déploiement.

.DESCRIPTION
    Contrôle localement la compilation JSX et la règle zéro tiret, puis vérifie
    en production le build, le Service Worker, les 9 URL du sitemap, le 301 des
    fiches livres, la CSP et les fichiers sensibles.

.EXAMPLE
    powershell -ExecutionPolicy Bypass -File .\scripts\verify-release.ps1

.EXAMPLE
    powershell -ExecutionPolicy Bypass -File .\scripts\verify-release.ps1 -SkipProd
#>
[CmdletBinding()]
param(
    [string]$BaseUrl = 'https://hylst.fr/books_reader/',
    [switch]$SkipProd
)

$ErrorActionPreference = 'Stop'
$script:failures = 0
$root = Split-Path -Parent $PSScriptRoot
Push-Location $root

function Ok([string]$message) {
    Write-Host "[OK] $message" -ForegroundColor Green
}

function Ko([string]$message) {
    Write-Host "[KO] $message" -ForegroundColor Red
    $script:failures++
}

function Get-HttpCode([string]$url) {
    $result = & curl.exe -sS -o NUL -w '%{http_code}|%{redirect_url}' --max-time 30 $url 2>$null
    if ($LASTEXITCODE -ne 0 -or [string]::IsNullOrWhiteSpace($result)) {
        return [pscustomobject]@{ Code = '000'; Redirect = '' }
    }
    $parts = $result -split '\|', 2
    return [pscustomobject]@{
        Code = $parts[0]
        Redirect = if ($parts.Count -gt 1) { $parts[1] } else { '' }
    }
}

try {
    Write-Host "== Contrôles locaux =="
    & node scripts/build_jsx.js --check
    if ($LASTEXITCODE -ne 0) { Ko 'js/dist désynchronisé' } else { Ok 'JSX compilé à jour' }

    & python scripts/check_dashes.py --root .
    if ($LASTEXITCODE -ne 0) { Ko 'tirets cadratins ou demi-cadratins détectés' } else { Ok 'zéro tiret long' }

    if ($SkipProd) {
        if ($script:failures -gt 0) {
            Write-Host "$($script:failures) échec(s)." -ForegroundColor Red
            exit 1
        }
        Write-Host 'Contrôles locaux terminés.' -ForegroundColor Green
        exit 0
    }

    if (-not $BaseUrl.EndsWith('/')) { $BaseUrl += '/' }
    if (-not (Get-Command curl.exe -ErrorAction SilentlyContinue)) {
        throw 'curl.exe est requis pour les contrôles de redirection.'
    }

    Write-Host "== Contrôles production : $BaseUrl =="
    $cacheBuster = [DateTimeOffset]::UtcNow.ToUnixTimeSeconds()
    $index = Invoke-WebRequest -Uri ($BaseUrl + '?cb=' + $cacheBuster) -UseBasicParsing
    $sw = Invoke-WebRequest -Uri ($BaseUrl + 'sw.js?cb=' + $cacheBuster) -UseBasicParsing
    $sitemap = Invoke-WebRequest -Uri ($BaseUrl + 'sitemap.xml?cb=' + $cacheBuster) -UseBasicParsing

    $indexHash = [regex]::Match($index.Content, '\?v=([a-f0-9]{12})').Groups[1].Value
    $swHash = [regex]::Match($sw.Content, 'hylst-reader-([a-f0-9]{12})').Groups[1].Value
    if ($indexHash -and $swHash -and $indexHash -eq $swHash) {
        Ok "build $indexHash cohérent entre index et Service Worker"
    } else {
        Ko "build incohérent : index=$indexHash, sw=$swHash"
    }

    if ($index.Content -match 'text/babel|vendor/babel\.min\.js|js/(?:dist/)?[^"'']+\.jsx') {
        Ko 'Babel ou une source JSX est encore référencée par l''index'
    } else {
        Ok 'aucune référence Babel ou JSX dans l''index'
    }

    if ($index.Content -match 'Content-Security-Policy') {
        Ok 'CSP présente sur l''index'
    } else {
        Ko 'CSP absente de l''index'
    }

    $sitemapUrls = [regex]::Matches($sitemap.Content, '<loc>([^<]+)</loc>') | ForEach-Object { $_.Groups[1].Value }
    if ($sitemapUrls.Count -eq 0) {
        Ko 'sitemap sans URL'
    } else {
        Ok "$($sitemapUrls.Count) URL dans le sitemap"
    }

    foreach ($url in $sitemapUrls) {
        $result = Get-HttpCode $url
        if ($result.Code -eq '200') {
            Ok "200 $url"
        } else {
            Ko "$($result.Code) $url"
        }
    }

    $bookPages = $sitemapUrls | Where-Object { $_ -match '/livres/[^/]+/$' }
    foreach ($url in $bookPages) {
        $noSlash = $url.TrimEnd('/')
        $result = Get-HttpCode $noSlash
        if ($result.Code -eq '301' -and $result.Redirect -eq $url) {
            Ok "301 $noSlash"
        } else {
            Ko "301 attendu pour $noSlash, obtenu $($result.Code) vers $($result.Redirect)"
        }
    }

    foreach ($url in $sitemapUrls) {
        if ($url -notmatch '/livres/') { continue }
        $page = Invoke-WebRequest -Uri $url -UseBasicParsing
        if ($page.Content -match 'Content-Security-Policy') {
            Ok "CSP fiche $url"
        } else {
            Ko "CSP absente de $url"
        }
    }

    $sensitive = @(
        @{ Path = '.env'; Expected = '403' },
        @{ Path = 'vendor/babel.min.js'; Expected = '404' },
        @{ Path = 'js/components/Icon.jsx'; Expected = '404' }
    )
    foreach ($item in $sensitive) {
        $url = $BaseUrl + $item.Path
        $result = Get-HttpCode $url
        if ($result.Code -eq $item.Expected) {
            Ok "$($item.Expected) $($item.Path)"
        } else {
            Ko "$($result.Code) $($item.Path), attendu $($item.Expected)"
        }
    }

    $appJs = Get-HttpCode ($BaseUrl + 'js/dist/app.js')
    if ($appJs.Code -eq '200') {
        Ok '200 js/dist/app.js'
    } else {
        Ko "$($appJs.Code) js/dist/app.js"
    }
}
finally {
    Pop-Location
}

if ($script:failures -gt 0) {
    Write-Host "$($script:failures) échec(s)." -ForegroundColor Red
    exit 1
}

Write-Host 'Toutes les vérifications sont passées.' -ForegroundColor Green
