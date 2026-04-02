$ErrorActionPreference = 'Stop'

$targetMax = 20
$posts = Get-ChildItem _posts -File -Filter '2026-03-*.md' | Sort-Object Name

if ($posts.Count -le $targetMax) {
    Write-Host "ALREADY_WITHIN_LIMIT=$($posts.Count)"
    exit 0
}

$stop = @(
    'review','complete','new','sealed','edition','vintage','classic','game','card','board','pack','set','box',
    'with','for','the','and','of','in','by','from','de','del','la','el','en','y','con','por','para',
    'official','original','special','limited','family','players','player','juego','gioco','cartas','cards'
)

function Get-Slug([string]$name) {
    if ($name -match '^\d{4}-\d{2}-\d{2}-(.+)\.md$') { return $Matches[1] }
    return ''
}

function Get-Key([string]$slug) {
    $tokens = $slug.ToLowerInvariant() -split '-'
    $norm = @()
    foreach ($t in $tokens) {
        if ([string]::IsNullOrWhiteSpace($t)) { continue }
        if ($t -match '^\d+$') { continue }
        if ($t.Length -lt 3) { continue }
        if ($stop -contains $t) { continue }
        $norm += $t
    }
    if ($norm.Count -eq 0) {
        return $slug.ToLowerInvariant()
    }
    return (($norm | Sort-Object -Unique) -join '-')
}

$items = foreach ($p in $posts) {
    $slug = Get-Slug $p.Name
    [pscustomobject]@{
        Name = $p.Name
        Path = $p.FullName
        Slug = $slug
        Key  = Get-Key $slug
    }
}

$groups = $items | Group-Object Key | Sort-Object -Property @{Expression='Count';Descending=$true}, @{Expression='Name';Descending=$false}

# Keep one representative per largest clusters until targetMax
$keep = New-Object System.Collections.Generic.HashSet[string]
foreach ($g in $groups | Select-Object -First $targetMax) {
    $rep = $g.Group | Sort-Object Name | Select-Object -First 1
    [void]$keep.Add($rep.Path)
}

# If still less than targetMax (edge case), top up with earliest remaining
if ($keep.Count -lt $targetMax) {
    $needed = $targetMax - $keep.Count
    $topUp = $items | Where-Object { -not $keep.Contains($_.Path) } | Sort-Object Name | Select-Object -First $needed
    foreach ($t in $topUp) { [void]$keep.Add($t.Path) }
}

$toDelete = $items | Where-Object { -not $keep.Contains($_.Path) }

$deleted = 0
foreach ($d in $toDelete) {
    if (Test-Path $d.Path) {
        Remove-Item $d.Path -Force
        $deleted++
    }
}

$after = (Get-ChildItem _posts -File -Filter '2026-03-*.md' | Measure-Object).Count

Write-Host "BEFORE=$($posts.Count)"
Write-Host "KEPT=$($keep.Count)"
Write-Host "DELETED=$deleted"
Write-Host "AFTER=$after"
