# Broken post_url References Report

Generated: 2026-05-02

## Summary

- **Total broken references:** 293
- **Unique broken slugs:** 236
- **Files affected:** 142

## Top 20 Files with Most Broken Links

1. \_posts/2025-12-15-top-5-strategy-board-games-2025.md (13 broken links)
2. \_posts/2025-06-20-macbook-air-15m4-review.md (13 broken links)
3. \_posts/2025-04-16-gloom-109-108-ar-sv3-ruler-of-the-black-flame-jp-nm.md (9 broken links)
4. \_posts/2025-10-25-uno-gold-edition-card-game-2025-review.md (7 broken links)
5. \_posts/2025-06-15-macbook-air-m4-13-2025-review.md (6 broken links)
6. \_posts/1994-04-01-mtg-fourth-edition-booster-pack.md (6 broken links)
7. \_posts/2025-11-12-uno-no-mercy-card-game-2025-review.md (5 broken links)
8. \_posts/2025-11-12-apple-macbook-air-15-m4-chip-16gb-ram-256gb-ssd-midnight-mw1l3ll-a-2025-model.md (5 broken links)
9. \_posts/2025-11-01-wicked-uno-movie-edition.md (5 broken links)
10. \_posts/2024-11-20-trio-family-card-game-review.md (5 broken links)
11. \_posts/2024-04-07-vintage-skip-bo-1993-review.md (5 broken links)
12. \_posts/2021-11-01-exploding-kittens-exploding-minions-card-game-2-5-players-age-7-new.md (5 broken links)
13. \_posts/2015-04-11-asmodee-dixit-promo-cards-tabletop-day-2015-nm.md (5 broken links)
14. \_posts/2026-12-20-cards-against-humanity-die-weihnachtsedition.md (4 broken links)
15. \_posts/2026-12-18-uno-family-pack-family-game-night-2-10-players-christmas-games.md (4 broken links)
16. \_posts/2025-11-01-uno-nfl-elite-core-edition-wild-foil-flux-will-mcdonald-iv-sp.md (4 broken links)
17. \_posts/2025-10-14-uno-elite-core-edition-yellow-tyler-goodson.md (4 broken links)
18. \_posts/2025-04-28-uno-elite-core-edition-2025-amarillo.md (4 broken links)
19. \_posts/2025-04-08-mattel-pocket-size-phase-10-go-2025-mini-card-game.md (4 broken links)
20. \_posts/2022-10-15-phase-10-40th-anniversary-metal-steel-case.md (4 broken links)

## Categories of Issues

### 1. Invalid/Malformed Slugs (Not actual post references)

These appear to be parsing errors or placeholder text mistakenly captured:

- `per`, `tag`, `to`, `so`, `for`, `and`, `di`, `e`
- `below`, `link`, `links`, `pages`, `markers`, `references`
- `Verweise` (German for "references")

Count: ~20 false positives

### 2. Slugs with .html or .md Extensions

Should not include file extensions in post_url:

- `2019-11-20-beste-brettspiele-2019.html`
- `2020-05-01-monopoly-kritik.html`
- `2023-03-12-family-game-night-essentials.html`
- `2023-06-10-vintage-games-guide.html`
- `2023-06-15-board-games-for-kids.html`
- `2023-12-01-quick-party-games.html`
- `2024-01-01-uno-classic.md`
- `2024-01-15-uno-vs-skip-bo.html`
- `2024-04-14-codenames-original.md`
- `2024-07-18-uno-sport-edition.md`
- `2024-10-05-family-game-night-hack.html`
- `2025-11-01-family-games-night.html`
- `2026-04-01-inclusive-humor.md`
- `2026-05-01-adult-party-games.md`

Count: 14 references

### 3. Slugs with Trailing Punctuation

Punctuation should not be part of the slug:

