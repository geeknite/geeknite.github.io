#!/usr/bin/env python3
"""
fix-broken-post-urls.py - Fix broken post_url references in Jekyll posts.

Scans all _posts/*.md for post_url tags that reference non-existent slugs,
then applies fixes using a combination of known mappings and fuzzy matching.

Usage:
    python scripts/fix-broken-post-urls.py [--dry-run] [--verbose]
"""

import os
import re
import sys
from pathlib import Path
from difflib import SequenceMatcher

# --- Configuration ---
POSTS_DIR = "_posts"
POST_URL_PATTERN = re.compile(r"post_url\s+([\w\-]+)")

# Known fixes: broken_slug -> correct_slug (manually verified)
KNOWN_FIXES = {
    "2025-04-07-cmon-zombicide-prison-outbreak-review": "2014-10-26-Zombicide-Prison-Outbreak-Review",
    "2023-06-15-top-10-racing-board-games": "2023-06-17-top-10-racing-board-games",
    "2023-08-15-marvel-united-multiverse-complete-review": "2023-08-22-marvel-united-multiverse-complete-review",
    "2023-08-15-baldurs-gate-3-review": "2023-08-18-baldurs-gate-3-review",
    "2015-08-01-codenames-board-game-review": "2015-06-15-codenames-board-game-review",
    "2024-03-20-review-heat-pedal-to-the-metal": "2024-03-21-review-heat-pedal-to-the-metal",
    "2024-05-07-samsung-sm951-256gb-nvme-ssd-review": "2024-05-08-samsung-sm951-256gb-nvme-ssd-review",
    "2023-08-15-marvel-united-multiverse-review": "2023-08-22-marvel-united-multiverse-complete-review",
    "2025-08-20-ultimate-tablet-showdown": "2025-08-20-ultimate-tablet-showdown-2025",
    "2025-03-15-marvel-united-multiverse-board-game": "2023-08-22-marvel-united-multiverse-complete-review",
    "2023-06-04-Adventure-Tactics-CoraQuest-Which-Game-Choose-for-young-teens": "2023-06-04-adventure-tactics-coraquest-which-game-choose-for-young-teens",
}


def build_post_index(posts_dir):
    """Build a dict of lowercase_slug -> original_slug for all existing posts."""
    index = {}
    for f in Path(posts_dir).glob("*.md"):
        slug = f.stem  # filename without .md
        index[slug.lower()] = slug
    return index


def extract_post_url_refs(posts_dir):
    """Extract all post_url references and which files contain them."""
    refs = {}  # slug -> list of file paths
    for f in Path(posts_dir).glob("*.md"):
        try:
            content = f.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        for match in POST_URL_PATTERN.finditer(content):
            slug = match.group(1)
            refs.setdefault(slug, []).append(str(f))
    return refs


def fuzzy_match(broken_slug, post_index, threshold=0.55):
    """Find the best matching existing slug using multiple scoring strategies."""
    broken_lower = broken_slug.lower()

    # Extract date and name parts
    broken_date = broken_lower[:10] if len(broken_lower) > 10 else ""
    broken_name = broken_lower[11:] if len(broken_lower) > 11 else broken_lower

    best_match = None
    best_score = 0.0

    for existing_lower, original_slug in post_index.items():
        existing_date = existing_lower[:10] if len(existing_lower) > 10 else ""
        existing_name = (
            existing_lower[11:] if len(existing_lower) > 11 else existing_lower
        )

        # Strategy 1: Exact name match (just wrong date)
        if broken_name == existing_name:
            score = 0.95
            if broken_date[:7] == existing_date[:7]:  # same year-month
                score = 0.98
            if score > best_score:
                best_score = score
                best_match = original_slug
            continue

        # Strategy 2: SequenceMatcher on the name part
        name_ratio = SequenceMatcher(None, broken_name, existing_name).ratio()

        # Strategy 3: Word overlap
        broken_words = set(w for w in broken_name.split("-") if len(w) >= 3)
        existing_words = set(w for w in existing_name.split("-") if len(w) >= 3)
        if broken_words and existing_words:
            overlap = len(broken_words & existing_words)
            union = len(broken_words | existing_words)
            word_ratio = overlap / union if union > 0 else 0
        else:
            word_ratio = 0

        # Combined score
        score = max(name_ratio * 0.7, word_ratio * 0.8)

        # Bonus for date proximity
        if broken_date and existing_date:
            if broken_date[:7] == existing_date[:7]:
                score += 0.1
            elif broken_date[:4] == existing_date[:4]:
                score += 0.05

        if score > best_score:
            best_score = score
            best_match = original_slug

    if best_score >= threshold:
        return best_match, best_score
    return None, 0.0


