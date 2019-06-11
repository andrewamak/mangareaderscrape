#downloads manga from mangareader.net

import bs4 as bs
import urllib
import shutil
#downloads manga from mangareader.net

import bs4 as bs
import urllib
import requests
from urllib.request import Request, urlopen
import os
headers = requests.utils.default_headers()


c = 1
p = 1
count = 1

url = 'https://www.mangareader.net/highschool-dxd'
url2 = url

if url[-1] != '/':
    url = url + '/'
else:
    pass

#making the directory to put the images in
dir_name = url.split('/')[3]
path = '/home/andy/Desktop/' + dir_name
#path = '/home/andy/Desktop/kengan-ashura'
os.mkdir(path)


print('Loading images...')

while True:
    url = url2 + '/' + str(c) + '/' + str(p)
    print(url)

    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    response = requests.get(url, headers=headers)

    if response.status_code == 404:
        c += 1
        p = 1
    else:
        pass
    html = response.text
    soup = bs.BeautifulSoup(html, 'html.parser')


    for links in soup.find_all('img'):
        img_src = links.get("src")
        #img_name = img_src[:-11]
        #print(img_src)

        opener = urllib.request.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib.request.install_opener(opener)
        urllib.request.urlretrieve(img_src, path + '/' + dir_name + "-" + str(c) + '-' + str(p))
        p += 1
        count += 1

print('Done')
