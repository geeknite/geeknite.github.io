# Validate Branch Before Commit

Validate all pending changes on the current branch against `main`: $ARGUMENTS

Compares the working tree and staged changes with the `main` branch to ensure post renames, date changes, new posts, and deletions are coherent and safe to commit. Catches mistakes like accidental slug changes, nonsensical dates, missing redirects, orphaned internal links, and duplicate posts. Use subagents in parallel to validate multiple posts simultaneously.

## Safety Rules

- **READ-ONLY validation** — this agent does NOT modify files, it only reports problems
- **All issues are reported** with severity levels: 🔴 ERROR (must fix), 🟡 WARNING (should fix), 🔵 INFO (review)
- If `$ARGUMENTS` specifies a filter (e.g., "2026-02", "board games", a slug), narrow validation to matching posts
- If `$ARGUMENTS` is empty or "all", validate ALL pending changes

## Process

### Step 1: Gather Branch State

Run these commands to understand the full scope of changes:

1. `git diff --name-status main...HEAD -- _posts/` — committed changes on this branch vs main
2. `git diff --name-status -- _posts/` — unstaged changes in working tree
3. `git diff --name-status --cached -- _posts/` — staged changes
4. `git status -- _posts/` — overall status summary

Combine all three to build a complete picture of what will be pushed. For each changed post, classify the change type:

- **A** (Added): New post not on main
- **M** (Modified): Content changed, filename unchanged
- **D** (Deleted): Post removed
- **R** (Renamed): File moved/renamed (may include content changes)
- **RD** (Renamed + Deleted on main): Complex rename situation

Also run `git ls-tree main --name-only -- _posts/` to get the full list of posts on `main` for comparison.

### Step 2: Validate Renames (R and RM changes)

For each renamed post, check:

1. **Slug preservation**: Extract the slug (everything after `YYYY-MM-DD-` without `.md`) from both old and new filenames. The slug MUST be identical — if it changed, flag as 🔴 ERROR.
   - Exception: if the old file had no date prefix (legacy migration), only the addition of a date prefix is expected
2. **Date coherence**: The new date prefix must make sense:
   - Is the date format valid (`YYYY-MM-DD`)?
   - Is the date in the past or reasonable near future (not years ahead)?
   - Does the date plausibly match the product being reviewed? (Read frontmatter `title:` to identify the product)
   - Flag as 🟡 WARNING if date seems implausible for the product (e.g., a 2013 board game dated 2026)
3. **Redirect check**: If the post existed on `main` with a different year/month:
   - Read the post's frontmatter for `redirect_from:`
   - The old URL path (`/OLD_YEAR/OLD_MONTH/slug.html`) MUST be present in `redirect_from:` — flag as 🔴 ERROR if missing
   - Remember: permalink format is `/:year/:month/:title:output_ext`, so only year/month changes affect the URL
4. **No filename collision**: Verify no other file in `_posts/` has the same target filename — flag as 🔴 ERROR if collision found
5. **Frontmatter date match**: The `date:` field in frontmatter should match the filename date prefix — flag as 🟡 WARNING if mismatched

### Step 3: Validate Deletions (D changes)

For each deleted post:

1. **Not a real deletion of unique content**: Check if the slug exists under a different date prefix (rename detection). If it's just one side of a rename, it's fine (🔵 INFO)
2. **Orphaned internal links**: Search all remaining `_posts/` files for `post_url` references to the deleted post's slug — flag as 🔴 ERROR if references exist without a replacement
3. **Redirect stub check**: If the deleted post has `redirect_to:` in its frontmatter, deletion is expected (🔵 INFO). If it does NOT have `redirect_to:`, flag as 🟡 WARNING — content may be lost
4. **Duplicate deletion**: If multiple files with similar slugs are being deleted, verify this is intentional (e.g., deduplication) — flag as 🔵 INFO

### Step 4: Validate New Posts (A and ?? changes)

For each new/untracked post:

1. **Filename format**: Must match `YYYY-MM-DD-slug.md` — flag as 🔴 ERROR if malformed
2. **Date sanity**: Date should be plausible (not far in the future, not before 2013 unless justified)
3. **No duplicate slug**: Check that no other post (on main or in working tree) has the same slug with a different date — flag as 🟡 WARNING if found (potential duplicate)
4. **Required frontmatter**: Must have `title:`, `date:`, `tags:`, `description:` — flag as 🟡 WARNING for missing fields
5. **Frontmatter date match**: `date:` field should match filename date prefix
6. **Not a duplicate of a deleted post**: If a deleted file has the same slug, this is likely a rename — verify content is preserved (🔵 INFO)

