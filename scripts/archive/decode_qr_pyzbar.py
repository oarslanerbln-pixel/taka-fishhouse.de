import sys
import subprocess

try:
    from pyzbar.pyzbar import decode
    from PIL import Image
except ImportError:
    subprocess.run([sys.executable, '-m', 'pip', 'install', 'pyzbar', 'Pillow', '-q'], check=True)
    from pyzbar.pyzbar import decode
    from PIL import Image

image_path = r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\qr-menu\QR_Taka_Menu_Premium.png"

try:
    img = Image.open(image_path)
    decoded_objects = decode(img)
    if decoded_objects:
        for obj in decoded_objects:
            print(f"DECODED QR DATA: {obj.data.decode('utf-8')}")
    else:
        print("Could not decode QR code with pyzbar either.")
except Exception as e:
    print(f"Error: {e}")
