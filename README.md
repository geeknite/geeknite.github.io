# geeknite.github.io -- migrated

**This blog moved to <https://blog.geeknite.com/>.**
**Its source moved to [`FerranSalguero/geek-blog`](https://github.com/FerranSalguero/geek-blog).**

This repository was the blog's ancestor. Its content -- posts, layouts, data,
scripts -- was **removed from `main` on 2026-09-16** and now lives only in the git
history, where `git log` still reaches it. Nothing here is published any more.
**Do not write a post here**; write it in `geek-blog`, which deploys to
`blog.geeknite.com` through Cloudflare Pages.

What is left is the redirect, and that is the only reason the repository exists:

| file | what it covers |
|---|---|
| `index.html` | the home page -- `canonical` + `meta refresh` to `https://blog.geeknite.com/` |
| `404.html` | **every other path** -- rewrites the location to the *same path* on `blog.geeknite.com` |
| `robots.txt` | lets crawlers read the two files above |
| `.nojekyll` | no build; the four files are served as they are |

Deleting `index.html` or `404.html` does not tidy this repository up, it kills the
redirect.

## Old links still land

This blog used the permalink `/:year/:month/:title.html`; `geek-blog` uses
`/:year/:month/:title`, and its `_redirects` turns the `.html` form into a 301. The
path is preserved across the hop, so an old link resolves in two, verified end to end:

```
https://geeknite.github.io/2016/03/nintendo-ds-lite-ultimate-retro-handheld-review.html
  -> https://blog.geeknite.com/2016/03/nintendo-ds-lite-ultimate-retro-handheld-review.html
  -> 301 -> https://blog.geeknite.com/2016/03/nintendo-ds-lite-ultimate-retro-handheld-review  (200)
```

## Why this is not an HTTP 301

**GitHub Pages cannot return a 301 from anything in a repository.** It is a static
host: 200 for a file that exists, 404 for one that does not. The only real redirect it
emits is `<owner>.github.io/*` towards the custom domain named in a `CNAME` file -- and
`blog.geeknite.com` is served by Cloudflare Pages now, so this repository cannot claim
that hostname back.

HTML cannot supply one either. A 301 is a response status line plus a `Location`
header, both sent before the browser parses a single tag; `<meta http-equiv>` does not
set an HTTP header despite its name, and no server reads it. What is left is the
documented equivalent that search engines follow as a permanent move: a canonical link
plus a zero-delay meta refresh.

One consequence to state rather than re-diagnose: every path other than `/` is answered
with **HTTP 404** plus the redirect markup. Browsers follow it; crawlers see the status
first. That is the ceiling of the platform, which is why `404.html` carries a `noindex`.
