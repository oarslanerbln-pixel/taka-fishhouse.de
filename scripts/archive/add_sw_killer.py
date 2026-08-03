import os
import re

def add_sw_killer(filepath):
    if not os.path.exists(filepath): return
    with open(filepath, 'r', encoding='utf-8') as f:
        c = f.read()
        
    killer_script = '''
    <script>
      if ('serviceWorker' in navigator) {
        navigator.serviceWorker.getRegistrations().then(function(registrations) {
          for(let registration of registrations) {
            registration.unregister();
          }
        });
        
        // Hard reload if coming from an old cache
        if (document.cookie.indexOf('cache_cleared=1') === -1) {
            document.cookie = "cache_cleared=1; max-age=86400; path=/";
            window.location.reload(true);
        }
      }
    </script>
    '''
    
    if "registration.unregister()" not in c:
        c = c.replace("</head>", killer_script + "\n</head>")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(c)

add_sw_killer(r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\index.html")
add_sw_killer(r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\menu.html")
add_sw_killer(r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\qr-menu\index.html")
