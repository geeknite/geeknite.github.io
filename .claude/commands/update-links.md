# Update Links Across Posts

Find and update outdated links for: $ARGUMENTS

## Argument Formats
- **Post slug**: `/update-links 2023-07-04-prime-day-bike-gadgets` - find all references to this post
- **Replacement**: `/update-links "old-post-slug" -> "new-post-slug"` - replace old with new
- **Product update**: `/update-links "Garmin Edge 530" -> "Garmin Edge 540"` - update product references

## Process

### Step 1: Parse Arguments
- If $ARGUMENTS contains `->`: treat as old -> new replacement
- If $ARGUMENTS is a post slug: find all `post_url` references to it
- If $ARGUMENTS is a product name: find all mentions in content and links

### Step 2: Find All References
Search across all `_posts/` files:
- For post slugs: search for `post_url.*slug` patterns
- For products: search for the product name in text and affiliate links
- Report total files and occurrences found

### Step 3: Plan Updates
For each file containing references, show:
```
File: _posts/YYYY-MM-DD-slug.md
  Line X: [current text] -> [proposed replacement]
```

### Step 4: Execute Updates
- Replace old `post_url` references with new ones
- Update product names and affiliate links
- If replacing a post reference, verify the NEW post exists in `_posts/`

### Step 5: Safety Rules
- **NEVER** delete content, only update references
- If a referenced post doesn't exist and no replacement given, FLAG it but don't remove
- Preserve surrounding context and formatting
- Show a summary diff for each modified file

### Step 6: Verify
- Re-search to confirm all old references have been updated
- List any references that could not be automatically updated
- Report: X references updated across Y files

### Step 7: Report
```markdown
## Link Update Report

### Search: [what was searched for]

### Files Modified (Y total)
| File | Changes | Details |
|------|---------|---------|
| filename.md | X replacements | old -> new |

### Unresolved References
- [list any that couldn't be auto-fixed with explanation]

### Verification
- Old references remaining: X (should be 0)
- New references verified: Y
```
