import urllib.request
import urllib.error

urls = [
    "https://imageproxy.wolt.com/assets/69a80af27d25f60394a12d3d",
    "https://wolt-menu-images-cdn.wolt.com/menu-images/5f96f0713ecde1f8e087069e/0211094c-17a7-11eb-8056-b6507305cae7_cocacola_0_2.jpeg"
]

for url in urls:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(req, timeout=3)
        print(f"{url} - {response.status}")
    except urllib.error.HTTPError as e:
        print(f"{url} - HTTP {e.code}")
    except Exception as e:
        print(f"{url} - Error: {e}")
