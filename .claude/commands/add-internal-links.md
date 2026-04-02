# Add Internal Links to Post

Find related posts and add internal `post_url` links to: $ARGUMENTS

Use subagents in parallel to search for related posts by tags, topics, and keywords simultaneously.

## Process

### Step 1: Load and Analyze Target Post
- Read the target post file from `_posts/`
- Extract: title, tags, topic keywords, product names mentioned
- Determine the post's language (English or Spanish)
- Note current internal links already present

### Step 2: Find Related Posts
Search `_posts/` for related content using multiple strategies in parallel:

1. **Tag match**: search for posts with overlapping tags
2. **Topic match**: search for posts mentioning the same products, games, or topics
3. **Category match**: find posts in the same domain (board games, tech, gaming, anime, etc.)
4. **Language match**: prefer linking to posts in the same language
5. **Recency**: prefer newer posts when relevance is equal

**CRITICAL**: For EVERY candidate post, verify the EXACT filename (including date prefix) exists in `_posts/`. Many posts lack the standard `YYYY-MM-DD-` date prefix. Always run a file existence check before using any `post_url` tag.

### Step 3: Select Best Candidates
- Choose 8-12 related posts total (for body + Related Posts section)
- Rank by relevance to the target post's content
- Ensure diversity: don't link 5 posts about the same sub-topic
- Exclude posts that are already linked in the current content

### Step 4: Insert Contextual Links (In-Body)
Add 3-5 internal links within the body text at contextually appropriate locations:
- Format: `[descriptive text]({%- post_url YYYY-MM-DD-slug -%})`
- Place in sentences that naturally reference the linked content
- Example: "If you enjoy cooperative board games, check out our [Marvel United review]({%- post_url 2023-08-15-marvel-united-multiverse-complete-review -%})."

Rules:
- **NEVER** use file extensions in `post_url` tags
- Use `{%-` and `-%}` whitespace stripping syntax
- Don't cluster all links in one paragraph; spread them throughout the content
- Link text should be descriptive (not "click here")

### Step 5: Add/Update Related Posts Section
- If no "Related Posts" section exists, create one at the end:
  ```markdown
  ## Related Posts
  - [Post Title]({%- post_url YYYY-MM-DD-slug -%})
  - [Post Title]({%- post_url YYYY-MM-DD-slug -%})
  ...
  ```
- If section exists, add new links to reach 3-5 minimum
- Don't duplicate links already in the section

### Step 6: Final Verification
For EVERY `post_url` added:
1. Verify the exact filename exists in `_posts/` (use ls/glob)
2. Remove any links to non-existent files
3. Ensure no file extensions are used

### Step 7: Report
```markdown
## Internal Links Report: [filename]

### Links Added to Body (X total)
| Link Text | Target Post | Section Placed |
|-----------|-------------|----------------|
| text | YYYY-MM-DD-slug | H2 Section Name |

### Links Added to Related Posts (X total)
- [Post Title](post_url reference)

### Already Present (X total)
- [list existing internal links]

### Summary
- Before: X internal links
- After: Y internal links (+Z added)
- Body: X links | Related Posts: Y links
```
