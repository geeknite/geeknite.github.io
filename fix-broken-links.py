#!/usr/bin/env python3
"""
Fix broken post_url references in Jekyll blog posts.
Handles:
- Trailing punctuation in slugs
- .html/.md extensions that should be removed
- Single quotes around slugs
- Legitimate missing posts (replace with generic text or remove)
"""

import csv
import re
from pathlib import Path
from collections import defaultdict

# Read the CSV
broken_links = []
with open("broken-post-urls.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        broken_links.append(row)

# Group by file
files_to_fix = defaultdict(list)
for link in broken_links:
    file_path = link["File"]
    broken_slug = link["Broken Slug"]
    line_num = int(link["Line"])
    files_to_fix[file_path].append((line_num, broken_slug))

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

# Process each file
for file_path, issues in files_to_fix.items():
    full_path = Path(file_path)
    if not full_path.exists():
        print(f"[WARN] File not found: {file_path}")
        continue

    with open(full_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    modified = False
    for line_num, broken_slug in issues:
        # Skip false positives
        if broken_slug in false_positives:
            continue

        if line_num > len(lines):
            continue

        line = lines[line_num - 1]  # Convert to 0-indexed

        # Pattern 1: Remove trailing punctuation
        if (
            broken_slug.endswith(".")
            or broken_slug.endswith(",")
            or broken_slug.endswith(")")
        ):
            clean_slug = broken_slug.rstrip(".,)")
            pattern = r"{%\s*post_url\s+" + re.escape(broken_slug) + r"\s*%}"
            replacement = "{% post_url " + clean_slug + " %}"
            if re.search(pattern, line):
                lines[line_num - 1] = re.sub(pattern, replacement, line)
                modified = True
                print(
                    f"[OK] Fixed punctuation: {broken_slug} -> {clean_slug} in {file_path}:{line_num}"
                )
                continue

        # Pattern 2: Remove .html/.md extensions
        if broken_slug.endswith(".html") or broken_slug.endswith(".md"):
            clean_slug = broken_slug.rsplit(".", 1)[0]
            pattern = r"{%\s*post_url\s+" + re.escape(broken_slug) + r"\s*%}"
            replacement = "{% post_url " + clean_slug + " %}"
            if re.search(pattern, line):
                lines[line_num - 1] = re.sub(pattern, replacement, line)
                modified = True
                print(
                    f"[OK] Fixed extension: {broken_slug} -> {clean_slug} in {file_path}:{line_num}"
                )
                continue

        # Pattern 3: Remove single quotes
        if "'" in broken_slug:
            clean_slug = broken_slug.replace("'", "")
            pattern = (
                r'{%\s*post_url\s+[\'"]?'
                + re.escape(broken_slug.replace("'", ""))
                + r'[\'"]?\s*%}'
            )
            replacement = "{% post_url " + clean_slug + " %}"
            if re.search(pattern, line):
                lines[line_num - 1] = re.sub(pattern, replacement, line)
                modified = True
                print(
                    f"[OK] Fixed quotes: {broken_slug} -> {clean_slug} in {file_path}:{line_num}"
                )
                continue

        # Pattern 4: Legitimate missing posts - remove the entire link
        if re.search(r"{%\s*post_url\s+" + re.escape(broken_slug) + r"\s*%}", line):
            # Remove the entire post_url link, keep the surrounding text
            new_line = re.sub(
                r"\[([^\]]+)\]\({%\s*post_url\s+" + re.escape(broken_slug) + r"\s*%}\)",
                r"\1",
                line,
            )
            if new_line != line:
                lines[line_num - 1] = new_line
                modified = True
                print(
                    f"[OK] Removed broken link: {broken_slug} in {file_path}:{line_num}"
                )
                continue

            # If it's a standalone reference, comment it out
            new_line = line.replace(
                "{% post_url " + broken_slug + " %}",
                "<!-- removed broken link: " + broken_slug + " -->",
            )
            if new_line != line:
                lines[line_num - 1] = new_line
                modified = True
                print(
                    f"[OK] Commented out broken link: {broken_slug} in {file_path}:{line_num}"
                )

    # Write back if modified
    if modified:
        with open(full_path, "w", encoding="utf-8") as f:
            f.writelines(lines)
        print(f"[SAVE] Saved {file_path}\n")

print("\n[DONE] All fixable issues have been processed.")
