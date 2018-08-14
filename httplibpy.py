#coding:utf8
import httplib
httplib.HTTPConnection.debuglevel=1
import urllib

feedData = urllib.urlopen('http://local.tp5.com').read()