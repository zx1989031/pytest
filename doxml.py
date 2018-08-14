#conding:utf8
#/usr/bin/python
#fileName:doxml.py
from xml.dom import minidom
xmldoc = minidom.parse('./binary.xml')
# print xmldoc.toxml()
content = xmldoc.firstChild.toxml()
# print content
grammarNode = xmldoc.firstChild
print grammarNode

pnode = grammarNode.childNodes[0]
print pnode.childNodes[0].data

