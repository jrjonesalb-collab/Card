"""Deterministic blueprint concept; preserve a standard QR and its quiet zone."""
import sys, html
from pathlib import Path
sys.path.insert(0, str(Path('artifacts/qr-runtime').resolve()))
import qrcode, zxingcpp
from PIL import Image, ImageDraw, ImageFont

out=Path('print/concepts');out.mkdir(parents=True,exist_ok=True)
W,H=1000,1240
navy='#12334c'; ink='#e5eef2'; muted='#91adbd'; grid='#21435a'
im=Image.new('RGB',(W,H),navy);d=ImageDraw.Draw(im)
svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',f'<rect width="{W}" height="{H}" fill="{navy}"/>']
def line(points,fill=muted,width=2):
    d.line(points,fill=fill,width=width)
    svg.append(f'<polyline points="'+ ' '.join(f'{x},{y}' for x,y in points)+f'" fill="none" stroke="{fill}" stroke-width="{width}"/>')
def rect(box,fill=None,stroke=None,width=1):
    d.rectangle(box,fill=fill,outline=stroke,width=width)
    x,y,x2,y2=box
    svg.append(f'<rect x="{x}" y="{y}" width="{x2-x}" height="{y2-y}" fill="{fill or "none"}" stroke="{stroke or "none"}" stroke-width="{width}"/>')
def text(x,y,s,size=22,fill=ink,bold=False,anchor='left'):
    font=ImageFont.truetype('C:/Windows/Fonts/'+('arialbd.ttf' if bold else 'consola.ttf'),size)
    dx=x if anchor=='left' else x-d.textlength(s,font=font)/2
    d.text((dx,y),s,font=font,fill=fill)
    svg.append(f'<text x="{x}" y="{y}" dominant-baseline="text-before-edge" text-anchor="{"middle" if anchor!="left" else "start"}" font-family="{"Arial" if bold else "Consolas,monospace"}" font-size="{size}" font-weight="{"700" if bold else "400"}" fill="{fill}">{html.escape(s)}</text>')
for x in range(40,961,24):line([(x,40),(x,1200)],grid,1)
for y in range(40,1201,24):line([(40,y),(960,y)],grid,1)
rect((40,40,960,1200),stroke=muted,width=2)
rect((64,64,936,178),fill=navy)
text(76,70,'JRJ',64,bold=True)
text(220,99,'CONSTRUCTION',25,bold=True)
text(923,82,'01',34,anchor='center')
text(76,151,'CONNECTION PLAN / JORDAN JONES',18,muted)
line([(64,190),(936,190)],muted,2)
url='https://jrjonesalb-collab.github.io/Card/'
qr=qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M,border=4,box_size=18)
qr.add_data(url);qr.make(fit=True)
matrix=qr.get_matrix();cell=18;side=len(matrix)*cell;x=(W-side)//2;y=260
# Opaque white includes the standard four-module quiet zone.
rect((x,y,x+side,y+side),fill='#ffffff')
for row,values in enumerate(matrix):
    for col,dark in enumerate(values):
        if dark:rect((x+col*cell,y+row*cell,x+(col+1)*cell-1,y+(row+1)*cell-1),fill=navy)
# Dimension lines live outside the entire white quiet zone.
line([(x,232),(x+side,232)])
for px in (x,x+side):
    line([(px,216),(px,248)])
    line([(px-7,239),(px+7,225)],ink,2)
rect((342,215,658,248),fill=navy)
text(500,218,'SCAN TO CONNECT',22,anchor='center')
line([(x-30,y),(x-30,y+side)])
for py in (y,y+side):
    line([(x-44,py),(x-16,py)])
    line([(x-37,py+7),(x-23,py-7)],ink,2)
# Drafting registration marks on the right, away from the code.
for cy in (y+36,y+side-36):
    cx=900;line([(cx-14,cy),(cx+14,cy)]);line([(cx,cy-14),(cx,cy+14)])
text(500,952,'A DIRECT CONNECTION. ONE SCAN.',19,anchor='center')
rect((64,1010,936,1176),fill=navy,stroke=muted,width=2)
line([(740,1010),(740,1176)])
text(84,1026,'CONTACT',14,muted)
text(84,1053,'Jordan Jones',37,bold=True)
text(84,1103,'Owner / Chief Innovation Officer',18)
text(84,1144,'JRJ CONSTRUCTION',16,muted)
text(764,1027,'DETAIL',15,muted)
text(764,1058,'01',52,bold=True)
text(764,1145,'JRJ / CONNECT',13,muted)
svg.append('</svg>')
(out/'jordan-blueprint-qr.svg').write_text('\n'.join(svg),encoding='utf-8')
im.save(out/'jordan-blueprint-qr.png',dpi=(300,300))
for width in (1000,600,400):
    proof=im.resize((width,round(H*width/W)),Image.Resampling.LANCZOS)
    result=zxingcpp.read_barcode(proof)
    assert result and result.text==url,f'QR failed at {width}px'
print('Blueprint QR decoded correctly at 1000, 600 and 400 pixels wide. Actual printed/device scan not yet tested.')
