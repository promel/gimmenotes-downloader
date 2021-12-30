import requests
import urllib.request
from bs4 import BeautifulSoup
import os

def checkAndCreateFolder(path):

    # Check whether the specified path exists or not
    isExist = os.path.exists(path)

    if not isExist:
        # Create a new directory because it does not exist 
        os.makedirs(path)
        print(f"The {path} directory is created!")

def checkExtension(link):
    for ext in ['.pdf','.docx','.zip']:
        if ext in link:
            return ext


htmlFolder = './html'
checkAndCreateFolder(htmlFolder)
path = f'{htmlFolder}/results.html'

url = input('Please end link: ')
request = requests.get(url)
f = open(path, "wb")
f.write(request.content)

soup = BeautifulSoup(open(path,encoding="utf8"),features="html.parser")
hrefs = soup.select('p > a')

filesFolder = './files'
checkAndCreateFolder(filesFolder)

for href in hrefs:
    title = href.text   
    link = href.get('href')
    ext = checkExtension(link)
    if(ext):
        r = requests.get(link, allow_redirects=True)
        filename = f'{title}{ext}'
        open(f'{filesFolder}/{filename}', 'wb').write(r.content)

        print("downloaded : " + filename )
