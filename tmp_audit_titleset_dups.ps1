$ErrorActionPreference = 'Stop'
$files = Get-ChildItem _posts -File -Filter '2026-03-*.md'
$stop = @('review','new','sealed','edition','for','the','and','with','from','by','in','on','of','a','an')

function Get-Title([string]$path) {
    $inYaml = $false
    foreach ($line in Get-Content $path -Encoding UTF8) {
        if ($line.Trim() -eq '---') {
            if (-not $inYaml) { $inYaml = $true; continue }
            break
        }
        if ($inYaml -and $line -match '^title\s*:\s*(.+)$') {
            return $Matches[1].Trim().Trim('"')
        }
    }
    return ''
}

function Get-BodyLen([string]$path) {
    $raw = Get-Content $path -Raw -Encoding UTF8
    $body = $raw
    if ($raw.StartsWith('---')) {
        $parts = $raw -split "`r?`n---`r?`n", 2
        if ($parts.Count -eq 2) { $body = $parts[1] }
    }
    return $body.Trim().Length
}

function Get-TitleKey([string]$title) {
    $n = $title.ToLowerInvariant()
    $n = $n.Normalize([Text.NormalizationForm]::FormD)
    $sb = New-Object System.Text.StringBuilder
    foreach ($c in $n.ToCharArray()) {
        if ([Globalization.CharUnicodeInfo]::GetUnicodeCategory($c) -ne [Globalization.UnicodeCategory]::NonSpacingMark) {
            [void]$sb.Append($c)
        }
    }
    $n = $sb.ToString() -replace '[^a-z0-9\s]', ' '
    $tokens = $n -split '\s+' | Where-Object { $_ -and $_.Length -ge 2 -and -not ($stop -contains $_) }
    if (-not $tokens) { return '' }
    return (($tokens | Sort-Object -Unique) -join ' ')
}

$rows = @()
foreach ($f in $files) {
    $title = Get-Title $f.FullName
    if ($title) {
        $rows += [pscustomobject]@{
            File  = $f.Name
            Path  = $f.FullName
            Title = $title
            Key   = Get-TitleKey $title
            Len   = Get-BodyLen $f.FullName
        }
    }
}

$groups = $rows | Where-Object { $_.Key.Length -gt 0 } | Group-Object Key | Where-Object { $_.Count -gt 1 } | Sort-Object Count -Descending
$dupFiles = (($groups | Measure-Object Count -Sum).Sum)
if (-not $dupFiles) { $dupFiles = 0 }

Write-Host "TITLE_TOKENSET_GROUPS=$($groups.Count)"
Write-Host "TITLE_TOKENSET_FILES=$dupFiles"

$groups | Select-Object -First 40 | ForEach-Object {
    Write-Host ("COUNT=" + $_.Count + " | KEY=" + $_.Name)
}
