# Add Affiliate Links to Post(s)

Review and maximize Amazon affiliate links in: $ARGUMENTS

Use subagents in parallel to search for product mentions and existing links simultaneously.

## Process

### Step 1: Load Target File(s)
- Read the post file(s) matching $ARGUMENTS from `_posts/`
- If $ARGUMENTS is a partial name, search `_posts/` for matching files
- If multiple files match a glob pattern, process each

### Step 2: Identify Unlinked Product Mentions
Scan content for product names that are NOT wrapped in affiliate links. Look for:
- **Consoles**: PlayStation, PS5, PS4, Xbox Series X/S, Nintendo Switch, Steam Deck
- **Games**: any game title mentioned as plain text
- **Tech**: headphones, keyboards, phones, laptops, tablets, monitors, smartwatches
- **Board games**: any board game name
- **Movies/Shows**: Blu-ray, DVD, streaming device mentions
- **Fashion/Books**: brand items, book titles
- **Any purchasable product** mentioned as plain text

A product is "unlinked" if it appears as plain text without being inside a markdown link to `{{ site.constants.wsib }}`.

### Step 3: Add Inline Affiliate Links
For each unlinked product mention:
- **FROM**: `Product Name` (plain text)
- **TO**: `[Product Name]({{ site.constants.wsib }}Product Name)`

Rules:
- Do NOT double-link already linked mentions
- Do NOT link generic terms ("controller" alone) - only link specific products ("Xbox Wireless Controller")
- Do NOT link mentions inside headings that are already linked elsewhere
- Keep the first mention linked per section; subsequent mentions in same paragraph can stay plain
- Preserve the original text casing

### Step 4: Verify Hero Image
- Check if hero image at top has an affiliate link wrapper:
  `[![Alt](url){: .align-right}]({{ site.constants.wsib }}Product)`
- If hero image exists but lacks affiliate wrapper: add it
- If no hero image exists: add one using `/assets/images/general.jpg` as fallback
- Flag any hero images using example.com or suspicious URLs

### Step 5: Check for Product Tables
- Count existing `{% include amazon.html %}` tables
- If major featured products (2-3 main products discussed in H3 headings) lack tables, note them as candidates
- Do NOT add tables in this command (use `/add-product-tables` for that)

### Step 6: Report Changes
```markdown
## Affiliate Links Report: [filename]

### Links Added (X total)
| Product | Section | Link |
|---------|---------|------|
| Product Name | H2 Section | `[Product Name]({{ site.constants.wsib }}Product Name)` |

### Already Linked (X total)
- [list of products that were already linked]

### Hero Image
- Status: [Fixed / Already correct / Added fallback]

### Product Tables
- Existing: X tables
- Candidates for /add-product-tables: [list products needing tables]

### Summary
- Before: X affiliate links
- After: Y affiliate links (+Z added)
```
