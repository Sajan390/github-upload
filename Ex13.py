#  Extracting Data from XML

# In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py.
# The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data,
# compute the sum of the numbers in the file.
# We provide two files for this assignment.
# One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

#     Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
#     Actual data: http://py4e-data.dr-chuck.net/comments_418763.xml (Sum ends with 47)

# You do not need to save these files to your folder since your program will read the data directly from the URL.
# Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.

import xml.etree.ElementTree as et
import ssl
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

api_key = False

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter - ')
print('Retrieving',address)
fhand=urllib.request.urlopen(address,context=ctx).read()


g=fhand.decode()
tree = et.fromstring(g)
counts = tree.findall('.//count')

print('Retrieved',len(g),'characters')
print('Count',len(counts))
s=0
for line in counts:

    s+=int(line.text)
print('Sum',s)




