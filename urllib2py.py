#coding:utf8
import httplib
import urllib2


httplib.HTTPConnection.debuglevel=1
# http://zs-test.chaojue.org.cn/ 报304
# request = urllib2.Request('http://zs-test.chaojue.org.cn/')
request = urllib2.Request('http://zs-admin.1989031.com/')
opener = urllib2.build_opener()
feedData = opener.open(request).read()
firstDataStream = opener.open(request)

# request.add_header('If-Modified-Since',firstDataStream.headers.get('Last-Modified'))

# twodatastream = opener.open(request)

print firstDataStream.headers.dict


class DefaultErrorHandler(urllib2.HTTPDefaultErrorHandler):
    def http_error_default(self, req, fp, code, msg, headers):
        result = urllib2.HTTPError(req.get_full_url,code,msg,headers,fp)
        result.status = code
        return result

class SmartDriectHandler(urllib2.HTTPRedirectHandler):
    def http_error_301(self,req,fp,code,msg,headers):
        result = urllib2.HTTPRedirectHandler.http_error_301(self,req,fp,code,msg,headers)
        result.status = code
        return result

    def http_error_302(self,req,fp,code,msg,headers):
        result = urllib2.HTTPRedirectHandler.http_error_302(self,req,fp,code,msg,headers)
        result.status = code
        return result

request.add_header('Accept-encoding','gzip')

opener = urllib2.build_opener(SmartDriectHandler)


threeDataStream = opener.open(request)
print threeDataStream.headers
compressedData = threeDataStream.read()

print len(compressedData)

import StringIO
import gzip

compressedStream = StringIO.StringIO(compressedData)
gzipPer = gzip.GzipFile(fileobj=compressedStream)
# data = gzipPer.read()
# print data