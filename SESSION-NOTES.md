# Session notes

## 2026-09-08 — design feedback

Removed the decorative red top border following Jordan's feedback. Added his explicitly confirmed https://jrjinc.com/ and 1140 SW Ric Williamson Memorial Hwy, Weatherford, TX 76088 as website and map-linked office rows, and as URL/structured ADR fields in the vCard. Shared data supports optional website/address for employees; omitted fields stay absent. Build, lint and all three updated tests pass. Preview only; device import and publishing remain pending.

## 2026-09-08 — first card preview

Built a shared static card system from the existing Card repository. Confirmed the original URL currently returns 404 and Pages is absent, despite a successful historical deployment. Kept all confirmed Jordan contact details in employees.json; omitted website/address. Inspected and retained the correct JRJ logo and unchanged repository portrait. Preview only; no publishing or Pages repairs.

Passed build, syntax checks, and 3 automated tests. Browser verified at 320px and 390px with no horizontal overflow, and visually reviewed at 390px and 1440px. Images load, root and employee routes render, instructions expand on click, and vCard fetch returns 200 with correct text/vcard MIME and fields. No browser errors reported. Initial screenshot failed because the artifacts directory was missing; creating it resolved that. A text-based automation locator missed the native disclosure; direct summary click verified it. Actual phone import and live QR checks remain pending. See README.md for maintenance and MILESTONE-1.md for hosting evidence.

## 2026-09-08 — stronger red-header design preview

Jordan found the first layout too plain and requested the proposed stronger direction. Added a substantial JRJ red identity area, larger original-photo circle, bold name, larger logo, dark Save Contact and tinted action buttons. Removed the small decorative rule. Confirmed contact information remains unchanged. Build, lint and three tests pass; browser checks show no errors, loaded images, no 320px overflow and 57px-or-larger action targets. Mobile and desktop previews inspected. Design approval and real-phone importing remain pending; nothing published.

## 2026-09-08 — realistic phone-height revision

Removed both Digital business card labels and the redundant footer. Reduced header, portrait and section spacing while retaining the red identity area. Build/lint/3 tests pass. Browser at 390x740: page height 844px, primary actions end at 489px, no horizontal overflow; address and saving instructions require a short scroll. At 375x667 all four actions remain visible. Screenshots show initial viewports, not full-page images. No browser errors; actual device checks remain pending.

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

