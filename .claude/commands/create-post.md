# Create New Blog Post

Create a comprehensive blog post for the GeekNite blog about: $ARGUMENTS

Parse $ARGUMENTS for: topic/product name, optional language flag (`--lang es` for Spanish, default English).

Use subagents in parallel for research: one to find related posts, another to search for product info.

## Process

### Step 1: Research & Planning
- Determine: topic, product(s), target language from $ARGUMENTS
- Search `_posts/` for existing related posts (by keywords from the topic)
- Identify 8-12 candidate posts for internal linking
- Examine tags on similar existing posts to determine appropriate tags
- Check if a post on this topic already exists (warn user if so)

### Step 2: Generate Filename
- Format: `_posts/YYYY-MM-DD-descriptive-slug.md`
- Use today's date
- Slug: lowercase, hyphens only, descriptive
- Examples: `2026-03-09-ps5-pro-review.md`, `2026-03-09-mejores-tablets-2026.md`

### Step 3: Write Frontmatter
```yaml
---
title: "Full Descriptive Title"
date: "YYYY-MM-DD"
tags: [tag1, tag2, tag3]
description: "Short excerpt (150-160 chars) in the same language as the post."
---
```

### Step 4: Write Content

#### Hero Image
```markdown
[![Product Name](imageUrl){: .align-right}]({{ site.constants.wsib }}Product Name)
```
- Search for real Amazon product images for the main product
- If no real image available, use `/assets/images/general.jpg`
- **NEVER invent imgur URLs**
- Always include `{: .align-right}`
- Wrap in affiliate link

#### Content Structure
1. **Introduction** - Context, hook, why this matters (2-3 paragraphs)
2. **H2 sections** for major topics:
   - Design/Build Quality
   - Performance/Features
   - Comparisons with competitors
   - Use cases / Who is it for
   - Pros and Cons
3. **H3 subsections** for specific products - **each H3 product name MUST link to wsib**:
   ```markdown
   ### [Product Name]({{ site.constants.wsib }}Product Name)
   ```
4. **Product tables** for top 2-3 products:
   ```
   {% include amazon.html asin="REAL_ASIN" imageUrl="REAL_IMAGE_URL" %}
   ```
5. **Conclusion** with recommendation
6. **Related Posts** section (3-5 links)

#### Writing Guidelines
- Target ~10,000 words minimum for comprehensive coverage
- Professional, informative tone with enthusiastic touch
- Fact-check all specifications, prices, release dates
- Use emoji when appropriate: 🎮 gaming, 📱💻 tech, 🎬 movies, 🎌 anime
- Content in the language specified (default English)

### Step 5: Maximize Affiliate Links
- **EVERY product mention** must link to `{{ site.constants.wsib }}`
- Format: `[Product Name]({{ site.constants.wsib }}Product Name)`
- Include `{% include amazon.html %}` tables for top 2-3 products with **real** ASINs
- Link games, consoles, gadgets, books, movies, fashion items, board games

### Step 6: Maximize Internal Links
- Add 3-5 `post_url` links in the body text at contextually relevant places
- Add 3-5 links in the Related Posts section at the bottom
- Format: `[text]({%- post_url YYYY-MM-DD-slug -%})`
- **VERIFY** each filename exists in `_posts/` before using
- Never use file extensions in `post_url`

### Step 7: Cycling/Sports Check
- If the topic is about cycling, running, or sports:
  - Add `redirect_to: https://bikinggeek.github.io/YYYY/MM/slug` to frontmatter
  - Warn user: "This content belongs on bikinggeek.github.io"

### Step 8: Quality Verification
Run through the full checklist:
- [ ] Hero image with affiliate link + `.align-right`
- [ ] Frontmatter: title, date, tags, description
- [ ] 3-5+ internal `post_url` links in body (all verified to exist)
- [ ] 3-5+ links in Related Posts section
- [ ] All product mentions linked to `{{ site.constants.wsib }}`
- [ ] 1-3 `amazon.html` product tables with real ASINs
- [ ] H2/H3 structure with product names as H3
- [ ] No invented image URLs
- [ ] ~10,000+ words
- [ ] Proper UTF-8 encoding for special characters
