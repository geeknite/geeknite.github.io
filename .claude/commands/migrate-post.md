# Migrate Post to BikingGeek

Migrate cycling/sports content to bikinggeek.github.io: $ARGUMENTS

## Argument Formats
- **Filename**: `/migrate-post garmin-edge-540-review.md` - migrate a specific post
- **Keyword**: `/migrate-post cycling` - find all cycling posts needing migration
- **Pattern**: `/migrate-post 2023-*-bike*` - migrate posts matching pattern

## Process

### Step 1: Identify Posts to Migrate
- If $ARGUMENTS is a filename: load that specific post from `_posts/`
- If $ARGUMENTS is a keyword: search `_posts/` for posts matching the topic

Cycling/sports indicators in tags, title, or content:
- cycling, mtb, bike, bicycle, gravel, road bike
- garmin, wahoo, shimano, sram (cycling-specific brands)
- running, trail running, marathon
- sports, fitness, training
- padel, tennis, swimming (other sports)

### Step 2: Check Current State
For each identified post:
- Check if `redirect_to:` already exists in frontmatter
- If already redirected: report as "already migrated" and skip
- Extract the post's date and slug for constructing the redirect URL
- Note: permalink pattern is `/:year/:month/:title:output_ext`

### Step 3: Add Redirect
Add `redirect_to` to the frontmatter:

```yaml
---
title: "Original Title"
date: "YYYY-MM-DD"
tags: [cycling, ...]
redirect_to: https://bikinggeek.github.io/YYYY/MM/slug
---
```

- The redirect URL slug must match the post's filename slug (without date and .md)
- Extract YYYY and MM from the post's date field
- The `jekyll-redirect-from` plugin handles the actual HTTP redirect
- Preserve ALL existing frontmatter fields

### Step 4: Find Cross-References
Search all `_posts/` for references to the migrated post:
- `post_url` tags referencing this slug
- Direct URL references to the post's permalink
- List all files that reference this post

Note: Existing `post_url` references will still work (they generate the local URL which then redirects). But flag them for user awareness.

### Step 5: Report
```markdown
## Migration Report

### Posts Migrated (X total)
| Post | Redirect URL | Cross-References |
|------|-------------|------------------|
| YYYY-MM-DD-slug.md | https://bikinggeek.github.io/YYYY/MM/slug | X files reference this |

### Already Migrated (skipped)
- [list posts that already had redirect_to]

### Cross-References Found
| Referencing File | References Post |
|-----------------|----------------|
| file.md | migrated-slug |

### Action Items
- Cross-references still work via redirect but may want to update with `/update-links`
- Verify the post exists on bikinggeek.github.io
```
