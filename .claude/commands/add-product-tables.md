# Add Amazon Product Tables to Post

Add visual product tables with `{% include amazon.html %}` to: $ARGUMENTS

## Process

### Step 1: Load Post
- Read the target post from `_posts/` matching $ARGUMENTS
- Identify all products mentioned (in H3 headings, affiliate links, body text)

### Step 2: Inventory Existing Tables
- Find all existing `{% include amazon.html %}` in the post
- Map which products already have tables vs which don't
- Note ASINs already used to avoid duplicates

### Step 3: Select Products for Tables
Choose top 2-4 featured products that LACK tables:
- **Priority 1**: The primary product being reviewed (in the title)
- **Priority 2**: Products discussed in their own H3 heading
- **Priority 3**: Products compared head-to-head
- Do NOT add tables for briefly mentioned products
- Do NOT add more than 4 tables total in a single post

### Step 4: Find ASINs and Images
For each product needing a table:
- Search Amazon for the correct ASIN (10-character alphanumeric code, e.g., `B0C4KLCD4D`)
- Find the product image URL from Amazon: `https://m.media-amazon.com/images/I/XXXXX.jpg`

**CRITICAL Rules**:
- Use REAL ASINs and image URLs only. Never invent them.
- If you cannot find a real ASIN, skip that product and note it in the report
- Verify the ASIN corresponds to the correct product
- Image URLs must start with `https://m.media-amazon.com/images/I/`

### Step 5: Insert Tables
For each product, add the include tag after its discussion section:

```
{% include amazon.html asin="B0XXXXXXXXX" imageUrl="https://m.media-amazon.com/images/I/XXXXX.jpg" %}
```

Placement rules:
- Place immediately after the product's descriptive paragraph(s)
- Add a blank line before and after the include tag
- The `amazon.html` template auto-generates a 6-region table (US, UK, DE, ES, FR, IT) with the correct affiliate tags from `_config.yml`

### Step 6: Report
```markdown
## Product Tables Report: [filename]

### Tables Added (X total)
| Product | ASIN | Image URL | Placement |
|---------|------|-----------|-----------|
| Product Name | B0XXXXXX | https://m.media-amazon.com/... | After H3 "Product Name" |

### Existing Tables (X total)
| Product | ASIN |
|---------|------|
| ... | ... |

### Skipped Products
- Product Name: reason (ASIN not found, already has table, etc.)

### Summary
- Before: X tables
- After: Y tables (+Z added)
```
