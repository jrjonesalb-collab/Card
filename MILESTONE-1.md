# Milestone 1 — local design preview, 2026-09-08

## Design revision after review

Jordan rejected the decorative top stripe; removed it. He supplied https://jrjinc.com/ and 1140 SW Ric Williamson Memorial Hwy, Weatherford, TX 76088, now included on the page and in the vCard. The screenshot of the old card remains a visual reference only; its placeholder contact values were not reused. The initial omission of website/address described below is superseded by these confirmed values. Build, lint and three updated tests pass; revised browser check verifies the stripe is absent and the website/map links contain confirmed values.

## Starting state and investigation

The workspace was empty. Cloned `jrjonesalb-collab/Card`, branch `main`, starting commit `62a3251e2856a3c7d99f3c88961850424ae9ebf0`. No repository AGENTS.md, prior session notes, product rules, or project handoff existed. README contained only the project name.

Inspected Card's HTML, logo.png and photo.jpg, and fetched Business-Card's `index (3).html`. Both HTML samples use placeholder identity/branding. Reused none of those contact values. The actual logo image visually reads JRJ construction (red mark, black wordmark); appropriate for the requested company. Repository portrait used provisionally because no separate image attachment was available in this task. The source image is unchanged; only CSS framing is applied.

Authenticated GitHub API checks (admin permission) returned `private:true`, `has_pages:false` for both repositories; `/repos/jrjonesalb-collab/Card/pages` and Business-Card's Pages endpoint returned 404. A direct request to `https://jrjonesalb-collab.github.io/Card/` returned HTTP 404.

Jordan supplied the historical environment link: https://github.com/jrjonesalb-collab/Card/deployments/github-pages . Latest deployment ID `3869051187` at commit `62a3251e2856a3c7d99f3c88961850424ae9ebf0` has a success status dated 2026-02-18T15:43:51Z and environment_url equal to the original QR destination. Earlier successful workflow runs also exist.

Conclusion: the historical deployment was successful, but there is no active Pages site now. This verifies the current cause of the unavailable destination; it does not establish the event that removed/disabled Pages. Privacy/plan changes are possible but unproven. No settings were changed and nothing was published.

## Implementation

Shared static generator, employee data file, original photo and logo, mobile layout, prominent Save Contact/Call/Text/Email links, native saving guidance with no false success message. Jordan at the legacy root and the stable employee path. Generated vCards use CRLF, escaped values and UTF-8 line folding. Build emits only public site assets to `dist/`.

## Verification

Build and JavaScript syntax checks pass. Three automated tests pass: confirmed contact fields and omitted unconfirmed fields; vCard escaping/UTF-8 line folding; equivalent root/employee routes and correct Text action with no old placeholders. Browser results are recorded in SESSION-NOTES.md.

No TypeScript typecheck applies. iPhone/Android contact importing, phone app handoffs, live hosting and printed QR scans remain unverified. Print QR files intentionally await a verified live destination. Next gate: Jordan reviews the design and confirms the repository portrait is the intended photograph, then approves publication/restoration.

## Stronger visual direction — review pending

The sparse initial design is superseded for review by a substantial red identity header, large circular original portrait, bold name, prominent JRJ logo and dark Save Contact action. Confirmed website/address remain included. No thin decorative top stripe. Build/lint/tests and narrow-phone browser checks pass; no publication or actual phone import validation.

## Phone-height revision

Removed redundant format labels/footer and compacted the layout. Realistic viewport captures at 390x740 and 375x667 show all primary actions before scrolling. At 390x740 the page is 844px tall; address and instructions need a short scroll. Build/lint/3 tests pass; actual mobile device verification remains pending.

## 2026-09-08 separate Option B
Preserved the red-header card at /Card/. Added /Card/option-b/ with white logo area, side-by-side original portrait and name, red Save Contact, compact action row and grouped details with a deliberate two-line address. Shared employee data and vCard retained. Build/lint/3 tests pass. At 390x740 all details and instructions label are visible; total height 744px. At 320px no horizontal overflow and actions end at 405px. Browser images and action links verified; no errors reported. Actual phone importing and design approval remain pending. Not published.


## 2026-09-08 publishing plan gate
Option B promoted to main local routes; Pages workflow prepared. Build/lint/3 tests and browser check pass. GitHub refused Pages creation with HTTP 422 because the plan does not support this private repository. No visibility change or publication. Requires explicit public-repository or eligible-plan decision. Original QR is not yet live.


## 2026-09-08 LIVE release
Jordan explicitly authorized public Card visibility and publishing. Pages enabled; release 0854832 deployed successfully in workflow 34283806473. Root and employee routes, styles, images and vCard return HTTP 200. Live phone-sized browser shows correct Option B, loaded images, correct action links and no overflow/errors. Print SVG/740px PNG created with four-module margin; independent decoder confirms original root URL. Actual phone contact imports and printed scans remain pending; existing QR destination preserved. No paid service or new domain.


## 2026-09-08 contact portrait fix
Jordan confirmed iPhone contact saving works but reported missing photo. Download previously omitted PHOTO. Embed original portrait bytes as vCard 3.0 PHOTO;ENCODING=b;TYPE=JPEG (RFC 2426 section 3.1.4), with CRLF line folding. Save link versioned to avoid reuse of cached text-only file. Build/lint and four tests pass, including decoding the generated photo and comparing exact source bytes. Publishing authorized; actual iPhone photo import retest remains pending.


## 2026-09-08 iPhone photo import confirmed
Jordan checked the actual saved contact and confirmed the portrait works. The preceding missing-photo report applied to the import preview, not the saved contact. Release eae7757 accepted for this iPhone photo-import test; no further code change needed. Android and printed proof scans remain unverified.


## 2026-09-08 end-of-day closeout
Jordan requested closeout and will provide the remaining employee names tomorrow. Current accepted state: Option B live at original /Card/ URL; iPhone saved contact including portrait confirmed by Jordan. QR SVG/PNG available in print/. No further deployment needed. Next session: collect each employee's approved name, title, email, mobile and portrait; confirm shared website/address; create frozen slugs and verify before publishing. Android and print-proof scans remain pending. No new tests run for documentation-only closeout; previous build/lint/four tests and live checks passed.

