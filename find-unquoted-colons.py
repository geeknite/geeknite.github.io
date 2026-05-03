#!/usr/bin/env python3
import re
from pathlib import Path

print("Searching for tags with unquoted colons...")

for file in Path("_posts").glob("*.md"):
    try:
        content = file.read_text(encoding="utf-8")
        # Find tags line
        match = re.search(r"^tags:\s*\[(.*?)\]", content, re.MULTILINE)
        if match:
            tags_str = match.group(1)
            # Check for unquoted colons
            if ":" in tags_str:
                # Split by comma and check each tag
                tags = [t.strip() for t in tags_str.split(",")]
                for tag in tags:
                    if ":" in tag and not (tag.startswith('"') or tag.startswith("'")):
                        print(
                            f"{file}: line {content[:match.start()].count(chr(10))+1}: {tag}"
                        )
                        break
    except Exception as e:
        pass
