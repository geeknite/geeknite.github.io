# geeknite.github.io -- moved

**The blog now lives at <https://blog.geeknite.com/>.**
**Its source now lives in [`FerranSalguero/geek-blog`](https://github.com/FerranSalguero/geek-blog).**

This repository is the blog's ancestor. It is frozen: nothing here is published
any more, and the files under `_posts/`, `_pages/`, `_data/` and the rest are
kept only as history. **Do not edit a post here** -- it will never reach the
site. Write it in `geek-blog`, which deploys to `blog.geeknite.com` through
Cloudflare Pages.

The repository stays alive for one reason: to send old links to the new address.

## How the redirect works

GitHub Pages still serves this repository at `https://geeknite.github.io/`, and
two files do the whole job:

| file | what it covers |
|---|---|
| `index.html` | the home page -- `canonical` + `meta refresh` to `https://blog.geeknite.com/` |
| `404.html` | **every other path** -- rewrites the location to the *same path* on `blog.geeknite.com` |

Path preservation is what makes the old permalinks land. This blog used
`/:year/:month/:title.html`; `geek-blog` uses `/:year/:month/:title`, and its
`_redirects` file turns the `.html` form into a 301. So an old link resolves in
two hops, verified end to end:

```
https://geeknite.github.io/2016/03/nintendo-ds-lite-ultimate-retro-handheld-review.html
  -> https://blog.geeknite.com/2016/03/nintendo-ds-lite-ultimate-retro-handheld-review.html
  -> 301 -> https://blog.geeknite.com/2016/03/nintendo-ds-lite-ultimate-retro-handheld-review  (200)
```

## Why it is not an HTTP 301

**GitHub Pages cannot return a 301.** It has no server-side redirect rules: a
static host answers `200` for a file that exists and `404` for one that does
not, and nothing in a repository changes that. A `CNAME` file produces real
redirects, but only towards the custom domain it names -- and
`blog.geeknite.com` is served by Cloudflare Pages now, so this repository
cannot claim that hostname.

What is left is the documented equivalent that search engines follow: a
`<link rel="canonical">` plus a `<meta http-equiv="refresh" content="0; ...">`.
It is treated as a permanent move. Two consequences worth knowing before
someone files this as a bug:

- Requests for any path other than `/` are answered with **HTTP 404** plus the
  redirect markup. Browsers follow it; crawlers see the status first. This is
  the ceiling of the platform, not an oversight.
- `robots.txt` deliberately keeps crawlers out of the frozen source
  (`_posts/`, `_data/`, `*.md`, ...). `.nojekyll` means this site serves the
  repository files verbatim, so without those rules the 926 old posts would be
  fetchable as a second copy of a corpus that is published at
  `blog.geeknite.com`. The root stays crawlable on purpose -- that is how the
  redirect gets seen.
