$ErrorActionPreference = 'Stop'

$clusters = @(
    @{ 
        Name = 'Exploding Kittens Original'
        Keep = '2026-03-13-exploding-kittens-original-edition-card-game.md'
        Include = 'exploding-kittens'
        Exclude = 'party-pack'
    },
    @{ 
        Name = 'Exploding Kittens Party Pack'
        Keep = '2026-03-13-exploding-kittens-party-pack-card-game.md'
        Include = 'exploding-kittens-party-pack'
        Exclude = ''
    },
    @{ 
        Name = 'The Mind Generic'
        Keep = '2026-03-13-the-mind-card-game-review.md'
        Include = 'the-mind|mind-games|mind-card-game|mind-game'
        Exclude = 'pandasaurus'
    },
    @{ 
        Name = 'Pandasaurus The Mind'
        Keep = '2026-03-13-pandasaurus-games-the-mind-card-game.md'
        Include = 'pandasaurus.*mind'
        Exclude = ''
    },
    @{ 
        Name = 'Cerebria Inside World'
        Keep = '2026-03-19-cerebria-the-inside-world-the-card-game.md'
        Include = 'cerebria.*inside-world|cerebria.*the-inside-world'
        Exclude = ''
    }
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
    for ($i = 1; $i -lt $lines.Count; $i++) {
        if ($lines[$i].Trim() -eq '---') { $end = $i; break }
    }
    if ($end -lt 0) { return $false }

    $fm = @($lines[1..($end-1)])
    $body = @()
    if ($end + 1 -lt $lines.Count) { $body = @($lines[($end+1)..($lines.Count-1)]) }

    $hasRedirect = $false
    $redirIndex = -1
    for ($i = 0; $i -lt $fm.Count; $i++) {
        if ($fm[$i] -match '^redirect_from:\s*$') { $hasRedirect = $true; $redirIndex = $i; break }
    }

    if (-not $hasRedirect) {
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
            if ($insertAt -ge $fm.Count) {
                $fm += "  - $url"
            } else {
                $fm = @($fm[0..($insertAt-1)] + "  - $url" + $fm[$insertAt..($fm.Count-1)])
            }
        }
    }

    $newContent = @('---') + $fm + @('---') + $body
    Set-Content $keepPath -Value $newContent -Encoding UTF8
    return $true
}

$consolidated = 0
$skipped = 0

Write-Host '=== PHASE 5 AUTO CONSOLIDATION ===' -ForegroundColor Green

foreach ($cluster in $clusters) {
    $keepName = $cluster.Keep
    $keepPath = Join-Path '_posts' $keepName
    if (-not (Test-Path $keepPath)) {
        Write-Host "SKIP cluster '$($cluster.Name)': keep not found $keepName" -ForegroundColor Yellow
        continue
    }

    $candidates = Get-ChildItem '_posts' -File | Where-Object {
        $_.Name -like '2026-03-*.md' -and
        $_.Name -match $cluster.Include -and
        ($cluster.Exclude -eq '' -or $_.Name -notmatch $cluster.Exclude)
    } | Sort-Object Name

    $toDelete = $candidates | Where-Object { $_.Name -ne $keepName }
    Write-Host ("Cluster: " + $cluster.Name + " | keep=" + $keepName + " | delete=" + $toDelete.Count)

    foreach ($f in $toDelete) {
        $url = New-RedirectUrl $f.Name
        if (Add-Redirect $keepPath $url) {
            Remove-Item $f.FullName -Force
            $consolidated++
        } else {
            $skipped++
        }
    }
}

Write-Host "CONSOLIDATED=$consolidated" -ForegroundColor Green
Write-Host "SKIPPED=$skipped" -ForegroundColor Yellow
