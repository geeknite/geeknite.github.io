$ErrorActionPreference = 'Stop'

$clusters = @(
    @{ Name='Codenames Pictures'; Include='codenames-pictures'; PreferredKeep='2026-03-13-codenames-pictures-board-game.md' },
    @{ Name='Codenames'; Include='(^|-)codenames(-|$)'; PreferredKeep='2026-03-13-codenames-board-game.md' },
    @{ Name='Sushi Go'; Include='sushi-go'; PreferredKeep='2026-03-13-sushi-go-card-game.md' },
    @{ Name='Monopoly Deal'; Include='monopoly-deal'; PreferredKeep='2026-03-13-monopoly-deal-card-game.md' },
    @{ Name='Saboteur'; Include='(^|-)saboteur(-|$)'; PreferredKeep='2026-03-13-saboteur-card-game.md' },
    @{ Name='Dixit'; Include='(^|-)dixit(-|$)'; PreferredKeep='2026-03-13-dixit-board-game.md' },
    @{ Name='Bananagrams'; Include='bananagrams'; PreferredKeep='2026-03-13-bananagrams-new-unopened-package.md' },
    @{ Name='Vintage Whitman Animal Rummy'; Include='vintage-whitman-animal-rummy'; PreferredKeep='2026-03-13-vintage-whitman-animal-rummy.md' }
)

function New-RedirectUrl([string]$filename) {
    $datePrefix = $filename.Substring(0, 10)
    $slug = $filename.Substring(11, $filename.Length - 14)
    return "/$($datePrefix.Substring(0,4))/$($datePrefix.Substring(5,2))/$slug/"
}

function Add-Redirect([string]$keepPath, [string]$url) {
    $lines = Get-Content $keepPath -Encoding UTF8
    if ($lines.Count -lt 3 -or $lines[0].Trim() -ne '---') { return $false }
    $end = -1
    for ($i = 1; $i -lt $lines.Count; $i++) { if ($lines[$i].Trim() -eq '---') { $end = $i; break } }
    if ($end -lt 0) { return $false }
    $fm = @($lines[1..($end-1)])
    $body = @(); if ($end + 1 -lt $lines.Count) { $body = @($lines[($end+1)..($lines.Count-1)]) }
    $redirIndex = -1
    for ($i = 0; $i -lt $fm.Count; $i++) { if ($fm[$i] -match '^redirect_from:\s*$') { $redirIndex = $i; break } }
    if ($redirIndex -lt 0) {
        $fm += 'redirect_from:'
        $fm += "  - $url"
    } else {
        $exists = $false
        for ($j = $redirIndex + 1; $j -lt $fm.Count; $j++) {
            if ($fm[$j] -notmatch '^\s*-\s+') { break }
            if ($fm[$j].Trim() -eq "- $url") { $exists = $true; break }
        }
        if (-not $exists) {
            $insertAt = $redirIndex + 1
            while ($insertAt -lt $fm.Count -and $fm[$insertAt] -match '^\s*-\s+') { $insertAt++ }
            if ($insertAt -ge $fm.Count) { $fm += "  - $url" }
            else { $fm = @($fm[0..($insertAt-1)] + "  - $url" + $fm[$insertAt..($fm.Count-1)]) }
        }
    }
    $newContent = @('---') + $fm + @('---') + $body
    Set-Content $keepPath -Value $newContent -Encoding UTF8
    return $true
}

$consolidated = 0
$skipped = 0
Write-Host '=== PHASE 6 GAME CLUSTERS ===' -ForegroundColor Green

foreach ($cluster in $clusters) {
    $all = Get-ChildItem '_posts' -File | Where-Object { $_.Name -like '2026-03-*.md' -and $_.Name -match $cluster.Include } | Sort-Object Name
    if ($all.Count -lt 2) { continue }

    $keep = $all | Where-Object { $_.Name -eq $cluster.PreferredKeep } | Select-Object -First 1
    if (-not $keep) { $keep = $all | Select-Object -First 1 }

    $toDelete = $all | Where-Object { $_.Name -ne $keep.Name }
    Write-Host ("Cluster: " + $cluster.Name + " | keep=" + $keep.Name + " | delete=" + $toDelete.Count)

    foreach ($f in $toDelete) {
        if (Add-Redirect $keep.FullName (New-RedirectUrl $f.Name)) {
            Remove-Item $f.FullName -Force
            $consolidated++
        } else {
            $skipped++
        }
    }
}

Write-Host "CONSOLIDATED=$consolidated" -ForegroundColor Green
Write-Host "SKIPPED=$skipped" -ForegroundColor Yellow
