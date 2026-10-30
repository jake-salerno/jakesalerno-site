# Jake Salerno website

Static website for https://www.jakesalerno.ai/. Vercel serves the checked-in HTML; no framework, install step, or production runtime is required.

Preview from this directory:

    python3 -m http.server 8000 --bind 127.0.0.1

Open http://127.0.0.1:8000/.

## Editing

- `content/site.json`: photo, card, talk and media records; explicit editorial ranks select the homepage order. Exact dates and year-only dates are different levels of evidence.
- `content/home-sections.json`: approved bio, career, recognition and contact markup.
- `content/images.json`: intrinsic dimensions and responsive asset mapping.
- `scripts/build_site.py`: standard-library-only generator; appearance summaries/sources and page templates live here.
- `assets/site.css` and `assets/site.js`: shared presentation and progressive lightbox enhancement.
- Generated `index.html`, archive folders, appearance folders, and `sitemap.xml` are checked in so publishing needs no generator dependency.

After editing content/templates:

    python3 scripts/build_site.py
    python3 scripts/check_site.py
    node --check assets/site.js

The generator's editorial revision date is a real content modification date. Update it when making a substantive later revision, never just to imply a fresh crawl or publication. Keep original public image URLs stable. Responsive WebP copies live in `assets/responsive/`.

Review desktop/mobile crops, links, captions and the no-JavaScript experience. Preserve complete artwork on cards. Unknown credits/licenses and exact event dates must not be invented.

## Publishing

Production branch: `main`, through the existing Vercel Git integration. Work on `codex/bio-update` remains local until Jake approves. Do not push, merge or publish before that approval. See AGENTS.md and PREPUBLICATION.txt for evidence, unresolved links, and post-publication checks.

Visual-system evidence and limitations: DESIGN-SYSTEM-AUDIT.txt records the exact readable Figma tokens, site-specific mappings, intentional omissions, and the Aeonik Pro licensing limitation. DM Sans is the explicitly documented preview fallback. Homepage-only short captions live in homeCaption; full archive metadata remains unchanged.
