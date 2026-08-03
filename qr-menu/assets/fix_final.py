import codecs

MENU_JS = r'c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\qr-menu\assets\js\menu-data.js'
with codecs.open(MENU_JS, 'r', 'utf-8') as f:
    c = f.read()

c = c.replace('assets/pastirmali_ahtapot_1781257158550.png', 'assets/ubereats_imgs/oktopus_mit_speck.jpg')
c = c.replace('assets/patlicanli_balik_1781257218087.png',  'assets/ubereats_imgs/fisch_auf_auberginenp_reebett.jpg')
c = c.replace('assets/pastirmali_humus_1781257187585.png',  'assets/ubereats_imgs/hummus_mit_speck.jpg')

with codecs.open(MENU_JS, 'w', 'utf-8') as f:
    f.write(c)

print('Replaced 3 AI images with UberEats originals.')
