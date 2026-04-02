# Merge Related Posts

Merge duplicate or closely related posts about the same product into a single consolidated post: $ARGUMENTS

Use subagents in parallel to analyze candidate posts, check main branch status, and scan for cross-references simultaneously.

## Argument Formats

- **Keyword**: `/merge-posts macbook air m3` - find and merge all posts about MacBook Air M3
- **Explicit list**: `/merge-posts 2023-07-25-macbook-air-m3-review.md 2024-03-15-macbook-air-m3-review.md`
- **Pattern**: `/merge-posts *airpods-pro*` - merge posts matching glob pattern
- **`--dry-run`**: append to any format to preview without making changes
- **`--base FILENAME`**: force a specific post as the merge base instead of auto-selecting

## Safety Rules

- **NEVER delete a post that exists on the `main` branch** - always convert it to a redirect stub
- **NEVER merge posts in different languages** - Spanish and English posts about the same product stay separate
- **NEVER merge posts about genuinely different products** - e.g., "Zombicide: Black Plague" and "Zombicide: Prison Outbreak" are different games
- **ALWAYS write the consolidated post BEFORE modifying/deleting any source posts**
- **ALWAYS verify `post_url` targets exist** before updating cross-references
- **SKIP posts that already have `redirect_to:`** in their frontmatter
- If in doubt about whether posts should merge, **list them and ask the user** rather than merging automatically

## Process

### Step 1: Find Candidate Posts

- If $ARGUMENTS is a keyword: search `_posts/` filenames and frontmatter `title:` fields for matches
- If $ARGUMENTS is an explicit list: load those specific files
- If $ARGUMENTS is a glob pattern: match against `_posts/` filenames

For keyword search, normalize the query:

- Strip common suffixes: "review", "guide", "comparison"
- Search both filenames and `title:` frontmatter fields
- Include partial matches (e.g., "airpods pro" matches "airpods-pro-review" and "review-airpods-pro")

**Filter out non-candidates:**

- Posts with `redirect_to:` already set (already consolidated)
- Posts about genuinely different products (check title and first 50 lines of content)
  - Same product, different titles = DO merge (e.g., "MacBook Air M3 Review" vs "MacBook Air M3: The Featherweight Champ")
  - Different products in same franchise = do NOT merge (e.g., "The Mind" vs "The Mind: 2 Player Edition")
- Posts in different languages (detect from title, description, and first paragraph)

### Step 2: Group and Validate Candidates

Display the candidate posts for user confirmation:

```
Found X posts about "Product Name":

| # | Filename | Title | Date | Lines | Lang | On Main? |
|---|----------|-------|------|-------|------|----------|
| 1 | YYYY-MM-DD-slug.md | Title | YYYY-MM-DD | 95 | EN | YES |
| 2 | YYYY-MM-DD-slug.md | Title | YYYY-MM-DD | 83 | EN | NO |
```

Check main branch status for each candidate:

- Run `git ls-tree main --name-only -- _posts/` and check each candidate filename
- Also check if the file was renamed from a different name on main (look at `git status` for `R` entries)
- Mark each post as "On Main: YES/NO"

If `--dry-run` flag is set, **stop here** and report the candidates without making changes.

**CRITICAL**: If candidates span multiple languages, split into separate groups. Never merge across languages.

### Step 3: Select the Base Post

Auto-select the "base" post (the one that becomes the consolidated version) unless `--base` is specified.

**Selection criteria (in priority order):**

1. **Exists on main branch** - preserves established/indexed URL
2. **Most content** - longest post (line count / word count)
3. **Best quality** - hero image, affiliate links, internal links, product tables, description in frontmatter
4. **Most recent date** - more likely to have up-to-date information

If the best-content post differs from the on-main post, use the on-main post as the base (to preserve the URL) but merge the better content INTO it.

Report the selection:

```
Selected base: YYYY-MM-DD-slug.md (on main, URL: /YYYY/MM/slug.html)
Content source: YYYY-MM-DD-slug.md (longest at X lines, merging content from this)
```

### Step 4: Analyze and Merge Content

Read ALL candidate posts fully. For the consolidated post, combine the best elements:

**Frontmatter:**

- `title:` - Use the most descriptive/SEO-friendly title
- `date:` - Use the base post's date (preserves the established URL)
- `tags:` - Union of all unique tags from all candidates, in array format
- `description:` - Use the best description (longest, most keyword-rich)
- `last_modified_at:` - Set to today's date
- Do NOT include `redirect_to:` in the consolidated post

**Hero Image:**

- Select the best hero image across all candidates:
  - Prefer Amazon product images (`m.media-amazon.com`) over others
  - Prefer images with proper `{: .align-right}` formatting
  - Prefer images wrapped in affiliate link `[![...](url){: .align-right}]({{ site.constants.wsib }}...)`
  - NEVER use example.com or suspicious URLs

**Body Content:**

