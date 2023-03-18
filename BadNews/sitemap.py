import requests
from bs4 import BeautifulSoup as bs

sitemap_url = 'https://btvnovinite.bg/lbin/v3/sitemap.php'

r = requests.get(sitemap_url)
print(r)
if r.status_code == 200:
    html = r.text
    # print(html)

    links = []
    soup = bs(html, 'lxml')
    # links = [f"{l.text.replace('\n', "")}" for l in soup]
    for l in soup:
        links.append(l.text.replace('\n', ""))
        # print(l.text)
    # print(soup.text)
    print(links)


