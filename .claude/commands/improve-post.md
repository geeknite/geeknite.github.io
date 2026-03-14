# Improve Post (Orchestrator)

Comprehensively improve the blog post: $ARGUMENTS

This command runs all improvement tasks sequentially on a single post. Use subagents in parallel where possible (e.g., searching for related posts and scanning for unlinked products simultaneously).

## Process

### Step 1: Initial Assessment
Read the target post and perform a quick audit:
1. Read the full post content from `_posts/`
2. Check frontmatter completeness (title, date, tags, description)
3. Count current affiliate links (`site.constants.wsib`)
4. Count current internal links (`post_url`)
5. Count current product tables (`amazon.html`)
6. Check hero image format
7. Estimate word count
8. Check if post is cycling/sports content (needs migration)

Report the initial state before making changes.

### Step 2: Fix Frontmatter
- Add missing `description:` field (generate from first paragraph, match post language)
- Ensure `tags:` is in array format `[tag1, tag2]`
- Ensure `date:` is properly formatted as `YYYY-MM-DD`
- If cycling/sports content: add `redirect_to: https://bikinggeek.github.io/YYYY/MM/slug`

### Step 3: Fix Hero Image
- If hero image is **missing**: add one with affiliate link and `.align-right`
  - Use product image from Amazon if available
  - Fallback: `/assets/images/general.jpg`
- If hero image **lacks affiliate link wrapper**: wrap it
  ```markdown
  [![Product](imageUrl){: .align-right}]({{ site.constants.wsib }}Product)
  ```
- If hero image uses **example.com or suspicious URL**: replace with fallback and flag for user

### Step 4: Add Affiliate Links
Scan for unlinked product mentions and wrap them:
- `[Product Name]({{ site.constants.wsib }}Product Name)`
- Cover: consoles, games, gadgets, board games, movies, books, fashion
- Don't double-link existing affiliate links
- Don't link generic terms, only specific products

### Step 5: Add Product Tables
Add `{% include amazon.html %}` for top 2-3 products missing tables:
- Use real ASINs and Amazon image URLs only
- Place after the product's discussion section
- Skip products where ASIN cannot be verified

### Step 6: Add Internal Links
Search `_posts/` for related content and add links:
- 3-5 contextual `post_url` links in the body text
- 3-5 links in Related Posts section at bottom
- **VERIFY** each filename exists before using `post_url`
- Use `{%- post_url YYYY-MM-DD-slug -%}` syntax (no file extensions)

### Step 7: Content Enhancement (if needed)
- If word count < 3,000: flag as "needs content expansion" but don't auto-generate filler
- Add **Pros and Cons** section if missing
- Ensure H2/H3 heading structure is proper
- Add appropriate emoji (🎮📱🎬🎌) where natural

### Step 8: Final Quality Check
Verify all improvements:
- [ ] Hero image with `.align-right` and affiliate link
- [ ] Description in frontmatter
- [ ] 3+ internal `post_url` links in body
- [ ] 3+ internal `post_url` links in Related Posts
- [ ] All product mentions affiliate-linked
- [ ] 1+ `amazon.html` product tables
- [ ] No example.com or invented URLs
- [ ] All `post_url` references point to existing files

### Step 9: Summary Report
```markdown
## Improvements Applied: [filename]

### Initial State
| Metric | Value |
|--------|-------|
| Word count | X |
| Affiliate links | X |
| Internal links | X |
| Product tables | X |
| Hero image | OK / Missing / Fixed |

### Changes Made
- **Frontmatter**: [what was fixed]
- **Hero image**: [fixed / already correct]
- **Affiliate links**: +X added (Y total)
- **Internal links**: +X added (Y total)
- **Product tables**: +X added (Y total)
- **Content**: [sections added/enhanced]

### Final State
| Metric | Before | After |
|--------|--------|-------|
| Affiliate links | X | Y |
| Internal links | X | Y |
| Product tables | X | Y |

### Remaining Issues (require user action)
- [anything that needs manual intervention]
```
