# GeekNite Blog - Copilot Instructions

## Project Overview
GeekNite is a Jekyll-based blog focused on geek culture: video games, movies, anime, gadgets, fashion, board games, and Amazon shopping guides. Published via GitHub Pages at `blog.geeknite.com` using the custom theme `FerranSalguero/geeknite-theme`. Only use english or spanish.

**Important**: Cycling and sports content has been moved to bikinggeek.github.io. GeekNite now focuses exclusively on geek/pop culture content. Add redirects to existing posts when editing: redirect_to: https://bikinggeek.github.io/YYYY/MM/slug

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
7. If post is a product review post date should be close to product release date and last_modified_at should be current date

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
  - If no suitable image exists, use the fallback image: `/assets/images/general.jpg`
  - Use imgur URLs for hosting: `https://i.imgur.com/xxxxx.jpg` (medium size, no 's' suffix)
  - **Note**: Uploading custom images to imgur requires user intervention (Copilot cannot upload images)
  - **CRITICAL**: Never invent imgur URLs - always verify the image exists by checking with `fetch_webpage` or using existing URLs from the blog
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
- **Professional and informative** — NO enthusiastic/casual tone
- Focus on solving specific user problems with clear decisions
- Product comparisons and "vs" reviews frequent
- Emoji use sparingly when appropriate (gaming: 🎮, tech: 📱💻, movies: 🎬, anime: 🎌)

### Monetization-First Content Strategy

**CRITICAL**: Every post must follow this user journey pattern:

```
User arrives with a specific question
    → Reads content
    → Makes a decision
    → Clicks affiliate link
```

**Content Philosophy:**
- **DO NOT "recommend things"** — Instead, **SOLVE DECISIONS**
- User searches with a specific problem → Post provides the answer → User clicks to buy
- Every section must lead to an actionable decision with a clear affiliate link
- Avoid generic "top 10 lists" — Focus on "Which X should I buy for Y situation?"

**Post Types That Convert:**
| Post Type | Example Title | Why It Works |
|-----------|---------------|--------------|
| Decision resolver | "PS5 vs Xbox Series X: Which Console for You?" | User has a specific choice to make |
| Problem solver | "Best Gaming Headset Under €100 for FPS Games" | User has budget + use case |
| Comparison | "GTA IV Complete vs Red Dead Redemption GOTY" | User deciding between options |
| Buying guide | "Which Nintendo Switch Model to Buy in 2024?" | User ready to purchase |

**Post Structure for Conversion:**
1. **Title**: Frame as a decision/question the user needs answered
2. **Intro**: Acknowledge the user's specific problem (1-2 sentences max)
3. **Quick Answer**: Give the verdict immediately for users who want fast answers
4. **Detailed Analysis**: For users who want to understand why
5. **Decision Table**: Summary table at the end with affiliate links
6. **Single CTA**: One clear "buy now" action per section

**Avoid These Patterns:**
- ❌ "Here are 10 great games you should try"
- ❌ "I recommend checking out..."
- ❌ Generic product lists without decision context
- ❌ Long intros before getting to the point
- ❌ Multiple CTAs that confuse the user

**Use These Patterns:**
- ✅ "If you want X, buy [Product A](affiliate). If you need Y, get [Product B](affiliate)."
- ✅ "The verdict: [Product](affiliate) is the best choice for [specific use case]."
- ✅ Tables with clear winner indicators and affiliate links
- ✅ "Bottom line: Buy [this](affiliate) if... Buy [that](affiliate) if..."

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
7. **Never** write generic recommendation posts — always frame content as decision resolution
8. **Avoid** long introductions — get to the decision point fast

### When reviewing newly created _posts from current or last month and without date in the filename (considered drafts even they are not in the _drafts/), follow this checklist:
1. **Check for duplicates**: Search `_posts/` for similar content before publishing, specially if too brief content
2. **Date assignment**: If no date exists, use approximate release date of main product/topic (never beyond actual release) and set `last_modified_at` to current date. nomes hi hauria d'haver un post per dia sino solen ser duplicats
3. **Merge or delete**: If a published post covers the same topic, merge useful content or delete the draft
4. **Cycling/sports content**: Add redirect to bikinggeek.github.io, do not publish on GeekNite
5. **Obsolete promotions**: Delete drafts about closed promotions, expired offers, or discontinued services
6. **Convert HTML to Markdown**: Old Blogger imports are in HTML — convert to clean Markdown when publishing
7. **Image check**: - If no specific image exists, generate a prompt for image generation and set it into the frontmatter in field `hero_image`
8. **Quality check**: Ensure affiliate links, images, internal links and long content follow guidelines before publishing


