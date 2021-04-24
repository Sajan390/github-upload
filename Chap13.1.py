import xml.etree.ElementTree as ET
data = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>'''

tree = ET.fromstring(data)
last=tree.findall('users/user')
print('User Count : ',len(last))

for item in last:
    print('Name',item.find('name').text)
    print('Id', item.find('id').text)
    print('Attr', item.get("x"))
    