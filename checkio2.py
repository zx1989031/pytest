#coding:utf8
def checkio(data):
    if len(data):
        key=0
        res=[]
        for value in data:
            if key%2 ==0:res.append(value)

            key = key+1
        return sum(res)*data[-1]
    else:
        return 0

def checkio_other(array):
        return sum(array[::2]) * array[-1] if array else 0

def checkio_key(array):
    multiply = 1
    for val in array:
        multiply = multiply*val

    print multiply
    pass

#list 列乘积
def chekcio_num(array):
    print range(0,10,2)
    pass

if __name__=='__main__':
    data=[1,2,3,4,5]
    print (checkio(data))
    print (checkio_other(data))
    print (checkio_key(data))
    print (chekcio_num(data))
