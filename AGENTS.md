# Project guide

- Personal static site for Jake Salerno. Edit `content/site.json`, `content/home-sections.json`, shared assets, and `scripts/build_site.py`; run `python3 scripts/build_site.py` and `python3 scripts/check_site.py`. Checked-in HTML serves directly on Vercel without a runtime/build install. Images remain at existing paths; responsive derivatives are in `assets/responsive/`. See README.md for the current architecture.
- Read `README.md` and any future `CLAUDE.md`; check branch, remotes, and working-tree status before editing. Preserve existing work and use a dedicated branch.
- Preserve design, typography, section IDs, navigation, media entries, canonical URLs, social links, verification tags, and image references unless the task requests changes.
- Write profile copy in third person without em dashes. Current title: Vice President of Go-to-Market at 0G Labs. Describe 0G as “the trust layer for AI.” Do not add an unverified Chainlink Total Value Secured figure.
- Local preview, verified from this directory: `python3 -m http.server 8000 --bind 127.0.0.1`. Open `http://127.0.0.1:8000/`. Stop the server with Ctrl-C when no longer needed.
- After editing, verify desktop and mobile layouts, navigation, gallery expansion and lightbox controls, browser errors, JSON-LD parsing, inline JavaScript syntax, and `git diff --check`. Review the diff for unrelated changes.
- Show the local browser preview and wait for Jake's approval before pushing, merging, or publishing.
- Deployment configuration check complete. Host: Vercel, project `jakesalerno-site` (`prj_BWqRSWzK5mvYFj9LWEnytKH6gnIo`), team `jakesalerno`, linked to `jake-salerno/jakesalerno-site`. API and GitHub records verify Production deployments from `main`; live HTML matched `e48b79e`. Feature branches have Preview deployments. No tracked GitHub Actions workflows or hosting config.
- Dashboard findings supplied and confirmed by Jake on October 29, 2026: production branch `main`; Auto-assign Custom Production Domains Enabled; Ignored Build Step Automatic; framework preset Other; root directory `./`; no Git or deployment source restrictions shown. Configuration check complete. These dashboard findings are user-confirmed, not a new direct inspection by Codex. Main is the production Git branch; keep local work on `codex/bio-update` until preview approval.
- Domain settings independently verified through Vercel: both custom domains verified, `jakesalerno.ai` redirects to `www.jakesalerno.ai`, neither pinned to a feature branch or custom environment. Do not alter hosting settings as part of content preparation.

## Pending photos and media

The latest explicit date in the current JavaScript content arrays is May 13, 2026 (Builder Nights photo and speaker card). Several entries have only a year or no date, so this is not a verified complete content cutoff.

Pending confirmation: batch of 13 photos described as dated May 21; `Builders Night Jake.HEIC`; `Jake Salerno-14.jpg`; `YBR09571.jpg`; `DSC04512.jpg`; `photo_2026-08-03 13.15.36.jpeg`; `X.png`, `X-2.png`, `X-3.png`. These filenames are not in the tracked checkout. Confirm source files, event associations, dates, captions, and selections before adding them. Do not infer them from filenames.

Local candidate review created October 29, 2026 in `/Users/jakesalerno/Documents/website-refresh-review/`: three numbered contact sheets and `candidate-manifest.json` (source paths and SHA-256 hashes). All eight named candidates were found in Downloads. There are 18 May 21 JPEG candidates, not the reported 13; all are included as numbers 09-26. Two additional Builders Night alternatives are 27-28. The second `Jake Salerno-14.jpg` in Desktop/June Desktop/Blue Spot Photography Gallery is byte-identical to the Downloads copy, so shown once. Original files were preserved. No event/date associations inferred from filenames.


## Source verification for the content refresh

Deployment check is complete per Jake's dashboard findings above. No hosting changes or publication authorized.

Source-date evidence is saved locally outside the deployable checkout in `/Users/jakesalerno/Documents/website-refresh-review/source-date-evidence.json`; before/after entry changes are in `verified-content-changes.json`.

