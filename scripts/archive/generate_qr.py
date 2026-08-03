import subprocess, sys

# Install dependencies
subprocess.run([sys.executable, '-m', 'pip', 'install', 'qrcode', 'Pillow', '-q'], check=True)

import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer, GappedSquareModuleDrawer
from qrcode.image.styles.colormasks import SolidFillColorMask
from PIL import Image, ImageDraw, ImageFont
import os

# QR Configuration
URL = "https://taka-fisch-haus.vercel.app/qr-menu/"
OUTPUT_PATH = r"qr-menu\QR_Taka_Menu_Premium.png"

# Colors (matching the existing gold-on-black design)
BG_COLOR = (15, 15, 15)       # near-black
FG_COLOR = (212, 175, 55)     # gold #D4AF37

qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=14,
    border=3,
)
qr.add_data(URL)
qr.make(fit=True)

img = qr.make_image(
    image_factory=StyledPilImage,
    module_drawer=RoundedModuleDrawer(),
    color_mask=SolidFillColorMask(
        back_color=BG_COLOR,
        front_color=FG_COLOR
    )
)

# Save
img.save(OUTPUT_PATH)
print(f"QR saved to: {OUTPUT_PATH}")
print(f"URL encoded: {URL}")
print(f"Size: {img.size}")
