import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
fhand=urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
for lines in fhand:
    wored=lines.decode().strip()
    print(wored)
