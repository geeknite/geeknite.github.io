$ErrorActionPreference = 'Stop'
$files = Get-ChildItem _posts -File -Filter '2026-03-*.md'

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

$stop = @(
    'review','new','sealed','edition','for','the','and','with','from','by','in','on','of','a','an',
    'card','game','board','pack','set','box','deluxe','vintage','classic','official','geeknite'
)

function Get-Tokens([string]$s) {
    $n = $s.ToLowerInvariant()
    $n = $n.Normalize([Text.NormalizationForm]::FormD)
    $sb = New-Object System.Text.StringBuilder
    foreach ($c in $n.ToCharArray()) {
        if ([Globalization.CharUnicodeInfo]::GetUnicodeCategory($c) -ne [Globalization.UnicodeCategory]::NonSpacingMark) {
            [void]$sb.Append($c)
        }
    }
    $n = $sb.ToString() -replace '[^a-z0-9\s-]', ' '
    $tokens = $n -split '[\s-]+' | Where-Object { $_ -and $_.Length -ge 3 -and -not ($stop -contains $_) }
    return $tokens
}

$rows = @()
foreach ($f in $files) {
    $title = Get-Title $f.FullName
    if (-not $title) { continue }
    $slug = $f.BaseName.Substring(11)
    $tok = (Get-Tokens ($title + ' ' + $slug)) | Sort-Object -Unique
    if ($tok.Count -eq 0) { continue }
    $key = ($tok | Select-Object -First 3) -join '-'
    $rows += [pscustomobject]@{ File = $f.Name; Key = $key }
}

$groups = $rows | Group-Object Key | Sort-Object Count -Descending
Write-Host "FILES=$($rows.Count)"
Write-Host "KEY_GROUPS=$($groups.Count)"
Write-Host "KEEP_ESTIMATE=$($groups.Count)"

$groups | Select-Object -First 30 | ForEach-Object {
    Write-Host ("COUNT=" + $_.Count + " KEY=" + $_.Name)
}
