import re
import os
import sys

posts_dir = r"e:\Repository\geeknite.github.io\_posts"

# Load all actual post slugs (basenames without .md)
actual_slugs = set()
for fname in os.listdir(posts_dir):
    if fname.endswith(".md"):
        actual_slugs.add(fname[:-3])  # strip .md

# Pattern to match post_url tags
pattern = re.compile(r'\{%-?\s*post_url\s+([^\s%]+)\s*-?%\}')

broken = []

for fname in sorted(os.listdir(posts_dir)):
    if not fname.endswith(".md"):
        continue
    fpath = os.path.join(posts_dir, fname)
    try:
        with open(fpath, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except Exception as e:
        print(f"ERROR reading {fname}: {e}", file=sys.stderr)
        continue

    for lineno, line in enumerate(lines, 1):
        for m in pattern.finditer(line):
            ref = m.group(1).strip()
            if ref not in actual_slugs:
                broken.append((fname, lineno, ref))

print(f"Total posts: {len(actual_slugs)}")
print(f"Broken post_url references: {len(broken)}")
print()
print("FILE | LINE | BROKEN SLUG")
print("-" * 80)
for fname, lineno, ref in broken:
    print(f"{fname} | {lineno} | {ref}")
