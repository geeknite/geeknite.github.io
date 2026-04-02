import os, re, glob

posts_dir = "_posts"
valid_slugs = set()
for f in glob.glob(os.path.join(posts_dir, "*.md")):
    valid_slugs.add(os.path.basename(f)[:-3])

pattern = re.compile(r"\{%-?\s*post_url\s+(.*?)\s*-?%\}", re.DOTALL)
for fpath in sorted(glob.glob(os.path.join(posts_dir, "*.md"))):
    with open(fpath, "r", encoding="utf-8-sig") as f:
        content = f.read()
    for m in pattern.finditer(content):
        raw = m.group(1)
        slug = raw.strip().replace("\n", " ")
        # Normalize whitespace
        slug = " ".join(slug.split())
        if " " in slug or "%" in slug or slug.endswith(".md"):
            print(f"{os.path.basename(fpath)}: [{repr(slug)}]")
