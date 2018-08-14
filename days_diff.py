#coding:utf8
def days_diff(date1, date2):
    """
        Find absolute diff in days between dates
    """
    import time

    start = '-'.join(str(x) for x in date1)
    end = '-'.join(str(x) for x in date2)

    return abs (int((time.mktime(time.strptime(start, '%Y-%m-%d')) - time.mktime(time.strptime(end, '%Y-%m-%d'))) // 60 // 60 // 24))

def days_diff_other(date1,date2):

    def getMonthDay(month,more):
        day = 0
        for x in range(1,month,1):
            if(x in [1,3,5,7,8,10,12]):
                day += 31
            elif(x in [4,6,9,11]):
                day += 30
            elif(x==2 and more==1):
                day += 29
            else:
                day += 28
        return day

    num1=date1[0]*365
    num2=date2[0]*365
    if(date1[0]%400==0 or (date1[0]%4==0 and date1[0]%100!=0)):
        num1+=getMonthDay(date1[1],1)+date1[2]
    else:
        num1+=getMonthDay(date1[1],0)+date1[2]

    if (date2[0] % 400 == 0 or (date2[0] % 4 == 0 and date2[0] % 100 != 0)):
        num2 += getMonthDay(date2[1], 1) + date2[2]
    else:
        num2 += getMonthDay(date2[1], 0) + date2[2]


    return abs(num2-num1)

def days_diff_others(date1,date2):

    def getMonthDay(month,more):
        day = 0
        for x in range(1,month,1):
            if(x in [1,3,5,7,8,10,12]):
                day += 31
            elif(x in [4,6,9,11]):
                day += 30
            elif(x==2 and more==1):
                day += 29
            else:
                day += 28
        return day

    num1=date1[0]*365
    num2=date2[0]*365
    if(date1[0]%400==0 or (date1[0]%4==0 and date1[0]%100!=0)):
        num1+=getMonthDay(date1[1],1)+date1[2]
    else:
        num1+=getMonthDay(date1[1],0)+date1[2]

    if (date2[0] % 400 == 0 or (date2[0] % 4 == 0 and date2[0] % 100 != 0)):
        num2 += getMonthDay(date2[1], 1) + date2[2]
    else:
        num2 += getMonthDay(date2[1], 0) + date2[2]


    resNum=0
    if date2[0]>date1[0]:
        minNum = date1[0]
        MaxNum = date2[0]
    else:
        minNum = date2[0]
        MaxNum = date1[0]

    for i in range(minNum,MaxNum,1):
        if (date1[0] % 400 == 0 or (date1[0] % 4 == 0 and date1[0] % 100 != 0)):
            resNum +=1

    return abs(num2-num1)+resNum

if __name__ == '__main__':
    # print days_diff((2014,1,1), (2014,8,27))
    # print days_diff_other((2014,1,1), (2014,8,27))
    # print days_diff_other((1, 1, 1), (9999, 12, 31)) #3652058
    print days_diff_others((2011, 1, 1), (2010, 12, 31)) #3652058
    # These "asserts" using only for self-checking and not necessary for auto-testing
    # assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
    # assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
    # assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238
