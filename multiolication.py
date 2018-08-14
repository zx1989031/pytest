#coding:utf8
def checkio(number):
    strs = ''
    for i in str(number).replace('0','1'):
        strs  = strs+i+'*'

    return eval(strs+'1')
    # return eval(number.repleace(1,0))
def checkio1(number):
    result=1
    for i in str(number).replace('0', '1'):
        result *= int(i)

    return result

def checkio2(number):
    return eval('*'.join(str(number).replace('0','1')))

def checkio_other(number):
    result = 1
    for k in str(number):
        if int(k) != 0:
            result *= int(k)
    return result

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print checkio(1342340)
    print checkio1(1342340)
    print checkio2(1342340)
    print checkio_other(1342340)
    # assert checkio(123405) == 120
    # assert checkio(999) == 729
    # assert checkio(1000) == 1
    # assert checkio(1111) == 1
    # print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
