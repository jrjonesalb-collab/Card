# Milestone 2 — employee batch, September 9, 2026

Local drafts for Piper Wise, Chris Bryan and Kyle Vick use the approved shared design, user-supplied mobile numbers, and public JRJ team-page titles/portraits. See ASSET-SOURCES.md. Individual emails await Jordan; drafts omit email controls. Not published.

Build, syntax checks and five tests pass; phone browser checks pass. Contact photos embed JPEG copies of the website originals. Actual phone importing for these employees remains untested. Jordan's existing live root and QR remain unchanged.

## 2026-09-09 employee batch ready to publish
Jordan confirmed pwise@jrjinc.com, cbryan@jrjinc.com and kvick@jrjinc.com. All three cards now include Email and work-email vCard fields. Build/lint/five tests pass, including per-employee phone, email and embedded-image verification. Permanent paths: /Card/piper-wise/, /Card/chris-bryan/, /Card/kyle-vick/. Device imports and print proof checks remain pending.


## 2026-09-09 employee batch LIVE
Release e63b558 deployed successfully in workflow 34372537535. Piper Wise, Chris Bryan and Kyle Vick live pages and vCards returned 200; email/phone and all embedded JPEG bytes match confirmed records. Jordan root also reverified. Per-employee SVG/820px PNG QR files generated and independently decoded to permanent routes. Build/lint/five tests passed locally and in CI; prior mobile layouts passed. Actual phone imports and physical print scans remain pending. CI emitted a non-blocking legacy-action Node runtime warning; deployment succeeded.


## 2026-09-09 blueprint QR concept
Created a separate blueprint-style QR example for Jordan using deterministic vector/raster drawing: navy grid, dimension marks, title block and intact QR quiet zone. Output print/concepts/jordan-blueprint-qr.svg and .png, source scripts/blueprint-qr.py. PNG independently decoded at 1000/600/400px to the original /Card/ URL. SVG visually mirrors PNG but not independently rendered/decoded. Concept only; no site changes. Actual phone/print scan and design acceptance pending. No site tests rerun because site code is unchanged.