- Compare section structures (H2/H3 headings) across all candidates
- For each topic/section, pick the most comprehensive version
- Merge unique sections that only appear in one candidate
- Deduplicate overlapping content (don't repeat same specs/features)
- Preserve all `post_url` internal links (verify each still works)
- Preserve all affiliate links (`{{ site.constants.wsib }}`)
- Preserve all product tables (`{% include amazon.html %}`) - deduplicate by ASIN
- Ensure the final structure follows the standard pattern:
  1. Hero image with affiliate link
  2. Introduction
  3. H2/H3 topic sections
  4. Pros and Cons
  5. Conclusion
  6. Related Posts section

### Step 5: Write the Consolidated Post

Write the merged content to the base post's filename.

**CRITICAL**: Write the consolidated post FIRST, before modifying or deleting any source posts.

### Step 6: Handle Source Posts (Redirects and Deletions)

For each NON-base candidate post:

**If the post exists on the `main` branch** (found via `git ls-tree main --name-only -- _posts/`):

- Replace its entire content with a redirect stub:
  ```yaml
  ---
  title: "Original Title"
  date: "YYYY-MM-DD"
  redirect_to: /YYYY/MM/base-slug.html
  ---
  ```

  - The redirect URL uses the BASE post's date (YYYY/MM) and slug
  - Preserve the source post's own `date:` in the stub so its original URL still resolves
  - The `jekyll-redirect-from` plugin handles the HTTP 301 redirect

**Also check for renames**: If `git status` shows the post was renamed FROM another name on main (`R` status), the ORIGINAL filename on main also needs a redirect stub.

**If the post does NOT exist on `main`** (only on current branch):

- Delete the file entirely (it was never published, no URL to preserve)

### Step 7: Update Cross-References

Search ALL `_posts/` files for references to the non-base source posts:

1. **`post_url` references**: Search for `post_url.*SOURCE_SLUG` patterns
   - Replace with `{%- post_url BASE-YYYY-MM-DD-slug -%}`
   - Verify the base post filename exists

2. **Direct URL references**: Search for `/YYYY/MM/source-slug` patterns
   - Replace with `/YYYY/MM/base-slug.html`

3. **Verify**: After updates, confirm no old references remain

### Step 8: Quality Verification

Run a quick quality check on the consolidated post:

- [ ] Hero image with `{: .align-right}` and affiliate link wrapper
- [ ] Frontmatter complete: title, date, tags, description, last_modified_at
- [ ] 3+ internal `post_url` links in body (all targets verified to exist)
- [ ] 3+ internal `post_url` links in Related Posts section
- [ ] All product mentions affiliate-linked to `{{ site.constants.wsib }}`
- [ ] 1+ `{% include amazon.html %}` product tables
- [ ] No duplicate ASINs in product tables
- [ ] No invented or example.com image URLs
- [ ] No `redirect_to:` in the consolidated post itself
- [ ] Proper H2/H3 heading structure

If issues found, fix them. If content is thin (< 3000 words), flag for user follow-up with `/improve-post`.

### Step 9: Report

```markdown
## Merge Report: [product/topic]

### Candidates Found (X total)

| #   | Filename           | Title | Lines | Lang | On Main? | Action                        |
| --- | ------------------ | ----- | ----- | ---- | -------- | ----------------------------- |
| 1   | YYYY-MM-DD-slug.md | Title | 95    | EN   | YES      | **BASE**                      |
| 2   | YYYY-MM-DD-slug.md | Title | 83    | EN   | NO       | Deleted                       |
| 3   | YYYY-MM-DD-slug.md | Title | 82    | EN   | YES      | Redirect → /YYYY/MM/slug.html |

### Consolidated Post

- **File**: YYYY-MM-DD-slug.md
- **URL**: /YYYY/MM/slug.html
- **Title**: "Final Title"
- **Word count**: X words
- **Content sources**: merged best sections from X posts

### Redirects Created (X total)

| Source Post            | Redirect URL            |
| ---------------------- | ----------------------- |
| YYYY-MM-DD-old-slug.md | /YYYY/MM/base-slug.html |

### Posts Deleted (X total)

- YYYY-MM-DD-slug.md (not on main, never published)

### Cross-References Updated (X total)

| File                | Old Reference     | New Reference      |
| ------------------- | ----------------- | ------------------ |
| YYYY-MM-DD-other.md | post_url old-slug | post_url base-slug |

### Skipped Posts

- [posts with redirect_to already set]
- [posts in different language]
- [posts about different products despite similar name]

### Quality Check

| Metric                         | Status     |
| ------------------------------ | ---------- |
| Hero image                     | OK / Fixed |
| Affiliate links                | X total    |
| Internal links (body)          | X          |
| Internal links (Related Posts) | X          |
| Product tables                 | X          |
| Word count                     | X words    |

### Suggested Follow-ups

- `/improve-post YYYY-MM-DD-slug.md` to further enhance the consolidated post
- `/review-post YYYY-MM-DD-slug.md` to verify quality score
- `/update-links` if additional cross-references need attention
```
