import xml.etree.ElementTree as ET

# Parsing an XML string or file
tree = ET.parse('/home/mirafra/Desktop/python_learnings/data.xml')
root = tree.getroot()

# Accessing data
for child in root:
    print(child.tag, child.attrib)

# Finding specific elements
for email in root.iter('email'):
    print(email.text)