import sys
import subprocess

try:
    import cv2
except ImportError:
    subprocess.run([sys.executable, '-m', 'pip', 'install', 'opencv-python-headless', '-q'], check=True)
    import cv2

image_path = r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\qr-menu\QR_Taka_Menu_Premium.png"

img = cv2.imread(image_path)
if img is not None:
    detector = cv2.QRCodeDetector()
    data, bbox, straight_qrcode = detector.detectAndDecode(img)
    if data:
        print(f"DECODED QR DATA: {data}")
    else:
        print("Could not decode QR code.")
else:
    print("Could not load image.")
