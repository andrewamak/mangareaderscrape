#downloads manga from mangareader.net

import bs4 as bs
import urllib
import requests
from urllib.request import Request, urlopen
import os
headers = requests.utils.default_headers()

my_path = "C:\\Users\Andy\\Desktop\\" + 'asdf'

c = 1
p = 1


url = 'https://www.mangareader.net/kengan-ashua/' + str(c) + '/' + str(p)

req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
response = requests.get(url, headers=headers)
html = response.text
soup = bs.BeautifulSoup(html, 'html.parser')

for links in soup.find_all('img'):
    img_src = links.get("src")
    img_name = img_src[:-11]
    #print(img_src)
    with open(img_src,'wb') as f:
        f.write(r.content)
