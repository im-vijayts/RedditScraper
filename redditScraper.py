import urllib
from urllib import request
from bs4 import BeautifulSoup as bs
import datetime
import re

url = 'https://www.reddit.com/r/python/'

link = urllib.request.urlopen(url)
soupMade = bs(link, "html.parser")

scriptTag = soupMade.findAll("script")

scriptStr = str(scriptTag[6]).replace('\\u0026', '&')
mediaList = scriptStr.split('"')

imgURL = [i for i, e in enumerate(mediaList) if e == "url"]
imgURL = tuple(imgURL)

rex = 'https://preview\.redd\.it/(.*)\.jpg\?auto=webp\&(.*)'

url_links = list()	
for i in imgURL:
    if re.search(rex, mediaList[i+2]):
        url_links.append(mediaList[i+2].replace("\\u0026","&"))

with open('links.txt', 'w') as fp:
    for i in url_links:
        fp.write(str(i))
        fp.write('\n')