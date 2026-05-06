#!/usr/bin/env python3
"""
Comprehensive fix for ALL broken post_url links.
This script will process every single broken link from the CSV and remove them all.
"""

import csv
import re
from pathlib import Path
from collections import defaultdict

print("Loading broken links from CSV...")

# Read the CSV
broken_links = []
with open("broken-post-urls.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        broken_links.append(row)

print(f"Found {len(broken_links)} broken link references")

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
    "Check",
    "See",
}

# Group by file and collect all unique slugs per file
files_to_fix = defaultdict(set)
for link in broken_links:
    broken_slug = link["Broken Slug"]
    # Clean up the slug
    broken_slug = broken_slug.strip()
    broken_slug = broken_slug.rstrip(".,)")
    broken_slug = broken_slug.replace(".html", "").replace(".md", "")
    broken_slug = broken_slug.replace("'", "")

    if broken_slug and broken_slug not in false_positives:
        files_to_fix[link["File"]].add(broken_slug)

print(f"Processing {len(files_to_fix)} files...")

# Process each file
total_removed = 0
files_modified = 0

for file_path, slugs in files_to_fix.items():
    full_path = Path(file_path)
    if not full_path.exists():
        print(f"[SKIP] File not found: {file_path}")
        continue

    with open(full_path, "r", encoding="utf-8") as f:
        content = f.read()

    original = content
    removed_in_file = 0

    for slug in slugs:
        # Try multiple patterns to catch all variations

        # Pattern 1: [text]({% post_url SLUG %}) -> keep text only
        pattern1 = r"\[([^\]]+)\]\(\{%\s*post_url\s+" + re.escape(slug) + r"\s*%}\)"
        matches1 = len(re.findall(pattern1, content))
        if matches1 > 0:
            content = re.sub(pattern1, r"\1", content)
            removed_in_file += matches1

        # Pattern 2: Standalone {% post_url SLUG %} -> comment out
        pattern2 = r"\{%\s*post_url\s+" + re.escape(slug) + r"\s*%}"
        matches2 = len(re.findall(pattern2, content))
        if matches2 > 0:
            content = re.sub(pattern2, f"<!-- removed: {slug} -->", content)
            removed_in_file += matches2

        # Pattern 3: With quotes (single or double): [text]({% post_url 'SLUG' %})
        pattern3 = (
            r'\[([^\]]+)\]\(\{%\s*post_url\s+[\'"]' + re.escape(slug) + r'[\'"]\s*%}\)'
        )
        matches3 = len(re.findall(pattern3, content))
        if matches3 > 0:
            content = re.sub(pattern3, r"\1", content)
            removed_in_file += matches3

        # Pattern 4: Liquid variable syntax: {{ post_url 'SLUG' }}
        pattern4 = r'\{\{\s*post_url\s+[\'"]' + re.escape(slug) + r'[\'"]\s*\}\}'
        matches4 = len(re.findall(pattern4, content))
        if matches4 > 0:
            content = re.sub(pattern4, f"<!-- removed: {slug} -->", content)
            removed_in_file += matches4

    if content != original:
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"[OK] Fixed {removed_in_file} links in {file_path}")
        files_modified += 1
        total_removed += removed_in_file

print(f"\n[DONE] Removed {total_removed} broken links from {files_modified} files.")
