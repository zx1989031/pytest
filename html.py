#conding:utf8
#/usr/bin/python
#fileName:html.py

import urllib
import re

htmlcontent = urllib.urlopen('https://baike.baidu.com/item/%E7%99%BE%E7%A7%91/29?fr=aladdin')
htmlsource = htmlcontent.read();
patten = '<meta(.*?)>'
meta = re.search(patten,htmlsource)
print meta.groups()
