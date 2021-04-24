import urllib.request, urllib.parse, urllib.error

from bs4 import BeautifulSoup
fhand=urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
counts={}
for line in fhand:
    word=line.decode().split()
    for words in word:
        counts[words]=counts.get(words,0)+1
        print(words)
print(counts)
