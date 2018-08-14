#coding:utf8
import urllib
import re
data = urllib.urlopen('http://www.baidu.com').read()
text = "string head"
print text[text.find('head'):]

pattern = "<title>(.*)</title>"

# print data
print data.find('head')

print re.search(pattern,data).group(1)