- Event dates: Scaling Summit February 16, 2026 (0G ETHDenver recap); Toronto decentralized AI forum May 13, 2025 (linked Luma `29c32p2o` Event JSON-LD and recap); MUBC fireside October 23, 2025 (Luma `g4553kdo` and both existing fireside cards); Open AGI Summit February 19, 2026 (existing card explicitly prints date/year).
- Existing card evidence: Agents Unleashed October 1, 2025 with panel title “Prediction markets and AI: hype or substance?”; Warden December 20, 2024; House of AI and Consensus 2026 schedule explicitly say Miami, not Toronto. The schedule also places Marketers in the Arena in Miami. Applied these supported corrections.
- Articles: TheStreet February 25, 2026; ETHDenver recap March 5, 2026; EthCC recap April 23, 2026; Toronto recap May 26, 2025; verification article March 27, 2026; DL News April 10, 2026; Khalani October 29, 2025; Chainlink integration September 24, 2025; SwissBorg November 15, 2024. These are publication dates, not dates of interviews/events.
- Direct linked source metadata: Allora Space June 18, 2025; WAGMI Space December 27, 2024; Apple episode October 7, 2025; YouTube podcast premiered October 6, 2025; Web3 Roundtable Space February 14, 2025; FP Block recording post May 14, 2026; ETHDenver Main Stage recording post February 18, 2026. Post dates do not establish filming dates.
- Video upload dates remain separate from event dates: Scaling Summit X post February 26, 2026; Open AGI upload March 3, 2026; Quantum upload March 6, 2026; BASS upload February 19, 2026; InnovateDenver upload February 25, 2026; TOKEN2049 upload October 7, 2025; EthCC upload April 1, 2026. Do not replace known event dates with these upload dates.
- Zero Coding linked Luma event is February 20, 2026. It advertises a $3,000 coding prize pool, whereas the existing winners image visibly shows a separate $500,000 CGT Season 2 award dated February 20, 2026. Preserve the image caption and do not equate these prizes.

Remaining questions after source review:
- Select candidates 01-28 and supply event associations/captions for the chosen images. Filenames do not establish event dates.
- Builders Night card visibly says Miami, May 6; current entry says May 13, 2026. Confirm year/date and whether the existing photo is the same event. Korea Blockchain Week card says September 23-24 while entries use September 22, 2025; confirm Jake's session date.
- Quantum speaker card is a February 12 warm-up Space; Tectonic card is a February 19 in-person panel. Confirm warm-up year and whether to distinguish their event labels; do not conflate them.
- Exact dates and/or primary event links still missing for CUDIS, NodeOps fireside and outdoor panel, OnePiece solo talk and university panel, Prosperia, AI Frontier, NextGen, UT Austin, Huddle01, Autonomous AI, Alpha Edition and Plume. Some cards print month/day without a year. Bass Summit card depicts BASS Denver; confirm whether it is a duplicate feature of February 17, 2026 rather than a 2025 appearance.
- Aethir broadcast date and Binance repost date not confirmed from their existing pages. TheStreet publication date does not establish the interview/photo date. Do not add guessed dates.


## Additional asset batch: Website Update

Reviewed `/Users/jakesalerno/Desktop/Website Update/` locally: 5 Speaker Cards plus 28 Website Photos stills and 1 MP4. Existing references 01-28 preserved; additional references 29-62. No byte-identical or decoded-pixel-identical duplicates found against prior candidates/current site assets or within the new batch. Original hashes verified unchanged. Selections subsequently authorized below; other assets remain pending.

Review output: `/Users/jakesalerno/Documents/website-refresh-review/additional-asset-inventory.csv`, `additional-asset-inventory.json`, `additional-asset-review.txt`, `near-duplicate-screen.json`, `speaker-cards-1.jpg`, and `website-photos-1.jpg` through `website-photos-4.jpg`. The text report records card transcriptions, evidence, recommendations, quality issues and remaining questions.

