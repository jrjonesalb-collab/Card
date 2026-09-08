"""Generate print assets only after verifying the permanent HTTPS destination."""
import sys
from pathlib import Path
import urllib.request
sys.path.insert(0, str(Path('artifacts/qr-runtime').resolve()))
import qrcode
import qrcode.image.svg
import zxingcpp
from PIL import Image

url = 'https://jrjonesalb-collab.github.io/Card/'
with urllib.request.urlopen(url) as response:
    html = response.read().decode()
    assert response.status == 200 and 'Jordan Jones' in html and 'jjones@jrjinc.com' in html
out = Path('print'); out.mkdir(exist_ok=True)
qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=20, border=4)
qr.add_data(url); qr.make(fit=True)
png = out / 'jordan-jones-qr.png'
qr.make_image(fill_color='black', back_color='white').save(png, dpi=(600,600))
qr.make_image(image_factory=qrcode.image.svg.SvgPathImage).save(out / 'jordan-jones-qr.svg')
decoded = zxingcpp.read_barcode(Image.open(png))
assert decoded and decoded.text == url, 'QR decode mismatch'
print(f'QR verified: {decoded.text}; PNG {Image.open(png).size}; four-module quiet zone; 600 dpi metadata')
