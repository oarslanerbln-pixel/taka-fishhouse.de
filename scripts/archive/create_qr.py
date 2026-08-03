import qrcode
import os

target_url = "https://taka-fisch-haus.vercel.app/qr-menu/"
artifact_path = r"c:\Users\oarsl\.gemini\antigravity-ide\brain\0ef7b752-cec1-4f33-8c81-3f6f4460c05e\taka_yeni_qr_kod.png"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data(target_url)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save(artifact_path)
print("Yeni QR kod artifact olarak uretildi:", artifact_path)
