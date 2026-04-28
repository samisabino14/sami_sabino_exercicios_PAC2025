import requests
import  re
from datetime import datetime
#baseUrl = 'https://www.w3schools.com'
#baseUrl = 'https://pathfinder.w3schools.com/'
#baseUrl = 'https://www.amazon.es/'
#baseUrl = 'https://www.canva.com/settings/your-account'
baseUrl = 'https://pathfinder.w3schools.com/_next/static/chunks/webpack-737a62c8851aed7d.js'

headers = {
    "User-Agent": "Uso académico e formativo"
}

response = requests.get(baseUrl, headers)

siteTitle = re.search("<title>(.*?)</title>", response.text, re.IGNORECASE)
#siteLinks = re.findall(r'<a[^>]*href=["\'](.*?)["\']', response.text, re.IGNORECASE)
standard = re.compile(
    r'(?:href|src|action)\s*=\s*["\']([^"\']+)["\']',
    re.IGNORECASE
)

matches = standard.findall(response.text)

siteLinks = []


#print(siteTitle[1])
print()
print("\nLinks encontrados: ", datetime.now())

#for link in matches:
#    if link.startswith("/"):
#        print("\n", {
#            "Link relativo: ": link,
#            "Completo": baseUrl + link
#        })
#    else:
#        print("\nLink normal: ", link)