Verified new evidence: 29 is October 5, 2026 Dev Day at National Gallery Singapore, moderator of “Beyond Scale: Where Does AI Go From Here?” (card plus organizer https://build.0g.ai/dev-day-2026). 31 is October 6, 2026 Multichain Day Singapore, “Agentic Finance: Autonomous Capital, Execution, and AI-Native Markets,” 3:15-3:45 PM; panel lineup (card plus venue https://luma.com/multichaindaysingapore). 30 explicitly says KBW2026, not KBW2025. 32 confirms Rare Evo Las Vegas July 28-31, 2026 conference range, not individual session dates. 33 is a roster crop without event heading; do not assume its association from styling alone.

Recommended shortlist: Event Features 29-32; Event Photos 36/38 (Dev Day), 44/46 (KBW2026, session pending), 51/54 (Rare Evo, dates pending). Near-duplicate/alternate groups: Dev Day 35-42, KBW 44-46, Rare Evo panel 49-51, title slide 52-54, same talk different slides 55-57, Liquidity Evening frames 58-62 plus photos 47-48. Prefer clean source photographs over video screenshots where possible. 34 is a 65-second 117MB portrait video, not a photo. No new batch evidence resolves the older different-year/city/session conflicts; retain supported corrections and keep unresolved details unguessed.


## Selected additions incorporated locally

Jake selected Event Features 29, 30, 31, 32 and Event Photos 36, 38, 44, 45, 51, 54. Reference 45, not 46, is the wider KBW image. Created optimized WebP copies in existing image folders, at most 2000 pixels per side, with EXIF orientation applied and original proportions retained. Original source hashes match the inventory. All unselected assets, including 01-28, remain outside the site for later selection.

New photos are inserted in preferred relative order 36, 44, 54, 38, 45, 51, then the existing sorter applies: verified exact dates descending, then year-only items. Thus Dev Day 36/38 appears together; year-only 44/54/45/51 retains its relative order after exact-dated 2026 entries. No fabricated sort dates or exact KBW/Rare Evo session dates. Rare Evo conference range is caption text only. Profile JSON-LD remains unchanged by these additions.

Speaker card thumbnails now use object-fit contain with no hover zoom, preserving all printed text and original proportions. Lightbox retains full-image contain behavior; selected entries have descriptive alt text and factual captions. Dev Day and Multichain Day lightboxes link to the verified organizer/event pages. No unverified recording links added.

Validation after selection: all ten additions opened in the lightbox with expected captions/alt text and correct image paths; organizer links checked against recorded sources, and speaker cards offer a full-size image link for fine print. Both gallery expansion controls work. Mobile viewport 390x844 has no horizontal overflow, captions wrap within the lightbox, and all loaded images decode. Desktop gallery and Rare Evo lightbox reviewed visually; Rare Evo source screenshots are darker/softer than professional event photos, with small slide text limited at thumbnail/mobile sizes. No browser warnings/errors. JSON-LD parses, inline JavaScript passes node --check, git diff --check passes. New images total approximately 1.6MB. Current local galleries: 37 photos, 34 event features. Nothing pushed, merged or published.


## Current media scope supersedes earlier selection instructions

Use only current contents of Desktop/Website Update for new refresh assets; preserve existing site and bio/corrections. All five cards are included, including roster 33 with neutral caption because its event heading/date are not visible. Full artwork retained and full-size viewing available. Independently select strongest professional photographs per event.

Rescan found 5 cards, 28 still photos and 1 MP4, rather than the user's expected 35 photos. Exact paths/hashes recorded in current-folder-rescan.json outside checkout. Do not imply missing files were reviewed. Selected photos: Dev Day DevDay-MainStage-227.jpg and DevDay-MainStage-234.jpg; KBW IMG_0201-2.jpg and IMG_0211-2.jpg; Rare Evo Screenshot 2026-10-29 at 2.22.19 PM.png and Screenshot 2026-10-29 at 2.28.02 PM.png; Liquidity Evening Screenshot 2026-10-29 at 3.30.29 PM.png (exact screenshot filenames use narrow no-break spaces before PM). The latter is the most expressive close view available but projected light covers faces; event name comes from visible Liquidity Evening branding, with no inferred date or year. Enlarged source artwork explicitly prints Seoul, Korea, so the caption includes Seoul. Source video is not a still-photo selection. Unselected files and earlier 01-28 remain outside site. Previous shortlist is historical, superseded by this selection.

Refresh now adds 5 speaker cards and 7 photos. Dev Day/KBW pairs provide expressive close views and complementary full-panel context; Rare Evo combines an engaged panel moment with standing presentation. Preserve native photo proportions in lightboxes; existing thumbnail crops retain Jake's face/gestures. No screenshot capture date used as event date. Originals verified unchanged.

Revised-scope QA: 38 total photos and 35 total event features; five new cards confirmed in DOM. New roster full-size link and Liquidity Evening lightbox checked, mobile 390px layout has no overflow, no broken loaded images, and no console errors/warnings. JSON-LD, JavaScript syntax, source hashes, and diff whitespace checks pass. No push, merge, publication or hosting changes.


Recursive count audit: exact path `/Users/jakesalerno/Desktop/Website Update/Website Photos` resolves to itself. Includes all hidden entries and extension-independent file identification. 14 JPEGs + 14 PNGs + 1 MP4 + 1 hidden .DS_Store = 30 filesystem entries; 28 photos. No subfolders, symlinks, Finder aliases, unknown image formats, cloud placeholders, unreadable image files or image decoding failures. All 28 images fully decoded; no additional photos discovered. The expected 35-photo count is not reproducible in this directory. Filename/type/size/decode audit is in recursive-folder-inventory.txt/.csv and recursive-folder-audit.json outside checkout. Selection finalized against these 28 available stills, retaining seven photos across four events and all five cards. Do not imply 35 photos were reviewed.


## Editorial/static discovery refresh supersedes previous rendering guidance

Homepage order: hero, three explicitly ranked appearances (EthCC, Scaling Summit, TOKEN2049), approved About/stats, six explicitly ranked On stage photos, selected interviews/media, Career, event-feature collection, Recognition, Contact. Native details and permanent archives keep all 38 photos/35 cards reachable, including five added cards and seven new photos. No JavaScript required for content, captions, navigation, full-size image links or details expansion. JS enhances native image links with an accessible dialog.

Eight indexable pages: /, /photos/, /media/, /event-features/, /appearances/ethcc-2026/, /appearances/scaling-summit-2026/, /appearances/token2049-2025/, /appearances/0g-dev-day-2026/. Canonical/schema/social/sitemap host is www.jakesalerno.ai; asset/navigation paths are root-relative for local preview and deployment compatibility. Training crawler preference remains wildcard Allow. OAI-SearchBot explicitly allowed. Local readiness is not actual indexing or AI citation evidence.

New dedicated source evidence supersedes earlier inferred session dates: EthCC April 1, 2026 (official session archive); TOKEN2049 October 2, 2025 (official recording description), uploaded October 7. Do not revert these to conference opening dates. TOKEN2049 playback and auto-generated transcript verified; summaries distinguish source speakers and historical roles. Dev Day has organizer-based summary, no invented recording takeaways.

PREPUBLICATION.txt records unresolved external links, QA limits and post-publication Search Console/Bing/account-access steps. content/link-audit.json retains request evidence; homepage redirects differ from 404 and access-restricted/unverified pages. Preserve BASS timestamp. Nothing published or submitted to search engines.


Final media follow-up: nine indexable pages including /appearances/agentic-finance-2026/. Agentic Finance video FEqSe1xZShQ matches Multichain Day card 31; October 6, 2026 session vs October 13 upload. Playback and auto-generated transcript verified; panelist role, not moderator. Connected homepage card, archive card, speaking and video listings. Existing three featured talks unchanged. TheStreet browser check reaches DataDome restriction, superseding earlier automated 404 classification. Yahoo syndicated copy loads with TheStreet attribution; use Read on Yahoo Finance for same single interview and related photo. Preserve original February 25 publication vs Yahoo February 26. KBW2025 archive unavailable; homepage link labelled honestly. See PREPUBLICATION.txt.


Visual-system pass supersedes previous photo rank and typography guidance. See DESIGN-SYSTEM-AUDIT.txt for verified Figma tokens versus explicit site-specific mappings. Both supplied Figma files specify Aeonik Pro display/text, not anticipated Regola Pro; identity uses 400/500. No licensed webfont source exists here. DM Sans remains the clearly documented authorized preview fallback; do not copy font files from Figma or corporate URLs. DM Serif removed. Shared CSS uses exact Brand/Neutral ramps, spacing/radius and type-scale values read from Figma. Exact component bindings, grid gutters, motion timings and dark mapping not inspected; site adaptations labelled in audit. Hero eyebrow AI INFRASTRUCTURE × GO-TO-MARKET; approved bio unchanged. Three featured talks retain order and gain existing image/artwork. Home photo order: Scaling, Dev Day, TOKEN wide, AI Frontier, BASS, KBW2026. homeCaption affects only homepage; archives keep complete supported metadata. AI Frontier city still unverified, so no Singapore added. All nine pages/38 photos/35 cards and Agentic Finance retained.
