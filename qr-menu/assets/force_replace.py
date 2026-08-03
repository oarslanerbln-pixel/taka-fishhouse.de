import codecs
import re

MENU_JS = r'c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\qr-menu\assets\js\menu-data.js'

with codecs.open(MENU_JS, 'r', 'utf-8') as f:
    content = f.read()

replacements = {
    '"image": "assets/havuc_tarator_ai.png",': '"image": "assets/ubereats_imgs/tarator.jpg",',
    '"image": "assets/antepe_ezmesi_ai.png"': '"image": "assets/ubereats_imgs/scharfes_paprikap_ree.jpg"',
    '"image": "assets/kopoglu_ai.png",': '"image": "assets/ubereats_imgs/k_poglu.jpg",',
    '"image": "assets/narli_dibariye_ai.png"': '"image": "assets/ubereats_imgs/narli_dilberiye.jpg"',
    '"image": "assets/ahtapot_salatasi_ai.png",': '"image": "assets/ubereats_imgs/gegrillter_oktopus.jpg",',
    '"image": "assets/humus.png"': '"image": "assets/ubereats_imgs/hummus.jpg"'
}

for old, new in replacements.items():
    content = content.replace(old, new)

with codecs.open(MENU_JS, 'w', 'utf-8') as f:
    f.write(content)

print("Forced replacement of AI images completed.")
