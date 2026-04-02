#!/usr/bin/env python3
"""Comprehensive broken post_url detector and fixer"""
import re
from pathlib import Path

posts_dir = Path("e:\\Repository\\geeknite.github.io\\_posts")

# Get list of valid posts
valid_slugs = {Path(f).stem for f in posts_dir.glob("*.md")}

# Find all broken references
broken_refs = {}  # slug -> list of files
for filepath in posts_dir.glob("*.md"):
    content = filepath.read_text(encoding="utf-8")
    # Find all post_url tags
    for match in re.finditer(r"{%\-?\s*post_url\s+([^\s%]+)\s*\-?%}", content):
        slug = match.group(1).strip()
        if slug not in valid_slugs:
            if slug not in broken_refs:
                broken_refs[slug] = []
            broken_refs[slug].append(filepath.name)

print(f"Found {len(broken_refs)} unique broken post_url slugs\n")
for slug in sorted(broken_refs.keys()):
    files = broken_refs[slug]
    print(f"  {slug}")
    print(f"    Used in: {', '.join(files[:3])}{' +more' if len(files) > 3 else ''}\n")

# Fix them all by removing the lines
fixed_count = 0
for filepath in posts_dir.glob("*.md"):
    content = filepath.read_text(encoding="utf-8")
    original = content

    for broken_slug in broken_refs.keys():
        pattern = rf"{{\%\-?\s*post_url\s+{re.escape(broken_slug)}\s*\-?%}}"
        # Replace the post_url tag with empty string, clean up line
        content = re.sub(pattern, "", content)

    # Clean up lines that became empty or have orphaned brackets
    lines = content.split("\n")
    cleaned_lines = []
    for line in lines:
        # Remove lines that are just whitespace after removing post_url
        if line.strip() and not line.strip() in ["[]", "[]()", "[]()"]:
            # Remove orphaned [text]() patterns
            line = re.sub(r"\[\s*\]\s*\(\s*\)", "", line)
            line = re.sub(r",\s*\n", "\n", line)  # Remove trailing commas
            if line.strip():
                cleaned_lines.append(line)
            else:
                cleaned_lines.append("")
        elif line.strip() in ["[]", "[]()", "[]()"]:
            cleaned_lines.append("")
        else:
            cleaned_lines.append(line)

    content = "\n".join(cleaned_lines)

    if content != original:
        filepath.write_text(content, encoding="utf-8")
        fixed_count += 1
        print(f"Fixed: {filepath.name}")

print(f"\nTotal files fixed: {fixed_count}")
