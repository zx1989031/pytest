#coding:utf8
def checkio10(data):
    data.sort()

    if(len(data)%2 ==0):
        return (data[int(len(data)/2)]+data[int(len(data)/2)-1])/float(2)
    else:
        return data[int(len(data)/2)]

if __name__=='__main__':
    print checkio10([1 ,2,3,4,5,6])