- `2021-05-03-best-party-games-roundup].`
- `2023-12-31-best-albums-2023](`
- `2022-08-14-storytelling-in-metal](`
- `2024-02-01-top-10-retro-card-games.`
- `below.`
- `tag.`

Count: 6 references

### 4. Slugs with Single Quotes (encoding/formatting issues)

- `'2023-08-20-uno-variant-history'`
- `'2024-05-14-macbook-air-typing-differences'`
- `'2024-09-12-macbook-air-2024-review'`
- `'2024-11-01-uno-edition-review'`
- `'2024-11-05-air-ports-evolution'`
- `'2024-12-02-air-vs-pro-value'`
- `'2025-01-11-laptop-display-nerd-notes'`
- `'2025-01-23-macos-linux-windows-workflow'`
- `'2025-02-28-mac-gaming-performance'`
- `'2025-03-01-energy-smart-laptops'`
- `'2025-03-22-laptop-performance-roundup'`
- `'2025-04-08-windows-vs-mac-port-choices'`
- `'2025-04-15-creative-workflows-mac'`
- `'best-party-games-2023'`
- `'board-games-collectors-opinions'`
- `'game-night-organization-101'`
- `'geeknite-board-game-night-essentials'`
- `'nostalgia-gaming-collectibles-roundup'`
- `'party-games-dynamics-101'`
- `'ps4-adventures-review'`
- `'uno-edition-overview'`
- `'uno-original-review'`

Count: 22 references

### 5. Missing Date Prefix

Should have YYYY-MM-DD prefix:

- `magic`
- `trudvang-legends-core-set-review`

Count: 2 references

### 6. Legitimate Missing Posts

Properly formatted slugs referencing non-existent posts (190+ unique slugs).

Examples:

- 2014-12-20-cah-strategy-and-first-experiences
- 2015-01-20-dixit-base-game-review
- 2015-02-14-dixit-promos-and-night-hijinks
- 2015-03-30-dixit-odyssey-expansion-notes
- 2015-12-25-geeknite-holiday-board-games-roundup
- 2018-04-12-tolkien-language-mechanics
- 2019-03-21-old-school-boosters
- 2020-05-10-sushi-go-party-review
- 2020-07-04-core-set-2020-booster-pack
- 2021-07-18-retro-mtg-unboxings
- ... and 180+ more

## Recommendations

### Immediate Actions

1. **Fix malformed references** (categories 1-5): ~64 references
   - Remove file extensions (.html, .md)
   - Strip trailing punctuation
   - Remove single quotes
   - Fix obviously broken slugs (single words like "tag", "magic", etc.)

### Strategic Actions

2. **Address legitimate missing posts** (~190 references)
   - Option A: Create the referenced posts
   - Option B: Replace with `{{ site.constants.wsib }}` links for product-related topics
   - Option C: Update to link to existing similar posts with correct slugs
   - Option D: Remove the references if they're not essential

## Detailed Broken References

For the complete list with file paths and line numbers, see the detailed output file.

## How to Fix

{% raw %}

### Example 1: Remove file extension

```markdown
# Before

[Link text]({%- post_url 2024-01-01-uno-classic.md -%})

# After

[Link text]({%- post_url 2024-01-01-uno-classic -%})
```

### Example 2: Remove trailing punctuation

```markdown
# Before

[Link text]({%- post_url 2024-02-01-top-10-retro-card-games. -%})

# After

[Link text]({%- post_url 2024-02-01-top-10-retro-card-games -%})
```

### Example 3: Remove quotes

```markdown
# Before

[Link text]({%- post_url '2024-11-01-uno-edition-review' -%})

# After

[Link text]({%- post_url 2024-11-01-uno-edition-review -%})
```

### Example 4: Replace missing post with wsib link

```markdown
# Before

[Link text]({%- post_url 2021-07-18-retro-mtg-unboxings -%})

# After

[Link text]({{ site.constants.wsib }}retro mtg unboxings)
```

{% endraw %}
