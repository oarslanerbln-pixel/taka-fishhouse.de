import cv2
import numpy as np

img_path = r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\qr-menu\QR_Taka_Menu_Premium.png"
img = cv2.imread(img_path)

if img is not None:
    detector = cv2.QRCodeDetector()
    data, bbox, straight_qrcode = detector.detectAndDecode(img)
    if data:
        print("QR BARKOD ICINDEKI URL:", data)
    else:
        # Let's try PyZbar as fallback if installed
        try:
            from pyzbar.pyzbar import decode
            decoded = decode(img)
            if decoded:
                print("QR BARKOD (PyZbar):", decoded[0].data.decode('utf-8'))
            else:
                print("QR Kod coZulemedi (Pyzbar bos dondu).")
        except:
            print("QR Kod OpenCV ile cozulemedi ve pyzbar yok.")
else:
    print("QR Resim dosyasi bulunamadi.")
