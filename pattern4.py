#coding:utf8
#/usr/bin/python
#fileName:pattern1.py

def big_num(data):
    return sorted(data)

#被3整除 被5整除 被3和5整除 其它
def checkio(number):
    numberStr = str(number)
    if(number>1000 or number<0):
        return numberStr
    if(number%3==0 and number%5==0):
        numberStr = "Fizz Buzz"
    elif(number%3==0):
        numberStr= "Fizz"
    elif(number%5==0):
        numberStr = "Buzz"
    else:
        pass
    return numberStr

if __name__=='__main__':
    # print(big_num({'price':10,'age':5,'name':22}))
    print(checkio(3))