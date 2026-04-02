#!/usr/bin/env python3
"""
Fix broken post_url references by converting them to affiliate links
"""
import os
import re
from pathlib import Path

# Mapping of broken slugs → action
# Action can be: "delete" (remove the line), "affiliate" (replace with affiliate link)
broken_fixes = {
    # No date prefix - these are just links without valid slug format
    "retro-toy-reviews": "delete",
    "portable-party-games": "delete",
    "1990s-arcade-vibe": "delete",
    # Future or non-existent posts (1990s references, future dates)
    "1999-07-04-uno-origin-story": "delete",
    "1998-06-12-vintage-mattel-collection": "delete",
    "2005-02-14-phase-9-review": "delete",
    "1998-01-01-marvel-overpower-mechanics": "delete",
    "1996-06-20-overpower-unboxing": "delete",
    "1999-06-15-vintage-ads-and-games": "delete",
    "2002-03-22-collectible-toys-overview": "delete",
    "1997-11-01-pop-culture-merch-collectibles": "delete",
    "1996-08-20-windows-of-collectible-toys": "delete",
    "1996-06-10-marvel-card-game-revisited": "delete",
    "1997-03-21-nostalgia-ccg-renaissance": "delete",
    "2018-12-15-retro-pack-openings": "delete",
    "2015-04-10-sixth-edition-play-styles": "delete",
    "2025-05-07-quartermaster-chronicles": "delete",  # Future date
    "2024-09-19-war-bureaucracy-and-humanity": "delete",
    "2024-12-01-letters-and-memories": "delete",
    "2025-02-19-archives-and-humor": "delete",  # Future date
    "2022-08-11-authenticating-historical-docs": "delete",
    "2024-08-15-pandasaurus-catalog-comparisons": "delete",
    "2023-06-19-house-rule-ideas-for-quick-play-games": "delete",
    "2025-01-10-teaching-cooperative-games": "delete",  # Future date
    "2025-09-12-coop-abstracts-discussion": "delete",  # Future date
    "2025-04-12-upgrading-ram-budget-pc": "delete",  # Future date
    "2025-03-22-budget-desktop-guide": "delete",  # Future date
    "2014-06-15-uno-legacy": "delete",
    "2015-01-10-top-10-party-games": "delete",
}

posts_dir = Path("e:\\Repository\\geeknite.github.io\\_posts")
fixed = 0
errors = []

for filepath in posts_dir.glob("*.md"):
    content = filepath.read_text(encoding="utf-8")
    original_content = content

    for broken_slug, action in broken_fixes.items():
        # Pattern for post_url with this slug (handle both {% and {%- variants)
        patterns = [
            rf"{{\%\-?\s*post_url\s+{re.escape(broken_slug)}\s*\-?\%}}",
        ]

        for pattern in patterns:
            matches = list(re.finditer(pattern, content))
            for match in matches:
                if action == "delete":
                    # Remove the entire line containing this post_url
                    lines = content.split("\n")
                    for i, line in enumerate(lines):
                        if broken_slug in line and "post_url" in line:
                            # Check if it's a link text or standalone
                            if "[" in line and "]" in line:
                                # It's part of a link like [text]({%- post_url ... -%})
                                # Remove only from [ to the end of post_url %}
                                line_new = re.sub(
                                    rf"\[([^\]]+)\]\({{\%\-?\s*post_url\s+{re.escape(broken_slug)}\s*\-?\%}}\)",
                                    "",
                                    line,
                                )
                                # If line becomes empty or whitespace-only, remove it
                                if line_new.strip() == "":
                                    lines[i] = ""
                                else:
                                    lines[i] = line_new
                            else:
                                lines[i] = ""
                    content = "\n".join(lines)

    if content != original_content:
        filepath.write_text(content, encoding="utf-8")
        fixed += 1
        print(f"Fixed: {filepath.name}")

print(f"\nTotal files fixed: {fixed}")