def fix_file(filepath, old_slug, new_slug, dry_run=False):
    """Replace post_url references in a file."""
    content = Path(filepath).read_text(encoding="utf-8", errors="replace")
    # Replace all occurrences of this specific post_url reference
    new_content = content.replace(f"post_url {old_slug}", f"post_url {new_slug}")
    if content != new_content:
        if not dry_run:
            Path(filepath).write_text(new_content, encoding="utf-8")
        return True
    return False


def main():
    dry_run = "--dry-run" in sys.argv
    verbose = "--verbose" in sys.argv

    # Navigate to repo root
    root = Path(__file__).resolve().parent.parent
    os.chdir(root)

    if dry_run:
        print("=== DRY RUN MODE - no files will be modified ===\n")

    # Build index
    post_index = build_post_index(POSTS_DIR)
    print(f"Indexed {len(post_index)} posts.\n")

    # Find all post_url references
    all_refs = extract_post_url_refs(POSTS_DIR)
    print(
        f"Found {len(all_refs)} unique post_url slugs, {sum(len(v) for v in all_refs.values())} total references.\n"
    )

    # Identify broken ones
    broken_refs = {}
    for slug, files in all_refs.items():
        if slug.lower() not in post_index:
            broken_refs[slug] = files

    if not broken_refs:
        print("No broken post_url references found!")
        return

    print(
        f"Found {len(broken_refs)} broken slug(s) across {sum(len(v) for v in broken_refs.values())} reference(s).\n"
    )

    total_files_fixed = 0
    unresolved = []

    for broken_slug, files in sorted(broken_refs.items(), key=lambda x: -len(x[1])):
        # Try known fixes first
        correct_slug = KNOWN_FIXES.get(broken_slug)
        match_source = "known"

        if not correct_slug:
            # Try fuzzy matching
            correct_slug, score = fuzzy_match(broken_slug, post_index)
            match_source = f"fuzzy ({score:.2f})"

        if not correct_slug:
            unresolved.append((broken_slug, len(files)))
            print(f"  UNRESOLVED: '{broken_slug}' ({len(files)} refs) - no match found")
            continue

        # Verify target exists
        if correct_slug.lower() not in post_index:
            unresolved.append((broken_slug, len(files)))
            print(
                f"  UNRESOLVED: '{broken_slug}' -> '{correct_slug}' but target doesn't exist"
            )
            continue

        print(
            f"  FIX [{match_source}]: '{broken_slug}' -> '{correct_slug}' ({len(files)} files)"
        )

        for filepath in files:
            changed = fix_file(filepath, broken_slug, correct_slug, dry_run=dry_run)
            if changed:
                total_files_fixed += 1
                if verbose:
                    action = "Would fix" if dry_run else "Fixed"
                    print(f"    {action}: {Path(filepath).name}")

    # Summary
    print(f"\n{'=' * 50}")
    print(f"=== Summary ===")
    print(f"Broken slugs found:  {len(broken_refs)}")
    print(f"Files {'to fix' if dry_run else 'fixed'}:  {total_files_fixed}")
    if unresolved:
        print(f"Unresolved:          {len(unresolved)}")
        for slug, count in unresolved:
            print(f"  - {slug} ({count} refs)")
    if dry_run:
        print(
            f"\n(Dry run - no changes were made. Run without --dry-run to apply fixes.)"
        )


if __name__ == "__main__":
    main()
