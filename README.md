# JRJ Construction digital business cards

Static, shared employee cards intended for the existing GitHub Pages project. No subscriptions, tracking, external fonts, runtime dependencies, or backend. Public content comes only from details Jordan explicitly supplied and the inspected repository assets; never copy vault content into cards.

## Local preview

Requires Node.js 20 or later. Run `npm run build`, `npm test`, then `npm run preview`. Open http://127.0.0.1:4173/Card/. The server binds only to this computer. Generated deployment files live in `dist/`; deploy that folder, never the repository root. `npm run lint` checks JavaScript syntax. There is no TypeScript or separate typecheck.

## Add or update an employee

1. Add the approved original portrait to the repository, using a simple filename such as `alex-smith.jpg`. Do not regenerate a person's face. Images are visually cropped with CSS; source files remain untouched.
2. Add an entry to `employees.json`, following Jordan's record. Use a unique, lowercase hyphenated slug, confirmed first/last name, title, company, email, E.164 phone and display phone. `photoPosition` controls the crop in percentages.
3. Run build, lint, and tests. Inspect the new `/<slug>/` page at narrow and wide widths and open its `.vcf`. Confirm the employee authorized all public details.
4. Review the generated files before publishing through GitHub Pages. Deploy only a fresh `dist/`. Before rebuilding after removing an employee, remove the old `dist/` directory so obsolete cards cannot survive in the deployment output.

`styles.css` and `scripts/build.mjs` provide the shared design. Employee data generates both HTML and vCard files, avoiding contact-detail drift. Cards work without JavaScript. Contact file fields include name, company, title, mobile phone, and work email. Optional `website` and structured `address` fields populate both the page and vCard. Jordan confirmed https://jrjinc.com/ and 1140 SW Ric Williamson Memorial Hwy, Weatherford, TX 76088 on September 8. Address objects use street, city, region, postalCode and optional country; never guess missing details.

## Permanent links and QR policy

- Jordan's original printed QR destination stays `https://jrjonesalb-collab.github.io/Card/`. The root must always show Jordan's card, not an employee directory. `/Card/jordan-jones/` is an equivalent secondary route.
- New employees get `https://jrjonesalb-collab.github.io/Card/<slug>/`. Freeze slugs after printing. Update the data behind a link instead of changing the URL. Do not reuse a former employee's slug for someone else; use an approved retired-card notice when necessary.
- Keep repository owner and `Card` repository name unchanged if preserving existing QR codes.
- Generate print QR files after HTTPS destination verification; proof on an actual phone before a print run. Encode the permanent page URL, never the `.vcf` or localhost. Export black-on-white SVG plus high-resolution PNG, preserve at least a four-module quiet zone, avoid decorative logos over modules, and test the actual printed size. QR codes here are ordinary static codes and need no paid service.

## Live hosting

Published September 8, 2026 at https://jrjonesalb-collab.github.io/Card/ using the approved Option B design. Jordan explicitly approved making Card public after GitHub refused Pages on the private repository under the current plan. No new domain or paid service was introduced.

The workflow in .github/workflows/pages.yml builds, checks and tests a fresh checkout, then deploys only dist/. Pushing main publishes changes automatically; verify changes locally before pushing. Initial release: 0854832, successful workflow run 34283806473. Root, employee route, images, CSS and vCard returned HTTP 200; live phone-sized browser had no overflow or errors.

Print assets are in print/; the PNG was independently decoded to the permanent root URL. Existing printed QR codes already use this URL and need no replacement. Actual phone importing and printed proof scans remain pending.

## Actual phone acceptance checks

- iPhone Safari: scan original QR with Camera, check portrait and action visibility; Save Contact should open/download the vCard; complete Create New Contact/Add to Existing Contact and confirm fields in Contacts.
- Android Chrome: scan QR, open downloaded vCard in Contacts, choose account if asked, save and confirm fields. Check downloaded-file fallback and duplicate/merge behavior.
- On both: Call opens the dialer with `+18179910339`; Text opens a composer with that recipient; Email opens a composer for `jjones@jrjinc.com`. Do not send or place calls during automated testing.
- Check large text, keyboard focus, portrait/landscape, and actual print scans. Desktop browser checks do not prove native phone handoffs or contact persistence.

## Selected design

Option B is now the shared main design in styles.css. The /Card/option-b/ review alias remains available; it is not a new QR destination. Future design edits should update styles.css and option-b.css together while the alias exists.

Contact files now embed the original employee portrait as inline vCard 3.0 PHOTO data (https://www.rfc-editor.org/rfc/rfc2426#section-3.1.4). CSS crop is page-only; contact apps control photo framing. Jordan confirmed basic iPhone contact saving on September 8; photo-import retest remains pending.


## Employee batch — September 9
Piper Wise, Chris Bryan and Kyle Vick are live at their permanent slug routes. Public image/title sources are in ASSET-SOURCES.md; emails and mobile numbers were confirmed by Jordan. Optional photoScale controls CSS framing. Email may be omitted for local drafts, but confirm it before releasing a complete card. Run python scripts/make-qr.py followed by selected slugs to generate print assets after live verification. New employee phone imports still need actual device checks; Jordan's iPhone import with photo is confirmed.


## Additional company branding
An employee can set logo (asset filename), logoWidth (60–200 pixels), accent and accentHover (six-digit hex colors). Defaults retain JRJ branding. Copy the supplied logo into the repository. Title can be omitted while awaiting confirmation. Tom Allen's GSW draft is pending title confirmation and publication.

Optional webPhoto selects a display-only derivative; photo remains the original embedded in the vCard. Tom uses a 528x704 Lanczos-resized JPEG, quality95, without retouching.
