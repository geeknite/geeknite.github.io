# Review Post Quality

Perform a comprehensive quality review of: $ARGUMENTS

Read the post from `_posts/` and generate a structured quality report.

## Process

### Step 1: Load Post
- Find and read the target post from `_posts/` matching $ARGUMENTS
- If partial name given, search for matching files
- Parse frontmatter and body content separately

### Step 2: Frontmatter Audit
Check each field (report PASS/FAIL):
- [ ] `title:` - Present, descriptive, in quotes
- [ ] `date:` - Present, format YYYY-MM-DD
- [ ] `tags:` - Present, array format `[tag1, tag2]`
- [ ] `description:` - Present, matches post language, serves as excerpt
- [ ] No stale/incorrect fields

### Step 3: Structure Audit
Check each element (report PASS/FAIL):
- [ ] Hero image at top with `{: .align-right}` and affiliate link wrapper
- [ ] Hero image URL is real (not example.com or invented)
- [ ] Introduction paragraph after hero image
- [ ] H2 sections for major topics
- [ ] H3 sections for product names (each linked to `{{ site.constants.wsib }}`)
- [ ] Conclusion/recommendation section
- [ ] Related Posts section at bottom with `post_url` links

### Step 4: Affiliate Link Audit
- Count total product mentions in the post
- Count product mentions wrapped in `{{ site.constants.wsib }}` links
- List the top 5 unlinked product mentions
- Count `{% include amazon.html %}` tables present
- Check for hardcoded Amazon URLs (should use `site.constants` instead)
- Flag any broken or example.com URLs

### Step 5: Internal Link Audit
- Count `post_url` links in body text
- Count `post_url` links in Related Posts section
- **Target**: minimum 3-5 in body + 3-5 at bottom
- Verify each `post_url` reference points to an existing file in `_posts/`
- If under minimum, search for 5 related posts that could be linked

### Step 6: Content Quality
- Word count (comprehensive target: ~10,000 words)
- Flag suspicious claims about specs, prices, or dates
- Check for placeholder/example URLs
- Check for invented imgur URLs
- Verify Markdown syntax is correct
- Check UTF-8 encoding for special characters

### Step 7: SEO Check
- Title length (50-60 chars ideal)
- Description length (150-160 chars ideal)
- H2/H3 headings contain relevant keywords
- Images have descriptive context

### Step 8: Migration Check
- If post contains cycling, running, MTB, bike, sports content:
  - Check if `redirect_to:` to bikinggeek is present
  - If missing, flag as **CRITICAL**

### Step 9: Generate Report
```markdown
## Review Report: [post title]
**File**: [filename]
**Score**: X/10
**Word Count**: X words

### Critical Issues (must fix)
- ...

### Warnings (should fix)
- ...

### Suggestions (nice to have)
- ...

### Stats
| Metric | Current | Target |
|--------|---------|--------|
| Affiliate links | X | All product mentions |
| Internal links (body) | X | 3-5 minimum |
| Internal links (related) | X | 3-5 minimum |
| Product tables | X | 1-3 for featured products |
| Word count | X | ~10,000 |

### Quick Fix Commands
- `/add-affiliate-links [filename]` to fix X unlinked products
- `/add-internal-links [filename]` to add X missing internal links
- `/add-product-tables [filename]` to add product tables
- `/improve-post [filename]` to fix everything at once
```
