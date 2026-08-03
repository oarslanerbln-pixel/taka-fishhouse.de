import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import SolidFillColorMask

url = "https://qr-menu-two-delta.vercel.app"

qr = qrcode.QRCode(
    version=5,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=30,
    border=2,
)
qr.add_data(url)
qr.make(fit=True)

# Gold dots on a dark background for maximum premium feel
img = qr.make_image(
    image_factory=StyledPilImage,
    module_drawer=RoundedModuleDrawer(),
    color_mask=SolidFillColorMask(front_color=(212, 175, 55), back_color=(17, 17, 17))
)

img.save("QR_Taka_Menu_Premium.png")