### Step 5: Validate Modified Posts (M changes)

For each modified post:

1. **Frontmatter integrity**: Read the post and verify frontmatter is valid YAML with required fields
2. **Date not changed in filename**: Modified posts should NOT have a different date prefix than what's on main — if the date prefix changed, it should show as R (rename), not M. Flag as 🔴 ERROR if somehow the filename date changed without git detecting a rename
3. **No broken internal links**: Check any `post_url` references in the modified content against existing files — flag as 🔴 ERROR for references to non-existent posts

### Step 6: Cross-Validation

Perform global checks across all changes:

1. **Internal link integrity**: For ALL posts in `_posts/` (not just changed ones), run a quick scan for `post_url` references. Verify each referenced post exists (considering renames). Flag any broken links as 🔴 ERROR
2. **Duplicate slug detection**: Build a map of all slugs across all posts. Flag any slug that appears more than once as 🟡 WARNING (possible duplicate content)
3. **Date density**: Count posts per month after all changes. Flag months with unusual density (>10 posts) as 🔵 INFO
4. **Orphaned redirects**: For any post with `redirect_from:` entries, verify the redirect source URL doesn't conflict with an actual existing post — flag as 🟡 WARNING if it does
5. **Mass operation coherence**: If >20 posts are being renamed with similar date patterns (e.g., all moved from 2026-02-XX to various historical dates), verify this looks like an intentional batch migration, not a scripting error. Flag as 🔵 INFO with summary

### Step 7: Generate Validation Report

```markdown
## Branch Validation Report: [branch-name] vs main

### Overview

| Metric            | Count |
| ----------------- | ----- |
| Posts added       | X     |
| Posts modified    | X     |
| Posts renamed     | X     |
| Posts deleted     | X     |
| **Total changes** | **X** |

### 🔴 Errors (Must Fix Before Commit)

| #   | Post    | Issue                  | Details                                    |
| --- | ------- | ---------------------- | ------------------------------------------ |
| 1   | slug.md | Slug changed in rename | Old: `old-slug`, New: `new-slug`           |
| 2   | slug.md | Missing redirect_from  | Was on main at /2026/02/, now at /2017/06/ |
| 3   | slug.md | Broken post_url ref    | References `non-existent-post`             |

### 🟡 Warnings (Should Fix)

| #   | Post    | Issue                     | Details                         |
| --- | ------- | ------------------------- | ------------------------------- |
| 1   | slug.md | Implausible date          | Product from 2005 dated 2025-08 |
| 2   | slug.md | Missing frontmatter field | No `description:` field         |
| 3   | slug.md | Potential duplicate       | Same slug as `other-slug.md`    |

### 🔵 Info (For Review)

| #   | Post    | Note                                                |
| --- | ------- | --------------------------------------------------- |
| 1   | slug.md | Deletion is part of rename (slug found in new file) |
| 2   | slug.md | Redirect stub deleted (had redirect_to:)            |

### Rename Validation (X renames)

| #   | Old Filename      | New Filename      | Slug Match  | Date OK | Redirect OK |
| --- | ----------------- | ----------------- | ----------- | ------- | ----------- |
| 1   | 2026-02-05-foo.md | 2017-06-15-foo.md | ✅          | ✅      | ✅          |
| 2   | bar.md            | 2019-03-15-bar.md | ✅ (legacy) | ✅      | N/A (new)   |

### Deletion Validation (X deletions)

| #   | Deleted File      | Has Replacement | Had redirect_to | Orphaned Links |
| --- | ----------------- | --------------- | --------------- | -------------- |
| 1   | 2026-02-05-foo.md | ✅ (renamed)    | No              | 0              |
| 2   | duplicate-post.md | ❌              | No              | 2 references   |

### New Post Validation (X new posts)

| #   | Filename          | Format OK | Date OK | Frontmatter OK | Duplicate? |
| --- | ----------------- | --------- | ------- | -------------- | ---------- |
| 1   | 2019-03-15-new.md | ✅        | ✅      | ✅             | No         |

### Date Density After Changes

| Month   | Post Count | Flag     |
| ------- | ---------- | -------- |
| 2026-02 | 3          | ✅ OK    |
| 2017-06 | 12         | ⚠️ Dense |

### Internal Link Health

- Total `post_url` references scanned: X
- Valid references: X
- Broken references: X (listed in Errors above)

### Summary

- 🔴 **X errors** — must fix before committing
- 🟡 **X warnings** — recommended to fix
- 🔵 **X info** — for your awareness
- **Verdict**: ✅ SAFE TO COMMIT / ❌ FIX ERRORS FIRST
```
