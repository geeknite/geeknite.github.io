# Find Posts

Search the GeekNite blog for posts matching: $ARGUMENTS

Use subagents in parallel when searching multiple criteria.

## Process

### Step 1: Parse Query
Determine search type from $ARGUMENTS:
- **Keywords**: search titles and content for topic matches
- **`--tag TAG`**: search posts by specific tag
- **`--no-affiliate`**: find posts WITHOUT `site.constants.wsib` links
- **`--no-internal`**: find posts WITHOUT `post_url` links
- **`--no-tables`**: find posts WITHOUT `amazon.html` includes
- **`--needs-migration`**: find cycling/sports posts WITHOUT `redirect_to`
- **`--no-description`**: find posts missing `description:` in frontmatter
- **`YYYY` or `YYYY-MM`**: filter by date in filename

### Step 2: Execute Search
Search across `_posts/` files using grep:
- For content/title keywords: search file content and filenames
- For tags: search frontmatter `tags:` lines
- For missing features: use inverted grep to find posts LACKING the pattern
- Combine multiple flags to narrow results

### Step 3: Output Results
Format results as a markdown table:
```
| # | Filename | Title | Date | Affiliates | Internal Links | Tables |
|---|----------|-------|------|------------|----------------|--------|
```

Show up to 20 results. If more exist, report the total count.

### Step 4: Suggest Actions
Based on results, suggest relevant slash commands:
- "Run `/add-affiliate-links` on these X posts to add missing affiliate links"
- "Run `/improve-post` on posts with the most issues"
- "Run `/migrate-post` on cycling posts lacking redirects"
- "Run `/review-post` on a specific post for detailed analysis"
