#coding:utf8
#/usr/bin/python
#fileName:pattern1.py
def best_stock(data):
    # your code here
    num = data.values()
    maxNum = max(num)
    for y in data:
        if (data[y] == maxNum):
            print  y

def best_stock_other(data):
    # print data.__getitem__('CAC')
    print max(data,key=data.__getitem__)

def bet_stock_other_lambda(data):
    g = lambda x:data[x]
    print max(data,key=lambda x:data[x])

if __name__ == '__main__':
    best_stock({'CAC':10,'ATX':20,'WIG':1.2})
    best_stock_other({'CAC':10,'ATX':20,'WIG':1.2})
    bet_stock_other_lambda({'CAC':10,'ATX':20,'WIG':1.2})
    # print("Example:")
    # print(best_stock({
    #     'CAC': 10.0,
    #     'ATX': 390.2,
    #     'WIG': 1.2
    # }))
    #
    # # These "asserts" are used for self-checking and not for an auto-testing
    # assert best_stock({
    #     'CAC': 10.0,
    #     'ATX': 390.2,
    #     'WIG': 1.2
    # }) == 'ATX', "First"
    # assert best_stock({
    #     'CAC': 91.1,
    #     'ATX': 1.01,
    #     'TASI': 120.9
    # }) == 'TASI', "Second"
    # print("Coding complete? Click 'Check' to earn cool rewards!")