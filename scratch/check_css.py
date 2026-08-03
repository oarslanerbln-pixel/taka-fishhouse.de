data = open('qr-menu/assets/css/menu-page.css', 'r', encoding='utf-8').read()
tail = data[-3000:]
with open('scratch/css_tail.txt', 'w', encoding='utf-8') as f:
    f.write(tail)
print("Written tail to scratch/css_tail.txt")
print("Total CSS length:", len(data))
# Check if object-position exists
if 'object-position' in data:
    print("object-position FOUND in CSS")
    idx = data.find('object-position')
    print("Context:", data[idx-100:idx+200])
else:
    print("object-position NOT FOUND in CSS - needs to be added")
