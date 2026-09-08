# Jordan Jones QR print files

Destination: https://jrjonesalb-collab.github.io/Card/

The same permanent destination as the original printed QR. Existing QR codes do not need replacing.

- `jordan-jones-qr.svg`: scalable vector master. Place at 30 mm square or larger for initial proofing, preserving the entire white margin. The SVG has a transparent background; place it on solid white.
- `jordan-jones-qr.png`: high-resolution black-on-white raster with 600 dpi metadata and four-module quiet zone. Do not crop, recolor, stretch or overlay a logo.
- Source: `scripts/make-qr.py` (qrcode, Pillow, zxing-cpp). Generation checks the live destination and decodes the PNG independently to confirm the exact URL.

Live HTTPS destination and digital PNG decoding verified September 8, 2026. Actual printed proof scans and iPhone/Android contact importing still require a device test before a print run. Size is a starting recommendation, not a guarantee for every printer/material.
