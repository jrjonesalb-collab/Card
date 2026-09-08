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
- Generate print QR files only after HTTPS destination verification and phone scan tests. Encode the permanent page URL, never the `.vcf` or localhost. Export black-on-white SVG plus high-resolution PNG, preserve at least a four-module quiet zone, avoid decorative logos over modules, and test the actual printed size. QR codes here are ordinary static codes and need no paid service.

## Hosting restoration — pending design approval

See `MILESTONE-1.md` for observed evidence. GitHub reports both repositories private with `has_pages:false`. Card has historical successful Pages deployments, but no active Pages site today. No repository visibility or Pages settings were changed.

After design approval, inspect account eligibility for Pages on a private repository. GitHub Free supports Pages from public repositories; private repository Pages requires an eligible paid plan. Do not purchase a plan or make the existing repository public without discussing it. If the existing account is eligible, prefer restoring Pages in `Card` with GitHub Actions uploading only `dist/` using the official Pages actions. Gate the first deployment on explicit approval; no deployment workflow is installed yet.

Once approved: build and validate; configure Pages; deploy `dist/`; verify root and employee route return HTTP 200, images/CSS load, contact downloads are correct, and original QR scans to Jordan. Only then release print QR assets. This repository's root source is a generator project, so branch-root Pages publishing is not appropriate.

## Actual phone acceptance checks

- iPhone Safari: scan original QR with Camera, check portrait and action visibility; Save Contact should open/download the vCard; complete Create New Contact/Add to Existing Contact and confirm fields in Contacts.
- Android Chrome: scan QR, open downloaded vCard in Contacts, choose account if asked, save and confirm fields. Check downloaded-file fallback and duplicate/merge behavior.
- On both: Call opens the dialer with `+18179910339`; Text opens a composer with that recipient; Email opens a composer for `jjones@jrjinc.com`. Do not send or place calls during automated testing.
- Check large text, keyboard focus, portrait/landscape, and actual print scans. Desktop browser checks do not prove native phone handoffs or contact persistence.

## Design comparison
Current red-header option: /Card/. Separate white composition: /Card/option-b/. Option B uses option-b.css and scripts/option-b.mjs, reusing generated employee content and vCard; comparison route is for review and is not a new permanent QR destination.

