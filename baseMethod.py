#encoding: utf-8
#!/usr/bin/python
#Filename baseMethod.py
import types
class test:
    def __init__(self):
        print 1


testfunction = lambda x,y:x+y

print reduce(testfunction,[1,2,3,4,5,6,7,8,9,10])

testint = 1
teststring = '1'
testclass = test()


print type(testclass)
print type(testfunction)
print type(testint)
print type(teststring)
hello='hellos'
testzuples = ('hello',)#加逗号表示元组，不加表示字串

print type(testzuples)
print testzuples
print testzuples[0]