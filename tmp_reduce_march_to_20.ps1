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
    'gioco','juego','cartas','card','cards','boardgame','board-game','official','original'
)

function Get-SlugFromName([string]$name) {
    if ($name -match '^\d{4}-\d{2}-\d{2}-(.+)\.md$') { return $Matches[1] }
    return ''
}

function Get-Tokens([string]$slug) {
    $tokens = $slug.ToLowerInvariant() -split '-'
    $out = @()
    foreach ($t in $tokens) {
        if ([string]::IsNullOrWhiteSpace($t)) { continue }
        if ($t.Length -lt 3) { continue }
        if ($t -match '^\d+$') { continue }
        if ($stop -contains $t) { continue }
        $out += $t
    }
    return ($out | Sort-Object -Unique)
}

function OverlapScore([string[]]$a, [string[]]$b) {
    if (-not $a -or -not $b) { return 0.0 }
    $ha = @{}; foreach($x in $a){ $ha[$x]=$true }
    $inter = 0
    foreach($y in $b){ if($ha.ContainsKey($y)){ $inter++ } }
    $den = [Math]::Max($a.Count, $b.Count)
    if ($den -eq 0) { return 0.0 }
    return [double]$inter / [double]$den
}

function Get-RedirectUrlFromName([string]$name) {
    if ($name -notmatch '^(\d{4})-(\d{2})-(\d{2})-(.+)\.md$') { return $null }
    return "/$($Matches[1])/$($Matches[2])/$($Matches[4])/"
}

function Ensure-Redirect([string]$targetPath, [string]$url) {
    $raw = Get-Content $targetPath -Raw -Encoding UTF8
    $lines = $raw -split "`r?`n"

    if ($lines.Count -lt 3 -or $lines[0].Trim() -ne '---') { return $false }

    $end = -1
    for ($i = 1; $i -lt $lines.Count; $i++) {
        if ($lines[$i].Trim() -eq '---') { $end = $i; break }
    }
    if ($end -eq -1) { return $false }

    for ($i = 1; $i -lt $end; $i++) {
        if ($lines[$i].Trim() -eq "- $url") { return $true }
    }

    $redirectIdx = -1
    for ($i = 1; $i -lt $end; $i++) {
        if ($lines[$i].Trim() -match '^redirect_from\s*:') { $redirectIdx = $i; break }
    }

    if ($redirectIdx -ge 0) {
        $insertAt = $redirectIdx + 1
        while ($insertAt -lt $end -and $lines[$insertAt].TrimStart().StartsWith('- ')) { $insertAt++ }

        $newLines = @()
        $newLines += $lines[0..($insertAt-1)]
        $newLines += "  - $url"
        $newLines += $lines[$insertAt..($lines.Count-1)]
        Set-Content $targetPath -Value ($newLines -join "`n") -Encoding UTF8
        return $true
    }

    $newLines2 = @()
    $newLines2 += $lines[0..($end-1)]
    $newLines2 += 'redirect_from:'
    $newLines2 += "  - $url"
    $newLines2 += $lines[$end..($lines.Count-1)]
    Set-Content $targetPath -Value ($newLines2 -join "`n") -Encoding UTF8
    return $true
}

# Build dataset
$data = @()
foreach ($p in $posts) {
    $slug = Get-SlugFromName $p.Name
    $tokens = Get-Tokens $slug
    $data += [pscustomobject]@{
        Name = $p.Name
        Path = $p.FullName
        Tokens = $tokens
    }
}

# Seed 20 centroids with most token-rich / distinctive posts
$seeded = $data | Sort-Object { $_.Tokens.Count } -Descending | Select-Object -First $targetMax
$centroids = @()
foreach ($s in $seeded) {
    $centroids += [pscustomobject]@{
        Canonical = $s.Name
        CanonicalPath = $s.Path
        Tokens = $s.Tokens
        Members = New-Object System.Collections.ArrayList
    }
}

# Assign each post to best centroid by overlap
foreach ($row in $data) {
    $bestIdx = 0
    $best = -1.0
    for ($i = 0; $i -lt $centroids.Count; $i++) {
        $score = OverlapScore $row.Tokens $centroids[$i].Tokens
        if ($score -gt $best) {
            $best = $score
            $bestIdx = $i
        }
    }
    [void]$centroids[$bestIdx].Members.Add($row)
}

# Re-select canonical in each centroid as oldest filename (lexicographically earliest date+slug)
for ($i = 0; $i -lt $centroids.Count; $i++) {
    $members = @($centroids[$i].Members)
    if ($members.Count -eq 0) { continue }
    $canon = $members | Sort-Object Name | Select-Object -First 1
    $centroids[$i].Canonical = $canon.Name
    $centroids[$i].CanonicalPath = $canon.Path
}

# Deduplicate same canonical picked by multiple centroids by keeping first and moving members
$byCanon = $centroids | Group-Object Canonical | Where-Object { $_.Count -gt 1 }
foreach ($g in $byCanon) {
    $keepers = $g.Group | Select-Object -First 1
    $others = $g.Group | Select-Object -Skip 1
    foreach ($o in $others) {
        foreach ($m in @($o.Members)) { [void]$keepers.Members.Add($m) }
        $o.Members.Clear()
    }
}

# Keep only active centroids (with members)
$active = $centroids | Where-Object { $_.Members.Count -gt 0 }

# If still > 20 active due to edge cases, keep first 20 and reassign others by overlap
if ($active.Count -gt $targetMax) {
    $keep20 = $active | Sort-Object { $_.Members.Count } -Descending | Select-Object -First $targetMax
    $drop = $active | Where-Object { $keep20 -notcontains $_ }
    foreach ($d in $drop) {
        foreach ($m in @($d.Members)) {
            $bestIdx = 0; $best = -1.0
            for ($i = 0; $i -lt $keep20.Count; $i++) {
                $score = OverlapScore $m.Tokens $keep20[$i].Tokens
                if ($score -gt $best) { $best = $score; $bestIdx = $i }
            }
            [void]$keep20[$bestIdx].Members.Add($m)
        }
    }
    $active = $keep20
}

$deleted = 0
$skipped = 0

# Apply consolidation: for each centroid, delete non-canonical members with redirects
foreach ($c in $active) {
    $canonName = $c.Canonical
    $canonPath = $c.CanonicalPath

    if (-not (Test-Path $canonPath)) { $skipped += $c.Members.Count; continue }

    $members = @($c.Members) | Sort-Object Name
    foreach ($m in $members) {
        if ($m.Name -eq $canonName) { continue }
        if (-not (Test-Path $m.Path)) { $skipped++; continue }

        $url = Get-RedirectUrlFromName $m.Name
        if (-not $url) { $skipped++; continue }

        if (Ensure-Redirect -targetPath $canonPath -url $url) {
            Remove-Item $m.Path -Force
            $deleted++
        } else {
            $skipped++
        }
    }
}

$remaining = (Get-ChildItem _posts -File -Filter '2026-03-*.md').Count

Write-Host "TARGET_MAX=$targetMax"
Write-Host "ACTIVE_CLUSTERS=$($active.Count)"
Write-Host "DELETED=$deleted"
Write-Host "SKIPPED=$skipped"
Write-Host "REMAINING_MONTH_FILES=$remaining"
