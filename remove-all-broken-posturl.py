#!/usr/bin/env python3
"""
Remove ALL broken post_url references by checking if target posts exist.
"""

import re
from pathlib import Path

print("Scanning all posts for broken post_url references...")

_posts_dir = Path("_posts")
existing_posts = set()

# Build set of existing post slugs
for file in _posts_dir.glob("*.md"):
    # Extract slug: YYYY-MM-DD-slug
    existing_posts.add(file.stem)

print(f"Found {len(existing_posts)} existing posts")

# Now scan all posts for post_url references
total_removed = 0
files_modified = 0

for file in _posts_dir.glob("*.md"):
    try:
        content = file.read_text(encoding="utf-8")
        original = content

        # Find all post_url references
        pattern = r"\{%\s*post_url\s+([^\s%]+)\s*%\}"
        matches = re.findall(pattern, content)

        for slug in set(matches):
            # Clean up slug
            clean_slug = slug.strip().strip("'\"")

            # Check if post exists
            if clean_slug not in existing_posts:
                # Remove this broken reference
                # Pattern 1: [text]({% post_url SLUG %}) -> keep text
                pattern1 = (
                    r"\[([^\]]+)\]\(\{%\s*post_url\s+" + re.escape(slug) + r"\s*%}\)"
                )
                if re.search(pattern1, content):
                    content = re.sub(pattern1, r"\1", content)
                    total_removed += 1
                    print(f"[REMOVED] {file.name}: [link]({{%post_url {slug}%}})")

                # Pattern 2: Standalone {% post_url SLUG %} -> comment out
                pattern2 = r"\{%\s*post_url\s+" + re.escape(slug) + r"\s*%}"
                if re.search(pattern2, content):
                    content = re.sub(pattern2, f"<!-- removed: {slug} -->", content)
                    total_removed += 1
                    print(f"[REMOVED] {file.name}: {{%post_url {slug}%}}")

        if content != original:
            file.write_text(content, encoding="utf-8")
            files_modified += 1

    except Exception as e:
        print(f"[ERROR] {file.name}: {e}")

print(
    f"\n[DONE] Removed {total_removed} broken post_url references from {files_modified} files"
)
