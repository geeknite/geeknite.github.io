# GeekNite Blog - Claude Code Project Context

Fes servir subagents sempre que sigui possible per a accelerar les tasques i millorar la qualitat de les respostes. Referencia completa: `.github/copilot-instructions.md`

## Site Architecture

- Jekyll blog at `blog.geeknite.com` via GitHub Pages
- Remote theme: `FerranSalguero/geeknite-theme`
- Posts: `_posts/YYYY-MM-DD-slug.md` (700+ posts, some legacy without date prefix)
- Timezone: `Europe/Madrid` | Permalink: `/:year/:month/:title:output_ext`
- Multilingual: English and Spanish content

## Amazon Affiliate Constants (from \_config.yml)

- **wsib URL**: `{{ site.constants.wsib }}` = `https://www.geeknite.com/`
- Regions: US (`vp04a-20`), UK (`kxl-21`), DE (`kvl-21`), ES (`kcl-21`), FR (`krv-21`), IT (`gkx09-21`)
- Inline link: `[Product Name]({{ site.constants.wsib }}product name)`
- Product table: `{% include amazon.html asin="ASIN" imageUrl="https://m.media-amazon.com/images/I/..." %}`
- **MAXIMIZE affiliate linking** - every product mention must link to wsib

## Internal Link Convention

- Format: `[text]({%- post_url YYYY-MM-DD-slug -%})`
- No file extension, hyphens only, full date prefix
- Use `{%-` whitespace stripping syntax `-%}`
- Minimum 3-5 in body + 3-5 in Related Posts section
- **ALWAYS verify filename exists** in `_posts/` before using post_url

## Post Frontmatter Template

```yaml
---
title: "Title Here"
date: "YYYY-MM-DD"
tags: [tag1, tag2, tag3]
description: "Excerpt in same language as post content."
---
```

## Hero Image Format

```markdown
[![Product Name](https://i.imgur.com/xxxxx.jpg){: .align-right}]({{ site.constants.wsib }}Product Name)
```

- Fallback image: `/assets/images/general.jpg`
- **NEVER invent imgur URLs** - verify they exist or use Amazon product images
- Always include `{: .align-right}` for proper text wrapping

## Content Rules

- Professional, informative, enthusiastic tone
- ~10k words minimum for comprehensive posts
- Fact-check all specs, prices, dates
- Emojis when appropriate: 🎮 gaming, 📱💻 tech, 🎬 movies, 🎌 anime
- Cycling/sports content belongs at `bikinggeek.github.io` (add `redirect_to:` in frontmatter)

## Quality Checklist

- [ ] Hero image with affiliate link + `.align-right`
- [ ] Frontmatter: title, date, tags, description
- [ ] 3-5+ internal `post_url` links in body
- [ ] 3-5+ links in Related Posts section at bottom
- [ ] All product mentions linked to `{{ site.constants.wsib }}`
- [ ] `{% include amazon.html %}` tables for major products (real ASINs only)
- [ ] H2/H3 structure (product names as H3, linked to wsib)
- [ ] No invented/broken image URLs
- [ ] No pipe `|` characters in titles — use `&#124;` HTML entity instead (pipes break Markdown table rendering in "Related Posts")

## Available Slash Commands

- `/create-post` - Create new blog post from topic
- `/add-affiliate-links` - Add Amazon affiliate links to product mentions
- `/add-internal-links` - Add internal post_url links to related posts
- `/review-post` - Quality review with score and recommendations
- `/update-links` - Update outdated links across posts
- `/add-product-tables` - Add amazon.html product tables
- `/migrate-post` - Migrate cycling/sports content to bikinggeek
- `/improve-post` - Orchestrator: run all improvements on a post
- `/find-posts` - Search posts by topic, tag, or quality criteria
- `/validate-branch` - Validate all pending changes vs main before committing (renames, dates, redirects, links)
- `/fix-branch` - Auto-fix issues detected by validate-branch (redirects, dates, broken links, duplicates)
- `/merge-posts` - Merge duplicate/related posts into single consolidated post
