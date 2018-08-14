#coding:utf8
def checkio(str_number,number):
    try:
        return int(str_number,number)
    except:
        return -1
    pass


if __name__=='__main__':
    print checkio('AB',10)
    # checkio("AF", 16) == 175 10*16+15
    # checkio("101", 2) == 5   1*(2*2)+0*(2)+1*(1)
    # checkio("101", 5) == 26  1*(5*5)+0*(2)+1(1)
    # checkio("Z", 36) == 35   35*(1)
    # checkio("AB", 10) == -1