# GeekNite Blog - Copilot Instructions

## Project Overview
GeekNite is a Jekyll-based blog focused on geek culture: video games, movies, anime, gadgets, fashion, board games, and Amazon shopping guides. Published via GitHub Pages at `geeknite.github.io` using the custom theme `FerranSalguero/geeknite-theme`.

**Important**: Cycling and sports content has been moved to bikinggeek.github.io. GeekNite now focuses exclusively on geek/pop culture content.

## Key Architecture Decisions

### Content Structure
- **Posts**: `_posts/YYYY-MM-DD-title.md` with YAML frontmatter (title, date, tags)
- **Multilingual**: Content in both English and Spanish (Castellano/Catalan)
- **Cross-linking**: Heavy use of Jekyll's `{% post_url %}` tag for internal references
- **Affiliate Focus**: Product reviews with Amazon affiliate links via `site.constants.wsib` and regional Amazon tags

### Custom Theme & Configuration
- Remote theme: `FerranSalguero/geeknite-theme` (custom fork)
- Configuration: `_config.yml` defines critical constants for Amazon affiliate tags (amazon_es, amazon_com, etc.)
- Timezone: `Europe/Madrid`
- Permalinks: `/:year/:month/:title:output_ext`

### Amazon Affiliate Integration
**Critical**: All product mentions must link to `{{ site.constants.wsib }}` - MAXIMIZE affiliate linking throughout content. Posts should use standardized multi-region Amazon product tables via `_includes/amazon.html` component showing the same ASIN across 6 Amazon regions (US, UK, DE, ES, FR, IT) with corresponding affiliate tags from `_config.yml`.

**Product Linking Strategy:**
- Link EVERY product mention (consoles, games, gadgets, books, movies, fashion items) to `{{ site.constants.wsib }}`
- Use inline text links: `[PlayStation 5]({{ site.constants.wsib }}playstation 5)`
- Add product tables with images for major products: `{% include amazon.html asin="B0C4KLCD4D" imageUrl="https://m.media-amazon.com/images/I/..." %}`
- Images must use existing Amazon product images with affiliate links
- Prioritize visual product tables over plain text links when possible

## Critical Workflows

### Local Development
- **Serve site**: `.\sv.bat` (runs `bundle exec jekyll serve -I --config _config.yml`) don't execute in terminal, let user do it
- **PowerShell script**: `m2jl.ps1` converts markdown posts to JSON (likely for AI processing)
- Drafts stored in `_drafts/` (extensive collection of unpublished posts)

### Post Creation Pattern
1. Create file: `_posts/YYYY-MM-DD-slug.md`
2. Add frontmatter with title, date, tags
3. **MAXIMIZE internal linking** - reference 3-5 related existing posts using `{% post_url YYYY-MM-DD-slug %}` (NO file extension)
4. **MAXIMIZE affiliate links** - link ALL product mentions to `{{ site.constants.wsib }}`
5. Include product images from Amazon or imgur with `https://i.imgur.com/` or `https://m.media-amazon.com/images/I/` URLs
6. Add `{% include amazon.html %}` product tables for major items with ASINs and images

### Internal Linking Convention
**Critical**: When linking between posts, use Jekyll's `post_url` tag:
```markdown
[link text]({%- post_url 2023-07-06-garmin-edge-540-review -%})
```
- No file extension
- Include full date prefix
- Hyphens only (no spaces)
- Use `{%-` syntax to strip whitespace

## Content Guidelines

### Post Structure
- **Hero image at top** - Must follow this format with affiliate link and alignment:
  ```markdown
  [![Product Name](https://i.imgur.com/image_id.jpg){: .align-right}]({{ site.constants.wsib }}Product Name)
  ```
  - Image must be an existing product image from Amazon or other stores
  - If no suitable image exists, you MUST find or generate an appropriate product image first
  - Use imgur URLs for hosting: `https://i.imgur.com/xxxxx.jpg` (medium size, no 's' suffix)
  - Always include `{: .align-right}` for proper text wrapping
  - Wrap in affiliate link using `{{ site.constants.wsib }}`
- Intro paragraph establishing context
- H2 sections for major topics
- H3 for product names/specific items - **link each product to `{{ site.constants.wsib }}`**
- **Reference 3-5 related existing posts** throughout content using `{% post_url %}` tags
- Add visual `{% include amazon.html %}` tables for featured products
- Conclusion with related posts links
- Related posts section at end (3-5 posts minimum) using `post_url` tags

### Tone & Style
- **Professional and informative** with enthusiastic touch
- Avoid overly casual or humorous tone
- Focus on product details, comparisons, and value propositions
- Emoji use when appropriate (gaming: 🎮, tech: 📱💻, movies: 🎬, anime: 🎌)
- Product comparisons and "vs" reviews frequent

### Content Quality & Rigor
- **Fact-check all data**: Never invent specifications, prices, or product details
- **Be rigorous**: Verify technical specs, release dates, and product features
- **Long-form content**: Posts should aim for ~10k words minimum for comprehensive coverage
- If uncertain about a detail, research it or omit it rather than guessing
- Use precise measurements, accurate model numbers, and verified information

## Common Tasks

### Updating Product Links
When a post becomes outdated, create a new post and update ALL references:
```bash
# Find all references to old post
grep -r "2023-07-04-prime-day-bike-gadgets" _posts/
```
Then replace with new `post_url` tag across affected files.

### Adding New Posts
Follow naming: `YYYY-MM-DD-descriptive-slug.md`
```yaml
---
title: "Your Title Here"
date: "YYYY-MM-DD"
tags: [tag1, tag2, tag3]
description: "Excerpt or summary of the post in the same language as the post."
---
```


## Domain-Specific Notes

### Video Games
- Console reviews (PlayStation, Xbox, Nintendo Switch)
- Game reviews across all platforms
- Gaming accessories and peripherals
- **Link every game/console mention to `{{ site.constants.wsib }}`**
- **Links to amazon should use tags defined in site.constants
  - amazon_es: "kcl-21"
  - amazon_com: "vp04a-20"
  - amazon_it: "gkx09-21"
  - amazon_uk: "kxl-21"
  - amazon_fr: "krv-21"
  - amazon_de: "kvl-21"

### Board Games
- Extensive collection of board game reviews
- Strategic use of related posts for game comparisons
- Link board games to Amazon affiliate

### Gadgets & Tech
- Smartphones, tablets, laptops, smartwatches
- Smart home devices, audio equipment
- Photography gear, drones
- **Every gadget must have Amazon affiliate link**

### Movies, Anime & Fashion
- Blu-ray/DVD reviews with Amazon links
- Anime merchandise and collectibles
- Fashion items and geek apparel
- Link all products to Amazon

### Amazon Shopping Guides
- Spanish-language guides for buying on Amazon.es from Spain
- Historical context (Brexit impacts, shipping changes)
- References to "Wishlist Manager" tool for price tracking
- Prime Day and seasonal shopping guides

## Pitfalls to Avoid
1. **Never** use file extensions in `post_url` tags
2. **Always** check `_config.yml` constants before hardcoding affiliate links
3. **Remember** to update date in frontmatter when creating posts
4. When linking to posts, verify the exact filename (dates matter!)
5. Imgur image URLs should use the `/...s.jpg` (small) or full size format consistently
6. Always keep UTF-8 encoding for special characters (é, ñ, ü, etc.)
