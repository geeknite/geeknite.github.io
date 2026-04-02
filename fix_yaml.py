#!/usr/bin/env python3
import os
import re
from pathlib import Path

fixes = [
    (
        "2018-04-12-exploding-kittens-a-card-game-for-those-who-love-kittens-asmodee-2018.md",
        "ttitle: Exploding Kittens: A Card Game For Those Who Love Kittens (Asmodee 2018)",
        'title: "Exploding Kittens: A Card Game For Those Who Love Kittens (Asmodee 2018)"',
    ),
    ("2015-07-01-exploding-kittens-review.md", None, None),  # Special: tab indent fix
    (
        "2025-11-01-mattel-uno-gold-edition-review.md",
        "title: Mattel UNO GOLD Edition: Gioco di Carte - Premium Gold Foil Cards - Nuovo",
        'title: "Mattel UNO GOLD Edition: Gioco di Carte - Premium Gold Foil Cards - Nuovo"',
    ),
    (
        "2025-11-01-zombicide-toxic-city-mall-expansion.md",
        "title: Zombicide: Toxic City Mall Expansion — Geeknite Review",
        'title: "Zombicide: Toxic City Mall Expansion — Geeknite Review"',
    ),
    (
        "2025-11-15-mattel-uno-elite-core-edition-yaya-diaby-yellow-tampa-bay-buccaneer.md",
        "title: Mattel UNO Elite Core Edition: YaYa Diaby Yellow Tampa Bay Buccaneer – 2025 Review",
        'title: "Mattel UNO Elite Core Edition: YaYa Diaby Yellow Tampa Bay Buccaneer – 2025 Review"',
    ),
    (
        "2025-11-15-mattel-uno-gold-edition-card-game-premium-gold-foil-cards-new.md",
        "title: 2025 Mattel UNO GOLD Edition Card Game Review: Premium Gold Foil Cards and a Sparkly Future",
        'title: "2025 Mattel UNO GOLD Edition Card Game Review: Premium Gold Foil Cards and a Sparkly Future"',
    ),
    (
        "2026-03-11-pesas-para-ciclismo.md",
        "title: Pesas para Ciclismo: A Jornada do Peso Extra",
        'title: "Pesas para Ciclismo: A Jornada do Peso Extra"',
    ),
    (
        "2026-03-15-15u-open-frame-server-rack-19-free-standing-wall-mounted.md",
        "ttitle: 15U Open Frame Server Rack: Free Standing or Wall Mounted – The Geeknite Review",
        'title: "15U Open Frame Server Rack: Free Standing or Wall Mounted – The Geeknite Review"',
    ),
    (
        "2026-03-19-hp-desktop-windows-10-pro-240gb-ssd-dual-core-8gb-dvd-rw-desktop-pc-wi-fi.md",
        "title: HP Desktop Windows 10 Pro: 240GB SSD, Dual-Core, 8GB RAM, DVD-RW, Wi-Fi",
        'title: "HP Desktop Windows 10 Pro: 240GB SSD, Dual-Core, 8GB RAM, DVD-RW, Wi-Fi"',
    ),
]

posts_dir = Path("e:\\Repository\\geeknite.github.io\\_posts")
fixed = 0

for info in fixes:
    if info[1] is None:  # Special case for 2015-07-01
        filepath = posts_dir / info[0]
        if filepath.exists():
            content = filepath.read_text(encoding="utf-8")
            # Replace tab indentation with 2 spaces in redirect_from
            content = re.sub(r"redirect_from:\n\t", "redirect_from:\n  ", content)
            filepath.write_text(content, encoding="utf-8")
            fixed += 1
            print(f"Fixed (tabs): {info[0]}")
    else:
        filepath = posts_dir / info[0]
        if filepath.exists():
            content = filepath.read_text(encoding="utf-8")
            old, new = info[1], info[2]
            if old in content:
                content = content.replace(old, new)
                filepath.write_text(content, encoding="utf-8")
                fixed += 1
                print(f"Fixed: {info[0]}")
            else:
                print(f"NOT FOUND pattern in: {info[0]}")

print(f"\nTotal fixed: {fixed}")
