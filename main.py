import requests
import urllib.request
from bs4 import BeautifulSoup

import ssl

# This restores the same behavior as before.
context = ssl._create_unverified_context()


path = './html/results.html'

url = input('Please end link: ')
request = requests.get(url)
f = open(path, "wb")
f.write(request.content)

soup = BeautifulSoup(open(path,encoding="utf8"),features="html.parser")
hrefs = soup.select('p > a')

for href in hrefs:
    title = href.text   
    link = href.get('href')
    if('.pdf' in link or '.docx' in link):
        ext =  'pdf' if '.pdf' in link else 'docx'
        # urllib.request.urlretrieve(link,"./files/" + f'{title}.{ext}')

        r = requests.get(link, allow_redirects=True)

        open("./files/" + f'{title}.{ext}', 'wb').write(r.content)

        print("downloaded : " + title )
        break
