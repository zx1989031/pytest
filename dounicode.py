#conding:utf8
#/usr/bin/python
#fileName:dounicode.py
import StringIO
import sys
s = u'Dive in'
print s

z = u'/23x2\xf1a'
print z

content = 'the is string'

stringObj = StringIO.StringIO(content)

print stringObj.read()
stringObj.close()

#return file obj
def openAnythin(source):
    # try open with urllib(if source is http,ftp ,or file url)
    import urllib
    try:
        return urllib.urilopen(source)
    except(IOError,OSError):
        pass

    #try to open with native opent function (if source is pathname)
    try:
        return open(source)
    except(IOError,OSError):
        pass

    #treat souce as string
    import StringIO
    return StringIO.StringIO(str(source))


print 'dive in'
saveout = sys.stdout
fsock = open('out.log','w')
sys.stdout = fsock

print 'this message will be loggoed instead of displayed'
sys.stdout = saveout
fsock.close()