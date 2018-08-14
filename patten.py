#coding:utf8
#/usr/bin/python
#fileName:patten.py 正则测试
import re

patten1 = "^[a-zA-Z]{2}"
patten2 = "[a-z]+"
patten3 = "[A-Z]+"
patten4 = "[0-9]+"
def checkio(password):
    print str(re.search(patten1,password))
    print str(re.search(patten2,password))
    print str(re.search(patten3,password))
    print str(re.search(patten4,password))


password='Aaa123123abc'
checkio(password)

import re
def checkio(password):
    patten1 = str(re.search("^[a-zA-Z]{2}",password))
    patten2 = str(re.search("[a-z]+",password))
    patten3 = str(re.search("[A-Z]+",password))
    patten4 = str(re.search("[0-9]+",password))
    #print(str(patten1)=='None')
    if(len(password)<6):
        #return '密码长度小于6位'
        return 'false'
    elif len(password)>65:
        #return "长度不能大于10"
        return 'false'
    elif patten1=='None':
        #return '密码必须包含大小写字母和数字'
        return 'false'
    elif patten2=='None':
        #return '密码必须包含大小写字母和数字'
        return 'false'
    elif patten3=='None':
        #return '密码必须包含大小写字母和数字'
        return 'false'
    elif patten4=='None':
        return 'false'
    else:
        return 'true'

if __name__ == '__main__':
    name = '1231111a1'
