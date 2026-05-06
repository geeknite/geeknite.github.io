#!/usr/bin/env python3
"""
Remove ALL broken post_url references aggressively.
"""

import csv
import re
from pathlib import Path

# Read the CSV
broken_links = []
with open("broken-post-urls.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        broken_links.append(row)

# False positives to skip
false_positives = {
    "per",
    "tag",
    "references",
    "links",
    "Verweise",
    "See",
    "Related",
    "Check",
}

# Group by file
from collections import defaultdict

files_to_fix = defaultdict(set)
for link in broken_links:
    broken_slug = link["Broken Slug"]
    if broken_slug not in false_positives:
        files_to_fix[link["File"]].add(broken_slug)

# Process each file
count = 0
for file_path, slugs in files_to_fix.items():
    full_path = Path(file_path)
    if not full_path.exists():
        print(f"[SKIP] File not found: {file_path}")
        continue

    with open(full_path, "r", encoding="utf-8") as f:
        content = f.read()

    original = content

    for slug in slugs:
        # Pattern 1: [text]({% post_url SLUG %}) -> just remove the link, keep text
        pattern1 = r"\[([^\]]+)\]\({%\s*post_url\s+" + re.escape(slug) + r"\s*%}\)"
        if re.search(pattern1, content):
            content = re.sub(pattern1, r"\1", content)
            print(f"[OK] Removed markdown link to {slug} in {file_path}")
            count += 1

        # Pattern 2: Standalone {% post_url SLUG %} -> comment it out
        pattern2 = r"{%\s*post_url\s+" + re.escape(slug) + r"\s*%}"
        if re.search(pattern2, content):
            content = re.sub(pattern2, f"<!-- removed: {slug} -->", content)
            print(f"[OK] Commented out {slug} in {file_path}")
            count += 1

    if content != original:
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"[SAVE] {file_path}\n")

print(f"\n[DONE] Removed {count} broken links.")
