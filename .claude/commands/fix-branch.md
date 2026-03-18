# Fix Branch Issues

Auto-fix issues detected by `/validate-branch` on the current branch: $ARGUMENTS

Reads the pending changes against `main`, identifies all fixable errors and warnings (same checks as `/validate-branch`), and applies corrections automatically. Use subagents in parallel to fix multiple posts simultaneously.

## Safety Rules

- **NEVER delete post content** — only fix metadata, add redirects, fix links, and rename files
- **NEVER modify post body content** unless fixing a broken `post_url` reference
- **NEVER change a post's slug** — only date prefixes and frontmatter may change
- **NEVER remove existing `redirect_from:` entries** — only append new ones
- **ALWAYS verify no filename collision** before any rename
- **ALWAYS preserve all existing frontmatter fields** when updating
- **SKIP posts with `redirect_to:`** in frontmatter (redirect stubs, not real posts)
- If `$ARGUMENTS` specifies a filter (e.g., "2026-02", "errors only", a slug), narrow fixes to matching posts
- If `$ARGUMENTS` is empty or "all", fix ALL detected issues

## Process

### Step 1: Gather Branch State (same as validate-branch Step 1)

Run these commands to understand the full scope of changes:

1. `git diff --name-status main...HEAD -- _posts/` — committed changes on this branch vs main
2. `git diff --name-status -- _posts/` — unstaged changes in working tree
3. `git diff --name-status --cached -- _posts/` — staged changes
4. `git status -- _posts/` — overall status summary
5. `git ls-tree main --name-only -- _posts/` — full list of posts on `main`

Combine all to build the complete picture. Classify each change as A/M/D/R/RD.

### Step 2: Detect Issues (run validate-branch logic internally)

For each changed post, detect the same issues as `/validate-branch`:

**From renames (R/RM):**

- Missing `redirect_from:` when year/month changed vs main
- Frontmatter `date:` mismatch with filename date prefix
- Slug changed accidentally (cannot auto-fix — flag for manual review)
- Filename collision (cannot auto-fix — flag for manual review)

**From deletions (D):**

- Orphaned `post_url` references in other posts pointing to deleted slugs

**From new posts (A/??):**

- Malformed filename (cannot auto-fix — flag for manual review)
- Frontmatter `date:` mismatch with filename date prefix
- Missing required frontmatter fields (`title:`, `date:`, `tags:`, `description:`)

**From modifications (M):**

- Broken `post_url` references to non-existent posts
- Frontmatter `date:` mismatch with filename date prefix

**Cross-validation:**

- Broken `post_url` references anywhere in `_posts/`
- Duplicate slugs across different date prefixes

Build a fix plan before making any changes.

### Step 3: Fix Missing `redirect_from:` (🔴 ERROR)

For each renamed post where the year/month changed vs main and `redirect_from:` is missing:

1. Determine the old URL from the filename on `main`: `/OLD_YEAR/OLD_MONTH/slug.html`
2. Read the post's current frontmatter
3. If `redirect_from:` exists, APPEND the old URL (do not duplicate existing entries)
4. If `redirect_from:` does not exist, add it after the last frontmatter field before `---`

**Format:**

```yaml
redirect_from:
  - /OLD_YEAR/OLD_MONTH/slug.html
```

**Example:** Post was `2026-02-05-modern-art-card-game-review.md` on main, now `2017-06-15-modern-art-card-game-review.md`:

```yaml
redirect_from:
  - /2026/02/modern-art-card-game-review.html
```

### Step 4: Fix Frontmatter `date:` Mismatches (🟡 WARNING)

For each post where the frontmatter `date:` does not match the filename date prefix:

1. Extract the date from the filename: `YYYY-MM-DD`
2. Read the post's frontmatter
3. Update the `date:` field to match the filename date
4. If `date:` field does not exist, add it after `title:` (or as the second field)

**Rules:**

- The filename is the source of truth — frontmatter `date:` adapts to the filename, never the reverse
- Preserve the existing format style (quoted vs unquoted) if possible
- If the frontmatter has a time component (e.g., `"2026-02-05 10:00:00"`), keep the time part but update the date

### Step 5: Fix Broken `post_url` References (🔴 ERROR)

For each broken `post_url` reference found in any post:

