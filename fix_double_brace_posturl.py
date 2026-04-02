"""Fix {{ post_url '...' }} (wrong Liquid syntax) across all _posts/*.md files.
- If slug exists: convert to {% post_url slug %}
- If slug not exists: remove link bracket, keep plain text; or remove standalone occurrence
"""

import os, re, glob

posts_dir = "_posts"
# Build valid slugs set
valid_slugs = set()
for f in glob.glob(os.path.join(posts_dir, "*.md")):
    slug = os.path.basename(f)[:-3]  # remove .md
    valid_slugs.add(slug)


def slug_clean(raw):
    """Remove .md extension if present."""
    s = raw.strip().strip("'\"")
    if s.endswith(".md"):
        s = s[:-3]
    return s


# Pattern: [link text]({{ post_url 'slug' }}) or [text]({{ post_url 'slug' })
# Also: [text]( {{ post_url 'slug' }} )
link_pattern = re.compile(
    r"\[([^\]]+)\]\(\s*(?:\{\{\s*site\.baseurl\s*\}\})?\s*\{\{\s*post_url\s+\'([^\']+)\'\s*\}\}?\s*\)",
    re.DOTALL,
)
# Standalone {{ post_url 'slug' }} not in a link
standalone_pattern = re.compile(r"\{\{\s*post_url\s+\'([^\']+)\'\s*\}\}", re.DOTALL)
# Unquoted {{ post_url slug-slug }} not in a link
unquoted_pattern = re.compile(r"\{\{\s*post_url\s+([\w-]+)\s*\}\}", re.DOTALL)
# Link with unquoted slug [text]({{ post_url slug }})
unquoted_link_pattern = re.compile(
    r"\[([^\]]+)\]\(\s*\{\{\s*post_url\s+([\w-]+)\s*\}\}\s*\)", re.DOTALL
)

total_fixed = 0

for fpath in sorted(glob.glob(os.path.join(posts_dir, "*.md"))):
    with open(fpath, "r", encoding="utf-8-sig") as f:
        content = f.read()

    original = content

    # Fix [text]({{ post_url 'slug' }}) or [text]({{ post_url 'slug' })
    def replace_link(m):
        text = m.group(1)
        slug = slug_clean(m.group(2))
        if slug in valid_slugs:
            return f"[{text}]({{% post_url {slug} %}})"
        else:
            return text  # just keep the link text, remove the broken link

    content = link_pattern.sub(replace_link, content)

    # Fix [text]({{ post_url slug }}) (unquoted)
    def replace_unquoted_link(m):
        text = m.group(1)
        slug = m.group(2).strip()
        if slug in valid_slugs:
            return f"[{text}]({{% post_url {slug} %}})"
        else:
            return text

    content = unquoted_link_pattern.sub(replace_unquoted_link, content)

    # Fix standalone {{ post_url 'slug' }} (not in a link)
    def replace_standalone(m):
        slug = slug_clean(m.group(1))
        if slug in valid_slugs:
            return "{{% post_url {} %}}".format(slug)
        else:
            return ""

    content = standalone_pattern.sub(replace_standalone, content)

    # Fix standalone {{ post_url slug }} (unquoted, not in a link)
    def replace_unquoted(m):
        slug = m.group(1).strip()
        if slug in valid_slugs:
            return "{{% post_url {} %}}".format(slug)
        else:
            return ""

    content = unquoted_pattern.sub(replace_unquoted, content)

    if content != original:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        total_fixed += 1
        print(f"Fixed: {os.path.basename(fpath)}")

print(f"\nTotal files fixed: {total_fixed}")
