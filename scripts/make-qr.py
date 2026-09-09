"""Generate print assets only after verifying the permanent HTTPS destination."""
import sys
from pathlib import Path
import urllib.request
import json
sys.path.insert(0, str(Path('artifacts/qr-runtime').resolve()))
import qrcode
import qrcode.image.svg
import zxingcpp
from PIL import Image

people = json.loads(Path('employees.json').read_text(encoding='utf-8'))
selected = set(sys.argv[1:]) or {p['slug'] for p in people}
assert selected <= {p['slug'] for p in people}, 'Unknown employee slug'
for p in people:
    if p['slug'] not in selected:
        continue
    url = 'https://jrjonesalb-collab.github.io/Card/' + ('' if p['slug'] == 'jordan-jones' else p['slug'] + '/')
    with urllib.request.urlopen(url) as response:
        html = response.read().decode()
        assert response.status == 200 and p['firstName']+' '+p['lastName'] in html and p['phone'] in html
        assert not p.get('email') or p['email'] in html
    out = Path('print'); out.mkdir(exist_ok=True)
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=20, border=4)
    qr.add_data(url); qr.make(fit=True)
    png = out / (p['slug']+'-qr.png')
    qr.make_image(fill_color='black', back_color='white').save(png, dpi=(600,600))
    qr.make_image(image_factory=qrcode.image.svg.SvgPathImage).save(out / (p['slug']+'-qr.svg'))
    decoded = zxingcpp.read_barcode(Image.open(png))
    assert decoded and decoded.text == url, 'QR decode mismatch'
    print(f'QR verified: {decoded.text}; PNG {Image.open(png).size}; four-module quiet zone; 600 dpi metadata')