1. Extract the referenced slug from the broken `post_url` tag
2. Search all files in `_posts/` for a file matching that slug (with any date prefix)
3. If exactly ONE match is found:
   - Replace the old `post_url` reference with the correct filename (date prefix + slug, no `.md`)
   - Use `{%- post_url YYYY-MM-DD-slug -%}` syntax
4. If ZERO matches found:
   - The referenced post was deleted with no replacement — remove the entire link and leave just the anchor text
   - Flag in the report for manual review
5. If MULTIPLE matches found:
   - Cannot auto-fix — flag for manual review (duplicate slug situation)

### Step 6: Fix Orphaned `post_url` from Deletions (🔴 ERROR)

For each deleted post that has `post_url` references pointing to it:

1. Check if the slug exists under a different filename (rename scenario)
2. If replacement found: update all `post_url` references to use the new filename
3. If no replacement found: remove the broken link, keep anchor text, flag for review

### Step 7: Remove Duplicate Files (🟡 WARNING)

For each slug that appears in multiple files with different date prefixes:

1. Identify which file is the "canonical" one:
   - If one is on `main` and one is new, the one on `main` is canonical — delete the new duplicate
   - If both are new, keep the one with the more plausible date — delete the other
   - If both are on `main`, **do NOT auto-fix** — flag for manual review
2. Before deleting any duplicate:
   - Verify the canonical file has equal or better content (compare file sizes as a proxy)
   - If the duplicate has significantly more content (>20% larger), flag for manual review instead
3. Use `git rm` for tracked files, `rm` for untracked files

### Step 8: Add Missing Frontmatter Fields (🟡 WARNING)

For each post missing required frontmatter fields:

1. **Missing `date:`** — add it from the filename date prefix (see Step 4)
2. **Missing `title:`** — derive from the filename slug:
   - Replace hyphens with spaces
   - Title-case the result
   - Wrap in quotes
   - Example: `2017-06-15-modern-art-card-game-review.md` → `title: "Modern Art Card Game Review"`
3. **Missing `tags:`** — add empty tags: `tags: []`
   - Do NOT guess tags — just add the empty array so the field exists
4. **Missing `description:`** — add empty description: `description: ""`
   - Do NOT generate description content — just add the field

### Step 9: Verify All Fixes

After applying all fixes:

1. Re-run the validation logic from Steps 2-6 on all changed files
2. Confirm all 🔴 ERRORs that were auto-fixable are now resolved
3. Collect any remaining issues that could not be auto-fixed

### Step 10: Generate Fix Report

```markdown
## Branch Fix Report: [branch-name]

### Fixes Applied

| #   | Post     | Fix Type                   | Details                                                 |
| --- | -------- | -------------------------- | ------------------------------------------------------- |
| 1   | slug.md  | Added redirect_from        | `/2026/02/slug.html`                                    |
| 2   | slug.md  | Fixed date: in frontmatter | `2026-02-05` → `2017-06-15`                             |
| 3   | other.md | Fixed post_url reference   | `old-slug` → `2017-06-15-old-slug`                      |
| 4   | dup.md   | Removed duplicate          | Kept `2017-06-15-slug.md`, removed `2026-02-05-slug.md` |
| 5   | new.md   | Added missing title        | Derived from filename: "New Post Title"                 |

### Summary of Fixes

| Fix Type                    | Count |
| --------------------------- | ----- |
| redirect_from added         | X     |
| date: frontmatter corrected | X     |
| post_url references fixed   | X     |
| Duplicate files removed     | X     |
| Missing frontmatter added   | X     |
| **Total fixes**             | **X** |

### Issues NOT Fixed (Manual Review Required)

| #   | Post    | Issue                  | Reason                                      |
| --- | ------- | ---------------------- | ------------------------------------------- |
| 1   | slug.md | Slug changed in rename | Cannot auto-determine correct slug          |
| 2   | slug.md | Multiple slug matches  | Ambiguous duplicate — human decision needed |
| 3   | slug.md | Duplicate on main      | Both files published — need manual merge    |

### Remaining Validation Status

- 🔴 Errors remaining: X (all require manual intervention)
- 🟡 Warnings remaining: X
- 🔵 Info: X
- **Verdict**: ✅ ALL AUTO-FIXABLE ISSUES RESOLVED / ⚠️ X ISSUES NEED MANUAL REVIEW

### Recommended Next Steps

1. [If manual issues remain] Review and fix the issues listed above
2. Run `/validate-branch` to confirm clean state
3. Commit when ready
```
